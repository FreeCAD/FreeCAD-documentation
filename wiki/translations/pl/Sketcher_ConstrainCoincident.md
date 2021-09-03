---
- GuiCommand:/pl
   Name:Sketcher ConstrainCoincident
   Name/pl:Wiązanie zbieżności punktów
   MenuLocation:Sketch → Wiązania szkicownika → Wiązanie zbieżności
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**C**
   SeeAlso:[Wiązanie blokady odległości](Sketcher_ConstrainLock/pl.md), [wiązanie punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md)
---

## Opis

Stwórz wiązanie zbieżności z wybraną pozycją.

Narzędzie to przyjmuje dwa punkty jako swój argument i służy do nadania tym dwóm punktom zbieżności. *(To znaczy, że stają się one tylko jednym punktem)*.

W praktyce narzędzie to jest użyteczne w przypadku przerwania profilu, na przykład gdy dwie linie kończą się blisko siebie i muszą zostać połączone - wiązanie zbieżności w punkcie końcowym doprowadzi do zlikwidowania tej przerwy.

## Użycie

Jak stwierdzono powyżej, narzędzie to przyjmuje dwa argumenty - oba są punktami.

1.  Po pierwsze, konieczne jest zaznaczenie dwóch różnych punktów. *(**Uwaga:** to nie zadziała, jeżeli na przykład spróbujemy wybrać punkt początkowy i punkt końcowy tej samej linii prostej. Wybranie punktów początkowych i końcowych łuku spowoduje utworzenie zamkniętego okręgu lub elipsy, ale ograniczy położenie szwu do tego punktu)*.
2.  Podświetlenie elementu rysunku uzyskuje się poprzez umieszczenie na nim kursora myszki i kliknięcie lewym przyciskiem myszy.
3.  Możliwe jest również zaznaczenie wszystkich elementów wewnątrz prostokąta poprzez kliknięcie i przeciągnięcie. Przy przeciąganiu od lewej do prawej (z dowolnym ruchem pionowym) zostaną podświetlone tylko kształty, które w całości mieszczą się w prostokącie; w drugim kierunku zostaną podświetlone wszystkie kształty, które przecinają się z prostokątem zaznaczenia. Można to wykorzystać do zaznaczenia tylko wierzchołków bez zaznaczania krawędzi, przeciągając mały prostokąt wokół niektórych wierzchołków od lewej do prawej, o ile nie ma krawędzi, które w całości mieszczą się w prostokącie.
4.  Podświetlony element zmieni swój kolor na zielony. *(Kolor ten można dostosować do własnych potrzeb w **Edycja → Preferencje → Wyświetlanie → Kolory → Zaznaczanie**)*.
5.  Kolejne punkty mogą być podświetlone poprzez powtórzenie powyższych procedur. **Uwaga"** Nie trzeba przytrzymywać żadnego specjalnego klawisza, jak **Ctrl** aby uzyskać wielokrotny wybór pozycji na rysunku.
6.  Po podświetleniu dwóch punktów, można wywołać komendę za pomocą kilku metod:
    -   Wciskając przycisk wiązania na pasku przyborów **<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> [Wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md)**.
    -   Użycie skrótu klawiszy **C** przy pomocy klawiatury.
    -   Użycie polecenia w górnym menu **Szkicownik → Wiązania szkicownika → Wiązanie zbieżności**.


**Wynik:**

polecenie to spowoduje, że dwa punkty staną się *nałożone na siebie* i zostaną zastąpione jednym punktem.


**Uwaga:**

Aby uczynić dwa punkty zbieżnymi, FreeCAD musi z konieczności przenieść jeden *(lub oba)* z oryginalnych pozycji.

## Alternatywy dla wiązania zbieżności 

Dwa ograniczone elementy wiązania [zbieżności](Sketcher_ConstrainCoincident/pl.md) muszą być punktami początkowymi lub końcowymi wierzchołkami lub punktami środkowymi łuków, okręgów lub elips. Niektóre kombinacje, które nie są możliwe przy wiązaniu zbieżnym, można emulować przy użyciu innych wiązań:

-   Ograniczenie <img alt="" src=images/_Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [ Symetrii](Sketcher_ConstrainSymmetric/pl.md) może być użyte do umieszczenia punktu początkowego, końcowego lub środkowego na środku linii prostej.
-   Umieszczenie dwóch linii prostych od środka do punktu środkowego można uzyskać, tworząc nowy <img alt="" src=images/_Sketcher_CreatePoint.svg  style="width:24px;"> [punkt](Sketcher_CreatePoint/pl.md) i używając dwóch wiązań \[\[File: Sketcher\_ConstrainSymmetric.svg\|24px\] \] [Symetrii](Sketcher_ConstrainSymmetric/pl.md), tak aby leżał w środku obu linii.
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

Strona [skrypty w środowiszku szkicownika](Sketcher_scripting.md) opisuje wartości, których można użyć dla `LineFixed`, `PointOfLineFixed`, `LineMoving` i `PointOfLineMoving`, a także zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher Tools navi

}}  
