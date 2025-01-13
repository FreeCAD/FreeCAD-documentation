---
 GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/pl: Szkicownik: Wiązanie zablokowania
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie zablokowania
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **K** **B**
   Version: 0.17
   SeeAlso: Sketcher_ConstrainLock/pl
---

# Sketcher ConstrainBlock/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> **Wiązanie zablokowania** blokuje krawędzie w miejscu za pomocą pojedynczego wiązania. Jest ono przeznaczone głównie dla [krzywych złożonych](Sketcher_CreateBSpline/p.md), które mogą być trudne do pełnego związania w inny sposób.

Wiązanie blokujące wpływa tylko na swobodnie ruchome części krawędzi. Zablokowane krawędzie mogą mieć inne wiązania, a zastosowanie dodatkowych wiązań do zablokowanej krawędzi może ją zmodyfikować.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> '''Wiązanie zablokowania'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Wiązanie zablokowania**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Wiązanie zablokowania** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **B**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz pojedynczą krawędź.
5.  Zostanie dodane wiązanie.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wybierz jedną lub więcej krawędzi.
2.  Wywołaj narzędzie jak wyjaśniono powyżej lub z następującą dodatkową opcją:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widok 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> Wiązanie zablokowania** z menu podręcznego.
3.  W zależności od wyboru dodawane jest jedno lub więcej ograniczeń.



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Krawędzi` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/pl
