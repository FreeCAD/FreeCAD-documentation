---
- GuiCommand:/ru
   Name:Sketcher Trimming
   Name/ru:Обрезать
   MenuLocation:Эскиз → Геометрия эскиза → Обрезать
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Version:0.12
   SeeAlso:[Sketcher Продлить](Sketcher_Extend/ru.md)
---

# Sketcher Trimming/ru

## Описание

Этот инструмент обрезает ребро до ближайшего пересечения с другим ребром.

![](images/SketcherTrimExample1.png ) ![](images/SketcherTrimExample2.png ) ![](images/SketcherTrimExample3.png )

## Применение


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку <img alt="" src=images/Sketcher_Trimming.svg  style="width:24px;"> **Обрезать**. Указатель мыши изменится на белый крест с красным символом обрезки.
2.  Нажмите на ребро, которое вы хотите обрезать.
3.  Сегмент линии будет обрезан до ближайшей пересекающейся линии. Если с обеих сторон позиции, по которой щелкнули, есть другие элементы эскиза, вырезаемая часть будет вырезана до них.
4.  Нажатие {{KEY | ESC}} или правой кнопки мыши закрывает функцию.


</div>

## Ограничения

-    {{VersionMinus/ru|0.18}}Не могут быть обрезаны дуги гиперболы, дуги параболы и B-сплайны.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Trimming/ru
