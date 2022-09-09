# Release notes 1.0/ru
**FreeCAD 1.0 is under development, there is no expected released date yet.**


{{Message|
Are features missing? Mention them in the [https   *//forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Release notes for v1.0] forum thread.

See [Help FreeCAD](Help_FreeCAD.md) for ways to contribute to FreeCAD.
}}


{{Message|All images on this page must use the **_relnotes_1.0** suffix}}


{{TOCright}}

**FreeCAD 0.10** был выпущен **DD MM 2023**, скачать его можно со [страницы загрузок](Download/ru.md). Текущая страница содержит описание новых возможностей и изменений.

Older FreeCAD release notes can be found in the [Feature list](Feature_list#Release_notes.md).

Placeholder for an eye-catching image selected by the admins from the [user showcases forum](https   *//forum.freecadweb.org/viewforum.php?f=24).

## Основные

## Интерфейс пользователя 

### Планируемые улучшения интерфейса пользователя 

## Ядро системы и API 

### Ядро

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### New Python API 


<div class="mw-collapsible-content">

-   *ShapeFix\_EdgeConnectPy*   * Root class for fixing operations. [commit 4d4adb93](https   *//github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix\_EdgePy*   * Fixing invalid edge. [commit 4089cbfb](https   *//github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix\_FaceConnectPy*   * Rebuilds connectivity between faces in shell. [commit a0eb2e9d](https   *//github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix\_FacePy*   * Class for fixing operations on faces. [commit b6cd635c](https   *//github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix\_FixSmallFacePy*   * Class for fixing operations on faces. [commit 4c2946c8](https   *//github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix\_FixSmallSolidPy*   * Fixing solids with small size. [commit b70d8d37](https   *//github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix\_FreeBoundsPy*   * Intended to output free bounds of the shape. [commit 1ee1aee1](https   *//github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix\_RootPy*   * Root class for fixing operations. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_ShapePy*   * Class for fixing operations on shapes. [commit 87db9dcc](https   *//github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix\_ShapeTolerancePy*   * Modifies tolerances of sub-shapes (vertices, edges, faces). [commit 125d5b63](https   *//github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix\_ShellPy*   * Root class for fixing operations. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_SolidPy*   * Root class for fixing operations. [commit 8d568793](https   *//github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix\_SplitCommonVertexPy*   * Class for fixing operations on shapes. [commit 4b44c54c](https   *//github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix\_SplitToolPy*   * Tool for splitting and cutting edges. [commit bbecc3f2](https   *//github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix\_WireframePy*   * Provides methods for fixing wireframe of shape. [commit 6843a461](https   *//github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix\_WirePy*   * Class for fixing operations on wires. [commit 94f6279a](https   *//github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix\_WireVertexPy*   * Fixing disconnected edges in the wire. [commit 8c6ffc99](https   *//github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>

#### Изменения в Python API 


</div>

## Менеджер Дополнений 

## Архитектурный Верстак (Arch) 

## Верстак Draft 

### Планируемые улучшения верстака Draft 

## Верстак FEM 

### Планируемые улучшения верстака FEM 

## Экспортирование

## Верстак Mesh 

### Планируемые улучшения верстака Mesh 

## Верстак OpenSCAD 

## Верстак Part 

### Планируемые улучшения верстака Part 

## Верстак PartDesign 

### Планируемые улучшения верстака PartDesign 

## Верстак Path 

-   Camotics integration. If camotics (version 1.2.2 or later) is installed, a new icon will be added to the Path toolbar. Select a Path Job and press the button to open the Camotics dialog. Then drag the slider to generate a simulated solid at any point in the job. You can also launch the full camotics application to run the animated simulaton. This results in a silent post-processing of the job and creation of a camotics project file. [Pull request \#6637](https   *//github.com/FreeCAD/FreeCAD/pull/6637)

-   Additional substitution strings for automatic output naming. If output is being split into multiple files, the filenames can automatically substitute the toolcontroller label, WCS, or operation label. This is in addition to the other existing substitution strings like date, job name, etc.

## Plot module 

## Верстак Sketcher 

### Планируемые улучшения Sketcher 

## Верстак Spreadsheet 

### Планируемые улучшения электронных таблиц 

## Верстак TechDraw 

### Планируемые улучшения верстака TechDraw 

## Web

## Внешние верстаки 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Сборка

Since this release FreeCAD can only be compiled using Qt 5.x and Python 3.x. The lowest supported Python version is 3.8 according to the [FreeCAD 1.0 development goals](FreeCAD_1.0_Development_Cycle.md).

To compile FreeCAD see the instructions for [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) and [MacOS](Compile_on_MacOS.md).

The supported operating systems are   *

-   Windows 7, 8, 10 and 11
-   Linux Ubuntu Focal Fossa (20.04) and newer
-   MacOS   * 10.12 Sierra or newer

### Известные Ограничения 

### 32bit Windows 

Since FreeCAD 0.19 we no longer officially support 32bit Windows. FreeCAD might work on these systems, but no support is given.

### Remote Desktop under Windows 

Depending on the OpenGL graphics capabilities of a computer, it might be that one encounters a crash when running FreeCAD via remote desktop. To fix this upgrade your OpenGL driver. Only if this doesn\'t help   *

-   Download [this](https   *//downloads.fdossena.com/geth.php?r=mesa64-latest) OpenGL library for 64bit Windows and extract it.
-   Rename the DLL file to *opengl32sw.dll* and copy it to the *bin* subfolder of FreeCAD\'s installation folder (overwrite the existing DLL there).

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/ru