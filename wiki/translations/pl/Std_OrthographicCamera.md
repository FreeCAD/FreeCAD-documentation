---
- GuiCommand:
   Name:Std OrthographicCamera
   Name/pl:Std: Widok ortogonalny
   MenuLocation:Widok - Widok ortogonalny
   Workbenches:wszystkie
   Shortcut:**V** - **O**
   SeeAlso:[Widok perspektywy](Std_PerspectiveCamera/pl.md)
---

# Std OrthographicCamera/pl



## Opis

Polecenie **Widok ortogonalny** przełącza ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w tryb widoku ortogonalnego. W tym trybie obiekty znajdujące się dalej od kamery nie wydają się mniejsze od tych, które znajdują się bliżej.

![](images/Std_OrthographicCamera_example.svg ) 
*Dwa sześciany o tych samych wymiarach w widoku ortogonalnym*



## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wybierz z menu opcję **Widok → <img src="images/Std_OrthographicCamera.svg" width=16px> Widok ortogonalny**.
    -   Wybierz opcję **<img src="images/Std_OrthographicCamera.svg" width=16px> Widok ortogonalny** z menu mini kostki [nawigacyjnej](Navigation_Cube/pl.md).
    -   Użyj skrótu klawiaturowego: **V** kolejnie **O**.



## Ustawienia

-   Typ ujęcia widoku można zmienić w preferencjach: **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Typ projekcji**. Wybrany typ będzie używany dla wszystkich widoków 3D wszystkich otwartych dokumentów, a także dla nowych dokumentów. Zobacz dodatkowe informacje o [konfiguracji](Preferences_Editor/pl#Widok_3D.md).



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na ortognalny, należy użyć metody `setCameraType` obiektu ActiveView. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Orthographic')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std OrthographicCamera/pl
