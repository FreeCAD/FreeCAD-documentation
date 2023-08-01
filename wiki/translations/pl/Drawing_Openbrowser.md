---
- GuiCommand:
   Name:Drawing Openbrowser
   Name/pl:Otwórz przeglądarkę WEB
   Workbenches:[Drawing](Drawing_Workbench/pl.md)
   MenuLocation:Rysunek → Otwiera wybrana stronę w przeglądarce
   Shortcut:brak
---

# Drawing Openbrowser/pl



## Opis

To polecenie pozwala wyświetlić wybraną [Stronę rysunku](Drawing_Landscape_A3/pl.md) za pomocą wewnętrznej przeglądarki internetowej FreeCAD. Normalna przeglądarka stron rysunku w programie FreeCAD jest oparta na [wbudowanym module renderującym SVG Qt](http://qt-project.org/doc/qt-5.0/qtsvg/svgrendering.html), który obsługuje tylko niewielki podzbiór pełnego Specyfikacja SVG. W rezultacie niektóre bardziej zaawansowane funkcje SVG, takie jak wypełnienie wzorkiem lub tekst wielowierszowy, nie są obsługiwane przez tę przeglądarkę. Wewnętrzna przeglądarka internetowa FreeCAD jest jednak zbudowana na [Webkit](http://en.wikipedia.org/wiki/WebKit), który jest jednym z najlepszych dostępnych programów renderujących SVG i poprawnie renderuje twoją stronę ze wszystkimi jej funkcjami.



## Użycie

1.  Utwórz [Stronę rysunku](Drawing_Landscape_A3/pl.md).
2.  Dodaj trochę [widoków](Drawing_View/pl.md) lub innej zawartości do swojej strony.
3.  [Przeładuj](Std_Refresh.md) widok jeśli widok rysunku nie został otwarty.
4.  Naciśnij przycisk **<img src="images/Drawing_Openbrowser.png" width=16px>** [Otwórz wybraną stronę w przeglądarce](Drawing_Openbrowser/pl.md).



## Ograniczenia

-   Strona otwarta w przeglądarce internetowej nie będzie się automatycznie odświeżać przy zmianach. Musisz użyć prawego przycisku myszy → przeładuj.





{{Drawing Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Openbrowser/pl
