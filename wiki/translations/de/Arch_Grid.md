---
 GuiCommand:
   Name: Arch Grid
   Name/de: Arch Raster
   MenuLocation: Anmerkung , Raster
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_Axis/de, Arch_AxisSystem/de
---

# Arch Grid/de



## Beschreibung

Das Werkzeug **Arch Raster** ermöglicht, ein gitterartiges Objekt im Dokument zu platzieren. Dieses Objekt soll als Basis für die Erstellung von Arch-Objekten dienen, die einen regelmäßigen, aber komplexen Rahmen benötigen, wie z.B. Fenster, Vorhangfassaden, Säulengitter, Geländer usw. Das Rasterobjekt (Grid-Objekt) kann wie eine Tabellenkalkulation bearbeitet werden, indem Spalten und Zeilen hinzugefügt oder entfernt werden, die Größe festgelegt und Zellen zusammengeführt werden.

Das Raster ist ein 2D-Objekt und kann daher überall dort verwendet werden, wo eine 2D-Form wie z.B. ein [Draft](Draft_Workbench/de.md)-Objekt oder eine [Skizze](Sketcher_Workbench/de.md) benötigt wird, es kann sich aber auch wie ein [Arch AchsenSystem](Arch_AxisSystem/de.md) verhalten und dazu verwendet werden, die Positionierung anderer Arch-Objekte zu verbreiten.

<img alt="" src=images/Arch_Grid_example.jpg  style="width:600px;"> 
*Eine Anordnung von Säulen, ein Geländersystem und ein Fenster, die jeweils auf einem [Arch Raster](Arch_Grid/de.md)-Objekt basieren.*



## Anwendung

1.  Die Schaltfläche **<img src="images/Arch_Grid.svg" width=16px> [Arch Raster](Arch_Grid/de.md)** drücken.
2.  \# **Breite** und **Höhe** des Rasters in den Eigenschaften festlegen.
3.  Durch doppelklick auf das Raster-Objekt in der Baumansicht in den Bearbeitungsmodus wechseln.
4.  Zeilen und Spalten hinzufügen.
5.  Die gewünschte Breite und Höhe der Zeilen und Spalten einstellen, indem die Zeilen- oder Spaltenüberschriften doppelt angeklickt werden.



## Optionen

-   Eine Spaltenbreite oder Zeilenhöhe von 0 bedeutet, dass die Größe automatisch an die Gesamtbreite/-höhe des Rasters angepasst wird.
-   Zellen können zusammengeführt und wieder getrennt werden, indem sie ausgewählt und auf die entsprechende Schaltfläche geklickt wird.
-   Bei Verwendung als **Achsen**-Eigenschaft anderer Arch-Objekte steuert das Raster die Positionierung dieser Objekte. Die Eigenschaft **Punkteausgabe** definiert, wie die anderen Objekte auf dem Raster platziert werden: An Knotenpunkten, Kantenmittelpunkten oder Flächenmittelpunkten.
-   Durch festlegen der Eigenschaften **Auto Höhe** oder **Auto Breite** auf einen Wert ungleich Null, wird die Gesamtzahl der Zeilen/Spalten und ihre individuellen Höhen/Breiten ignoriert. Stattdessen wird automatisch die maximale Anzahl von Spalten oder Zeilen der angegebenen Auto Breite/Höhe erzeugt.



## Eigenschaften

-    {{PropertyData/de|Zeilen}}: Die Anzahl der Zeilen

-    {{PropertyData/de|Spalten}}: Die Anzahl der Spalten

-    {{PropertyData/de|Zeilengröße}}: Die Größen für Zeilen

-    {{PropertyData/de|Spaltengröße}}: Die Größen für Spalten

-    {{PropertyData/de|Punkte Ausgabe}}: Die Art der von diesem Rasterobjekt erzeugten 3D-Punkte

-    {{PropertyData/de|Breite}}: Die Gesamtbreite dieses Rasters

-    {{PropertyData/de|Höhe}}: Die Gesamthöhe dieses Rasters

-    {{PropertyData/de|Auto Breite}}: Erstellt automatische Spalteneinteilungen (zum Deaktivieren auf 0 setzen)

-    {{PropertyData/de|Auto Höhe}}: Erstellt automatische Zeileneinteilungen (zum Deaktivieren auf 0 setzen)

-    {{PropertyData/de|Neuausrichten}}: Gibt an ob dieses Raster Kindobjekte entlang der Kantennormalen neu ausrichtet, wenn es sich im Modus Kantenmittelpunkt befindet, oder nicht.

-    {{PropertyData/de|Ausgeblendete Flächen}}: Die Indizes der auszublendenden Flächen.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Raster kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus durch folgende Funktion verwendet werden:


```python
Grid = makeGrid(name="Grid")
```

-   Erstellt ein `Raster`-Objekt.

Seine Attribute `Breite`, `Höhe`, `Zeilen`, und `Spalten` können direkt geändert werden, um das Aussehen des Rasters festzulegen.


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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Grid/de
