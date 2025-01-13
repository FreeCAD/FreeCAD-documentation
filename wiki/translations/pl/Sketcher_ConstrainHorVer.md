---
 GuiCommand:
   Name:  Sketcher ConstrainHorVer
   Name/pl: Szkicownik: Wiązanie poziomo / pionowo
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie poziomo / pionowo
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **A**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainHorizontal/pl, Sketcher_ConstrainVertical/pl
---

# Sketcher ConstrainHorVer/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:24px;"> **Wiązanie poziomo / pionowo** ogranicza linie lub pary punktów, aby były poziome *(równoległe do poziomej osi szkicu)* lub pionowe, w zależności od tego, co jest najbliższe bieżącemu wyrównaniu.

Narzędzie to łączy [Wiązanie poziomo](Sketcher_ConstrainHorizontal/pl.md) i [wiązanie pionowo](Sketcher_ConstrainVertical/pl.md).



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Jeśli w [ustawieniach](Sketcher_Preferences/pl#Ogólne.md) wybrana jest opcja **Automatyczne narzędzie dla wiązania poziomo / pionowo** *(domyślnie)*: naciśnij przycisk **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> '''Wiązanie poziomo / pionowo'''**.
    -   Wybierz z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Wiązanie poziomo / pionowo**.
    -   Kliknij prawym przyciskiem myszy [widok 3D](3D_view/pl.md) i wybierz **Wiązanie → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Constrain horizontal/vertical** z menu podręcznego.
    -   Użyj skrótu klawiaturowego: **A**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty.
    -   Wybierz pojedynczą linię.
5.  Zostanie dodane wiązanie.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa lub więcej punktów *(kolejność wyboru może być istotna, patrz [Uwagi](#Uwagi.md))*.
    -   Wybierz jedną lub więcej linii. Punkty mogą zostać uwzględnione w zaznaczeniu, ale zostaną zignorowane.
2.  Wywołaj narzędzie jak wyjaśniono powyżej lub z następującą dodatkową opcją:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Wiązanie poziomo / pionowo** z menu kontekstowego.
3.  W zależności od wyboru dodawane jest jedno lub więcej wiązań.



## Uwagi

Więcej niż dwa punkty są przetwarzane w kolejności wyboru, po jednej parze na raz. Pierwszy punkt jest łączony z drugim. Podczas wiązania drugi punkt może się przesunąć. Nowa lokalizacja drugiego punktu określa, które wiązanie jest stosowane, gdy wiązane są drugi i trzeci punkt itd.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorVer/pl
