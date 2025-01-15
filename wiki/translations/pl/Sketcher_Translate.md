---
 GuiCommand:
   Name: Sketcher TranslatePrzekształcanie w szykuPrzekształcenie
   MenuLocation: Szkic , Narzędzia szkicownika , Przekształcanie w szyku
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Translate/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Translate.svg  style="width:24px;">**Przekształcanie w szyku** przesuwa lub opcjonalnie tworzy kopie wybranych elementów. Kopie są równomiernie rozłożone wzdłuż jednego lub dwóch kierunków.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}



### Przesunięcie geometrii 

1.  Wybierz jedną lub więcej krawędzi i / lub obiektów [punktów](Sketcher_CreatePoint/pl.md). Przetwarzane są również więzy nałożone na wybrane elementy. Wszelkie inne wiązania powiązane z elementami zostaną usunięte.
2.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Sketcher_Translate.svg" width=16px> '''Przekształcanie w szyku'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzie szkicownika → <img src="images/Sketcher_Translate.svg" width=16px> Przekształcanie w szyku**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_Translate.svg" width=16px> Przekształcanie w szyku** z menu podręcznego.
    -   Użyj skrótu klawiaturowego: **W**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Sekcja **Parametry przekształcenia** jest dodawana w górnej części [okna dialogowego](Sketcher_Dialog/pl.md).
5.  Wybierz punkt początkowy wektora przekształcenia. Lub z Pos-OVP: wprowadź jego współrzędne X i / lub Y.
6.  Wybierz punkt końcowy wektora przekształcenia. Lub za pomocą Dim-OVP: wprowadź długość i / lub kąt wektora. Kąt jest odniesiony do osi X szkicu.
7.  Elementy zostaną przesunięte. Nie są dodawane żadne wiązania oparte na Pos-OVP lub Dim-OVP.



### Kopia geometrii 

1.  Wybierz jedną lub więcej krawędzi i / lub obiektów [punktów](Sketcher_CreatePoint/pl.md). Przetwarzane są również więzy nałożone na wybrane elementy.
2.  Wywołaj narzędzie, jak wyjaśniono powyżej.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Sekcja **Parametry przekształcenia** jest dodawana na górze [okna dialogowego](Sketcher_Dialog/pl.md).
5.  Opcjonalnie zmień liczbę **kopii** wzdłuż pierwszego wektora:
    -   Wprowadź liczbę.
    -   Naciśnij przycisk **U**, aby zwiększyć liczbę.
    -   Naciśnij przycisk **J**, aby zmniejszyć liczbę.
6.  Opcjonalnie zmień liczbę **rzędów** wzdłuż drugiego wektora:
    -   Wprowadź liczbę.
    -   Naciśnij przycisk **R**, aby zwiększyć liczbę.
    -   Naciśnij przycisk **F**, aby zmniejszyć liczbę.
7.  Opcjonalnie zaznacz pole wyboru *\'Zastosuj więzy równości*, aby utworzyć <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [więzy równości](Sketcher_ConstrainEqual/pl.md) zamiast kopii wiązań odległości, promienia i średnicy.
8.  Wybierz punkt początkowy pierwszego wektora. Lub za pomocą Pos-OVP: wprowadź jego współrzędną X i / lub Y. Ten wektor definiuje przesunięcie między kopiami.
9.  Wybierz punkt końcowy pierwszego wektora. Lub za pomocą Dim-OVP: wprowadź długość i / lub kąt wektora. Kąt odnosi się do osi X szkicu.
10. Jeśli są dwa lub więcej wierszy: Wybierz punkt końcowy drugiego wektora. Lub za pomocą Dim-OVP: wprowadź długość i / lub kąt wektora. Kąt odnosi się do osi X szkicu. Ten wektor definiuje przesunięcie między wierszami.
11. Elementy zostaną skopiowane. Nie są dodawane żadne wiązania oparte na Pos-OVP lub Dim-OVP.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Translate/pl
