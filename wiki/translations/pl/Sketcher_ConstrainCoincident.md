---
 GuiCommand:
   Name: Sketcher ConstrainCoincident
   Name/pl: Szkicownik: Wiązanie zbieżności punktów
   MenuLocation: Szkicownik , Wiązania szkicownika , Wiązanie zbieżności punktów
   Workbenches: Sketcher Workbench/pl
   Shortcut: **C**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/pl, Sketcher_ConstrainPointOnObject/pl
---

# Sketcher ConstrainCoincident/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> **Wiązanie zbieżności** tworzy wiązanie zbieżne między punktami lub *(<small>(v0.21)</small> )* koncentryczne wiązanie pomiędzy okręgami, łukami i / lub elipsami *(poprzez zapewnienie zbieżności ich środków)*.


{{Version/pl|1.0}}

: Polecenie to jest zastępowane przez polecenie [Wiązanie zbieżności punktów (ujednolicone)](Sketcher_ConstrainCoincidentUnified/pl.md), jeśli opcja **Połącz wiązania zbieżności i punkt na obiekcie** jest zaznaczona w [ustawieniach](Sketcher_Preferences/pl#Ogólne.md) szkicownika.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainCoincident.svg" width=16px> '''Wiązanie zbieżności'''** na pasku narzędzi.
    -   Wybierz opcja z menu **Szkic → Ograniczenia szkicownika → <img src="images/Sketcher_ConstrainCoincident.svg" width=16px> Wiązanie zbieżności**.
    -   Użyj skrótu klawiaturowego **C**.
3.  Kursor zmieni się na krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty.
    -   Wybierz dwie krawędzie okręgów, łuków, elips lub łuków elips.
5.  Wiązanie zostanie dodane.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa lub więcej punktów.
    -   Wybierz dwie lub więcej krawędzi okręgów, łuków, elips lub łuków elips.
2.  Wywołaj narzędzie, jak wyjaśniono powyżej.
3.  W zależności od wyboru dodawane jest jedno lub więcej wiązań.



## Uwagi

-    {{Version/pl|1.0}}: Punkty z wiązaniami zbieżnymi są oznaczone [kolorem](Sketcher_Preferences/pl#Wyświetlanie.md) **symboli wiązań**.



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



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/pl
