---
- GuiCommand:/de
   Name:Sketcher RemoveAxesAlignment
   Name/de:Sketcher AchsenausrichtungenEntfernen
   MenuLocation:Sketch → Skizzen-Werkzeuge → Achsenausrichtung entfernen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**Z** **R**
   Version:0.20
---

# Sketcher RemoveAxesAlignment/de

## Beschreibung

Dieses Werkzeug entfernt die Achsenausrichtungen (die Randbedingungen <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [HorizontalFestlegen](Sketcher_ConstrainHorizontal/de.md), <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [VertikalFestlegen](Sketcher_ConstrainVertical/de.md)) von den ausgewählten Elementen und versucht dabei die Beziehungen durch Festlegen neuer Randbedingungen zu erhalten.

## Anwendung

1.  Geometrie mit Achsenausrichtungen auswählen, z.B. ein [Rechteck](Sketcher_CreateRectangle/de.md).
2.  Die Schaltfläche <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> **Achsenausrichtung entfernen** drücken.

Als Ergebnis werden die Randbedingungen HorizontalFestlegen und VertikalFestlegen entfernt. Im Beispiel bleibt das Rechteck ein Rechteck kann aber jetzt gedreht werden.

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*Ein ausgewähltes Rechteck mit Horizontal- und Vertikalbedingungen*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*Das Rechteck nach der Anwendung von Achsausrichtung entfernen*





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/de
