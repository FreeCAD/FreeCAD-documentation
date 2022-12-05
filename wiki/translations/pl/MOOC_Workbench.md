# <img alt="" src=images/MOOC_workbench_icon.svg  style="width:240px;">  MOOC Workbench/pl
*align=center|The FreeCAD MOOC External Workbench Icon*

## Overview


{{TOCright}}

The MOOC Workbench is an [external workbench](External_workbenches.md) with which you can follow interactive tutorials and make evaluation of your work directly within the FreeCAD interface. The MOOC workbench offers 2 tools: interactive tutorials and evaluations.

-   Currently only in French (and hard-coded).
-   Only compatible with FreeCAD Py3 and Qt5 (PySide2)
-   LGPLv2 (or similar) code funded by Europe through IMT and EESAB.
-   Modular: This workbench was created with the intention that the addition of tutorials and evaluations was modular. In other words, one has to add a tutorial in the **lessons** folder or an evaluation in the **exercises** folder to show up in the respective tool.

### Interactive

**Interactive** tutorials (AKA <img alt="" src=images/MOOC_Player.svg  style="width:24px;"> Player) are step-by-step guided exercises with objective checks. It launches directly into FreeCAD and allows you to advance one step at a time of modeling of an object. The user has a text, a video and above all a check that the objectives have been achieved.

<img alt="" src=images/MOOC_Player_Dialog_Context.png  style="width:1024px;"> 
*align=center|MOOC Player Dialog within FreeCAD GUI* ![](images/MOOC_Player_Dialog.png ) 
*MOOC Player Dialog close up*

### Evaluations

**Evaluations** (AKA <img alt="" src=images/MOOC_Grader.svg  style="width:24px;"> Grader) consist of a small program that checks certain criteria of a FreeCAD document, for example, the presence of a part body, a sketch or the final volume. <img alt="" src=images/MOOC_Grader_Dialog.png  style="width:1024px;"> 
*align=center|The MOOC Grader Dialog*

## Installation

This workbench can be installed from the [Addon Manager](Std_AddonMgr.md). For manual installation see [Installing more workbenches](Installing_more_workbenches.md).

## Limitations

ATM this workbench is only available in the French language.

## Technical Details 

From a technical point of view, the workbench is composed of:

-   an \"API\" that contains the code that analyzes the document (**MoocChecker.py**)
-   the code that executes the tutorials in the \"lessons\" folder (**MoocPlayer.py**)
-   the code that executes the evaluations in the \"exercises\" folder (**MoocGrader.py**)

## Roadmap

-   internationalization of the workbench
-   Integration of videos in FreeCAD (PySide2.QtWebEngineWidgets?)
-   request the integration of the workbench in the list of the addon manager DONE

## Links

-   Source code hosted on Framagit: [1](https://framagit.org/freecad-france/mooc-workbench)
-   Official complete [2](https://framagit.org/freecad-france/mooc-workbench#mooc-workbench)
-   Discussion threads: [English](https://forum.freecadweb.org/viewtopic.php?f=9&t=37584) / [French](https://forum.freecadweb.org/viewtopic.php?f=12&t=37322)

## External workbenches 

FreeCAD workbenches are easy to program in [Python](Python.md), there are therefore many people developing additional workbenches outside of the FreeCAD main developers.

The [external workbenches](external_workbenches.md) page has some information and tutorials on some of them, and the [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) project aims at gathering them and making them easily installable from within FreeCAD.

New workbenches are in development, stay tuned!



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > MOOC Workbench/pl
