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

-   Istnieje również możliwość powiększania / pomniejszenia obrazu za pomocą kółka przewijania myszy.

## Ustawienia

-   Współczynnik powiększenia można zmienić w preferencjach: **Edycja → Preferencje ... → Wyświetlanie → Nawigacja → Krok powiększenia**. To ustawienie ma również wpływ na powiększanie za pomocą kółka przewijania. Zobacz informacje na stronie [Edytor ustawień](Preferences_Editor/pl#Nawigacja.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby powiększyć obraz, użyj metody `zoomIn` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomIn()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewZoomIn/pl
