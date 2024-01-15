---
 GuiCommand:
   Name: Sketcher BSplinePoleWeight
   Name/pl: Szkicownik: Pokaż / ukryj wagę punktu kontrolnego krzywej złożonej
   MenuLocation: Szkic , Wygląd w szkicowniku , Pokaż / ukryj wagę punktu kontrolnego krzywej złożonej
   Workbenches: Sketcher_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_CompCreateBSpline/pl
---

# Sketcher BSplinePoleWeight/pl



## Opis

Pokazuje lub ukrywa wyświetlanie **wag** dla punktów kontrolnych krzywej złożonej *(zobacz [poniższy akapit](#Objaśnienie_wagi.md) dla wyjaśnienia wag)*.

<img alt="" src=images/sketcher_BSplineWeightShow.png  style="width:468px;"> 
*Krzywa złożona z wagami punktów kontrolnych podanymi w nawiasach.*



## Użycie

1.  Wybierz krzywą złożoną i użyj przycisku na pasku narzędzi **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> '''Pokaż / ukryj wagę punktu kontrolnego krzywej złożonej'''**.



## Objaśnienie wagi 

Krzywe złozone są w zasadzie kombinacją [Krzywych Béziera](B-Splines/pl#Krzywe_Béziera.md) *(ładnie wyjaśnione w filmie [From Bézier curves to B-spline curves](https://www.youtube.com/watch?v=bE1MrrqBAl8) oraz [Properties of B-spline curves](https://www.youtube.com/watch?v=xXJylM2S72s))*.

Krzywą Béziera oblicza się według poniższego wzoru:

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{polynomial term}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{polynomial term}}\; \underbrace{P_{i}}_{\text{point coordinate}}$

\"n\" jest niniejszym stopniem krzywej. Zatem krzywa Béziera stopnia *n* jest wielokątem rzędu *n*. Współczynniki $P_{i}$ są więc współrzędnymi punktów kontrolnych krzywych Béziera. Wizualizację można znaleźć na stronie [kontrolowanie krzywizn Béziera](https://pomax.github.io/bezierinfo/#control).

Termin waga w FreeCAD jest nieco mylący, ponieważ w literaturze współczynniki $P_{i}$ również często nazywane są wagami. Wagi w FreeCAD są czymś innym. Ideą tych wag jest zmodyfikowanie krzywej tak, aby różne punkty kontrolne były \"ważone\". Chodzi o to, że punkt o wadze 2 powinien mieć dwa razy większy wpływ niż punkt o wadze 1. Osiąga się to poprzez użycie tej innej formuły do obliczenia krzywej:

$\quad
\mathrm{Rational\ Bezier}(n,t)=\cfrac{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}P_{i}}{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}\;\;\;\,}$

dzięki której $w_{i}$ jest wagą dla punktu $P_{i}$.

Jest to nowa klasa krzywych Béziera, ponieważ pomimo tego, że punkty są rzeczywiście ważone w pożądany sposób, krzywa nie jest już wielomianem, ale wielomianem ułamkowym. Dlatego krzywe te nazywane są racjonalnymi krzywymi Béziera, a krzywe złożonymi nazywane są wtedy racjonalnymi krzywymi złożonymi.

W konsekwencji zyskujemy większą elastyczność w definiowaniu kształtu krzywej. Jeśli wszystkie wagi są równe, kształt krzywej nie zmienia się. Ważne są więc wagi względem siebie, a nie sama wartość. Na przykład ta krzywa ma dokładnie taki sam kształt jak ten na pierwszym obrazku:

<img alt="" src=images/sketcher_BSplineWeightDouble.png  style="width:468px;"> 
*Ta sama krzywa złożona co na pierwszym obrazie, ale z różnymi wartościami wag bezwzględnych.*

Waga równa zero byłaby osobliwością w równaniu do obliczania racjonalnych krzywych Béziera, dlatego FreeCAD zapewnia, że nie może ona stać się zerowa. Niemniej jednak małe wartości mają taki sam efekt, jak gdyby punkt kontrolny prawie nie istniał:

<img alt="" src=images/sketcher_BSplineWeightZero.png  style="width:468px;"> 
*Ta sama krzywa złożona z prawie zerowym punktem kontroli wagi.*



## Zmiana wag 

Sposób zmiany wag jest opisany na stronie przedstawiającej [Krzywe złożone](B-Splines/pl#Zmiana_wagi.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplinePoleWeight/pl
