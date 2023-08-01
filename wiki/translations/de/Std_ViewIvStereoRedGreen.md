---
- GuiCommand:/de
   Name:Std ViewIvStereoRedGreen
   Name/de:Std AnsichtStereoRotGrün
   MenuLocation:Ansicht → Stereo → Stereo rot/cyan
   Workbenches:Alle
   SeeAlso:[Std AnsichtStereoVierfachPuffer](Std_ViewIvStereoQuadBuff/de.md), [Std AnsichtStereoVersetzteZeilen](Std_ViewIvStereoInterleavedRows/de.md), [Std AnsichtStereoVersetzteSpalten](Std_ViewIvStereoInterleavedColumns/de.md), [Std AnsichtStereoAus](Std_ViewIvStereoOff/de.md)
---

# Std ViewIvStereoRedGreen/de



## Beschreibung

Der Befehl **Std AnsichtStereoRotGrün** stellt den Stereo-Modus der aktiven [3D-Ansicht](3D_view/de.md) auf Stereo rot/cyan um,siehe [anaglyph](https://en.wikipedia.org/wiki/Anaglyph_3D) (engl.). Zur Verwendung dieses Stereo-Modus ist eine Brille mit farbigen Gläsern erforderlich.



## Anwendung

1.  Den Menüeintrag **Ansicht → Stereo → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stereo rot/cyan** auswählen.



## Einstellungen

-   Der Augenabstand kann in den Einstellungen geändert werden: **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Augenabstand für Stereo-Modi**. Siehe [Einstellungseditor](Preferences_Editor/de#3D-Viewer.md).



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um den Stereo-Modus der Ansicht auf Stereo rot/cyan zu ändern, wird die Methode `setStereoType` des ActiveView-Objekts verwendet. Diese Methode steht nicht zur Verfügung, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewIvStereoRedGreen/de
