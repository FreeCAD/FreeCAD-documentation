# Raytracing Workbench/ru
<div class="mw-translate-fuzzy">





</div>


**The '''Raytracing Workbench''' is no longer included after version 0.20.<br>
 The external [https://github.com/FreeCAD/FreeCAD-render Render Workbench] should be used instead.**

<img alt="Логотип верстака Raytracing" src=images/Workbench_Raytracing.svg  style="width:128px;">



## Введение




<img alt="" src=images/Workbench_Raytracing.svg  style="width:24px;"> [Верстак Raytracing](Raytracing_Workbench/ru.md) предназначен для создания фотореалистичной изображения ваших моделей с помощью внешних программ рендеринга.

Модуль работает с помощью [шаблонов](Raytracing_templates/ru.md), это файлы проектов, определяющих сцену для вашей объёмной модели. Вы можете поместить свет и геометрию, вроде плоскости земли, и там содержится место для позиции камеры и для указания материалов объектов этой сцены. Проект может быть экспортирован в готовый для рендеринга файл, или отрисован напрямую в FreeCAD.

В настоящее время поддерживаются два визуализатора: [POV-Ray](POV-Ray/ru.md) и [LuxRender](LuxRender/ru.md). Чтобы иметь возможность визуализации из FreeCAD, нужна хотя бы одна из этих программ, установленная и сконфигурированная в Вашей системе. Но даже если ни одного визуализатора не установлено, Вы можете экспортировать файл проекта для визуализации впоследствии.


<div class="mw-translate-fuzzy">

Верстак Raytracing по сути устарел. Ведётся новая разработка [верстака Render](https://github.com/FreeCAD/FreeCAD-render), который предназначен для его замены. Этот верстак полностью запрограммирован на Python, поэтому его гораздо проще расширить, чем текущий верстак, который запрограммирован на C ++. Тем не менее, информация на этой странице в целом полезна для нового верстака, так как оба модуля работают в основном одинаково.


</div>

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">

## Типивой рабочий процесс 

1.  Создайте или откройте прокет FreeCAD, добавьте некоторые твердотельные объекты модулей ([Part](Part_Workbench/ru.md) или [PartDesign](PartDesign_Workbench/ru.md)); сетки пока не поддерживаются.
2.  Создайте проект трассировки лучей (для povray или luxrender).
3.  Выделите объекты, которые Вы хотите добавить в проект трассировки лучей и добавьте их.
4.  Экспортируйте файл проекта или визуализируйте его напрямую.

<img alt="" src=images/Raytracing_Workbench_workflow.svg  style="width:600px;">



*Работа верстака Raytracing; верстак готовит файл проекта из данного шаблона, затем вызывает внешнюю программу для визуализации сцены. Внешний визуализатор может использоваться независимо от FreeCAD.*



## Инструменты



### Инструменты проекта 

Это главные инструменты для экспорта Вашей трёхмерной работы во внешние визуализаторы.

-   <img alt="" src=images/Raytracing_New.svg  style="width:32px;"> [Новый проект Pov-Ray](Raytracing_New/ru.md): Вставляет в документ новый проект PovRay
-   <img alt="" src=images/Raytracing_Lux.svg  style="width:32px;"> [Новый проект LuxRender](Raytracing_Lux/ru.md): Вставляет в документ новый проект LuxRender
-   <img alt="" src=images/Raytracing_InsertPart.svg  style="width:32px;"> [Вставить деталь](Raytracing_InsertPart/ru.md): Вставляет вид объекта Part в проект визуализации
-   <img alt="" src=images/Raytracing_ResetCamera.svg  style="width:32px;"> [Сброс камеры](Raytracing_ResetCamera/ru.md): Сопоставляет позицию камеры проекта трассировки лучей с текущим видом
-   <img alt="" src=images/Raytracing_ExportProject.svg  style="width:32px;"> [Экспортировать проект](Raytracing_ExportProject/ru.md): Экспортирует проект визуализации в файл сцены для отрисовки во внешнем визуализаторе
-   <img alt="" src=images/Raytracing_Render.svg  style="width:32px;"> [Визуализировать](Raytracing_Render/ru.md): Визуализирует проект трассировки лучей во внешнем визуализаторе



### Утилиты

Это вспомогательные инструменты для ручного выполнения особых задач.

-   <img alt="" src=images/Raytracing_WriteView.svg  style="width:32px;"> [Экспорт вида в POV-Ray](Raytracing_WriteView/ru.md): Записывает активный трёхмерный вид с камерой и содержимым в файл povray
-   <img alt="" src=images/Raytracing_WriteCamera.svg  style="width:32px;"> [Экспорт вида в POV-Ray](Raytracing_WriteCamera/ru.md): Экспортирует позицию камеры активного трёхмерного вида в формате POV-Ray в файл
-   <img alt="" src=images/Raytracing_WritePart.svg  style="width:32px;"> [Экспортировать деталь в POV-Ray](Raytracing_WritePart/ru.md): Записывает выделенный объект Part как файл povray



## Настройки

-   <img alt="" src=images/Preferences-raytracing.svg  style="width:32px;"> [Preferences](Raytracing_Preferences/ru.md): Доступные настройки для инструментов Raytracing.

## Учебники

-   [Базовый учебник Raytracing](Raytracing_tutorial/ru.md)
-   [Учебник Raytracing среднего уровня](Tutorial_FreeCAD_POV_ray/ru.md)

## Ручное создание файла povray 

Описанные выше вспомогательные инструменты позволяют экспортировать текущий трёхмерный вид и его содержимое в файл [Povray](http://www.povray.org/). Сначала вы должны загрузить или создать данные САПР и расположить ориентацию трёхмерного вида по своему желанию. Затем выберите из меню трассировки \"Вспомогательные → Экспорт вида\...\".

![](images/FreeCAD_Raytracing.jpg )

У Вас уточнят положение для сохранения итогового файла \*.pov. После этого Вы можете открыть его в [Povray](http://www.povray.org/) и визуализировать: ![](images/Povray.jpg )

Как обычно, в визуализаторе Вы сможете сделать большие и красивые картинки: <img alt="" src=images/Scharniergreifer_render.jpg  style="width:800px;">



## Программирование

Смотрите [Примеры программного интерфейса Raytracing](Raytracing_API_example/ru.md) для информации о создании сцен через программирование.



## Ссылки

### POV-Ray 

-   [POV-Ray страница в данной wiki](POV-Ray.md)
-   <http://www.spiritone.com/~english/cyclopedia/>
-   <http://www.povray.org/>
-   <http://en.wikipedia.org/wiki/POV-Ray>

### LuxRender

-   [LuxRender страница в данной wiki](LuxRender.md)
-   <http://www.luxrender.net/>

### Рендеры, которые могут быть реализованы в будущем 

-   <http://www.yafaray.org/>
-   <http://www.mitsuba-renderer.org/>
-   <http://www.kerkythea.net/>
-   <http://www.artofillusion.org/>

## Exporting to Kerkythea 

Although direct export to the Kerkythea XML-File-Format is not supported yet, you can export your Objects as Mesh-Files (.obj) and then import them in Kerkythea.

-   if using Kerkythea for Linux, remember to install the WINE-Package (needed by Kerkythea for Linux to run)
-   you can convert your models with the help of the mesh workbench to meshes and then export these meshes as .obj-files
-   If your mesh-export resulted in errors (flip of normals, holes \...) you may try your luck with [netfabb studio basic](http://www.netfabb.com/downloadcenter.php?basic=1)

:   Free for personal use, available for Windows, Linux and Mac OSX.
:   It has standard repair tools which will repair you model in most cases.

-   another good program for mesh analysing/repairing is [Meshlab](http://sourceforge.net/projects/meshlab/)

:   Open Source, available for Windows, Linux and Mac OSX.
:   It has standard repair tools which will repair you model in most cases (fill holes, re-orient normals, etc.)

-   you can use \"make compound\" and then \"make single copy\" or you can fuse solids to group them before converting to meshes
-   remember to set in Kerkythea an import-factor of 0.001 for obj-modeler, since Kerkythea expects the obj-file to be in m (but standard units-scheme in FreeCAD is mm)

:   Within WIndows 7 64-bit Kerkythea does not seem to be able to save these settings.
:   So remember to do that each time you start Kerkythea

-   if importing multiple objects in Kerkythea you can use the \"File → Merge\" command in Kerkythea



## Разработка

Эти страницы ссылаются на новую рабочую среду, запрограммированную на Python, предназначенную для замены текущей Raytracing Workbench.

-   [Верстак Render](https://github.com/FreeCAD/FreeCAD-render)
-   [Верстак Render](https://forum.freecadweb.org/viewtopic.php?f=9&t=25933) (только анонс, без дискуссии)
-   [FreeCAD Renderer Workbench improvements](https://forum.freecadweb.org/viewtopic.php?t=39168)


<div class="mw-translate-fuzzy">





</div>


{{Raytracing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete%20Workbenches.md) > [Raytracing](Category_Raytracing.md) > Raytracing Workbench/ru
