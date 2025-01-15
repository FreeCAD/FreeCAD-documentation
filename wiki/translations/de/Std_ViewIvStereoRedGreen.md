---
 GuiCommand:
   Name: Std ViewIvStereoRedGreen
   Name/de: Std AnsichtStereoRotGrün
   MenuLocation: Ansicht , Stereo , Stereo rot/cyan
   Workbenches: Alle
   SeeAlso: Std_ViewIvStereoQuadBuff/de, Std_ViewIvStereoInterleavedRows/de, Std_ViewIvStereoInterleavedColumns/de, Std_ViewIvStereoOff/de
---

# Std ViewIvStereoRedGreen/de



## Beschreibung

Der Befehl **Std AnsichtStereoRotGrün** stellt den Stereo-Modus der aktiven [3D-Ansicht](3D_view/de.md) auf Stereo rot/cyan um,siehe [anaglyph](https://en.wikipedia.org/wiki/Anaglyph_3D) (engl.). Zur Verwendung dieses Stereo-Modus ist eine Brille mit farbigen Gläsern erforderlich.



## Anwendung

1.  Den Menüeintrag **Ansicht → Stereo → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stereo rot/cyan** auswählen.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Der Augenabstand kann geändert werden: **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Augenabstand für Stereo-Modi**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `setStereoType` des View-Objekts wird verwendet, um den Stereo-Modus der Ansicht auf Stereo rot/cyan zu ändern. Die zur Verfügung stehenden Modi sind `"Anaglyph"`, `"QuadBuffer"`, `"InterleavedRows"`, `"InterleavedColumns"` und `"None"`.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.setStereoType("Anaglyph")
view.getStereoType()
```



---
⏵ [documentation index](../README.md) > Std ViewIvStereoRedGreen/de
