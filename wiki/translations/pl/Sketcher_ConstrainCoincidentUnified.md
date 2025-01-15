---
 GuiCommand:
   Name: Sketcher ConstrainCoincidentUnified
   Name/pl: Szkicownik: Wiązanie zbieżności punktów 
   MenuLocation: Szkicownik , Wiązania szkicownika , Wiązanie zbieżności punktów 
   Workbenches: Sketcher Workbench/pl
   Shortcut: **C**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainCoincident/pl, Sketcher_ConstrainPointOnObject/pl
---

# Sketcher ConstrainCoincidentUnified/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:24px;"> tworzy wiązanie zbieżne między punktami. Polecenie **Wiązanie zbieżności punktów *(ujednolicone)*** tworzy wiązanie zbieżne między punktami, ustala punkty na krawędziach lub osiach *(linie są wtedy traktowane jako nieskończone, a otwarte krzywe są również praktycznie wydłużone)*, lub tworzy wiązanie koncentryczne między okręgami, łukami i / lub elipsami *(poprzez uczynienie ich środków zbieżnymi)*.

Narzędzie to zastępuje polecenia [Wiązanie zbieżności punktów](Sketcher_ConstrainCoincident/pl.md) i [Zwiąż punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md), jeśli opcja **Połącz wiązania zbieżności i punkt na obiekcie** jest zaznaczona w [Ustawieniach](Sketcher_Preferences/pl#Ogólne.md) szkicownika.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> '''Wiązanie zbieżności'''**.
    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika constraints → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Wiązanie zbieżności**.
    -   Kliknij prawym przyciskiem myszy w oknie [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązania → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Wiązanie zbieżności** z menu podręcznego.
    -   Użyj skrótu klawiaturowego: **C**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty.
    -   Wybierz dwie krawędzie okręgów, łuków, elips lub łuków elips.
    -   Wybierz pojedynczy punkt i pojedynczą krawędź *(w dowolnej kolejności)*.
5.  Wiązanie zostanie dodane.
6.  Opcjonalnie można kontynuować tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwa lub więcej punktów.
    -   Wybierz dwie lub więcej krawędzi okręgów, łuków, elips lub łuków elips.
    -   Wybierz pojedynczy punkt i pojedynczą krawędź *(w dowolnej kolejności)*.
    -   Wybierz kilka punktów i jedną krawędź *(analogicznie)*.
    -   Wybierz pojedynczy punkt i kilka krawędzi *(analogicznie)*.
2.  Wywołaj narzędzie w sposób opisany powyżej lub za pomocą następującej dodatkowej opcji:
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Wiązanie zbieżności** z menu podręcznego.
3.  W zależności od wyboru dodawane jest jedno lub więcej wiązań.



## Uwagi

-    {{Version/pl|1.0}}: Punkty z wiązaniami zbieżnymi są oznaczone [kolorem](Sketcher_Preferences/pl#Wyświetlanie.md) **symboli wiązań**.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincidentUnified/pl
