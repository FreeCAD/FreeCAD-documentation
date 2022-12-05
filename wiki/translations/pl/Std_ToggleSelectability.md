---
- GuiCommand:/pl
   Name:Std ToggleSelectability
   Name/pl:Std: Przełącz możliwość zaznaczenia
   MenuLocation:Widok → Widoczność → Przełącz możliwość zaznaczenia
   Workbenches:wszystkie
---

# Std ToggleSelectability/pl

## Opis

Polecenie **Przełącz możliwość zaznaczenia** przełącza możliwość wyboru obiektów w oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz z opcję menu **Widok → Widoczność → <img src="images/Std_ToggleSelectability.svg" width=16px> Przełącz możliwość zaznaczenia**.
    -   Wybierz z opcję **<img src="images/Std_ToggleSelectability.svg" width=16px> Przełącz możliwość zaznaczenia** z menu podręcznego [Widoku drzewa](Tree_view/pl.md). Opcja ta nie jest dostępna w środowisku pracy [PartDesign Workbench](PartDesign_Workbench/pl.md)
    -   Wybierz opcję **<img src="images/Std_ToggleSelectability.svg" width=16px> Przełącz możliwość zaznaczenia** z menu kontekstowego widoku 3D.

## Uwagi

-   Wybieralność obiektu można również zmienić poprzez jego powiązaną właściwość **Selectable** w [Edytorze właściwości](Property_editor/pl.md) lub oknie [Widoku połączonego](Combo_view/pl.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Właściwość `Selectable` obiektu określa jego możliwość zaznaczenia.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Selectable == True:
  obj.Selectable = False
else:
  obj.Selectable = True
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ToggleSelectability/pl
