---
 GuiCommand:
   Name: Sketcher ConstrainRadiam
   Name/pl: Szkicownik: Zwiąż automatycznie promień / średnicę
   MenuLocation: Szkic , Wiązania szkicownika , Zwiąż automatycznie promień / średnicę
   Workbenches: Sketcher_Workbench/pl,
   Shortcut: **K** **S**
   Version: 0.20
   SeeAlso: Sketcher_ConstrainRadius/pl, Sketcher_ConstrainDiameter/pl
---

# Sketcher ConstrainRadiam/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> **Zwiąż automatycznie promień / średnicę** ustala promień łuków i [okręgów wagowych](Sketcher_CreateBSpline/pl#Uwagi.md) oraz średnicę okręgów.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli **Wiązania wymiarów** [skonfigurowano](Sketcher_Preferences/pl#Ogólne.md) na {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Zwiąż automatycznie promień / średnicę** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość *({{VersionMinus/pl|0.21}})*: naciśnij przycisk **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> '''Zwiąż automatycznie promień / średnicę'''**.

    -   Wybierz z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Zwiąż automatycznie promień / średnicę**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wymiar → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Zwiąż automatycznie promień / średnicę** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **S**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz krawędź okręgu lub łuku.
    -   Wybierz krawędź okręgu o wadze krzywej złożonej.
5.  Jeśli utworzono [konstrukcyjne wiązanie wymiaru](Sketcher_ToggleDrivingConstraint/pl.md), w zależności od [konfiguracji](Sketcher_Preferences/pl#Wyświetlanie.md), otworzy się okno dialogowe [do edycji wartości](Sketcher_Workbench/pl#Edycja_wiązań.md).
6.  Wiązanie zostanie dodane.
7.  Opcjonalnie można kontynuować tworzenie wiązań.
8.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz krawędź jednego lub więcej okręgów lub łuków.
    -   Wybierz krawędź jednego lub więcej okręgów wagi krzywej złożonej.
2.  Wywołaj narzędzie, jak wyjaśniono powyżej.
3.  Opcjonalnie [popraw wartość](Sketcher_Workbench/pl#Edycja_wiązań.md).
4.  W zależności od wyboru dodawane jest jedno lub więcej wiązań, patrz [Uwagi](#Uwagi.md).



## Uwagi

-   Jeśli utworzono [wiązanie konstrukcyjne](Sketcher_ToggleDrivingConstraint/pl.md) i wstępnie wybrano wiele elementów, które nie są [geometria zewnętrzną](Sketcher_External/pl.md), tylko pierwszy z nich otrzymuje wiązanie wymiarowe, podczas gdy między pierwszym a pozostałymi stosowane są [wiązania równości](Sketcher_ConstrainEqual/pl.md).



## Tworzenie skryptów 


```python
Sketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))
Sketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('246.0 mm')))
```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) opisuje wartości, których można użyć dla `ArcOrCircle` i zawiera dalsze przykłady tworzenia wiązań ze skryptów Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/pl
