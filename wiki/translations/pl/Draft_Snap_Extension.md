---
 GuiCommand:
   Name: Draft Snap Extension
   Name/pl: Rysunek Roboczy: Przyciągnij na wydłużeniu
   MenuLocation: Przyciąganie , Przyciągnij na wydłużeniu
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   SeeAlso: Draft_Snap/pl, Draft_Snap_Lock/pl
---

# Draft Snap Extension/pl



## Opis

Polecenie <img alt="" src=images/Draft_Snap_Extension.svg  style="width:24px;"> **Przyciągnij na wydłużeniu** przyciąga do umownej linii, która rozciąga się poza punkty końcowe prostych krawędzi. Krawędzie mogą należeć do obiektów środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) lub [BIM](BIM_Workbench/pl.md), ale także do obiektów utworzonych za pomocą innych [środowisk pracy](Workbenches/pl.md).

Za pomocą tej opcji przyciągania i [przyciągania równoległego](Draft_Snap_Parallel/pl.md) można odwołać się do maksymalnie 8 krawędzi, umożliwiając przyciąganie do wirtualnych przecięć. Obie opcje przyciągania mogą być również łączone z innymi opcjami przyciągania.

![](images/Draft_Snap_Extension_example.png ) 
*Przyciąganie drugiego punktu linii do przedłużenia krawędzi.*



## Użycie

Ogólne informacje na temat przyciągania można znaleźć na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Upewnij się, że przyciąganie jest włączone. Zobacz stronę <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md).
2.  Jeśli opcja **Przyciągnij prostopadle** nie jest aktywna, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk **<img src="images/Draft_Snap_Extension.svg" width=16px> [Przyciągnij na wydłużeniu](Draft_Snap_Extension/pl.md)** na pasku narzędzi przyciągania.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Naciśnij i przytrzymaj przycisk **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** na pasku narzędzi [Widżet przyciągania](Draft_snap_widget/pl.md) i w otwartym menu wybierz opcję **<img src="images/Draft_Snap_Extension.svg" width=16px> Przyciągnij na wydłużeniu**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Przyciąganie → <img src="images/Draft_Snap_Extension.svg" width=16px> Przyciągnij na wydłużeniu** z menu lub z menu kontekstowego [widoku 3D](3D_view/pl.md).
3.  Wybierz polecenie środowiska Rysunek Roboczy lub BIM, aby utworzyć geometrię.
4.  Pamiętaj, że możesz również zmienić opcje przyciągania, gdy polecenie jest aktywne.
5.  Przesuń kursor nad prostą krawędź.
6.  Krawędź zostanie podświetlona.
7.  Jeśli teraz przesuniesz kursor poza punkty końcowe krawędzi, zobaczysz przerywaną linię, gdy kursor znajdzie się na przedłużonej krawędzi.
8.  Punkt zostanie zaznaczony, a ikona <img alt="" src=images/Draft_Snap_Extension.svg  style="width:16px;"> zostanie wyświetlona w pobliżu kursora.
9.  Kliknij, aby potwierdzić punkt.



## Ustawienia

Zobacz stronę [Przyciąganie](Draft_Snap/pl#Ustawienia.md) aby uzyskać więcej informacji.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Extension/pl
