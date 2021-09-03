




<img alt="Иконка верстака TechDraw" src=images/Workbench_TechDraw.svg  style="width:128px;">

## Введение


<div class="mw-translate-fuzzy">

Верстак [TechDraw](TechDraw_Workbench/ru.md) используется для создания базовых технических чертежей из 3D-моделей, созданных с помощью другого верстака, такого как [Part](Part_Workbench/ru.md), [PartDesign](PartDesign_Workbench/ru.md), или [Arch](Arch_Workbench.md), или импортированных моделей из других приложений. Каждый чертеж представляет собой страницу, которая может содержать различные виды рисуемых объектов, такие как Part::Features, PartDesign::Bodies, App::Part groups и группу Объектов Документа. Полученные чертежи можно использовать для таких вещей, как документация, производственные инструкции, контракты, разрешения и т. д.


</div>

Размеры, сечения, заштрихованные области, аннотации и [SVG](SVG/ru.md) символы могут быть добавлены на страницу, которую затем можно экспортировать в различные форматы, такие как [DXF](DXF/ru.md), [SVG](SVG/ru.md), и [PDF](PDF/ru.md).

TechDraw был официально включен в FreeCAD начиная с версии 0.17; он предназначен для замены неподдерживаемого верстака [Drawing](Drawing_Workbench/ru.md). Оба верстака все еще представлены в версии v0.17, но верстак Drawing может быть удален в будущих релизах. Чтобы не отставать от планов и разработок TechDraw, посетите дорожную карту [TechDraw](TechDraw_Roadmap/ru.md).

FreeCAD - это, прежде всего, приложение для 3D-моделирования, и поэтому у него нет многих инструментов для 2D-рисования, которые в основном включены в верстаки [Draft](Draft_Workbench/ru.md) и [Sketcher](Sketcher_Workbench/ru.md). Если вашей основной целью является создание сложных 2D-чертежей и файлов в формате [DXF](DXF/ru.md), и вам не нужно 3D-моделирование, возможно вы захотите использовать специальное программное обеспечения для технического черчения, такое как [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), TurboCad, и другое.


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Страницы

Это инструменты для создания объектов Page.

-   <img alt="" src=images/techdraw-new-default.svg  style="width:32px;"> [Новый По Умолчанию](TechDraw_PageDefault/ru.md): добавляет новую страницу используя [шаблон](TechDraw_Templates/ru.md) по умолчанию.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/techdraw-new-pick.svg  style="width:32px;"> [Выбрать Новый](TechDraw_New_Pick/ru.md): добавляет новую страницу, используя выбранный [шаблон](TechDraw_Templates/ru.md).


</div>

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Redraw Page](TechDraw_RedrawPage.md): forces an update of the selected page. <small>(v0.19)</small> 

## Виды

Это инструменты для создания Видов (Проекций).

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Новый Вид](TechDraw_View/ru.md): добавляет 2D проекционный вид объекта.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Insert Active View](TechDraw_ActiveView.md): inserts a view of the active 3D view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Новая Группа Проекций](TechDraw_NewProjGroup/ru.md): вызывает диалоговое окно для создания множества видов объекта с нескольких направлений.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/techdraw-viewsection.svg  style="width:32px;"> [Новое Сечение](TechDraw_NewSection/ru.md): добавляет поперечное сечение существующего вида.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/techdraw-viewdetail.svg  style="width:32px;"> [Новый Детальный Вид](TechDraw_NewDetail/ru.md): добавляет подробный вид части существующего вида.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/techdraw-draft-view.svg  style="width:32px;"> [Новый Чертеж](TechDraw_NewDraft/ru.md): добавляет Вид объекта из верстака [Draft ](Draft_Workbench/ru.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/techdraw-arch-view.svg  style="width:32px;"> [Новый Архитектурный Вид](TechDraw_NewArch/ru.md): добавляет Вид объекта из верстака [Arch](Arch_Workbench/ru.md) или вид [Секущей Плоскости](Arch_SectionPlane/ru.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/techdraw-spreadsheet.svg  style="width:32px;"> [Таблица](TechDraw_Spreadsheet/ru.md): добавляет таблицу из верстака [Spreadsheet](Spreadsheet_Workbench/ru.md).


</div>

## Группа Видов 

Это инструменты для создания и управления группой Видов.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Вставить группу срезов](TechDraw_ClipGroup/ru.md): Вставить группу срезов.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Добавить вид в группу срезов](TechDraw_ClipGroupAdd/ru.md): Добавить вид в группу срезов.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Удалить вид из группы срезов](TechDraw_ClipGroupRemove/ru.md): Удалить вид из группы срезов.

