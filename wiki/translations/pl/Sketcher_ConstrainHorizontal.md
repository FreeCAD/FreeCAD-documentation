---
 GuiCommand:
   Icon: Constraint Horizontal.svg
   Name: Sketcher ConstrainHorizontal
   Name/pl: Szkicownik: Zwiąż w poziomie
   MenuLocation: Szkic , Wiązania szkicownika , Zwiąż w poziomie
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **H**
   SeeAlso: Sketcher_ConstrainHorVer/pl, Sketcher_ConstrainVertical/pl
---

# Sketcher ConstrainHorizontal/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> **Zwiąż w poziomie** ogranicza linie lub pary punktów, aby były poziome *(równoległe do poziomej osi szkicu)*.


{{Version/pl|1.0}}

: W większości przypadków zaleca się użycie połączonego narzędzia [Poziomo / pionowo](Sketcher_ConstrainHorVer/pl.md).



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [ustawienie](Sketcher_Preferences/pl#Ogólne.md) **Automatyczne narzędzie dla wiązania poziomo / pionowo** jest aktywne *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_ConstrainHorVer.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Zwiąż w poziomie** z rozwijanej listy.

    -   Jeśli ta preferencja nie jest wybrana \'\'(i {{VersionMinus/pl|0.21}}): naciśnij **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> '''Zwiąż w poziomie'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Zwiąż w poziomie**.

    -   Użyj skrótu klawiaturowego: **H**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty.
    -   Wybierz pojedynczą linię.
5.  Wiązanie zostanie dodane.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa lub więcej punktów.
    -   Wybierz jedną lub więcej linii. Punkty mogą zostać uwzględnione w zaznaczeniu, ale zostaną zignorowane.
2.  Wywołaj narzędzie jak wyjaśniono powyżej lub z następującą dodatkową opcją:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Zwiąż w poziomie** z menu kontekstowego.
3.  W zależności od wyboru dodawane jest jedno lub więcej ograniczeń.



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Line` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/pl
