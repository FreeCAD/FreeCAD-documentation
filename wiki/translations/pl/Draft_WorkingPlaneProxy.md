---
 GuiCommand:
   Name: Draft WorkingPlaneProxy
   Name/pl: Rysunek Roboczy: Pośrednia płaszczyzna robocza
   MenuLocation: Narzędzia , Pośrednia płaszczyzna robocza
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   SeeAlso: Draft_SelectPlane/pl
---

# Draft WorkingPlaneProxy/pl



## Opis

Polecenie <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:24px;"> **Pośrednia płaszczyzna robocza** tworzy proxy płaszczyzny roboczej w celu zapisania bieżącej [płaszczyzny roboczej](Draft_SelectPlane/pl.md). Pośrednia płaszczyzna robocza może być użyta do szybkiego przywrócenia płaszczyzny roboczej. Ujęcie widoku i widoczność obiektów w oknie [widoku 3D](3D_view/pl.md) są również zapisywane w obiekcie pośrednim płaszczyzny roboczej i mogą, [opcjonalnie](#Właściwości.md), zostać przywrócone.

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Trzy pośrednie płaszczyzny robocze pokazujące różne orientacje i przesunięcia.*



## Użycie

1.  Opcjonalnie zmień [płaszczyznę roboczą](Draft_SelectPlane/pl.md).
2.  Opcjonalnie można zmienić ujęcie [widoku 3D](3D_view/pl.md).
3.  Opcjonalnie można zmienić widoczność obiektów w dokumencie.
4.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_WorkingPlaneProxy.svg" width=16px> '''Pośrednia płaszczyzna robocza''**.
    -   Wybierz opcję z menu **Narzędzia → <img src="images/Draft_WorkingPlaneProxy.svg" width=16px> Pośrednia płaszczyzna robocza**.
5.  Zostanie utworzona pośrednia płaszczyzna robocza.
6.  Aby wyrównać [płaszczyznę roboczą](Draft_SelectPlane/pl.md) z pośrednią płaszczyzną roboczą, kliknij dwukrotnie pośrednią płaszczyznę roboczą w [widoku drzewa](Tree_view/pl.md) lub użyj polecenia [Wybór płaszczyzny](Draft_SelectPlane/pl.md).



## Menu podręczne 

W przypadku Pośredniej płaszczyzny roboczej środowiska Rysunek Roboczy te dodatkowe opcje są dostępne w menu kontekstowym [widoku drzewa](Tree_view/pl.md):

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Zapisz pozycję kamery**: aktualizuje właściwość **Wyświetlanie danych** proxy płaszczyzny roboczej z bieżącymi ustawieniami kamery [widoku 3D](3D_view/pl.md).

-    **<img src="images/Draft_SelectPlane.svg" width=16px>: Zapisz stan obiektów**: aktualizuje właściwość **Mapa widoczności** proxy płaszczyzny roboczej z bieżącym stanem widoczności obiektów w dokumencie.



## Uwagi

-   Pośrednie płaszczyzny robocze mogą być [przenoszone](Draft_Move/pl.md) i [obracane](Draft_Rotate/pl.md) jak każdy inny obiekt. Użyj <img alt="" src=images/Draft_Snap_Center.svg  style="width:16px;"> [Przyciągnij do środka](Draft_Snap_Center/pl.md), aby przyciągnąć je do punktu **Umiejscowienia**.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Pośrednia płaszczyznarobocza środowiska pracy Rysunek Roboczy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Podstawa}}

-    **Umiejscowienie|Placement**: określa pozycję proxy płaszczyzny roboczej w [widoku 3D](3D_view/pl.md). Aby dowiedzieć się więcej zapoznaj się z informacjami na stronie [Umiejscowienie](Placement/pl.md).

-    **Kształt|Hidden**: określa kształt pośredniej płaszczyzny roboczej.



### Widok


{{TitleProperty|Podstawa}}

-    **Kolor linii|Color**: określa kolor wszystkich elementów pośredniej płaszczyzny roboczej.

-    **Szerokość linii|Float**: określa szerokość linii osi i symboli strzałek.

-    **Przywróć stan|Bool**: określa, czy **Mapa widoczności** jest przywracana, gdy [płaszczyzna robocza](Draft_SelectPlane/pl.md) jest wyrównana z pośrednią płaszczyzną roboczą.

-    **Przywróć widok|Bool**: określa, czy **Widok danych** jest przywracany, gdy [płaszczyzna robocza](Draft_SelectPlane/pl.md) jest wyrównana z pośrednią płaszczyzną roboczą.

-    **Widoczność|Percent**: określa przezroczystość powierzchni pośredniej płaszczyzny roboczej.

-    **Widok danych|FloatList**: określa pozycję i ustawienia kamery.

-    **Mapa widoczności|Map|ukryte**: określa stan widoczności obiektów.


{{TitleProperty|Rysunek Roboczy}}

-    **Rozmiar strzałki|Length**: określa rozmiar symboli strzałek wyświetlanych na końcu trzech osi.

-    **Wyświetlany rozmiar|Length**: określa długość i szerokość pośredniej płaszczyzny roboczej.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Pośrednią płaszczyznę roboczą środowiska Rysunek Roboczy należy użyć metody `make_workingplaneproxy` modułu Rysunek Roboczy.

Jeśli środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) jest aktywne, obiekt aplikacji FreeCAD posiada właściwość `DraftWorkingPlane`, która przechowuje bieżącą płaszczyznę roboczą. Wartość {{Incode|Umiejscowienie}} z metody {{Incode|getPlacement}} obiektu {{Incode|DraftWorkingPlane}} może być użyta do utworzenia wyrównanej pośredniej płaszczyzny roboczej. Z kolei {{Incode|Umiejscowienie}} pośredniej płaszczyzny roboczej może być użyte do wyrównania płaszczyzny roboczej.


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

workplane = App.DraftWorkingPlane
place = workplane.getPlacement()

proxy = Draft.make_workingplaneproxy(place)
proxy.ViewObject.DisplaySize = 3000
proxy.ViewObject.ArrowSize = 200

axis2 = App.Vector(1, 1, 1)
point2 = App.Vector(3000, 0, 0)
place2 = App.Placement(point2, App.Rotation(axis2, 90))

proxy2 = Draft.make_workingplaneproxy(place2)
proxy2.ViewObject.DisplaySize = 3000
proxy2.ViewObject.ArrowSize = 200

workplane.setFromPlacement(proxy2.Placement, rebase=True)
Gui.Snapper.setGrid()

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WorkingPlaneProxy/pl
