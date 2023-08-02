---
- GuiCommand:
   Name/de: Std WahlBegrenzungRahmen
   MenuLocation: Ansicht -> Begrenzungsrahmen
   Workbenches: Alle
   Version: 0.19
   SeeAlso: Std_DrawStyle/de
---

# Std SelBoundingBox/de



## Beschreibung

Der **Std WahlBegrenzungRahmen** Befehl schaltet den Modus der globalen Begrenzungsrahmenhervorhebung ein und aus. Wenn dieser Modus eingeschaltet ist, werden ausgewählte Objekte in einer [3D Ansicht](3D_view/de.md) mit einem hervorgehobenen Begrenzungsrahmen markiert, auch wenn ihr {{PropertyView/de|Auswahlstil}} auf \'Form\' eingestellt ist.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Std_SelBoundingBox.svg" width=16px> [Std SelBoundingBox](Std_SelBoundingBox.md)** Schaltfläche.
    -   Wähle die **Ansicht → <img src="images/Std_SelBoundingBox.svg" width=16px> Begrenzungsrahmen** Option aus dem Menü.



## Einstellungen

Die zugehörige Einstellung wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Einstellungen → Anzeige → ZeigeAuswahlBegrenzungsRahmen**. Es ist ein boolscher Wert, die Vorgabe ist `False`.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die AnzeigeAuswahlBegrenzungRahmen Einstellung zu ändern, verwende die `SetBool` Methode des entsprechenden ParameterGrp. Das Code Beispiel funktioniert nicht, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/View')
if grp.GetBool('ShowSelectionBoundingBox'):
  grp.SetBool('ShowSelectionBoundingBox',False)
else:
  grp.SetBool('ShowSelectionBoundingBox',True)

FreeCADGui.updateCommands()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SelBoundingBox/de
