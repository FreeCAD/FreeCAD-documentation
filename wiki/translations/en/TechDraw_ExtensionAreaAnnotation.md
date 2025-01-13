---
 GuiCommand:
   Name: TechDraw ExtensionAreaAnnotation
   MenuLocation: TechDraw , Extensions: Attributes/Modifications , Calculate the area of selected faces
   Workbenches: TechDraw_Workbench
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_AreaDimension
---

# TechDraw ExtensionAreaAnnotation/en

## Description

The **TechDraw ExtensionAreaAnnotation** tool calculates the area of selected faces and inserts an area annotation.

<img alt="" src=images/TechDraw_ExtensionAreaAnnotationExample.png  style="width:400px;"> 
*On the right the inserted area annotation*

## Usage

1.  Select one or more faces.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> [Calculate the area of selected faces](TechDraw_ExtensionAreaAnnotation.md)** button.
    -   Select the **TechDraw → Extensions: Attributes/Modifications → <img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> Calculate the area of selected faces** option from the menu.
3.  The total area of the faces is calculated and an area annotation is inserted.

## Limitation

-    {{VersionMinus|0.21}}: The tool cannot handle faces with curved edges.

-   Holes (islands) in the selected face are ignored. This [forum post](https://forum.freecad.org/viewtopic.php?p=783325#p783325) shows a workaround. You can also use [TechDraw AreaDimension](TechDraw_AreaDimension.md) but you must then correctly set the **References 3D** property of the created dimension.

-   The calculated area is not dynamically linked to the face. If the area of the face changes the text is not updated.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionAreaAnnotation/en
