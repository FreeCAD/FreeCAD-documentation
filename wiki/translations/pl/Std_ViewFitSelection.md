---
 GuiCommand:
   Name: Std ViewFitSelection
   Name/pl: Std: Widok dopasowany do wyboru
   MenuLocation: Widok , Widoki standardowe , Dopasuj do wyboru
   Workbenches: wszystkie
   Shortcut: **V** , **S**
   SeeAlso: Std_ViewFitAll/pl
---

# Std ViewFitSelection/pl



## Opis

Polecenie **Dopasuj do wyboru** powiększa i przesuwa ujęcie widoku tak, że wszystkie wybrane obiekty mieszczą się w aktywnym oknie [widoku 3D](3D_view/pl.md). Polecenie to jest przydatne w przypadkach, gdy z jakiegoś powodu obiekty znajdują się poza granicami bieżącego widoku 3D lub nie mogą być łatwo znalezione przy użyciu [nawigacji myszką](Mouse_navigation/pl.md).



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewFitSelection.svg" width=16px> [Dopasuj do wyboru](Std_ViewFitSelection/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewFitSelection.svg" width=24px>Dopasuj do wyboru**.
    -   Wybierz z menu opcję **<img src="images/Std_ViewFitSelection.svg" width=24px> Dopasuj do wyboru** z menu kontekstowego w oknie [widoku 3D](3D_view/pl.md).
    -   Wybierz opcję **<img src="images/Std_ViewFitSelection.svg" width=16px> Dopasuj do widoku** z menu mini kostki [kostki nawigacyjnej](Navigation_Cube/pl.md).
    -   Użyj skrótu klawiaturowego: **V**, a następnie **S**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na *dopasowany do wyboru* można użyć metody `SendMsgToActiveView` obiektu FreeCADGui.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView("ViewSelection")
```



---
⏵ [documentation index](../README.md) > Std ViewFitSelection/pl
