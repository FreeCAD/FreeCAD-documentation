# Drawing Workbench/pl
**Środowisko pracy '''Kreślenie''' nie jest już dołączone po wersji 0.20.<br>
Jego bardziej zaawansowanym zamiennikiem jest [Rysunek Techniczny](TechDraw_Workbench/pl.md).**

<img alt="Ikonka FreeCAD dla środowiska pracy Kreślenie" src=images/Workbench_Drawing.svg  style="width:128px;">



## Wprowadzenie

Środowisko pracy Drawing pozwala na umieszczenie na papierze modelu 3D. Oznacza to, że możesz umieścić widoki obiektu w oknie 2D i wstawić to okno do rysunku. Na przykład stronę z ramką, tytułem i logo, a następnie wydrukować tę stronę.




<img alt="" src=images/Drawing_extraction.png  style="width:600px;">



## Przybory

Narzędzia do tworzenia, konfigurowania i eksportowania arkuszy rysunków 2D.

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Otwórz skalowalna grafike wektorową](Drawing_Open_SVG.md): Otwiera arkusz rysunku wcześniej zapisany jako plik SVG.

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Wstaw nowy rysunek](Drawing_Landscape_A3.md): Tworzy nowy arkusz rysunku z domyślnego szablonu A3 programu FreeCAD.

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Wstaw nowy widok \...](Drawing_View.md): Wstawia widok wybranego obiektu w aktywnym arkuszu rysunku.

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Wstaw adnotację](Drawing_Annotation.md): Dodaje adnotację do aktualnego arkusza rysunku.

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Spinacz](Drawing_Clip.md): Dodaje grupę elementów złączników do aktualnego arkusza rysunku.

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Otwórz widok w przeglądarce](Drawing_Openbrowser.md): Otwiera podgląd aktualnego arkusza w przeglądarce.

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Wstaw widok ortogonalny](Drawing_Orthoviews.md): Automatycznie tworzy widoki ortograficzne obiektu na aktualnym arkuszu rysunku.

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Dodaje treść pliku SVG jako symbol na aktualnym arkuszu rysunku.

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Widok szkicu](Draft_Drawing.md): Wstawia specjalny widok roboczy zaznaczonego obiektu w aktualnym arkuszu rysunku.

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Widok arkusza kalkulacyjnego](Drawing_SpreadsheetView.md): Wstawia widok wybranego arkusza kalkulacyjnego do bieżącego arkusza rysunku.

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Zapisz stronę](Drawing_Save.md): Zapisuje aktualny arkusz jako plik SVG.

-   [Kształt projektu](Drawing_ProjectShape.md): Tworzy widok wybranego obiektu (Źródło) w widoku 3D.

-    **Uwaga:**narzędzie [Drawing](Draft_Drawing.md) jest używane z [Draft objects](Draft_Workbench.md). Ma pewne dodatkowe możliwości w stosunku do narzędzi Drawing i obsługuje określone obiekty, takie jak [wymiary](Draft_Dimension.md).

## Organizacja pracy 

Dokument zawiera obiekt kształtu 3D *(leg)*, z którego chcemy wykonać rysunek. Dlatego też tworzona jest nowa **strona**. Jest ona generowana z szablonu, na przykład szablonu **A3_Landscape**. Szablon jest dokumentem [SVG](SVG/pl.md), który może pomieścić ramkę strony, logo i inne elementy.

Na tej stronie możemy wstawić jeden lub więcej widoków. Każdy widok posiada pozycję na stronie, współczynnik skali i dodatkowe właściwości. Za każdym razem, gdy zmienia się strona, widok lub obiekt, do którego się odwołuje, strona jest ponownie odtwarzana i wyświetlany jest zaktualizowany widok.



## Tworzenie skryptów 

W chwili obecnej graficzny interfejs użytkownika jest bardzo ograniczony, więc interfejs API skryptów jest bardziej interesujący.

Opis funkcji używanych do tworzenia stron rysunku i widoków znajduje się na stronie [Przykład rysunku API](Drawing_API_example.md).



## Rozszerzanie Środowiska pracy Drawing 

Niektóre uwagi dotyczące programowania Środowiska pracy Drawing zostaną dodane do strony [Dokumentacja rysunkowa](Drawing_Documentation.md). Ma to pomóc w szybkim zrozumieniu sposobu działania Środowiska pracy Drawing, umożliwiając programistom sprawne rozpoczęcie programowania.



## Zewnętrzne odnośniki internetowe 

-   [Wprowadzenie do rysunku mechanicznego na Youtube - według Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)





{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/pl
