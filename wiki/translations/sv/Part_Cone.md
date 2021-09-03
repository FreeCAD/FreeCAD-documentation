---
- GuiCommand:/sv   Name:Part Cone   Name/sv:Part Cone   MenuLocation:Part -> Cone   Workbenches:[SeeAlso:[[Part_CreatePrimitives/sv|Part CreatePrimitives](Part_Workbench/sv___Part]],_Complete.md)---


</div>

## Description

A parametric truncated Part Cone primitive is available in the Part workbench from the Part tool bar, Part menu (primitives sub-menu) and the Create Primitives dialogue.

<img alt="" src=images/Otherwisedefault270degree_Part_Cone.png  style="width:300px;"> 
*A Part Cone with the parameter "Angle" set to 270 degrees and all other parameters are set to their default values.*

## Usage

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md)
2.  There are two ways to invoke the command:
    -   Press the **<img src="images/Part_Cone.svg" width=16px> Cone** button in the toolbar.
    -   Select the {{MenuCommand|Part → Primitives → <img src="images/Part_Cone.svg" width=16px> Cone}} from the menu bar.

**Result:** The default values create a truncated parametric cone that is positioned at the origin (point 0,0,0) and attached to the global xy-plane. Its height of 10 mm is along the global z-axis. The lower **Radius 1** is 2 mm, the upper **Radius 2** is 4 mm.

The cone properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cone in the [Tree view](Tree_view.md).

## Properties

-    **Radius 1**: Radius of the arc or circle defining the lower face

-    **Radius 2**: Radius of the arc or circle defining the upper face

-    **Height**: Height of the Part Cone

-    **Angle**: Number of degrees of the arc or circles defining the upper and lower faces of the truncated cone. The default 360° creates circular faces, a lower value will create a portion of a cone as defined by upper and lower faces each with edges defined by an arc of the number of degrees and two radii.





  
