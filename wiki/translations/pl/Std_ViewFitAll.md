---
- GuiCommand   */pl
   Name   *Std ViewFitAll
   Name/pl   *Std   * Dopasuj wszystko
   MenuLocation   *Widok → Widoki standardowe → Dopasuj wszystko
   Workbenches   *wszystkie
   Shortcut   ***V** → **F**
   SeeAlso   *[Widok dopasowany do wyboru](Std_ViewFitSelection/pl.md)
---

# Std ViewFitAll/pl

## Opis

Polecenie **Przybliż i dopasuj wszystko** powiększa i przesuwa ujęcie widoku tak, że wszystkie widoczne obiekty mieszczą się w aktywnym oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie tego polecenia   *
    -   Naciśnij przycisk **<img src="images/Std_ViewFitAll.svg" width=16px> [Przybliż i dopasuj wszystko](Std_ViewFitAll/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewFitAll.svg" width=16px> Przybliż i dopasuj wszystko**.
    -   Wybierz z menu opcję **<img src="images/Std_ViewFitAll.svg" width=16px> Przybliż i dopasuj wszystko** z menu kontekstowego w oknie [widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego   * **V**, a następnie **F**.

## Uwagi

-   Można również przełączyć się do trybu widoku *Przybliż i dopasuj wszystko* za pomocą menu Mini-sześcianu [kostki nawigacyjnej](Navigation_Cube/pl.md).

## Tworzenie skryptów 


**Zobacz również   ***

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Przybliż i dopasuj wszystko*, należy użyć metody `fitAll` obiektu ActiveView. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

Alternatywnie można użyć metody `SendMsgToActiveView` obiektu FreeCADGui. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewFitAll/pl
