---
- GuiCommand:
   Name:Sketcher ToggleActiveConstraint
   Name/pl:Szkicownik: Przełącz aktywność wiązania
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   MenuLocation:Szkic → Wiązania szkicownika → Przełącz aktywność wiązania
   Shortcut:**K** **Z**
   Version:0.19
   SeeAlso:[Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md)
---

# Sketcher ToggleActiveConstraint/pl



## Opis

Narzędzie **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Przełącz aktywność wiązania](Sketcher_ToggleActiveConstraint/pl.md)** pozwala aktywować i dezaktywować już nałożone wiązania. Dzięki temu można zachować wiązanie w tle, ale tymczasowo przetestować inny układ istniejącej geometrii.

Narzędzie **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md)** jest podobne w tym, że wyłącza działanie danego wiązania. Jednak w przypadku tego narzędzia wiązanie nie zachowuje swojej starej wartości. Z drugiej strony, z **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Przełącz aktywność wiązania](Sketcher_ToggleActiveConstraint/pl.md)** możesz natychmiast ponownie aktywować stare wiązanie.



## Użycie

1.  Wybierz wiązanie ustawione już wcześniej, a następnie naciśnij **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> '''Przełącz aktywność wiązania'''**.
2.  Alternatywnie, przejdź do [panelu zadań](Task_panel/pl.md), w sekcji **Wiązania**, wybierz wiązanie, następnie otwórz menu podręczne *(kliknij prawym przyciskiem myszy)* i wybierz **Dezaktywuj**.
3.  Aby ponownie aktywować wiązanie, zaznacz je i naciśnij **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> '''Przełącz aktywność wiązania'''** ponownie.



## Przykłady

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:" height="350px;"> 
*W pełni związany szkic.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:" height="350px;"> <img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:" height="350px;"> 
*Po lewej: dezaktywowane wiązanie. Szkic nie jest już w pełni związany.<br>Po prawej: niezwiązana geometria może być przesuwana. Starsze wiązanie jest nadal dostępne i można je ponownie aktywować, aby powrócić do w pełni związanego szkicu.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_task_panel.png  style="width:" height="350px;"> 
*Panel zadań z wyłączonym wiązaniem.*



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aktywny status wiązania może być kontrolowany w [makrodefinicjachs](Macros/pl.md) i z [konsoli środowiska Python](Python_console/pl.md). 
```python
SketchObject.toggleActive(index)
```

Użyj metody `toggleActive` istniejącego [obiektu szkicu](Szkicownik_SketchObject/pl.md) oraz `index` wiązania, aby je aktywować lub dezaktywować. Indeks zaczyna się od `0` aż do `N-1`, gdzie `N` to całkowita liczba więzów.

Przykład: 
```python
import FreeCAD as App

sketch = App.ActiveDocument.Sketch
sketch.toggleActive(3)
```





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/pl
