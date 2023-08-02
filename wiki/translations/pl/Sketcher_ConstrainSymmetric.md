---
- GuiCommand:
   Name: Sketcher ConstrainSymmetric
   Name/pl: Szkicownik: Wiązanie symetrii
   MenuLocation: Szkic -> Wiązania szkicownika -> Wiązanie symetrii
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **S**
   SeeAlso: Sketcher_ConstrainParallel/pl
---

# Sketcher ConstrainSymmetric/pl

## Opis

**Wiązanie symetrii** nadaje dwóm wybranym punktom symetrię wokół danej prostej, tzn. oba wybrane punkty muszą leżeć na normalnej do prostej przechodzącej przez oba punkty i muszą być jednakowo odległe od tej prostej. Alternatywnie funkcja ta może wymuszać, aby dwa punkty były symetryczne względem trzeciego.

## Użycie

<img alt="" src=images/SymmetricConstraint1.png  style="width:500px;">

Wybierz dwa punkty *(wierzchołki)* oraz linię na szkicu. Wybrane punkty i prosta będą miały kolor ciemnozielony.

<img alt="" src=images/SymmetricConstraint2.png  style="width:500px;">

Kliknij na przycisk **[<img src=images/Sketcher_ConstrainSymmetric.svg style="width:16px"> [Utwórz wiązanie symetrii ...](Sketcher_ConstrainSymmetric/pl.md)** lub wybierz pozycję z menu **Szkic → Wiązana szkicownika → Wiązanie symetrii**.

Spowoduje to zastosowanie tego wiązania do wybranych elementów.

<img alt="" src=images/SymmetricConstraint3.png  style="width:500px;">


**Uwaga:**

Przed wersją 0.19 (zobacz poprawkę [1](https://github.com/FreeCAD/FreeCAD/pull/3746)), jeśli chcesz zdefiniować wiązanie symetrii względem punktu, kolejność wyboru jest ważna, w zależności od tego, czy wybierasz narzędzie na wstępie, czy na końcu.

-   Jeśli klikniesz w narzędzie jako pierwsze: wybierz najpierw pierwszy punkt, następnie punkt odniesienia symetrii, a na końcu drugi punkt.
-   Jeśli narzędzie zostanie kliknięte jako ostatnie: wybierz pierwszy punkt, następnie drugi punkt, a na końcu punkt odniesienia symetrii.

Zobacz tracker [issue #4144](https://freecadweb.org/tracker/view.php?id=4144), oraz [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=39611).

## Tworzenie skryptów 

Dwa punkty i linia symetrii:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Dwa punkty i punkt symetrii:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

Linia i punkt symetrii *(W GUI można wybrać linię i punkt, ale używa się wewnętrznie takiej samej formy jak powyżej, z dwoma końcami tej samej linii)*:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `Line1`, `Line2`, `LineS`, `Line`, `PointOfLine1`, `PointOfLine2` i `PointOfLineS`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/pl
