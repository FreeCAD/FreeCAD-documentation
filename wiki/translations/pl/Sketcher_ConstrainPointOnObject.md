---
 GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   Name/pl: Szkicownik: Zwiąż punkt na obiekcie
   MenuLocation: Szkic , Wiązania szkicownika , Zwiąż punkt na obiekcie
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **O**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/pl, Sketcher_ConstrainCoincident/pl
---

# Sketcher ConstrainPointOnObject/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> **Zwiąż punkt na obiekcie** przyłącza punkt do innego obiektu, takiego jak linia, łuk lub oś szkicu. Linie są traktowane jako nieskończone, a otwarte krzywe są również praktycznie rozszerzone.


{{Version/pl|1.0}}

: Narzędzie to jest zastępowane przez [Wiązanie zbieżności punktów (ujednolicone)](Sketcher_ConstrainCoincidentUnified/pl.md), jeśli opcja **Połącz wiązania zbieżności i punkt na obiekcie** jest zaznaczona w [ustawieniach](Sketcher_Preferences/pl#Ogólne.md) szkicownika.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> '''Zwiąż punkt na obiekcie'''**.
    -   Wybierz z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> Zwiąż punkt na obiekcie**.
    -   Użyj skrótu klawiaturowego: **O**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz pojedynczy punkt i pojedynczą krawędź *(w dowolnej kolejności)*.
5.  Zostanie dodane wiązanie.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz pojedynczy punkt i pojedynczą krawędź *(w dowolnej kolejności)*.
    -   Wybierz kilka punktów i jedną krawędź *(analogicznie)*.
    -   Wybierz pojedynczy punkt i kilka krawędzi *(analogicznie)*.
2.  Wywołaj narzędzie w sposób opisany powyżej.
3.  W zależności od wyboru dodawane jest jedno lub więcej ograniczeń.



## Tworzenie skryptów 

Wiązanie może być utworzone zarówno przez [makrodefinicje](Macros/pl.md) jak i z konsoli [Python](Python/pl.md) za pomocą następującego polecenia:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`obiekt szkicu.

-    `LineMoving`jest numerem oznaczającym linię, która zawiera punkt, który ma być przeniesiony na `LineFixed` *(linię, która jest ustalona)*.

-    `PointOfLineMoving`jest numerem wierzchołka linii `LineMoving`, który ma zostać przeniesiony na `LineFixed`.

-    `LinedFixed`jest numerem linii, która ma być dołączona do punktu `PointOfLineMoving`.

Na stronie [Skrypty Szkicownika](Sketcher_scripting/pl.md) wyjaśniono, jak identyfikować numery oznaczające linie i punkty.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/pl
