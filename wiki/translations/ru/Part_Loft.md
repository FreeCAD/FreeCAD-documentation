---
 GuiCommand:
   Name: Part Loft
   Name/ru: Лофт
   MenuLocation: Деталь , Лофт...
   Workbenches: Part_Workbench/ru
   SeeAlso: Part Sweep/ru
---

# Part Loft/ru


</div>

## Description

The <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft.md) command creates a face, a shell, or a solid shape from two or more profiles (cross-sections).

<img alt="" src=images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg  style="width:400px;"> 
*Loft from three profiles which are two [Part Circles](Part_Circle.md) and one [Part Ellipse](Part_Ellipse.md). Parameters are Solid "True" and Ruled "True".*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Loft.svg" width=16px> [Loft...](Part_Loft.md)** button.
    -   Select the **Part → <img src="images/Part_Loft.svg" width=16px> Loft...** option from the menu.
2.  The Loft [task panel](Task_panel.md) opens.
3.  In the *Available Profiles* list on the left select the first profile and click on the right arrow to place it in the *Selected profiles* list on the right.
4.  Repeat for the second profile and again if more than two profiles are desired.
5.  Optionally use the up and down arrows to reorder the selected profiles.
6.  Define options [Create solid](#Data.md), [Ruled surface](#Data.md), and [Closed](#Data.md).
7.  Click **OK**.

### Accepted geometry 

-   **Profiles:** can be a point (vertex), line (edge), wire or face. Edges and wires may be either open or closed. There are various [Limitations](#Limitations.md), see below.

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles. <small>(v0.20)</small> 

## Options

#### Create solid 

If \"Solid\" is set to \"true\", FreeCAD creates a solid, provided the profiles are closed; if set to \"false\", FreeCAD creates a face or a shell for either open or closed profiles.

#### Ruled surface 

If \"Ruled surface\" is \"true\" FreeCAD creates a face, a shell or a solid from [ruled surfaces](http://en.wikipedia.org/wiki/Ruled_surface).

#### Closed

If \"Closed\" is \"true\" FreeCAD attempts to loft the last profile to the first profile to create a closed loop.

For more information on how profiles are joined together see [Part Loft Technical Details](Part_Loft_Technical_Details.md).

## Properties

See also: [Property editor](Property_editor.md).

A Part Loft object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Loft}}

-    **Sections|LinkList**: lists the sections used.

-    **Solid|Bool**: true or false (default). True creates a solid.

-    **Ruled|Bool**: true or false (default). True creates a ruled surface.

-    **Closed|Bool**: rue or false (default). True creates a closed loft by connecting last to first profile.

-    **Max Degree|IntegerConstraint**: Maximum degree.

## Limitations

A Part Loft has the same limitations as a [Part Sweep](Part_Sweep#Limitations.md).

### Closed Lofts 

-   The results of a closed Loft may be unexpected, the Loft may develop twists or kinks. Lofting is very sensitive to the Placement of the profiles and the complexity of the curves required to connect the corresponding vertices in all the profiles.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/ru
