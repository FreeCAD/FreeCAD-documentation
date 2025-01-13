---
 GuiCommand:
   Name: TechDraw CosmeticCircle
   Name/pl: Rysunek Techniczny Okrąg kosmetyczny
   MenuLocation: Rysunek Techniczny , Dodaj linie , Dodaj okrąg kosmetyczny
   Workbenches: TechDraw_Workbench/pl
   Version: 1.0
   SeeAlso: TechDraw_2PointCosmeticLine/pl
---

# TechDraw CosmeticCircle/pl



## Opis

Narzędzie **Dodaj okrąg kosmetyczny** dodaje okrąg kosmetyczny w wybranym punkcie środka. Punkt może znajdować się w przestrzeni 2D lub 3D.

<img alt="" src=images/CosmeticCircleSample.png  style="width:200px;">



*Geometria okręgu pomocniczego*



## Użycie

1.  Wybierz punkt środkowy w widoku rysunku technicznego lub w oknie [Widoku 3D](3D_view/pl.md).
2.  Jeśli wybrałeś punkt w widoku 3D: dodaj właściwy widok Rysunku Technicznego do zaznaczenia, wybierając go w oknie [Widoku drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_CosmeticCircle.svg" width=16px> '''Dodaj okrąg kosmetyczny'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Dodaj linie → <img src="images/TechDraw_CosmeticCircle.svg" width=16px> Dodaj okrąg kosmetyczny**.
4.  Otworzy się panel zadań.
5.  Opcjonalnie dostosuj współrzędne punktu środkowego, promień oraz kąt rozpoczęcia i zakończenia okręgu.
6.  Naciśnij przycisk **OK**.
7.  Zostanie dodana geometria okręgu pomocniczego. W przypadku punktu środkowego 3D okrąg jest umieszczany na rzucie punktu.



## Edycja

Aby zmienić atrybuty okręgu kosmetycznego:

1.  Wybierz geometrię okręgu kosmetycznego.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_CosmeticCircle.svg" width=16px> '''Dodaj okrąg kosmetyczny'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Dodaj linie → <img src="images/TechDraw_CosmeticCircle.svg" width=16px> Dodaj okrąg kosmetyczny.**.
3.  Otworzy się panel zadań.
4.  Dostosuj współrzędne punktu środkowego, promień lub kąt początkowy i końcowy okręgu.
5.  Naciśnij przycisk **OK**.



## Uwagi

-   Aby usunąć okrąg kosmetyczny, zaznacz go i naciśnij **Delete**.
-   Aby zmienić wygląd okręgu kosmetycznego, użyj narzędzia <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [Zmień wygląd linii](TechDraw_DecorateLine/pl.md).



## Właściwości

Okręgi kosmetyczne nie mają własnych właściwości, ponieważ nie są obiektami dokumentu.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Okręgi kosmetyczne mogą być tworzone przy użyciu metody DrawViewPart {{Incode|makeCosmeticCircle(center, radius, start angle, end angle)}}.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticCircle/pl
