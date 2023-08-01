---
- GuiCommand:/de
   Name:Arch Grid
   Name/de:Arch Gitter
   MenuLocation:Arch → Achsenwerkzeuge → Gitter
   Workbenches:[Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch Achse](Arch_Axis/de.md), [Arch AchsenSystem](Arch_AxisSystem/de.md)
---

# Arch Grid/de

## Beschreibung

Das **<img src="images/Arch_Grid.svg" width=16px> [Arch Gitter](Arch_Grid/de.md)** Werkzeug ermöglicht es dir, ein gitterartiges Objekt im Dokument zu platzieren. Dieses Objekt soll als Basis für die Erstellung von Arch Objekten dienen, die einen regelmäßigen, aber komplexen Rahmen benötigen, wie z.B. Fenster, Vorhangfassaden, Säulengitter, Geländer usw. Das Gitterobjekt ist wie eine Tabellenkalkulation bearbeitbar, in der du Spalten und Zeilen hinzufügst oder entfernst, ihre Größe definierst und Zellen zusammenführen kannst.

Das Gitter ist ein 2D Objekt und kann daher überall dort verwendet werden, wo eine 2D Form wie z.B. eine [Entwurf](Draft_Workbench/de.md) oder [Skizze](Sketcher_Workbench/de.md) benötigt wird, es kann sich aber auch wie ein [Arch AchsenSystem](Arch_AxisSystem/de.md) verhalten und dazu verwendet werden, die Positionierung anderer Arch Objekte zu verbreiten.

<img alt="" src=images/Arch_Grid_example.jpg  style="width:600px;"> 
*Eine Anordnung von Säulen, ein Geländersystem und ein Fenster, die jeweils auf einem [Arch Gitter](Arch_Grid/de.md) Objekt basieren.*

## Anwendung

1.  Drücke die **<img src="images/Arch_Grid.svg" width=16px> [Arch Gitter](Arch_Grid/de.md)** Taste.
2.  \# Lege die **Breite** und **Höhe** des Gitters in den Eigenschaften fest.
3.  Wechsle in den Bearbeitungsmodus durch doppelklick des Gitterobjekts in der Baumansicht.
4.  Füge Zeilen und Spalten hinzu.
5.  Stelle die gewünschte Breite und Höhe der Zeilen und Spalten ein, indem du auf die Zeilen- oder Spaltenüberschriften doppelklickst.

## Optionen

-   Eine Spaltenbreite oder Zeilenhöhe von 0 bedeutet, dass die Größe automatisch an die Gesamtbreite/-höhe des Gitters angepasst wird.
-   Zellen können zusammengeführt und wieder getrennt werden, indem sie ausgewählt und auf die entsprechende Schaltfläche geklickt wird.
-   Bei Verwendung als **Achsen** Eigenschaft anderer Arch Objekte steuert das Gitter die Positionierung dieser Objekte. Die **Punkteausgabe** Eigenschaft definiert, wie die anderen Objekte auf dem Gitter platziert werden: An Knotenpunkten, Kantenmittelpunkten oder Flächenmittelpunkten.
-   Durch festlegen der **Auto Höhe** oder **Auto Breite** Eigenschaften auf einen Wert ungleich Null zu setzen, ignoriert die Gesamtzahl der Zeilen/Spalten und ihre individuellen Höhen/Breiten. Stattdessen wird automatisch die maximale Anzahl von Spalten oder Zeilen der angegebenen Auto Breite/Höhe erzeugt.

## Eigenschaften

-    **Zeilen**: Die Anzahl der Zeilen

-    **Spalten**: Die Anzahl der Spalten

-    **Zeilengröße**: Die Größen für Zeilen

-    **Spaltengröße**: Die Größen für Spalten

-    **Punkte Ausgabe**: Die Typ der von diesem Gitterobjekt erzeugten 3D Punkte

-    **Breite**: Die Gesamtbreite dieses Gitters

-    **Höhe**: Die Gesamthöhe dieses Gitters

-    **Auto Breite**: Erstellt automatische Spalteneinteilungen (zum Deaktivieren auf 0 gesetzt)

-    **Auto Höhe**: Erstellt automatische Zeileneinteilungen (zum Deaktivieren auf 0 gesetzt)

-    **Neuausrichten**: Wenn sich dieses Gitter im Kantenmittelpunkt Modus befindet, muss es seine Kinder entlang der Kantennormalen neu ausrichten oder nicht

-    **Ausgeblendete Flächen**: Die Indizes der ausgeblendeten Flächen

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Gitter kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus durch folgende Funktion verwendet werden:


```python
Grid = makeGrid(name="Grid")
```

-   Erstellt ein `Gitter` Objekt.

Seine `Breite`, `Höhe`, `Zeilen`, und `Spalten` Attribute können direkt geändert werden, um das Aussehen des Gitters festzulegen.


```python
import FreeCAD, Draft, Arch
Grid = Arch.makeGrid()

Grid.Width = 5000
Grid.Height = 5000
Grid.Rows = 4
Grid.Columns = 6
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = Grid
FreeCAD.ActiveDocument.recompute() 
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Grid/de
