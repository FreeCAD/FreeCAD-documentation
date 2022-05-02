---
- TutorialInfo:/ru
   Topic:Ship Workbench
   Level:Beginner
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial/ru





## Introduction

In this tutorial we will work with Series 60 ship, from the Iowa University. The tutorial is aimed to show how to work with a symmetric monohull ship, however multihull or non-symmetric ships can be performed with the same proceeding.

Learn more about <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> [Ship Workbench](Ship_Workbench.md).

## Loading geometry 

### Background

The <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> [Ship Workbench](Ship_Workbench.md) works over **Ship entities**, that must be created on top of provided geometry. Geometry must be a solid (or set of solids), the following criteria must be taken into account:

-   All hull geometry must be provided (including symmetric bodies).
-   Starboard geometry must be included at negatives *y* domain.
-   Origin (0,0,0) point is the **Midship section** (Midpoint between after and forward perpendicular) and **base line** intersection.

![Schematic view of sign criteria](images/FreeCAD-Ship-SignCriteria.jpg )


<center>

FreeCAD-Ship sign criteria


</center>

### Loading Series 60 geometry 

In order to help new users the Ship workbench includes a geometries example loader, with the following to choose from:

-   Series 60 from Iowa University
-   Wigley Canonical Ship
-   Series 60 Catamaran
-   Wigley Catamaran

![Example ship geometries loader icon.](images/Ship_Load.svg )


<center>

 Ship Geometries Examples loader icon


</center>

Executing the tool (Ship design/Load an example ship geometry) a task dialogue will shown. Select **Series 60 from Iowa University** and press Accept. Tool loads new document with **s60\_IowaUniversity** geometry.


**'''Warning, before editing anything!'''
You are now working with the original example file.
To preserve the original unedited example, '''you must first save it as a new file before editing anything.'''**

## Create ship instance 

In order to create a **Ship instance** select s60 geometry and execute the **ship creation tool** (Ship design/Create a new ship).

![Ship creation tool.](images/Ship_Logo.svg )


<center>

Ship creation tool icon


</center>

Creating a Ship task dialogue and some annotations in the [3D view](3D_view.md) will be shown. The annotations will disappear when you close the Ship creation tool, so don\'t worry about this.

Most relevant ship data must be introduced (the <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> Ship workbench uses a progressive data introduction system, so basic operations can be performed knowing only basic ship data, more information is needed as the operations become more complex).

### Ship data 

Main dimensions must be introduced here:

-   Length: Length between perpendiculars, 25.5 m for this ship.
-   Beam: Total ship beam, 3.389 m for this ship.
-   Draft: Design draft, 1.0 m for this ship.

