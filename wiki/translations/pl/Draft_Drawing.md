---
 GuiCommand:
   Name: Draft Drawing
   Name/pl: Kreślenie: Projekt rysunku
   Workbenches: Drawing_Workbench/pl, Arch_Workbench/pl
   SeeAlso: TechDraw_DraftView/pl
---

# Draft Drawing/pl



## Opis

Polecenie <img alt="" src=images/Draft_Drawing.svg  style="width:24px;"> **Kreślenie** wstawia widoki wybranych obiektów do strony [Rysunek Roboczy](Drawing_Workbench/pl.md).

To polecenie jest podobne do polecenia [Widok](Drawing_View/pl.md), ale jest zoptymalizowane dla obiektów środowiska [Rysunek Roboczy](Draft_Workbench/pl.md). W przeciwieństwie do tego polecenia, może ono obsługiwać określone obiekty, takie jak [Wymiar](Draft_Dimension/pl.md) i [Tekst](Draft_Text/pl.md), a także może renderować ściany.

To polecenie jest już przestarzałe. Zamiast niego należy użyć środowiska pracy [Rysunek Roboczy](TechDraw_Workbench/pl.md) i polecenia [Wstaw obiekt środowiska Rysunek Roboczy](TechDraw_DraftView/pl.md).

<img alt="" src=images/Draft_drawing_example.jpg  style="width:640px;"> 
*Po lewej wybrane obiekty szkicu. Po prawej stronie znajdują się utworzone widoki rysunku.*



## Użycie

1.  Aby użyć tego polecenia w FreeCAD w wersji 0.19 i nowszych, należy dodać przycisk do niestandardowego paska narzędzi. Zapoznaj się z informacjami zawartymi na stronie [Dostosowywanie interfejsu użytkownika do własnych potrzeb](Interface_Customization/pl.md).
2.  Wybierz jeden lub więcej obiektów. Dla każdego obiektu zostanie utworzony osobny widok.
3.  Opcjonalnie dodaj stronę środowiska pracy [Kreślenie](Drawing_Workbench/pl.md) do zaznaczenia. Jeśli tego nie zrobisz, widok zostanie wstawiony do pierwszej strony w dokumencie. Jeśli w dokumencie nie ma stron, najpierw tworzona jest nowa strona.
4.  Naciśnij przycisk **<img src="images/Draft_Drawing.svg" width=16px> [Kreślenie: Projekt rysunku](Draft_Drawing/pl.md)**.
5.  W wersji FreeCAD 0.19 występuje błąd w poleceniu. Początkowa wartość właściwości **Kierunek** to {{Value|[0, 0, 0]}}, co jest niedozwolone. W przypadku obiektów na płaszczyźnie równoległej do płaszczyzny XY globalnego układu współrzędnych należy ją zmienić na {{Value|[0, 0, 1]}}. Po zmianie tej właściwości strona i widok mogą wymagać [przeliczenia](Std_Refresh/pl.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Drawing/pl
