---
- GuiCommand:

   Name: Std ViewDockUndockFullscreen
   Empty: 1
   MenuLocation: View -> Document window -> Docked/Undocked
   Workbenches: All
   Shortcut: **V** **D** / **V** **U**
   SeeAlso: Std_ViewFullscreen, Std_MainFullscreen
---

# Std ViewDockUndockFullscreen/ro

## Introduction

[3D views](3D_view.md) can be undocked from the main [FreeCAD interface](Interface.md) and moved to a different display for example.

![](images/FinestraNonAgganciata.png ) 
*An undocked 3D view*

## Docked

### Description

The **Docked** menu option docks the active [3D view](3D_view.md) inside the main FreeCAD interface.

### Usage

1.  Activate an undocked 3D view.
2.  There are several ways to invoke the option:
    -   If there are no docked 3D views: select the **View → Document window → Docked** option from the menu.
    -   Select the **Document window → Docked** option from the 3D view context menu.
    -   Use the keyboard shortcut: **V** then **D**.

## Undocked

### Description 

The **Undocked** menu option undocks the active [3D view](3D_view.md) from the main FreeCAD interface.

### Usage 

1.  Activate a docked 3D view.
2.  There are several ways to invoke the option:
    -   Select the **View → Document window → Undocked** option from the menu.
    -   Select the **Document window → Undocked** option from the 3D view context menu.
    -   Use the keyboard shortcut: **V** then **U**.

## Notes

-   Multiple 3D views for the same document can be created with the [Std ViewCreate](Std_ViewCreate.md) command.
-   3D views can also be docked and undocked with the [Std ViewFullscreen](Std_ViewFullscreen.md) command.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewDockUndockFullscreen/ro
