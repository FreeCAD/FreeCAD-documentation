---
 GuiCommand:
   Name: Draft Join
   Name/de: Draft Verbinden
   MenuLocation: Änderung , Verbinden
   Workbenches: Draft_Workbench/de, Arch_Workbench
   Shortcut: **J** **O**
   Version: 0.18
   SeeAlso: Draft_Split/de
---

# Draft Join/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Join.svg  style="width:24px;"> **Draft Verbinden** verbindet [Draft Linien](Draft_Line/de.md) und [Draft Polylinien](Draft_Wire/de.md) zu einer einzigen Polylinie. Dieser Befehl ist das Gegenstück zum Befehl [Draft Teilen](Draft_Split/de.md).



## Anwendung

1.  Die Endpunkte der [Draft Linien](Draft_Line/de.md) und/oder [Draft Polylinien](Draft_Wire/de.md), die verbunden werden sollen, müssen exakt deckungsgleich sein. Wenn erforderlich, werden zuerst die Punkte justiert, um dies sicherzustellen.
2.  Zwei oder mehrere [Draft Linien](Draft_Line/de.md) und/oder [Draft Polylinien](Draft_Wire/de.md).
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Join.svg" width=16px> [Verbinden](Draft_Join/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Join.svg" width=16px> Verbinden** auswählen.
    -   Das Tastaturkürzel **J** dann **O**.



## Hinweise

-   [Draft Linien](Draft_Line/de.md) und [Draft Polylinien](Draft_Wire/de.md) können auch mit dem Befehl [Draft Polylinie](Draft_Wire/de.md) oder dem Befehl [Draft Hochstufen](Draft_Upgrade/de.md) verbunden werden.
-   Um Objekte zu verbinden, die keine [Draft Linien](Draft_Line/de.md) oder [Draft Polylinien](Draft_Wire/de.md) sind, kann zunächst versucht werden, [Draft Hochstufen](Draft_Upgrade/de.md) und/oder [Draft Herabstufen](Draft_Downgrade/de.md) einmal oder mehrmals auf sie anzuwenden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Drähte zu verbinden, wird die Methode `join_wires` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `joinWires`. Diese Methode gibt `None` zurück.


```python
join_wires(wires)
```

-    `wires`ist eine Liste von Polylinienobjekten, die verbunden werden sollen.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(500, 0, 0)
p3 = App.Vector(500, 500, 0)
p4 = App.Vector(0, 500, 0)

wire1 = Draft.make_wire([p1, p2])
wire2 = Draft.make_wire([p2, p3])
wire3 = Draft.make_wire([p3, p4])
wire4 = Draft.make_wire([p4, p1])

Draft.join_wires([wire1, wire3, wire2, wire4])
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Join/de
