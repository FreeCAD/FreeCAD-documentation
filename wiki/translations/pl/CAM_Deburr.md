---
 GuiCommand:
   Name: CAM Deburr
   Name/pl: CAM: Usuwanie zadziorów
   MenuLocation: CAM , Usuwanie zadziorów
   Workbenches: CAM_Workbench/pl
   Version: 0.18
---

# CAM Deburr/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Deburr.svg  style="width:24px;"> **Usuwanie zadziorów** służy przede wszystkim do gratowania krawędzi.



## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wciśnij przycisk **<img src="images/CAM_Deburr.svg" width=16px> [Usuwanie zadziorów](CAM_Deburr/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_Deburr.svg" width=16px> Usuwanie zadziorów** z menu.
2.  Otwiera się panel zadań **Usuwanie zadziorów**. Zobacz [Opcje](#Opcje.md).
3.  Wybierz **Geometrię bazową**.
4.  Określ wymagane parametry.
5.  Naciśnij przycisk **OK**.



## Opcje

Po wybraniu geometrii w sekcji **Geometria bazowa** panelu zadań możesz wcisnąć przycisk **Zastosuj** aby zobaczyć ścieżkę narzędzia zdefiniowaną z domyślnymi opcjami.

Następnie możesz sprawdzić swoje głębokości/zejścia i wysokości, jak z innymi poleceniami ścieżki.

Ostatnim krokiem jest aktywacja sekcji **Operacja**, w której można określić następujące parametry:

-    **Kontroler narzędzia**: Wybierz narzędzie do użycia.

-    **Tryb chłodzenia**: Wybierz {{Value|Żaden}}, {{Value|Zalewanie}} lub {{Value|Mgiełka}}.

-    **Directions**: Wybierz {{Value|CW}} (zgodnie z ruchem wskazówek zegara) lub {{Value|CCW}} (przeciwnie do ruchu wskazówek zegara).

-    **W**: Wymiar krawędzi.

-    **h**: Przesunięcie od dolnej części narzędzia. To funkcja bezpieczeństwa, ponieważ jeśli końcówka narzędzia znajdzie się powyżej krawędzi, nie będzie już cięła.

:   <img alt="Interfejs usuwania zadziorów z opcjami" src=images/Path_Deburr_Operations-tab.png  style="width:300px;">



## Właściwości



### Dane


{{TitleProperty|Podstawa}}

-    **Placement**:

-    **Label**: Dostosowywalna nazwa obiektu (UTF-8)


{{TitleProperty|Usuwanie zadziorów}}

-    **Direction**: {{Value|CCW}} lub {{Value|CW}}.

-    **Entry Point**: Punkt wejścia operacji; jeśli ustawiony na 2, będzie przechodzić w 2 narożnikach od domyślnego.

-    **Extra depth**: Dodatkowa głębokość (**h** w panelu zadań).

-    **Join||Hidden**: Sposób łączenia segmentów fazy, {{Value|Round}} lub {{Value|Miter}}.

-    **Side||Hidden**: Strona operacji, {{Value|Outside}} lub {{Value|Inside}}.

-    **Width**: Szerokość fazy (**W** w panelu zadań).


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do przejścia ponad zaciskami i przeszkodami (domyślnie ustawione na `OpStockZMax + SetupSheet.ClearanceHeightOffset`).

-    **Safe Height**: Wysokość, powyżej której dozwolone są szybkie ruchy (ustawione na `OpStockZMax + SetupSheet.SafeHeightOffset`).

-    **Start Depth**: Początkowa głębokość narzędzia, pierwsza głębokość cięcia w osi Z.

-    **Step Down**: Krok narzędzia w dół.


{{TitleProperty|Wartości operacyjne}}

-    **Op Stock ZMax**: Maksymalna wartość Z materiału.

-    **Op Stock ZMin**: Minimalna wartość Z materiału.

-    **Op Tool Diameter**: Średnica narzędzia.


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na {{False/pl}}, aby zapobiec generowaniu kodu przez operację.

-    **Base**: Geometria bazowa dla tej operacji, krawędzie lub powierzchnia.

-    **Comment**: Opcjonalny komentarz do tej operacji.

-    **Coolant Mode**: Tryb chłodzenia dla tej operacji.

-    **Cycle Time**: Szacunkowy czas cyklu dla tej operacji.

-    **Tool Controller**: Kontroler narzędzia, który będzie używany do obliczenia ścieżki.

-    **User Label**: Etykieta przypisana przez użytkownika.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Deburr/pl
