---
- GuiCommand:
   Name:Std RecallWorkingView
   Name/pl:Std: Odtwórz widok
   MenuLocation:Widok - Widoki standardowe - Odtwórz widok
   Workbenches:wszystkie
   Shortcut:**End**
   Version:0.21
   SeeAlso:[Przechowaj widok roboczy](Std_StoreWorkingView/pl.md), [Zamroź widok](Std_FreezeViews/pl.md)
---

# Std RecallWorkingView/pl



## Opis

Polecenie **Odtwórz widok** przywołuje zapisany widok roboczy aktywnego okna [widoku 3D](3D_view/pl.md). Więcej informacji można znaleźć na stronie [Przechowaj widok roboczy](Std_StoreWorkingView/pl.md).



## Użycie

1.  Upewnij się, że aktywne jest okno [widoku 3D](3D_view/pl.md), dla którego co najmniej raz użyto polecenia [Przechowaj widok roboczy](Std_StoreWorkingView/pl.md).
2.  Polecenie można wywołać na kilka sposobów:
    -   Wybierając z menu opcję **Widok → Widoki standardowe → Odtwórz widok**.
    -   Użyć skrótu klawiaturowego: **End**.



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Odtworzenie zapisanego widoku roboczego do aktywnego okna widoku 3D:


```python
import FreeCADGui

FreeCADGui.runCommand("Std_RecallWorkingView", 0)
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std RecallWorkingView/pl
