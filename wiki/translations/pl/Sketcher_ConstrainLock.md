---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/pl: Sketcher: Wiązanie blokady odległości
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie blokady odległości
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **K** **L**
   SeeAlso: Sketcher_ConstrainBlock/pl
---

# Sketcher ConstrainLock/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;">**Wiązanie blokady odległości** nakłada [dystans poziomy](Sketcher_ConstrainDistanceX/pl.md) i [dystans pionowy](Sketcher_ConstrainDistanceY/pl.md) na punkty. Jeśli wybrany jest pojedynczy punkt, wiązania odnoszą się do początku szkicu. Jeśli wybrano dwa lub więcej punktów, ograniczenia odnoszą się do ostatniego punktu w zaznaczeniu.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [ustawienie](Sketcher_Preferences/pl#Ogólne.md) **Wiązania wymiarów** jest aktywne i wybrano {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainLock.svg" width=16px> Wiązanie blokady odległości** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość ({{VersionMinus/pl|0.21}}): naciśnij przycisk **<img src="images/Sketcher_ConstrainLock.svg" width=16px> '''Wiązanie blokady odległości'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Wiązanie blokady odległości**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązanie → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Wiązanie blokady odległości** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **L**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz pojedynczy punkt.
5.  Zostaną dodane dwa wiązania.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wybierz jeden lub więcej punktów.
2.  Wywołaj narzędzie, jak wyjaśniono powyżej.
3.  W zależności od wyboru dodawane są dwa lub więcej wiązań.



## Uwagi

-   Nie ma automatycznego monitu o edycję wartości wiązań. Jeśli jest to wymagane, wartości mogą być [edytowane](Sketcher_Workbench/pl#Edycja_wiązań.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/pl
