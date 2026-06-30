import marimo

__generated_with = "0.23.11"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The g-h filter (aka alpha-beta filter) is a simple signal filter.

    The filter uses a prediction (\(x'\)) and a measurement (\(z\)) to estimate a state (\(x\)). The gain (\(g\)) determines whether the measurement or the estimate is weighted more heavily:

    \[\text{estimate(}x\text{)} = \text{prediction(}x'\text{)} + \text{gain(}g\text{)} \cdot (\text{measurement(}z\text{)} - \text{prediction(}x'\text{)}).\]

    The difference \((\text{measurement}-\text{prediction})\) is called the residual (\(y\)), giving

    \[x = x' + g \cdot y.\]

    ---

    The implementation is as follows:

    **Initialization**
    1. Initialize the state of the filter
    2. Initialize our belief in the state

    **Predict**
    1. Use system behavior to predict state at the next time step
    2. Adjust belief to account for the uncertainty in prediction

    **Update**
    1. Get a measurement and associated belief about its accuracy
    2. Compute residual between estimated state and measurement
    3. New estimate is somewhere on the residual line
    """)
    return


if __name__ == "__main__":
    app.run()
