---
 GuiCommand:
   Name: Draft Edit
   Name/pl: Rysunek Roboczy: Edytuj
   MenuLocation: Modyfikacja , Edytuj
   Workbenches: Draft_Workbench/pl
   Shortcut: **D** **E**
   SeeAlso: Std_Edit/pl
---

# Draft Edit/pl



## Opis

Polecenie <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> **Edycja** przełącza wybrane obiekty w tryb Edycji. W tym trybie właściwości obiektów mogą być edytowane graficznie. Zazwyczaj mogą być przesuwane węzły, a w niektórych przypadkach można wybrać opcje menu kontekstowego. Polecenie może obsługiwać większość obiektów środowiska Rysunek Roboczy, ale także niektóre inne obiekty. Zobacz sekcję [Obsługiwane obiekty](#Obsługiwane_obiekty.md). Obsługiwane obiekty szkicu można również umieścić w trybie edycji za pomocą polecenia [Std: Edycja](Std_Edit/pl.md).

![](images/Draft_Edit_example.png ) 
*Cztery obiekty w trybie edycji środowiska Rysunek Roboczy: polilinia ''(czerwony)'', łuk ''(czarny)'', krzywa złożona ''(zielony)'' i krzywa Bézier'a ''(magenta)''.*



## Użycie

Zobacz także strony: [Rysunek Roboczy: Przyciąganie](Draft_Snap/pl.md) i [Rysunek Roboczy: Wiązania](Draft_Constrain/pl.md).

1.  Opcjonalnie wybierz jeden lub więcej obiektów. Należy pamiętać, że chociaż wiele obiektów może znajdować się w trybie edycji wersji roboczej, obiekty mogą być edytowane tylko pojedynczo.
2.  Polecenie można wywołać na kilka sposobów:
    -   Jeśli obiekt nie został jeszcze wybrany: kliknij dwukrotnie obiekt w oknie [widoku drzewa](Tree_view/pl.md). Działa to tylko w przypadku obsługiwanych obiektów Draft.
    -   Naciśnij przycisk z menu **<img src="images/Draft_Edit.svg" width=16px> [Edytuj](Draft_Edit/pl.md)**.
    -   Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Edit.svg" width=16px> Edytuj**.
    -   Użyj skrótu klawiaturowego: **D**, a następnie **E**.
    -   Dla pojedynczego obiektu: wybierz opcję **Edytuj** z menu podręcznego [widoku drzewa](Tree_view/pl.md). Działa to tylko dla obsługiwanych obiektów środowiska Rysunek Roboczy. {{Version/pl|0.21}}
3.  Jeśli obiekt nie został jeszcze wybrany: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Wybrane obiekty zostaną oznaczone tymczasowymi węzłami i otworzy się [Główny panel zadań](#Główny_panel_zadań.md). Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
5.  Opcjonalnie można użyć menu podręcznego węzła lub krawędzi. Te menu podręczne są dostępne tylko dla niektórych obiektów Draft. Więcej informacji znajduje się w sekcji [obsługiwane obiekty](#obsługiwane_obiekty.md).
    -   Wykonaj jedną z następujących czynności:
        -   Dotyczy wszystkich systemów operacyjnych: przytrzymaj **E** i kliknij węzeł lub krawędź. Aby użyć klawisza **E** może być konieczne jednokrotne kliknięcie w obszarze okna [widoku 3D](3D_view.md), aby upewnić się, że jest ono aktywne.
        -   W systemie Windows: przytrzymaj **Alt** i kliknij węzeł lub krawędź.
        -   W systemie Linux: przytrzymaj **Shift**+**Alt**, **Ctrl**+**Alt** lub **Alt** i kliknij węzeł lub krawędź.
        -   Na macOS: przytrzymaj **Option** i kliknij węzeł lub krawędź.
    -   Wybierz opcję z menu kontekstowego.
    -   Jeśli wybrana opcja wymaga wprowadzenia punktu:
        -   Otworzy się panel zadań [edycji węzła](#Panel_zadań_edycji_węzła.md). Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
        -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
6.  Opcjonalnie przenieś węzeł:
    -   Kliknij węzeł w oknie [widoku 3D](3D_view/pl.md).
    -   Otworzy się panel zadań [edycji węzła](#Panel_zadań_edycji_węzła.md). Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
    -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
    -   Wynik zależy od obiektu i wybranego węzła.
7.  Naciśnij **Esc** lub przycisk **Zamknij** (przycisk na górze panelu zadań, bez obrazka), aby zakończyć polecenie.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.



### Pierwszy panel zadań 

-   Naciśnij przycisk **Esc** lub przycisk **Zamknij** aby zakończyć wykonywanie polecenia.



### Panel zadań edycji węzła 

-   Aby ręcznie wprowadzić współrzędne, wprowadź element X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie kursora poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Aby użyć współrzędnych biegunowych, wprowadź wartość dla **Długości** i wartość dla **Kąta**, a następnie naciśnij **Enter** po każdej z nich.
-   Zaznacz pole wyboru **Kąt**, aby ograniczyć kursor do określonego kąta.
-   Naciśnij **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne wybranego punktu są względne do oryginalnego punktu, w przeciwnym razie są one odnoszone do początku układu współrzędnych. {{Version/pl|1.0}}
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).



## Obsługiwane obiekty 



### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Linia](Draft_Line/pl.md) oraz <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Polilinia](Draft_Wire/pl.md) 

-   Jeśli węzeł początkowy lub końcowy otwartej linii zostanie przesunięty tak, aby zbiegł się, linia zostanie zamknięta.
-   Menu kontekstowe węzła: {{Value|Usuń punkt}}. Muszą pozostać co najmniej dwa punkty.
-   Menu kontekstowe krawędzi: {{Value|Dodaj punkt}}, {{Value|Otwórz polilinię}}/{{Value|Zamknij polilinię}} *({{Version/pl|0.21}})* i {{Value|Odwróć polilinię}}.



### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Łuk](Draft_Arc/pl.md) oraz <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Łuk przez trzy punkty](Draft_Arc_3Points/pl.md) 

-   Menu kontekstowe węzła środkowego: {{Value|Przesuń łuk}}.
-   Menu kontekstowe węzła początkowego: {{Value|Ustaw pierwszy kąt}}.
-   Menu kontekstowe węzła końcowego: {{Value|Ustaw ostatni kąt}}.
-   Menu kontekstowe węzła pośredniego: {{Value|Ustaw promień}}.
-   Menu kontekstowe krawędzi: {{Value|Odwróć łuk}}.



### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Okrąg](Draft_Circle/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Elipsa](Draft_Ellipse/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Prostokąt](Draft_Rectangle/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Wielokąt](Draft_Polygon/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Krzywa złożona](Draft_BSpline/pl.md) 

-   Jeśli węzeł początkowy lub końcowy otwartej krzywej zostanie przesunięty tak, aby się pokrywały, krzywizna zostanie zamknięta.
-   Menu kontekstowe węzła: {{Value|Usuń punkt}}. W przypadku otwartej krzywej muszą pozostać co najmniej dwa punkty. W przypadku zamkniętej minimalna liczba punktów wynosi trzy.
-   Menu kontekstowe krawędzi: {{Value|Dodaj punkt}}, {{Value|Otwórz polilinię}}/{{Value|Zamknij polilinię}} *({{Version/pl|0.21}})* i {{Value|Odwróć krzywą złożoną}} *({{Version/pl|0.21}})*.



### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Sześcienna krzywa Béziera](Draft_CubicBezCurve/pl.md) oraz <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Krzywa Bézier\'a](Draft_BezCurve/pl.md) 

-   Jeśli węzeł początkowy lub końcowy otwartej krzywej zostanie przesunięty tak, aby się pokrywały, krzywa zostanie zamknięta.
-   Menu kontekstowe węzła: {{Value|Usuń punkt}}, {{Value|Ustaw ostro}}, {{Value|Ustaw stycznie}} i {{Value|Ustaw symetrycznie}}.
-   Menu kontekstowe krawędzi: {{Value|Dodaj punkt}}, {{Value|Otwórz polilinię}}/{{Value|Zamknij polilinię}} *({{Version/pl|0.21}})* i {{Value|Odwróć krzywą}} *({{Version/pl|0.21}})*.



### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Wymiar](Draft_Dimension/pl.md) 

-   Nie można edytować wymiarów kątowych.
-   Nie można przenosić węzłów początkowych i końcowych wymiarów parametrycznych.
-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Architektura: ściana](Arch_Wall/pl.md) 

-   Pojedynczy węzeł kontrolujący wysokość ściany jest wyświetlany nad **Umiejscowieniem** ściany.
-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Arch_Structure.svg  style="width:24px;"> [Architektura: Konstrukcja](Arch_Structure/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Architektura: Okno](Arch_Window/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Arch_Space.svg  style="width:24px;"> [Architektura: Przestrzeń](Arch_Space/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Arch_Panel_Cut.svg  style="width:24px;"> [Architektura: Panelizacja do cięcia](Arch_Space/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:24px;"> [Architektura: Arkusz panela](Arch_Panel_Sheet/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Część: Sześcian](Part_Box/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Część: Walec](Part_Cylinder/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Część: Sfera](Part_Sphere/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Część: Stożek](Part_Cone/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Część: Linia](Part_Line/pl.md) 

-   Brak menu kontekstowego dla tego obiektu.



### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Szkicownik: Szkic](Sketcher_NewSketch/pl.md) 

-   Można edytować tylko szkice zawierające pojedynczą, nieograniczoną linię.
-   Brak menu kontekstowego dla tego obiektu.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   Kolor tymczasowych węzłów jest taki sam jak kolor symboli przyciągania. Kolor ten można zmienić w preferencjach: **Edycja → Preferencje ... → Rysunek Roboczy → Siatka i przyciąganie → Kolor domyślny dla symboli przyciągania**. Należy pamiętać, że ten kolor nie jest używany dla tymczasowych węzłów wyświetlanych dla [Krzywa Bézier\'a](Draft_BezCurve/pl.md). Te węzły używają zamiast tego właściwości **Kolor linii** dla krzywej.
-   Rozmiar węzłów zależy od opcji: **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Rozmiar znacznika**. {{Version/pl|1.0}}



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Nie ma metody Python do **Edycji** obiektów środowiska Rysunek Roboczy. Aby naśladować wyniki polecenia, należy zmodyfikować właściwości geometryczne obiektów.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/pl
