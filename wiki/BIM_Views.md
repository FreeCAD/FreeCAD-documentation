---
 GuiCommand:
   Name: BIM Views
   MenuLocation: Manage , Views manager
   Workbenches: BIM_Workbench
---

# BIM Views

## Description

The **BIM views and levels manager** is a dockable window that opens below the normal tree view, that contains all the [Building Parts](Arch_BuildingPart.md) and [Working Plane Proxies](Draft_WorkingPlaneProxy.md) of your model.

The aim of this window is to allow to quickly access your levels and working plane configurations, without the need to navigate through the tree to find them.

 <img alt="" src=images/BIM_views_screenshot.png  style="width:600px;">  
*The BIM views and levels manager*

## Usage

The BIM views manager will show all the levels (building parts) and working plane proxies of your document. It can be docked anywhere in the FreeCAD interface or be left in a standalone window. Building Parts will also show their level (the Z coordinate of their placement).

-   Pressing Ctrl+9 or clicking the **BIM Views** button in the status bar shows or hides the BIM Views manager
-   Clicking any entry selects the corresponding object
-   Double-clicking the height of a level allows you to edit it
-   Double-clicking the name of any object sets the working plane to it, and, if the **Restore View** property of the object is set to True, and a view configuration has been stored in it, that viewpoint is also restored
-   The BIM Views manager has a right-click context menu with the following options:
    -   **Add level** creates a new [level](Arch_BuildingPart.md)
    -   **Add proxy** creates a new [working plane proxy](Draft_WorkingPlaneProxy.md)
    -   **Delete** deletes the selected item
    -   **Toggle on/off** turns a selected level on/off (same as the Space bar)
    -   **Isolate** turns all levels off except the selected one
    -   **Save view position** stores the current view settings in the selected object, allowing to restore it if its **Restore View** property is set to True
    -   **Rename** allows you to rename a selected object



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Views
