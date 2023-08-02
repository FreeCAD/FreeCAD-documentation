---
- GuiCommand:
   Name: Std ViewIvStereoInterleavedColumns
   Name/de: Std AnsichtStereoVersetzteSpalten
   MenuLocation: Ansicht -> Stereo -> Vertikales Interlacing
   Workbenches: Alle
   SeeAlso: Std_ViewIvStereoRedGreen/de, Std_ViewIvStereoQuadBuff/de, Std_ViewIvStereoInterleavedRows/de, Std_ViewIvStereoOff/de
---

# Std ViewIvStereoInterleavedColumns/de



## Beschreibung

Der Befehl **Std AnsichtStereoVersetzteSpalten** stellt den Stereo-Modus der aktiven [3D-Ansicht](3D_view/de.md) auf Vertikales Interlacing um. Zur Verwendung dieses Stereo-Modus wird eine spezielle Grafikkarte, ein spezieller Bildschirm und eine Brille mit Polarisationsfilter-Gläsern. Siehe [glasses with polarized lenses](https://en.wikipedia.org/wiki/Polarized_3D_system) (engl.).



## Anwendung

1.  Den Menüeintrag **Ansicht → Stereo → <img src="images/Std_ViewIvStereoInterleavedColumns.svg" width=16px> Vertikales Interlacing** auswählen.



## Einstellungen

-   Der Augenabstand kann in den Einstellungen geändert werden: **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Augenabstand für Stereo-Modi**. Siehe [Einstellungseditor](Preferences_Editor/de#3D-Viewer.md).



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf Vertikales Interlacing (interleaved columns) zu ändern, wird die Methode `setStereoType` des ActiveView-Objekts verwendet. Diese Methode steht nicht zur Verfügung, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedColumns')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoInterleavedColumns/de
