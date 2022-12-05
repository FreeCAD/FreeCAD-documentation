---
- GuiCommand:/de
   Name:Draft Split
   Name/de:Entwurf Teilen
   MenuLocation:Änderung → Teilen
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Shortcut:**S** **P**
   Version:0.18
   SeeAlso:[Entwurf Verbinden](Draft_Join/de.md)
---

# Draft Split/de

## Beschreibung

Der <img alt="" src=images/Draft_Split.svg  style="width:24px;"> **Entwurf Teilen** Befehl teilt eine [Entwurf Linie](Draft_Line/de.md) oder [Entwurf Draht](Draft_Wire/de.md) an einem bestimmten Punkt oder einer Kante. Dieser Befehl ist das Gegenstück zum Befehl [Entwurf Verbinden](Draft_Join/de.md).

## Anwendung

#\* Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:

#\* Drücke die **<img src="images/Draft_Split.svg" width=16px> [Entwurf teilen](Draft_Split/de.md)**.

#\* Wähle die Option **Änderung → <img src="images/Draft_Split.svg" width=16px> Teilen** aus dem Menü.

#\* Verwende die Tastaturkürzel: **S** und dann **P**.

1.  Bewege den Mauszeiger über die richtige Kante einer [Entwurf Linie](Draft_Line/de.md) oder eines [Entwurf Draht](Draft_Wire/de.md).
2.  Die Kante wird markiert.
3.  Führe einen der folgenden Schritte aus:
    -   Wenn der Draht geschlossen ist:
        -   Wähle einen beliebigen Punkt auf der Kante.
        -   Die Kante wird vom Draht abgetrennt und wird zu einem separaten Draht.
    -   Wenn der Draht offen ist:
        -   Wähle den richtigen Punkt auf der Kante. Siehe [Hinweise](#Hinweise.md).
        -   Der Draht wird an der gegriffenen Stelle geteilt.

## Hinweise

-   Wenn ein offener Draht geteilt wird und der angeklickte Punkt nicht genau auf der ausgewählten Kante liegt, wird der neue Punkt nicht kollinear mit der ehemaligen Kante sein. Verwende eine entsprechende [Entwurf Fang](Draft_Snap/de.md) Option, um dies zu verhindern.
-   Um Objekte zu teilen, die keine [Entwurf Linien](Draft_Line/de.md) oder [Entwurf Drähte](Draft_Wire/de.md) sind, kannst du zunächst versuchen, sie mit [Entwurf Hochstufen](Draft_Upgrade/de.md) und/oder [Entwurf Herabstufen](Draft_Downgrade/de.md) einmal oder mehrmals zu teilen.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://www.freecadweb.org/api) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um einen Draht zu teilen, verwende die Methode `split` des Moduls Entwurf. Diese Methode gibt `None` zurück.


```python
split(wire, newPoint, edgeIndex)
```

-    `wire`das Drahtobjekt, das geteilt werden soll.

-    `newPoint`der Punkt, an dem die Aufteilung erfolgen soll.

-    `edgeIndex`Index der Kante, an der die Aufteilung erfolgen soll (1-basiert).

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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Split/de
