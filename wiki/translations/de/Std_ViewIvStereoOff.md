---
- GuiCommand:/de
   Name:Std ViewIvStereoOff
   Name/de:Std AnsichtStereoAus
   MenuLocation:Ansicht → Stereo → Stereo aus
   Workbenches:Alle
   SeeAlso:[Std AnsichtStereoRotGrün](Std_ViewIvStereoRedGreen/de.md), [Std AnsichtStereoVierfachPuffer](Std_ViewIvStereoQuadBuff/de.md), [Std AnsichtStereoVersetzteZeilen](Std_ViewIvStereoInterleavedRows/de.md), [Std AnsichtStereoVersetzteSpalten](Std_ViewIvStereoInterleavedColumns/de.md)
---

# Std ViewIvStereoOff/de



## Beschreibung

Der Befehl **Std AnsichtStereoAus** schaltet den Stereo-Modus in der aktiven [3D-Ansicht](3D_view/de.md) aus.



## Anwendung

1.  Den Menüeintrag **Ansicht → Stereo → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Stereo aus** auswählen.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um den Stereo-Modus der Ansicht zu beenden, wird die Methode `setStereoType` des ActiveView-Objekts verwendet. Diese Methode steht nicht zur Verfügung, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('None')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoOff/de
