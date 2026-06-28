import marimo

__generated_with = "0.23.9"
app = marimo.App()

with app.setup:
    import marimo as mo
    from utils.user_editor import UserEditor


@app.cell
def _():
    ue = UserEditor()
    return (ue,)


@app.cell
def _(ue):
    run_btn = ue.run_button
    return (run_btn,)


@app.cell
def _(run_btn, ue):
    mo.vstack([
        run_btn,
        ue.editor,
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


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Example Notebook

    This notebook demonstrates a few things `marimo-book` handles for you:

    - Hidden setup cells (the `import marimo as mo` above) don't appear
      in the rendered page.
    - `mo.md(...)` cells become native Markdown.
    - Code cells are shown with syntax highlighting and a copy button.
    - Cell outputs are baked in at build time — this page works without
      a Python kernel.
    - `mo.callout(...)` becomes a themed admonition.
    """)
    return


@app.cell
def _():
    # # Regular code cells run at build time; their output is embedded in the page.
    # import math

    # values = [math.sin(x / 10) for x in range(10)]
    # values
    return


@app.cell(hide_code=True)
def _():
    mo.callout(
        mo.md("**Hot reload works.** Try editing this cell while `marimo-book serve` is running."),
        kind="info",
    )
    return


if __name__ == "__main__":
    app.run()
