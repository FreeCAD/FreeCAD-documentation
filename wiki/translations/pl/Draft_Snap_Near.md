---
 GuiCommand:
   Name: Draft Snap Near
   Name/pl: Rysunek Roboczy: Przyciągnij do najbliższego
   MenuLocation: Przyciąganie , Przyciągnij do najbliższego
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   SeeAlso: Draft_Snap/pl, Draft_Snap_Lock/pl
---

# Draft Snap Near/pl



## Opis

Polecenie <img alt="" src=images/Draft_Snap_Near.svg  style="width:24px;"> **Przyciągnij do najbliższego** powoduje przyciąganie do najbliższego punktu na powierzchniach oraz krawędziach. Ściany i krawędzie mogą należeć do obiektów środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [BIM](BIM_Workbench/pl.md), ale także do obiektów stworzonych w innych [środowiskach pracy](Workbenches/pl.md).

![](images/Draft_Snap_Near_example.png ) 
*Przyciąganie drugiego punktu prostej do najbliższego punktu na krawędzi.*



## Użycie

Ogólne informacje na temat przyciągania można znaleźć na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Upewnij się, że przyciąganie jest włączone. Zobacz <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md).
2.  Jeśli opcja **Przyciągnij do najbliższego** nie jest aktywna, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk **<img src="images/Draft_Snap_Near.svg" width=16px> [Przyciągnij do najbliższego](Draft_Snap_Near/pl.md)** na pasku narzędzi.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Przytrzymaj wciśnięty przycisk **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=16px>** w [widżecie przyciągania](Draft_snap_widget/pl.md) i w menu wybierz opcję **<img src="images/Draft_Snap_Near.svg" width=16px> Przyciąganie do najbliższego**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Przyciąganie → <img src="images/Draft_Snap_Near.svg" width=16px> Przyciągnij do najbliższego** z menu lub z menu kontekstowego [widoku 3D](3D_view/pl.md).
3.  Wybierz polecenie środowiska Rysunek Roboczy lub BIM, aby utworzyć geometrię.
4.  Uwaga: opcje przyciągania można zmieniać także wtedy, gdy polecenie jest aktywne.
5.  Przesuń kursor na ścianę lub krawędź.
6.  Ściana lub krawędź zostanie podświetlona.
7.  Jeśli zostanie znaleziony najbliższy punkt, zostanie on zaznaczony.
8.  Opcjonalnie przesuń kursor wzdłuż powierzchni lub krawędzi, aby wybrać inny najbliższy punkt.
9.  Kliknij, aby potwierdzić punkt.



## Uwagi

-   Nie jest dobrym pomysłem, aby opcja [Przyciągnij do najbliższego](Draft_Snap_Near/pl.md) była stale aktywna, ponieważ ma ona pierwszeństwo przed wieloma innymi opcjami przyciągania.



## Ustawienia

Zobacz stronę [Przyciąganie](Draft_Snap/pl#Ustawienia.md) aby uzyskać więcej informacji.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/pl
