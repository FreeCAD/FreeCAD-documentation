---
- GuiCommand:
   Name: Sketcher BSplineDecreaseKnotMultiplicity
   Name/pl: Szkicownik: Zwiększ krotność węzła krzywej złożonej
   MenuLocation: Szkic - Narzędzia szkicownika krzywej złożonej - Zwiększ krotność węzła krzywej złożonej
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md)
   Version: 0.17
   SeeAlso: [Pokaż / ukryj wyświetlanie węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity/pl.md), [Zwiększ krotność węzła krzywej złożonej](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md)
---

# Sketcher BSplineDecreaseKnotMultiplicity/pl



## Opis

Zwiększa stopień *(kolejność)* krzywej złożonej *(zobacz stronę [Krzywe złożone](B-Splines/pl.md) aby uzyskać więcej informacji)*.

Krzywe złożone są w zasadzie kombinacją [Krzywych Béziera](B-Splines/pl#Krzywe_Béziera.md) *(ładnie wyjaśnione w filmie [From Bézier curves to B-spline curves](https://www.youtube.com/watch?v=bE1MrrqBAl8) oraz [Properties of B-spline curves](https://www.youtube.com/watch?v=xXJylM2S72s))*. Punkty, w których dwie krzywe Béziera są połączone, tworząc splajn, nazywamy węzłami. Węzeł na krzywej stopnia *d* o krotności *m* oznacza, że krzywa na lewo i prawo od węzła ma co najmniej równą pochodną rzędu *n* *(zwaną*C*^*n*^ ciągłą)*, podczas gdy $n=d-m$.
Oto krzywa sześcienna *($d=3$)*, której węzły mają krotność 1. Mnogość jest wskazywana przez liczbę w nawiasie. Wskazanie można zmienić za pomocą przycisku na pasku narzędzi **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:24px"> [Pokaż / ukryj wyświetlanie węzłów krzywej złożonej](Sketcher_BSplineKnotMultiplicity/pl.md)**:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*Krzywa złożona gdzie oba węzły mają mnogość 1.*

Krotność 3 zmieni tą krzywą tak, że nawet pochodne pierwszego rzędu nie będą równe *(*C\'\'^0^ ciągłości). Oto ta sama krzywa, w której krotność węzła lewego została zwiększona do 3:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*Krzywa złożona z góry z krotnością węzłów 3. Punkt kontrolny został przesunięty, aby pokazać, że węzeł ma ciągłość „C”<sup>0</sup>.*

Konsekwencją większej krotności jest to, że za cenę utraty ciągłości zyskujemy lokalną kontrolę. Oznacza to, że zmiana jednego punktu kontrolnego wpływa na krzywą tylko lokalnie do tego zmienionego punktu. Widać to na tym przykładzie, gdzie wzięto krzywą z pierwszego obrazka powyżej i przesunięto w górę jej drugi punkt kontrolny z prawej strony:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width:400px;"> 
*Efekt lokalności ze względu na różną krotność.*

Można zauważyć, że krzywa z krotnością węzła 1 jest całkowicie zmieniona, natomiast krzywa z krotnością 2 zachowała swoją formę po swojej lewej stronie.

**Uwaga:** Jeśli zmniejszysz krotność, węzeł zniknie, ponieważ matematycznie pojawia się wtedy zero razy w wektorze węzłów, co oznacza, że nie ma już funkcji bazowej. Zrozumienie tego wymaga trochę matematyki, ale będzie również jasne, gdy spojrzysz na krotność: Na przykład stopień = 3, a następnie krotność = 0 oznacza, że w miejscu węzła dwa kawałki Béziera są połączone z „C" ^3^ ciągłości. Zatem trzecia pochodna powinna być równa po obu stronach węzła. Jednak w przypadku sześciennej krzywej Béziera *(czyli wielomianu stopnia 3)* oznacza to, że obie strony muszą należeć do tej samej krzywej. Tak więc w rzeczywistości nie ma już węzła łączącego 2 różne krzywe Béziera, poprzedni węzeł jest wtedy po prostu punktem na jednej krzywej Béziera.



## Użycie

1.  Wybierz węzeł krzywej złożonej, albo:
    -   Naciśnij przycisk **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> '''Zmniejsz krotność węzła krzywej złożonej'''**.
    -   Użyj menu **Szkic → Narzędzia szkicownika krzywej złożonej → [<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> Zmniejsz krotność węzła krzywej złożonej**.

**Uwaga:** Zmniejszenie krotności z 1 do 0 spowoduje usunięcie węzła, ponieważ wynikiem byłaby krzywa z \"krawędzią\" w miejscu *(*C*^0^ ciągłości)* węzła, a to nie jest obsługiwane. *(Aby stworzyć krzywe z \"krawędzią\", możesz stworzyć dwa odcinki krzywej i połączyć je)*.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/pl