## Размеры

Это инструменты для создания и работы с размерами.

Линейные размеры могут основываться на двух точках, на одной линии или на двух линиях.

-   <img alt="" src=images/TechDraw_Dimension_Length.svg  style="width:32px;"> [Задать Расстояние](TechDraw_Dimension_Length/ru.md): задает произвольное расстояние.

-   <img alt="" src=images/TechDraw_Dimension_Horizontal.svg  style="width:32px;"> [Задать Горизонтальный Размер](TechDraw_Dimension_Horizontal/ru.md): задает размер по горизонтали.

-   <img alt="" src=images/Dimension_Vertical.png  style="width:32px;"> [Задать Вертикальный Размер](TechDraw_Dimension_Vertical/ru.md): задает размер по вертикали.

-   <img alt="" src=images/TechDraw_Dimension_Radius.svg  style="width:32px;"> [Задать Радиус](TechDraw_Dimension_Radius/ru.md): задает радиус окружности или дуги.

-   <img alt="" src=images/TechDraw_Dimension_Diameter.svg  style="width:32px;"> [Задать Диаметр](TechDraw_Dimension_Diameter/ru.md): задает диаметр окружности или дуги.

-   <img alt="" src=images/TechDraw_Dimension_Angle.svg  style="width:32px;"> [Задать Угол](TechDraw_Dimension_Angle/ru.md): задает величину угла между двумя прямыми краями.

-   <img alt="" src=images/TechDraw_Dimension_Angle3Pt.svg  style="width:32px;"> [Задать Угол по 3 Вершинам](TechDraw_Dimension_Angle3Pt/ru.md): задает величину угла, используя три вершины.

-   <img alt="" src=images/TechDraw_Dimension_Horizontal_Extent.svg  style="width:32px;"> [New Horizontal Extent](TechDraw_Dimension_Horizontal_Extent.md): adds a horizontal extent dimension. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Dimension_Vertical_Extent.svg  style="width:32px;"> [New Vertical Extent](TechDraw_Dimension_Vertical_Extent.md): adds a vertical extent dimension. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Dimension_Link.svg  style="width:32px;"> [Создать Ссылку](TechDraw_Dimension_Link/ru.md): связывает существующий размер с трехмерной геометрией.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Создать Аннотацию](TechDraw_Balloon/ru.md): создает аннотацию на странице. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_Dimension_Landmark.svg  style="width:32px;"> [New Landmark Dimension](TechDraw_Dimension_Landmark.md): adds a landmark distance dimension. <small>(v0.19)</small> 

## Импорт/Экспорт

Это инструменты для экспорта страниц в другие приложения.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Экспорт страницы в SVG](TechDraw_ExportPageSVG/ru.md): Экспорт страницы в [SVG](SVG/ru.md) файл.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Экспорт страницы в DXF](TechDraw_ExportPageDXF/ru.md): Экспорт страницы в [DXF](DXF/ru.md) файл.

## Доработка

Это инструменты для добавления недостающих элементов в чертеж или Вид:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Заштриховать грань, используя файл изображения](TechDraw_Hatch/ru.md): Штриховать грань, используя файл изображения.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Применить геометрическую штриховку к грани](TechDraw_GeometricHatch/ru.md): Применяет шаблон штриховки к участку, используя спецификацию Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [Вставить SVG Символ](TechDraw_Symbol/ru.md): Вставляет на страницу Символ из [SVG](SVG/ru.md) файла.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Techdraw-image.svg  style="width:32px;"> [Вставить Рисунок](TechDraw_Image/ru.md): вставляет на страницу рисунок в формате [bitmap](bitmap/ru.md) PNG или JPG.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/techdraw-toggleframe.svg  style="width:32px;"> [Выключатель Рамки](TechDraw_Toggle/ru.md): включает и выключает рамки и метки, окружающие вид.


</div>

## Аннотации

