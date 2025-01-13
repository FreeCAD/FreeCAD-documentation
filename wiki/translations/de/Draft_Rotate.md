---
 GuiCommand:
   Name: Draft Rotate
   Name/de: Draft Drehen
   MenuLocation: Änderung , Drehen<br>Bearbeiten , Drehen
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **R****O**
   Version: 0.7
   SeeAlso: Draft_SubelementHighlight/de
---

# Draft Rotate/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Rotate.svg  style="width:24px;"> **Draft Drehen** dreht oder kopiert ausgewählte Objekte um ein Zentrum in einem gegebenen Winkel. Die Drehachse steht senkrecht auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) und der Drehwinkel ist relativ zu dieser Ebene. Im Unterelemente-Modus dreht die Anweisung ausgewählte Punkte und Kanten oder Kopien von ausgewählten Kanten von [Draft Linien](Draft_Line/de.md) und [Draft Linienzügen](Draft_Wire/de.md).

Der Befehl kann auf 2D-Formen angewendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, kann aber auch mit vielen Arten von 3D-Objekten benutzt werden, wie denen, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erzeugt wurden.

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;"> 
*Drehen eines Objekts um einen Drehpunkt*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen oder Unterelemente von [Draft Linien](Draft_Line/de.md) oder [Draft Drähten](Draft_Wire/de.md).
2.  Es gibt mehrere Möglichkeiten den Befehl auszuführen:
    -   Die Schaltfläche **<img src="images/Draft_Rotate.svg" width=16px> [Drehen](Draft_Rotate/de.md)** klicken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → <img src="images/Draft_Rotate.svg" width=16px> Drehen** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_Rotate.svg" width=16px> Drehen** auswählen.
    -   Das Tastenkürzel **R** dann **O**.
3.  Wenn noch kein Objekt ausgewählt wurde: ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgaben-Bereich **Drehen** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Wenn Unterelemente ausgewählt wurden: die Check-Box **Unterelemente ändern** aktivieren, um in den Unterelemente-Modus umzuschalten.
6.  Den ersten Punkt, das Zentrum der Drehung, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** anklicken.
7.  Den zweiten Punkt in the [3D-Ansicht](3D_view/de.md) wählen oder einen **Basiswinkel** eingeben.
8.  Den dritten Punkt in der [3D-Ansicht](3D_view/de.md) wählen oder eine **Drehung** eingeben.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **N**drücken oder die Checkbox **Fortsetzen** aktivieren, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet. Dieser Modus ist nur sinnvoll, wenn der Kopieren-Modus aktiviert ist. Abhängig von der Einstellung **Select base objects after copying** werden entweder die Originalobjekte für den nächsten Befehlsaufruf ausgewählt oder die zuletzt erstellten Kopien. Siehe [Einstellungen](#Einstellungen.md).

-    **C**drücken oder die Checkbox **Kopieren** aktivieren, um den Kopieren-Modus umzuschalten. Ist der Kopieren-Modus aktiviert, werden gedrehte Kopien erstellt, anstatt die Originalobjekte zu drehen.

-    **B**drücken oder die Checkbox **Unterelemente anpassen** aktivieren, um den Unterelemente-Modus umzuschalten. Ist der Unterelemente-Modus aktiviert, werden die ausgewählten Unterelemente anstatt der ganzen Objekte verwendet. Die Unterelemente müssen [Draft-Linien](Draft_Line/de.md) oder [Draft-Polylinien](Draft_Wire/de.md) sein.

-   Sind sowohl der Kopieren-Modus als auch der Unterelemente-Modus aktiviert und Kanten von [Draft-Polylinien](Draft_Wire/de.md) ausgewählt, werden neue Polylinien aus diesen Kanten erstellt.

-   Wird **ALT** nach der Eingabe des **Basiswinkel**s gedrückt gehalten, wird ebenfalls der Kopieren-Modus umgeschaltet. Während **ALT** gedrückt gehalten wird, können mehrere Punkte für **Drehung** ausgewählt werden. Sobald **ALT** losgelassen wird, wird der Befehl abgeschlossen und die erstellten Kopien werden angezeigt.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl fertigzustellen.



## Hinweise

-   Ein Objekt, das [angehängt](Part_EditAttachment/de.md) ist, kann nicht mit dem Befehl Drehen gedreht werden. Entweder wird sein {{PropertyData/de|Support}}-Objekt gedreht, oder sein {{PropertyData/de|Attachment Offset}} wird geändert, um es zu drehen.
-   Das Basiswinkelkonzept kann irgendwie verwirrend sein, besonders, da es nur funktioniert, wenn Punkte ausgewählt werden und nicht, wenn der Winkel im Eingabefeld eingegeben wird. Eine Erklärung mit einem Beispiel, wie es funktioniert, findet man in diesem [Forum Beitrag](https://forum.freecad.org/viewtopic.php?p=736674#p736674).



## Einstellungen

Siehe auch: [Editor Einstellungen](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Auswählen der Originalobjekte nach dem Kopieren: **Bearbeiten → Einstellungen... → Draft → Allgemein → Wähle ursprüngliche Objekte nach dem Kopieren aus**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Verwende die `Drehen`-Methode des Entwurfmodules, um Objekte zu drehen.


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```

-    `objectlist`enthält die zu drehenden Objekte. Dies ist entweder ein einzelnes Objekt oder es sind mehrere Objekte.

-    `angle`is der Winkel der Drehung in Grad.

-    `center`ist das Zentrum der Drehung.

-    `axis`ist die Richtung der Drehachse.

-   Wenn `copy` `True` ist, werden Kopien erstellt anstatt die originalen Objekte zu drehen.

-   Eine `rotatedlist` wird mit den gedrehten Originalen oder mit den neuen Kopien gemeldet. Dies ist entweder ein einzelnes Objekt oder es sind mehrere Objekte, abhängig von `objectlist`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/de
