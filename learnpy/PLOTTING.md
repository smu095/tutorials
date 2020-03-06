# Matplotlib
What follows is a summary of the [Matplotlib Usage Guide](https://matplotlib.org/tutorials/introductory/usage.html). Note that not all the material has been summarised, only those of greatest interest and use to me.

* Everything in Matplotlib is organised in a hierarchy.
* At the top of the hierarchy is `matplotlib.pyplot`.
* `matplotlib.pyplot` is a collection of command style functions that make Matplotlib work like MATLAB, which expects `np.array` or `np.ma.masked_array` as inputs.
* At this level, simple functions are used make some change to a figure (e.g. create a figure, create plotting area, creates lines, etc.).
* Various states are preserved across function calls, allowing Matplotlib to keep track of changes.
* The next level down is the first level of the object-oriented interface. 
* Here, the user use pyplot to create figures, and through those figurs one or more axes objects can be created. These are then used for most plotting actions.

## Anatomy of a figure
![](https://matplotlib.org/_images/anatomy.png)

* A **figure** keeps track of all the child `Axes`, titles, figure legends, etc., and the **canvas** which is the object that does the drawing (usually invisible to the user).
* A figure can have any number of `Axes`.

```python
# Create an empty figure with no axes
fig = plt.figure()

# Add a title
fig.suptitle('No axes on this figure')
```
![](https://matplotlib.org/_images/sphx_glr_usage_001.png)

```python
# A figure with a 2x2 grid of Axes
fig, ax_lst = plt.subplots(2, 2)
```
![](https://matplotlib.org/_images/sphx_glr_usage_002.png)

* The **Axes** can be thought of as 'a plot', it is the region of the image with the data space.
* The Figure is the final image that may contain one or more Axes.
* A given `Axes` object can only be in one figure.
* The Axes represent an individual plot (don't confuse this with the word "axis", which refers to the x/y axis of a plot).
* Each `Axes` object has a title, and x-label and a y-label.
* The `Axes` object contains `Axis` objects (two in the case of 2D-plots, three in the case of 3D-plots).
* `Axis` objects are number-line-like objects, and take care of setting the graph limits.
* The location of the ticks is determined by a `Locator` object, and the tick label strings are formatted by a `Formatter`.
* Almost everything ypu see is an `Artist` object. When a figure is rendered, all Artists are drawn to a canvas.
* Most Artists are tied to an Axes and cannot be shared by multiple Axes.

## Pyplot
* Pyplot provides the interface to the underlying object-oriented plotting library.

```python
x = np.linspace(0, 2, 100)

# First call to plt.plot automatically create the necessary figure and axes to achieve the desired plot
plt.plot(x, x, label='linear')

# Subsequent calls re-use the current axes and each add another line
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

# Setting the title, legend, and axis labels also automatically use the current axes
plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
```

![](https://matplotlib.org/_images/sphx_glr_usage_003.png)

## Coding styles
* There are **two officially supported coding styles**: the "simpler" pyplot interface and the "wordier" object-oriented style.
* **Pyplot:** Also known as a state-based interface. This is encapsulated in the pyplot module.
* **Object-oriented:** Utilize an instance of axes.Axes in order to render visualizations on an instance of figure.Figure.
* As figures get increasingly complex, the latter can help make the code easier extend and maintain.

```python
x = np.arange(0, 10, 0.2)
y = np.sin(x)

# Pyplot
plt.plot(x, y)
plt.show()

# Object-oriented
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```
# Introduction to Pyplot
## The `plot()` method
* `plot()` is a versatile method that can take an arbitrary number of arguments.
* For every x, y pair of arguments, an optional third argument can be set to control the color and line type of plot (by concatenating a color string with a line string).

```python
# Note that lists are converted to numpy arrays internally
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

![](https://matplotlib.org/_images/sphx_glr_pyplot_003.png)

* Sometimes your data will be in a format that allows you to access a particular variable with a string. The `data` keyword in `plot()` allows you to access these variables using the same string keys.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
```

![](https://matplotlib.org/_images/sphx_glr_pyplot_005.png)

* Line properties, such as linewidth, dash style, etc., can be controlled using keyword arguments to `plot()`. See the official tutorial for [available line properties](https://matplotlib.org/tutorials/introductory/pyplot.html#controlling-line-properties).

## Plotting categorical variables
* The following example shows two approaches to plotting categorical variables.

```python
# Declaring variables
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# Pyplot
plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

# Object-oriented
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9,3))

ax1.bar(names, values)
ax2.scatter(names, values)
ax3.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```

![](https://matplotlib.org/_images/sphx_glr_pyplot_006.png)

## Working with multiple figures/axes
* Multiple figures can be created using multiple calls to `plt.figure()` with an increasing figure number.
    * By default, calling the `plot()` method will create a figure. Alternatively, `plt.figure(1)` can be called explicitly to generate the first figure. Calling `plt.figure(2)` will generate the *second* figure.
* Figures and Axes can be cleared using the `clf()` and `cla()` methods, respectively.
* Note that the memory required for generating a figure is not completely released until `close()` is called.

## Working with text
* The `text()` method can be used to add text at an arbitrary location.
* Mathematical expressions can be added by writing a TeX expression surrounded by dollar signs. Note that in these cases the string must be preceded by an `r` to signify that it is a raw string, i.e. not to treat backslashes as escape characters.
* The `annotate()` method allows us to annotate specific (x, y) points with text.

## Logarithmic and other non-linear axes
* Changing the scale of an axis can be done by calling the `xscale()` or `yscale()` method and passing the appropriate string argument.
