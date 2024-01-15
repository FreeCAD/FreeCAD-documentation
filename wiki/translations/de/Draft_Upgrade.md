---
 GuiCommand:
   Name: Draft Upgrade
   Name/de: Draft Hochstufen
   MenuLocation: Änderung , Hochstufen
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **U** **P**
   SeeAlso: Draft_Downgrade/de
---

# Draft Upgrade/de



## Beschreibung

Der <img alt="" src=images/Draft_Upgrade.svg  style="width:24px;"> Der Befehl **Draft Hochstufen** (Aufrüsten) aktualisiert ausgewählte Objekte. Das Ergebnis ist abhängig von der Anzahl der ausgewählten Objekte und deren Typ. Der Befehl kann zum Beispiel Elemente verschmelzen und Flächen erzeugen. Es lohnt sich, eine Auswahl mehrmals zu aktualisieren, um zu sehen, ob ein besseres Ergebnis erzielt werden kann. Siehe das Beispiel im Bild. Beachte, dass nicht alle Objekte hochgestuft werden können. Dieser Befehl ist das Gegenstück zum Befehl [Draft Herabstufen](Draft_Downgrade/de.md) (Zurückstufen).

<img alt="" src=images/Draft_Upgrade_example.jpg  style="width:400px;"> 
*Ein offener nicht editierbarer Draht wird zu einem geschlossenen Draht und dann zu einer Fläche hochgestuft. Ein geschlossener, nicht editierbarer quadratischer Draht wird ebenfalls zu einer Fläche hochgestuft. Die beiden Flächen werden dann hochgestuft, um einen Verbund zu erstellen, der schließlich zu einem einzelnen bearbeitbaren Entwurf Draht hochgestuft wird.*



## Anwendung

1.  Wahlweise ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Upgrade.svg" width=16px> [Hochstufen](Draft_Upgrade/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Upgrade.svg" width=16px> Hochstufen** auswählen.
    -   Das Tastaturkürzel **U** dann **P**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.



## Hinweise

-   [Entwurf Linien](Draft_Line/de.md) und [Entwurf Drähte](Draft_Wire/de.md) können mit diesem Befehl, aber auch mit dem Befehl [Entwurf Fügen](Draft_Join/de.md) oder dem Befehl [Entwurf Draht](Draft_Wire/de.md) verbunden werden.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Objekte hochzustufen, verwende die `upgrade` Methode des Entwurf Moduls.


```python
upgrade_list = upgrade(objects, delete=False, force=None)
```

-    `objects`enthält die zu aktualisierenden Objekte. Es ist entweder ein einzelnes Objekt oder eine Liste von Objekten.

-   Wenn `delete` gleich `True` ist, werden die Quellobjekte gelöscht.

-    `force`erzwingt eine bestimmte Art des Upgrades durch den Aufruf einer bestimmten internen Funktion. Das kann sein: `"makeCompound"`, `"closeGroupWires"`, `"makeSolid"`, `"closeWire"`, `"turnToParts"`, `"makeFusion"`, `"makeShell"`, `"makeFaces"`, `"draftify"`, `"joinFaces"`, `"makeSketchFace"`, `"makeWires"` oder `"turnToLine"`.

-    `upgrade_list`wird zurückgegeben. Es ist eine Liste, die zwei Listen enthält: eine Liste der neuen Objekte und eine Liste der zu löschenden Objekte. Wenn `delete` `True` ist, ist die zweite Liste leer.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle = Draft.make_circle(1000)
rectangle = Draft.make_rectangle(2000, 800)
doc.recompute()

add_list1, delete_list1 = Draft.upgrade([circle, rectangle], delete=False)

line1 = Draft.make_line(App.Vector(2000, 0, 0), App.Vector(2500, 1500, 0))
line2 = Draft.make_line(App.Vector(2500, 1500, 0), App.Vector(3000, -1000, 0))
doc.recompute()

add_list2, delete_list2 = Draft.upgrade([line1, line2], delete=False)

simple_wire = add_list2[0]
add_list3, delete_list3 = Draft.upgrade(simple_wire, delete=False)

closed_wire = add_list3[0]
add_list4, delete_list4 = Draft.upgrade(closed_wire, delete=False)

face = add_list4[0]
add_list5, delete_list5 = Draft.upgrade(face, delete=False)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Upgrade/de
