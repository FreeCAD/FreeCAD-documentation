---
 GuiCommand:
   Name: Sketcher ConstrainCoincident
   Name/pl: Szkicownik: Wiązanie zbieżności punktów
   MenuLocation: Szkicownik , Wiązania szkicownika , Wiązanie zbieżności punktów   Workbenches: Sketcher Workbench/pl
   Shortcut: **C**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/pl, Sketcher_ConstrainPointOnObject/pl
---

# Sketcher ConstrainCoincident/pl



## Opis

Przypisuje punkt do jednego lub kilku innych punktów *(pokrywa się z nimi)*. {{Version/pl|0.21}}: Działa jako wiązanie punktów środka, jeśli wybrane są dwa lub więcej okręgów, łuków, elips lub łuków elips.



## Użycie

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa lub więcej punktów.
    -   Wybierz dwie lub więcej krawędzi okręgów, łuków, elips lub łuków elips.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> '''Wiązanie zbieżności'''** na pasku narzędzi.
    -   Użyj skrótu klawiaturowego **C**.
    -   Użyj pozycji w menu głównym **Szkic → Ograniczenia szkicownika → [<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> Wiązanie zbieżności**.



## Alternatywy dla wiązania zbieżności 

Dwa ograniczone elementy wiązania [zbieżności](Sketcher_ConstrainCoincident/pl.md) muszą być punktami początkowymi lub końcowymi wierzchołkami lub punktami środkowymi łuków, okręgów lub elips. Niektóre kombinacje, które nie są możliwe przy wiązaniu zbieżnym, można emulować przy użyciu innych wiązań:

-   Ograniczenie <img alt="" src=images/_Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [ Symetrii](Sketcher_ConstrainSymmetric/pl.md) może być użyte do umieszczenia punktu początkowego, końcowego lub środkowego na środku linii prostej.
-   Umieszczenie dwóch linii prostych od środka do punktu środkowego można uzyskać, tworząc nowy <img alt="" src=images/_Sketcher_CreatePoint.svg  style="width:24px;"> [punkt](Sketcher_CreatePoint/pl.md) i używając dwóch wiązań \[\[File: Sketcher_ConstrainSymmetric.svg\|24px\] \] [Symetrii](Sketcher_ConstrainSymmetric/pl.md), tak aby leżał w środku obu linii.
-   Wierzchołek może być związany z krawędzią za pomocą ograniczenia <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Zauważ, że dzięki temu wiązaniu punkt może leżeć w dowolnym miejscu na całej długości odcinka lub krzywej *(tj. również przed punktem początkowym lub za punktem końcowym)*.
-   Współliniowe umieszczenie dwóch prostych można uzyskać przez zastosowanie wiązania <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [styczności](Sketcher_ConstrainTangent/pl.md), lub przez połączenie wiązań <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) i <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [równoległości](Sketcher_ConstrainParallel/pl.md).
-   Dwie krawędzie mogą być identyczne poprzez użycie dwóch wiązań <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [zbieżności](Sketcher_ConstrainCoincident/pl.md), po jednym dla każdej pary końców.
-   Dwa okręgi można uczynić identycznymi za pomocą wiązania <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [zbieżności](Sketcher_ConstrainCoincident/pl.md), aby połączyć środki, i stosując wiązanie <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;">. [równości](Sketcher_ConstrainEqual/pl.md) w stosunku do ich krawędzi. W przypadku łuków, zapewni to, że oba łuki będą częścią tego samego okręgu, ale pozwoli im mieć różne punkty początkowe i końcowe.



### Ogólne zasady tworzenia skryptów 

Wiązanie może być utworzone zarówno przez [makrodefinicje](Macros/pl.md) jak i z konsoli [Python](Python.md) za pomocą następującego polecenia:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

gdzie:

-    `Sketch`jest obiektem szkicu,

-    `LineFixed`to numer linii, która nie przesunie się po zastosowaniu wiązania,

-    `PointOfLineFixed`wskazuje, który wierzchołek `LineFixed` musi spełniać warunek wiązania,

-    `LineMoving`to numer linii, która ulegnie przesunięciu przez zastosowanie wiązania,

-    `PointOfLineMoving`wskazuje, który wierzchołek `LineMoving`, musi spełniać warunek wiązania,

Jak wskazują nazwy `LineFixed` i `LineMoving`, jeśli oba związane wierzchołki mogą się poruszać w dowolnym kierunku, pierwszy z nich (wybrany jako pierwszy w Gui) pozostanie nieruchomy, a drugi będzie się poruszał. Jednak w obecności istniejących wiązań, obie krawędzie mogą się poruszać.

Strona [skrypty w środowisku szkicownika](Sketcher_scripting/pl.md) opisuje wartości, których można użyć dla `LineFixed`, `PointOfLineFixed`, `LineMoving` i `PointOfLineMoving`, a także zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/pl
