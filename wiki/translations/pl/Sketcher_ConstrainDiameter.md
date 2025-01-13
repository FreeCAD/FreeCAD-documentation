---
 GuiCommand:
   Name: Sketcher ConstrainDiameter
   Name/pl: Szkicownik: Wiązanie średnicy
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie średnicy
   Workbenches: Sketcher_Workbench/pl,
PartDesign_Workbench/pl
   Shortcut: **K** **O**
   Version: 0.18
   SeeAlso: Sketcher_ConstrainRadiam/pl, Sketcher_ConstrainRadius/pl
---

# Sketcher ConstrainDiameter/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;"> **Wiązanie średnicy** ustala średnicę okręgów i łuków. Nie można go używać do [krzywych złożonych przez punkty kontrolne](Sketcher_CreateBSpline/pl#Uwagi.md).



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [ustawienie](Sketcher_Preferences/pl#Ogólne.md) **Wiązania wymiarów** jest aktywne i wybrano {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainDiameter.svg" width=16px> Wiązanie średnicy** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość *(w {{VersionMinus/pl|0.21}})*: naciśnij **<img src="images/Sketcher_ConstrainDiameter.svg" width=16px> '''Wiązanie średnicy'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainDiameter.svg" width=16px> Wiązanie średnicy**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie wymiarów → <img src="images/Sketcher_ConstrainDiameter.svg" width=16px> Wiązanie średnicy** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **O**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz krawędź okręgu lub łuku.
5.  Jeśli utworzono [kontrolujące wiązanie wymiarowe](Sketcher_ToggleDrivingConstraint/pl.md), w zależności od [konfiguracji](Sketcher_Preferences/pl#Wyświetlanie.md), otworzy się okno dialogowe [Wprowadź średnicę](Sketcher_Workbench/pl#Edycja_wiązań.md).
6.  Wiązanie zostanie dodane.
7.  Opcjonalnie można kontynuować tworzenie wiązań.
8.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wybierz krawędź jednego lub więcej okręgów lub łuków.
2.  Wywołaj narzędzie, jak wyjaśniono powyżej.
3.  Opcjonalnie [dostosuj wartość](Sketcher_Workbench/pl#Edycja_wiązań.md).
4.  W zależności od zaznaczenia dodawane jest jedno lub więcej wiązań, patrz [Uwagi](#Uwagi.md).



## Uwagi

-   Jeśli utworzono [wiązanie konstrukcyjne](Sketcher_ToggleDrivingConstraint/pl.md) i wstępnie wybrano wiele elementów, które nie są [geometria zewnętrzną](Sketcher_External/pl.md), tylko pierwszy z nich otrzymuje wiązanie wymiarowe, podczas gdy między pierwszym a pozostałymi stosowane są [wiązania równości](Sketcher_ConstrainEqual/pl.md).



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `ArcOrCircle` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/pl
