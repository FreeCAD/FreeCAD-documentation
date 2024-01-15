---
 GuiCommand:
   Name: TechDraw SpreadsheetView
   name/pl: Rysunek Techniczny: Wstaw widok Arkusza kalkulacyjnego
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw widok Arkusza kalkulacyjnego
   Workbenches: TechDraw_Workbench/pl, Spreadsheet_Workbench/pl
---

# TechDraw SpreadsheetView/pl



## Opis

Narzędzie **Wstaw widok Arkusza kalkulacyjnego** pozwala na umieszczenie widoku wybranego [arkusza kalkulacyjnego](Spreadsheet_Workbench/pl.md) na [stronie](TechDraw_Workbench/pl.md) rysunku.

![](images/TechDraw_Spreadsheetview.png ) 
*Element arkusza kalkulacyjnego wstawiony do strony Rysunku Technicznego*



## Użycie

1.  Wybierz pojedynczy arkusz w [Widoku drzewa](Tree_view.md).
2.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie dodaj żądaną stronę do zaznaczenia, wybierając ją w oknie [Widok drzewa](Tree_view.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_SpreadsheetView.svg" width=16px> '''Wstaw widok Arkusza kalkulacyjnego'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Widoki → <img src="images/TechDraw_SpreadsheetView.svg" width=16px>. Wstaw widok arkusza kalkulacyjnego**.
4.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze wybrana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
5.  Dostosuj zakres komórek widoku, zmieniając jego właściwości **Komórka początkowa** i **Komórka końcowa**.



## Uwagi

-   W {{VersionMinus/pl|0.19}} niektóre znaki w komórkach arkusza kalkulacyjnego będą powodować błędy podczas wyświetlania w widoku arkusza kalkulacyjnego. Znaki te muszą być zakodowane w XML. Obecnie znane znaki to: {{Incode|&}} (zamień na {{Incode|&amp;amp;}}) i {{Incode|&lt;}}. (zamień na {{Incode|&amp;lt;}}). Zobacz także tę [dyskusję](https://forum.freecadweb.org/viewtopic.php?p=629853#p629885) na forum.



## Właściwości

Zapoznaj się również informacjami na stronie [właściwości widoku](TechDraw_View/pl#Widok.md) środowiska Rysunek Techniczny.



### Dane


{{TitleProperty|Arkusz kalkulacyjny}}

-    **Żródło|Link**: Arkusz kalkulacyjny, który ma zostać dodany do strony.

-    **Komórka początkowa|String**: Lewa górna komórka zakresu komórek, który ma zostać uwzględniony w tym widoku.

-    **Komórka końcowa|String**: Prawa dolna komórka zakresu komórek, który ma być uwzględniony w tym widoku.

-    **Czcionka|Font**: Nazwa czcionki używanej dla tekstów.

-    **Kolor tekstu|Color**: Kolor tekstów i linii, które nie mają określonego koloru w arkuszu kalkulacyjnym.

-    **Rozmiar tekstu|Float**: Rozmiar czcionki tekstu.

-    **Szerokość linii|Float**: Szerokość obramowania komórki.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/pl
