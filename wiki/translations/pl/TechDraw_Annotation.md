---
 GuiCommand:
   Name: TechDraw Annotation
   Name/pl: Rysunek Techniczny: Wstaw adnotację
   MenuLocation: TechDraw , Adnotacje , Wstaw adnotację
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: Draft_Text/pl, Draft_ShapeString/pl
---

# TechDraw Annotation/pl


</div>



## Opis

Narzędzie *Wstaw adnotację* dodaje blok tekstu do strony rysunku.

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Adnotacja na stronie rysunku.*



## Użycie


<div class="mw-translate-fuzzy">

1.  Jeśli w dokumencie znajduje się wiele stron rysunku, należy wybrać żądaną stronę w oknie drzewa.
2.  Naciśnij przycisk **<img src="images/TechDraw_Annotation.svg" width=24px> '''Wstaw adnotację'''**.
3.  Na stronie pojawi się blok tekstowy zawierający *Tekst domyślny*. Użyj edytora właściwości, aby dostosować tekst. Przeciągnij adnotację do wymaganej pozycji.
4.  Może być konieczne naciśnięcie przycisku **<img src="images/Std_Refresh.svg" width=16px> [Odśwież](Std_Refresh/pl.md)** i/lub **<img src="images/TechDraw_RedrawPage.svg" width=16px> [Przerysuj stronę](TechDraw_RedrawPage.md)**, aby zobaczyć zmianę tekstu.


</div>

![](images/UpdateAnnotation.png )


<div class="mw-translate-fuzzy">



*Modyfikowanie adnotacji za pomocą edytora właściwości.*


</div>



## Uwagi


<div class="mw-translate-fuzzy">


**Uwaga:**

Niektóre znaki zakłócają wewnętrzną reprezentację tekstu adnotacji. W szczególności są to symbole cudzysłowu `"`, mniejszy niż `<` i większy niż `>`; muszą one zostać zastąpione tagami HTML, odpowiednio `&amp;quot;`, `&amp;lt;` i `&amp;gt;`. Aby uzyskać szczegółowe informacje, zobacz informacje o [Kodowaniu znaków w HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references).


</div>



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