![Front view annotations](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Length annotations.


</center>

Usually the Length between perpendiculars depends on design draft, so if you don\'t know what is the length of your ship you can set draft, and fit length in order to get bow and draft intersection.

![Side view annotations](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Beam annotations.


</center>

Same process is valid for Beam fit. Note that requested value is total beam, but annotation is only refered to starboard half ship.

When you press the **Accept** button, a new Ship instance is created called **Ship** in the *Tags & Attributes* dialog. We don\'t need geometry anymore, so you can hide it.

![Ship instance icon](images/FreeCAD-Ship-ShipInstance.png )


<center>

Ship instance icon.


</center>

From here onward, you must have **Ship** selected before you execute any of the Ship Workbench tools.

## Lines drawing 

The Ship workbench provides a tool that makes it easy to obtain a Lines Plan from the ship lines drawing

![Outline draw tool.](images/Ship_OutlineDraw.svg )


<center>

Lines drawing tool icon


</center>

Lines drawing is a set of lines from section cuts in all 3 axis, that will eventually show the hull geometry in a Lines Plan. We need to provide the lines for the 3 following views:

-   Body Plan (using the Transversal Cuts)
-   Sheer Plan (using the Longitudinals Cuts)
-   Half-Breadth Plan (using the Waterlines Cuts)

### Transversal cuts 

Usually 21 transversal equidistant sections between perpendiculars must be performed. in order to do it FreeCAD provides an automatic tool in order to do it, simply select **Transversal** type of sections, go to **Auto create** box and set **21** sections, then press **Create sections**

![Outline draw transversal sections preview.](images/S60OutlineTransversal.png )


<center>

Outline draw transversal sections preview


</center>

Sections table is filled and sections preview called **OutlineDraw** is shown. Usually more sections are added at bow and stern, where more complex curvatures are registered, to do this:

1.  Go to the end of the table and *double click* on an empty item in order to edit it.
2.  Press **intro** to confirm.
3.  Add the following sections:

:   

    :   X~22~ = -12.1125 m
    :   X~23~ = 12.1125 m

Depending hull geometry complexity, sections preview can take some time. In order to remove a section, just fill it with an empty text and press enter.

### Longitudinal cuts 

Two longitudinal cuts must be added, so select **Longitudinal** type of sections, go to **Auto create** box and set **2** sections, then press **Create sections**. Sections table is filled, and sections preview updated.

### Waterlines

6 Waterlines between base line and design draft must be added, so select **Waterlines** type of sections, go to **Auto create** box and set **5** (Z = 0 m will not be considered, add it manually if you need it) sections, then press **Create sections**. Sections table is filled, and sections preview updated.

Several additional waterlines must be added:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m

### Perform plot 

Select **1:100** scale and press **Accept** to let the tool to generate the 3D sections in a new object.

![Resultant sections.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Resultant sections.


</center>

In order to plot these sections you can use the [Drawing workbench](Drawing_Workbench.md):

![Outline draw plot.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Outline draw plot.


</center>

## Transversal areas curve 

One typical ship design hydrodynamic parameter is the transversal areas curve, that retrieves some indicators about the behaviour of the hull (towing resistance, seakeeping, \...). The Ship workbench provides a simple tool in order to perform transversal areas curve.

![Transversal areas curve tool icon.](images/FreeCAD-Ship-AreaCurveIco.png )


<center>

Transversal areas curve tool icon.


</center>

When tool is executed a task dialog is shown, and free surface preview is created in the [3D view](3D_view.md) (Free surface preview will be removed when tool finished, so don\'t worry about this). Into task dialog input and output data is present.

### Input data 

Draft and trim (Hull *y edge* rotation angle, positive if stern draft may increase) must be provided. Several areas curves may be performed, depending on ship load situations, but two typical plot should be performed:

-   Design transversal areas curve: Without trimming angle and using design draft, 1.0 m in this case.
-   Maximum draft transversal areas curve: Without trimming angle, and maximum draft allowed, 2.0 m in this case.

### Output data 

Some relevant data is shown at real time:

-   **L**: Length between perpendiculars, value set at ship instance creation.
-   **B**: Beam selected at ship creation.
-   **T**: Actual draft amidships.
-   **Trim**: Trim angle.
-   **T~AP~**: After perpendicular draft.
-   **T~FP~**: Forward perpendicular draft.
-   **Displacement**: Ship displacement (salt water considered, divide by 1.025 in order to know displaced volume).
-   **XCB**: Buoyancy centre point X coordinate (relative to midship section).

When **Accept** button is pressed a plot is performed (depending on geometry complexity can take some time, you can see progress on terminal, and stop the work pressing **Ctrl**+**C**). When the task has finished FreeCAD will generate a Plot (see the [Plot workbench](Plot_Workbench.md) documentation) and a SpreadSheet (see the [Spreadsheet workbench](Spreadsheet_Workbench.md) documentation).

<img alt="Design draft transversal areas curve. " src=images/FreeCAD-Ship-s60Areas.png  style="width:800px;">


<center>

Design draft transversal areas curve. 


</center>

You can perform maximum draft transversal areas curve in order to see the differences (for instance you are noticing that areas curve is passing through length perpendiculars now).

## Hydrostatics

Hydrostatics computation is a critical stage at ship design due to know principal stability hull parameters. Hydrostatics are mandatory data in order to classification societies certificates ship, and joined with loading condition data (weights and gravity position) provides essential data about ship stability. FreeCAD-Ship provides a tool to obtain main hydrostatics curves (GZ curves are considered in other tool).

![Hydrostatics tool icon.](images/FreeCAD-Ship-HydrostaticsIco.png‎ )


<center>

Hydrostatics tool icon.


</center>

When tool is executed a task dialog is shown. Usually Hydrostatics curves are presented for each trim angle, in this tutorial only upright trimming angle will considered (0º), with an interval around every loading condition draft. Since we don\'t know what loading conditions we can get, we will consider almost draft possibilities (Usually, in order to get as many resolution as possible, naval architects fits the interval to feasible drafts).

So we set following data:

-   **Trim** = 0 deg
-   **Minimum Draft** = 0.1 m
-   **Maximum Draft** = 2.0 m
-   **Number of points** = 39. A lot of points or really complex geometries imply long computation times, in this case around 1 minute can be expend.

When **Accept** button is pressed plots are performed (see the [Plot workbench](Plot_Workbench.md) documentation) and a spreadsheet is generated (see the [Spreadsheet workbench](Spreadsheet_Workbench.md) documentation).

<img alt="Hydrostatics curves." src=images/FreeCAD-Ship-HydrostaticsCurves.png  style="width:800px;">


<center>

Hydrostatics curves.


</center>

## Continue learning 

The [FreeCAD Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md) is the second chapter of Series 60 from Iowa university ship.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial/ru
