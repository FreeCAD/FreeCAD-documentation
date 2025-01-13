---
 GuiCommand:
   Name: Sketcher ConstrainDistanceY
   Name/pl: Szkicownik: Zwiąż odległość pionową
   Workbenches: Sketcher_Workbench/pl
   MenuLocation: Szkic , Wiązania szkicownika , Zwiąż odległość pionową
   Shortcut: **I**
   SeeAlso: Sketcher_ConstrainDistanceX/pl, Sketcher_ConstrainDistance/pl
---

# Sketcher ConstrainDistanceY/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> **Zwiąż odległość pionową** ustala pionową odległość między dwoma punktami lub punktami końcowymi linii. Jeśli wstępnie wybrano pojedynczy punkt, odległość jest względna do początku szkicu.

![](images/Sketcher_ConstraintDistanceY_example.png )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [ustawienie](Sketcher_Preferences/pl#Ogólne.md) **Wiązania wymiarów** jest aktywne i wybrano {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_ConstrainDistanceY.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Zwiąż odległość poziomą** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość *({{VersionMinus/pl|0.21}})*: naciśnij **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> '''Zwiąż odległość pionową'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Zwiąż odległość pionową**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie wymiarów → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Zwiąż odległość pionową** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **I**.
3.  Dalsze kroki można znaleźć w prezentacji narzędzia [Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl#Tryb_kontynuacji.md).



### Tryb jednorazowy 

Zapoznaj się z informacjami na stronie: [Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl#Tryb_jednorazowy.md).



## Tworzenie skryptów 

Odległość od odniesienia położenia:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Odległość pomiędzy dwoma wierzchołkami:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Pozioma rozpiętość linii *(GUI pozwala wybrać samą krawędź, ale jest to tylko skrót do użycia dwóch skrajnych punktów tej samej linii)*:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2` i `Line`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/pl
