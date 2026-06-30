import marimo

__generated_with = "0.23.11"
app = marimo.App()

with app.setup:
    import marimo as mo
    import altair as alt
    import polars as pl
    import numpy as np


@app.cell(hide_code=True)
def _():
    mo.md("""
    This is a static notebook page (the default). All code cells are shown for example purposes. Because it is static, it will not display ui elements like
    """)
    return


@app.cell
def _():
    mo.ui.dropdown([1, 2, 3, 4])
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    or
    """)
    return


@app.cell
def _():
    mo.ui.slider(1,9,1)
    return


@app.cell(hide_code=True)
def _():
    mo.md("""
    or even make a chart like
    """)
    return


@app.cell
def _():
    # Create dummy dataset
    np.random.seed(42)
    df = pl.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], size=100)
    })

    # Build standard Altair chart
    chart = alt.Chart(df).mark_circle(size=60).encode(
        x='x:Q', 
        y='y:Q',
        color='category:N'
    ).properties(
        width=500, 
        height=350,
        title="Static Plot (Non-reactive)"
    )

    chart
    return


if __name__ == "__main__":
    app.run()
