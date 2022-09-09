# TechDraw Templates/pl
{{TOCright}}

## Informacje ogólne 

Każda strona środowiska Rysunek Roboczy jest oparta na obiekcie Szablonu. Szablon określa rozmiar papieru i zawiera stałą grafikę i tekst, na przykład ramkę lub obramowanie strony.

Szablon może również zawierać edytowalne pola tekstowe dla atrybutów takich jak *Tytuł*, *Podtytuł*, *Autor*, *Data*, *Skala*, *Waga*, *Numer rysunku* i *Arkusz*.

Szablony to pliki [SVG](SVG.md), które można tworzyć i modyfikować poza środowiskiem programu FreeCAD, za pomocą aplikacji takiej jak np. [Inkscape](https   *//en.wikipedia.org/wiki/Inkscape).

## Właściwości

-    **Orientacja**   * Portret lub Krajobraz.

-    **Szerokość**   * Szerokość papieru w mm.

-    **Wysokość**   * Wysokość papieru w mm.

-    **Strona Wynikowa**   * Kopia oryginalnego pliku Szablonu zawierająca wszystkie zmiany w edytowalnych tekstach. Pozwala to użytkownikom, którzy mogą nie mieć kopii pliku Szablonu, zobaczyć stronę zgodnie ze swoim przeznaczeniem. Nie jest to typowo przydatne dla użytkowników końcowych.

-    **Szablon**   * a) wskaźnik do kopii oryginalnego pliku Szablonu, który jest włączony do tego pliku \*.FCStd, lub b) ścieżka do pliku szablonu dostępnego na bieżącym komputerze. Użyj wielokropka przy wyborze pliku *(\...)*, aby zmienić szablon na inny.

## Wybór innego pliku szablonu 

Aby wybrać inny szablon dla rysunku   *

1.  Zlokalizuj żądany obiekt Strony w [Widoku drzewa](Tree_view/pl.md).
2.  Rozwiń węzeł Strona, jeśli to konieczne.
3.  Wybierz obiekt Szablon.
4.  W [Edytorze właściwości](Property_editor/pl.md) kliknij w polu właściwości **Szablon**.
5.  Naciśnij przycisk **...** *(wielokropek)*, który się pojawi.
6.  Otwiera się okno dialogowe plik, w którym znajduje się folder z aktualnym szablonem. Jeżeli Strona została utworzona w bieżącej sesji FreeCAD będzie to domyślny folder szablonu *(skonfigurowany w [Ustawieniach Rysunku Technicznego](TechDraw_Preferences/pl#Plik.md))*.
7.  Opcjonalnie przejdź do innego folderu.
8.  Wybierz inny plik szablonu.
9.  Naciśnij przycisk **OK**.

Jeśli zmodyfikowałeś plik szablonu i chcesz zaktualizować Stronę utworzoną w bieżącej sesji FreeCAD, która używa tego szablonu, tymczasowo wybierz najpierw inny plik, a następnie ponownie wybierz zmodyfikowany plik.

## Szablony użytkownika 

Do programu FreeCAD dołączona jest niewielka liczba wstępnie sformatowanych szablonów w różnych standardowych rozmiarach stron. Znajdują się one w   *


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

Gdzie `$INSTALL_DIR` to katalog, w którym zainstalowano FreeCAD, na przykład   *


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

Szablony własne można również określić jako domyślne w [Ustawieniach](TechDraw_Preferences/pl.md) środowiska Rysunek Techniczny.

Zobacz również stronę [Jak stworzyć własny szablon Rysunku Technicznego](TechDraw_TemplateHowTo/pl.md).

## Uwagi

-   Szablony środowiska pracy Rysunek Techniczny nie są całkowicie zamienne z szablonami [Rysunku Roboczego](Drawing_templates/pl.md). Ogólnie rzecz biorąc, szablony środowiska Rysunku Roboczego będą działać w środowisku Rysunek Techniczny, ale mogą wystąpić problemy z edytowalnym tekstem.

-   Klauzule transform Svg **spowodują problemy** w niestandardowych szablonach. Zobacz dyskusję Stackoverflow na temat [usuwanie klauzul transform w plikach SVG](https   *//stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

-   Klauzula **xml   *space=\"preserve\"** czasami powoduje problemy z rozmiarem i pozycjonowaniem tekstu. Najlepiej jest unikać / usunąć tę klauzulę z kodu SVG twojego niestandardowego szablonu.

-   Szablony działają najlepiej, gdy nie zawierają zbędnego kodu SVG *(nazywanego przez niektórych \"śmieciowym SVG\")*. Istnieje dobry artykuł na temat [usuwanie śmieci z SVG](https   *//freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). Artykuł napisano w języku rosyjskim.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/pl
