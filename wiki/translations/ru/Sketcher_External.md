---
 GuiCommand:
   Name/ru: Внешняя геометрия
   Name: Sketcher_External
   MenuLocation: Sketch , Геометрия эскиза , Внешняя геометрия
   Workbenches: Sketcher_Workbench/ru
   Shortcut: X
   SeeAlso: Sketcher_ToggleConstruction/ru
---

# Sketcher External/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Используйте инструмент **<img src="images/Sketcher_External.svg" width=16px> [Внешняя геометрия](Sketcher_External/ru.md)**, когда вам нужно применить ограничение между геометрией эскиза и чем-то вне эскиза. Это работает путем вставки связанной вспомогательной геометрии в эскиз. По умолчанию цвет связанной внешней геометрии пурпурный. Как и в случае стандартной несвязанной вспомогательной геометрии (синего цвета), связанная внешняя геометрия видна только тогда, когда эскиз находится в режиме редактирования, и напрямую не используется в последующих результатах использования эскиза другими инструментами. Оба типа вспомогательной геометрии могут использоваться в качестве ссылок для ограничений в эскизе.


</div>


<small>(v1.1)</small> 

: See <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projection](Sketcher_Projection.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*The two magenta lines are external geometry linked to edges of a pre-existing [Pad](PartDesign_Pad.md). They are used to constrain the circles.*



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Создайте новый эскиз или откройте существующий эскиз.
-   Нажмите кнопку \'Внешняя Геометрия\'.
-   Выберите ребро или вершину, которую вы хотите связать с эскизом.
-   Нажмите Esc, или выберите другой инструмент, чтобы прекратить импорт геометрии в эскиз.


</div>

## Notes

-   Only edges and vertices from objects within the same coordinate system can be selected. The sketch and the object must be in same [Body](PartDesign_Body.md), or the same [Part](Std_Part.md), or both in the global coordinate system. Use a [Binder](PartDesign_SubShapeBinder.md) to bring a copy of the object into the current coordinate system if required.
-   Circular dependencies are not allowed. You cannot link to an object that depends on the sketch itself.
-   Links to elements from other sketches are possible, and encouraged, as they are more reliable than links to generated (solid) geometry. The latter can suffer from the [Topological Naming Problem](Topological_naming_problem.md). See [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/ru
