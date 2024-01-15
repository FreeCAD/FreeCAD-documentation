---
 GuiCommand:
   Name: Draft Snap Perpendicular
   Name/pl: Rysunek Roboczy: Przyciągnij prostopadle
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   SeeAlso: Draft_Snap/pl, Draft_Snap_Lock/pl
---

# Draft Snap Perpendicular/pl



## Opis

Polecenie <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:24px;"> **Przyciągnij prostopadle** przyciąga prostopadłe rzuty poprzedniego punktu na powierzchnie *({{Version/pl|0.21}})* i krawędzie. Ściany i krawędzie mogą należeć do obiektów środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md), ale także do obiektów utworzonych za pomocą innych [środowisk pracy](Workbenches/pl.md).

Ta opcja przyciągania znajdzie również punkty na przedłużeniach powierzchni i krawędzi.

![](images/Draft_Snap_Perpendicular_example.png ) 
*Przyciąganie drugiego punktu linii do prostopadłego punktu na przedłużonej krawędzi*



## Użycie

Ogólne informacje na temat przyciągania można znaleźć na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Upewnij się, że przyciąganie jest włączone. Zobacz stronę <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md).
2.  Jeśli opcja **Przyciągnij prostopadle** nie jest aktywna, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk **<img src="images/Draft_Snap_Perpendicular.svg" width=16px>** na pasku narzędzi przyciągania.
    -   Naciśnij i przytrzymaj przycisk **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** na pasku narzędzi [Widżet przyciągania](Draft_snap_widget/pl.md) i w otwartym menu wybierz opcję **<img src="images/Draft_Snap_Perpendicular.svg" width=16px> Przyciągnij prostopadle
        **.
3.  Wybierz polecenia środowiska [Rysunku Roboczego](Draft_Workbench/pl.md) lub [Architektury](Arch_Workbench/pl.md), aby utworzyć geometrię.
4.  Pamiętaj, że możesz również zmienić opcje przyciągania, gdy polecenie jest aktywne.
5.  Wybierz pierwszy punkt. Ta opcja przyciągania wymaga poprzedniego punktu. Punkt prostopadły zostanie wyznaczony w odniesieniu do tego punktu.
6.  Przesuń kursor nad powierzchnię lub krawędź.
7.  Ściana lub krawędź zostanie podświetlona.
8.  Jeśli zostanie znaleziony punkt prostopadły, zostanie on zaznaczony, a ikona <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:16px;"> zostanie wyświetlona w pobliżu kursora.
9.  Jeśli istnieje wiele punktów prostopadłości: opcjonalnie przesuń kursor bliżej innego punktu prostopadłości. {{Version/pl|0.21}}
10. Kliknij, aby potwierdzić punkt.



## Ustawienia

Zobacz stronę [Przyciąganie](Draft_Snap/pl#Ustawienia.md) aby uzyskać więcej informacji.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Perpendicular/pl
