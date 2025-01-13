---
 GuiCommand:
   Name: Draft Stretch
   Name/pl: Rysunek Roboczy: Rozciągnij
   MenuLocation: Modyfikacja , Rozciągnij
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: **S** **H**
   Version: 0.17
---

# Draft Stretch/pl



## Opis

Polecenie <img alt="" src=images/Draft_Stretch.svg  style="width:24px;"> **Rozciągnij** rozciąga obiekty, przesuwając wybrane punkty.

<img alt="" src=images/Draft_Stretch_Example.jpg  style="width:400px;"> 
*Rozciąganie trzech linii.*



## Użycie

Zobacz także strony: [Rysunek Roboczy: Przyciąganie](Draft_Snap/pl.md) i [Rysunek Roboczy: Wiązania](Draft_Constrain/pl.md).

1.  Opcjonalnie wybierz jeden lub więcej obiektów. Obiekty muszą być [liniami](Draft_Line/pl.md), [poliliniami](Draft_Wire/pl.md), [prostokątami](Draft_Rectangle/pl.md), [krzywymi złożonymi](Draft_BSpline/pl.md) lub [krzywymi Béziera](Draft_BezCurve/pl.md). Inne obiekty są ignorowane.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Stretch.svg" width=16px> '''Rozciągnij'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz opcję z menu **Modyfikacja → <img src="images/Draft_Stretch.svg" width=16px> Rozciągnij**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Modyfikacja → <img src="images/Draft_Stretch.svg" width=16px> Rozciągnij** z menu.
    -   Użyj skrótu klawiaturowego: **S**, a następnie **H**.
3.  Jeśli obiekt nie został jeszcze wybrany: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Otworzy się panel zadań **Rozciągnij**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
5.  Wybierz pierwszy punkt, jeden z rogów prostokątnego obszaru zaznaczenia, w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
6.  Wybierz drugi punkt, przeciwległy narożnik obszaru zaznaczenia, w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
7.  Punkty wybranych obiektów, które znajdują się wewnątrz obszaru zaznaczenia, zostaną zaznaczone.
8.  Wybierz trzeci punkt, punkt bazowy, w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.
9.  Wybierz czwarty punkt, punkt docelowy, w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, wprowadź składowe X, Y i Z i naciśnij **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view.md) przed wprowadzeniem współrzędnych.
-   Wciśnij **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne drugiego punktu przesunięcia są względne do pierwszego punktu, w przeciwnym razie są one względne do początku układu współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby przerwać polecenie.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Nie ma metody Python do rozciągania obiektów. Aby naśladować wyniki polecenia **Rozciągnij**, należy zmodyfikować właściwości geometryczne obiektów.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Stretch/pl
