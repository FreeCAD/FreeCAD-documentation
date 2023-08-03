---
 GuiCommand:
   Name: Image CreateImagePlane
   Name/pl: Obraz: Utwórz płaszczyznę obrazu
   MenuLocation: 
   Workbenches: Image_Workbench/pl
   SeeAlso: Image_Open/pl, Image_Scaling/pl
---

# Image CreateImagePlane/pl

## Opis

Narzędzie [Utwórz płaszczyznę obrazu](Image_CreateImagePlane/pl.md) importuje obraz [bitmapy](Bitmap/pl.md) i umieszcza go na jednej z płaszczyzn XY, YZ lub XZ.

## Użycie

1.  Naciśnij przycisk **<img src="images/Image_CreateImagePlane.svg" width=24px> [Utwórz płaszczyznę obrazu](Image_CreateImagePlane/pl.md)**.
2.  Wybierz żądany obraz z Twojego systemu.
3.  Wybierz płaszczyznę, na której zostanie umieszczony obraz, podaj wartość offsetu i naciśnij przycisk **OK**.

Wynikowy obiekt Płaszczyzny Obrazu wykorzystuje stosunek 1 piksela do 1 milimetra. Aby obraz był dobrze wyświetlany, powinien mieć wystarczającą rozdzielczość.

Podczas importowania obrazu możesz dodać odsunięcie o `-0.1mm`, aby umieścić obraz nieco za płaszczyzną roboczą. Ułatwi to śledzenie *(rysowanie na wierzchu)* obrazu za pomocą narzędzi [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownika](Sketcher_Workbench/pl.md).

Jeśli początkowo nie podano żadnego odsunięcia dla obrazka, jego pozycję można nadal korygować w [edytorze właściwości](Property_editor/pl.md).

## Właściwości


{{Properties_Title|Podstawowe}}

-    **Pozycja**: określa współrzędne punktu bazowego płaszczyzny obrazu.

-    **Kąt**: określa kąt obrotu płaszczyzny obrazu.

-    **Oś**: określa oś używaną dla kąta obrotu.


{{Properties Title|Płaszczyzna obrazu}}

-    **Obraz płaszczyzny**: określa obraz, który ma być użyty dla tej płaszczyzny.

-    **RozmiarX**: określa szerokość płaszczyzny obrazu.

-    **RozmiarY**: określa wysokość płaszczyzny obrazu.





{{Image Tools navi

}}



---
⏵ [documentation index](../README.md) > [Image](Image_Workbench.md) > Image CreateImagePlane/pl
