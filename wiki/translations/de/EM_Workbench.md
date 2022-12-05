# <img alt="EM Arbeitsbereichssymbol" src=images/EMWorkbench.svg  style="width:64px;"> EM Workbench/de


{{TOCright}}

## Einleitung

Der Arbeitsbereich EM (ElectroMagnetic) stellt das CAD front-end interface für einige open source free solvers zur Verfügung. Aktuell unterstützt es den 3D magnetoquasistatic impedance solver [FastHenry](https://www.fastfieldsolvers.com/software.htm#fasthenry2) (d.h. Induktivitäts- und Widerstandsermittlung für \"niedrige\" Frequenzen). Unterstützung für den 3D electrostatic capacitance solver [FasterCap](https://www.fastfieldsolvers.com/software.htm#fastercap) ist in Arbeit.

<img alt="" src=images/Screenshot_EM_window.png  style="width:600px;">

## Installation

Der [Arbeitsbereich EM](EM_Workbench/de.md) ist ein [externer Arbeitsbereich](External_workbenches/de.md), der mit FreeCADs <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden kann. Dies kann über den Menüeintrag **Werkzeuge → Addon-Manager** erfolgen.

Die Löser für elektromagnetische Zusammenhänge FastHenry2 und FasterCap müssen separat installiert werden. Ihre Binärcodes und auch die Quelldateien sind frei erhältlich von [FastFieldSolvers](https://www.fastfieldsolvers.com).

## Anwendung

### FastHenry

FastHenry is a software for computing the frequency-dependant self and mutual inductances and resistances of a generic tridimensional conductive structure, in the magnetoquasistatic approximation. It can also generate Spice-compatible, multiple-frequency equivalent-circuit models.

Knowledge of FastHenry is a pre-condition for the proficient usage of the ElectroMagnetic Workbench for FastHenry. We suggest you to read the original [FastHenry User\'s manual](https://www.fastfieldsolvers.com/documentation.htm) and play a bit with the sample files that are provided with the installation.

### FasterCap

FasterCap is a powerful three- and two-dimensional capacitance extraction program.

Knowledge of FasterCap is a pre-condition for the proficient usage of the ElectroMagnetic Workbench for FasterCap. We suggest you to read the original [FasterCap help file](https://www.fastfieldsolvers.com/documentation.htm) and play a bit with the sample files that are provided with the installation.

## FastHenry-Werkzeuge 

These are tools used to interface with FastHenry:

-   <img alt="" src=images/EM_FHNode.svg  style="width:32px;"> [FHNode](EM_FHNode.md): Creates a FastHenry Node object
-   <img alt="" src=images/EM_FHSegment.svg  style="width:32px;"> [FHSegment](EM_FHSegment.md): Creates a FastHenry Segment object
-   <img alt="" src=images/EM_FHPath.svg  style="width:32px;"> [FHPath](EM_FHPath.md): Creates a FastHenry Path object
-   <img alt="" src=images/EM_FHPlane.svg  style="width:32px;"> [FHPlane](EM_FHPlane.md): Creates a FastHenry uniform conductive Plane object
-   <img alt="" src=images/EM_FHPlaneHole.svg  style="width:32px;"> [FHPlaneHole](EM_FHPlaneHole.md): Creates a FastHenry uniform conductive plane Hole object
-   <img alt="" src=images/EM_FHPlaneAddRemoveNodeHole.svg  style="width:32px;"> [FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole.md): Add or Remove a Node or a Hole from/to a conductive plane
-   <img alt="" src=images/EM_FHEquiv.svg  style="width:32px;"> [FHEquiv](EM_FHEquiv.md): Creates a FastHenry node Equivalence object
-   <img alt="" src=images/EM_FHPort.svg  style="width:32px;"> [FHPort](EM_FHPort.md): Creates a FastHenry Port object
-   <img alt="" src=images/EM_FHSolver.svg  style="width:32px;"> [FHSolver](EM_FHSolver.md): Creates a FastHenry Solver object
-   <img alt="" src=images/EM_FHInputFile.svg  style="width:32px;"> [FHInputFIle](EM_FHInputFile.md): Creates a FastHenry Input File

## FasterCap-Werkzeuge 

At present, FasterCap is supported via some Macros in the **Export_mesh.py** file available in the [ElectroMagnetic Workbench GitHub source code](https://github.com/ediloren/EM-Workbench-for-FreeCAD).

## API

Die EM-Werkzeug können in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch Verwendung der EM-API genutzt werden:

## Tutorien

Some video tutorials are available for the EM Workbench beta versions:

-   [FreeCAD ElectroMagnetic Workbench tutorial - Getting started](https://www.youtube.com/watch?v=h6Pp-_ovLZM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 1](https://www.youtube.com/watch?v=5pSzPizw4e8)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 2](https://www.youtube.com/watch?v=BeBNtfH25rM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 3](https://www.youtube.com/watch?v=BtgdJOf-ql0)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 1](https://www.youtube.com/watch?v=CRqDuEtbdds)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 2](https://www.youtube.com/watch?v=slsLdLoF2OI)


{{EM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [EM](Category_EM.md) > EM Workbench/de
