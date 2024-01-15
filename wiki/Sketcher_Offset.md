---
 GuiCommand:
   Name: Sketcher Offset
   MenuLocation: Sketch , Sketcher tools , Offset geometry
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **T**
   Version: 0.22
   SeeAlso: 
---

# Sketcher Offset

## Description

The <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> [Sketcher Offset](Sketcher_Offset.md) command draws equidistant edges around selected edges. When starting the command, the mouse pointer changes to a white cross with a red offset icon:  <img alt="" src=images/Sketcher_Pointer_Create_Offset.svg  style="width:32px;"> .

 <img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;">  
*Equidistant edges around a closed (O) and an open (U) construction polyline*

## Usage

1.  Select one or more edges.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Sketcher_Offset.svg" width=16px> [Offset geometry](Sketcher_Offset.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_Offset.svg" width=16px> Offset geometry** option from the menu.
    -   The keyboard shortcut: **Z** then **T**.
3.  An **Offset parameters** section is added at the top of the Sketcher [Task panel](Task_panel.md).
4.  Optionally change the **Mode** combobox from {{Value|Arc}} (default) to {{Value|Intersection}}.
5.  Optionally check the **Delete original geometries** checkbox to only keep the new outline.
6.  Optionally check the **Add offset constraint** checkbox to add a dimensional constraint between the offset outline and the original geometry.
7.  Drag the cursor and click, or enter a distance to set the offset and finish the command. This also removes the **Offset parameters** section from the Task panel.

If **Add offset constraint** was activated the offset can be adjusted by changing the dimensional constraint.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset
