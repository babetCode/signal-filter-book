import inspect
from hypothesis import find, strategies as st, settings, Phase
from hypothesis.errors import NoSuchExample

def is_equivalent(func1, func2) -> bool:
    """
    Uses hypothesis to test function equivalence.
    If functions are equivalent, returns True.
    """

    FAST_SETTINGS = settings(
        max_examples=100,       # Hypothesis default (thorough enough for ~100% confidence)
        database=None,          # CRITICAL: Prevents slow SQLite disk writes in Marimo
        phases=[Phase.generate, Phase.shrink]  # Skip explicit reuse phases to save time
    )
    
    # 2. Match parameter lengths instantly to avoid slow engine startups
    sig1 = inspect.signature(func1)
    sig2 = inspect.signature(func2)
    if len(sig1.parameters) != len(sig2.parameters):
        return False

    # 3. Dynamically build strict strategies using type hints
    argument_strategies = []
    for param in sig1.parameters.values():
        hint = param.annotation

        # Fallback to integer if the student didn't type-hint
        if hint == inspect.Parameter.empty:
            hint = int

        # st.from_type natively handles int, float, str, bool, List[int], etc.
        # We filter out infinite/NaN floats as they ruin simple == assertions
        if hint is float:
            strategy = st.floats(allow_nan=False, allow_infinity=False)
        else:
            strategy = st.from_type(hint)

        argument_strategies.append(strategy)

    # 4. Define the falsification condition
    def is_different(args):
        try:
            return func1(*args) != func2(*args)
        except Exception:
            # If the student's code crashes on a valid input, it's an error
            return True

    # 5. Execute using find() wrapped in our fast settings profile
    try:
        find(
            st.tuples(*argument_strategies), 
            is_different, 
            settings=FAST_SETTINGS
        )
        return False  # Counterexample found! Functions are NOT equivalent.
    except NoSuchExample:
        return True