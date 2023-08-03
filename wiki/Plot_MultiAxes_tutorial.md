---
 TutorialInfo:
   Topic: Plot workbench
   Level: Intermediate
   Time: 
   Author: 
   FCVersion: 0.19
   Files: 
---

# Plot MultiAxes tutorial

 



Please complete the [basic tutorial](Plot_Basic_tutorial.md) before starting with this tutorial. In this tutorial we will learn how to create and edit a multiaxes plot. You can learn more about the [Plot Workbench here](Plot_Workbench.md).

 <img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;">  
*Multiaxes plot example*

In the image you can see the result that we will approximately obtain. Following this tutorial you will learn:

-   How to create a multiaxes Plot from the [Python console](Python_console.md).
-   How to edit axes properties.
-   How to control the grid and the legend when several axes sets are present.
-   How to edit the position of labels, titles and legends.

## Plotting data 

As we did in the [previous tutorial](Plot_Basic_tutorial.md) we will use the [Python console](Python_console.md) or [macros](Macros.md) to plot the data, but in this case we will plot the data using two axes sets.

### Creating plot data 

In this example we will plot 3 functions, the two used in the [previous tutorial](Plot_Basic_tutorial.md), and a new polynomial one. The range of the polynomial function is different from the other functions therefore new axes are required. The next commands will create the data arrays for us:

 
```python
import math
p = range(0,1001)
x = [2.0*xx/1000.0 for xx in p]
y = [xx**2.0 for xx in x]
t = [tt/1000.0 for tt in p]
s = [math.sin(math.pi*2.0*tt) for tt in t]
c = [math.cos(math.pi*2.0*tt) for tt in t]
```

As *x* moves from 0 to 2, the *y* function has a maximum value of 4, so if we try to plot this function with the trigonometrical ones, at least one function will be truncated or badly scaled, therefore we we need a multiaxes plot. A multiaxes plot in FreeCAD is intended to get a plot with multiple axes, not to get multiple plots in the same document.

### Drawing functions, adding new axes 

We will plot the trigonometrical functions using the main axes. If all your axes have the same size it is not relevant which function is plotted first. But if this is not the case the function that uses the biggest axes, in our case the polynomial function, should be plotted last. The legend will be attached to the last axes system and it is more convenient if this is the biggest. To plot the trigonometrical functions we only need to launch some commands.

 
```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.plot(t,s,r"$\sin\left( 2 \pi t \right)$")
Plot.plot(t,c,r"$\cos\left( 2 \pi t \right)$")
```

In this example we pass the series labels for the legend directly. Note that the label strings have the *r* prefix in order to prevent Python from trying to interpret special characters (the *\\* symbol is used frequently in [LaTeX](http://www.latex-project.org) syntax).

Before we can plot the polynomial function, we need to create new axes. In the [Plot Workbench](Plot_Workbench.md) new axes are automatically selected as the active ones, and new plots will be associated with these axes.

 
```python
Plot.addNewAxes()
Plot.plot(x,y,r"$x^2$")
```

As you can see your plot has gone crazy, with axes ticks overlapping, curves of the same color, etc. Now we need to use the [Plot Workbench](Plot_Workbench.md) to fix this graph.

## Configuring plot 

### Configuring axes 

The [Plot Workbench](Plot_Workbench.md) provides a tool to modify the properties of axes.

 ![](images/Plot_Axes.svg‎ )  
*Axes configuration tool icon*

With the [axes tool](Plot_Axes.md) you can add or remove axes, and set the active axes, which are then used if you plot more data.

To change the size of the first axes set, associated with the trigonometrical functions, it has to be activated first by changing the active axes from 1 to 0. We can then move the horizontal and vertical dimension sliders to reduce its size (try to emulate the example). We also need to change the alignment of the axes: select top and right respectively.

### Configuring series 

Set the series properties as we did in the [previous tutorial](Plot_Basic_tutorial.md).

### Showing grid and legend 

The [grid](Plot_Grid.md) and [legend](Plot_Legend.md) can be shown, and hidden, with the tools already described in the [previous tutorial](Plot_Basic_tutorial.md), but in this case the behavior is a little different because there are two axes sets.

Grid lines are added to the active axes set. To add lines to the second axes set in our example, it has to be activated first by changing the active axes from 0 to 1 in the [axes tool](Plot_Axes.md).

As already mentioned the legend will be positioned relative last axes set. If you show the legend now you will see that it is really badly placed, but we will fix that later.

### Setting axes labels 

When it comes to setting the axes [labels](Plot_Labels.md) we again have to deal with our two axes sets. But since labels are usually set for all axes, the procedure is the same as described in the [previous tutorial](Plot_Basic_tutorial.md). The [Plot Workbench](Plot_Workbench.md) allows you to set a title per axes set. In this case we only want to set a title for the last, the biggest, axes set.

**Axes 0:**

-   X Label = \$t\$
-   Y Label = \$\\mathrm{f} \\left( t \\right)\$

**Axes 1:**

-   Title = Multiaxes example
-   X Label = \$x\$
-   Y Label = \$\\mathrm{f} \\left( x \\right)\$

Change the font size of all labels to 20, and the font size of the title to 24. Again there is an element, the title, that is badly placed.

### Setting elements position 

The [Plot Workbench](Plot_Workbench.md) provides a tool to change the position of several plot elements, such as as titles, labels and legends.

 ![](images/Plot_Positions.svg )  
*Position editor icon*

When you run the tool you will see a list of all editable elements. Titles and legends can be moved in both directions, but axis labels can only be moved along the axis they belong to. Select the title of axes 1 and move it to (0.24,1.01), then select the legend and move it to a better position. You can increase the font size of the legend labels as well.

## Saving plot 

Now you can save your work. See the [previous tutorial](Plot_Basic_tutorial.md) if you don\'t remember how to do it.

 {{Plot_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > [Plot](Plot_Workbench.md) > Plot MultiAxes tutorial
