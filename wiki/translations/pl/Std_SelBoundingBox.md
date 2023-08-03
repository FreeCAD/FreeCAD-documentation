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

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_SelBoundingBox.svg" width=16px> [Ramka otaczająca](Std_SelBoundingBox/pl.md)**.
    -   Wybierz opcję z menu **Widok → <img src="images/Std_SelBoundingBox.svg" width=16px> Ramka otaczająca**.



## Ustawienia

Odpowiednie ustawienie jest zapisywane w: **Przybory → Edycja parametrów ... → BaseApp → Preferences → View → ShowSelectionBoundingBox**. Jest to wartość typu {{value|boolean}}, domyślnie ustawiona na wartość {{FALSE/pl}}.



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić ustawienie `ShowSelectionBoundingBox`, należy użyć metody `SetBool` odpowiedniego parametru `ParameterGrp`. Przykładowy kod nie działa, jeśli program FreeCAD jest uruchomiony w trybie konsoli.


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
⏵ [documentation index](../README.md) > Std SelBoundingBox/pl
