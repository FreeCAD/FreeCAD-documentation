---
- GuiCommand:
   Name: Sketcher BSplineDecreaseDegree
   MenuLocation: Szkic - Narzędzia szkicownika krzywej złożonej - Szkic - Narzędzia szkicownika krzywej złożonej
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md)
   Version: 0.19
   SeeAlso: [Pokaż / ukryj stopień krzywej złożonej](Sketcher_BSplineDegree/pl.md), [Zwiększ stopień krzywej złożonej](Sketcher_BSplineIncreaseDegree/pl.md)
---

# Sketcher BSplineDecreaseDegree/pl



## Opis

Zmniejsza stopień *(kolejność)* krzywej złożonej *(zobacz stronę [Krzywe złożone](B-Splines/pl.md) aby uzyskać więcej informacji)*.

Krzywe złożone są w zasadzie kombinacją [Krzywych Béziera](B-Splines/pl#Krzywe_Béziera.md) *(ładnie wyjaśnione w filmie [From Bézier curves to B-spline curves](https://www.youtube.com/watch?v=bE1MrrqBAl8) oraz [Properties of B-spline curves](https://www.youtube.com/watch?v=xXJylM2S72s))*.

W tej sześciennej krzywej *(3 stopnia)* są 3 segmenty, co oznacza, że 3 krzywe są połączone w 2 węzłach
*(stopień jest oznaczony liczbą, wskazanie można zmienić za pomocą przycisku na pasku narzędzi **[<img src=images/Sketcher_BSplineDegree.svg style="width:24px"> [Pokaż / ukryj stopień krzywej złożonej](Sketcher_BSplineDegree/pl.md)**)*:

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*Krzywa złożona o stopniu 3 i 2 węzłach, z których każdy ma krotność 1.*

Zewnętrzne odcinki mają po 2 punkty kontrolne, wewnętrzne żadnego, aby spełnić warunek, że węzły mają krotność 1. *(zobacz stronę opisującą [krotność](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md))*.

Zmniejszenie stopnia nie spowoduje usunięcia punktów kontrolnych, lecz będzie próbowało zachować kształt krzywej. Dlatego segmenty będą dodawane. W naszym przykładzie widać wiele nowych segmentów krzywej z każdym jednym punktem kontrolnym, a kształt krzywej został tylko nieznacznie zmieniony:

<img alt="" src=images/Sketcher_BSplineDegree2.png  style="width:400px;"> 
*Ta sama krzywa złożona, w której stopień został zmieniony z 3 na 2. Należy zauważyć, że również zwiększono liczbę węzłów, aby zachować kształt krzywej. W efekcie węzły mają teraz ciągłość „C”<sup>0</sup>, dzięki czemu krzywa uzyska „krawędzie”, gdy przesuniesz punkt kontrolny. ''(zobacz stronę [krotność węzła](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md), aby uzyskać wyjaśnienie ciągłości)''*

Jeśli weźmiesz ten wynik i zwiększysz stopień, nie możesz uzyskać początkowego stanu krzywej, ponieważ informacje zostały utracone przez wcześniejsze zmniejszenie stopnia. Dla naszego przykładu zwiększanie stopnia znów prowadzi do:

<img alt="" src=images/Sketcher_BSplineDegree3again.png  style="width:400px;"> 
*Ta sama krzywa, w której stopień został zmieniony z powrotem z 2 na 3. Zauważ, że krotność węzła również wzrosła, ponieważ informacja o możliwej wyższej ciągłości została utracona.*



## Użycie

1.  Wybierz krawędź z istniejącej krzywej złożonej i naciśnij przycisk **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> '''Zmniejsz stopień krzywej złożonej'''**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseDegree/pl
