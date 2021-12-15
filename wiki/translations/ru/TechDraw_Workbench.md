# <img alt="Логотип верстака TechDraw" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/ru

## Введение

Верстак _, [PartDesign](PartDesign_Workbench/ru.md), [Arch](Arch_Workbench.md). 3D модели импортированные из других приложений, так же могут быть применены для построения чертежа. Каждый чертеж представляет собой лист, который может содержать различные виды отображаемых объектов, таких как: Part::Features, PartDesign::Bodies, App::Part groups и группы объектов документа. Полученные листы можно использовать в качестве документации, инструкции по эксплуатации, перечня элементов, спецификации и т. д.

В чертеж могут быть добавлены такие элементы как: размеры, сечения 3D Вида, дополнительные заштрихованные области, надписи и примечания, чертежные знаки в формате [SVG](SVG/ru.md). Чертеж так же можно экспортировать в различные форматы, такие как [DXF](DXF/ru.md), [SVG](SVG/ru.md) или [PDF](PDF/ru.md).

TechDraw был официально включен в FreeCAD начиная с версии 0.17; он предназначен для замены неподдерживаемого верстака [Drawing](Drawing_Workbench/ru.md). Оба верстака все еще представлены в версии v0.17, но верстак Drawing может быть удален в будущих релизах. Чтобы не отставать от планов и разработок TechDraw, посетите дорожную карту [TechDraw](TechDraw_Roadmap/ru.md).

Если вашей основной целью является создание сложных 2D чертежей и файлов в формате [DXF](DXF/ru.md), и вам не нужно 3D-моделирование, возможно FreeCAD будет не самым лучшим выбором для вас. Вы можете использовать специальное программное обеспечение для построения технических чертежей, такое как [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) или [QCad](https://en.wikipedia.org/wiki/QCad).


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example_ru-ru.png  style="width:425px;">

## Страницы

Содержит инструменты для создания объектов Page.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> _ по умолчанию.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Перерисовать страницу](TechDraw_RedrawPage/ru.md): принудительно обновляет выбранные листы. {{Version/ru|0.19}}

## Виды

Содержит инструменты для создания Видов (Проекций).

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Новый Вид](TechDraw_View/ru.md): добавляет 2D проекционный вид объекта.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Вставить активный вид (3D Вид)](TechDraw_ActiveView/ru.md): вставляет в чертеж Вид, активного 3D вида. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Вставить группу проекций](TechDraw_ProjectionGroup/ru.md): вызывает диалоговое окно для создания множества видов объекта с нескольких направлений.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Вставить Вид сечения](TechDraw_SectionView/ru.md): добавляет вид поперечного сечения в существующий вида.

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Вставить подробный Вид](TechDraw_DetailView/ru.md): добавляет подробный вид части существующего вида.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> _ или вид [Секущей Плоскости](Arch_SectionPlane/ru.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> _.

## Группа Видов 

Содержит инструменты для создания и управления группой Видов.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Создать группу Видов](TechDraw_ClipGroup/ru.md): Вставляет группу Видов.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Добавить Вид в группу](TechDraw_ClipGroupAdd/ru.md): Добавляет существующий Вид в группу.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Удалить Вид из группы](TechDraw_ClipGroupRemove/ru.md): Удаляет вид из группы.

## Доработка

Содержит инструменты для добавления недостающих элементов в чертеж или Вид:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Заштриховать грань, используя файл изображения](TechDraw_Hatch/ru.md): Штриховать грань, используя файл изображения.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Применить геометрическую штриховку к грани](TechDraw_GeometricHatch/ru.md): Применяет шаблон штриховки к участку, используя спецификацию Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> _ файла.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> _ PNG или JPG.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Вкл/выкл отображение рамки](TechDraw_ToggleFrame/ru.md): включает и выключает рамки и метки, окружающие Вид.

## Размеры

Содержит инструменты для создания и работы с размерами.

