---
 GuiCommand:
   Name: Sketcher Extend
   Name/pl: Szkicownik: Przedłuż krawędź
   MenuLocation: Szkic , Narzędzia szkicownika , Przedłuż krawędź
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **Q**
   Version: 0.17
   SeeAlso: Sketcher_Trimming/pl
---

# Sketcher Extend/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Extend.svg  style="width:24px;"> **Przedłuż krawędź** wydłuża lub skraca linię lub łuk do dowolnego miejsca lub do docelowej krawędzi lub punktu.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*Rysunek z lewej '''(1)''', dwa elementy szkicu przed operacją,<br>w środku '''(2)''', linia jest przedłużana do łuku,<br>z prawej '''(3)''', efekt końcowy.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_Extend.svg" width=16px> '''Przedłuż krawędź'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_Extend.svg" width=16px> Przedłuż krawędź**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i z menu kontekstowego wybierz opcję **<img src="images/Sketcher_Extend.svg" width=16px> Przedłuż krawędź**.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **Q**.
2.  Jeśli istnieje poprzednie zaznaczenie, zostanie ono usunięte. Narzędzie nie akceptuje wstępnego zaznaczenia.
3.  Kursor zmienia się w krzyżyk z ikoną narzędzia.
4.  Wybierz linię lub łuk.
5.  Przesuń kursor w kierunku, w którym chcesz wydłużyć lub skrócić.
6.  Wykonaj jedną z następujących czynności:
    -   Kliknij dowolny punkt.
    -   Aby wydłużyć / skrócić do innej krawędzi opcja *([wiązania automatyczne](Sketcher_Workbench/pl#Wiązania_automatyczne.md) musi być włączona)*: Umieść kursor nad krawędzią docelową. Gdy jest ona podświetlona, a ikona wiązania <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) pojawi się obok kursora, kliknij aby potwierdzić. Wiązanie zostanie dodane.
    -   Aby wydłużyć / skrócić do punktu *(automatyczne wiązania muszą być włączone)*: Umieść kursor nad punktem docelowym. Gdy jest on podświetlony i obok kursora pojawi się ikona <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [wiązania zbieżności](Sketcher_ConstrainCoincident/pl.md), kliknij, aby potwierdzić. Wiązanie zostanie dodane.
7.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj wydłużanie / skracanie krawędzi.
    2.  Aby zakończyć, kliknij w pustym obszarze w [widoku 3D](3D_view/pl.md), kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   Docelowy obiekt krawędzi lub punktu może być również modyfikowany, jeśli nie jest w pełni związany.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/pl
