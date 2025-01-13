---
 GuiCommand:
   Name: Draft Point
   Name/pl: Rysunek Roboczy: Punkt
   MenuLocation: Kreślenie , Punkt<br>Kreślenie 2D , Punkt
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Version: 0.7
---

# Draft Point/pl



## Opis

Polecenie <img alt="" src=images/Draft_Point.svg  style="width:24px;"> **Punkt** środowiska Rysunek Roboczy tworzy zwykły punkt. Punkty mogą być przydatne jako odniesienie do umieszczania linii, polilinii lub innych obiektów.

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Point.svg" width=16px> '''Punkt'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Point.svg" width=16px> Punkt**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Kreślenie 2D → <img src="images/Draft_Point.svg" width=16px> Punkt** z menu.
2.  Otworzy się panel zadań **Punkt**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
3.  Wybierz punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi *(w wersji 1.0)*.

-   Aby ręcznie wprowadzić współrzędne, wprowadź element X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie kursora poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby włączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).
-   Naciśnij **N** lub kliknij pole wyboru **Kontynuuj**, aby włączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po zakończeniu, umożliwiając dalsze tworzenie punktów.
-   Wciśnij **S** by włączyć lub wyłączyć [Przyciąganie](Draft_Snap/pl.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby przerwać wykonywanie polecenia.



## Uwagi

-   Użyj narzędzia <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md), aby przyciągać do punktów szkicu.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Punkt środowiska pracy Rysunek Roboczy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **X|Distance**: określa współrzędną punktu X.

-    **Y|Distance**: określa współrzędną punktu Y.

-    **Z|Distance**: określa współrzędną punktu Z.



### Widok


{{TitleProperty|Rysunek Roboczy}}

-    **Wzór|Enumeration**: niewykorzystane.

-    **Rozmiar wzoru|Float**: niewykorzystane.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Punkt środowiska Rysunek Roboczy użyj metody `make_point` modułu Rysunek Roboczy *({{Version/pl|0.19}})*. Ta metoda zastępuje przestarzałą metodę `makePoint`.


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```

-   Tworzy obiekt `point` w podanych współrzędnych `X`, `Y` i `Z`, z jednostkami w milimetrach. Jeśli nie podano współrzędnych, punkt zostanie utworzony w punkcie odniesienia położenia (0,0,0).
    -   Jeśli `X` jest `point` zdefiniowanym przez `FreeCAD.Vector`, jest on używany.

-    `color`jest krotką `(R, G, B)`, która wskazuje kolor punktu w skali RGB; Każda wartość w krotce powinna mieścić się w zakresie od `0` do `1`.

-    `name`jest nazwą obiektu.

-    `point_size`to rozmiar obiektu w pikselach, jeśli załadowany jest graficzny interfejs użytkownika.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

point1 = Draft.make_point(1600, 1400, 0)

p2 = App.Vector(-3200, 1800, 0)
point2 = Draft.make_point(p2, color=(0.5, 0.3, 0.6), point_size=10)

doc.recompute()
```

Przykład:

Ten kod tworzy `N` losowych punktów w kwadracie o boku `2L`. Wykonuje pętlę tworzącą `N` punktów, które mogą pojawić się w dowolnym miejscu od `-L` do `+L` na X i Y. Wybiera również losowy kolor i rozmiar dla każdego punktu. Zmień wartość `N`, aby zmienić liczbę punktów, i zmień wartość `L`, aby zmienić obszar pokryty przez punkty.


```python
import random
import FreeCAD as App
import Draft

doc = App.newDocument()

L = 1000
centered = App.Placement(App.Vector(-L, -L, 0), App.Rotation())
rectangle = Draft.make_rectangle(2*L, 2*L, placement=centered)

N = 10
for i in range(N):
    x = 2*L*random.random() - L
    y = 2*L*random.random() - L
    z = 0
    r = random.random()
    g = random.random()
    b = random.random()
    size = 15*random.random() + 5
    Draft.make_point(x, y, z, color=(r, g, b), point_size=size)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Point/pl
