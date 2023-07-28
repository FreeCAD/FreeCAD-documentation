---
- GuiCommand:/pl
   Name:TechDraw SpreadsheetView
   name/pl:Rysunek Techniczny: Wstaw widok Arkusza kalkulacyjnego
   MenuLocation:Rysunek Techniczny → Wstaw widok Arkusza kalkulacyjnego
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md), [Arkusz kalkulacyjny](Spreadsheet_Workbench/pl.md)
---

# TechDraw SpreadsheetView/pl


</div>



## Opis

Narzędzie **Wstaw widok Arkusza kalkulacyjnego** pozwala na umieszczenie widoku wybranego [arkusza kalkulacyjnego](Spreadsheet_Workbench/pl.md) na [stronie](TechDraw_Workbench/pl.md) rysunku.

![](images/TechDraw_Spreadsheetview.png ) 
*Element arkusza kalkulacyjnego wstawiony do strony Rysunku Technicznego*



## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz arkusz kalkulacyjny w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Naciśnij przycisk **<img src="images/TechDraw_SpreadsheetView.svg" width=16px> '''Wstaw widok Arkusza kalkulacyjnego'''**.


</div>



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
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/pl
