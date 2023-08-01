---
- GuiCommand:/de
   Name:Draft Move
   Name/de:Draft Verschieben
   MenuLocation:Änderung → Verschieben
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**M****V**
   Version:0.7
   SeeAlso:[Draft UnterelementHervorheben](Draft_SubelementHighlight/de.md)
---

# Draft Move/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Move.svg  style="width:24px;"> **Draft-Verschieben** verschiebt oder kopiert die ausgewählten Objekt von einem Punkt zu einem anderen. Im Unterelemente-Modus verschiebt die Anweisung ausgewählte Punkte und Kanten oder kopiert ausgewählte Kanten von [Draft Linien](Draft_Line/de.md) und [Draft Drähten](Draft_Wire/de.md).

Die Anweisung kann auf 2D-Formen, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, angewendet werden, aber auch auf viele 3D-Objekte, wie jenen, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erzeugt wurden.

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;"> 
*Verschieben eines Objekts von einem Punkt zu einem anderen Punkt*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) and [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen, oder ein oder mehrere Unterelemente einer [Draft Linie](Draft_Line/de.md) oder eines [Draft Drahtes](Draft_Wire/de.md).
2.  Es gibt mehrere Moglichkeiten die Anweisung auszuführen:
    -   Die Schaltfläche **<img src="images/Draft_Move.svg" width=16px> [Draft Verschieben](Draft_Move/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Move.svg" width=16px> Verschieben** auswählen.
    -   Die Tastenkombination: **M** dann **V**.
3.  Wenn noch kein Objekt ausgewählt wurde: ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgabenbereich **Verschieben** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Wenn Unterelemente ausgewählt wurden: die Check-Box **Unterelemente ändern** aktivieren, um in den Unterelemente-Modus umzuschalten.
6.  Den ersten Punkt, den Basispunkt, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und auf die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** klicken.
7.  Den zweiten Punkt, den Zielpunkt, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und auf die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** klicken.



## Optionen

Das jeweilige Verhalten eines Tastaturkürzels, das hier genannt wird kann geändert sein. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Um manuell x, y und z - Koordinaten einzugeben, jeweils die Werte eingeben und die **Enter**-Taste drücken oder die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** klicken, wenn die gewünschten Werte eingegeben sind. Man sollte aber vorher den Mauszeiger aus der [3D-Ansicht](3D_view.md) herausziehen.
-   Zur Verwendung von Polarkoordinaten gibt man einen Wert für die **Länge** und einen Wert für den **Winkel** ein und drückt jeweils die **Enter**-Taste.
-   Ein Häckchen in **Winkel**-Kästchen eintragen, um den Cursor auf den jeweiligen Winkel zu setzen.
-   Mit der **H**-Taste den Fokus vom **X**-Eingabefeld auf das to the **Länge**-Eingabefeld und umgekehrt zu setzen. Abhängig davon, auf welchem Eingabefeld der Fokus liegt ist das Häckchen im **Winkel**-Kästchen gesetzt oder nicht.
-   Mit der **R**-Taste oder durch Klicken auf das **Relativ**-Kästchen wird in den entsprechenden Modus geschaltet. Ist der Modus für die Eingabe relativer Werte eingeschaltet, werden die Koordinaten des zweiten Punktes relativ zum ersten verwendet. Ansonsten werden sie bezoden auf das Ursprungskoordinatensystem verwendet.
-   Mit der **G**-Taste oder durch Klicken auf das **Global**-Kästchen wird in den Modus global geschaltet. Wenn der Modus global eingeschaltet ist, werden die Koordinaten bezogen auf das globale Koordinatensystem verwendet. Ansonsten werden sie bezogen auf das [EntwurfWähleEbene](Draft_SelectPlane/de.md) Koordinatensystem verwendet. {{Version/de|0.20}}
-   Mit der **T**-Taste oder durch Klicken auf das **Fortsetzen**-Kästchen wird auf den Modus Fortfahren geschaltet. Ist der Modus Fortfahren eingeschaltet, beginnt das Bearbeiten der Anweisung erneut nach dem Abschluss der Arbeit. Dieser Modus ist nur sinnvoll, wenn der Kopiermodus eingeschaltet ist. Abhängig von der **Wähle ursprüngliche Objekte nach dem Kopieren aus**-Eigenschaft, wird entweder das Ursprungsobjekt oder die zuletzt erstellte Kopie für die nächste Ausführung der Anweisung ausgewählt. Siehe [Einstellungen](#Preferences.md).
-   Mit der **P**-Taste oder durch Klicken auf das **Kopieren**-Kästchen wird auf den Kopiermodus geschaltet. Ist der Kopiermodus eingeschaltet, wird das Ausführen der Anweisung Kopien erstellen und verschieben anstatt die Ursprungsobjekte zu verschieben.
-   Mit der **D**-Taste oder durch Klicken auf das **Subelemente ändern**-Kästchen wird auf den Modus \"Subelemente ändern\" geschaltet. Ist dieser Modus \"Subelemente ändern\" eingeschaltet, verwendet die Anweisung Subelemente anstatt der ganzen Objekte. Die Subelemente müssen den Elementen [Draft Linie](Draft_Line/de.md) oder [Draft Polylinie](Draft_Wire/de.md) angehören.
-   Sind sowohl der Kopiermodus als auch der Modus Subelemente eingeschaltet und die Kanten von [Draft Polylinie](Draft_Wire.md) sind ausgewählt, werden neue Linien aus diesen Kanten erstellt.
-   Wird die **Alt**-Taste gedrückt und gehalten, nachdem der Basispunkt angeklickt wurde, wird ebenfalls der Kopiermodus eingeschaltet. Wenn die **Alt**-Taste gedrückt ist, können mehrere Zielpunkte angewählt werden. Das Lösen der **Alt**Taste beendet die Anweisung und die erstellten Kopien werden angezeigt.
-   Mit der **S**-Taste wird über [Draft Fangen](Draft_Snap/de.md) die Fangfunktion ein- oder ausgeschaltet.
-   Mit der **Esc**-Taste oder der **Close**-Schaltfläche wird die Anweisung abgebrochen.



## Hinweise

-   Ein Objekt, das [angehängt](Part_EditAttachment/de.md) ist, kann nicht mit der Draft Verschieben Anweisung verschoben werden. Um es trotzdem zu verschieben, muss sein unterstützendes **Support** Object verschoben werden, oder seine **Attachment Offset** geändert werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe der Koordinaten, wie Längen und Winkel zu ändern, ist die Eigenschaft: **Bearbeiten→ Eigenschaften... → Allgemein → Einheiten → Einheiten-Einstellungen → Anzahl der Nachkommastellen** einzustellen.
-   Um den Fokus beim Öffnen der Aufgabenansicht auf **Länge** zu legen, ist die Eigenschaft: **Bearbeiten → Eigenschaften... → Draft → Allgemeine Einstellungen → Entwurfswerkzeuge Optionen → Fokusierung auf Länge statt auf X-Koordinate setzen** anzupassen. Beachte, dass der Zeiger in der [3D Ansicht](3D_view/de.md) bewegt werden muss, um die Auswirkung sehen zu können.
-   Um die gleiche Kopiermethode über alle Anweisungen zu speichern und wieder zu verwenden, ist die Eigenschaft: **Bearbeiten → Eigenschaften... → Draft → Allgemeine Einstellungen → Entwurfswerkzeuge Optionen → Globaler Kopiermodus** einzustellen.
-   Um die Origialobjekte nach dem Kopieren zu markieren, ist die Eigenschaft: **Bearbeiten → Eigenschaften... → Draft → Allgemeine Einstellungen → Entwurfswerkzeuge Optionen → Wähle ursprüngliche Objekte nach dem Kopieren aus** einzustellen.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Objekte zu verschieben, benutze die `move`-Methode des Entwurfmodules.


```python
moved_list = move(objectslist, vector, copy=False)
```

-    `objectslist`enthält die zu verschiebenden Objekte. Es kann ein einzelnes Objekt oder es können mehrere Objekte sein.

-    `vector`ist der Versatz.

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
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/de
