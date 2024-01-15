---
 GuiCommand:
   Name: TechDraw Annotation
   Name/pl: Rysunek Techniczny: Wstaw adnotację
   MenuLocation: Rysunek Techniczny , Adnotacje , Wstaw adnotację
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_RichTextAnnotation/pl
---

# TechDraw Annotation/pl



## Opis

Narzędzie *Wstaw adnotację* dodaje blok tekstu do strony rysunku.

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Adnotacja na stronie rysunku.*



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj wymaganą stronę, wybierając ją w [Widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
3.  Naciśnij przycisk **<img src="images/TechDraw_Annotation.svg" width=24px> '''Wstaw adnotację'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Adnotacje → <img src="images/TechDraw_Annotation.svg" width=16px> Wstaw adnotację**.
4.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
5.  Na stronie pojawi się blok tekstowy zawierający *Tekst domyślny*.
6.  Użyj [Edytora właściwości](Property_editor/pl.md), aby zmienić jego wygląd.
7.  Opcjonalnie przeciągnij adnotację w inne miejsce.

![](images/UpdateAnnotation.png ) 
*Modyfikowanie adnotacji za pomocą edytora właściwości.*



## Uwagi

Niektóre znaki zakłócają wewnętrzną reprezentację tekstu adnotacji. W szczególności są to symbole cudzysłowu `"`, mniejszy niż `<` i większy niż `>`; muszą one zostać zastąpione tagami HTML, odpowiednio `&amp;quot;`, `&amp;lt;` i `&amp;gt;`. Aby uzyskać szczegółowe informacje, zobacz informacje o [Kodowaniu znaków w HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references).



## Właściwości

Adnotacja dziedziczy wszystkie odpowiednie podstawowe właściwości widoku z wyjątkiem **Skali**. Zamiast tego należy użyć właściwości **RozmiarTekstu**.

-    **Tekst**: Tekst do wyświetlenia.

-    **Czcionka**: Nazwa czcionki do użycia. Adnotacja użyje najlepszego dopasowania zainstalowanych czcionek.

-    **KolotTekstu**: Kolor tekstu.

-    **RozmiarTekstu**: Rozmiar tekstu w mm.

-    **MaxSzerokość**: Maksymalna szerokość bloku adnotacji. -1 oznacza brak maksymalnej szerokości.

-    **OdstępWierszów**: Regulacja odstępu między wierszami (%).

-    **StylTekstu**: \"Normalny\", \"Pogrubiony\", \"Kursywa\", \"Kursywa-Pogrubiony\".



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie \\\Wstaw adnotację\\\ może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
anno = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewAnnotation','TestAnno')
anno.Text = ['Different Text']
anno.TextStyle = 'Bold'
rc = page.addView(anno)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Annotation/pl