Инструменты аннотаций предназначены для «разметки» чертежа дополнительной информацией.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Добавить Аннотацию](TechDraw_Annotation/ru.md): добавляет простой текстовый блок в качестве аннотации.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:24px;"> [Линия-выноска](TechDraw_LeaderLine/ru.md): добавляет линию-выноску к Виду. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:24px;"> [Вставка форматированной аннотаци](TechDraw_RichTextAnnotation/ru.md): добавляет в Вид блок форматированного текста в качестве аннотации к линии-выноске. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:24px;"> [Добавить Вспомогательную Вершину](TechDraw_CosmeticVertex/ru.md): добавляет вершину, которая не является частью исходной геометрии. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:24px;"> [Добавить Средние Вершины](TechDraw_Midpoints/ru.md): добавляет вспомогательные вершины в центральные точки выбраных граней.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:24px;"> [Четверть](TechDraw_Quadrants/ru.md): Инструмент Четверть добавляет вспомогательные вершины в окружность, деля ее на четверти. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:24px;"> [Осевая Линия](TechDraw_FaceCenterLine/ru.md): добавляет осевую линию к выбранной грани или граням. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:24px;"> [Добавить Осевую линию между 2 Линиями](TechDraw_2LineCenterLine/ru.md): добавляет осевую линию между 2 линиями. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:24px;"> [Добавить Осевую линию между 2 точками](TechDraw_2PointCenterLine/ru.md): добавляет осевую линию между 2 точками. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:24px;"> [Добавить косметическую линию](TechDraw_2PointCosmeticLine/ru.md): добавить вспомогательную линию соединяющую 2 точки. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:24px;"> [Удалить вспомогательный объект](TechDraw_CosmeticEraser/ru.md): удаляет вспомогательные объекты с чертежа. {{Version/ru|0.19}}


</div>

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Change Appearance of Lines](TechDraw_DecorateLine.md): changes the appearance of selected line(s). <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Show/Hide Invisible Edges](TechDraw_ShowAll.md): shows/hides invisible lines/edges in a view. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:24px;"> [Добавить информацию о сварке в Линию-выноску](TechDraw_WeldSymbol.md): добавляет символы сварки и другие параметры к существующей Линии-выноске. <small>(v0.19)</small> 


</div>

## Дополнительные возможности 


<div class="mw-translate-fuzzy">

-   [Штриховка](TechDraw_Hatching/ru.md): объяснение различных методов штриховки.
-   [Группы Линий](TechDraw_LineGroup/ru.md): можно назначить толщины по умолчанию различным типам линий.
-   [Шаблоны](TechDraw_Templates/ru.md): шаблоны по умолчанию, определенные для страниц чертежей.


</div>

## Настройки

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Настройки](TechDraw_Preferences/ru.md): настройки значений по умолчанию для страницы чертежа, такие как угол проекции, цвета, размеры текста и стили линий.


<div class="mw-translate-fuzzy">

## Скриптинг

Инструменты TechDraw можно использовать в [macros](macros/ru.md) и в консоли [Python](Python/ru.md) с помощью двух APIs.

-   [TechDraw API](TechDraw_API/ru.md)
-   [TechDrawGui API](TechDrawGui_API/ru.md)


</div>


<div class="mw-translate-fuzzy">

## Ограничения

-   Чертежи TechDraw и его API не являются взаимозаменяемыми с [Чертежами Drawing](Drawing_Workbench/ru.md) и его API. Можно конвертировать чертежи Drawing в чертежи TechDraw, используя скрипт Python (`moveViews.py`).
-   В одном документе FreeCAD можно совмещать как чертежи TechDraw, так и чертежи Drawing, поскольку каждая страница полностью независима друг от друга.
-   Существуют небольшие различия в спецификации редактируемого текста в [SVG](SVG/ru.md) шаблонах по сравнению с модулем Drawing. В TechDraw масштабирование документа SVG влияет на положение редактируемых текстовых полей. Смотрите обсуждение на форуме [TechDraw templates scale](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271) для более детальной информации.
-   Не вырезайте, не копируйте и не вставляйте объекты TechDraw в древовидном виде, так как это обычно не работает.


</div>

## Уроки


<div class="mw-translate-fuzzy">

-   [Базовое руководство по TechDraw](Basic_TechDraw_Tutorial/ru.md): введение в создание чертежей с помощью Верстака TechDraw.
-   [Создание нового шаблона](TechDraw_TemplateHowTo/ru.md): инструкции по созданию нового шаблона страницы в Inkscape для использования с Верстака TechDraw.
-   [Measurement Of Angles On Holes](Measurement_Of_Angles_On_Holes/ru.md): инструкция по добавлению осевых линий и последующих угловых представлений на отверстиях.


</div>

Видео уроки by sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   Верстак TechDraw [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
