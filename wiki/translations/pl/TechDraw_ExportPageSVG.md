---
- GuiCommand:/pl
   Name:TechDraw ExportPageSVG
   Name/pl:Rysunek Techniczny: Wyeksportuj stronę do formatu SVG
   MenuLocation:Rysunek Techniczny → Strona → Wyeksportuj stronę do formatu SVG
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Szablony](TechDraw_Templates/pl.md), [SVG](Draft_SVG/pl.md)
---

# TechDraw ExportPageSVG/pl



## Opis

Narzędzie **Wyeksportuj stronę do formatu SVG** zapisuje bieżącą stronę rysunku jako plik [SVG](SVG/pl.md).



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ExportPageSVG.svg" width=16px> [Export Page as SVG](TechDraw_ExportPageSVG/pl.md)**.
    -   Wybierz opcję z menu **TechDraw → Strona → <img src="images/TechDraw_ExportPageSVG.svg" width=16px> Eksportuj stronę jako SVG**.
    -   Jeśli strona jest wyświetlana w [głównym obszarze widoku](Main_view_area/pl.md): kliknij prawym przyciskiem myszki okno strony i wybierz opcję **Eksportuj do formatu SVG** z menu podręcznego.
3.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: <small>(v0.20)</small> .
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
4.  Otworzy się okno dialogowe **Eksportuj stronę do formatu SVG**.
5.  Wybierz lokalizację i nazwę pliku.



## Uwagi

-   Wzory [kreskowania](TechDraw_Hatch/pl.md) nie są eksportowane do pliku [SVG](SVG/pl.md) z powodu ograniczeń w obsłudze SVG w Qt4.
-   Pozycje i rozmiary tekstu nie są poprawne w wyeksportowanym pliku. Użycie domyślnej czcionki \"systemowej\" na rysunku znacznie poprawia problem z rozmiarem.



## Tworzenie skryptów 

Zobacz również strony: [Autogenerowana dokumentacja API](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wyeksportuj stronę do formatu SVG** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath)
```

Należy pamiętać, że moduł FreeCADGui musi być aktywny, aby korzystać z tej funkcji.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageSVG/pl
