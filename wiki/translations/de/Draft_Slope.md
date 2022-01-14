---
- GuiCommand:/de
   Name:Draft Slope
   Name/de:Entwurf Neigung
   MenuLocation:Entwurf → Setze Neigung<br>Dienstprogramme → Setze Neigung
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Version:0.17
---

# Draft Slope/de


</div>

## Beschreibung

Der Befehl <img alt="" src=images/Draft_Slope.svg  style="width:24px;"> *\' Entwurf Neigung*\' neigt ausgewählte [Entwurf Linien](Draft_Line/de.md) oder [Entwurf Drähte](Draft_Wire/de.md), indem er die Z-Koordinate aller Punkte nach dem ersten Punkt erhöht oder verringert. Er kann auch zum Abflachen von [Entwurf Drähte](Draft_Wire/de.md) verwendet werden. Beachten, dass die Neigung relativ zur auf XY Ebene ist, die durch die **Placement** der Objekte definiert ist.

<img alt="" src=images/Draft_Slope_example.png  style="width:400px;"> 
*Links eine horizontale Entwurfslinie. Rechts die gleiche Linie mit einem Neigungswert von 1 (Winkel ist 45°)*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine oder mehrere [Entwurf Linie](Draft_Line/de.md) und/oder [Entwurf Draht](Draft_Wire/de.md).
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_Slope.svg" width=16px> [Entwurfsneigung](Draft_Slope/de.md)**.
    -   Wählen Sie die Option **Änderung → <img src="images/Draft_Slope.svg" width=16px> Neigung festlegen** aus dem Menü.
    -   Wähle die Option **Hilfsprogramme → <img src="images/Draft_Slope.svg" width=16px> Neigung einstellen** aus dem Menü.
3.  Gib einen **Neigungs**wert ein. {{Value|0}} bedeutet, dass jedes Segment horizontal ist, {{Value|0,5}} bedeutet, dass die Delta Höhe für jedes Segment das {{Value|0,5}}-fache seiner Länge beträgt, usw. Der Wert kann auch negativ sein.
4.  Drücke **Enter** oder die Taste {{button|OK}}, um den Befehl zu beenden.


</div>

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python Methode zur Neigung von Objekten. Um die Ergebnisse des Entwurf Neigung Befehls zu emulieren, muss die `Points`-Eigenschaft von Drahtobjekten geändert werden.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Slope/de
