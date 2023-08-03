---
 GuiCommand:
   Name: Sketcher BSplineIncreaseDegree
   Name/pl: Szkicownik: Zwiększ stopień krzywej złożonej
   MenuLocation: Szkic , Narzędzia szkicownika krzywej złożonej , Zwiększ stopień krzywej złożonej
   Workbenches: Sketcher_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_BSplineDegree/pl, Sketcher_BSplineDecreaseDegree/pl
---

# Sketcher BSplineIncreaseDegree/pl



## Opis

Zwiększa stopień *(kolejność)* krzywej złożonej *(zobacz stronę [Krzywe złożone](B-Splines/pl.md) aby uzyskać więcej informacji)*.

Krzywe złożone są w zasadzie kombinacją [Krzywych Béziera](B-Splines/pl#Krzywe_Béziera.md) *(ładnie wyjaśnione w filmie [From Bézier curves to B-spline curves](https://www.youtube.com/watch?v=bE1MrrqBAl8) oraz [Properties of B-spline curves](https://www.youtube.com/watch?v=xXJylM2S72s))*.

W tej sześciennej krzywej *(3 stopnia)* są 3 segmenty, co oznacza, że 3 krzywe są połączone w 2 węzłach
*(stopień jest oznaczony liczbą, wskazanie można zmienić za pomocą przycisku na pasku narzędzi **[<img src=images/Sketcher_BSplineDegree.svg style="width:24px"> [Pokaż / ukryj stopień krzywej złożonej](Sketcher_BSplineDegree/pl.md)**)*:

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*Krzywa złożona o stopniu 3 i 2 węzłach, z których każdy ma krotność 1.*

Zewnętrzne odcinki mają po 2 punkty kontrolne, wewnętrzne żadnego, aby spełnić warunek, że węzły mają krotność 1. *(zobacz stronę opisującą [krotność](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md))*.

Zwiększenie stopnia powoduje dodanie punktów kontrolnych, a kształt krzywej nie ulega zmianie:

<img alt="" src=images/Sketcher_BSplineDegree4.png  style="width:400px;"> 
*Ta sama krzywa, w której stopień został zmieniony z 3 na 4. Zauważ, że zwiększono również krotność węzłów.*

Jeśli weźmiesz ten wynik i zmniejszysz stopień, nie będziesz w stanie uzyskać stanu początkowego krzywej. W wyniku tej operacji informacje zostaną utracone. W naszym przykładzie zmniejszenie stopnia ponownie prowadzi do:

<img alt="" src=images/Sketcher_BSplineDegree3from4.png  style="width:400px;"> 
*Ta sama splajna B, w której stopień został zmieniony z powrotem z 4 na 3. Zauważ, że zwiększono krotność węzłów. W zależności od krzywej, algorytm zmniejszania stopnia może dodać wiele węzłów, aby zachować kształt krzywej, jak to się stało w tym przykładzie.*

Możesz zobaczyć, że teraz każdy segment ma 2 punkty kontrolne, a węzły pokrywają się z każdym kolejnym punktem kontrolnym. Węzły mają teraz ciągłość „C"^0^, dzięki czemu krzywa uzyska „krawędzie", gdy przesuniesz punkt kontrolny. Tak więc informacja o wyższej ciągłości zostaje utracona. *(zobacz stronę [krotność węzła](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md), aby uzyskać wyjaśnienie ciągłości)*



## Użycie

1.  Wybierz krawędź z istniejącej krzywej złożonej i naciśnij przycisk **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> '''Zwiększ stopień krzywej złożonej'''**.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseDegree/pl
