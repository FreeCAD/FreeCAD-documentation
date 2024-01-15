# Body/pl
## Wprowadzenie

W programie FreeCAD słowo **Zawartość** jest zwykle używane w odniesieniu do obiektu [zawartości](PartDesign_Body/pl.md) środowiska Projekt Części *(klasa `PartDesign::Body`)*, który jest zdefiniowany przez środowisko [Projekt Części](PartDesign_Workbench/pl.md). Jest to obiekt kontenerowy, który może przechowywać [szkice 2D](Sketch/pl.md) i [przestrzenne cechy geometryczne](PartDesign_Feature/pl.md) w celu zbudowania bryły.

Zobacz stronę [Zawartość](PartDesign_Body/pl.md) środowiska Projekt Części, aby uzyskać więcej informacji na temat tego typu obiektu.



## Użycie

1.  Przełącz się na środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md)
2.  Naciśnij przycisk **[<img src=images/PartDesign_Body.svg style="width:16px"> [Stwórz zawartość](PartDesign_Body/pl.md)**.
3.  Naciśnij przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Nowy szkic](PartDesign_NewSketch/pl.md)**, aby utworzyć nowy [szkic](Sketch/pl.md).
4.  Utwórz zamkniętą linię, a następnie użyj narzędzia **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Wyciągnij](PartDesign_Pad/pl.md)**, aby wyciągnąć szkic i utworzyć bryłę wyjściową.
5.  Dodaj więcej szkiców i wyciągnięć oraz użyj innych narzędzi środowiska [Projekt Części](PartDesign_Workbench/pl.md), aby zmodyfikować i przekształcić początkową bryłę.

Alternatywnie, zamiast używać [szkicu](Sketch/pl.md), możesz dodać [cechę](PartDesign_Feature/pl.md) jako element pierwotny, na przykład **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Addytywny prostopadłościan](PartDesign_AdditiveBox/pl.md)**. Do stworzenia ostatecznej objętości można użyć dowolnej liczby cech addytywnych i subtraktywnych.



## Uwagi

Zawartość jest niezbędna podczas korzystania ze środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md) w metodologii [edycji cech](Feature_editing/pl.md).

Zawartość nie jest wymagana podczas używania środowiska pracy [Część](Part_Workbench/pl.md), ponieważ to środowisko używa przepływu pracy [konstrukcyjnej geometrii brył](Constructive_solid_geometry/pl.md), opartego na [kształtach pierwotnych](Part_Primitives/pl.md) i operacjach logicznych.


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Body/pl
