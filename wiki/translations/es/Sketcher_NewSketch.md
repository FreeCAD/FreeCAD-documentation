---
 GuiCommand:
   Name: Sketcher NewSketch
   Name/es: Croquizador Nuevo croquis
   MenuLocation: Croquis , Crear croquis
   Workbenches: Sketcher_Workbench/es
   SeeAlso: PartDesign_NewSketch/es, Sketcher_MapSketch/es, Sketcher_ReorientSketch/es
---

# Sketcher NewSketch/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esto creará un nuevo [Croquis](Sketcher_Workbench/es.md).


</div>


<div class="mw-translate-fuzzy">

Tenga en cuenta que la <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/es.md) tiene su propia herramienta [nuevo croquis](PartDesign_NewSketch/es.md), cuando se trabaja en un [Cuerpo DiseñoPiezas](PartDesign_Body/es.md) es preferible utilizar esa herramienta.


</div>



## Utilización

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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/es
