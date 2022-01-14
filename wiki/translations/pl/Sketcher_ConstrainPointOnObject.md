---
- GuiCommand:/pl
   Name:Sketcher ConstrainPointOnObject
   Name/pl:Wiązanie punktu na obiekcie
   MenuLocation:Szkic → Wiązania szkicownika → Wiązanie punktu na obiekcie
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**Shift** + **O**
   SeeAlso:[Wiązanie spójności punktów](Sketcher_ConstrainCoincident/pl.md)
---

# Sketcher ConstrainPointOnObject/pl

## Opis

Przyłącza punkt do innego obiektu, takiego jak linia, łuk lub oś szkicu.

## Użycie

1.  Wybierz punkt, który chcesz umieścić na linii / łuku / itd. *(*Rezultat:\'\' Po wybraniu punkt stanie się zielony)\'\'.
2.  Wybierz linię, którą chcesz dołączyć do punktu, który właśnie wybrałeś *(*Wynik:\'\' Po wybraniu linia stanie się zielona)\'\'.
3.  Wywołaj narzędzie **Ustaw punkt na obiekcie** używając kilku metod:
    -   Naciśnij przycisk **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Ustaw punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md)** na pasku narzędzi.
    -   Użyj kombinacji klawiszy **Shift** + **O**.
    -   Użyj pozycji **Szkic → Wiązania szkicownika → Zwiąż punkt na obiekcie** w menu głównym.

**Uwaga:** Kolejność, w jakiej wybierasz linię i punkt, nie ma znaczenia. Punkt zawsze będzie przesuwał się do linii. Innymi słowy, linia pozostaje nieruchoma.

## Tworzenie skryptów 

Wiązanie może być utworzone zarówno przez [makrodefinicje](Macros/pl.md) jak i z konsoli [Python](Python/pl.md) za pomocą następującego polecenia:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`obiekt szkicu.

-    `LineMoving`jest numerem oznaczającym linię, która zawiera punkt, który ma być przeniesiony na `LineFixed` *(linię, która jest ustalona)*.

-    `PointOfLineMoving`jest numerem wierzchołka linii `LineMoving`, który ma zostać przeniesiony na `LineFixed`.

-    `LinedFixed`jest numerem linii, która ma być dołączona do punktu `PointOfLineMoving`.

Na stronie [Skrypty Szkicownika](Sketcher_scripting/pl.md) wyjaśniono, jak identyfikować numery oznaczające linie i punkty.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/pl
