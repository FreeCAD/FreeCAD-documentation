---
 GuiCommand:
   Name: Draft Snap Ortho
   Name/pl: Rysunek Roboczy: Przyciągnij ortogonalnie
   MenuLocation: Przyciąganie , Przyciągnij ortogonalnie
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   SeeAlso: Draft_Snap/pl, Draft_Snap_Lock/pl
---

# Draft Snap Ortho/pl



## Opis

Polecenie <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:24px;"> **Przyciągnij ortogonalnie** przyciąga do umownych linii, które przecinają poprzedni punkt pod kątem wielokrotności 45°. Linie i kąty odnoszą się do płaszczyzny XY układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).

![](images/Draft_Snap_Ortho_example.png ) 
*Przyciąganie drugiego punktu linii do umownej linii o kącie 45° względem osi X. Małe okręgi w kolorze magenta wskazują wszystkie możliwe kierunki.*



## Użycie

Ogólne informacje na temat przyciągania można znaleźć na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Upewnij się, że przyciąganie jest włączone. Zobacz <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md).
2.  Jeśli opcja **Przyciągnij ortogonalnie** nie jest aktywna, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk **<img src="images/Draft_Snap_Ortho.svg" width=16px> [Przyciągnij ortogonalnie](Draft_Snap_Ortho/pl.md)** na pasku narzędzi przyciągania
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Naciśnij przycisk **<img src="images/Draft_Snap_Ortho.svg" width=16px>** w [widżecie przyciągania](Draft_snap_widget/pl.md)
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Przyciąganie → <img src="images/Draft_Snap_Ortho.svg" width=16px> Przyciągnij ortogonalnie** z menu lub menu kontekstowego [widoku 3D](3D_view/pl.md).
3.  Wybierz polecenie środowiska Rysunek Roboczy lub BIM, aby utworzyć geometrię.
4.  Pamiętaj, że możesz również zmienić opcje przyciągania, gdy polecenie jest aktywne.
5.  Wybierz pierwszy punkt. Ta opcja przyciągania wymaga poprzedniego punktu.
6.  Jeśli przesuniesz kursor wokół poprzedniego punktu, zauważysz efekt \"magnetyczny\", gdy kursor znajdzie się na umownej nieskończonej linii przecinającej ten punkt pod kątem 0°, 45°, 90° lub 135°.
7.  Punkt zostanie zaznaczony, a ikona <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:16px;"> zostanie wyświetlona w pobliżu kursora.
8.  Kliknij, aby potwierdzić punkt.



## Ustawienia

Zobacz stronę [Przyciąganie](Draft_Snap/pl#Ustawienia.md) aby uzyskać więcej informacji.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Ortho/pl
