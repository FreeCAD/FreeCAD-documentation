---
 GuiCommand:
   Name: Sketcher_MapSketch
   Name/ru: Разместить эскиз на грани
   MenuLocation: Part Design/Sketch ,  Разместить эскиз на грани...
   Workbenches: Sketcher_Workbench/ru, PartDesign_Workbench/ru
   SeeAlso: Sketcher_NewSketch/ru
---

# Sketcher MapSketch/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент размещает созданный эскиз на грани фигуры. Элементы PartDesign, созданные из этого эскиза, будут объединены с базовым телом при использовании добавочных операций (Выдавливание, Вращение) или вычтены из базового тела в случае вычитающих операций (Вырез, Паз).


</div>


<div class="mw-translate-fuzzy">

Обратите внимание, что этот инструмент не используется для создания новых эскизов. Он только размещает или переназначает существующий эскиз на грань тела или элемент PartDesign-а. Типичные случаи использования:

-   Эскиз был создан на стандартной плоскости (XY, XZ, YZ), и вы хотите разместить его на грани твердого тела, чтобы построить из него элемент.
-   Эскиз был размещен на определенной грани твердого тела, но необходимо его перенести на другую грань.
-   Ремонт сломанной модели.


</div>

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">



## Применение


<div class="mw-translate-fuzzy">

-   Выберите грань элемента PartDesign-а или твердого тела.
-   Нажмите на кнопку панели инструментов **<img src="images/Sketcher_MapSketch.svg" width=16px> [Разместить эскиз на грани](Sketcher_MapSketch/ru.md)** (или перейдите в меню PartDesign или Sketch в зависимости от того, какой верстак активен).
-   В открывшемся диалоге **Выбор эскиза**, выберите из списка эскиз для размещения на грани и нажмите OK.
-   Эскиз автоматически откроется в режиме редактирования.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/ru
