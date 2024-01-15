# Draft Pattern/pl
## Opis

Obiekty środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) z właściwością **Utwórz ścianę** mogą wyświetlać wzór SVG zamiast jednolitego koloru ściany.

![](images/DraftPatternSample.png ) 
*Elipsa i wielokąt z wzorem SVG.*



## Użycie

1.  Upewnij się, że obiekty są zamknięte, płaskie i nie przecinają się.

2.  Aby zamknąć [polilinię](Draft_Wire/pl.md), [krzywa złożoną](Draft_BSpline/pl.md), [Sześcienną krzywą Béziera](Draft_CubicBezCurve/pl.md) lub [Krzywą Bézier\'a](Draft_BezCurve/pl.md) ustaw ich właściwość **Zamknięty** na {{TRUE/pl}}.

3.  Aby zamknąć [okrąg](Draft_Circle/pl.md) lub [elipsę](Draft_Ellipse/pl.md) ustaw ich właściwości **kąt pierwszy** i **kąt drugi** na tę samą wartość.

4.  Wybierz obiekty.

5.  Przejdź do zakładki **Widok** w [Edytorze właściwości](Property_editor.md).

6.  
    **Tryb wyświetlania**musi być ustawiony na {{Value|Cieniowany z krawędziami}}.

7.  Wybierz **Wzór**.

8.  Opcjonalnie zmień rozmiar **Rozmiar wzoru**. Należy pamiętać, że większa wartość skutkuje gęstszym wzorem.

9.  Wzór nie jest wyświetlany, gdy obiekty są zaznaczone. Usuń ich zaznaczenie, aby sprawdzić wynik.

10. Opcjonalnie można ponownie wybrać obiekty, aby zmienić właściwości wzoru.



## Dostępne wzory 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc



## Uwagi

-   Wzory SVG są przechowywane w plikach **.SVG**. Możliwe jest użycie własnych niestandardowych wzorców. Zobacz [Ustawienia](#Ustawienia.md).
-   Same wzory nie są zapisywane w dokumencie FreeCAD. Obiekty, których **Wzór** nie zostanie znaleziony, są wyświetlane z jednolitym kolorem powierzchni.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   Aby zmienić **Rozmiar wzoru** używany dla nowych obiektów: **Edycja → Preferencje ... → Rysunek Roboczy → Wygląd → Rozmiar wzoru SVG**.
-   Aby określić katalog z dodatkowymi wzorcami SVG: **Edycja → Preferencje ... → Rysunek Roboczy → Wygląd → Dodatkowa lokalizacja wzorów SVG**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/pl
