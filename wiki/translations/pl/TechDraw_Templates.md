# TechDraw Templates/pl
## Opis

Każda strona środowiska Rysunek Techniczny jest oparta na obiekcie Szablonu. **Szablon** zapewnia obszar na tle strony do wstawiania widoków, symboli i innych obiektów adnotacji oraz definiuje rozmiar arkusza strony. Tylko elementy w obszarze rysunku będą renderowane do eksportu lub drukowania.

Szablon może też zawierać grafiki, takie jak ramka definiująca obszar rysunku włączając pola indeksowe, znaczniki zwijania i opcjonalnie blok tytułowy, który z kolei zawiera stałe i [edytowalne teksty](Svg_Namespace/pl#freecad_editable.md). Blok tytułowy można również wstawić osobno jako [symbol](TechDraw_Symbol/pl.md).

Szablony, tak jak symbole, to pliki [SVG](SVG.md), które można tworzyć i modyfikować poza programem FreeCAD, za pomocą aplikacji takiej jak np. [Inkscape](https://en.wikipedia.org/wiki/Inkscape) lub prostego edytora tekstu. Podobnie jak symbole, mogą zawierać edytowalne pola tekstowe, ale używają innych narzędzi do edycji.

Nowe narzędzie autouzupełniania ({{Version/pl|1.0}}) może automatycznie wypełnić edytowalne pola tekstowe szablonu gdy jest on wstawiany. To wymaga szablonów, które korzystają z nowego atrybutu [freecad:autofill](Svg_Namespace/pl#freecad_autofill.md). Następujące nazwy atrybutów są prawidłowe dla autouzupełniania: \"author\", \"date\", \"organization\", \"scale\", \"sheet\", \"title\", \"page_number\" i \"page_count\".



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Szablon ma następujące właściwości:


{{TitleProperty|Base}}

-    **Orientation|Enumeration**: {{Value|Portrait}} lub {{Value|Landscape}}.


{{TitleProperty|Page Properties}}

-    **Width|Length**: Szerokość arkusza w mm.

-    **Height|Length**: Wysokość arkusza w mm.

-    **Editable Texts|Map|Hidden**: Lista Key:Value edytowalnych tekstów w szablonie.


{{TitleProperty|Template}}

-    **Page Result|FileIncluded**: Kopia oryginalnego pliku szablonu uwzględniająca wszelkie zmiany w edytowalnych tekstach. Pozwala użytkownikom, którzy mogą nie mieć kopii pliku szablonu na zobaczenie strony tak jak ma wyglądać. Nie jest to przydatne dla większości użytkowników końcowych.

-    **Template|File**: Wskazuje kopię oryginalnego pliku szablonu, która jest włączona w ten plik ***.FCStd** lub ścieżkę do szablonu dostępnego na bieżącym komputerze. Zobacz [następny akapit](#Wybór_innego_pliku_szablonu.md) aby uzyskać informacje o tym jak zmienić szablon.



## Wybór innego pliku szablonu 

Aby wybrać inny szablon dla rysunku:

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

Do programu FreeCAD dołączona jest niewielka liczba wstępnie sformatowanych szablonów w różnych standardowych rozmiarach stron. Znajdują się one w:


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

Gdzie `$INSTALL_DIR` to katalog, w którym zainstalowano FreeCAD, na przykład:


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

Szablony własne można również określić jako domyślne w [Ustawieniach](TechDraw_Preferences/pl.md) środowiska Rysunek Techniczny.

Zobacz również stronę [Jak stworzyć własny szablon Rysunku Technicznego](TechDraw_TemplateHowTo/pl.md) lub jeśli wolisz szablony generowane przez skrypt, [Generator szablonów](TechDraw_TemplateGenerator/pl.md) i [Makro TemplateHelper](Macro_TemplateHelper/pl.md).



## Uwagi

-   Biblioteka używana przez FreeCAD do przetwarzania SVG *obsługuje tylko specyfikację svg-tiny*. W szczególności: \"SVG Tiny nie obsługuje gradientów, przezroczystości, przycinania, masek, symboli, wzorów, podkreślania tekstu, przekreślania tekstu, tekstu pionowego ani efektów filtrów SVG\" *(z pomocy programu Adobe Illustrator)*. Użycie tych funkcji w szablonie niestandardowym spowoduje problemy z renderowaniem.

-   Klauzule transform Svg **mogą powodować problemy** w niestandardowych szablonach. Zobacz dyskusję Stackoverflow na temat [usuwanie klauzul transform w plikach SVG](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files), szczególnie jeśli Inkscape użył ich zbyt wielu. Ale nie można ich uniknąć jeśli potrzebny jest obrócony tekst w szablonie.

-   Klauzula **xml:space=\"preserve\"** czasami powoduje problemy z rozmiarem i pozycjonowaniem tekstu. Najlepiej jest unikać / usunąć tę klauzulę z kodu SVG twojego niestandardowego szablonu.

-   Szablony działają najlepiej, gdy nie zawierają zbędnego kodu SVG *(nazywanego przez niektórych \"śmieciowym SVG\")*. Istnieje dobry artykuł na temat [usuwanie śmieci z SVG](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). Artykuł napisano w języku rosyjskim.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/pl