Линейные размеры могут основываться на двух точках, на одной линии или на двух линиях.

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Указать длинну](TechDraw_LengthDimension/ru.md): задает произвольное расстояние.

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Указать горизонтальный размер](TechDraw_HorizontalDimension/ru.md): задает размер по горизонтали.

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Указать вертикальный размер](TechDraw_VerticalDimension/ru.md): задает размер по вертикали.

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Указать радиус](TechDraw_RadiusDimension/ru.md): задает радиус окружности или дуги.

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Указать диаметр](TechDraw_DiameterDimension/ru.md): задает диаметр окружности или дуги.

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Указать угловой размер](TechDraw_AngleDimension/ru.md): задает величину угла между двумя прямыми краями.

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Указать угловой размер по 3 точкам](TechDraw_3PtAngleDimension/ru.md): задает величину угла, используя три вершины.

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Указать горизонтальный габаритный размер](TechDraw_HorizontalExtentDimension/ru.md): добавляет габаритный размер по горизонтали. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Указать вертикальный габаритный размер](TechDraw_VerticalExtentDimension/ru.md): добавляет габаритный размер по вертикали. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Связать размер с 3D геометрией](TechDraw_LinkDimension/ru.md): связывает существующий размер с трехмерной геометрией.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Вставить примечание в выноску](TechDraw_Balloon/ru.md): создает аннотацию на странице. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Вставить размер знака](TechDraw_LandmarkDimension/ru.md): добавляет размер указывающий расстояние до landmark. {{Version/ru|0.19}}


<div class="mw-translate-fuzzy">

## Вспомогательные инструменты 


</div>

Вспомогательные инструменты предназначены для \"нанесения поверх чертежа\" дополнительной информации.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Добавить Аннотацию](TechDraw_Annotation/ru.md): добавляет простой текстовый блок в качестве аннотации.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Добавить линию-выноску в Вид](TechDraw_LeaderLine/ru.md): добавляет линию-выноску к Виду. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Вставка аннотаций c форматированным текстом](TechDraw_RichTextAnnotation/ru.md): добавляет в Вид блок форматированного текста в качестве аннотации к линии-выноске. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Добавить вспомогательную вершину](TechDraw_CosmeticVertex/ru.md): добавляет вершину, которая не является частью исходной геометрии. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Добавить вершины по центрам граней](TechDraw_Midpoints/ru.md): добавляет вспомогательные вершины в центральные точки выбраных граней.

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Добавить 4-ре вершины по краям окружности](TechDraw_Quadrants/ru.md): Инструмент Четверть добавляет вспомогательные вершины в окружность, деля ее на четверти. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Добавить осевую линию к граням](TechDraw_FaceCenterLine/ru.md): добавляет осевую линию к выбранной грани или граням. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Добавить осевую линию между 2 линиями](TechDraw_2LineCenterLine/ru.md): добавляет осевую линию между 2 линиями. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Добавить осевую линию между 2 точками](TechDraw_2PointCenterLine/ru.md): добавляет осевую линию между 2 точками. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Добавить вспомогательную линию между 2-мя точками](TechDraw_2PointCosmeticLine/ru.md): добавить вспомогательную линию по двум точкам. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Удалить вспомогательный объект](TechDraw_CosmeticEraser/ru.md): удаляет вспомогательные объекты с чертежа. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Изменить внешний вид линий](TechDraw_DecorateLine/ru.md): позволяет изменить внешний вид выделенных линий. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Показать/скрыть невидимые края](TechDraw_ShowAll/ru.md): позволяет показать/скрыть невидимые линии/грани Вида. {{Version/ru|0.19}}

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Добавить информацию о сварке в линию-выноску](TechDraw_WeldSymbol/ru.md): добавляет символы сварки и другие параметры к существующей Линии-выноске. <small>(v0.19)</small> 

## Инструменты дополнения 

Данные инструменты предназначены для улучшения TechDraw чертежей.


**Некоторые из этих инструментов еще не опубликованы.**

