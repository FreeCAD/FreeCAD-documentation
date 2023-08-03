---
 GuiCommand:
   Name: Sketcher BSplineIncreaseKnotMultiplicity
   Name/pl: Szkicownik: Zmniejsz krotność węzła krzywej złożonej
   MenuLocation: Szkic , Narzędzia szkicownika krzywej złożonej , Zmniejsz krotność węzła krzywej złożonej
   Workbenches: Sketcher_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_BSplineKnotMultiplicity/pl, Sketcher_BSplineDecreaseKnotMultiplicity/pl
---

# Sketcher BSplineIncreaseKnotMultiplicity/pl



## Opis

Zmniejsza stopień *(kolejność)* krzywej złożonej *(zobacz stronę [Krzywe złożone](B-Splines/pl.md) aby uzyskać więcej informacji)*.

Krzywe złożone są w zasadzie kombinacją [Krzywych Béziera](B-Splines/pl#Krzywe_Béziera.md) *(ładnie wyjaśnione w filmie [From Bézier curves to B-spline curves](https://www.youtube.com/watch?v=bE1MrrqBAl8) oraz [Properties of B-spline curves](https://www.youtube.com/watch?v=xXJylM2S72s))*. Punkty, w których połączone są dwie części Béziera, nazywane są węzłami. Węzeł na krzywej o stopniu *d* i krotności *m* oznacza, że krzywa na lewo i na prawo od węzła ma co najmniej równą pochodną rzędu *n* *(zwaną*C*^*n*^ ciągłą)*, podczas gdy $n=d-m$.
Oto krzywa sześcienna *($d=3$)*, której węzły mają krotność 1. Mnogość jest wskazywana przez liczbę w nawiasie. Wskazanie można zmienić za pomocą przycisku na pasku narzędzi **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:24px"> [Zwiększ krotność węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity/pl.md)**:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*Krzywa złożona gdzie oba węzły mają mnogość 1.*

Krotność 3 zmieni tą krzywą tak, że nawet pochodne pierwszego rzędu nie będą równe *(*C\'\'^0^ ciągłości). Oto ta sama krzywa, w której krotność węzła lewego została zwiększona do 3:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*Krzywa złożona z góry z krotnością węzłów 3. Punkt kontrolny został przesunięty, aby pokazać, że węzeł ma ciągłość „C”<sup>0</sup>.*

Konsekwencją większej krotności jest to, że za cenę utraty ciągłości zyskujemy lokalną kontrolę. Oznacza to, że zmiana jednego punktu kontrolnego wpływa na krzywą tylko lokalnie do tego zmienionego punktu. Widać to na tym przykładzie, gdzie wzięto krzywą z pierwszego obrazka powyżej i przesunięto w górę jej drugi punkt kontrolny z prawej strony:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width:400px;"> 
*Efekt lokalności ze względu na różną krotność.*

Można zauważyć, że krzywa z krotnością węzła 1 jest całkowicie zmieniona, natomiast krzywa z krotnością 2 zachowała swoją formę po swojej lewej stronie.



## Użycie

1.  Wybierz węzeł krzywej złożonej, albo:
    -   Naciśnij przycisk **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> '''Zwiększ krotność węzłów krzywej złożonej'''**
    -   Użyj menu **Szkic → Narzędzia szkicownika krzywej złożonej → [<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> Zwiększ krotność węzłów krzywej złożonej**.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/pl
