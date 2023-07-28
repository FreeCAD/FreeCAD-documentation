---
- GuiCommand:/pl
   Name:Sketcher ConstrainPointOnObject
   Name/pl:Szkicownik: Zwiąż punkt na obiekcie
   MenuLocation:Szkic → Wiązania szkicownika → Zwiąż punkt na obiekcie
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**O**
   SeeAlso:[Wiązanie spójności punktów](Sketcher_ConstrainCoincident/pl.md)
---

# Sketcher ConstrainPointOnObject/pl



## Opis

Przyłącza punkt do innego obiektu, takiego jak linia, łuk lub oś szkicu.



## Użycie

1.  Wybierz punkt i krawędzi w dowolnej kolejności.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> '''Zwiąż punkt na obiekcie'''** na pasku narzędzi.
    -   Użyj klawisza **O**.
    -   Użyj pozycji w menu głównym **Szkic → Wiązania szkicownika → [<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> Zwiąż punkt na obiekcie**.



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
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/pl
