---
- GuiCommand:
   Name: TechDraw RichTextAnnotation
   Name/pl: Rysunek Techniczny: Wstaw adnotację w postaci tekstu sformatowanego
   MenuLocation: Rysunek Techniczny - Adnotacja - Wstaw adnotację w postaci tekstu sformatowanego
   Workbenches: [Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version: 0.19
   SeeAlso: [Szablony](TechDraw_Templates/pl.md), [SVG](Draft_SVG/pl.md), [Dodaj linię odniesienia do widoku](TechDraw_LeaderLine/pl.md)
---

# TechDraw RichTextAnnotation/pl


</div>



## Opis

Narzędzie **Wstaw adnotację w postaci tekstu sformatowanego** dodaje sformatowany blok adnotacji do [linii odniesienia](TechDraw_LeaderLine/pl.md) lub widoku.

<img alt="" src=images/TechDraw_RichTextBlock_sample.png  style="width:220px;"> 
*Samodzielna adnotacja w postaci tekstu sformatowanego.*



## Użycie


<div class="mw-translate-fuzzy">

1.  Naciśnij przycisk **<img src="images/TechDraw_RichTextAnnotation.svg" width=16px> '''Wstaw adnotację w postaci tekstu sformatowanego'''**.
2.  Otworzy się okno dialogowe zadania. Okno dialogowe umożliwia szybkie wprowadzanie tekstu.
3.  Przycisk **Uruchom edytor tekstu sformatowanego** otworzy w pełni funkcjonalny edytor. Naciśnij ikonę Zapisz, aby zapisać zmiany.
4.  Po utworzeniu bloku można go edytować, klikając dwukrotnie obiekt AdnotacjaTekstuSformatowanego w Widoku drzewa.
5.  Aby dołączyć blok do [linię odniesienia](TechDraw_LeaderLine/pl.md), wybierz linię przed uruchomieniem narzędzia Adnotacji.


</div>



## Uwagi


<div class="mw-translate-fuzzy">

-   Możesz edytować *Adnotację w postaci tekstu sformatowanego* klikając na niej dwukrotnie w widoku Drzewa. Podwójne kliknięcie w obszarze graficznym nie jest jeszcze obsługiwane.


</div>



## Właściwości

-    **X,Y**: Położenie bloku. Względem końca linii, jeśli jest dołączony do [linii odniesienia](TechDraw_LeaderLine/pl.md), w przeciwnym razie jest to pozycja na stronie.

-    **WyświetlRamkę**: Rysuje kontur wokół bloku.

-    **MaxSzerokość**: Ogranicza poziomy rozmiar bloku. Wartość -1 oznacza nieograniczoną szerokość.

-    **AnnoText**: Tekst HTML bloku.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw adnotację w postaci tekstu sformatowanego** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md).


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
blockObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawRichAnno','DrawRichAnno')
FreeCAD.activeDocument().myPage.addView(blockObj)
blockObj.X = 5
blockObj.Y = 5
blockObj.AnnoText = myHTMLText
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RichTextAnnotation/pl
