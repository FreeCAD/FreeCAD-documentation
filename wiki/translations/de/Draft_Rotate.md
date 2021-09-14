---
- GuiCommand:/de
   Name:Draft Rotate
   Name/de:Entwurf Drehen
   MenuLocation:Entwurf → Drehen
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**R****O**
   Version:0.7
   SeeAlso:[Draft Verschieben](Draft_Move/de.md), [Draft Anordnung](Draft_Array/de.md)
---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Drehen-Werkzeug dreht oder kopiert die ausgewählten Objekte um einen gegebenen Winkel bezogen auf einen Referenzpunkt.


</div>


<div class="mw-translate-fuzzy">

Das Drehen-Werkzeug kann mit 2D-Formen verwendet werden, die mit dem [Draft](Draft_Workbench/de.md)- oder [Skizzierer](Sketcher_Workbench/de.md)-Arbeitsbereich erstellt wurden, kann aber auch mit vielen Arten von 3D-Objekten benutzt werden, wie die mit dem [Part](Part_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Arbeitsbereich erzeugten.


</div>

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Drehen eines Objekts mit einem Mittelpunkt-Referenzpunkt, von einem Referenzwinkel zu einen anderen Winkel*


</div>

## Anwendung

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Die Objekte auswählen, die gedreht oder kopiert werden sollen
2.  Auf die Schaltfläche **<img src="images/Draft_Rotate.svg" width=16px> [Entwurf Drehen](Draft_Rotate.md)** klicken oder die Tasten **R** und dann **O** drücken. Wenn kein Objekt ausgewählt wurde, erscheint die Bitte, das zu tun.
3.  Auf einen ersten Punkt in der [3D-Ansicht](3D_view/de.md) klicken oder die [Entwurfskoordinaten](Draft_Coordinates/de.md) eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** drücken. Dieser dient als Basispunkt der Operation, durch den die Drehachse verlaufen wird.
4.  Auf einen zweiten Punkt in der [3D-Ansicht](3D_view/de.md) klicken oder einen Basiswinkel angeben. Dies definiert eine Grundlinie, die sich um den ersten Punkt dreht.
5.  Auf einen dritten Punkt in der [3D-Ansicht](3D_view/de.md) klicken oder einen Rotationswinkel angeben. Dies startet die Drehung der Grundlinie und dadurch auch der Objekte.


</div>

## Optionen

The single character keyboard shortcuts and the modifier key mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Die Taste **X**, **Y** oder **Z** nach einem Punkt betätigen, um den nächsten Punkt auf der entsprechenden Achse einzuschränken.
-   Zur manuellen Eingabe der Koordinaten einfach die Werte eingeben und jeweils die **ENTER**-Taste zwischen jeder X-, Y- und Z-Komponente betätigen.

:   Die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)**-Schaltfläche betätigen, wenn die gewünschten Werte für den einzufügenden Punkt eingegeben sind.

-   Die **T**-Taste betätigen oder auf das Auswahlkästchen klicken, um in den \"Nächstes-Modus\" umzuschalten. Wenn der \"Nächstes\_Modus\" aktiv ist, wird das Werkzeug Drehen wieder aufgerufen, nachdem die Operation abgeschlossen wurde. Dies ermöglicht es, weitere Objekte zu drehen oder zu kopieren ohne jedesmal wieder auf die Drehen-Schaltfläche klicken zu müssen.
-   Die **P**-Taste betätigen oder auf das Auswahlkästchen klicken, um in den \"Kopiermodus\" umzuschalten. Wenn der \"Kopier\_Modus\" aktiv ist, wird das Werkzeug Drehen die Originalform bzw. das Originalobjekt an seinem Platz lassen, aber eine Kopie erzeugen und mit dem angegebenen Winkel am dritten Punkt einfügen.

:   Es können beide **T**- und **P**-Tasten verwendet werden, um mehrere Kopien der Reihe nach zu positionieren.

-   Durch Halten der **ALT**-Taste nach dem zweiten Punkt wird ebenfalls in den \"Kopiermodus\" geschalten. Wenn die **ALT**-Taste nach dem Klicken des dritten Punktes gehalten wird, kann man weitere Kopien mit dem gleichen Rotationspunkt und der gleichen Rotationsachse positionieren. Nach dem Lösen der **ALT**-Taste wird die Aktion abgeschlossen und die Kopien werden angezeigt.
-   Durch das Halten der **Ctrl**-Taste wird das [Einrasten](Draft_Snap/de.md) (Fangen) zum nächstgelegenen Einrastpunkt aktiviert, unabhängig von der Distanz dahin.
-   Das Halten der Taste **CTRL** während der Mausbewegung erzwingt den [Einrasten](Draft_Snap/de.md) zur nächsten Einrastposition unabhängig vom Abstand dazu.
-   Das Halten der **Umschalt**-Taste während des Drehens [schränkt](Draft_Constrain/de.md) die Bewegung zum nächsten horizontalen oder vertikalen Punkt den nächsten Punkt in Bezug auf das Rotationszentrum ein.
-   Mit der **ESC**-Taste oder durch Klicken auf die {{button|Schließen}}-Schaltfläche wird der aktuelle Befehl abgebrochen. Kopien, die bereits erstellt wurden, bleiben erhalten.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be rotated with the Draft Rotate command. To rotate it either its **Support** object has to be rotated, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To store and reuse the same copy mode setting across commands: **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD GrundlagenSkripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Drehen-Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion veerwendet werden:


</div>


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```


<div class="mw-translate-fuzzy">

-   Dreht den Basispunkt der Objekte in der angegebenen Liste `objectlist` mit dem angegebenen Winkel `angle` um das Rotationszentrum.
    -   
        `objectlist`
        
        kann ein einzelnes Objekt oder eine Liste von Objekten sein.

    -   Wenn ein Rotationszentrum (`center`) und `axis` gegeben sind, werden sie verwendet, ansonten bezieht sich die Drehung auf den Ursprung und um die Z-Achse.

:   Der Drehungswinkel bezieht sich auf den Basispunkt des Objektes. Wenn also ein Objekt um 45 Grad gedreht wird und dann ein weiteres Mal um 45 Grad gedreht wird, wird es insgesamt um 90 Grad zu ihrer Ursprungsposition gedreht sein.

-   Wenn `copy` `True` ist, werden Kopien erstellt anstatt die originalen Objekte zu drehen.
-   Eine `rotatedlist` wird mit den gedrehten Originalen oder mit den neuen Kopien gemeldet.
    -   
        `rotatedlist`
        
        ist entweder ein einzelnes Objekt oder eine Liste von Objekten, abhängig von der Eingabe `objectlist`.


</div>

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


<div class="mw-translate-fuzzy">





</div>


 
