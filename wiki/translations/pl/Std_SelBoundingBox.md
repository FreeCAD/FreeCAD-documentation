---
 GuiCommand:
   Name: Std SelBoundingBox
   Name/pl: Std: Ramka otaczająca
   MenuLocation: Widok , Ramka otaczająca
   Workbenches: wszystkie
   Version: 0.19
   SeeAlso: Std_DrawStyle/pl
---

# Std SelBoundingBox/pl



## Opis

Polecenie **Ramka otaczająca** włącza globalny tryb wyróżniania ramek obramowań. Jeśli ten tryb jest włączony, wybrane obiekty są oznaczane w oknie [widoku 3D](3D_view/pl.md) podświetlonym obramowaniem, nawet jeśli ich parametr **Styl zaznaczenia** jest ustawiony na wartość `Kształt`.



## Użycie

#\* Wybierz opcję z menu **Widok → <img src="images/Std_SelBoundingBox.svg" width=16px> Ramka otaczająca**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić parametr ShowSelectionBoundingBox, należy użyć metody `SetBool` odpowiedniego ParameterGrp.


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
⏵ [documentation index](../README.md) > Std SelBoundingBox/pl
