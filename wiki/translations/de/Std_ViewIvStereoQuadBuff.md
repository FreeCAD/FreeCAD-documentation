---
- GuiCommand:
   Name:Std ViewIvStereoQuadBuff
   Name/de:Std AnsichtIvStereoVierfachPuffer
   MenuLocation:Ansicht → Stereo → Stereo Vierfach Puffer
   Workbenches:Alle
   SeeAlso:[Std AnsichtIvStereoRotGrün](Std_ViewIvStereoRedGreen/de.md), [Std AnsichtIvStereoÜberlappteZeilen](Std_ViewIvStereoInterleavedRows/de.md), [Std AnsichtIvStereoÜberlappteSpalten](Std_ViewIvStereoInterleavedColumns/de.md), [Std AnsichtIvStereoAus](Std_ViewIvStereoOff/de.md)
---

# Std ViewIvStereoQuadBuff/de



## Beschreibung

Der **Std AnsichtIvStereoVierfachPuffer** Befehl ändert den aktiven [3D Ansicht](3D_view/de.md) in den Vierfachpuffer Stereoansichtsmodus. Zur Verwendung dieses Stereomodus sind eine spezielle Grafikkarte, ein spezieller Bildschirm und [Shutter Brille](https://en.wikipedia.org/wiki/Active_shutter_3D_system) erforderlich.



## Anwendung

1.  Wähle die **Ansicht → Stereo → <img src="images/Std_ViewIvStereoQuadBuff.svg" width=16px> Stereo Vierfach Puffer** Option aus dem Menü.



## Einstellungen

-   Der Auge zu Auge Abstand kann in den Einstellungen geändert werden: **Bearbeiten → Einstellungen... → Anzeige → 3D Ansicht → Auge zu Auge Abstand für Stereomodi**. Siehe [Einstellungseditor](Preferences_Editor#3D_View/de.md).



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf Vierfach Puffer Stereo zu ändern, verwende die Methode `setStereoType` des AktivAnsicht Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('QuadBuffer')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewIvStereoQuadBuff/de
