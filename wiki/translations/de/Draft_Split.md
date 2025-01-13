---
 GuiCommand:
   Name: Draft Split
   Name/de: Draft Teilen
   MenuLocation: Änderung , Teilen<br>Bearbeiten , Teilen
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **S** **P**
   Version: 0.18
   SeeAlso: Draft_Join/de
---

# Draft Split/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Split.svg  style="width:24px;"> **Draft Teilen** teilt eine [Draft Linie](Draft_Line/de.md) oder [Draft Polylinie](Draft_Wire/de.md) an einem bestimmten Punkt oder einer Kante. Dieser Befehl ist das Gegenstück zum Befehl [Draft Verbinden](Draft_Join/de.md).



## Anwendung

#\* Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:

#\* Die Schaltfläche **<img src="images/Draft_Split.svg" width=16px> [Teilen](Draft_Split/de.md)** drücken.

#\* [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → <img src="images/Draft_Split.svg" width=16px> Teilen** auswählen.

#\* [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_Split.svg" width=16px> Split** auswählen.

#\* Das Tastaturkürzel **S** dann **P**.

1.  Den Mauszeiger über die richtige Kante einer [Draft Linie](Draft_Line/de.md) oder eines [Draft Polylinie](Draft_Wire/de.md) bewegen.
2.  Die Kante wird markiert.
3.  Eine der folgenden möglichkeiten auswählen:
    -   Wenn die Polylinie geschlossen ist:
        -   Einen beliebigen Punkt auf der Kante auswählen.
        -   Die Kante wird von der Polylinie abgetrennt und zu einer separaten Polylinie.
    -   Wenn die Polylinie offen ist:
        -   Den richtigen Punkt auf der Kante auswählen. Siehe [Hinweise](#Hinweise.md).
        -   Die Polylinie wird an der ausgewählten Stelle geteilt.



## Hinweise

-   Wenn eine offene Polylinie geteilt wird und der angeklickte Punkt nicht genau auf der ausgewählten Kante liegt, wird der neue Punkt nicht kollinear mit der ehemaligen Kante sein. Verwende eine entsprechende [Draft Einrasten](Draft_Snap/de.md) Option, um dies zu verhindern.
-   Um Objekte zu teilen, die keine [Draft Linien](Draft_Line/de.md) oder [Draft Polylinien](Draft_Wire/de.md) sind, kann man zuerst versuchen, [Draft Hochstufen](Draft_Upgrade/de.md) und/oder [Draft Herabstufen](Draft_Downgrade/de.md) einmal oder mehrmals auf sie anzuwenden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um einen Polylinie zu teilen, wird die Methode `split` des Moduls Draft verwendet. Diese Methode gibt `None` zurück.


```python
split(wire, newPoint, edgeIndex)
```

-    `wire`die Polylinie (wire object), die geteilt werden soll.

-    `newPoint`der Punkt, an dem die Abtrennung erfolgen soll.

-    `edgeIndex`Index der Kante, an der die Abtrennung erfolgen soll (1-basiert).

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(500, 0, 0)
p3 = App.Vector(250, 0, 0)

wire = Draft.make_wire([p1, p2])

Draft.split(wire, p3, 1)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Split/de
