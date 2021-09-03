---
- GuiCommand:/fr   Name:Ship Outline   Name/fr:Ship Outline   MenuLocation:Ship design → Outline draw   |Workbenches:[[Ship Workbench/fr   Ship]]|Shortcut:   SeeAlso:---


</div>

## Description

Plots the ship hull outline draw

## Lines drawing 

Ship provides a tool that makes it easy to obtain a Lines Plan from the ship lines drawing

![Outline draw tool.](images/Ship_OutlineDraw.svg )


<center>

Lines drawing tool icon


</center>

Lines drawing is a set of lines from section cuts in all 3 axis, that will eventually show the hull geometry in a Lines Plan. We need to provide the lines for the 3 following views:

-   Body Plan (using the Transversal Cuts)
-   Sheer Plan (using the Longitudinals Cuts)
-   Half-Breadth Plan (using the Waterlines Cuts)

### Transversal cuts 

Usually 21 transversal equidistant sections between perpendiculars must be performed. in order to do it FreeCAD provides an automatic tool in order to do it, simply select **Transversal** type of sections, go to **Auto create** box and set **21** sections, then press **Create sections**.

![Outline draw transversal sections preview.](images/S60OutlineTransversal.png )


<center>

Outline draw transversal sections preview


</center>

Sections table is filled, and sections preview called **OutlineDraw** shown. Usually more sections was added at bow and stern, where more complex curvatures are registered, in order to do it go to the end of the table, and do *double click* at empty item in order to edit it, pressing intro to confirm. Add following sections:

-   X~22~ = -12.1125 m
-   X~23~ = 12.1125 m

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

## Tutorials

-   [FreeCAD-Ship s60 tutorial ](FreeCAD-Ship_s60_tutorial.md)
-   [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)





{{Ship_Tools_navi

}}  
