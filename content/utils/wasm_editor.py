import marimo

__generated_with = "0.23.9"
app = marimo.App()

with app.setup:
    import marimo as mo
    import io
    from contextlib import redirect_stdout


@app.class_definition
class UserEditor:
    def __init__(self, code="print('hello')", on_click=None):
        self.editor = mo.ui.code_editor(value=code)
        # Use a regular button with a click handler instead of a run_button
        self.run_button = mo.ui.button(label="run", on_click=on_click)

    def run(self, sandbox_globals={}):
        buf = io.StringIO()
        sandbox_locals = {}
        try:
            with redirect_stdout(buf):
                exec(self.editor.value, sandbox_globals, sandbox_locals)
            output = buf.getvalue()
        except Exception as e:
            output = str(e)
        return output, sandbox_locals


if __name__ == "__main__":
    app.run()
