---
 GuiCommand:
   Name: Draft AutoGroup
   Name/de: Draft AutoGruppieren
   Empty: 1
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Version: 0.17
   SeeAlso: Draft_Layer/de, Std_Group/de
---

# Draft AutoGroup/de



## Beschreibung

Der Befehl **Draft AutoGruppieren** ändert den aktiven [Draft-Layer](Draft_Layer/de.md) oder [wahlweise](#Einstellungen.md) die aktive [Std Gruppe](Std_Group/de.md) bzw. gruppenartige [Arch](Arch_Workbench/de.md)-Objekte. Neue [Draft-](Draft_Workbench/de.md) und [Arch](Arch_Workbench/de.md)-Objekte werden automatisch auf diesem Layer bzw. in dieser Gruppe eingefügt.

Dieser Befehl war ursprünglich für Gruppen gedacht, daher sein Name, wurde aber in FreeCAD-Version 0.19 überarbeitet als ein Layer-System eingeführt wurde. Da der Umgang mit Layern jetzt die Standardaufgabe des Befehls ist, liegt der Fokus dieser Seite im folgenden haupfsächlich auf Layern.

![](images/Draft_tray_menu.png ) 
*Das Layer-Menü im Draft-Tray*



## Anwendung

1.  Optionally select the layer you want to make active in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the command:
    -   Press the ![](images/Draft_tray_button_layer.png ) button in the [Draft Tray](Draft_Tray.md). This button can look different. If there is an active layer it will show the name of the layer and a layer icon with the **Line Color** and **Shape Color** of the layer.
    -   If you have selected a layer: select the **<img src="images/button_right.svg" width=16px> Activate this layer** option from the [Tree view](Tree_view.md) context menu.
3.  If you have not yet selected a layer the layer menu opens. Do one of the following:
    -   Select **None** to work without an active layer.
    -   Select an existing layer to make active.
    -   Select **Add new Layer** to create a new layer. Selecting this option will not change the active layer.
4.  If the active layer was changed the button in the [Draft Tray](Draft_Tray.md) is updated.

## Notes

-   A new [layer](Draft_Layer.md) can also be created by right-clicking the layer container in the [Tree view](Tree_view.md) and selecting the **<img src="images/Draft_NewLayer.svg" width=16px> Add new layer** option from the context menu.
-   If [Draft construction mode](Draft_ToggleConstructionMode.md) is switched on the active [layer](Draft_Layer.md) is ignored.



## Einstellungen

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   This command can optionally also handle groups: **Edit → Preferences... → Draft → General → Include groups in layer list**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

If the [Draft Workbench](Draft_Workbench.md) is active the FreeCADGui application object has a `draftToolBar` property. This `draftToolBar` object has an `autogroup` property, which contains the name of the active autogroup, or is `None` if no autogroup is active. To change the active autogroup use the `setAutoGroup` method of the `draftToolBar` object. To put objects in the active autogroup use the `autogroup` method of the Draft module.


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

layer = Draft.make_layer()
Gui.draftToolBar.setAutoGroup(layer.Name)

Draft.autogroup(polygon1)
Draft.autogroup(polygon2)
Draft.autogroup(polygon3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AutoGroup/de
