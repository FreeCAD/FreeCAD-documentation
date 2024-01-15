---
 GuiCommand:
   Name: TechDraw RichTextAnnotation
   Name/pl: Rysunek Techniczny: Wstaw adnotację w postaci tekstu sformatowanego
   MenuLocation: Rysunek Techniczny , Adnotacja , Wstaw adnotację w postaci tekstu sformatowanego
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_Annotation/pl
---

# TechDraw RichTextAnnotation/pl



## Opis

Narzędzie **Wstaw adnotację w postaci tekstu sformatowanego** dodaje sformatowany blok adnotacji do [linii odniesienia](TechDraw_LeaderLine/pl.md) lub widoku.

<img alt="" src=images/TechDraw_RichTextBlock_sample.png  style="width:220px;"> 
*Samodzielna adnotacja w postaci tekstu sformatowanego.*



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w [Widoku drzewa](Tree_view.md).
2.  Aby dołączyć adnotację RichTextAnnotation do [Linii wiodącej](TechDraw_LeaderLine/pl.md), wybierz linię w [Widoku drzewa](Tree_view.md) lub na stronie.
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_RichTextAnnotation.svg" width=16px> '''Wstaw adnotację w postaci tekstu sformatowanego'''**.
    -   Wybierz opcję **Rysunek Techniczny → Adnotacje → <img src="images/TechDraw_RichTextAnnotation.svg" width=16px> Wstaw adnotację w postaci tekstu sformatowanego** z menu.
4.  Jeśli w dokumencie znajduje się wiele stron rysunkowych, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
5.  Otworzy się panel zadań.
6.  Panel zadań umożliwia szybkie wprowadzanie tekstu.
7.  Przycisk **Uruchom edytor tekstu sformatowanego** otwiera w pełni funkcjonalny edytor:
8.  Po zakończeniu naciśnij przycisk **<img src="images/Document-save.svg" width=16px>**, aby zapisać zmiany i zamknąć edytor.
9.  Naciśnij przycisk **OK**, aby zamknąć panel zadań.



## Uwagi

-   Możesz edytować *Adnotację w postaci tekstu sformatowanego* klikając na niej dwukrotnie na stronie.



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
