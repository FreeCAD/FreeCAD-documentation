---
 GuiCommand:
   Name: Sketcher ConstrainDistanceX
   Name/pl: Szkicownik: Zwiąż odległość poziomą
   MenuLocation: Szkic , Wiązania szkicownika , Zwiąż odległość poziomą
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **L**
   SeeAlso: Sketcher_ConstrainDistance/pl, Sketcher_ConstrainDistanceY/pl
---

# Sketcher ConstrainDistanceX/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> **Zwiąż odległość poziomą** ustala poziomą odległość między dwoma punktami lub punktami końcowymi linii. Jeśli wstępnie wybrano pojedynczy punkt, odległość jest względna do początku szkicu.

![](images/Constraint_H_Distance.png )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [ustawienie](Sketcher_Preferences/pl#Ogólne.md) **Wiązania wymiarów** jest aktywne i wybrano {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_ConstrainDistanceX.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Zwiąż odległość poziomą** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość *({{VersionMinus/pl|0.21}})*: naciśnij **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> '''Zwiąż odległość poziomą'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Zwiąż odległość poziomą**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie wymiarów → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Zwiąż odległość poziomą** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **L**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty *(jeden z nich może być punktem początkowym)*.
    -   Wybierz pojedynczą linię.
5.  Jeśli utworzono [kontrolujące wiązanie wymiarowe](Sketcher_ToggleDrivingConstraint/pl.md), w zależności od [konfiguracji](Sketcher_Preferences/pl#Wyświetlanie.md), otworzy się okno dialogowe [Wprowadź długość](Sketcher_Workbench/pl#Edycja_wiązań.md).
6.  Wiązanie zostanie dodane.
7.  Opcjonalnie można kontynuować tworzenie wiązań.
8.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz jeden lub dwa punkty.
    -   Wybierz pojedynczą linię.
2.  Wywołaj narzędzie, jak wyjaśniono powyżej.
3.  Opcjonalnie [dostosuj wartość](Sketcher_Workbench/pl#Edycja_wiązań.md).
4.  Wiązanie zostało dodane.



## Tworzenie skryptów 

Odległość od odniesienia położenia:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Odległość pomiędzy dwoma wierzchołkami:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Pozioma rozpiętość linii *(GUI pozwala wybrać samą krawędź, ale jest to tylko skrót do użycia dwóch skrajnych punktów tej samej linii)*:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` i `Line`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/pl
