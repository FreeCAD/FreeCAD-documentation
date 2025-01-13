---
 GuiCommand:
   Name: Std ViewZoomIn
   Name/pl: Std: Przybliż widok
   MenuLocation: Widok , Powiększenie , Przybliż
   Workbenches: wszystkie
   Shortcut: **Ctrl** + **+**
   SeeAlso: Std_ViewZoomOut/pl, Std_ViewBoxZoom/pl
---

# Std ViewZoomIn/pl



## Opis

Polecenie **Przybliż** powoduje powiększenie aktywnego widoku w oknie [widoku 3D](3D_view/pl.md).



## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wybierz z menu opcję **Widok → Powiększenie → <img src="images/Std_ViewZoomIn.svg" width=16px> Przybliż**.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **+**.



## Uwagi

-   W prawie wszystkich [stylach nawigacji](Mouse_navigation/pl.md) istnieje również możliwość powiększania / pomniejszenia obrazu za pomocą kółka przewijania myszy.



## Ustawienia

Zobacz też: [Edytor preferencji](Preferences_Editor/pl.md).

-   Współczynnik powiększenia można zmienić w preferencjach: **Edycja → Preferencje ... → Wyświetlanie → Nawigacja → Krok powiększenia**. To ustawienie ma również wpływ na powiększanie za pomocą kółka przewijania.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby powiększyć obraz, użyj metody `zoomIn` obiektu View. Jest też dostępna metoda `zoomOut`.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.zoomIn()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewZoomIn/pl
