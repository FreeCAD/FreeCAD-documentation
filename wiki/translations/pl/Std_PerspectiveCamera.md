---
- GuiCommand:/pl
   Name:Std PerspectiveCamera
   Name/pl:Std: Widok perspektywy
   MenuLocation:Widok → Widok perspektywy
   Workbenches:wszystkie
   Shortcut:**V** → **P**
   SeeAlso:[Widok ortograficzny](Std_OrthographicCamera/pl.md)
---

# Std PerspectiveCamera/pl

## Opis

Polecenie **Widok perspektywy** przełącza ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w tryb widoku perspektywy. W tym trybie obiekty znajdujące się dalej od kamery wydają się mniejsze niż te znajdujące się bliżej.

![](images/Std_PerspectiveCamera_example.svg ) 
*Dwa sześciany o tych samych wymiarach w widoku perspektywy*

## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wybierz z menu opcję **Widok → <img src="images/Std_PerspectiveCamera.svg" width=16px> Widok perspektywy**.
    -   Użyj skrótu klawiaturowego: **V** kolejnie **P**.

## Uwagi

-   Można również przełączyć się do trybu widoku perspektywy za pomocą menu Mini-sześcianu [kostki nawigacyjnej](Navigation_Cube/pl.md).

## Ustawienia

-   Typ ujęcia widoku można zmienić w preferencjach: **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Typ projekcji**. Wybrany typ będzie używany dla wszystkich widoków 3D wszystkich otwartych dokumentów, a także dla nowych dokumentów. Zobacz dodatkowe informacje o [konfiguracji](Preferences_Editor/pl#Widok_3D.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok perspektywy, należy użyć metody `setCameraType` obiektu ActiveView. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Perspective')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std PerspectiveCamera/pl
