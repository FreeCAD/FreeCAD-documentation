---
 GuiCommand:
   Name: CurvedShapes CurvedArray
   Name/it: CurvedShapes CurvedArray
   MenuLocation: 
   Workbenches: CurvedShapes Workbench/it
   Shortcut: 
   SeeAlso: 
---

# CurvedShapes CurvedArray/it

## Descrizione

Crea un array e ridimensiona gli elementi all\'interno di una o più curve limite. In questo esempio, la forma di base arancione viene ridimensionata entro le curve limite rosse e viola. Le curve non devono essere collegate. Le curve limite devono trovarsi sul piano XY, XZ o YZ, o su un piano parallelo.

<https://github.com/chbergmann/CurvedShapesWorkbench/blob/master/Examples/WingExample.png> [Image:](Image:.md)

## Utilizzo

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



---
⏵ [documentation index](../README.md) > [Name](Category_Name.md) > [External Command Reference](Category_External Command Reference.md) > CurvedShapes CurvedArray/it
