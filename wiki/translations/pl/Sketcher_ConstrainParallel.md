---
 GuiCommand:
   Name: Sketcher ConstrainParallel
   Name/pl: Szkicownik: Wiązanie równoległości
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie równoległości
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **P**
   SeeAlso: 
---

# Sketcher ConstrainParallel/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> **Zwiąż równolegle** wymusza, aby linie były równoległe.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> '''Wiązanie równoległości'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Wiązanie równoległości**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Wiązanie równoległości** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **P**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz dwie linie.
5.  Ograniczenie zostanie dodane.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wybierz dwie lub więcej linii. {{Version/pl|1.0}}: Punkty mogą zostać uwzględnione w zaznaczeniu, ale zostaną zignorowane.
2.  Wywołaj narzędzie jak wyjaśniono powyżej lub z następującą dodatkową opcją:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> Wiązanie równoległości** z menu podręcznego.
3.  W zależności od wyboru dodawane jest jedno lub więcej ograniczeń.



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Line1` oraz `Line2` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/pl
