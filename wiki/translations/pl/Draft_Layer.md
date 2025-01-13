---
 GuiCommand:
   Name: Draft Layer
   Name/pl: Rysunek Roboczy: Warstwa
   MenuLocation: Narzędzia , Warstwa
   Workbenches: Draft_Workbench/pl
   Version: 0.19
   SeeAlso: Draft_AutoGroup/pl, Draft_LayerManager/pl
---

# Draft Layer/pl



## Opis

Polecenie <img alt="" src=images/Draft_Layer.svg  style="width:24px;"> **Warstwa** tworzy warstwę roboczą. Warstwa jest specjalnym rodzajem grupy z szeregiem [właściwości wizualnych](#Widok.md). Te właściwości i wszelkie ich zmiany są przenoszone na obiekty umieszczone wewnątrz warstwy. Same warstwy są umieszczane w innej specjalnej grupie: Draft LayerContainer.



## Użycie

1.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Layer.svg" width=16px> '''Warstwa'''**.
    -   Wybierz opcję **Narzędzia → <img src="images/Draft_Layer.svg" width=16px> Warstwa** z menu lub z menu kontekstowego [widoku drzewa](Tree_view.md) bądź [widoku 3D](3D_view.md).
    -   Jeśli kontener warstwy już istnieje: kliknij go prawym przyciskiem myszy w widoku drzewa i wybierz opcję **<img src="images/Draft_NewLayer.svg" width=16px> Dodaj nową warstwę** z menu kontekstowego.
2.  Jeśli nie istnieje, najpierw tworzony jest kontener warstwy.
3.  Warstwa jest tworzona i umieszczana w kontenerze warstw.
4.  Opcjonalnie można zmienić [właściwości](#Właściwości.md) warstwy.
5.  Opcjonalnie umieść obiekty w warstwie, przeciągając i upuszczając je na warstwie w [widoku drzewa](Tree_view/pl.md). Obiekty mogą być również umieszczane w warstwie poprzez edycję właściwości **Grupa** warstwy.
6.  Opcjonalnie [aktywuj](#Opcje_warstwy.md) warstwę.



## Menu podręczne 



### Opcje kontenera warstw 

W przypadku kontenera warstw te dodatkowe opcje są dostępne w menu kontekstowym [widoku drzewa](Tree_view/pl.md):

-    **<img src="images/Draft_Layer.svg" width=16px>: scal wszystkie warstwy o tej samej etykiecie bazowej. Scal duplikaty warstw**: scala wszystkie warstwy z tą samą etykietą bazową.

:   Podstawowa etykieta warstwy to jej **Etykieta** pozbawiona końcowych cyfr i spacji. Wszystkie warstwy z tą samą etykietą bazową są łączone w jedną warstwę z **Etykietą** ustawioną na tę etykietę bazową.

-    **<img src="images/Draft_NewLayer.svg" width=16px>: Dodaj nową warstwę**: dodaje nową warstwę do bieżącego dokumentu.



### Opcje warstwy 

W przypadku warstwy środowiska Rysunek Roboczy te dodatkowe opcje są dostępne w menu podręcznym [Widok drzewa](Tree_view/pl.md):

-    **<img src="images/button_right.svg" width=16px>: [Aktywuj wybraną warstwę](Draft_AutoGroup/pl.md)**: aktywuje wybraną warstwę.

-    **<img src="images/Draft_SelectGroup.svg" width=16px> [Wybierz zawartość warstwy](Draft_SelectGroup/pl.md)**: zaznacza obiekty wewnątrz wybranej warstwy.



## Zachowanie przeciągnij i upuść 


{{Version/pl|0.21}}

Jeśli upuścisz obiekt z [Std: Grupa](Std_Group/pl.md), lub obiekt podobny do grupy, taki jak [Architektura\" Część budowli](Arch_BuildingPart/pl.md), na warstwę w [widoku drzewa](Tree_view/pl.md), nie zostanie on usunięty z grupy i vice versa. Aby usunąć obiekt z warstwy, musi on zostać upuszczony na innej warstwie lub na węźle dokumentu. Nie ma potrzeby przytrzymywania klawisza **Ctrl** podczas przeciągania z lub upuszczania na warstwę.



## Uwagi

-   Nową warstwę można również utworzyć za pomocą polecenia [Grupowanie automatyczne](Draft_AutoGroup/pl.md).
-   Środowisko pracy [BIM](BIM_Workbench/pl.md) oferuje kompletne [narzędzie do zarządzania warstwami](BIM_Layers/pl.md), które ostatecznie zostanie włączone do środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md).



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Warstwa środowiska pracy Rysunek Roboczy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Etykieta}}

-    **Group|LinkList**: określa obiekty znajdujące się wewnątrz warstwy.



### Widok


{{TitleProperty|Warstwa}}

Właściwości w tej sekcji są stosowane do obiektów umieszczonych wewnątrz warstwy. Wszelkie zmiany tych właściwości są do nich przenoszone. W przypadku dwóch właściwości, **Kolor linii** i **Kolor kształtu**, zachowanie to jest opcjonalne.

-    **Styl rysowania|Enumeration**: określa styl rysowania warstwy: {{value|Ciągła}}, {{value|Przerywana}}, {{value|Kropkowana}} lub {{value|KreskaKropka}}.

-    **Kolor linii|Color**: określa kolor linii warstwy.

-    **Szerokość linii|Float**: określa szerokość linii warstwy.

-    **Zastąp elementy potomne kolorem linii|Bool**: określa, czy zmiany w **Kolorze linii** warstwy są przekazywane do obiektów wewnątrz warstwy.

-    **Zastąp elementy podrzędne kolorem kształtu|Bool**: określa, czy zmiany w **Kolorze kształtu** warstwy są przekazywane do obiektów wewnątrz warstwy. {{Version/pl|1.0}}

-    **Wygląd kształtu|MaterialList**: określa wygląd kształtu warstwy. {{Version/pl|1.0}}

-    **Kolor kształtu|Color**: określa kolor kształtu warstwy.

-    **Przezroczystość|Percent**: określa przezroczystość warstwy.


{{TitleProperty|Drukuj}}

-    **Kolor wydruku linii|Color**: określa kolor wydruku linii warstwy.

-    **Użyj koloru wydruku|Bool**: określa, czy **Kolor wydruku linii|** warstwy jest używany, gdy [TechDraw DraftView](TechDraw_DraftView.md) jest tworzony z obiektów wewnątrz warstwy.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć warstwę środowiska Rysunek Roboczy, użyj metody `make_layer` modułu Rysunek Roboczy. Aby dodać lub usunąć obiekty z warstwy, zmień jej właściwość `Grupa`.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

layer = Draft.make_layer(line_color=(1.0, 0.0, 0.0, 0.0),
                         shape_color=(1.0, 1.0, 0.0, 0.0))

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)
layer.Group = [polygon1, polygon2, polygon3]

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Layer/pl
