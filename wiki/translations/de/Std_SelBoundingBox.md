---
 GuiCommand:
   Name/de: Std WahlBegrenzungRahmen
   MenuLocation: Ansicht , Begrenzungsrahmen
   Workbenches: Alle
   Version: 0.19
   SeeAlso: Std_DrawStyle/de
---

# Std SelBoundingBox/de



## Beschreibung

Der **Std WahlBegrenzungRahmen** Befehl schaltet den Modus der globalen Begrenzungsrahmenhervorhebung ein und aus. Wenn dieser Modus eingeschaltet ist, werden ausgewählte Objekte in einer [3D Ansicht](3D_view/de.md) mit einem hervorgehobenen Begrenzungsrahmen markiert, auch wenn ihr {{PropertyView/de|Auswahlstil}} auf \'Form\' eingestellt ist.



## Anwendung

#\* Die Menüoption **Ansicht → <img src="images/Std_SelBoundingBox.svg" width=16px> Begrenzungsrahmen** auswählen.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um den Parameter ShowSelectionBoundingBox zu ändern, wird die Methode `SetBool` des entsprechenden Parameters grp verwendet.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View")
if grp.GetBool("ShowSelectionBoundingBox"):
    grp.SetBool("ShowSelectionBoundingBox", False)
else:
    grp.SetBool("ShowSelectionBoundingBox", True)

FreeCADGui.updateCommands()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std SelBoundingBox/de