### Attributes and modifications 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Добавить осевые линии к окружности](TechDraw_ExtensionCircleCenterLines/ru.md): Позволяет добавить осевые линии к окружностям и дугам. {{Version/ru|0.20}}


</div>

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:32px;"> [Stretch](TechDraw_ExtensionExtendLine.md): extend a line at both ends. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width:32px;"> [Shorten](TechDraw_ExtensionShortenLine.md): shorten a line at both ends. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width:32px;"> [Lock/Unlock](TechDraw_ExtensionLockUnlockView.md): Lock/Unlock a view. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width:32px;"> [Align Section](TechDraw_ExtensionPositionSectionView.md): align a section view orthogonal to its source view. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:32px;"> [Align Horizontal](TechDraw_ExtensionPosHorizChainDimension.md): align a horizontal dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width:32px;"> [Align Vertical](TechDraw_ExtensionPosVertChainDimension.md): align a vertical dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width:32px;"> [Align Oblique](TechDraw_ExtensionPosObliqueChainDimension.md): align an oblique dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:32px;"> [Horizontal Spacing](TechDraw_ExtensionCascadeHorizDimension.md): cascade horizontal dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width:32px;"> [Vertical Spacing](TechDraw_ExtensionCascadeVertDimension.md): cascade vertical dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width:32px;"> [Oblique Spacing](TechDraw_ExtensionCascadeObliqueDimension.md): cascade oblique dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width:32px;"> [Change Aspect](TechDraw_ExtensionChangeLineAttributes.md): change style, width and colour of lines. <small>(v0.20)</small> 

### Centerlines and threading 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Arc-Circle Centerlines](TechDraw_ExtensionCircleCenterLines.md): adds centerlines to circles and arcs. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width:32px;"> [Circular Series Centerlines](TechDraw_ExtensionHoleCircle.md): draw the centerlines of a hole/bolt circle. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:32px;"> [Intersection Point](TechDraw_ExtensionVertexAtIntersection.md): create the vertexes at intersection of lines. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:32px;"> [Circunference](TechDraw_ExtensionDrawCosmCircle.md): draw a cosmetic circumference using center and radius vertex. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawArc.svg  style="width:32px;"> [Arch](TechDraw_ExtensionDrawArc.md): draw an arc rotating counterclockwise. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width:32px;"> [Perpendicular](TechDraw_ExtensionLinePerpendicular.md): draw a line perpendicular to another line through a vertex. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:32px;"> [Parallel](TechDraw_ExtensionLineParallel.md): draw a line parallel to another line through a vertex. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Обозначить внутреннюю резьбу в разрезе отверстия](TechDraw_ExtensionThreadHoleSide/ru.md): добавляет внутреннюю резьбу к разрезу отверстия. {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [Обозначить наружную резьбу в разрезе стержня](TechDraw_ExtensionThreadBoltSide/ru.md): добавляет наружную резьбу к разрезу стержня. {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Обозначить внутреннюю резьбу отверстия с сечением вдоль оси](TechDraw_ExtensionThreadHoleBottom/ru.md): добавляет внутреннюю резьбу к отверстию с сечением вдоль оси. {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Обозначить наружную резьбу стержня с сечением вдоль оси](TechDraw_ExtensionThreadBoltBottom/ru.md): добавляет наружную резьбу к стердню с сечением вдоль оси. {{Version/ru|0.20}}


</div>

