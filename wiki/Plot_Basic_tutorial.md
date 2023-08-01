---
- TutorialInfo:   Topic:Plot Workbench Basic Tutorial
   Level:Beginner
   Time:
   Author:
   FCVersion:0.19
   Files:
---

# Plot Basic tutorial

 



In this tutorial we will learn how to create a basic plot using the [Plot Workbench](Plot_Workbench.md) and the [Python console](Python_console.md).

 <img alt="" src=images/Plot_Trigonometric_Example.png  style="width:600px;">  
*Basic plot example*

In the image you can see the result that we will approximately obtain. Following this tutorial you will learn:

-   How to create a Plot from the [Python console](Python_console.md).
-   How to plot some data from the [Python console](Python_console.md).
-   How to show the <img alt="" src=images/Plot_Grid.svg  style="width:24px;"> [grid lines](Plot_Grid.md).
-   How to show the <img alt="" src=images/Plot_Legend.svg  style="width:24px;"> [legend](Plot_Legend.md).
-   How to edit <img alt="" src=images/Plot_Series.svg  style="width:24px;"> [series labels](Plot_Series.md), introducing text in [LaTeX](http://www.latex-project.org).
-   How to edit <img alt="" src=images/Plot_Labels.svg  style="width:24px;"> [axes labels](Plot_Labels.md), introducing text in [LaTeX](http://www.latex-project.org).
-   How to edit series styles.
-   How to save your plot.

## Plotting data 

To plot data you don\'t need a FreeCAD document, simply open the [Python console](Python_console.md) and start sending commands, or use [macros](Macros.md).

### Creating plot document 

Plots are special documents that can be created manually in order to add data later, or the workbench can create one automatically when you start plotting data. Creating your own plot document has two advantages:

-   You can set the document window label.
-   You can control the document where you plot your data.

To create a new plot document simply launch the following commands:

 
```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.figure("TrigonometricTest")
```

In FreeCAD version 0.19 it is required to install the <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Plot Workbench](Plot_Workbench.md) with the [Add-on manager](Std_AddonMgr.md), while from FreeCAD version 0.20 onward the external add-on is no longer required to perform plots. The commands above will create a new tab in the [Main view area](Main_view_area.md) called **TrigonometricTest**. The newly created document already has a set of axes. Each plot document has at least one set of axes.

### Drawing functions 

You can also start working from here because, as already explained, the plot command will create a new document if required. The next thing we need to do is create the data for the sine and cosine functions that we want to plot:

 
```python
import math
t = range(0,101)
t = [tt/100.0 for tt in t]
s = [math.sin(2.0*math.pi*tt) for tt in t]
c = [math.cos(2.0*math.pi*tt) for tt in t]
```

That will create 3 arrays of data (with 101 points):

-   *t* = Time in seconds.
-   *s* = Sine function.
-   *c* = Cosine function.

In order to plot both functions we only need to launch the next commands:

 
```python
Plot.plot(t,s)
Plot.plot(t,c)
```

The **plot** command allows the series label as an argument, but since we will edit it later using the Plot workbench tools, we don\'t pass this data yet.

## Configuring plot 

### Showing grid and legend 

Change the FreeCAD workbench to the [Plot Workbench](Plot_Workbench.md) with **View → Workbench → Plot** (you must install the add-on first with the [Add-on manager](Std_AddonMgr.md)). When the workbench has been loaded, use the [grid tool](Plot_Grid.md) to show the grid.

 ![](images/Plot_Grid.svg‎ )  
*Show/hide grid tool icon*

You can repeat the action to hide the grid. Use the [legend tool](Plot_Legend.md) to show, or hide, the legend.

 ![](images/Plot_Legend.svg )  
*Show/hide legend tool icon*

As you can see, the legend is very small and empty because we have not set any series label yet. In the [Plot Workbench](Plot_Workbench.md) series without a label are not displayed in the legend.

### Setting series label 

With the [series tool](Plot_Series.md) you can edit the parameters of each series.

 ![](images/Plot_Series.svg‎ )  
*Series configuration tool icon*

Select the series you want to edit, we will start with the first one. Uncheck **No label** and set this label:

 
```python
$y = \sin \left( 2 \pi t \right)$
```

Since [matplotlib](http://matplotlib.org/) supports [LaTeX](http://www.latex-project.org) you can set all labels and titles using LaTeX. Set the following label for the second series:

 
```python
$y = \cos \left( 2 \pi t \right)$
```

### Setting series style 

You can set many series properties. Try to set the properties shown in the example image, changing the colors and drawing style of the second series.

### Setting axes labels 

With the [labels tool](Plot_Labels.md) you can set the title and the labels for the axes.

 ![](images/Plot_Labels.svg‎ )  
*Labels tool icon*

Set this data:

-   Title = Trigonometric functions example
-   X Label = \$t\$
-   Y Label = \$y = \\mathrm{f} \\left( t \\right)\$

Also change the font size of the title and all labels to 20.

## Saving plot 

With the [save tool](Plot_Save.md) you can save your plot as an image file in several formats.

 ![](images/Plot_Save.svg )  
*Save tool icon*

First select the path and filename for the output file.

Set the output image size in inches, for example use 11.7x8.3 to get a **DIN A4** size. DPI (Dots per inch) will control the image resolution, for example use 100 dpi. In combination with the given dimensions this will result in an image of 1170x830 pixels.

 {{Plot_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > [Plot](Plot_Workbench.md) > Plot Basic tutorial
