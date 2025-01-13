---
 GuiCommand:
   Name: Arch Panel Sheet
   Name/pl: BIM: Arkusz panelu
   MenuLocation: Narzędzia , Narzędzia panelu , Arkusz panelu
   Workbenches: BIM_Workbench/pl
   Shortcut: **P** **S**
   Version: 0.17
   SeeAlso: Arch_Panel/pl, Arch_Panel_Cut/pl, Arch_Nest/pl
---

# Arch Panel Sheet/pl



## Opis

Narzędzie to pozwala zbudować arkusz 2D, zawierający dowolną liczbę obiektów [Cięcia panelu](Arch_Panel_Cut/pl.md) lub dowolny inny obiekt 2D, taki jak te wykonane za pomocą środowisk [Rysunek Roboczy](Draft_Workbench/pl.md) i [Szkicownik](Sketcher_Workbench/pl.md). Arkusz panelu jest zwykle tworzony w celu rozplanowania cięć, które mają być wykonane przez maszynę CNC. Arkusze te można następnie wyeksportować do pliku [DXF](Draft_DXF/pl.md).

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width:600px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width:600px;">

*Powyższy obraz przedstawia wygląd arkuszy paneli po wyeksportowaniu do formatu DXF*.



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów [Cięcia panelu](Arch_Panel_Cut/pl.md) lub dowolny inny obiekt 2D leżący na płaszczyźnie XY.
2.  Z menu wybierz narzędzie **Narzędzia → Narzędzia panelu → <img src="images/Arch_Panel_Sheet.svg" width=16px> '''Arkusz panelu'''**.
3.  Dostosuj żądane właściwości.



## Opcje

-   Po utworzeniu arkusza panelu, z obiektami podrzędnymi lub bez, każdy inny obiekt podrzędny można dodać lub usunąć z arkusza panelu, klikając go dwukrotnie w widoku drzewa i dodając lub usuwając obiekty z jego folderu Group.
-   Dwukrotne kliknięcie panelu w widoku drzewa umożliwia również przenoszenie obiektów zawartych w tym arkuszu lub przenoszenie jego znacznika.
-   Możliwe jest automatyczne tworzenie paneli składających się z więcej niż jednego arkusza materiału, poprzez zwiększenie jego właściwości Arkusze.
-   Arkusze paneli mogą wyświetlać margines, który jest przydatny, aby upewnić się, że między obiektami wewnętrznymi a granicą arkusza zawsze znajduje się pewna przestrzeń.
-   Gdy arkusze panelu są eksportowane do DXF, kontury, wewnętrzne otwory, znaczniki ich wewnętrznych elementów podrzędnych są umieszczane na różnych warstwach, jak pokazano na powyższym obrazku.



## Właściwości



### Dane

-    **Wysokość**: Wysokość arkusza.

-    **Szerokość**: Szerokość arkusza.

-    **Współczynnik wypełnienia**: Procent obszaru arkusza, który jest wypełniony wycięciami *(automatycznie)*.

-    **Tekst Tagu**: Tekst do wyświetlenia.

-    **Rozmiar Tagu**: Rozmiar tekstu znacznika.

-    **Pozycja Tagu**: Pozycja tekstu znacznika. Zachowaj (0,0,0) dla automatycznej pozycji środkowej.

-    **Obrót Tagu**: Obrót tekstu znacznika.

-    **Plik czcionki**: Czcionka tekstu znacznika.

-    **Utwórz ścianę**: Jeśli przyjmie wartość {{True/pl}}, panel jest obiektem ściana środowiska Część , w przeciwnym razie polilinią środowiska Część.

-    **Kierunek ziarna**: Pozwala poinformować o głównym kierunku włókien panelu *(kierunek zgodny z ruchem wskazówek zegara, 0° oznacza w górę)*.



### Widok

-    **Margines**: Margines, który może być wyświetlany poza kształtem wycięcia panelu.

-    **Pokaż Margines**: Włącza / wyłącza wyświetlanie marginesu.

-    **Show Grain**: Pokazuje teksturę włókna *(właściwość Utwórz ścianę musi być ustawione na {{True/pl}})*.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Arkusz panelu** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Tworzy obiekt `Sheet` z `panels`, który jest listą obiektów [Panelu](Arch_Panel/pl.md).

Przykład:


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(500, 200)
Polygon = Draft.makePolygon(5, 750)

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2000, 400, 0)
p3 = FreeCAD.Vector(1250, 800, 0)
Wire = Draft.makeWire([p1, p2, p3], closed=True)

Panel1 = Arch.makePanel(Rect, thickness=36)
Panel2 = Arch.makePanel(Polygon, thickness=36)
Panel3 = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

Cut1 = Arch.makePanelCut(Panel1)
Cut2 = Arch.makePanelCut(Panel2)
Cut3 = Arch.makePanelCut(Panel3)
Cut1.ViewObject.LineWidth = 3
Cut2.ViewObject.LineWidth = 3
Cut3.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()

Sheet = Arch.makePanelSheet([Cut1, Cut2, Cut3])
```



## Poradniki

-   [Poradnik przenoszenia Wikihouse](Wikihouse_porting_tutorial/pl.md)





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Panel Sheet/pl
