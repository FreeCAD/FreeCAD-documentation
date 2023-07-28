# Image Workbench/pl
**Środowisko pracy '''Obraz''' nie jest już dołączone po wersji 0.20.<br>
Jego funkcjonalność została zintegrowana w [Narzędziach podstawowych](Std_Base/pl.md). Zobacz strony[Std: Import](Std_Import/pl.md) i [Std: Otwórz widok obrazu](Std_ViewLoadImage/pl.md).**

<img alt="Ikonka FreeCAD dla Środowiska pracy Obraz" src=images/Workbench_Image.svg  style="width:128px;">


{{TOCright}}



## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Image.svg  style="width:24px;"> [Obraz](Image_Workbench/pl.md) zarządza różnymi typami plików graficznych [bitmap](bitmap/pl.md) i umożliwia ich otwarcie w programie FreeCAD.



## Przybory

-   <img alt="" src=images/Image_Open.svg  style="width:32px;"> [Otwórz widok obrazu](Image_Open/pl.md): otwórz obraz na nowej rzutni.
-   <img alt="" src=images/Image_CreateImagePlane.svg  style="width:32px;"> [Tworzy płaski obraz w przestrzeni 3D](Image_CreateImagePlane/pl.md): zaimportuj obraz do płaszczyzny w widoku 3D.
-   <img alt="" src=images/Image_Scaling.svg  style="width:32px;"> [Skaluje płaszczyznę obrazu \...](Image_Scaling/pl.md): skalowanie zaimportowanego obrazu do płaszczyzny.



## Funkcje

-   Podobnie jak w [Szkicowniku](Sketcher_Workbench/pl.md), importowany obraz może być dołączony do jednej z głównych płaszczyzn XY, XZ lub YZ, i może mieć dodatnią lub ujemną wartość odsunięcia.
-   Obraz jest importowany z zależnością 1 piksel na 1 milimetr.
-   Zaleca się, aby importowany obraz miał rozsądną rozdzielczość.



## Przepływ pracy 

Głównym zastosowaniem tego środowiska pracy jest tworzenie bryły na podstawie konturów obrazu za pomocą narzędzi środowisk [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md).

Operacja rysowania po obrazie działa najlepiej, jeśli obraz ma niewielkie ujemne odsunięcie, na przykład -0,1 mm, w stosunku do płaszczyzny roboczej. Oznacza to, że obraz będzie znajdował się nieco za płaszczyzną, na której rysujesz geometrię 2D, więc nie będziesz rysował na powierzchni samego obrazu.

Odsunięcie obrazu może być ustawione podczas importu lub zmienione później poprzez jego właściwości.





{{Image Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Image](Category_Image.md) > Image Workbench/pl
