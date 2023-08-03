---
 GuiCommand:
   Name: OpenSCAD AddOpenSCADElement
   Name/ru: OpenSCAD AddOpenSCADElement
   Workbenches: OpenSCAD_Workbench/ru
   MenuLocation: OpenSCAD -> Add OpenSCAD Element
---

# OpenSCAD AddOpenSCADElement/ru


</div>

## Description


<div class="mw-translate-fuzzy">

#### Описание

Добавьте элемент OpenSCAD, введя код OpenSCAD в панель задач и выполнив двоичный файл OpenSCAD (требуется OpenSCAD)


</div>

Когда выбран «как сетка», OpenSCAD визуализирует сетку.

Каждый раз, когда Добавить в OpenSCAD код выполняется и элементы импортируются.

If OpenSCAD returns successfully, its messages are displayed as warnings in the report window. This will be the case if the path to imported, included and used files is broken. In case of undesired results it is highly recommend to have a look at the report windows, as there might be a lot of other output, created by the importer. If OpenSCAD fails, its messages will be logged as errors.

Libraries should be accessible as usual, whereas example can be reached as stated below.


```python
include <../examples/example001.scad>;
```

would include the first examples also known as the OpenSCAD icon.

## Setup OpenSCAD within FreeCAD 

**Note:** OpenSCAD needs to be installed on your computer before FreeCAD will have this functionality
Install OpenSCAD in the appropriate manner for your operating system. See [the OpenSCAD web site](https://www.openscad.org/) for more information.

FreeCAD needs to be told where to find the OpenSCAD executable:

-   Switch to the <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md) via 
**View → Workbench → OpenSCAD**
-   Open the preferences dialog **Edit → Preferences**
-   Click on \"OpenSCAD\" on the left plane
-   Click on the button labled **...** in **General Settings → General OpenSCAD Settings → OpenSCAD executable** to browse the directory or enter the path (e.g. Ubuntu based Linux distributions `/usr/bin/openscad`) directly into the line input right to the button
-   Close and restart FreeCAD

:   **Result:** A new OpenSCAD icon will appear on the tool bar, and in the OpenSCAD menu, in the FreeCAD OpenSCAD workbench.

Note: It is also possible to add another optional Parameter which controls the maximum sides of a polygon before it is considered a circle (fn).


<div class="mw-translate-fuzzy">

Начиная с FreeCAD версии 0.14, FreeCAD будет искать исполняемый файл OpenSCAD, если вышеупомянутая настройка пуста.


</div>





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD AddOpenSCADElement/ru
