---
- GuiCommand:
   Name: TechDraw Balloon
   Name/pl: Rysunek Techniczny: Wstaw adnotację w formie dymka
   MenuLocation: Rysunek Techniczny - Adnotacje - Wstaw adnotację w formie dymka
   Workbenches: [Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version: 0.19
   SeeAlso: [Wstaw adnotację](TechDraw_Annotation/pl.md)
---

# TechDraw Balloon/pl



## Opis

Narzędzie **Wstaw adnotację w formie dymka** może dodawać do rysunku dymki z linią odniesienia.

<img alt="" src=images/Techdraw_balloon.png  style="width:600px;">



## Użycie

1.  Wybierz jedną z poniższych opcji:
    -   Widok *(na stronie lub w oknie [Widoku drzewa](Tree_view/pl.md))*.
    -   Wierzchołek w widoku. {{Version/pl|0.20}}
    -   Krawędź w widoku. {{Version/pl|0.20}}
    -   Zamknięty region w widoku. {{Version/pl|0.20}}
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnięcie przycisku **<img src="images/TechDraw_Balloon.svg" width=16px> '''Wstaw adnotację w formie dymka'''**.
    -   Wybierz **Rysunek Techniczny → Adnotacje → <img src="images/TechDraw_Balloon.svg" width=16px> Wstaw adnotację w formie dymka** z menu.
3.  Jeśli wybrano widok lub obszar:
    1.  Kursor zmienia się w ikonę dymka.
    2.  Kliknij punkt na stronie, który będzie początkiem dymka.

Aby przesunąć bańkę dymka, naciśnij i przytrzymaj lewy przycisk myszy na jego środku i przeciągnij kursor myszki.

Aby zmienić właściwości dymka, kliknij go dwukrotnie na stronie lub w oknie [widoku Drzewa](Tree_view/pl.md). Spowoduje to otwarcie panelu zadań Dymek.

**Uwaga:** Położenie dymka odnosi się do jego widoku źródłowego i wykorzystuje ten sam współczynnik skali.



## Używanie separatorów 

W przypadku korzystania z kształtu prostokąta, separatory można dodawać za pomocą znaku \"\|\" w tekście. Na przykład \"AAA\|TEST\|111\" daje:

<img alt="" src=images/balloon_separator.png  style="width:300px;">



## Właściwości



### Dane


<div class="mw-translate-fuzzy">

-    **Tekst**: Tekst do wyświetlenia.

-    **Widok źródłowy**: Widok źródłowy balonu.

-    **Odniesienie położenia X**: Pozycja x początku dymka względem widoku.

-    **Odniesienie położenia Y**: Pozycja y początku dymka względem widoku.

-    **Typ zakończenia**: Symbol końca linii balonu. Opcje: <img alt="" src=images/Arrownone.svg  style="width:20px;"> Brak, <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Wypełniona strzałka, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Otwarta strzałka, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Grot, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Kropka, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Otwarte koło, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Widelec, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Wypełniony trójkąt.

-    **Skala typu zakończenia**: Współczynnik skali dla **Typu zakończenia**.

-    **Kształt dymka**: Kształt bańki dymka. Opcje: <img alt="" src=images/Circular.svg  style="width:20px;"> Okrągły, Żaden, <img alt="" src=images/Triangle.svg  style="width:20px;"> Trójkąt, <img alt="" src=images/Inspection.svg  style="width:20px;"> Inspekcja, <img alt="" src=images/Hexagon.svg  style="width:20px;"> Sześciokąt, <img alt="" src=images/TechDraw_Square.svg  style="width:20px;"> Kwadrat, <img alt="" src=images/Rectangle.svg  style="width:20px;"> Prostokąt

-    **Skala kształtu**: Współczynnik skali dla **Kształtu**.

-    **Zawijanie tekstu**: Długość zawijania tekstu; -1 oznacza, że tekst nigdy nie zostanie zawinięty, a wynikiem będzie w każdym przypadku pojedyncza linia.

-    **Długość załamania**: Odległość od **kształtu** do załamania linii prowadzącej.

-    **X**: Poziome położenie dymku względem widoku.

-    **Y**: Pionowe położenie bańki balonu względem widoku.


</div>



### Widok

-    **Kolor**: Kolor tekstu w dymku.

-    **Czcionka**: Nazwa czcionki używanej w dymku.

-    **Rozmiar czcionki**: Rozmiar tekstu w mm.

-    **Linia widoczna**: Czy linia dymka jest widoczna.

-    **Szerokość linii**: Szerokość linii dymka.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw adnotację w formie dymka** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
bal1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewBalloon','Balloon')
rc = page.addView(bal1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Balloon/pl
