---
- GuiCommand:
   Name: Draft Join
   Name/de: Entwurf Verbinden
   MenuLocation: Änderung -> Verbinden
   Workbenches: Draft_Workbench/de, Arch_Workbench
   Shortcut: **J** **O**
   Version: 0.18
   SeeAlso: Draft_Split/de
---

# Draft Join/de

## Beschreibung

Der <img alt="" src=images/Draft_Join.svg  style="width:24px;"> **Entwurf Verbinden** Befehl verbindet [Entwurf Linien](Draft_Line/de.md) und [Entwurf Drähte](Draft_Wire/de.md) zu einem einzigen Draht. Dieser Befehl ist das Gegenstück zum Befehl [Entwurf Teilen](Draft_Split/de.md).

## Anwendung

1.  Die Endpunkte der zu verbindenden [Entwurf Linien](Draft_Line/de.md) und/oder [Entwurf Drähte](Draft_Wire/de.md) müssen genau deckungsgleich sein. Wenn erforderlich passe zunächst Punkte an, damit dies der Fall ist.
2.  Wähle zwei oder mehr [Entwurf Linien](Draft_Line/de.md) und/oder [Entwurf Drähte](Draft_Wire/de.md).
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_Join.svg" width=16px> [Entwurf_Verbinden](Draft_Join/de.md)** Schaltfläche.
    -   Wähle die Option **Änderung → <img src="images/Draft_Join.svg" width=16px> Verbinden** aus dem Menü.
    -   Verwende das Tastaturkürzel: **J** dann **O**.

## Hinweise

-   [Entwurf Linien](Draft_Line/de.md) und [Entwurf Drähte](Draft_Wire/de.md) können auch mit dem Befehl [Entwurf Draht](Draft_Wire/de.md) oder dem Befehl [Entwurf Hochstufen](Draft_Upgrade/de.md) verbunden werden.
-   Um Objekte zu verbinden, die keine [Entwurf Linien](Draft_Line/de.md) oder [Entwurf Drähte](Draft_Wire/de.md) sind, kannst du zunächst versuchen, sie mit [Entwurf Hochstufen](Draft_Upgrade/de.md) und/oder [Entwurf Herabstufen](Draft_Downgrade/de.md) ein- oder mehrmals zu verbinden.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://www.freecadweb.org/api) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Drähte zu verbinden, verwende die `join_wires` Methode ({{Version/de|0.19}}) des Moduls Entwurf. Diese Methode ersetzt die veraltete Methode `joinWires`. Diese Methode gibt `None` zurück.


```python
join_wires(wires)
```

-    `wires`ist eine Liste von Drahtobjekten, die verbunden werden sollen.

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
