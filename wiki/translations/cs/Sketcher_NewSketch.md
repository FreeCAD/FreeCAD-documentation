---
 GuiCommand:
   Name: Sketcher NewSketch
   Name/cs: Skicář Nový náčrt
   Workbenches: Sketcher Workbench/cs
   MenuLocation: Náčrt , Vytvoř náčrt
   SeeAlso: Sketcher_MapSketch/cs, Sketcher_ReorientSketch/cs
---

# Sketcher NewSketch/cs


</div>



## Popis

The <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher NewSketch](Sketcher_NewSketch.md) tool creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.

Note that the <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) has its own [new sketch](PartDesign_NewSketch.md) tool. When working on a [PartDesign Body](PartDesign_Body.md) that tool should be used instead.




<div class="mw-translate-fuzzy">

## Použití


</div>

1.  If the sketch should be [attached](Part_EditAttachment.md) to existing geometry: select an object with a shape, or one or more vertices, edges, and/or faces, and/or a plane.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_NewSketch.svg" width=16px> [Create sketch](Sketcher_NewSketch.md)** button.
    -   Select the **Sketch → <img src="images/Sketcher_NewSketch.svg" width=16px> Create sketch** option from the menu.
3.  If geometry has been selected:
    1.  The **Sketch attachment** dialog opens.
    2.  Select an [attachment method](Part_EditAttachment#Attachment_modes.md) from the dropdown list. Or select **Don\'t attach** to ignore the selection.
    3.  Press the **OK** button.
4.  If there is no selection, or **Don\'t attach** has been selected in the previous step:
    1.  The **Choose orientation** dialog opens.
    2.  Specify the plane for the orientation. The plane is relative to the local coordinate system the sketch is in:
        -   If the **Reverse direction** checkbox is not checked:
            -   Top: **XY-Plane**
            -   Front: **XZ-Plane**
            -   Right: **YZ-Plane**
        -   If the **Reverse direction** checkbox is checked:
            -   Bottom: **XY-Plane**
            -   Rear: **XZ-Plane**
            -   Left: **YZ-Plane**
    3.  Optionally change the **Offset**. The offset is measured along the Z, Y or X axis of the local coordinate system.
    4.  Press the **OK** button.
5.  A sketch is created.
6.  The sketch is put in edit mode and the [Sketcher Dialog](Sketcher_Dialog.md) opens.
7.  To finish edit mode see <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Sketcher LeaveSketch](Sketcher_LeaveSketch.md).

## Notes

-   Existing sketches can be attached to (different) object(s) with [Sketcher MapSketch](Sketcher_MapSketch.md) or detached and reoriented with [Sketcher ReorientSketch](Sketcher_ReorientSketch.md).





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/cs
