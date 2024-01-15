---
 GuiCommand:
   Name: Draft Move
   Name/de: Draft Verschieben
   MenuLocation: Änderung , Verschieben
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **M****V**
   Version: 0.7
   SeeAlso: Draft_SubelementHighlight/de
---

# Draft Move/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Move.svg  style="width:24px;"> **Draft-Verschieben** verschiebt oder kopiert die ausgewählten Objekt von einem Punkt zu einem anderen. Im Unterelemente-Modus verschiebt die Anweisung ausgewählte Punkte und Kanten oder kopiert ausgewählte Kanten von [Draft Linien](Draft_Line/de.md) und [Draft Polylinien](Draft_Wire/de.md).

Die Anweisung kann auf 2D-Formen, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, angewendet werden, aber auch auf viele 3D-Objekte, wie jenen, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erzeugt wurden.

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;"> 
*Verschieben eines Objekts von einem Punkt zu einem anderen Punkt*



## Anwendung

Siehe auch: [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen, oder ein oder mehrere Unterelemente einer [Draft Linie](Draft_Line/de.md) oder eines [Draft Drahtes](Draft_Wire/de.md).
2.  Es gibt mehrere Moglichkeiten den Befehl auszuführen:
    -   Die Schaltfläche **<img src="images/Draft_Move.svg" width=16px> [Verschieben](Draft_Move/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Move.svg" width=16px> Verschieben** auswählen.
    -   Die Tastenkombination: **M** dann **V**.
3.  Wenn noch kein Objekt ausgewählt wurde: ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgabenbereich **Verschieben** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Wenn Unterelemente ausgewählt wurden: die Check-Box **Unterelemente ändern** aktivieren, um in den Unterelemente-Modus umzuschalten.
6.  Den ersten Punkt, den Basispunkt, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und auf die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
7.  Den zweiten Punkt, den Zielpunkt, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und auf die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Um Koordinaten manuell einzugeben, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben oder die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** gedrückt, sobald die gewünschten Werte eingegeben sind. Man sollte aber vorher den Mauszeiger aus der [3D-Ansicht](3D_view.md) herausziehen.

-   Zur Verwendung von Polarkoordinaten gibt man einen Wert für die **Länge** und einen Wert für den **Winkel** ein und bestätigt jeweils mit **Enter**.

-   Die Check-Box **Winkel** aktivieren, um den Mauszeiger auf den angegebenen Winkel einzuschränken.

-    **L**drücken, um den Fokus vom Eingabefeld **X** auf das Eingabefeld **Länge** und zurück zu setzen. Abhängig davon, auf welchem Eingabefeld der Fokus liegt ist das Häkchen in der Check-Box **Winkel** aktiviert oder nicht.

-    **R**drücken oder die Check-Box **Relativ** anklicken, um den Relativ-Modus umzuschalten. Ist der Relativ-Modus aktiviert, beziehen sich die Koordinaten des zweiten Punktes auf den ersten. Andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Check-Box **Global** anklicken, um den Global-Modus umzuschalten. ist der Global-Modus aktiviert, beziehen sich die Koordinaten auf das globale Koordinatensystem. Andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **N**drücken oder die Check-Box **Fortsetzen** anklicken, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet. Dieser Modus ist nur sinnvoll, wenn der Kopieren-Modus aktiviert. Abhängig von der Eigenschaft **Wähle ursprüngliche Objekte nach dem Kopieren aus** wird entweder das Ursprungsobjekt oder die zuletzt erstellte Kopie für die nächste Ausführung des Befehls ausgewählt. Siehe [Einstellungen](#Einstellungen.md).

-    **C**drücken oder die Check-Box **Kopieren** anklicken, um den Kopieren-Modus umzuschalten. Ist der Kopiermodus aktiviert, erstellt der Befehl verschobene Kopien anstatt die Ursprungsobjekte zu verschieben.

-    **B**drücken oder die Check-Box **Subelemente ändern** anklicken, um den Unterelemente-ändern-Modus umzuschalten. Ist dieser Unterelemente-ändern-Modus aktiviert, verwendet der Befehl die ausgewählten Unterelemente anstatt der ganzen Objekte. Die Unterelemente müssen [Draft Linien](Draft_Line/de.md) oder [Draft Polylinien](Draft_Wire/de.md) sein.

-   Sind sowohl der Kopieren-Modus als auch der Unterelemente-ändern-Modus aktiviert, und sind Kanten von [Draft Polylinien](Draft_Wire.md) ausgewählt, werden neue Linien aus diesen Kanten erstellt.

-   Wird **Alt** gedrückt und gehalten, nachdem der Basispunkt angeklickt wurde, wird ebenfalls der Kopiermodus eingeschaltet. Wenn **Alt** gedrückt wird, können mehrere Zielpunkte angewählt werden. **Alt** loslassen, um den Befehl zu beenden und die erstellten Kopien anzuzeigen.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. ausgeschaltet.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Ein [angehängtes](Part_EditAttachment/de.md) Objekt kann nicht mit dem Befehl Draft-Verschieben verschoben werden. Um es trotzdem zu verschieben, muss entweder seine {{PropertyData/de|Support}}-Objekt verschoben werden, oder seine {{PropertyData/de|Attachment Offset}} angepasst werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Um den Fokus beim Öffnen des Aufgaben-Bereichs auf das Eigabefeld **Länge** zu legen: **Bearbeiten → Eigenschaften... → Draft → Allgemein → Fokusierung auf Länge statt auf X-Koordinate setzen** anzupassen. Beachte, dass der Zeiger in der [3D-Ansicht](3D_view/de.md) bewegt werden muss, damit sich die Änderung auswirken können.
-   Um die Origialobjekte nach dem Kopieren erneut auszuwählen: **Bearbeiten → Eigenschaften... → Draft → Allgemein → Wähle ursprüngliche Objekte nach dem Kopieren aus** einzustellen.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Verschieben von Objekten wird die Methode `move` des Draft-Moduls verwendet.


```python
moved_list = move(objectslist, vector, copy=False)
```

-    `objectslist`enthält die zu verschiebenden Objekte. Es kann ein einzelnes Objekt oder es können mehrere Objekte sein.

-    `vector`ist die Verschiebung.

-   Wenn `copy` `True` ist, werden Kopien erstellt, anstatt die Originale der Objekte zu verschieben.

-    `moved_list`gibt die verschobenen Originale oder die neuen Kopien aus. Es ist ein einzelnes Objekt oder eine Liste von Objekten, abhängig von `objectslist`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/de
