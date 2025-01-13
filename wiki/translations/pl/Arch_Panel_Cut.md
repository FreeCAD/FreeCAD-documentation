---
 GuiCommand:
   Name: Arch Panel Cut
   Name/pl: BIM: Cięcie panelu
   MenuLocation: Narzędzia , Narzędzia panelu , Cięcie panelu
   Workbenches: BIM_Workbench/pl
   Shortcut: **P** **C**
   Version: 0.17
   SeeAlso: Arch_Panel/pl, Arch_Panel_Sheet/pl, Arch_Nest/pl
---

# Arch Panel Cut/pl



## Opis

Narzędzie **Cięcie panelu** tworzy w dokumencie 3D płaski widok 2D [panelu](Arch_Panel/pl.md), który może zostać włączony do [arkusza](Arch_Panel_Sheet/pl.md) lub bezpośrednio wyeksportowany do formatu [DXF](Draft_DXF/pl.md). Obiekty Cięcia panelu są również obsługiwane przez środowisko pracy [CAM](CAM_Workbench/pl.md).

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width:1024px;">



## Użycie

1.  Wybierz jeden lub więcej obiektów [panelu](Arch_Panel/pl.md).
2.  Z menu wybierz narzędzie **Narzędzia → Narzędzia panelu → <img src="images/Arch_Panel_Cut.svg" width=16px> '''Cięcie panelu'''**.
3.  Dostosuj żądane właściwości.



## Opcje

-   Jeśli panel nie jest płaski *(na przykład pofałdowany)*, podcięcie nie pojawi się w panelu cięcia. Narzędzie to jest przydatne głównie w przypadku płaskich paneli
-   Cięcie panelu może wyświetlać znacznik. Znacznik ten może być niestandardową linią tekstu lub może automatycznie wyświetlać znacznik, etykietę lub opis powiązanego panelu.
-   Aby znacznik był przydatny w obróbce CNC, powinien być napisany przy użyciu czcionki typu stick, w której litery są prostymi poliliniami, łatwymi do odtworzenia przez maszynę. Po utworzeniu obiekt Cięcie panelu automatycznie użyje czcionki określonej w preferencjach: **Edycja → Preferencje ... → Rysunek Roboczy → Teksty i wymiary → Domyślny plik czcionki dla kształtu z tekstu**.
-   Dwukrotne kliknięcie obiektu Cięcie panelu w widoku drzewa po jego utworzeniu umożliwia przejście do trybu edycji i zmodyfikowanie położenia znacznika.
-   W przypadku konieczności ułożenia różnych wycięć panelu razem, wycięcia panelu mogą wyświetlać margines, który jest przydatny, aby upewnić się, że między jednym wycięciem a drugim zawsze znajduje się określona przestrzeń.



## Właściwości



### Dane

-    **Źródło**: Obiekt [panelu](Arch_Panel/pl.md) pokazywany przez to cięcie.

-    **Tekst Tagu**: Tekst do wyświetlenia. Może to być %tag%, %label% lub %description%, aby wyświetlić tag panelu lub etykietę.

-    **Rozmiar Tagu**: Rozmiar tekstu znacznika.

-    **Pozycja Tagu**: Pozycja tekstu znacznika. Zachowaj (0,0,0) dla automatycznej pozycji środkowej.

-    **Obrót Tagu**: Obrót tekstu znacznika.

-    **Plik Czcionki**: Czcionka tekstu znacznika.

-    **Utwórz ścianę**: Jeśli przyjmie wartość {{True/pl}}, panel jest obiektem ściana środowiska Część , w przeciwnym razie polilinią środowiska Część.



### Widok

-    **Margines**: Margines, który może być wyświetlany poza kształtem wycięcia panelu.

-    **Pokaż Margines**: Włącza / wyłącza wyświetlanie marginesu.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Cięcie panelu** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji: 
```python
View = makePanelCut(panel, name="PanelView")```

-   Tworzy obiekt {{Incode|View}} *(rzut 2D)* z istniejącego {{Incode|panel}}.

Przykład: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(500, 0, 0)
p3 = FreeCAD.Vector(500, 50, 0)
p4 = FreeCAD.Vector(550, 50, 0)
p5 = FreeCAD.Vector(600, 0, 0)
p6 = FreeCAD.Vector(1000, 0, 0)
p7 = FreeCAD.Vector(1000, 400, 0)
p8 = FreeCAD.Vector(600, 400, 0)
p9 = FreeCAD.Vector(600, 350, 0)
p10 = FreeCAD.Vector(550, 350, 0)
p11 = FreeCAD.Vector(500, 400, 0)
p12 = FreeCAD.Vector(0, 400, 0)

Wire = Draft.makeWire([p1, p2, p3, p4, p5, p6,
                       p7, p8, p8, p9, p10, p11, p12], closed=True)
Panel = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

View = Arch.makePanelCut(Panel)
View.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()
```



## Poradniki

-   [Poradnik przenoszenia Wikihouse](Wikihouse_porting_tutorial/pl.md)





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Panel Cut/pl
