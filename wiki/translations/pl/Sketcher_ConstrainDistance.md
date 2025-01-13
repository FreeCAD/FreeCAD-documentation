---
 GuiCommand:
   Name: Constraint Length
   Name/pl: Szkicownik: Wiązanie odległości
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie odległości
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **K** **D**
   SeeAlso: Sketcher_ConstrainDistanceX/pl, Sketcher_ConstrainDistanceY/pl
---

# Sketcher ConstrainDistance/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> **Wiązanie odległości** ustala długość prostej, odległość między dwoma punktami, odległość prostopadłą między punktem a prostą, lub {{Version/pl|0.21}} odległość między krawędziami dwóch okręgów lub łuków, lub między krawędzią okręgu lub łuku a prostą, lub {{Version/pl|1.0}} długość łuku.

![](images/Sketcher_ConstrainDistance_example.png )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [ustawienie](Sketcher_Preferences/pl#Ogólne.md) **Wiązania wymiarów** jest aktywne i wybrano {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> Wiązanie odległości** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość *(w {{VersionMinus|0.21}})*: naciśnij **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> '''Wiązanie odległości'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainDistance.svg" width=16px> Wiązanie odległości**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie wymiarów → <img src="images/Sketcher_ConstrainDistance.svg" width=16px> Wiązanie odległości** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **D**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz krawędź okręgu lub łuku.
5.  Jeśli utworzono [kontrolujące wiązanie wymiarowe](Sketcher_ToggleDrivingConstraint/pl.md), w zależności od [konfiguracji](Sketcher_Preferences/pl#Wyświetlanie.md), otworzy się okno dialogowe [Wprowadź \...](Sketcher_Workbench/pl#Edycja_wiązań.md).
6.  Wiązanie zostanie dodane.
7.  Opcjonalnie można kontynuować tworzenie wiązań.
8.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz pojedynczą linię.

    -   Wybierz dwa punkty.

    -   Wybierz punkt i linię (w dowolnej kolejności).

    -   Wybierz krawędzie dwóch okręgów lub łuków.

    -   Wybierz krawędź okręgu lub łuku i linię (idem).

    -   
        {{Version/pl|1.0}}
        
        : Wybieranie krawędzi pojedynczego łuku.
2.  Wywołaj narzędzie, jak wyjaśniono powyżej.
3.  Opcjonalnie [dostosuj wartość](Sketcher_Workbench/pl#Edycja_wiązań.md).
4.  Wiązanie zostanie dodane.



## Uwagi

-   Jeśli ma to zastosowanie, rozważ użycie wiązań **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl.md)** lub **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Zwiąż w pionie](Sketcher_ConstrainDistanceY/pl.md)** zamiennie. Są one bardziej wydajne.



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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/pl
