---
 GuiCommand:
   Name: Draft Dimension
   Name/pl: Draft: Wymiar
   MenuLocation: Adnotacja , Wymiar
   Workbenches: Draft_Workbench/pl
   Shortcut: **D** **I**
   Version: 0.8
   SeeAlso: Draft_FlipDimension/pl
---

# Draft Dimension/pl



## Opis

Polecenie <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> **Draft Dimension** [tworzy](#Tworzenie.md) [Wymiar liniowy](#Zastosowanie_wymiaru_liniowego.md), [Wymiar promieniowy](#Zastosowanie_wymiaru_promieniowego.md) lub [Wymiar kątowy](#Zastosowanie_wymiaru_kątowego.md).

Wymiary liniowe oparte na krawędziach i wymiary promieniowe są parametryczne. Oznacza to, że będą one aktualizowane, jeśli zmierzona krawędź zostanie zmodyfikowana. Zmierzone krawędzie mogą należeć do obiektów środowiska Rysunek Roboczy, ale także do brył. Wymiary kątowe nie są parametryczne.

Wymiary środowiska pracy Rysunek Techniczny mogą być wyświetlane na stronie [Rysunku Technicznego](TechDraw_Workbench/pl.md) za pomocą poleceń [Wstaw widok rysunku](TechDraw_DraftView/pl.md) lub [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md). środowisko [Rysunek Techniczny](TechDraw_Workbench/pl.md) oferuje swoje własne narzędzia wymiarowania. Tworzą one jednak wymiary, które są wyświetlane tylko na stronie rysunku, a nie w oknie [widoku 3D](3D_view/pl.md).

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;"> 
*Wymiar określony przez trzy punkty*



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).



### Wymiar liniowy 

1.  Opcjonalnie wybierz prostą krawędź w oknie [widoku 3D](3D_view/pl.md).
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Dimension.svg" width=16px> '''Wymiar'''**.
    -   Wybierz z menu opcję **Opisy → <img src="images/Draft_Dimension.svg" width=16px> Wymiar**.
    -   Użyj skrótu klawiaturowego: **D**, a następnie **I**.
3.  Otworzy się panel zadań **Wymiar**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
4.  Jeśli krawędź nie została jeszcze wybrana, wykonaj jedną z poniższych czynności:
    -   Naciśnij **E** lub przycisk **<img src="images/view-select.svg" width=16px> Wybierz krawędź** i wybierz prostą krawędź w [3D view](3D_view/pl.md).
    -   Przytrzymaj klawisz **Alt**, wybierz prostą krawędź w oknie [widoku 3Di](3D_view/pl.md) zwolnij klawisz **Alt**.
    -   Zdefiniuj zmierzoną odległość, wybierając punkty:
        -   Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
        -   Wybierz drugi punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.
5.  Aby ustawić linię wymiarową, wykonaj jedną z poniższych czynności:
    -   Dla wymiaru wyrównanego:
        -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
    -   Dla wymiaru poziomego:
        -   Przesuń wskaźnik powyżej lub poniżej krawędzi lub punktów.
        -   Przytrzymaj klawisz **Shift**, przesuń wskaźnik i wybierz punkt w oknie [widoku 3D](3D_view/pl.md).
    -   Dla wymiaru pionowego:
        -   Przesuń wskaźnik w lewo lub w prawo od krawędzi lub punktów.
        -   Przytrzymaj klawisz **Shift**, przesuń wskaźnik i wybierz punkt w oknie [widoku 3D](3D_view/pl.md).



### Wymiaru promieniowy 

1.  Opcjonalnie wybierz okrągłą krawędź w oknie [widoku 3D](3D_view/pl.md).
2.  Wywołaj polecenie jak opisano wyżej.
3.  Otworzy się panel zadań **Wymiar**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
4.  Jeśli krawędź nie została jeszcze wybrana, wykonaj jedną z poniższych czynności:
    -   Naciśnij **E** lub przycisk **<img src="images/view-select.svg" width=16px> Wybierz krawędź** i wybierz okrągłą krawędź w oknie [widoku 3D](3D_view/pl.md).
    -   Przytrzymaj klawisz **Alt**, wybierz okrągłą krawędź w oknie [widoku 3D](3D_view/pl.md) i zwolnij klawisz **Alt**.
5.  Aby ustawić linię wymiarową, wykonaj jedną z poniższych czynności:
    -   Dla wymiaru średnicy:
        -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
    -   Dla wymiaru radialnego:
        -   Przytrzymaj klawisz **Shift** i wybierz punkt w oknie [widoku 3D](3D_view/pl.md).



### Wymiaru kątowy 

1.  Wywołaj polecenie jak opisano wyżej.
2.  Otworzy się panel zadań **Wymiar**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
3.  Wykonaj jedną z następujących czynności:
    -   Naciśnij **E** lub przycisk **<img src="images/view-select.svg" width=16px> Wybierz krawędź** i wybierz pierwszą prostą krawędź w oknie [widoku 3D](3D_view/pl.md). Powtórz tę czynność, aby wybrać drugą prostą krawędź.
    -   Przytrzymaj klawisz **Alt**, wybierz dwie proste krawędzie w oknie [widoku 3D](3D_view/pl.md) i zwolnij klawisz **Alt**.
