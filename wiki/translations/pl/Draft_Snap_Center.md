---
 GuiCommand:
   Name: Draft Snap Center
   Name/pl: Rysunek Roboczy: Przyciągnij do środka
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   SeeAlso: Draft_Snap/pl, Draft_Snap_Lock/pl
---

# Draft Snap Center/pl



## Opis

Polecenie <img alt="" src=images/Draft_Snap_Center.svg  style="width:24px;"> **Draft Snap Center** przyciąga do punktu środkowego ścian i okrągłych krawędzi oraz do punktu **Umiejscowienia** obiektów [Pośrednia płaszczyzna robocza](Draft_WorkingPlaneProxy/pl.md) i [Architektura: Część budowl](Arch_BuildingPart/pl.md). Powierzchnie i krawędzie mogą należeć do obiektów środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md), ale także do obiektów utworzonych za pomocą innych [środowisk pracy](Workbenches/pl.md).

![](images/Draft_Snap_Center_example_arc.png ) 
*Przyciąganie drugiego punktu linii do środka okrągłej krawędzi.*

![](images/Draft_Snap_Center_example_buildingpart.png ) 
*Przyciąganie drugiego punktu linii do punktu umiejscowienia łuku części budowli.*



## Użycie

Ogólne informacje na temat przyciągania można znaleźć na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Upewnij się, że przyciąganie jest włączone. Więcej informacji na ten temat znajduje się na stronie <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md).
2.  Jeśli *\'przyciągane do środka* nie jest aktywne, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk **<img src="images/Draft_Snap_Center.svg" width=16px>** na pasku narzędzi przyciągania.
    -   Przytrzymaj przycisk **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** na pasku [widżetu przyciągania](Draft_snap_widget/pl.md) i w otwartym menu wybierz opcję **<img src="images/Draft_Snap_Center.svg" width=16px> Przyciągnij do środka**.
3.  Wybierz polecenie środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md), aby utworzyć geometrię.
4.  Pamiętaj, że możesz również zmienić opcje przyciągania, gdy polecenie jest aktywne.
5.  Wykonaj jedną z poniższych czynności:
    -   Aby wybrać punkt środkowy ściany lub okrągłej krawędzi:
        -   Przesuń kursor nad powierzchnię lub krawędź.
        -   Ściana lub krawędź zostanie podświetlona.
    -   Aby wybrać punkt **Umiejscowienia** [pośredniej płaszczyzny roboczej](Draft_WorkingPlaneProxy/pl.md):
        -   Przesuń kursor nad dowolny element proxy płaszczyzny roboczej.
        -   Płaszczyzna robocza proxy nie jest podświetlona.
    -   Aby wybrać punkt **Umiejscowienia** [Architektura: Część budowli](Arch_BuildingPart/pl.md):
        -   Przesuń kursor nad jedną z krawędzi małego symbolu osi części budynku lub nad tekstem obok, który wyświetla **etykietę** części budynku i jej poziom.
        -   Podświetlane są tylko krawędzie symbolu osi. Tekst nie jest podświetlony.
6.  Jeśli punkt zostanie znaleziony, zostanie on zaznaczony, a ikona <img alt="" src=images/Draft_Snap_Center.svg  style="width:16px;"> zostanie wyświetlona w pobliżu kursora.
7.  Kliknij, aby potwierdzić punkt.



## Ustawienia

Zobacz stronę [Przyciąganie](Draft_Snap/pl#Ustawienia.md) aby uzyskać więcej informacji.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Center/pl