### Dimensions

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:32px;"> [Diameter Symbol](TechDraw_ExtensionInsertDiameter.md): insert diameter sign as praefix character. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width:32px;"> [Tubular Symbol](TechDraw_ExtensionInsertSquare.md): insert square sign as praefix character. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Horizontal Series](TechDraw_ExtensionCreateHorizChainDimension.md): create a horizontal dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Vertical Series](TechDraw_ExtensionCreateVertChainDimension.md): create a vertical dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Oblique Series](TechDraw_ExtensionCreateObliqueChainDimension.md): create an oblique dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Parallel Horizontal](TechDraw_ExtensionCreateHorizCoordDimension.md): create cascaded horizontal dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Parallel Vertical](TechDraw_ExtensionCreateVertCoordDimension.md): create cascaded vertical dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Parallel Oblique](TechDraw_ExtensionCreateObliqueCoordDimension.md): create cascaded oblique dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Horizontal Chamfer](TechDraw_ExtensionCreateHorizChamferDimension.md): create a horizontal chamfer dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Vertical Chamfer](TechDraw_ExtensionCreateVertChamferDimension.md): create a vertical chamfer dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Arc Length](TechDraw_ExtensionCreateLengthArc.md): create an arc length dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:32px;"> [Increase Accuracy](TechDraw_ExtensionIncreaseDecimal.md): increase decimal places . <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width:32px;"> [Decrease Accuracy](TechDraw_ExtensionDecreaseDecimal.md): decrease decimal places . <small>(v0.20)</small> 

## Экспорт

Содержит инструменты для экспорта страниц в другие приложения.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> _ файл.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> _ файл.

## Дополнительные возможности 

-   [Группы Линий](TechDraw_LineGroup/ru.md): позволяет назначить толщину различным типам линий по умолчанию.
-   [Шаблоны](TechDraw_Templates/ru.md): шаблоны по умолчанию, определенные для страниц чертежей.
-   [Штриховка](TechDraw_Hatching/ru.md): объяснение различных методов штриховки.
-   [геометрические размеры и допуски](TechDraw_Geometric_dimensioning_and_tolerancing/ru.md): руководство по обознаению геометрических размеров и допусков.

## Настройки

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Настройки](TechDraw_Preferences/ru.md): настройки значений по умолчанию для страницы чертежа, такие как угол проекции, цвета, размеры текста и стили линий.

## Программирование

Инструменты TechDraw можно использовать в [macros](macros/ru.md) и в консоли [Python](Python/ru.md) с помощью двух APIs.

-   [TechDraw API](TechDraw_API/ru.md)
-   [TechDrawGui API](TechDrawGui_API/ru.md)

## Ограничения

-   Чертежи TechDraw и его API не являются взаимозаменяемыми с [Чертежами Drawing](Drawing_Workbench/ru.md) и его API. Можно конвертировать чертежи Drawing в чертежи TechDraw, используя скрипт Python (`moveViews.py`).
-   В одном документе FreeCAD можно совмещать как чертежи TechDraw, так и чертежи Drawing, поскольку каждая страница полностью независима друг от друга.
-   Существуют небольшие различия в спецификации редактируемого текста в [SVG](SVG/ru.md) шаблонах по сравнению с модулем Drawing. В TechDraw масштабирование документа SVG влияет на положение редактируемых текстовых полей. Смотрите обсуждение на форуме [TechDraw templates scale](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271) для более детальной информации.
-   Не вырезайте, не копируйте и не вставляйте объекты TechDraw в древовидном виде, так как это обычно не работает.

## Руководства


<div class="mw-translate-fuzzy">

-   [TechDraw руководство для начинающих](Basic_TechDraw_Tutorial/ru.md): введение в создание чертежей с помощью Верстака TechDraw.
-   [Создание нового шаблона](TechDraw_TemplateHowTo/ru.md): инструкции по созданию нового шаблона страницы в Inkscape для использования с Верстака TechDraw.
-   [Measurement Of Angles On Holes](Measurement_Of_Angles_On_Holes/ru.md): инструкция по добавлению осевых линий и последующих угловых представлений на отверстиях.
-   [Разнообразная информация](TechDraw_HowTo_Page/ru.md): инструкции по различным настройкам, таким как обозначение центральных осей и т. п.
-   [Создание окружностей с заданным шагом](TechDraw_Pitch_Circle_Tutorial/ru.md): инструкция по созданию окружностей по траектории с шагом.


</div>

Видео уроки by sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   Верстак TechDraw [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/ru
