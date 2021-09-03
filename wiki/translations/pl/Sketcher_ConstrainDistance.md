---
- GuiCommand:/pl
   Name:Constraint Length
   Name/pl:Wiązanie odległości
   MenuLocation:Szkic → Wiązania szkicownika → Wiązanie odległości
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**Shift** + **D**
   SeeAlso:[Wiązanie odległości poziomej](Sketcher_ConstrainDistanceX/pl.md), [Wiązanie odległości pionowej](Sketcher_ConstrainDistanceY/pl.md)
---

## Opis

Wiązanie odległości wyznacza długość linii, czyli odległość prostopadłą między punktem a linią, lub odległość między dwoma punktami, aby osiągnąć wymaganą wartość.

![](images/Sketcher_ConstrainDistance_example.png )

## Użycie

1.  Wybierz dwa punkty lub jeden punkt i jedną linię albo jedną linię.
2.  Wywołaj komendę na kilka sposobów:
    -   Naciśnij przycisk **<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md)** znajdujący się na pasku narzędzi Szkicownika.
    -   Użyj kombinacji klawiszy **Shift** + **D**. (**D** odnosi się do **D**istance).
    -   Użyj pozycji menu głównego {{MenuCommand|Szkic → Wiązania szkicownika → <img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Wiązanie odległości}}.
3.  Otworzy się wyskakujące okno dialogowe do edycji z proponowaną wartością. Naciśnij **OK**, aby ją zatwierdzić.

**Uwaga:** Narzędzie wiązania może być również uruchomione bez wcześniejszego zaznaczenia obiektów. Aby ustawić odległość prostopadłą pomiędzy punktem a prostą, należy najpierw zaznaczyć ten punkt. Domyślnie polecenie jest aktywne w trybie kontynuacji, by utworzyć nowe wiązanie; wciśnij raz prawy przycisk myszki lub klawisz **ESC**, by zakończyć działanie polecenia.

### Podpowiedź

Ewentualnie proszę rozważyć użycie **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> <img src=images/Sketcher_ConstrainDistanceY.svg style="width:Ustal poziomą odległość ...](Sketcher_ConstrainDistanceX/pl.md)** lub **[16px"> [Ustal pionową odległość ...](Sketcher_ConstrainDistanceY/pl.md)** zamiast tego wiązania. Wymienione wiązania są bardziej efektywne i szybsze do obliczenia niż to to prezentowane.

## Tworzenie skryptów {#tworzenie_skryptów}

Odległość od odniesienia położenia:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Odległość pomiędzy dwoma wierzchołkami:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Długość linii *(GUI pozwala wybrać samą krawędź, ale jest to tylko skrót do użycia dwóch skrajnych punktów tej samej linii)*: 
```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Odległość od punktu (`Edge, PointOfEdge`) do najbliższego punktu na linii (`Line`): 
```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, App.Units.Quantity('123.0 mm')))```

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` i `Line`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher Tools navi

}}  
