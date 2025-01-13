---
 GuiCommand:
   Name: Sketcher ConstrainSymmetric
   Name/pl: Szkicownik: Wiązanie symetrii
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie symetrii
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **S**
   SeeAlso: 
---

# Sketcher ConstrainSymmetric/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> **Wiązanie symetrii** wiąże dwa punkty, aby były symetryczne wokół linii lub osi, lub wokół trzeciego punktu.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> '''Wiązanie symetrii'''**.

    -   Wybierz z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Wiązanie symetrii**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Wiązanie symetrii** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **S**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty i punkt symetrii *(w tej kolejności)*.
    -   Wybierz dwa punkty i linię symetrii *(w tej samej kolejności)*.
    -   Wybierz punkt, linię symetrii i kolejny punkt *(w tej samej kolejności)*.
    -   Wybierz linię i punkt symetrii *(analogicznie)*.
5.  Wiązanie zostanie dodane.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty i punkt symetrii *(w tej kolejności)*.
    -   Wybierz dwa punkty i linię symetrii *(w dowolnej kolejności)*.
    -   Wybierz linię i punkt symetrii *(w tej samej kolejności)*.
2.  Wywołaj narzędzie jak wyjaśniono powyżej lub z następującą dodatkową opcją:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widok 3D](3D_view/pl.md) i wybierz **<img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Wiązanie symetrii** z menu podręcznego.
3.  Wiązanie zostanie dodane.



## Uwagi

-   Strzałki tego wiązania pokazują kolor więzów wymiarowych.



## Tworzenie skryptów 

Dwa punkty i linia symetrii:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Dwa punkty i punkt symetrii:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

Linia i punkt symetrii *(W GUI można wybrać linię i punkt, ale używa się wewnętrznie takiej samej formy jak powyżej, z dwoma końcami tej samej linii)*:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `Line1`, `Line2`, `LineS`, `Line`, `PointOfLine1`, `PointOfLine2` i `PointOfLineS`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/pl
