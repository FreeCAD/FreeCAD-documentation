---
 GuiCommand:
   Name: Sketcher Trimming
   Name/pl: Szkicownik: Przytnij krawędź
   MenuLocation: Szkic , Narzędzia szkicownika , Przytnij krawędź
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **T**
   Version: 0.12
   SeeAlso: Sketcher_Split/pl, Sketcher_Extend/pl
---

# Sketcher Trimming/pl



## Opis

To narzędzie <img alt="" src=images/Sketcher_Trimming.svg  style="width:24px;"> przycina krawędź w miejscu najbliższego przecięcia z innymi krawędziami. Jeśli wybrana krawędź nie przecina innych krawędzi, zostanie usunięta.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_Trimming.svg" width=16px> '''Przytnij krawędź'''**.
    -   Wybierz z menu opcję **Szkicownik → Narzędzia szkicownika → <img src="images/Sketcher_Trimming.svg" width=16px> Przytnij krawędź**.
    -   Kliknij prawym przyciskiem myszy w oknie [widoku 3D](3D_view/pl.md) i z menu podręcznego wybierz opcję **<img src="images/Sketcher_Trimming.svg" width=16px> Przytnij krawędź**.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **T**.
2.  Jeśli istnieje poprzednie zaznaczenie, zostanie ono usunięte. Narzędzie nie akceptuje wstępnego zaznaczenia.
3.  Kursor zmienia się w krzyżyk z ikoną narzędzia.
4.  Dostępne są dwa tryby:
    -   Przycinanie jednym kliknięciem:
        1.  Przesuń kursor nad część krawędzi, która ma zostać przycięta.
        2.  Krawędź zostanie podświetlona, a punkty przycięcia zostaną oznaczone tymczasowymi okręgami.
        3.  Kliknij, aby potwierdzić.
        4.  Krawędź zostanie przycięta w zaznaczonych punktach.
    -   Przytrzymaj i przeciągnij: {{Version/pl|1.0}}
        1.  Przytrzymaj lewy przycisk myszki.
        2.  Przesuń kursor nad fragmenty krawędzi, które mają zostać przycięte.
        3.  Przycinanie następuje natychmiast.
        4.  Zwolnij lewy przycisk myszy.
5.  Jeśli fragment zostanie wycięty, istniejące wiązania zostaną przeniesione na nową krawędź. Wiązania [Punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) są dodawane między punktem*(ami)* końcowym*(i)* przyciętej krawędzi a krawędzią*(ami)* tnącą*(i)*.
6.  To narzędzie zawsze działa w trybie kontynuacji: opcjonalnie kontynuuj przycinanie krawędzi.
7.  Aby zakończyć, kliknij w pustym obszarze w [widoku 3D](3D_view/pl.md), kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Trimming/pl
