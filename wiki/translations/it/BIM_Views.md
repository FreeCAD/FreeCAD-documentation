---
- GuiCommand:Addon/it
   Name:BIM Views
   Name/it:Viste BIM
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/it.md)
   Addon:BIM
   MenuLocation:Gestione → Viste
---

# BIM Views/it

## Descrizione


<div class="mw-translate-fuzzy">

Il gestore delle viste e dei livelli BIM è una finestra agganciabile che si apre sotto la normale visualizzazione ad albero, che contiene tutte le [Parti di edificio](Arch_BuildingPart/it.md) e tutti i [Piani Proxy](Draft_SetWorkingPlaneProxy/it.md) del modello.


</div>

The aim of this window is to allow to quickly access your levels and working plane configurations, without the need to navigate through the tree to find them.

<img alt="" src=images/BIM_views_screenshot.png  style="width:800px;">

## Utilizzo

The BIM views manager will show all the levels (building parts) and working plane proxies of your document. It can be docked anywhere in the FreeCAD interface or be left in a standalone window. Building Parts will also show their level (the Z coordinate of their placement).

-   Pressing Ctrl+9 or clicking the **BIM Views** button in the lower right corner of the screen shows or hides the BIM Views manager
-   Clicking any entry selects the corresponding object
-   Double-clicking the height of a level allows you to edit it
-   Double-clicking the name of any object sets the working plane to it, and, if the **Restore View** option of the object is turned on, and a view configuration has been stored in it, that viewpoint is also restored
-   Clicking the **Add a new level** button creates a new [level](Arch_BuildingPart.md)
-   Clicking the **Add a new working plane proxy** button creates a new [working plane proxy](Draft_WorkingPlaneProxy.md)
-   Clicking the **Delete** button deletes the selected item
-   Clicking the **Toggle on/off** button turns a selected level on/off (same as the Space bar)
-   Clicking the **Isolate** button turns all levels off except the selected one
-   Clicking the **Save camera position** button stores the current view settings in the selected object, allowing to restore it if its **Restore View** property is set to True
-   Clicking the **Rename** button allows you to rename a selected object


{{BIM Tools navi

}}

[Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [External Command Reference](Category:External Command Reference.md) > BIM Views/it
