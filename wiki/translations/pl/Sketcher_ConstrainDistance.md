---
- GuiCommand:
   Name:Constraint Length
   Name/pl:Szkicownik: Wiązanie odległości
   MenuLocation:Szkic → Wiązania szkicownika → Wiązanie odległości
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**K** **D**
   SeeAlso:[Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl.md), [Zwiąż w pionie](Sketcher_ConstrainDistanceY/pl.md)
---

# Sketcher ConstrainDistance/pl



## Opis

**Wiązanie odległości** określa długość prostej, odległość prostopadłą między punktem a prostą, odległość między dwoma punktami lub, {{Version/pl|0.21}}, odległość między krawędziami dwóch okręgów lub między krawędzią okręgu a linią.

![](images/Sketcher_ConstrainDistance_example.png )



## Użycie

1.  Wybierz jedną linię, albo jeden punkt i jedną linię, albo dwa punkty, albo krawędzie dwóch okręgów lub krawędzie okręgu i linii.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> '''Wiązanie odległości'''** znajdujący się na pasku narzędzi Szkicownika.
    -   Użyj kombinacji klawiszy **K** kolejnie **D**. (**D** odnosi się do **D**istance).
    -   Użyj pozycji menu głównego **Szkic → Wiązania szkicownika → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Wiązanie odległości**.
3.  Otworzy się wyskakujące okno dialogowe do edycji z proponowaną wartością. Naciśnij **OK**, aby ją zatwierdzić.

**Uwaga:** Narzędzie wiązania może być również uruchomione bez wcześniejszego zaznaczenia obiektów *(pomijając przypadki typu okrąg do okręgu i okrąg do linii)*. Aby ustawić odległość prostopadłą pomiędzy punktem a prostą, należy najpierw zaznaczyć ten punkt. Domyślnie polecenie jest aktywne w trybie kontynuacji, by utworzyć nowe wiązanie; wciśnij raz prawy przycisk myszki lub klawisz **ESC**, by zakończyć działanie polecenia.



### Podpowiedź

Ewentualnie proszę rozważyć użycie **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl.md)** lub **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Zwiąż w  pionie](Sketcher_ConstrainDistanceY/pl.md)** zamiast tego wiązania. Wymienione wiązania są bardziej efektywne i szybsze do obliczenia niż to to prezentowane.



## Tworzenie skryptów 

Odległość od odniesienia położenia:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Odległość pomiędzy dwoma wierzchołkami:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Długość linii *(GUI pozwala wybrać samą krawędź, ale jest to tylko skrót do użycia dwóch skrajnych punktów tej samej linii)*:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Odległość od punktu (`Edge, PointOfEdge`) do najbliższego prostopadłego punktu na linii (`Line`):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, 0, App.Units.Quantity('123.0 mm')))```

Odległość między krawędziami dwóch okręgów:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Circle1, 0, Circle2, 0, App.Units.Quantity('123.0 mm')))```

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `Edge`,`Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2` i `Line` oraz `Circle1`, `Circle2` a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/pl
