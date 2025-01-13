---
 GuiCommand:
   Name: Draft Slope
   Name/de: Draft Neigung
   MenuLocation: Änderung , Neigung festlegen<br>Werkzeuge , Neigung festlegen
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version: 0.17
---

# Draft Slope/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Slope.svg  style="width:24px;"> **Draft Neigung** neigt ausgewählte [Draft Linien](Draft_Line/de.md) oder [Draft Kantenzüge](Draft_Wire/de.md), indem er die Z-Koordinate aller Punkte nach dem ersten Punkt vergrößert oder verringert. Er kann auch zum Abflachen von [Draft Kantenzügen](Draft_Wire/de.md) verwendet werden. Man beachte, dass die Neigung relativ zur XY-Ebene ist, die durch die {{PropertyData/de|Placement}} der Objekte definiert ist.

<img alt="" src=images/Draft_Slope_example.png  style="width:400px;"> 
*Links eine horizontale Draft-Linie. Rechts die gleiche Linie mit einem Neigungswert von 1 (Winkel ist 45°)*



## Anwendung

1.  Eine oder mehrere [Draft Linien](Draft_Line/de.md) und/oder [Draft Kantenzüge](Draft_Wire/de.md) auswählen.

2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   [Draft](Draft_Workbench/de.md): Die Schaltfläche **<img src="images/Draft_Slope.svg" width=16px> [Neigung festlegen](Draft_Slope/de.md)** drücken.
    -   Draft: Den Menüeintrag **Änderung → <img src="images/Draft_Slope.svg" width=16px> Neigung festlegen** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Werkzeuge → <img src="images/Draft_Slope.svg" width=16px> Neigung festlegen** auswählen.

3.  Einen Wert für die **Neigung** eingeben. {{Value|0}} bedeutet, dass jedes Segment horizontal ist, {{Value|0,5}} bedeutet, dass der Höhenunterschied (Delta-Höhe) für jedes Segment das {{Value|0,5}}-fache seiner Länge beträgt, usw. Der Wert kann auch negativ sein.

4.  
    **Enter**oder die Schaltfläche **OK** drücken, um den Befehl zu abzuschließen.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python-Methode zum Neigen von Objekten. Um die Ergebnisse des Befehls Draft Neigung zu emulieren, muss die Eigenschaft `Points` von Drahtobjekten geändert werden.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Slope/de
