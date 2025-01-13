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


{{Version/pl|1.0}}

: Narzędzie [Wstaw widok](TechDraw_View/pl.md) również może utworzyć widok Arkusza kalkulacyjnego .

![](images/TechDraw_Spreadsheetview.png ) 
*Element arkusza kalkulacyjnego wstawiony do strony Rysunku Technicznego*



## Użycie

1.  Wybierz arkusz w [Widoku drzewa](Tree_view.md).
2.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie dodaj żądaną stronę do zaznaczenia, wybierając ją w oknie [Widok drzewa](Tree_view.md).
3.  Wybierz opcję **Rysunek Techniczny → Widoki z innych środowisk roboczych → <img src="images/TechDraw_SpreadsheetView.svg" width=16px> Wstaw widok Arkusza kalkulacyjnego** z menu.
4.  Jeśli w dokumencie znajduje się wiele stron rysunku i jeśli nie ma strony wyświetlonej w [obszarze widoku głównego](Main_view_area/pl.md), a strona nie została jeszcze wybrana, otworzy się okno dialogowe **Wybór strony**:
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
5.  Wstawiony zostanie widok Arkusza kalkulacyjnego.
6.  Dostosuj zakres komórek widoku, zmieniając jego właściwości **Komórka początkowa** i **Komórka końcowa**.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Widok Arkusza kalkulacyjnego, formalnie obiekt {{Incode|TechDraw::DrawViewSpreadsheet}} ma [właściwości](TechDraw_View/pl#Właściwości_-_Widok_części.md) wspólne dla wszystkich typów Widoków. Ma też następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Widok rysunku}}

-    **Symbol|String|Hidden**: Kod SVG definiujący ten symbol.

-    **Editable Texts|StringList**: Wartości podstawienia dla edytowalnych ciągów w tym symbolu.

-    **Owner|Link**: Cecha, do której ten symbol jest dołączony. {{Version/pl|1.0}}


{{TitleProperty|Arkusz kalkulacyjny}}

-    **Żródło|Link**: Arkusz kalkulacyjny, który ma zostać dodany do strony.

-    **Komórka początkowa|String**: Lewa górna komórka zakresu komórek, który ma zostać uwzględniony w tym widoku.

-    **Komórka końcowa|String**: Prawa dolna komórka zakresu komórek, który ma być uwzględniony w tym widoku.

-    **Czcionka|Font**: Nazwa czcionki używanej dla tekstów.

-    **Kolor tekstu|Color**: Kolor tekstów i linii, które nie mają określonego koloru w arkuszu kalkulacyjnym.

-    **Rozmiar tekstu|Float**: Rozmiar czcionki tekstu.

-    **Szerokość linii|Float**: Szerokość obramowania komórki.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/pl
