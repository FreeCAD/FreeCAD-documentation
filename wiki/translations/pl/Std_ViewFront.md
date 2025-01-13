---
 GuiCommand:
   Name: Std ViewFront
   Name/pl: Std: Widok od przodu
   MenuLocation: Widok , Widoki standardowe , Od przodu
   Workbenches: wszystkie
   Shortcut: **1**
   SeeAlso: Std_ViewTop/pl, Std_ViewRight/pl
---

# Std ViewFront/pl



## Opis

Polecenie **Widok od przodu** ustawia ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w kierunku dodatnim osi Y.

![](images/FreeCAD_views_front.svg ) 
*Strzałka 1 wskazuje kierunek widoku z przodu.*



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewFront.svg" width=16px> [Od przodu](Std_ViewFront/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewFront.svg" width=16px> Od przodu**.
    -   Z menu podręcznego [widoku 3D](3D_view/pl.md) wybierz opcję **Widoki standardowe → <img src="images/Std_ViewFront.svg" width=16px> Od przodu**.
    -   Użyj skrótu klawiaturowego: **1**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Od przodu*, należy użyć metody `viewFront`. Dostępne są też metody dla pozostąłych głównych orientacji widoku: `viewTop`, `viewRight`, `viewRear`, `viewBottom` i `viewRight`.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewFront()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFront/pl
