---
 GuiCommand:
   Name/ru: Скругление
   Name: Sketcher_CreateFillet
   MenuLocation: Sketch , Геометрия эскиза , Создать скругление
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **G** **F** **F**
   SeeAlso: Sketcher_CreatePointFillet/ru
---

# Sketcher CreateFillet/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Данный инструмент создает скругление между двумя линиями, соединенными в одной точке.


</div>


<small>(v1.0)</small> 

: If two straight edges connected by a [Coincident constraint](Sketcher_ConstrainCoincident.md) are filleted or chamfered, the corner point can optionally be preserved. The tool then adds a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both edges. Constraints connected to the corner point are transferred to the new point object.

![](images/SketcherCreateFilletExample.png‎ )



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Выберите вершину, соединяющую две линии; или нажмите на две соединенные линии, расстояние от вершины, на котором вы нажмете, установит радиус сопряжения.
-   Нажатие **Esc** или правой кнопки мыши закрывает функцию.


</div>

## Notes

-   The construction geometry arc of a chamfer is not visible outside the sketch. It cannot be deleted without breaking the geometry of the chamfer.
-   Some ([conic](Sketcher_Workbench#Sketcher_CompCreateConic.md)) curves may need to be [trimmed](Sketcher_Trimming.md) before they can be filleted.
-   The fillet radius depends on the selection method. If a [Coincident constraint](Sketcher_ConstrainCoincident.md) connecting two straight edges is selected, the fillet radius is derived from the length of the shortest edge. If two edges are selected the radius is the distance from the first clicked point to the (extended) intersection of the edges.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/ru
