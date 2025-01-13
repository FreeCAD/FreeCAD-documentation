---
 GuiCommand:
   Name:  Sketcher Dimension
   Name/pl: Szkicownik: Wiązania wymiarów
   MenuLocation: Szkic , Wiązania szkicownika , Wiązania wymiarów
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **D**
   Version: 1.0
---

# Sketcher Dimension/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Dimension.svg  style="width:24px;"> **Wiązania wymiarów** jest kontekstowym narzędziem wiązań w środowisku pracy Szkicownik. W oparciu o bieżący wybór, oferuje odpowiednie wiązania wymiarowe, ale także wiązania geometryczne.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Opcjonalnie wybierz jeden lub więcej elementów *(krawędzi lub punktów)*. Krawędzie [krzywej złożonej](Sketcher_Workbench#Sketcher_CompCreateBSpline/pl.md) nie są obecnie obsługiwane.
2.  Istnieje kilka sposobów na wywołanie narzędzia:
    -   Jeśli [preferencja](Sketcher_Preferences/pl#Ogólne.md) **Wiązania wymiarów** jest ustawiona na {{Value|Obydwa}} lub {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij przycisk **<img src="images/Sketcher_Dimension.svg" width=16px> [Wiązanie odległości](Sketcher_Dimension/pl.md)**.
    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_Dimension.svg" width=16px> Wiązania wymiarów**.
    -   Kliknij prawym przyciskiem myszy na [widoku 3D](3D_view/pl.md) i wybierz opcję **Wymiar → <img src="images/Sketcher_Dimension.svg" width=16px> Wiązania wymiarów** z menu kontekstowego.
    -   Jeśli istnieje zaznaczenie: Kliknij prawym przyciskiem myszy w widoku 3D i wybierz opcję **<img src="images/Sketcher_Dimension.svg" width=16px> Wiązania wymiarów** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **D**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Jeśli nie wybrano jeszcze żadnego elementu: wybierz go.
5.  W zależności od wybranych elementów zostanie zaproponowane wiązanie.
6.  Opcjonalnie wybierz dodatkowy element.
7.  Opcjonalnie usuń zaznaczenie elementu, klikając go ponownie.
8.  Proponowane ograniczenie jest aktualizowane po każdej zmianie zaznaczenia.
9.  Opcjonalnie naciśnij przycisk **M** jeden lub więcej razy, aby przełączać się między innymi dostępnymi wiązaniami, jeśli takie istnieją.
10. Jeśli proponowane jest wiązanie geometryczne, wybrane elementy mogą się zmienić, dając podgląd wyniku.
11. Wykonaj jedną z następujących czynności:
    -   Kliknij pusty obszar w [3D view](3D_view/pl.md), aby potwierdzić:
        1.  Jeśli tworzone jest wiązanie wymiarowe, kliknięty punkt określa jego położenie. W przypadku wymiaru liniowego kliknięty punkt określa również jego typ: <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:16px;"> [Odległość pozioma](Sketcher_ConstrainDistanceX/pl.md), <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:16px;"> [Odległość pionowa](Sketcher_ConstrainDistanceY/pl.md) lub <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:16px;"> [wiązanie odległości](Sketcher_ConstrainDistance/pl.md).
        2.  Jeśli [wiązanie kontrolujące](Sketcher_ToggleDrivingConstraint/pl.md) zostanie utworzone, w zależności od [preferencji](Sketcher_Preferences/pl#Wyświetlanie.md), otworzy się okno dialogowe [wstaw długość](Sketcher_Workbench/pl#Edycja_wiązań.md).
        3.  Wiązanie jest dodawane.
        4.  To narzędzie zawsze działa w trybie kontynuacji: opcjonalnie można kontynuować tworzenie ograniczeń.
    -   Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Dimension/pl
