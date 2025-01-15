---
 GuiCommand:
   Name: Arch Axis
   Name/pl: Architektura: Osie
   MenuLocation: Opisy , Osie
   Workbenches: BIM_Workbench/pl
   Shortcut: **A** **X**
   SeeAlso: Arch_AxisSystem/pl, Arch_Grid/pl
---

# Arch Axis/pl



## Opis

Narzędzie **<img src="images/Arch_Axis.svg" width=16px> '''Osie'''** pozwala na umieszczenie serii osi w bieżącym dokumencie. Odległość i kąt między osiami można dostosować, podobnie jak styl numeracji. Osie służą głównie jako odniesienia do przyciągania obiektów, ale mogą być również używane razem z **<img src="images/Arch_AxisSystem.svg" width=16px> [Układem osi](Arch_AxisSystem/pl.md)**. Mogą być one również przywoływane przez inne obiekty architektury w celu utworzenia parametrycznych szyków, na przykład belek lub słupów. Zamiast osi mozna również użyć **<img src="images/Arch_Grid.svg" width=16px> [Siatki](Arch_Grid/pl.md)**.

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Dwie osie obiektów ustawione prostopadle do siebie w celu utworzenia siatki.*



## Użycie

1.  Naciśnij przycisk **<img src="images/Arch_Axis.svg" width=16px> '''Osie'''** lub naciśnij **A**, a następnie **X** przyciski.
2.  [Przesuń](Draft_Move/pl.md) / [Obróć](Draft_Rotate/pl.md) system osi do żądanej pozycji.
3.  Przejdź do trybu edycji, klikając dwukrotnie układ osi w widoku drzewa, aby dostosować jego ustawienia, takie jak liczba osi, odległości i kąty między osiami.



## Opcje

-   Każda oś w serii ma swoją własną odległość i kąt w stosunku do poprzedniej osi. Pozwala to na tworzenie bardzo złożonych układów, takich jak układy nieortogonalne, układy biegunowe lub wszelkiego rodzaju układy niejednolite.
-   Dwukrotne kliknięcie osi w widoku drzewa umożliwia edycję odległości, kątów i etykiet każdej osi.
-   Długość osi, rozmiar bąbelków i style numeracji można dostosowywać bezpośrednio we właściwościach systemu osi.
-   Każda oś może również wyświetlać etykietę, którą można edytować za pomocą okna dialogowego panelu zadań.



## Właściwości

-    **Długość**: Długość osi.

-    **Limit**: Jeśli wartość jest większa niż zero, każda oś będzie przedstawiona jako dwie linie o danej długości zamiast jednej ciągłej linii {{Version/pl|0.20}}.

-    **Rozmiar dymka**: Rozmiar dymka osi.

-    **Style numerowania**: Sposób numerowania osi: 1,2,3, A,B,C, itd\...

-    **Pozycja dymka**: Definiuje gdzie znajduje się dymek na osi: Na punkcie początkowym, końcowym, oba lub żaden.

-    **Nazwa czcionki**: Czcionka do rysowania numeru dymka i / lub etykiet.

-    **Rozmiar czcionki**: Rozmiar tekstu etykiety *(tekst dymka jest kontrolowany przez rozmiar pęcherzyka)*.

-    **Wyświetl etykietę**: Włącza lub wyłącza wyświetlanie tekstów etykiet.



## Użycie jako oznaczenie przekroju 

Ustawiając właściwość **Pozycja dymka** na **Strzałka lewo/prawo** lub **Pasek lewo/prawo**, oś wyświetli wypełnioną strzałkę lub pasek zamiast dymka, dzięki czemu może być użyta jako oznaczenie przekroju. {{Version/pl|0.20}}



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Osi** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```

-   Tworzy obiekt `Axes` z podanej liczby (`num`) osi i `size`, odstępu między każdą osią.

Przykład:


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Axis/pl
