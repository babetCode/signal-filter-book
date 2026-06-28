import marimo

__generated_with = "0.23.9"
app = marimo.App()

with app.setup:
    import marimo as mo
    import io
    from contextlib import redirect_stdout


@app.class_definition
class UserEditor:
    """
    Lets the user write code and run it.
    Example use:
    **Cell 1**
    ``ue_example = UserEditor()
    run_example = ue.run_button``
    **Cell 2**
    ``_ = run_example
    ue_example.display()``
    """
    def __init__(self, code="print('hello')"):
        self.editor = mo.ui.code_editor(value=code)
        self.run_button = mo.ui.run_button(label="run")

    def run(self, sandbox_globals={}):
        buf = io.StringIO()
        sandbox_locals={}
        try:
            with redirect_stdout(buf):
                exec(self.editor.value, sandbox_globals, sandbox_locals)
            output = buf.getvalue()
        except Exception as e:
            output = e
        return output, sandbox_locals


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Example Use
    """)
    return


@app.cell
def _():
    ue = UserEditor()
    return (ue,)


@app.cell
def _(ue):
    run_btn = ue.run_button
    ui_editor = ue.editor
    return run_btn, ui_editor


@app.cell
def _(run_btn, ui_editor):
    mo.vstack([
        run_btn,
        ui_editor,
    ])
    return


@app.cell
def _(run_btn, ue):
    mo.stop(not run_btn.value, "Click run")

    console_out, sandbox_locals = ue.run()
    mo.vstack([
        console_out,
        mo.md("---"),
        sandbox_locals
    ])
    return


if __name__ == "__main__":
    app.run()
