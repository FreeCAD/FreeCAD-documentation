---
 GuiCommand:
   Name: Draft Mirror
   Name/pl: Rysunek Roboczy: Odbicie lustrzane
   MenuLocation: Modyfikacja , Mirror
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **M** **I**
   SeeAlso: Draft_Clone/pl
---

# Draft Mirror/pl



## Opis

Polecenie <img alt="" src=images/Draft_Mirror.svg  style="width:24px;"> **Odbicie lustrzane** tworzy lustrzane kopie obiektów [Odbicie lustrzane](Part_Mirror.md) środowiska pracy Część z wybranych obiektów. Obiekt [Odbicie lustrzane](Part_Mirror.md) środowiska pracy Część jest parametryczny, więc będzie aktualizowany, jeśli zmieni się jego obiekt źródłowy.

Narzędzie Przesuń może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md).

<img alt="" src=images/Draft_Mirror_example.jpg  style="width:400px;"> 
*Tworzenie kopii lustrzanej obiektu.*



## Użycie

Zobacz także strony: [Rysunek Roboczy: Przyciąganie](Draft_Snap/pl.md) i [Rysunek Roboczy: Wiązania](Draft_Constrain/pl.md).

1.  Opcjonalnie wybierz jeden lub więcej obiektów.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Mirror.svg" width=16px> [Odbicie lustrzane](Draft_Mirror.md)**.
    -   Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Mirror.svg" width=16px> Odbicie lustrzane**.
    -   Użyj skrótu klawiaturowego: **M**, a następnie **I**.
3.  Jeśli nie wybrałeś jeszcze żadnego obiektu: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Otworzy się panel zadań **Odbicie lustrzane**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
5.  Wybierz pierwszy punkt płaszczyzny lustra w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
6.  Wybierz drugi punkt płaszczyzny lustra w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
7.  Płaszczyzna lustrzana jest definiowana przez wybrane punkty i normalną [Płaszczyzna robocza szkicu](Draft_SelectPlane/pl.md).



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, wprowadź element X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Wciśnij **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne drugiego punktu są względne do pierwszego punktu, w przeciwnym razie są one względne do początku układu współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij **S**, aby włączyć lub wyłączyć [Przyciąganie](Draft_Snap/pl.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby przerwać polecenie.



## Uwagi

-   Kopie lustrzane [linii](Draft_Line/pl.md), [polilinii](Draft_Wire/pl.md), [łuków](Draft_Arc/pl.md) i [okręgów](Draft_Circle/pl.md) mogą zostać przekształcone w niezależne edytowalne obiekty środowiska Rysunek Roboczy przy użyciu narzędzia [Rozbij kształt](Draft_Downgrade/pl.md), a następnie [Ulepsz kształt](Draft_Upgrade/pl.md).
-   Polecenie [Utwórz prostą kopię](Part_SimpleCopy/pl.md) może być użyte do utworzenia kopii lustrzanej obiektu, która nie jest połączona z obiektem źródłowym.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Odbicie lustrzane** środowiska pracy Rysunek roboczy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Podstawa}}

-    **Źródło|Link**: określa obiekt, który zostanie odzwierciedlony.


{{TitleProperty|Płaszczyzna}}

-    **Baza|Vector**: określa punkt bazowy płaszczyzny lustrzanej.

-    **Normal|Vector**: określa normalny kierunek płaszczyzny lustra.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby wykonać odbicie lustrzane obiektów, użyj metody `mirror` środowiska Rysunek Roboczy.


```python
mirrored_list = mirror(objlist, p1, p2)
```

-    `objlist`zawiera obiekty, które mają zostać odzwierciedlone. Jest to pojedynczy obiekt lub lista obiektów.

-    `p1`jest pierwszym punktem płaszczyzny lustrzanej.

-    `p2`jest drugim punktem płaszczyzny lustrzanej.

-   Jeśli [płaszczyzna robocza](Draft_SelectPlane/pl.md) jest dostępna, wyrównanie płaszczyzny lustrzanej jest określane przez jej normalną, w przeciwnym razie używany jest kierunek widoku kamery w aktywnym oknie [widoku 3D](3D_view/pl.md). Jeśli interfejs graficzny nie jest dostępny, używana jest oś Z.

-    `mirrored_list`jest zwracany z nowymi obiektami `Part::Mirroring`. Jest to pojedynczy obiekt lub lista obiektów, w zależności od `objlist`.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(FreeCAD.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

p1 = App.Vector(2000, -1000, 0)
p2 = App.Vector(2000, 1000, 0)

line1 = Draft.make_line(p1, p2)
mirrored1 = Draft.mirror(polygon1, p1, p2)

Line2 = Draft.make_line(-p1, -p2)
mirrored2 = Draft.mirror([polygon1, polygon2], -p1, -p2)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Mirror/pl
