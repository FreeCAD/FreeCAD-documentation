---
- GuiCommand:/de
   Name:Std ViewIvStereoInterleavedRows
   Name/de:Std AnsichtStereoVersetzteZeilen
   MenuLocation:Ansicht → Stereo → Horizontales Interlacing
   Workbenches:Alle
   SeeAlso:[Std AnsichtStereoRotGrün](Std_ViewIvStereoRedGreen/de.md), [Std AnsichtStereoVierfachPuffer](Std_ViewIvStereoQuadBuff/de.md), [Std AnsichtStereoVersetzteSpalten](Std_ViewIvStereoInterleavedColumns/de.md), [Std AnsichtStereoAus](Std_ViewIvStereoOff/de.md)
---

# Std ViewIvStereoInterleavedRows/de



## Beschreibung

Der Befehl **Std AnsichtStereoVersetzteZeilen** stellt den Stereo-Modus der aktiven [3D-Ansicht](3D_view/de.md) auf Horizontales Interlacing um. Zur Verwendung dieses Stereo-Modus wird eine spezielle Grafikkarte, ein spezieller Bildschirm und eine Brille mit Polarisationsfilter-Gläsern. Siehe [glasses with polarized lenses](https://en.wikipedia.org/wiki/Polarized_3D_system) (engl.).



## Anwendung

1.  Den Menüeintrag **Ansicht → Stereo → <img src="images/Std_ViewIvStereoInterleavedRows.svg" width=16px> Horizontales Interlacing** auswählen.



## Einstellungen

-   Der Augenabstand kann in den Einstellungen geändert werden: **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Augenabstand für Stereo-Modi**. Siehe [Einstellungseditor](Preferences_Editor/de#3D-Viewer.md).



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf Horizontales Interlacing (interleaved rows) zu ändern, wird die Methode `setStereoType` des ActiveView-Objekts verwendet. Diese Methode steht nicht zur Verfügung, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedRows')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoInterleavedRows/de
