








{{TOCright}}

## Description

Draft DXF is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the DXF file format.

![](images/Screenshot_qcad.jpg ) *Qcad drawing exported to DXF, which is subsequently opened in FreeCAD*


<div class="mw-translate-fuzzy">

### Открытие

Данная функция открывает файл DXF (любую версию от 12 до 2007) в новом документе. В настоящее время поддерживаются следующие типы объектов DXF:

-   линии
-   полилинии и LW-полилинии (простые полилинии)
-   окружности
-   дуги
-   слои (слои содержащие объекты преобразуются в группы FreeCAD)
-   текст и M-текст
-   размеры
-   блоки (только геометрия, текст, размеры и атрибуты внутри блока будут пропущены)
-   точки <small>(v0.13)</small> 
-   выноски <small>(v0.13)</small> 

Остальные элементы DXF в настоящее время не импортируются, так как им нет соответствующих объектов FreeCAD. По мере добавления нового функционала, станет возможным импортировать остальные элементы DXF.


</div>

The importer has two modes, settable under **Edit → Preferences → Import/Export → DXF**: One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can sometimes handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

3D objects inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD. Simpler entities like 3DFACEs, though, are supported.

The following DXF objects can be imported:

-   lines
-   polylines (and lwpolylines)
-   circles
-   arcs
-   splines
-   ellipses
-   layers
-   texts and mtexts
-   dimensions
-   blocks (only geometry. texts, dimensions and attributes inside blocks will be skipped)
-   points
-   leaders
-   paper space objects


<div class="mw-translate-fuzzy">

### Экспорт

Экспортируемый файл DXF совместим с Autocad версии 12 и новее, поэтому он должен открываться в практически любом приложении поддерживающем формат DXF. В настоящее время поддерживается экспорт следующих объектов FreeCAD:

-   линии и многоточечные линии (полилинии)
-   дуги и окружности
-   текст
-   цвета отображаются из RGB в цветовой индекс Autocad (ACI). Чёрный всегда будет отображён в цвет \"по слою\"
-   слои отображаются по именам групп. При вложенных группах, имя слою даёт самая глубоко вложенная группа.
-   размеры, которые экспортируются со стилем \"стандартный\"


</div>

Files are exported in the R14 DXF format which can be handled by many applications.

The following FreeCAD objects can be exported:

-   all of FreeCAD\'s 2D geometry such as Draft objects or sketches
-   3D objects are exported as a flattened 2D view
-   Compound objects are exported as blocks
-   texts
-   colors are mapped from objects RGB colors to autocad color index (ACI). Black will always be \"by layer\"
-   layers are mapped from group names. When groups are nested, the deepest group gives the layer name.
-   dimensions, which are exported with \"Standard\" dimstyle.


<div class="mw-translate-fuzzy">

### Установка


</div>


<div class="mw-translate-fuzzy">

**Внимание!** По причине лицензирования библиотеки импорта и экспорта DXF более не входят в исходный код FreeCAD. Поэтому данные библиотеки должны быть установлены пользователем, после установки FreeCAD. Это может быть сделано автоматически или вручную.


</div>

## Preferences

For more information see: [Import Export Preferences](Import_Export_Preferences.md).

## Scripting


**See also:**

[Draft API](Draft_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

You can export elements to DXF by using the following function: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Example: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```


<div class="mw-translate-fuzzy">


</div>


 

[Category:User Documentation/ru](Category:User_Documentation/ru.md) [Category:File Formats{{\#translation:}}](Category:File_Formats.md)
