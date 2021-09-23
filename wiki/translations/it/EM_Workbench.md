# EM Workbench/it
 <img alt="" src=images/EMWorkbench.svg  style="width:240px;"> 
*align=center|The FreeCAD ElectroMagnetic External Workbench Icon*

## Introduzione


{{TOCright}}

The ElectroMagnetic (EM) Workbench provides the CAD front-end interface to some open source free solvers. At present it supports the 3D magnetoquasistatic impedance solver [FastHenry](https://www.fastfieldsolvers.com/software.htm#fasthenry2) (i.e. inductance and resistance extraction at \"low\" frequencies). Support for the 3D electrostatic capacitance solver [FasterCap](https://www.fastfieldsolvers.com/software.htm#fastercap) is ongoing.

<img alt="" src=images/Screenshot_EM_window.png  style="width:600px;">

## Installazione

[EM](EM_Workbench/it.md) è un [ambiente esterno](external_workbenches/it.md), che può essere installato da <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md). Questo può essere fatto tramite il menu **Strumenti → Addon Manager**.

I risolutori elettromagnetici FastHenry2 e FasterCap devono essere installati separatamente. I loro codici binari e i sorgenti sono liberamente disponibili in [FastFieldSolvers](https://www.fastfieldsolvers.com).

## Utilizzo

### FastHenry

FastHenry is a software for computing the frequency-dependant self and mutual inductances and resistances of a generic tridimensional conductive structure, in the magnetoquasistatic approximation. It can also generate Spice-compatible, multiple-frequency equivalent-circuit models.

Knowledge of FastHenry is a pre-condition for the proficient usage of the ElectroMagnetic Workbench for FastHenry. We suggest you to read the original [FastHenry User\'s manual](https://www.fastfieldsolvers.com/documentation.htm) and play a bit with the sample files that are provided with the installation.

### FasterCap

FasterCap is a powerful three- and two-dimensional capacitance extraction program.

Knowledge of FasterCap is a pre-condition for the proficient usage of the ElectroMagnetic Workbench for FasterCap. We suggest you to read the original [FasterCap help file](https://www.fastfieldsolvers.com/documentation.htm) and play a bit with the sample files that are provided with the installation.

## Strumenti di FastHenry 

Questi sono gli strumenti utilizzati per interfacciarsi con FastHenry:

-   <img alt="" src=images/EM_FHNode.svg  style="width:32px;"> [FHNode](EM_FHNode/it.md): Crea un oggetto FastHenry Node
-   <img alt="" src=images/EM_FHSegment.svg  style="width:32px;"> [FHSegment](EM_FHSegment/it.md): Crea un oggetto FastHenry Segment
-   <img alt="" src=images/EM_FHPath.svg  style="width:32px;"> [FHPath](EM_FHPath/it.md): Crea un oggetto FastHenry Path
-   <img alt="" src=images/EM_FHPlane.svg  style="width:32px;"> [FHPlane](EM_FHPlane/it.md): Crea un oggetto FastHenry uniform conductive Plane
-   <img alt="" src=images/EM_FHPlaneHole.svg  style="width:32px;"> [FHPlaneHole](EM_FHPlaneHole/it.md): Crea un oggetto FastHenry uniform conductive plane Hole
-   <img alt="" src=images/EM_FHPlaneAddRemoveNodeHole.svg  style="width:32px;"> [FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/it.md): Aggiunge o Rimuove un Node o un Hole da/a un piano conduttivo
-   <img alt="" src=images/EM_FHEquiv.svg  style="width:32px;"> [FHEquiv](EM_FHEquiv/it.md): Crea un oggetto FastHenry node Equivalence
-   <img alt="" src=images/EM_FHPort.svg  style="width:32px;"> [FHPort](EM_FHPort/it.md): Crea un oggetto FastHenry Port
-   <img alt="" src=images/EM_FHSolver.svg  style="width:32px;"> [FHSolver](EM_FHSolver/it.md): Crea un oggetto FastHenry Solver
-   <img alt="" src=images/EM_FHInputFile.svg  style="width:32px;"> [FHInputFIle](EM_FHInputFile/it.md): Crea un file FastHenry Input

## Strumenti di FasterCap 

At present, FasterCap is supported via some Macros in the {{FileName|Export_mesh.py}} file available in the [ElectroMagnetic Workbench GitHub source code](https://github.com/ediloren/EM-Workbench-for-FreeCAD).

## API

The EM tools can be used in [macros](macros.md) and from the [Python](Python.md) console by using the EM API.

## Tutorial

Per le versioni beta di EM Workbench sono disponibili alcune esercitazioni video :

-   [FreeCAD ElectroMagnetic Workbench tutorial - Getting started](https://www.youtube.com/watch?v=h6Pp-_ovLZM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 1](https://www.youtube.com/watch?v=5pSzPizw4e8)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 2](https://www.youtube.com/watch?v=BeBNtfH25rM)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: create a conductive plane, part 3](https://www.youtube.com/watch?v=BtgdJOf-ql0)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 1](https://www.youtube.com/watch?v=CRqDuEtbdds)
-   [FreeCAD ElectroMagnetic WorkBench tutorial: using the path object, part 2](https://www.youtube.com/watch?v=slsLdLoF2OI)

## External workbenches 

FreeCAD workbenches are easy to program in [Python](Python.md), there are therefore many people developing additional workbenches outside of the FreeCAD main developers.

The [external workbenches](external_workbenches.md) page has some information and tutorials on some of them, and the [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) project aims at gathering them and making them easily installable from within FreeCAD.

New workbenches are in development, stay tuned!


{{EM Tools navi

}}  

[Category:External Workbenches](Category:External_Workbenches.md)
