# Copying Objects/pl
{{TOCright}}

## Informacje ogólne 

Podobnie jak wiele innych programów komputerowych FreeCAD posiada możliwość wycinania, kopiowania i wklejania obiektów. Obiekty [dokumentu](Document_structure/pl.md) mogą być dowolnie kopiowane w obrębie dokumentu lub pomiędzy dokumentami za pomocą funkcji <img alt="" src=images/Std_Copy.svg  style="width   *24px;"> [Kopiuj](Std_Copy/pl.md), <img alt="" src=images/Std_Paste.svg  style="width   *24px;"> [Wklej](Std_Paste/pl.md) i [Powiel zaznaczone](Std_DuplicateSelection/pl.md).

![](images/Copy_past_duplicate.png )

Proszę wziąć pod uwagę, że skopiowane obiekty nie są zależne od oryginału. Jeśli chcesz mieć zależne klony, użyj funkcji <img alt="" src=images/Draft_Clone.svg  style="width   *24px;"> [Rysunek Roboczy   * Klonuj](Draft_Clone/pl.md) lub <img alt="" src=images/PartDesign_Clone.svg  style="width   *24px;"> [Projekt Części   * Utwórz klona](PartDesign_Clone/pl.md). Jeśli nie potrzebujesz ani klonu zależnego, ani repliki parametrycznej, możesz również użyć <img alt="" src=images/Part_SimpleCopy.svg  style="width   *24px;"> [Część   * Szybka kopia](Part_SimpleCopy/pl.md). Jeśli chodzi o klony wzorcowe, zajrzyj do sekcji [inne metody](Copying_Objects/pl#Inne_metody.md) na tej stronie.

## Kopiowanie obiektów powiązanych 

Jeśli obiekt, który ma zostać skopiowany, ma powiązania z obiektem *(obiektami)*, które nie znajdują się w zaznaczeniu, FreeCAD zapyta, czy niewybrane obiekty powinny zostać uwzględnione w operacji kopiowania.

## Znajdowanie i pozycjonowanie wklejonych obiektów 

Po operacji kopiuj - wklej może nie być oczywiste, gdzie znajdują się nowe obiekty w oknie [widoku 3D](3D_view/pl.md). Dzieje się tak, ponieważ nowe obiekty mają tę samą właściwość [Umiejscowienie](Placement/pl.md), co ich oryginały. Przełącz właściwość Widoczność *(klawiszem **Spacja**)*, aby ukryć oryginały, a następnie przesuń kopie do ich właściwej pozycji, na przykład używając narzędzia <img alt="" src=images/Std_TransformManip.svg  style="width   *24px;"> [Przemieszczenie](Std_TransformManip/pl.md) lub <img alt="" src=images/Std_Placement.svg  style="width   *24px;"> [Umiejscowienie](Std_Placement/pl.md).

## Inne metody 

Podobnie jak w przypadku większości rzeczy w programie FreeCAD, istnieje wiele sposobów utworzenia kopii. Więcej pomysłów znajdziesz na stronach   *

-   Projekt Części   * [Odbicie lustrzane](PartDesign_Mirrored/pl.md), [Szyk liniowy](PartDesign_LinearPattern/pl.md), [Szyk kołowy](PartDesign_PolarPattern/pl.md), [Transformacja wielokrotna](PartDesign_MultiTransform/pl.md)
-   Część   * [Odbicie lustrzane](Part_Mirror/pl.md), [Szybka kopia](Part_SimpleCopy/pl.md)
-   Rysunek Roboczy   * [Odsunięcie](Draft_Offset/pl.md), [Skaluj](Draft_Scale/pl.md), [Szyk ortogonalny](Draft_OrthoArray/pl.md), [Szyk po ścieżce](Draft_PathArray/pl.md), [Klonuj](Draft_Clone/pl.md), [Odbicie lustrzane](Draft_Mirror/pl.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > Copying Objects/pl
