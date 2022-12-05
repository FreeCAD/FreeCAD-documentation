# <img alt="Symbol des Arbeitsbereichs ExplodedAssembly" src=images/ExplodedAssembly_workbench_icon.svg  style="width:64px;"> ExplodedAssembly Workbench/de


{{TOCright}}

## Einleitung

Der Arbeitsbereich <img alt="" src=images/ExplodedAssembly_workbench_icon.svg  style="width:24px;"> [ExplodedAssembly](ExplodedAssembly_Workbench/de.md) ist ein externer Arbeitsbereich zum erstellen von Explosionsansichten und Animationen von Baugruppen.

## Funktionsumfang

-   Graphische Erstellung der Explosionsansichten von Baugruppen (ganz ohne Programmieren!)
-   Erstellung einzelner Explosionsansichten von Unterbaugruppen
-   Drehung von Schrauben und Muttern für realistische Montage bzw. Demontage
-   Mit den mitgelieferten HIlfs-Zusammenbauwekzeuge lassen sich Einzelteile zueinander Positionieren
-   Funktion in Arbeit: Erstellung eines Bewegungsablaufs aus Linienzügen und Skizzen

## Referenzen

-   Autor: JMG1
-   Homepage: [ExplodedAssembly](https://github.com/JMG1/ExplodedAssembly)
-   Quellkode auf github: [ExplodedAssembly](https://github.com/JMG1/ExplodedAssembly)

## Werkzeuge

![](images/ExplodedAssembly-menu-orizz.png ) 
*Werkzeugleiste*

![](images/ExplodedAssembly-menu-vert.png ) 
*Menü*

### Standardwerkzeuge

-   <img alt="" src=images/ExplodedAssembly_CreateBoltGroup.png  style="width:32px;"> Create Bolt Group
-   <img alt="" src=images/ExplodedAssembly_CreateSimpleGroup.png  style="width:32px;"> Create Simple Group
-   <img alt="" src=images/ExplodedAssembly_ModifyIndividualObjectTrajectory.png  style="width:32px;"> Modify Individual Object Trajectory
-   <img alt="" src=images/ExplodedAssembly_PlaceBefore.png  style="width:32px;"> Place Before
-   <img alt="" src=images/ExplodedAssembly_ExplodeToSelection.png  style="width:32px;"> Explode To Selection
-   <img alt="" src=images/ExplodedAssembly_Assemble.png  style="width:32px;"> Assemble
-   <img alt="" src=images/ExplodedAssembly_PlayBackwards.png  style="width:32px;"> Play Backwards
-   <img alt="" src=images/ExplodedAssembly_StopAnimation.png  style="width:32px;"> Stop Animation
-   <img alt="" src=images/ExplodedAssembly_PlayForward.png  style="width:32px;"> Play Forward
-   <img alt="" src=images/ExplodedAssembly_Disassemble.png  style="width:32px;"> Disassemble
-   <img alt="" src=images/ExplodedAssembly_TrajectoryVisibility.png  style="width:32px;"> Trajectory Visibility
-   <img alt="" src=images/ExplodedAssembly_AlignToEdge.png  style="width:32px;"> Align To Edge
-   <img alt="" src=images/ExplodedAssembly_Rotate90.png  style="width:32px;"> Rotate 90
-   <img alt="" src=images/ExplodedAssembly_PoinToPoint.png  style="width:32px;"> Poin To Point
-   <img alt="" src=images/ExplodedAssembly_PlaceConcentrically.png  style="width:32px;"> Place Concentrically

### Zusätzliche Werkzeuge 

These tools can be added to a custom toolbar. See [Interface Customization](Interface_Customization.md).

-   <img alt="" src=images/ExplodedAssembly_AnimationCameraEdge.png  style="width:32px;"> Animation Camera Edge
-   <img alt="" src=images/ExplodedAssembly_AnimationCameraFollow.png  style="width:32px;"> Animation Camera Follow
-   <img alt="" src=images/ExplodedAssembly_AnimationCameraManual.png  style="width:32px;"> Animation Camera Manual
-   <img alt="" src=images/ExplodedAssembly_WireTrajectory.png  style="width:32px;"> Wire Trajectory

## Installation

### Automatic installation 

This workbench can be installed from the [Addon Manager](Std_AddonMgr.md).

### From GitHub 

Using git on Ubuntu & Mint:

-   Open the command prompt (terminal) with the keys **Ctrl**+**Alt**+**t**
-   Install git: {{Incode|sudo apt-get install git}}
-   Clone repository: {{Incode|<nowiki>git clone https://github.com/JMG1/ExplodedAssembly ~/.FreeCAD/Mod/ExplodedAssembly</nowiki>}}

That\'s all, the next time you launch FreeCAD the workbench should be available.

To install manually download this repository as ZIP and:

-   For Ubuntu, Mint and similar OS\'s extract it inside: **/home/username/.local/share/FreeCAD/Mod** (<small>(v0.20)</small> ) or **/home/username/.FreeCAD/Mod** ({{VersionMinus|0.19}})
-   For Windows extract it inside: **C:\Users\your_user_name\AppData\Roaming\FreeCAD\Mod**

## Links to ExplodedAssembly Workbench 

-   FreeCAD Forum: <http://forum.freecadweb.org/viewtopic.php?f=24&t=9028>
-   Videos: [1](https://www.youtube.com/watch?v=lzYR7I2h7KQ) [2](https://www.youtube.com/watch?v=t72qdG772Q8&feature=youtu.be)
-   Files: inside the workbench
-   Report bugs: Please report bugs at <https://github.com/JMG1/ExplodedAssembly/issues>

## Other useful links 

-   [Externe Arbeitsbereiche](External_workbenches/de.md)
-   [Makro Rezepte](Macros_recipes/de.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > ExplodedAssembly Workbench/de
