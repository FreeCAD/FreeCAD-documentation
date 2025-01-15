---
 GuiCommand:
   Name: Sketcher RemoveAxesAlignment
   Name/de: Sketcher AchsenausrichtungenEntfernen
   MenuLocation: Sketch , Skizzen-Werkzeuge , Achsenausrichtung entfernen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **R**
   Version: 0.20
---

# Sketcher RemoveAxesAlignment/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Sketcher RemoveAxesAlignment](Sketcher_RemoveAxesAlignment/de.md) entfernt die Achsenausrichtungen ausgewählter Kanten, indem die Randbedingungen <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [HorizontalFestlegen](Sketcher_ConstrainHorizontal/de.md) und <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [VertikalFestlegen](Sketcher_ConstrainVertical/de.md) durch die Randbedingungen [ParallelFestlegen](Sketcher_ConstrainParallel/de.md) und [RechtwinkligFestlegen](Sketcher_ConstrainPerpendicular/de.md) ersetzt werden. Die Kanten können dann gedreht werden, ohne dass ihre rechtwinklige Ausrichtung verloren geht.



## Anwendung

1.  Zwei oder mehr Kanten, die horizontal oder vertikal festgelegt wurden, z.B. ein [Rechteck](Sketcher_CreateRectangle/de.md).
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> [Achsenausrichtung entfernen](Sketcher_RemoveAxesAlignment/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> Achsenausrichtung entfernen** auswählen.
    -   Das Tastaturkürzel **Z** dann **R**.



## Beispiel

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*Ein ausgewähltes Rechteck mit Horizontal- und Vertikalbedingungen*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*Das Rechteck nach Anwendung des Werkzeugs*



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/de
