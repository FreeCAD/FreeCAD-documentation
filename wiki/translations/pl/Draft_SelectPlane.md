---
 GuiCommand:
   Name: Draft SelectPlane
   Name/pl: Rysunek Roboczy: Wybór płaszczyzny
   MenuLocation: Kreślenie , Przybory , Wybierz płaszczyznę
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: Rysunek Roboczy: **W** **P**
   SeeAlso: Draft_SetWorkingPlaneProxy/pl, Draft_ToggleGrid/pl
---

# Draft SelectPlane/pl



## Opis

Polecenie <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Wybór płaszczyzny roboczej** definiuje bieżącą płaszczyznę roboczą. Jest to płaszczyzna zdefiniowana w [widoku 3D](3D_view/pl.md), na której tworzone są nowe obiekty [Rysunku Roboczego](Draft_Workbench/pl.md). Płaszczyzna robocza może być oparta na jednym z kilku [nastaw](#Użycie_z_ustawieniami_wstępnymi.md) lub na zaznaczeniu. Zaznaczenie może zostać utworzone przed *([wyborem wstępnym](#Użycie_ze_wstępnym_wyborem.md))* lub po *([uruchomieniu polecenia](#Użycie_z_wyborem_w_kolejnym_kroku.md))*.


<small>(v1.0)</small> 

: Dla każdego widoku 3D zapisywana jest osobna płaszczyzna robocza.

Przycisk ![](images/Draft_tray_button_plane.png ) w [Tacka narzędziowa](Draft_Tray/pl.md) zmienia swój wygląd w zależności od bieżącej płaszczyzny roboczej. {{Version/pl|1.0}}: Jeśli płaszczyzna robocza nie jest ustawiona na **Automatyczną**, gwiazdka *(*****)* jest dodawana do etykiety przycisku, jeśli punkt odniesienia położenia płaszczyzny roboczej nie pasuje do globalnego punktu odniesienia.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Kształty tworzone na różnych płaszczyznach roboczych.*



## Użycie ze wstępnym wyborem 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz pojedynczy obiekt. Obsługiwane są następujące obiekty:
        -   [Pośrednia płaszczyzna robocza](Draft_WorkingPlaneProxy/pl.md): **View Data** *(pozycja kamery)* i **Visibility Map** *(zapisana widoczność obiektów)* pośredniej płaszczyzny roboczej są również przywracane.
        -   [Architektura: Osie](Arch_Axis/pl.md) *({{Version/pl|1.0}})*
        -   [Architektura: Układ osi](Arch_AxisSystem/pl.md) ({{Version/pl|1.0}})
        -   [Architektura: Część budowli - piętro](Arch_BuildingPart/pl.md)
        -   [Architektura: Płaszczyzna przekroju](Arch_SectionPlane/pl.md)
        -   [Std: Część](Std_Part/pl.md): aby uniknąć zaznaczania elementów podrzędnych, zaleca się zaznaczanie ich w [widoku drzewa](Tree_view/pl.md).
        -   Obiekty nie będące bryłami, które składają się z pojedynczej płaskiej powierzchni lub pojedynczej zakrzywionej krawędzi, lub *({{Version/pl|1.0}})*, które mają trzy lub więcej wierzchołków.
        -   Obiekty bryłowe lub obiekty bez kształtu, które mają właściwość **Umiejscowienie**. *({{Version/pl|1.0}})*
    -   Wybierz jeden lub więcej elementów podrzędnych. Można wybrać:
        -   Płaską powierzchnię.
        -   Zakrzywioną krawędź.
        -   Trzy wierzchołki.
        -   Krawędź i wierzchołek lub dwie krawędzie. Połączone wierzchołki muszą definiować płaszczyznę. *({{Version/pl|1.0}})*
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk ![](images/Draft_tray_button_plane.png ) w [tacce narzędziowej](Draft_Tray/pl.md).
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz opcję **Narzędzia → <img src="images/Draft_SelectPlane.svg" width=16px> Wybierz płaszczyznę** z menu lub menu kontekstowego [widoku drzewa](Tree_view/pl.md) bądź [widoku 3D](3D_view/pl.md).
    -   Rysunek Roboczy: Użyj skrótu klawiaturowego: **W**, a następnie **P**.
3.  Płaszczyzna robocza i ikona [tacki narzędziowej](Draft_Tray/pl.md) zostaną zaktualizowane.



## Użycie z wyborem w kolejnym kroku 

1.  Wywołaj polecenie jak opisano wyżej.
2.  Otworzy się panel zadań **Ustawienia płaszczyzny roboczej**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Wykonaj jedną z następujących czynności:
    -   Wybierz pojedynczy obiekt. Zobacz [poprzedni akapit](#Użycie_ze_wstępnym_wyborem.md).
    -   Wybierz jeden lub więcej elementów podrzędnych. Zobacz [poprzedni akapit](#Użycie_ze_wstępnym_wyborem.md).
4.  Kliknij gdziekolwiek w oknie [widoku 3D](3D_view/pl.md), aby potwierdzić wybór i zakończyć polecenie.
5.  Płaszczyzna robocza i ikona [tacki narzędziowej](Draft_Tray/pl.md) zostaną zaktualizowane.



## Użycie z ustawieniami wstępnymi 

1.  Wywołaj polecenie jak opisano wyżej.
2.  Otworzy się panel zadań **Ustawienia płaszczyzny roboczej**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Naciśnij dowolny przycisk, aby zakończyć polecenie.
4.  Płaszczyzna robocza i ikona [tacki narzędziowej](Draft_Tray/pl.md) zostaną zaktualizowane.



## Opcje

-   Naciśnij przycisk **<img src="images/View-top.svg" width=16px> Góra (XY)**, aby wyrównać płaszczyznę roboczą z płaszczyzną XY globalnego układu współrzędnych.

-   Naciśnij przycisk **<img src="images/View-front.svg" width=16px> Przód (XZ)**, aby wyrównać płaszczyznę roboczą z płaszczyzną XZ globalnego układu współrzędnych.

-   Naciśnij przycisk **<img src="images/View-right.svg" width=16px> Bok (YZ)**, aby wyrównać płaszczyznę roboczą z płaszczyzną YZ globalnego układu współrzędnych.

-   Naciśnij przycisk **<img src="images/View-isometric.svg" width=16px> Wyrównaj do widoku**, aby wyrównać płaszczyznę roboczą z bieżącym [widokiem 3D](3D_view/pl.md). Jeśli pole wyboru **Wyśrodkuj płaszczyznę na widoku** nie jest zaznaczone, początek płaszczyzny roboczej będzie odpowiadał początkowi globalnego układu współrzędnych, w przeciwnym razie będzie odpowiadał środkowi bieżącego [widoku 3D](3D_view/pl.md).

-   Naciśnij przycisk **<img src="images/View-axonometric.svg" width=16px> Automatycznie**, aby ustawić płaszczyznę roboczą **Automatycznie**. Płaszczyzna robocza ustawiona na **Automatycznie**, automatycznie zostanie wyrównana do bieżącego [widoku 3D](3D_view/pl.md) za każdym razem, gdy uruchomione zostanie polecenie środowisko Rysunek Roboczy lub [BIM](BIM_Workbench/pl.md) wymagające wprowadzenia punktu. Jest to odpowiednik naciśnięcia przycisku **<img src="images/View-isometric.svg" width=16px> Wyrównaj do widoku** przed użyciem polecenia. Dodatkowo płaszczyzna robocza zostanie wyrównana do płaskich powierzchni, które zostały wybrane przed uruchomieniem polecenia lub gdy punkty na płaskich powierzchniach zostaną wybrane podczas polecenia.

-   Polecenie **Odsunięcie** definiuje prostopadłą odległość między obliczoną płaszczyzną a rzeczywistą płaszczyzną roboczą.

-   Zaznacz pole wyboru **Wyśrodkuj płaszczyznę na widoku**, aby umieścić początek płaszczyzny roboczej w środku bieżącego [widoku 3D](3D_view/pl.md). Opcja ta może być przydatna w połączeniu z przyciskiem **<img src="images/View-isometric.svg" width=16px> Wyrównaj do widoku**.

-   Wybierz wierzchołek w oknie [widoku 3D](3D_view/pl.md) i naciśnij przycisk **<img src="images/Draft_Move.svg" width=16px> Przesuń płaszczyznę roboczą**, aby przesunąć płaszczyznę roboczą tak, aby jej punkt odniesienia położenia odpowiadał pozycji wybranego wierzchołka.

-   Parametr **Grid color** pozwala na szybką zmianę koloru siatki. {{Version/pl|1.0}}

-   Parametr **Odstęp siatki** definiuje odległość między liniami siatki.

-   Wartość **Główna linia co** określa miejsce rysowania głównych linii siatki. Główne linie siatki są nieco grubsze niż zwykłe linie siatki. Na przykład, jeśli odstęp między liniami siatki wynosi {{Value|0.5 m}}, a główna linia występuje co {{Value|10 linii}}, taka linia będzie występować co {{Value|5 m}}.

-   Wartość **Rozmiar siatki** określa liczbę linii siatki w kierunku X i Y siatki.

-    **Promień przyciągania**to maksymalna odległość, w jakiej funkcja [Przyciągnij do siatki](Draft_Snap_Grid/pl.md) wykrywa przecięcia linii siatki.

-   Naciśnij przycisk **<img src="images/view-fullscreen.svg" width=16px> Wyśrodkuj widok**, aby wyrównać [widok 3D](3D_view/pl.md) z bieżącą płaszczyzną roboczą.

-   Naciśnij przycisk **<img src="images/sel-back.svg" width=16px> Poprzedni**, aby zresetować płaszczyznę roboczą do poprzedniej pozycji.

-   Naciśnij przycisk **<img src="images/sel-forward.svg" width=16px> Następny**, aby zresetować płaszczyznę roboczą do następnej pozycji. {{Version/pl|1.0}}

-   Naciśnij **Esc** lub przycisk **Zamknij**, aby przerwać wykonywanie polecenia.



## Uwagi

-   Przydatne może być wyrównanie [widoku 3D](3D_view/pl.md) z wybraną płaszczyzną roboczą. Na przykład po przełączeniu płaszczyzny roboczej na Przód możesz chcieć przełączyć się również na widok [z przodu](Std_ViewFront/pl.md).
-   Siatkę można przełączać za pomocą polecenia [Przełącz widoczność siatki](Draft_ToggleGrid/pl.md).
-   Klikając dwukrotnie narzędzie [Pośrednia płaszczyzna robocza](Draft_WorkingPlaneProxy/pl.md) w [Widoku drzewa](Tree_view/pl.md) można szybko przełączać się między płaszczyznami roboczymi.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   Ustawienia siatki w panelu zadań, a także kilka innych ustawień siatki są dostępne jako preferencje: **Edycja → Preferencje ... → Rysunek Roboczy → Siatka i przyciąganie**.
-   Promień przyciągania można również zmienić w locie *(patrz [ustawienia przyciągania](Draft_Snap/pl#Ustawienia.md))* lub poprzez modyfikację parametru: **Narzędzia → Edytuj parametry ... → BaseApp → Preferencje → Mod → Draft → snapRange**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).


{{Version/pl|1.0}}

Moduł PłaszczyznaRobocza oferuje dwie klasy do tworzenia obiektów płaszczyzny roboczej: klasę `PlaneBase` i klasę `PlaneGui`. Druga klasa dziedziczy z pierwszej. Obiekty klasy `PlaneGui` współdziałają z GUI *(przycisk [Tacka narzędziowa](Draft_Tray/pl.md))*, [widok 3D](3D_view/pl.md) i [siatka](Draft_Snap_Grid/pl.md). Obiekty `PlaneBase` nie.

Użyj metody `get_working_plane()` modułu PłaszczyznaRobocza, aby uzyskać instancję klasy `PlaneGui` powiązaną z bieżącym widokiem 3D. Metoda zwraca istniejącą płaszczyznę roboczą powiązaną z widokiem lub tworzy nową płaszczyznę roboczą, jeśli jest to wymagane.


```python
import FreeCAD as App
import WorkingPlane

wp = WorkingPlane.get_working_plane()

origin = App.Vector(0, 0, 0)
normal = App.Vector(1, 1, 1).normalize()
offset = 17
wp.align_to_point_and_axis(origin, normal, offset)

point = App.Vector(10, 15, 2)
projection = wp.project_point(point)
print(projection)
```

Klasa `PlaneBase` może być używana do tworzenia płaszczyzn roboczych niezależnie od GUI:


```python
import WorkingPlane

wp = WorkingPlane.PlaneBase()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/pl
