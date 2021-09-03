---
- GuiCommand:Addon/de
   Name:BIM Ansichten
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/de.md)
   Addon:BIM
   MenuLocation:Verwalten → Ansichten
---

## Beschreibung

Der BIM Ansichten und Ebenenmanager ist ein andockbares Fenster, das sich unterhalb der normalen Baumansicht öffnet und alle [GebäudeTeile](Arch_BuildingPart/de.md) und [Arbeitsebenen Proxies](Draft_WorkingPlaneProxy/de.md) deines Modells enthält.

Das Ziel dieses Fensters ist es, einen schnellen Zugriff auf Ihre Ebenen und Arbeitsebenen Konfigurationen zu ermöglichen, ohne dass du durch den Baum navigieren musst, um sie zu finden.

<img alt="" src=images/BIM_views_screenshot.png  style="width:800px;">

## Anwendung

Der BIM Ansichtenverwalter zeigt alle Ebenen (Gebäudeteile) und Arbeitsebenen Proxys deines Dokuments an. Er kann an einer beliebigen Stelle in der FreeCAD Oberfläche angedockt oder in einem eigenständigen Fenster belassen werden. Gebäudeteile zeigen auch ihre Ebene an (die Z Koordinate ihrer Positionierung).

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

[Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
