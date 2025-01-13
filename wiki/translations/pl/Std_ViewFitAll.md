---
 GuiCommand:
   Name: Std ViewFitAll
   Name/pl: Std: Dopasuj wszystko
   MenuLocation: Widok , Widoki standardowe , Dopasuj wszystko
   Workbenches: wszystkie
   Shortcut: **V** , **F**
   SeeAlso: Std_ViewFitSelection/pl
---

# Std ViewFitAll/pl



## Opis

Polecenie **Przybliż i dopasuj wszystko** powiększa i przesuwa ujęcie widoku tak, że wszystkie widoczne obiekty mieszczą się w aktywnym oknie [widoku 3D](3D_view/pl.md).



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewFitAll.svg" width=16px> [Przybliż i dopasuj wszystko](Std_ViewFitAll/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewFitAll.svg" width=16px> Przybliż i dopasuj wszystko**.
    -   Wybierz z menu opcję **<img src="images/Std_ViewFitAll.svg" width=16px> Przybliż i dopasuj wszystko** z menu kontekstowego w oknie [widoku 3D](3D_view/pl.md).
    -   Wybierz opcję **<img src="images/Std_ViewFitAll.svg" width=16px> Dopasuj wszystko** z menu minikostki [kostki nawigacyjnej](Navigation_Cube/pl.md).
    -   Użyj skrótu klawiaturowego: **V**, a następnie **F**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Przybliż i dopasuj wszystko*, należy użyć metody `fitAll` obiektu ActiveView.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.fitAll()
```

Alternatywnie można użyć metody `SendMsgToActiveView` obiektu FreeCADGui.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView("ViewFit")
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFitAll/pl
