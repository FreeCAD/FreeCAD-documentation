---
- TutorialInfo:/pl
   Topic: Projekty / Kreślenie
   Level: Początkujący
   Time: 15 minut
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16 lub nowszy
   Files:
---

# Drawing tutorial/pl

 **Rozwój Środowiska pracy [Kreślenie](Drawing_Workbench/pl.md) zatrzymał się w FreeCAD '''0.16''', a nowe Środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) mające na celu zastąpienie go zostało wprowadzone w wersji '''0.17'''. Oba Środowiska pracy są nadal dostępne w wersji '''0.17''', ale środowisko pracy Kreślenie może zostać usunięte w przyszłych wydaniach.**



### Introduction

This tutorial is meant to introduce the reader to the basic workflow of the [Drawing Workbench](Drawing_Workbench.md), as well as most of the tools that are available to create blueprints.

<img alt="" src=images/Drawing_tutorial_result.png  style="width:480px;">

### Requirements

-   FreeCAD version 0.16 or above
-   The reader has the basic knowledge to use the Part and PartDesign Workbenches
-   The reader has finished the [Draft tutorial](Draft_tutorial.md)

### Procedure

#### Preparations

To reduce the time required for this tutorial, it is compulsory to group together similar elements in the **Tree View** to apply operations at the same time to several elements.

##### Grouping elements 

1.  In the **Tree View**, right-click on the name of the document. In this case **Unnamed**.
2.  Select **Create group**. You can alter the name of the group by double clicking on it from the **Tree View**.
3.  Select the elements that you wish to add and **drag** them into the group

Create the following groups:

-   Draft_objects
-   Draft_dimensions
-   Draft_annotations_text

#### Drawing Templates 

Templates are the base for the creation of Drawings, you can use the templates provided or create your own.

1.  Slect the dropdown menu next to <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [New A3 landscape drawing](Drawing_Landscape_A3.md)
2.  Select **A4 Landscape**

We now have a folder called **Page** in the **Tree View**. This object will contain everything related to the **Drawing**.

#### Projections

Projections are defined as the visual representation of an object on a specific plane, it displays the properties of the object that are visible from that specific orientation.

##### Orthographic Projections 

These are used in Engineering to specify the properties of an object that will be machined. There are two common standards: **Third Angle** and **First Angle** projections.

For this tutorial, these projections aren\'t used because our objects only have a meaningful representation in the XY plane.

1.  Select the object you wish to project into the drawing.
2.  Select <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md)
3.  Select the type of **projection** you want to use
4.  Select the view you want to add

In the **General** and **Axonometric** tabs you can specify the **location**, **scale** and **separation** of each view.

##### Other Part Projections 

It is possible to create custom views of the object.

1.  Select the object you wish to project into the drawing.
2.  Select <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Insert a view](Drawing_View.md)
3.  In the **Data** tab edit the **Direction** of the **Shape View** by altering the values for the **X**, **Y**, and **Z** axes. By default, the values are **(0, 0, 1)**

You can also alter the **location**, **scale** and **rotation** of the **View** from within the **Data** tab. The same can be done for the **Orthographic Projections**.

##### Draft Projections 

The preferred way to add elements created in the **Draft Workbench** is with a tool contained in the **Draft Workbench** designed specifically for this. With this procedure, it is possible to import **Dimensions**, **Annotations**, **Shapestrings** and any other element created whithin the **Draft** Workbench.

1.  Switch to the **Draft** Workbench
2.  Select the **group** or **elements** that you wish to project. In this case **Draft_dimensions**
3.  Select ![](images/Draft_PutOnSheet.png ) [Drawing](Draft_Drawing.md)
4.  Edit the **X** and **Y** coordinates to **(140,100)**
5.  Set the scale to 0.5

Repeat for each group and set the values to the ones specified above.

#### Exporting your work 

FreeCAD supports the export of SVG and PDF files based on your **Drawings**

##### SVG

1.  Select <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save sheet](Drawing_Save.md)
2.  Specify the path and name of the exported file

##### PDF

1.  In the **File** menu, select **Export PDF \...**
2.  Specify the path and name of the exported file

We are now finished with the basic workflow for the [Drawing Workbench](Drawing_Workbench.md).

## Recommended Reading 

-   To learn how to create custom templates see [Drawing Template HowTo](Drawing_Template_HowTo.md)
-   For more information about the tools available check out the [Drawing Workbench](Drawing_Workbench.md) page


 {{Drawing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Drawing](Category_Drawing.md) > Drawing tutorial/pl
