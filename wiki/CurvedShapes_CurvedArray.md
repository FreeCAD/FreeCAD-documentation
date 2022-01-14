---
- GuiCommand:
   Name:CurvedShapes CurvedArray
   MenuLocation:
   Workbenches:[CurvedShapes](CurvedShapes_Workbench.md)
   Shortcut:
   SeeAlso:
---

# CurvedShapes CurvedArray

## Description

Creates an array and resizes the items in the bounds of one or more hull curves. In this example, the orange base shape is rescaled in the bounds of the red and violet hullcurves. The curves do not have to be connected. The hullcurves should lie on or parallel to the XY- XZ- or YZ- plane.

<https://github.com/chbergmann/CurvedShapesWorkbench/blob/master/Examples/WingExample.png> [Image:](Image:.md)

## Usage

1.  Step 1
2.  Step 2: Invoke the command several way:
    -   Using the <img alt="" src=images/WorkbenchName_Command.svg  style="width:24px;"> [ WorkbenchName Command](WorkbenchName_Command.md) button
    -   Using the {{KEY}} {{KEY}} keyboard shortcut
    -   Using the **Menu → Command** in the Menu dropdown
3.  Step 3

## Notes

-   The first curve that you select for CurvedArray creation will be the item that is swept and resized in the bounds of the other selected curves.

## Properties


{{Properties_Title|Base}}

-    **Base**: The object to make an array from

-    **Hullcurves**: List of one or more bounding curves

-    **Axis**: Direction axis of the Base shape

-    **Items**: Nr. of array items

-    **OffsetStart**: Offset of the first part in Axis direction

-    **OffsetEnd**: Offset of the last part from the end in opposite Axis direction

-    **Twist**: Applies a rotation around Axis to the array items.

-    **Surface**: make a surface over the array items

-    **Solid**: make a solid if Base is a closed shape




 

[<img src="images/Property.png" style="width:16px"> Name](Category_Name.md) [<img src="images/Property.png" style="width:16px"> External Command Reference](Category_External_Command_Reference.md)

---
[documentation index](../README.md) > [Name](Category_Name.md) > CurvedShapes CurvedArray
