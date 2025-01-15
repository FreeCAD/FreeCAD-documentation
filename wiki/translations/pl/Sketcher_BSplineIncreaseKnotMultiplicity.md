---
 GuiCommand:
   Name: Sketcher BSplineIncreaseKnotMultiplicity
   Name/pl: Szkicownik: Zwiększ liczebność węzłów
   MenuLocation: Szkic , Narzędzia szkicownika krzywej złożonej , Zwiększ liczebność węzłów
   Workbenches: Sketcher_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_BSplineDecreaseKnotMultiplicity/pl
---

# Sketcher BSplineIncreaseKnotMultiplicity/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:24px;"> **Zwiększ liczebność węzłów** zwiększa krotność węzła [krzywej złożonej](B-Splines/pl.md).



## Użycie

1.  Wybierz węzeł krzywej złożonej.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> '''Zwiększ liczebność węzłów'''**.
    -   Wybierz z menu **Szkic → Narzędzia szkicownika krzywej złożonej → <img src="images/Sketcher_BSplineIncreaseKnotMultiplicity.svg" width=16px> Zwiększ liczebność węzłów**.



## Przykład

Krzywe złożone są w zasadzie kombinacją [krzywych Béziera](B-Splines/pl#Krzywe_Béziera.md) *(ładnie wyjaśnione w prezentacji wideo [pierwszej](https://www.youtube.com/watch?v=bE1MrrqBAl8) i [drugiej](https://www.youtube.com/watch?v=xXJylM2S72s))*. Punkty, w których dwa elementy Béziera są połączone, nazywane są węzłami. Węzeł o krotności *m* na krzywej złożonej o stopniu *d* oznacza, że krzywa po lewej i prawej stronie węzła ma co najmniej taką samą pochodną rzędu *n* *(tzw. ciągłość*C^n^*)* gdzie „n = d - m".

W tej sześciennej krzywej złożonej *(stopnia 3)* znajdują się 3 segmenty, co oznacza, że 3 krzywe są połączone w 2 węzłach. Węzły mają krotność 1.

Krotność jest wskazywana przez liczby w nawiasach okrągłych. Zobacz również stronę <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:16px;"> [Pokaż / ukryj krotność węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity/pl.md).

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*Krzywa złożona gdzie oba węzły mają krotność 1.*

Krotność 3 zmieni tą krzywą tak, że nawet pochodne pierwszego rzędu nie będą równe *(*C^0^\'\' ciągłości). Oto ta sama krzywa złożona, w której krotność węzła po lewej stronie została zwiększona do 3:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*Krzywa złożona z góry z krotnością węzłów 3. Punkt kontrolny został przesunięty, aby pokazać, że węzeł ma ciągłość ''C<sup>0</sup>''.*

Konsekwencją wyższej krotności jest to, że za cenę utraty ciągłości zyskuje się lokalną kontrolę. Oznacza to, że zmiana jednego punktu kontrolnego wpłynie na krzywą złożoną tylko lokalnie.

Można to zobaczyć na tym przykładzie, gdzie wykonano krzywą złożoną z krotnością węzłów 1 z pierwszego zdjęcia powyżej, a drugi punkt kontrolny od prawej został przesunięty w górę. W rezultacie cały kształt krzywej złożonej uległ zmianie:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality1.png  style="width:400px;">

Po zwiększeniu krotności węzłów do 2, przesunięcie drugiego punktu kontrolnego od prawej strony powoduje znaczące zmiany tylko po prawej stronie kształtu:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality2.png  style="width:400px;">



## Uwagi

-   Mnogość węzłów można również zwiększyć za pomocą narzędzia [Wstaw węzeł krzywej złożonej](Sketcher_BSplineInsertKnot/pl.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/pl
