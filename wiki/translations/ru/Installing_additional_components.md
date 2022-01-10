# Installing additional components/ru
{{TOCright}}

# Введение


<div class="mw-translate-fuzzy">

После установки FreeCAD для вашей операционной системы ([Windows](Installing_on_Windows/ru.md), [Linux](Installing_on_Linux.md) или [Mac](Installing_on_Mac/ru.md)) вы можете пожелать установить одного или нескольких из следующих дополнительных компонентов.


</div>

# Файлы помощи 

Офлайн-документация не поставляется со всеми установщиками, но доступна в виде отдельного пакета. См. Страницу [Установка файла справки](Installing_Helpfile/ru.md) для получения дополнительной информации.

# Внешние верстаки 

Кроме стандартных [верстаков](workbenches/ru.md), привязанных к FreeCAD, есть большая коллекция полезных [сторонних верстаков](External_workbenches.md), созданных членами сообщества.

# Стороннее программное обеспечение 

FreeCAD поддерживает некоторые сторонние программные пакеты из коробки. Зачастую вам нужно лишь установить программное обеспечение, и при следующем запуске оно будет автоматически найдено и его можно использовать. В данном разделе представлен список всех таких пакетов ПО, а также некоторой информации о том, где он используется во FreeCAD и где его загрузить.

## Поддержка

### GitPython

_ может использовать эту библиотеку. GitPython включён в установщики FreeCAD для Windows и Mac.

### GraphViz

_.

### OpenCAMLib

_. Насчёт инструкций по установки смотрите страницу [OpenCamLib](OpenCamLib/ru.md).

### OpenSCAD

_ зависит от этого программного обеспечения, а [верстак Mesh](Mesh_Workbench/ru.md) использует его для своих булевых операций. Он так же необходим для импорта файлов SCAD с помощью инструмента [Std Import](Std_Import/ru.md).

## Форматы файлов 

Все программное обеспечение в этом разделе используется инструментами [Импорт](Std_Import/ru.md) или [Экспорт](Std_Export/ru.md).

### CADExchanger

[CADExchanger](https://cadexchanger.com) это комерческое приложение с закрытым исходным кодом для обмена файлами различных форматов файлов САПР. Для использования этого приложения в FreeCAD имеется [внешний верстак](https://github.com/yorikvanhavre/CADExchanger).

### Импортёр DXF 

FreeCAD имеет собственный импортер/экспортер файлов DXF, реализованный на C++. Пока что этот импортер реализует не все функции формата DXF. Для этих функций по-прежнему доступен устаревший импортер и экспортер, написанный на Python. Для него требуется библиотека Python _.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free, but not open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

### IfcOpenShell

_ ({{VersionMinus|0.18}}) и [BIM IfcExplorer](BIM_IfcExplorer/ru.md). IfcOpenShell включен в установщики FreeCAD для Windows и Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) - это библиотека, необходимая для экспорта в формат файла IFCJSON. IFCJSON - это новый формат IFC, который еще не поддерживается многими приложениями.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), также известная как `python-collada`, представляет собой библиотеку Python для чтения и записи документов COLLADA (DAE). Pycollada включён в установщики FreeCAD для Windows и Mac.

## Визуализация

### LuxCoreRender

_ project. Officially it is not supported by the _ page for more information and installation instructions.

### LuxRender

_. In 2013 the project has been rebooted becoming _ may work with the Raytracing Workbench, it might be worth to give it a try. See the [LuxRender](LuxRender.md) page for more information and installation instructions, and the [LuxCoreRender](LuxCoreRender.md) if you want to try a more modern software.

### POVRay

_. Дополнительную информацию и инструкцию по установке смотрите на странице [POV-Ray](POV-Ray/ru.md).

## Конечные элементы 

### CalculiX

_.

### Gmsh

_ и [Mesh FromPartShape](Mesh_FromPartShape/ru.md).

### Элмер

_.

### FEniCS

_.

### Z88

_. Для FreeCAD требуется пакет Z88OS с открытым исходным кодом.

### OpenFOAM

_ [Cfd](Cfd_Workbench/ru.md) и [CfdOF](https://github.com/jaheyns/CfdOF).

# Связанные страницы 

-   [Импорт и экспорт](Import_Export/ru.md)
-   [Настройки импорта и экспорта](Import_Export_Preferences/ru.md)
-   [Сторонние библиотеки](Third_Party_Libraries/ru.md)




_

---
[documentation index](../README.md) > Installing additional components/ru
