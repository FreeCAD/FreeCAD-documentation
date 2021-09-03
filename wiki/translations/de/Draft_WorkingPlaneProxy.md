---
- GuiCommand:/de
   Name:Draft WorkingPlaneProxy
   Name/de:Entwurf ArbeitsEbeneProxy
   MenuLocation:Entwurf → Dienstprogramme → Erstelle Arbeitsebenen Proxy
   Workbenches:[Entwurf](Draft_Module/de.md), [Architektur](Arch_Module/de.md)
   SeeAlso:[Entwurf WähleEbene](Draft_SelectPlane/de.md)
---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Dieser Befehl platziert ein Ebenen Proxy Objekt, ausgerichtet auf die aktuelle [Arbeitsebene](Draft_SelectPlane/de.md).


</div>

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Drei Proxies der Bearbeitungsebene mit unterschiedlichen Ausrichtungen und Versätzen*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Stelle sicher, dass die [Arbeitsebene](Draft_SelectPlane/de.md) so eingestellt ist, wie Du willst.
2.  Dann gehe zum Menü **Draft → Dienstprogramme → <img src="images/Draft_WorkingPlaneProxy.svg" width=16px> [Arbeitsebenen Proxy erstellen](Draft_WorkingPlaneProxy/de.md)**.


</div>

## Context menu 

For a Draft WorkingPlaneProxy these additional options are available in the [Tree view](Tree_view.md) context menu:

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write camera position**: updates the **View Data** property of the working plane proxy with the current [3D view](3D_view.md) camera settings.

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write objects state**: updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## Notes


<div class="mw-translate-fuzzy">

## Hinweise

-   Die im Proxy Objekt gespeicherte Arbeitsebene kann durch einen Doppelklick auf das Objekt in der Strukturansicht oder durch Auswahl des Proxy Objekts und Verwendung der **<img src="images/Draft_SelectPlane.svg" width=16px> [Entwurf WähleEbene](Draft_SelectPlane/de.md)** klicken.
-   Die Position der Kamera wird bei der Erstellung im Proxy Objekt gespeichert. Diese Position kann jederzeit aktualisiert werden: zoomen, schwenke und drehe die Ansicht nach Belieben, klicke dann mit der rechten Maustaste auf das Proxy Objekt in der Baumansicht und wähle **<img src="images/Draft_SelectPlane.svg" width=16px> Kameraposition schreiben**.
-   Der Sichtbarkeitsstatus aller Objekte wird bei der Erstellung ebenfalls im Proxy Objekt gespeichert. Dieser Zustand kann jederzeit aktualisiert werden: Setze die Eigenschaft **Sichtbarkeit** der Objekte je nach Wunsch auf `True` oder `False`, klicke dann mit der rechten Maustaste auf das Proxy Objekt in der Baumansicht und wähle **<img src="images/Draft_SelectPlane.svg" width=16px> Objektzustand schreiben**.
-   Ebenen Proxys können wie jedes andere Objekt verschoben und gedreht werden, so dass sie die gewünschte Arbeitsebene definieren. Ihr optisches Erscheinungsbild kann auch im [Eigenschafteneditor](Property_editor/de.md) verändert werden.


</div>

## Eigenschaften

See also: [Property editor](Property_editor.md).

A Draft WorkingPlaneProxy object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Placement|Placement**: specifies the position of the working plane proxy in the [3D view](3D_view.md). See [Placement](Placement.md).

-    **Shape|Shape|Hidden**: specifies the shape of the working plane proxy.

### View


{{TitleProperty|Arch}}

-    **Arrow Size|Length**: specifies the size of the arrow symbols displayed at the tip of the three axes.

-    **Display Size|Length**: specifies the length and width of the working plane proxy.


{{TitleProperty|Base}}

-    **Line Color|Color**: specifies the color of all elements of the working plane proxy.

-    **Line Width|Float**: specifies the line width of the axes and arrow symbols.

-    **Restore State|Bool**: specifies if the **Visibility Map** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Restore View|Bool**: specifies if the **View Data** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Transparency|Percent**: specifies the transparency of the face of the working plane proxy.

-    **View Data|FloatList**: specifies the camera position and settings.

-    **Visibility Map|Map|Hidden**: specifies the visibility state of objects.

## Skripten


<div class="mw-translate-fuzzy">


**Siehe auch:**

[Entwurf API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Arbeitsebenen Proxyobjekte können in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit der folgenden Funktion benutzt werden:


</div>


<div class="mw-translate-fuzzy">

-   Erzeugt ein `WPProxy` Objekt aus der gegebenen `Platzierung`, die ein `FreeCAD.Placement` ist.
    -   Eine Platzierung wird durch einen Basispunkt, gegeben durch seinen `FreeCAD.Vector`, und eine `FreeCAD.Rotation` definiert.


</div>


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


<div class="mw-translate-fuzzy">





</div>


 