4.  Aby ustawić łuk wymiarowy, wybierz punkt w oknie [widoku 3D](3D_view/pl.md).
5.  Wyświetlany kąt zależy od krawędzi i wybranego punktu.



### Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi *(w wersji 1.0)*.

-   Aby ręcznie wprowadzić współrzędne, wprowadź element X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Wciśnij **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne są względne do ostatniego punktu, jeśli jest dostępny, w przeciwnym razie są one względne do początku układu współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalne**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).
-   Naciśnij **N** lub kliknij pole wyboru **Kontynuuj**, aby włączyć tryb kontynuacji. Tryb ten działa tylko dla wymiarów liniowych. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po zakończeniu, umożliwiając dalsze tworzenie wymiarów. Wszystkie kolejne wymiary będą rozpoczynać się od ostatniego punktu poprzedniego wymiaru i będą używać tej samej linii bazowej co pierwszy wymiar. Należy pamiętać, że wybór krawędzi nie jest możliwy dla kolejnych wymiarów.
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby zakończyć polecenie.



## Uwagi

Liniowe i promieniowe wymiary środowiska Rysunek Roboczy można edytować za pomocą polecenia [Edytuj](Draft_Edit/pl.md).

-   Wymiary szkicu utworzone lub zapisane w [wersji FreeCAD 0.21](Release_notes_0.21/pl.md) nie są kompatybilne wstecz.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Wymiar środowiska pracy Rysunek Roboczy wywodzi się z obiektu [App: FeaturePython](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Poniższe właściwości są dodatkowe, chyba że zaznaczono inaczej.



### Dane w wymiarze liniowym i promieniowym 


{{TitleProperty|Wymiar}}

-    **Dimline|VectorDistance**: określa punkt, przez który przechodzi linia wymiaru.

-    **Połączona geometria|LinkSubList**: określa obiekt i jego elementy podrzędne, z którymi powiązany jest wymiar.

-    **Normalna|Vector**: określa normalną płaszczyzny tekstu.

-    **Podparcie|Link|hidden**: określa mierzony obiekt.


{{TitleProperty|Wymiar liniowy / promieniowy}}

-    **Kierunek|Vector**: określa kierunek pomiaru.

-    **Odległość|Length**: *(tylko do odczytu)* określa wartość pomiaru.

-    **Koniec|VectorDistance**: określa punkt końcowy pomiaru.

-    **Początek|VectorDistance**: określa punkt początkowy pomiaru.


{{TitleProperty|Wymiar promieniowy}}

-    **Średnica|Bool**: określa, czy wymiar promieniowy jest wyświetlany jako wymiar średnicy. Nie jest używane w przypadku wymiarów liniowych.



### Dane wymiaru kątowego 


{{TitleProperty|Wymiar kątowy}}

-    **Kąt|Angle**: (tylko do odczytu) określa wartość pomiaru.

-    **Środek|VectorDistance**: określa środek pomiaru.

-    **Kąt pierwszy|Angle**: określa kąt początkowy pomiaru.

-    **Kąt drugi|Angle**: określa kąt końcowy pomiaru.


{{TitleProperty|Wymiar}}

-    **Dimline|VectorDistance**: określa punkt, przez który przechodzi łuk wymiaru.

-    **Połączona geometria|LinkSubList|hidden**: nieużywane.

-    **Normalna|Vector|hidden**: określa normalną płaszczyzny wymiaru.

-    **Podparcie|Link|hidden**: nieużywane.



### Widok


{{TitleProperty|Adnotacja}}

-    **Styl adnotacji|Enumeration**: określa styl adnotacji zastosowany do wymiaru. Zobacz stronę [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md).

-    **Mnożnik skali|Float**: określa ogólny współczynnik skalowania zastosowany do tekstu.


{{TitleProperty|Opcje wyświetlania}}

-    **Tryb wyświetlania|Enumeration**: określa sposób wyświetlania tekstu. Jeśli wartością jest {{value|World}}, tekst będzie wyświetlany na płaszczyźnie zdefiniowanej przez **Normalną** pomiaru. Jeśli jest to {{value|Ekran}}, tekst będzie zawsze skierowany w stronę ekranu. To jest dziedziczona własność. Wspomniane opcje to opcje o zmienionych nazwach *({{Version/pl|0.21}})*.


{{TitleProperty|Grafika}}

-    **Rozmiar strzałki|Length**: określa rozmiar symbolu wyświetlanego na końcu krzywej.

-    **Typ strzałki|Enumeration**: określa typ symbolu wyświetlanego na końcu krzywej, którym może być {{value|Punkt}}, {{value|Okrąg}}, {{value|Strzałka}}, {{value|Grot}} lub {{value|Grot-2}}.

-    **Przekroczenie wymiaru|Distance**: określa dodatkową długość dodaną do linii wymiarowej. Nie używane dla wymiarów kątowych.

-    **Przedłużenie linii|Distance**: określa długość linii przedłużających, które biegną od linii wymiarowej do mierzonych punktów. Użyj {{Value|0}} dla pełnych linii przedłużających. Wartość ujemna określa odstęp między końcami linii przedłużających a punktami pomiarowymi. Wartość dodatnia określa maksymalną długość linii przedłużających. Używane tylko dla wymiarów liniowych.

-    **Przekroczenie przedłużenia|Distance**: określa dodatkową długość linii przedłużających poza linią wymiarową. Nieużywane w przypadku wymiarów kątowych.

-    **Odwróć strzałki|Bool**: określa, czy odwrócić orientację symboli na końcach linii wymiarowej lub łuku. Działa tylko wtedy, gdy symbole są strzałkami.

-    **Kolor linii|Color**: określa kolor linii wymiarowej lub łuku oraz strzałek.

-    **Szerokość linii|Float**: określa szerokość linii lub łuku należącego do wymiaru.

-    **Pokaż linię|Bool**: określa, czy wyświetlać linię wymiaru. Nie ma wpływu na wyświetlanie linii przedłużających i przekroczeń. Nieużywane w przypadku wymiarów kątowych.


{{TitleProperty|Tekst}}

-    **Odwróć tekst|Bool**: określa, czy odwrócić orientację tekstu.

-    **Nazwa czcionki|Font**: określa czcionkę używaną do rysowania tekstu. Może to być nazwa czcionki, taka jak {{value|Arial}}, domyślny styl, taki jak {{value|sans}}, {{value|serif}} lub {{value|mono}}, rodzina, taka jak {{value|Arial,Helvetica,sans}}, lub nazwa ze stylem, takim jak {{value|Arial:Bold}}. Jeśli podana czcionka nie zostanie znaleziona w systemie, zamiast niej zostanie użyta czcionka domyślna.

-    **Rozmiar czcionki|Length**: określa rozmiar liter. Tekst może być niewidoczny w oknie[widoku 3D](3D_view.md), jeśli ta wartość jest bardzo mała.

-    **Nadpisz|String**: określa niestandardowy tekst do wyświetlenia zamiast rzeczywistego pomiaru. Użyj ciągu {{value|$dim}} wewnątrz tekstu, aby dołączyć pomiar.

-    **Kolor tekstu|Color**: określa kolor tekstu. <small>(v0.21)</small> .

-    **Pozycja tekstu|VectorDistance**: określa położenie tekstu we współrzędnych bezwzględnych. {{Value|[0, 0, 0]}} wyświetli tekst w domyślnej pozycji w pobliżu linii wymiarowej lub łuku.

-    **Odstępy tekstu|Length**: określa odstęp między tekstem a linią wymiarową lub łukiem.


{{TitleProperty|Jednostki}}

-    **Miejsca dziesiętne|Integer**: określa liczbę miejsc dziesiętnych wyświetlanych dla pomiaru.

-    **Pokaż jednostki|Bool**: określa, czy jednostka ma być wyświetlana obok wartości liczbowej pomiaru. Nie używane dla wymiarów kątowych.

-    **Nadpisanie jednostki|String**: określa jednostkę, w której ma być wyrażony pomiar, na przykład {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} lub {{value|arch}} dla jednostek łukowych. Pozostaw to pole puste, aby użyć jednostki domyślnej. Nie używane dla wymiarów kątowych.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć **Wymiar** środowiska Rysunek Roboczy użyj metody `make_dimension` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeDimension`.


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

Istnieją różne sposoby wywołania tej metody, w zależności od przekazanych do niej argumentów:


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```

-   Tworzy `wymiar` liniowy, mierząc odległość między punktami `p1` i `p2`.
-   Tworzy liniowy `wymiar` powiązany z `obiektem`, mierząc odległość między jego wierzchołkami indeksowanymi `i1` i `i2`.
-   Tworzy `wymiar` kołowy powiązany z `obiektem`, z `i1` będącym indeksem zakrzywionej krawędzi do zmierzenia i `trybem` będącym `"promieniem"` lub `"średnicą"` określającym typ wymiaru.
    -   
        `p3`
        
        w pierwszym wywołaniu i `p4` w pozostałych dwóch, określają opcjonalny punkt, przez który powinna przechodzić linia wymiarowa.

    -   Wszystkie punkty są zdefiniowane przez ich `FreeCAD.Vector`.

Aby utworzyć wymiar kątowy, użyj następującej metody:


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```

-   Tworzy `wymiar` kąta z podanego punktu `środka`, listy `kątów` z dwoma elementami i punktu `p3`, przez który ma przechodzić łuk.
    -   Jeśli `angle1 > angle2`, wyświetlany kąt jest różnicą `angle1 - angle2`; w przeciwnym razie wyświetlany jest kąt dopełniający, `360 - (angle2 - angle1)`.
    -   Kąty powinny być podane w stopniach.

Właściwości widoku `wymiaru` można zmienić poprzez nadpisanie jego atrybutów. Na przykład, nadpisać `ViewObject.FontSize` nowym rozmiarem w milimetrach.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/pl
