---
 GuiCommand:-cn
   Name/zh-cn: 创建草图
   Name: Sketcher_NewSketch
   MenuLocation: Sketch , 创建草图
   Workbenches: Sketcher_Workbench/zh-cn
   SeeAlso: PartDesign_NewSketch/zh-cn, Sketcher_MapSketch/zh-cn, Sketcher_ReorientSketch/zh-cn
---

# Sketcher NewSketch/zh-cn


</div>



## 描述


<div class="mw-translate-fuzzy">

此工具将创建一个新的[草图（sketch）](Sketcher_Workbench.md)。


</div>


<div class="mw-translate-fuzzy">

请注意，[零件设计工作台（PartDesign workbench）](PartDesign_Workbench.md)有它自己的[创建新草图](PartDesign_NewSketch.md)命令，当您使用零件设计工作台时，它将采用自己专属的新建工具。


</div>




<div class="mw-translate-fuzzy">

## 如何使用


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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/zh-cn
