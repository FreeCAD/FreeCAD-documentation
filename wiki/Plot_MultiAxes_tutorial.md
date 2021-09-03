 


{{TutorialInfo
|Topic=Plot workbench
|Level=Intermediate
|Time=
|Author=
|FCVersion=
|Files=
}}

Ensure to visit [basic tutorial](Plot_Basic_tutorial.md) before starting with this tutorial. In this tutorial we will learn how to create and edit a multiaxes plot. You can learn more about [Plot module here](Plot_Module.md).

 <img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;">  
*Multiaxes plot example*

In previous image you can see the result that we aproximately will obtain. Following this tutorial you will learn:

-   How to create a multiaxes Plot from Python Console.
-   How to edit axes properties.
-   How to control grid/legend when several axes is present.
-   How to edit labels, titles and legend positions.

## Plotting data 

As we did in [previous tutorial](Plot_Basic_tutorial.md) we will use the Python console or [macros](Macros.md) in order to plot the data, with the difference that in this case we will plot the data in two different axes.

### Creating plot data 

In this example we will plot 3 functions, the two ones used in [previous tutorial](Plot_Basic_tutorial.md), and another polynomial one. The fact is that the polynomial one will need new axes due to the variation range is different from all others. Next commands will create data arrays for us:

 
```python
import math
p = range(0,1001)
x = [2.0*xx/1000.0 for xx in p]
y = [xx**2.0 for xx in x]
t = [tt/1000.0 for tt in p]
s = [math.sin(math.pi*2.0*tt) for tt in t]
c = [math.cos(math.pi*2.0*tt) for tt in t]
```

As *x* moves from 0 to 2, *y* function has a maximum value of 4, so if we try to plot this function with trigonometrical ones, at least one function will be truncated or bad scaled, then we need a multiaxes plot. Multiaxes plot in FreeCAD is oriented to get a plot with multiple axes, not to get multiple plots in same document.

### Drawing functions, adding new axes 

We will draw polynomial function at main axes. If all your axes will have same size then is not relevant what function is ploted in what axes, but if your plot has axes with other size (as in this example), main axes must be the biggest one (because this axes have the white background). In order to do it we only need to launch a command.

 
```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot
Plot.plot(x,y,r"$x^2$")
```

In this example we pass directly the series label for the legend. Note that the label string has the *r* prefix in order to avoid Python try to interpret special characters (*\\* symbol is used frecuently in [LaTeX](http://www.latex-project.org) syntax).

Now we can plot trigonometrical functions, creating new axes before. In [FreeCAD Plot module](Plot_Module.md) when you create new axes this axes are selected as active ones, so new plots will be associated to this axes.

 
```python
Plot.addNewAxes()
Plot.plot(t,s,r"$\sin\left( 2 \pi t \right)$")
Plot.plot(t,c,r"$\cos\left( 2 \pi t \right)$")
```

As you can see you plot has gone crazy, with axes ticks overlaped, curves of same color, etc. Now we needs to use [FreeCAD Plot module](Plot_Module.md) to fix this graph.

## Configuring plot 

### Configuring axes 

[FreeCAD Plot module](Plot_Module.md) provides a tool in order to modify the properties of each axes.

 ![](images/Plot_Axes.svg‎ )  *Axes configuration tool icon*

The first thing that you can find in axes tool is the active axes selector. Since the active axes are the last one, active axes is placed at one. The axes tool, as labels tool, allows to set the active axes, allowing you to plot more data in the axes that you want (including add/remove axes). For the moment we will work over the selected axes, that are the associated to trigonometrical functions.

In the dimensions sliders, we will move left horizontal and bottom vertical sliders (try to emulate example) in order to reduce axes size. Then we can set the axes alignement, changing it to top and right, and setting and small offset of two units.

### Configuring series 

Set series properties as we did in [previous tutorial](Plot_Basic_tutorial.md).

### Showing grid and legend 

Grid and legend is shown and hide with the same tools that used in [previous tutorial](Plot_Basic_tutorial.md), but in this case the behaviour is a little bit different due to the presence of two different axes.

Regarding grid lines, you can show lines for each axes set, for example, if you try to show grid now you will show only the grid of the trigonometrical functions, so in order to show the grid of polynomial function plot you needs to change active axes to 0 (using axes configuration tool) before using grid tool another time (Is possible that you need to press two times the tool).

Regarding legend, the legend will be the same for both axes, so you can choose the axes that you want in order to show the legend, but is strongly recommended to use the biggest ones (0 in this example) because position will be refered to this axes coordinates. If you show the legend you can see that is really bad placed, we will fix this problem later.

### Setting axes labels 

You can set axes labels with same tool used in [previous tutorial](Plot_Basic_tutorial.md), with the difference that now you have more axes. Since axes labels is ussually set as one per axis, is not a significant difference, but [FreeCAD Plot module](Plot_Module.md) allow you to set a title by axes too. In this case we only wants to set title to main axes, so set:

**Axes 0:**

-   Title = Multiaxes example
-   X Label = \$x\$
-   Y Label = \$\\mathrm{f} \\left( x \\right)\$

**Axes 1:**

-   X Label = \$t\$
-   Y Label = \$\\mathrm{f} \\left( t \\right)\$

Set also 20 to fontsize for all but title, that uses a fontsize of 24. As happens with legend, title is bad placed, interseting with second axes set, so we need to solve both problems.

### Setting elements position 

[FreeCAD Plot module](Plot_Module.md) provides a tool in order to set the position of several plot elements, as titles, labels or legend.

 ![](images/Plot_Positions.svg )  *Position editor icon*

When you run the tool you see a list with all the editable elements. Title elements, as well as legend, can be moved in both directions, since axes labels can be moved only on the axes direction. Select title of axes 0 and move it to (0.24,1.01), then select legend and move it to a better position. You can increase legend labels fontsize too.

## Saving plot 

Now you can save your work. See [previous tutorial](Plot_Basic_tutorial.md) if you don\'t remember how to do it.

 {{Tutorials_navi}} {{Plot_Tools_navi}} 

[Category:External\_Workbenches{{\#translation:}}](Category:External_Workbenches.md) [Category:Addons{{\#translation:}}](Category:Addons.md)
