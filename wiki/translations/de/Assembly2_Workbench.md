# Assembly2 Workbench/de
**der Arbeitsbereich Assembly2 ist veraltet. Sein Autor hat die Wartung eingestellt; er wird mit FreeCAD-Versions 0.17 und neuer wahrscheinlich nicht mehr funktionieren. Die Informationen dieser Seite werden nicht aktualisiert (und übersetzt); sie werden nur aus historischen Gründen behalten.**


{{Message|Als Alternative siehe [A2plus](A2plus_Workbench/de.md). Dieser Arbeitsbereich ist ein Ableger (fork) von Assembly2, ist aber mit jenem nicht kompatibel. Sind noch alte Modelle vorhanden, die geöffnet werden sollen, bleibt man liber bei FreeCAD 0.16 und Assembly2. Neuere Modelle sollten komplett in A2plus erstellt und geöffnet werden.<br/>

Weiter Möglichkeiten bieten [Assembly3](Assembly3_Workbench/de.md) oder [Assembly4](Assembly4_Workbench/de.md). Diese Arbeitsbereiche wurden auch durch Assembly2 inspiriert, sind aber auch beide nicht mit ihm kompatibel.}}

## Introduction

[Assembly2](Assembly2_Workbench.md) is an assembly workbench for FreeCAD v0.15 with support for importing parts from external files.

As stated by its author [on the forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=16591), it is no longer maintained since 2016, therefore it may have issues with FreeCAD 0.17 and above. The newer and actively maintained [A2plus Workbench](A2plus_Workbench.md) is a good alternative.

![](images/Assembly2_example.jpg )

## Usage

Intended work-flow:

-   each part in the assembly is designed in its own FreeCAD file
-   a separate assembly FreeCAD file is created
-   parts are imported to this assembly file using the Assembly 2 workbench
-   spacial constraints are then added to assemble the imported parts

Features

-   circular edge constraint
-   axial constraint
-   plane constraint
-   part importing
-   updating of parts already imported

Limitations

-   Poor constraint solver which may fail or take excessively long for complicated assemblies
-   undo and other similar features not supported

## References

-   Author: hamish
-   Home page: [Assembly2](https://github.com/hamish2014/FreeCAD_assembly2)
-   Source code on github: [Assembly2](https://github.com/hamish2014/FreeCAD_assembly2)

## Tools

Toolbar

![](images/Assembly2-menu-orizz.png )

Drop down menu

![](images/Assembly2-menu-vert.png )

-   <img alt="" src=images/Assembly2_ImportPart.png  style="width:32px;"> Import a part from another FreeCAD document
-   <img alt="" src=images/Assembly2_UpdatePart.png  style="width:32px;"> Update parts imported into the assembly
-   <img alt="" src=images/Assembly2_Move.png  style="width:32px;"> Move
-   <img alt="" src=images/Assembly2_CircularEdgeConstraint.png  style="width:32px;"> Add circular edge constraint
-   <img alt="" src=images/Assembly2_PlaneConstraint.png  style="width:32px;"> Add plane constraint
-   <img alt="" src=images/Assembly2_AxialConstraint.png  style="width:32px;"> Add axial constraint
-   <img alt="" src=images/Assembly2_AngularConstraint.png  style="width:32px;"> Create an angular constraint between two planes
-   <img alt="" src=images/Assembly2_SphericalSurfaceConstraint.png  style="width:32px;"> Add Spherical surface constraint
-   <img alt="" src=images/Assembly2_DOFAnimation.png  style="width:32px;"> Animate degrees of freedom
-   <img alt="" src=images/Assembly2_Assembly2Constraint.png  style="width:32px;"> Solve Assembly2 constraint
-   <img alt="" src=images/Assembly2_Mux.png  style="width:32px;"> Combine assembly into a single object (use to create a drawing of the assembly, and so on\...)
-   <img alt="" src=images/Assembly2_ListParts.png  style="width:32px;"> Create a parts list from the objects imported using the assembly2 workbench
-   <img alt="" src=images/Assembly2_Ceck.png  style="width:32px;"> Ceck assembly for part overlap/interferance

Other

-   <img alt="" src=images/Assembly2_BoltMultipleCircularEdges.png  style="width:32px;"> Bolt multiple circular edges
-   <img alt="" src=images/Assembly2_FlipConstraint.png  style="width:32px;"> Flip constraint
-   <img alt="" src=images/Assembly2_LockRotation.png  style="width:32px;"> Lock rotation
-   <img alt="" src=images/Assembly2_Preferences.png  style="width:32px;"> Preferences
-   <img alt="" src=images/Assembly2_Assembly2.png  style="width:32px;"> Assembly2 WB icon

## Installation

### Automatic installation 

This workbench can be installed from the [Addon Manager](Std_AddonMgr.md).

### From GitHub 

To use this workbench clone this git repository under your FreeCAD Mod directory, and install the pyside and numpy Python libraries. On a Linux Debian based system such as Ubuntu, installation can be done through BASH as follows


```python
sudo apt-get install git python-numpy python-pyside
mkdir ~/.FreeCAD/Mod
cd ~/.FreeCAD/Mod
git clone https://github.com/hamish2014/FreeCAD_assembly2.git
```

In FreeCAD you will now have a new workbench-entry called \"Assembly 2\". Once installed, use git to upgrade to the latest version through BASH as follows


```python
cd ~/.FreeCAD/Mod/FreeCAD_assembly2
git pull
rm *.pyc
```

Alternatilvely, on an Ubuntu system the freecad-community PPA can be used:


```python
Add ppa:freecad-community/ppa to your software sources
sudo apt-get update
sudo apt-get install freecad-extras-assembly2
```

In Windows

-   download the git repository as ZIP
-   assuming FreeCAD is installed in \"C:\\PortableApps\\FreeCAD 0_15\", go to \"C:\\PortableApps\\FreeCAD 0_15\\Mod\" within Windows Explorer
-   create new directory named \"assembly2\"
-   unzip downloaded repository in \"C:\\PortableApps\\FreeCAD 0_15\\Mod\\assembly2\"

FreeCAD will now have a new workbench-entry called \"Assembly 2\".

Pyside and Numpy are integrated in the FreeCAD 0.15 dev-Snapshots, so these Python packages do not need to be installed individually

To update to the latest version, delete the assembly2 folder and redownload the git repository.

## Links

-   Workbench Wiki:
-   FreeCAD Wiki:
-   FreeCAD Forum: <http://forum.freecadweb.org/viewtopic.php?f=10&t=8577>
-   Tutorials:
-   Videos: [video 1](https://www.youtube.com/watch?v=dhaYJKDk4GI), [video 2](http://youtu.be/ufhyUxQkeC0),
-   Files:
-   Report bugs: Please report bugs at <https://github.com/hamish2014/FreeCAD_assembly2/issues>

## Other useful links 

-   [Animation](http://www.freecadweb.org/wiki/index.php?title=Sandbox:Animation): This Workbench can be used to create sequences of pictures.
-   [ExplodedAnimation](http://www.freecadweb.org/wiki/index.php?title=Sandbox:ExplodedAnimation): FreeCAD workbench to create exploded views and animations of assemblies.
-   [External workbenches](External_workbenches.md)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User%20Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > Assembly2 Workbench/de
