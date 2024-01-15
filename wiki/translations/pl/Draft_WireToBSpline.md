---
 GuiCommand:
   Name: Draft WireToBSpline
   Name/pl: Rysunek Roboczy: Polilinia na krzywą złożoną
   MenuLocation: Modyfikacja , Polilinia na krzywą złożoną
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   SeeAlso: Draft_Wire/pl, Draft_BSpline/pl
---

# Draft WireToBSpline/pl



## Opis

Polecenie <img alt="" src=images/Draft_WireToBSpline.svg  style="width:24px;"> **Polilinia na krzywą złożoną** konwertuje [polilinię](Draft_Wire/pl.md) na [krzywą złożoną](Draft_BSpline/pl.md) i odwrotnie.

<img alt="" src=images/Draft_Wire2BSpline_example.jpg  style="width:400px;"> 
*Konwersja polinii pomocniczej w linię złożoną, a zamkniętej linii złożonej w zamkniętą polinię.*



## Użycie

1.  Wybierz narzędzie [Polilinia](Draft_Wire/pl.md) lub [Krzywa złożona](Draft_BSpline/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_WireToBSpline.svg" width=16px> '''Polilinia na krzywą złożoną'''**.
    -   Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_WireToBSpline.svg" width=16px> Polilinia na krzywą złożoną**.
3.  Tworzony jest nowy obiekt.



## Uwagi

-   Polecenie może spowodować powstanie zamkniętej, samoprzecinającej się [polilinii](Draft_Wire/pl.md) lub [krzywej złożonej](Draft_BSpline/pl.md) ze ścianą. Taki obiekt nie będzie wyświetlany poprawnie w [widoku 3D](3D_view/pl.md). Jego właściwość **Utwórz ścianę** lub **Zamknięta** musi być ustawiona na wartość {{FALSE/pl}}.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby przekonwertować polilinię na krzywą złożoną lub odwrotnie, należy przekazać właściwość `Punkty` obiektu źródłowego do metody `[make_bspline](Draft_BSpline/pl#Tworzenie_skryptów.md)` lub odpowiednio metody `[make_wire](Draft_Wire/pl#Tworzenie_skryptów.md)` modułu Rysunek Roboczy.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(1000, 1000, 0)
p2 = App.Vector(2000, 1000, 0)
p3 = App.Vector(2500, -1000, 0)
p4 = App.Vector(3500, -500, 0)

base_wire = Draft.make_wire([p1, p2, p3, p4])
base_spline = Draft.make_bspline([-p1, -1.3*p2, -1.2*p3, -2.1*p4])

points1 = base_wire.Points
spline_from_wire = Draft.make_bspline(points1)

points2 = base_spline.Points
wire_from_spline = Draft.make_wire(points2)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WireToBSpline/pl
