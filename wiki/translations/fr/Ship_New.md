---
- GuiCommand:/fr   Name:Ship New‏‎   Name/fr:Ship New‏‎    MenuLocation:Ship design → Create a new ship   |Workbenches:[[Ship Workbench/fr   Ship]]|Shortcut:   SeeAlso:---


</div>

## Description

Create a New Ship or new Ship Instance.

## Usage

In order to create a **Ship instance** (in other words, a New Ship), select s60 geometry and execute the **ship creation tool** {{MenuCommand|Ship design → Create a new ship}}

Creating ship task dialogue and some annotations at [3D view](3D_view.md) will shown. The annotations will removed when you close Ship creation tool, so don\'t worry about this.

Most relevant ship data must be introduced (Ship uses a progressive data introduction system, so basic operations can be performed knowing only basic ship data, more information is needed as the operations become more complex).

## Ship data {#ship_data}

Main dimensions must be introduced here:

-   Length: Length between perpendiculars, 25.5 m for this ship.
-   Beam: Total ship beam, 3.389 m for this ship.
-   Draft: Design draft, 1.0 m for this ship.

![\|Front view annotations](images/FreeCAD-Ship-S60ShipCreationFront.png ) *Length annotations*

Usually the Length between perpendiculars depends on design draft, so if you don\'t know what is the length of your ship you can set draft, and fit length in order to get bow and draft intersection.

![\|Side view annotations](images/FreeCAD-Ship-S60ShipCreationSide.png ) *Beam annotations*

Same process is valid for Beam fit. Note: that requested value is total beam, but annotation is only referred to starboard half ship.

When you press **Accept** button, a new Ship instance is created called **Ship** at *Tags & Attributes* dialog. We don\'t need geometry anymore, so you can hide it.

Note: From here onward, you must have **Ship** selected before you execute any Ship tool.

## Tutorials

-   [FreeCAD-Ship s60 tutorial ](FreeCAD-Ship_s60_tutorial.md)
-   [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)

\|[Ship Geometries Examples Loader](Ship_Geometries_Examples.md) \|[Lines drawing](Ship_Outline.md) \|[Ship](Ship_Workbench.md) \|IconL=Ship\_Load.svg \|IconC=Workbench\_Ship.svg \|IconR=Ship\_OutlineDraw.svg }}


{{Ship_Tools_navi

}} 
