---
- GuiCommand:
   Name:Ship CreateShip
   MenuLocation:Ship design - Create a new ship
   Workbenches:[Ship](Ship_Workbench.md)|
   Shortcut:
   SeeAlso:
---

# Ship CreateShip/es

## Descripción

Create a New Ship or new Ship Instance.

Ship works over **Ship entities**, that must be created on top of provided geometry. Geometry must be a solid, or set of solids.The following criteria must be taken into account:

-   All hull geometry must be provided (including symmetric bodies).
-   Starboard geometry must be included at negatives *y* domain.
-   Origin (0,0,0) point is the **Midship section** (Midpoint between after and forward perpendicular) and **base line** intersection.

![](images/FreeCAD-Ship-SignCriteria.jpg ) 
*Ship sign criteria*

## Uso

In order to create a **Ship instance** (in other words, a New Ship), select the hull solid geometry and invoke **Ship design → <img src="images/Ship_CreateShip.svg" width=16px> Create a new ship**.

The task panel and a free-surface annotation in the [3D view](3D_view.md) are shown. The annotation is temporary and will be removed when you close the tool, so don\'t worry about that.

Most relevant ship data must be introduced (Ship uses a progressive data introduction system, so basic operations can be performed knowing only basic ship data, more information is needed as the operations become more complex).

## Ship data 

Main dimensions must be introduced here:

-   Length: Length between perpendiculars.
-   Beam: Total ship beam.
-   Draft: Design draft.

![](images/FreeCAD-Ship-S60ShipCreationFront.png ) 
*Length annotations*

Usually the Length between perpendiculars depends on design draft, so if you don\'t know what is the length of your ship you can set draft, and fit length in order to get bow and draft intersection.

![](images/FreeCAD-Ship-S60ShipCreationSide.png ) 
*Beam annotations*

Same process is valid for Beam fit. Note that the requested value is the total beam, but just the annotation on starboard side is shown.

When you press **Accept** button, a new Ship instance named **Ship** is created at *Tags & Attributes* dialog. The geometry is not needed anymore, so feel free to hide or remove it.

## Tutoriales

-   [FreeCAD-Ship s60 tutorial ](FreeCAD-Ship_s60_tutorial.md)
-   [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship CreateShip/es
