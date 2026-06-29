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
    Sensors—and measurement tools in general—are imperfect. It is imposible to measure anything with 100% precision. However, by combining multiple measurements with knowlege about the things being measured, it is possible to make better estimates. That is what signal filters do.

    Humans generally have intuition on handling imperfect data: when making hard decisions, they consult multiple people (social measurements) and decide based on a combination of the input recieved and their understanding of the situation. Moreover, most understand that getting the input of more people can lead to better understanding even if no single person's input is 100% perfect.

    Signal filters do this same process, but instead estimating the best decision to make using social measurements, filters take a variety of measurements and use them to estimate any unknown state in a given system. For example, when traveling on a road (a system), a filter might be used to estimate location (a state), using imprecise GPS data (measurements). The crucial point—both here and with social decision making—is that having more measurements allows us to achieve better estimates *even if none of the measurements are 100% correct*.

    ## Basic example: averaging
    Since the core principle is that more measurements means better estimates, we want to find a way to combine a group of measurements. The simplest way to do this is just taking the average. This is not great for a constantly changing state (like traveling on a road), but is better for a static system like when weighing an object.

    Consider weighing yourself on an accurate but imprecise scale where one moment it says you are heavier and the next it says you are lighter. By taking the average of your measurements over time, you can smooth out the inconsistency and make a more reasonable estimate. For example if your first measurement was \(79\)kg and your second measurement was \(81\)kg, you would estimate your weight as \((79+81)/2=80\)kg. Then if your third measurement was \(77\)kg, your new estimate would be \((79+81+77)/3=79\)kg. After a few measurements we might have something like

    \[(79+81+77+76+80+79)/6=78.67.\]

    The longer we continued to do this, the better we would expect our estimate to get. However, the analog-to-digital converter on a normal bathroom scale samples the weight signal between 10 and 80 times per second, meaning we will quickly have a very long set of measurements to average.

    To avoid storing such a long list of measurements (usually called \(z_1\), \(z_2\), etc...) we can take a clever approach by storing only the number of measurements (called \(k\)) and the past average (called \(x\)). To see why this is sufficient, note that the average after \(k\) measurements is calculated as

    \[\frac{z_1 + z_2 + \cdot\cdot\cdot + z_k}{k},\]

    and the next is

    \[\frac{z_1 + z_2 + \cdot\cdot\cdot + z_k + z_{k+1}}{k+1},\]

    which can be rewritten as

    \[\frac{z_1 + z_2 + \cdot\cdot\cdot + z_k}{k+1} + \frac{z_{k+1}}{k+1} = \frac{k}{k+1}\left(\frac{z_1 + z_2 + \cdot\cdot\cdot + z_k}{k}\right) + \frac{z_{k+1}}{k+1}.\]

    Programatically, this can be implemented as:

    ```py
    def recursive_avg(z, x, k):
        new_x = (x * (k-1) + z)/k
        return new_x
    ```

    Note that we have used \(k-1\) and \(k\) this time instead of \(k\) and \(k+1\) in order to match the subscript to the incoming measurement \(z\) rather than the previous one. Despite this subscript notation, the functionality is exactly the same.

    ## Weighted average
    """)
    return


@app.cell(hide_code=True)
def _():
    slider = mo.ui.slider(0,10,1,0)
    slider
    return (slider,)


@app.cell(hide_code=True)
def _(slider):
    slider.value
    return


@app.cell(disabled=True, hide_code=True)
def _():
    # Generate avg latex

    _n = 6
    _measurements = [79, 81, 77]
    _measurements += np.round(
        3 * np.random.randn(_n - 3) + 80
    ).astype(int).tolist()
    _text = rf"\[({r'+'.join([str(z) for z in _measurements])})/{_n}={np.average(_measurements):.2f}.\]"
    return


if __name__ == "__main__":
    app.run()
