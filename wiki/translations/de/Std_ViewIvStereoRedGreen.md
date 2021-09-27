---
- GuiCommand:/de
   Name:Std ViewAnsichtIvStereoRotGrün
   MenuLocation:Ansicht → Stereo → Stereo rot/cyan
   Workbenches:Alle
   SeeAlso:[Std AnsichtIvStereoVierfachPuffer](Std_ViewIvStereoQuadBuff/de.md), [Std AnsichtIvStereoÜberlappteZeilen](Std_ViewIvStereoInterleavedRows/de.md), [Std AnsichtIvStereoÜberlappteSpalten](Std_ViewIvStereoInterleavedColumns/de.md), [Std AnsichtIvStereoAus](Std_ViewIvStereoOff/de.md)
---

# Std ViewIvStereoRedGreen/de

## Beschreibung

Der **Std AnsichtIvStereoRotGrün** Befehl ändert die aktive [3D Ansicht](3D_view/de.md) in rot/cyan, [anaglyph](https://en.wikipedia.org/wiki/Anaglyph_3D), Stereoansichtsmodus. Zur Verwendung dieses Stereomodus ist eine Brille mit farbigen Gläsern erforderlich.

## Anwendung

1.  Wähle die {{MenuCommand/de|Ansicht → Stereo → _ Stereo rot/cyan}} Option aus dem Menü.

## Einstellungen

-   Der Auge zu Auge Abstand kann in den Einstellungen geändert werden: {{MenuCommand/de|Bearbeiten → Einstellungen... → Anzeige → 3D Ansicht → Auge zu Auge Abstand für Stereomodi}}. Siehe [Einstellungseditor](Preferences_Editor#3D_View.md).

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf Rot/Cyan Stereo zu ändern, verwende die Methode `setStereoType` des AktivAnsicht Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewIvStereoRedGreen/de
