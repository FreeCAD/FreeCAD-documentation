---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   Name/pl: Szkicownik: Wiązanie równości
   Workbenches: Sketcher_Workbench/pl
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie równości
   Shortcut: **E**
   SeeAlso: 
---

# Sketcher ConstrainEqual/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> **Wiązanie równości** ogranicza krawędzie, aby miały taką samą długość *(linie)* lub krzywiznę *(inne krawędzie z wyjątkiem [krzywej złożonej](Sketcher_CreateBSpline/pl.md))*. Wybrane krawędzie muszą być tego samego typu. Okręgi i łuki kołowe są tego samego typu *(ich promienie są równe)*, podobnie jak elipsy i łuki eliptyczne *(ich główne i mniejsze promienie są równe)*.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> '''Wiązanie równości'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Wiązanie równości**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Wiązanie równości** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **E**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz dwie krawędzie tego samego typu.
5.  Zostanie dodane wiązanie.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wybierz jedną lub więcej krawędzi.
2.  Wywołaj narzędzie jak wyjaśniono powyżej lub z następującą dodatkową opcją:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widok 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> Wiązanie równości** z menu podręcznego.
3.  W zależności od wyboru dodawane jest jedno lub więcej wiązań.



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Edge1` oraz `Edge2` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/pl
