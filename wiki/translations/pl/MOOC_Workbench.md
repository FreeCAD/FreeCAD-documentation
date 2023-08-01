# <img alt="" src=images/MOOC_workbench_icon.svg  style="width:240px;">  MOOC Workbench/pl
*align=center|Ikonka FreeCAD dla zewnętrznego środowiska pracy MOOC*



## Informacje ogólne 




Środowisko pracy MOOC to [zewnętrzne środowisko pracy](External_workbenches/pl.md), za pomocą którego można śledzić interaktywne poradniki i dokonywać oceny swojej pracy bezpośrednio w interfejsie FreeCAD. Środowisko pracy MOOC oferuje 2 narzędzia: interaktywne poradniki i oceny.

-   Obecnie tylko w języku francuskim *(i zakodowane na stałe)*.
-   Kompatybilny tylko z FreeCAD Py3 i Qt5 *(PySide2)*
-   Kod LGPLv2 *(lub podobny)* finansowany przez Europę za pośrednictwem IMT i EESAB.
-   Modułowy: Ten workbench został stworzony z zamiarem, aby dodawanie poradników i ocen było modułowe. Innymi słowy, należy dodać poradnik w folderze **lessons** lub ewaluację w folderze **exercises**, aby pojawiły się w odpowiednim narzędziu.

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
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > MOOC Workbench/pl
