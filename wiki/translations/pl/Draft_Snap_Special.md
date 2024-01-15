---
 GuiCommand:
   Name: Draft Snap Near
   Name/pl: Rysunek Roboczy: Przyciągnij specjalnie
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.17
   SeeAlso: Draft_Snap/pl, Draft_Snap_Lock/pl
---

# Draft Snap Special/pl



## Opis

Polecenie <img alt="" src=images/Draft_Snap_Special.svg  style="width:24px;"> **Draft Snap Special** przyciąga do [punktów specjalnych](#Obsługiwane_punkty_specjalne.md) zdefiniowanych przez obiekt. Obsługiwane obiekty to [Architektura: Ściana](Arch_Wall/pl.md), [Architektura: Konstrukcja](Arch_Structure/pl.md) i [Architektura: Wyposażenie](Arch_Equipment/pl.md).

![](images/Draft_Snap_Special_example.png ) 
*Przyciąganie drugiego punktu linii do specjalnego punktu ściany, który jest wierzchołkiem obiektu bazowego.*



## Użycie

Ogólne informacje na temat przyciągania można znaleźć na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Upewnij się, że przyciąganie jest włączone. Zobacz stronę <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md).
2.  Jeśli opcja **Przyciągnij specjalnie** nie jest aktywna, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk **<img src="images/Draft_Snap_Special.svg" width=16px>** na pasku narzędzi przyciągania.
    -   Przytrzymaj przycisk **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** na pasku narzędzi [Widżet przyciągania](Draft_snap_widget/pl.md) i w otwartym menu wybierz opcję **<img src="images/Draft_Snap_Special.svg" width=16px> Przyciągnij specjalnie**.
3.  Wybierz polecenia środowiska [Rysunku Roboczego](Draft_Workbench/pl.md) lub [Architektury](Arch_Workbench/pl.md), aby utworzyć geometrię.
4.  Uwaga: opcje przyciągania można również zmieniać, gdy polecenie jest aktywne.
5.  Przesuń kursor nad obsługiwany obiekt.
6.  Obiekt zostanie podświetlony.
7.  Jeśli znaleziony zostanie punkt specjalny, zostanie on zaznaczony, a w pobliżu kursora wyświetlona zostanie ikona <img alt="" src=images/Draft_Snap_Special.svg  style="width:16px;">.
8.  Jeśli obiekt ma wiele punktów specjalnych: opcjonalnie przesuń kursor bliżej innego punktu specjalnego.
9.  Kliknij, aby potwierdzić punkt.



## Obsługiwane punkty specjalne 

-   Wierzchołki obiektu **Bazy** <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Architektura: Ściana](Arch_Wall/pl.md).

-   Punkt **Umiejscowienia** obiektu <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Architektura: Konstrukcja](Arch_Structure/pl.md).

-    **Punkt przyciągania**<img alt="" src=images/Arch_Equipment.svg  style="width:16px;"> [Architektura: Wyposażenie](Arch_Equipment/pl.md).



## Ustawienia

Zobacz stronę [Przyciąganie](Draft_Snap/pl#Ustawienia.md) aby uzyskać więcej informacji.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Special/pl
