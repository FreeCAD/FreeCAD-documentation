---
 GuiCommand:
   Name: Sketcher BSplineIncreaseDegree
   Name/pl: Szkicownik: Zwiększ stopień krzywej złożonej
   MenuLocation: Szkic , Narzędzia szkicownika krzywej złożonej , Zwiększ stopień krzywej złożonej
   Workbenches: Sketcher_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_BSplineDecreaseDegree/pl
---

# Sketcher BSplineIncreaseDegree/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:24px;"> **Zwiększ stopień krzywej złożonej** zwiększa stopień *(kolejność)* [krzywej złożonej](B-Splines/pl.md) .



## Użycie

1.  Wybierz jedną lub więcej krzywych złożonych.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> '''Zwiększ stopień krzywej złożonej'''**.

    -   Wybierz z menu **Szkic → Narzędzia szkicownika krzywej złożonej → <img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Zwiększ stopień krzywej złożonej**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Zwiększ stopień krzywej złożonej** z menu podręcznego.



## Przykład

Krzywe złozone są w zasadzie kombinacją [Krzywych Béziera](B-Splines/pl#Krzywe_Béziera.md) *(ładnie wyjaśnione w filmie [From Bézier curves to B-spline curves](https://www.youtube.com/watch?v=bE1MrrqBAl8) oraz [Properties of B-spline curves](https://www.youtube.com/watch?v=xXJylM2S72s))*.

W tej sześciennej krzywej *(3 stopnia)* są 3 segmenty, co oznacza, że 3 krzywe są połączone w 2 węzłach.

Stopień jest wskazywany przez liczbę w środku. Zobacz opis na stronie <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:16px;"> [Pokaż / ukryj stopień krzywej złożonej.](Sketcher_BSplineDegree/pl.md).

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*Krzywa złożona o stopniu 3 i 2 węzłach, z których każdy ma krotność 1.*

Zewnętrzne odcinki mają po 2 punkty kontrolne, segment wewnętrzny nie ma żadnego, aby zapewnić że węzły mają krotność 1. Zobacz stronę opisującą [krotność](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md).

Zwiększenie stopnia do 4 spowoduje dodanie punktów kontrolnych bez zmiany kształtu krzywej złozonej:

<img alt="" src=images/Sketcher_BSplineDegree4.png  style="width:400px;"> 
*Ta sama krzywa, w której stopień został zmieniony z 3 na 4. Zauważ, że zwiększono również krotność węzłów.*

Z tego wyniku nie można powrócić do stanu początkowego krzywej złożonej poprzez zmniejszenie stopnia. Niektóre informacje są tracone, gdy stopień krzywej złożonej jest zmieniany. Zmniejszenie stopnia z powrotem do 3 prowadzi do sytuacji:

<img alt="" src=images/Sketcher_BSplineDegree3from4.png  style="width:400px;"> 
*Ta sama krzywa, w której stopień został zmieniony z powrotem z 4 na 3. Zauważ, że zwiększono krotność węzłów. W zależności od krzywej, algorytm zmniejszania stopnia może dodać wiele węzłów, aby zachować kształt krzywej, jak to się stało w tym przykładzie.*

Możesz zobaczyć, że teraz każdy segment ma 2 punkty kontrolne, a węzły pokrywają się z każdym kolejnym punktem kontrolnym. Węzły mają teraz ciągłość „C"^0^, dzięki czemu krzywa uzyska \"narożniki\", gdy przesuniesz punkt kontrolny. Tak więc informacja o wyższej ciągłości zostaje utracona. Zobacz stronę [krotność węzła](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md), aby uzyskać wyjaśnienie ciągłości.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseDegree/pl
