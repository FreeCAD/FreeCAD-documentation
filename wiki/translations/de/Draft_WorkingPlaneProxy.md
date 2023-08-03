---
 GuiCommand:
   Name: Draft WorkingPlaneProxy
   Name/de: Draft ArbeitsebenenProxy
   MenuLocation:  Dienstprogramme , Arbeitsebenen-Proxy erstellen
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   SeeAlso: Draft_SelectPlane/de
---

# Draft WorkingPlaneProxy/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:24px;"> **Draft ArbeitsebenenProxy** erstellt einen Stellvertreter der Arbeitsebene, um die aktuelle [Draft Arbeitsebene](Draft_SelectPlane/de.md) zu sichern. Ein Arbeitsebenen-Proxy kann zum schnellen wiederherstellen einer Arbeitsebene verwendet werden. Kameraposition und Sichtbarkeit der Objekte in der [3D-Ansicht](3D_view/de.md) werden auch im Arbeitsebenen-Proxy gespeichert und können, [wahlweise](#Eigenschaften.md), auch wiederhergestellt werden.

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Drei Proxies der Bearbeitungsebene mit unterschiedlichen Ausrichtungen und Versätzen*



## Anwendung

1.  Wahlweise die [Arbeitsebene](Draft_SelectPlane/de.md) wechseln.
2.  Wahlweise die [3D-Ansicht](3D_view/de.md) wechseln.
3.  Wahlweise die Sichtbarkeit von Objekten im Dokument ändern.
4.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_WorkingPlaneProxy.svg" width=16px> [Arbeitsebenen-Proxy erstellen](Draft_WorkingPlaneProxy/de.md)** drücken.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_WorkingPlaneProxy.svg" width=16px> Arbeitsebenen-Proxy erstellen** auswählen.
5.  Ein Arbeitsebenen-Proxy wird erstellt.
6.  Zum Ausrichten einer [Arbeitsebene](Draft_SelectPlane/de.md) an einem Arbeitsebenen-Proxy klickt man doppelt auf den Arbeitsebenen-Proxy in der [Baumansicht](Tree_view/de.md) oder verwendet ihn mit dem Befehl [Draft EbeneAuswählen](Draft_SelectPlane/de.md).



## Kontextmenü

Für ein Draft Arbeitsebenen-Proxy sind diese zusätzlichen Optionen im Kontextmenü der [Baumansicht](Tree_view/de.md) vorhanden:

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write camera position**: aktualisiert die {{PropertyView/de|View Data}} des Arbeitsebenen-Proxys mit den aktuellen Kameraeinstellungen der [3D-Ansicht](3D_view/de.md).

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write objects state**: aktualisiert die {{PropertyView/de|Visibility Map}} des Arbeitsebenen-Proxys mit den aktuellen Sichtbarkeiten der Objekte im Dokument.



## Hinweise

-   Arbeitsebenen-Proxies können [verschoben](Draft_Move/de.md) und [gedreht](Draft_Rotate/de.md) werden, wie jedes andere Objekt auch. Mit aktiviertem <img alt="" src=images/Draft_Snap_Center.svg  style="width:16px;"> [Draft MittelpunktEinrasten](Draft_Snap_Center/de.md) wird auf dem Punkt seiner {{PropertyData/de|Placement}} eingerastet.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft ArbeitsebenenProxy wird von einem [App FeaturePython](App_FeaturePython.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Basis}}

-    **Placement|Placement**: specifies the position of the working plane proxy in the [3D view](3D_view.md). See [Placement](Placement.md).

-    **Shape|Shape|Hidden**: specifies the shape of the working plane proxy.



### Ansicht


{{TitleProperty|Basis}}

-    **Line Color|Color**: specifies the color of all elements of the working plane proxy.

-    **Line Width|Float**: specifies the line width of the axes and arrow symbols.

-    **Restore State|Bool**: specifies if the **Visibility Map** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Restore View|Bool**: specifies if the **View Data** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Transparency|Percent**: specifies the transparency of the face of the working plane proxy.

-    **View Data|FloatList**: specifies the camera position and settings.

-    **Visibility Map|Map|Hidden**: specifies the visibility state of objects.


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the arrow symbols displayed at the tip of the three axes.

-    **Display Size|Length**: specifies the length and width of the working plane proxy.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft Arbeitsebenen-Proxys verwendet man die Methode `make_workingplaneproxy` des Draft-Moduls.

Ist der Arbeitsbereich [Draft](Draft_Workbench/de.md) aktiv, besitzt FreeCADs Anwendungsobjekt (application object) eine Eigenschaft `DraftWorkingPlane`, die die aktuelle Arbeitsebene speichert. Die Positionierung {{Incode|Placement}} aus der Methode {{Incode|getPlacement}} des `DraftWorkingPlane`-Objekts kann zur Erstellung eines ausgerichteten Arbeitsebenen-Proxys verwendet werden. Die Positionierung {{Incode|Placement}} kann wiederum zu erneuten Ausrichten der Arbeitsebene verwendet werden.


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

workplane = App.DraftWorkingPlane
place = workplane.getPlacement()

proxy = Draft.make_workingplaneproxy(place)
proxy.ViewObject.DisplaySize = 3000
proxy.ViewObject.ArrowSize = 200

axis2 = App.Vector(1, 1, 1)
point2 = App.Vector(3000, 0, 0)
place2 = App.Placement(point2, App.Rotation(axis2, 90))

proxy2 = Draft.make_workingplaneproxy(place2)
proxy2.ViewObject.DisplaySize = 3000
proxy2.ViewObject.ArrowSize = 200

workplane.setFromPlacement(proxy2.Placement, rebase=True)
Gui.Snapper.setGrid()

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WorkingPlaneProxy/de
