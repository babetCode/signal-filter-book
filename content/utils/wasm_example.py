import marimo

__generated_with = "0.23.11"
app = marimo.App()

with app.setup:
    import marimo as mo


@app.cell
def _():
    slider = mo.ui.slider(0,9,1)
    slider
    return (slider,)


@app.cell
def _(slider):
    "🤖"*slider.value
    return


if __name__ == "__main__":
    app.run()
