---
 GuiCommand:
   Name: Sketcher ConstrainDistanceY
   Name/pl: Szkicownik: Zwiąż w pionie
   Workbenches: Sketcher_Workbench/pl
   MenuLocation: Szkic , Wiązania szkicownika , Zwiąż w pionie
   Shortcut: **I**
   SeeAlso: Sketcher_ConstrainDistanceX/pl, Sketcher_ConstrainDistance/pl
---

# Sketcher ConstrainDistanceY/pl



## Opis

Ustala poziomą odległość pomiędzy dwoma punktami lub końcami linii. Jeśli wybrany jest tylko jeden punkt, odległość jest ustalana względem punktu początku szkicu.

![](images/Sketcher_ConstraintDistanceY_example.png )



## Użycie

1.  Wybierz jeden lub dwa punkty albo jedną linię.
2.  Uruchomić narzędzie na jeden z możliwych sposobów:
    -   Naciśnij przycisk **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> '''Zwiąż w pionie'''** znajdujący się na pasku narzędzi Szkicownika.
    -   Użyj klawisza **I**.
    -   Użyj polecenia menu głównego **Sketch → Wiązania szkicownika → [<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> Zwiąż w pionie**.
3.  Otworzy się wyskakujące okno dialogowe do edycji z proponowaną wartością. Naciśnij **OK**, aby ją wartość.

**Uwaga:** Narzędzie wiązania może być również uruchomione bez wcześniejszego zaznaczenia obiektów, ale będzie wymagane wybranie dwóch punktów lub jednej linii. Aby ustawić odległość względem punktu początkowego, należy także zaznaczyć punkt początkowy szkicu. Domyślnie polecenie jest aktywne w trybie kontynuacji, by utworzyć nowe wiązanie; wciśnij raz prawy przycisk myszki lub klawisz **Esc**, by zakończyć działanie polecenia.



## Tworzenie skryptów 

Odległość od odniesienia położenia:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Odległość pomiędzy dwoma wierzchołkami:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Pozioma rozpiętość linii *(GUI pozwala wybrać samą krawędź, ale jest to tylko skrót do użycia dwóch skrajnych punktów tej samej linii)*:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` i `Line`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/pl
