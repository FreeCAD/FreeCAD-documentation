---
 GuiCommand:
   Name: Sketcher ToggleActiveConstraint
   Name/pl: Szkicownik: Przełącz aktywność wiązania
   Workbenches: Sketcher_Workbench/pl
   MenuLocation: Szkic , Wiązania szkicownika , Przełącz aktywność wiązania
   Shortcut: **K** **Z**
   Version: 0.19
   SeeAlso: Sketcher_ToggleDrivingConstraint/pl
---

# Sketcher ToggleActiveConstraint/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:24px;"> **Przełącz aktywność wiązania** aktywuje lub dezaktywuje wybrane wiązania. Dezaktywacja wiązań pozwala na testowanie innych układów geometrii bez usuwania wiązań.

Jest to narzędzie podobne do [Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md), ale w przeciwieństwie do niego działa również dla wiązań geometrycznych, a wartości dezaktywowanych wiązań wymiarowych są zachowywane.



## Użycie

1.  Wybierz jedno lub więcej wiązań.
2.  Istnieje kilka sposobów wywołania tego narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> '''Przełącz aktywność wiązania'''**.

    -   Wybierz z menu **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Przełącz aktywność wiązania**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Przełącz aktywność wiązania** z menu podręcznego.

    -   W sekcji **Wiązania** [okna dialogowego](Sketcher_Dialog/pl.md) wybierz opcję **Aktywuj** lub **Dezaktywuj** z menu podręcznego. Oferowana opcja zależy od wybranego stanu wybranego wiązania.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **Z**.
3.  Aktywne wybrane wiązania są dezaktywowane i zmieniają kolor na szary *(domyślny [kolor](Sketcher_Preferences#Wygląd.md))*, podczas gdy wybrane dezaktywowane wiązania są aktywowane i powracają do koloru czerwonego *(domyślny kolor)*.



## Przykład

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:400px;"> 
*W pełni związany szkic.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:400px;"> 
*Jedno z wiązań kątowych zostało dezaktywowane, szkic nie jest już w pełni wiązany.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:400px;"> 
*Geometria bez wiązań może być przemieszczana. Dezaktywowane wiązanie jest nadal dostępne i można je ponownie aktywować, aby powrócić do w pełni związanego szkicu.*



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aktywny status wiązania może być kontrolowany w [makrodefinicjachs](Macros/pl.md) i z [konsoli środowiska Python](Python_console/pl.md). 
```python
SketchObject.toggleActive(index)
```

Użyj metody `toggleActive` istniejącego [obiektu szkicu](Sketcher_SketchObject/pl.md) oraz `index` wiązania, aby je aktywować lub dezaktywować. Indeks zaczyna się od `0` aż do `N-1`, gdzie `N` to całkowita liczba więzów.

Przykład: 
```python
import FreeCAD as App

sketch = App.ActiveDocument.Sketch
sketch.toggleActive(3)
```



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/pl
