import marimo

__generated_with = "0.23.11"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import altair as alt
    import polars as pl
    import numpy as np


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    This is a cached notebook.
    """)
    return


if __name__ == "__main__":
    app.run()
