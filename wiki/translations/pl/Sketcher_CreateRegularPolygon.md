---
 GuiCommand:
   Name: Sketcher CreateRegularPolygon
   Name/pl: Szkicownik: Utwórz wielokąt foremny
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz wielokąt foremny
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **P** **R**
---

# Sketcher CreateRegularPolygon/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:24px;"> **Utwórz wielokąt foremny** tworzy wielokąt regularny.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> '''Utwórz wielokąt foremny'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> Utwórz wielokąt foremny**.
    -   Użyj skrótu klawiaturowego: **G**, **P**, **R**.
2.  Wprowadź **Liczbę boków** w otwartym oknie dialogowym.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Sekcja **Parametry wielokąta** *({{Version/pl|1.0}})* jest dodawana na górze [okna dialogowego](Sketcher_Dialog/pl.md).
5.  Opcjonalnie zmień liczbę **boków** *(można to również zrobić po wybraniu środka)*:
    -   Wprowadź liczbę większą niż dwa.
    -   Naciśnij przycisk **U**, aby zwiększyć liczbę.
    -   Naciśnij przycisk **J**, aby zmniejszyć liczbę.
6.  Wybierz środek wielokąta. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y.
7.  Wybierz pierwszy punkt wielokąta, który definiuje również promień opisanego okręgu. Lub za pomocą Dim-OVP: wprowadź promień okręgu i / lub kąt pierwszego punktu. Kąt jest odniesiony do osi X szkicu. Dla tego kąta nie jest tworzone żadne wiązanie.
8.  Tworzony jest wielokąt, w tym opisany okrąg geometrii konstrukcyjnej i dodawane są odpowiednie wiązania oparte na Pos-OVP i Dim-OVP.
9.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie wielokątów.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   Okrąg geometrii konstrukcji nie jest widoczny poza szkicem. Nie można go usunąć bez naruszenia geometrii wielokąta.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRegularPolygon/pl
