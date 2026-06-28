import marimo

__generated_with = "0.23.11"
app = marimo.App(width="medium")

with app.setup(hide_code=True):
    import marimo as mo
    import numpy as np


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## What are signal filters?
    Sensors—and measurement tools in general—are imperfect. It is imposible to measure anything with 100% accuracy. However, by combining multiple measurements with knowlege about the things being measured, it is possible to make better estimates. That is what signal filters do.

    ### Intuitive understanding
    Humans generally have intuition on handling imperfect data: when making hard decisions, they consult multiple people (social measurements) and decide based on a combination of the input recieved and their understanding of the situation. Moreover, most understand that gettin the input of more people can lead to better understanding even if no single person's input is 100% perfect.

    Signal filters do this same process, but instead estimating the best decision to make using social measurements, filters take a variety of measurements and use them to estimate any unknown state in a given system. For example, when traveling on a road (a system), a filter might be used to estimate location (a state), using imprecise GPS data (measurements). The crucial point—both here and with social decision making—is that having more measurements allows us to achieve better estimates *even if none of the measurements are 100% correct*.

    ### Basic example: averaging
    Since the core principle is that more measurements means better estimates, we want to find a way to combine a group of measurements. The simplest way to do this is just taking the average. This is not great for a constantly changing state (like traveling on a road), but is better for a static system like when weighing an object.

    Consider weighing yourself on an accurate but imprecise scale where one moment it says you are heavier and the next it says you are lighter. By taking the average of your measurements over time, you can smooth out the inconsistency and make a more reasonable estimate. For example if your first measurement was \(79\)kg and your second measurement was \(81\)kg, you would estimate your weight as \((79+81)/2=80\)kg. Then if your third measurement was \(77\)kg, your new estimate would be \((79+81+77)/3=79\)kg. After a few measurements we might have something like
    """)
    return


@app.cell(hide_code=True)
def _():
    _n = 6
    _measurements = [79, 81, 77]
    _measurements += np.round(
        3 * np.random.randn(_n - 3) + 80
    ).astype(int).tolist()

    mo.md(
        rf"\[({r'+'.join([str(z) for z in _measurements])})/{_n}={np.average(_measurements):.2f}.\]"
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    The longer we continued to do this, the better we would expect our estimate to get.
    """)
    return


if __name__ == "__main__":
    app.run()
