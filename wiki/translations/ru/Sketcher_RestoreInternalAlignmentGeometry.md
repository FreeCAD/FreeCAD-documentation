---
- GuiCommand:
   Name/ru: Показать/скрыть внутреннюю геометрию
   Name: Sketcher_RestoreInternalAlignmentGeometry
   MenuLocation: Sketch - Инструменты для эскиза - Показать/скрыть внутреннюю геометрию
   Workbenches: [Sketcher](Sketcher_Workbench/ru.md)
   Shortcut: Ctrl+Shift+E
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/ru



## Описание

The command deletes unused elements aligned to internal geometry, or recreates the missing ones.



## Применение

-   Select a sketch element that supports internal alignment ([Ellipse](Sketcher_CreateEllipseByCenter.md), [Arc of ellipse](Sketcher_CreateArcOfEllipse.md), [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md), [Arc of parabola](Sketcher_CreateArcOfParabola.md) or [B-spline](Sketcher_CreateBSpline.md)).
-   Invoke the command by clicking **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** or choose **Sketch → Sketcher tools → [<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> Show/hide internal geometry** or using the keyboard shortcut.

If there are free alignment places for the selected element, new construction geometry is created and aligned to the available places. If all alignment places are occupied, the unused internal geometry is deleted (the element is treated as unused if it is not constrained to anything else).



## Пример

1.  Create a new ellipse. New ellipses are always fully-packed. You\'ll see an ellipse and a bunch of construction geometry: major diameter, minor diameter, foci.
2.  Select minor diameter line and hit **Del**. The diameter is gone, but the ellipse remains. How do we get the diameter back?
3.  Select the ellipse and invoke the **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** command. The diameter is restored.
4.  Now, constrain the major diameter of the ellipse to some length. Select the ellipse and invoke the **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** command.

**Result:** Minor diameter and foci are deleted, but the major diameter is kept, because it participates in other constraints. Ellipse\'s center remains too, because it is inherent, like center of a circle.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/ru
