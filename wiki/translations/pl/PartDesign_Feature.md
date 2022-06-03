# PartDesign Feature/pl
## Wprowadzenie

[Cecha](PartDesign_Feature/pl.md) odnosi się do \"kroku\" w procesie modelowania, który dzieje się wewnątrz [zawartości projektu części](PartDesign_Body/pl.md). Na przykład, za każdym razem kiedy dodajesz sześcian opcją [Addytywny sześcian](PartDesign_AdditiveBox/pl.md), dodajesz cechę, kiedy dodajesz fazkę do krawędzi opcją [Fazka](PartDesign_Chamfer/pl.md), dodajesz kolejną cechę. Kiedy wycinasz otwór używając [szkicu](Sketch/pl.md) i opcji [kieszeń](PartDesign_Pocket/pl.md), dodajesz inną cechę.

<img alt="" src=images/PartDesign_Feature_example.png  style="width   *600px;"> 
*Edycja elementu w [Zawartości Projektu części](PartDesign_Body/pl.md) z trzema kolejnymi elementami.*

Istnieje wiele rodzajów cech, które mogą dodawać lub usuwać objętość z bryły początkowej. Słowo \"cecha\" odnosi się do samej operacji, jak również do bryły powstałej po tej operacji.

Aby dowiedzieć się więcej o możliwości tworzenia obiektów bryłowych za pomocą środowiska [Projekt części](PartDesign_Workbench/pl.md) zobacz stronę [edycja cech](Feature_editing/pl.md).

## Użycie

Prawie wszystkie narzędzia środowiska pracy [Projekt części](PartDesign_Workbench/pl.md) są przeznaczone do dodawania cech do [zawartości projektu części](PartDesign_Body/pl.md). Narzędzia te mogą być dostępne z menu i przycisków paska narzędzi, gdy obiekt lub element podrzędny *(wierzchołek, krawędź, ściana)* jest zaznaczony.

Cechy mogą być umieszczone w różnych kategoriach   *

-   Cechy bazowe   * odnosi się do obiektu Cecha bazowa, który może być utworzony w [zawartości Projektu części](PartDesign_Body/pl.md)
-   addytywne i subtraktywne
    -   Kształty pierwotne   * [sześcian](PartDesign_AdditiveBox/pl.md), [stożek](PartDesign_AdditiveCone/pl.md), [walec](PartDesign_AdditiveCylinder/pl.md), [elipsoida](PartDesign_AdditiveEllipsoid/pl.md), [graniastosłup](PartDesign_AdditivePrism/pl.md), [sfera](PartDesign_AdditiveSphere/pl.md), [torus](PartDesign_AdditiveTorus/pl.md), oraz [klin](PartDesign_AdditiveWedge/pl.md).
    -   Pierwotne kształty odejmowalne   * [Subtraktywny sześcian](PartDesign_SubtractiveBox/pl.md), [Subtraktywny stożek](PartDesign_SubtractiveCone/pl.md), [Subtraktywny walec](PartDesign_SubtractiveCylinder/pl.md), [Subtraktywna elipsoida](PartDesign_SubtractiveEllipsoid/pl.md), [Subtraktywny Pgraniastosłup](PartDesign_SubtractivePrism/pl.md), [Subtraktywna sfera](PartDesign_SubtractiveSphere/pl.md), [Subtraktywny torus](PartDesign_SubtractiveTorus/pl.md), i [Subtraktywny klin](PartDesign_SubtractiveWedge/pl.md).
    -   Oparte na profilu   * [wyciągnięcie](PartDesign_Pad/pl.md), [wyciągnięcie przez obrót](PartDesign_Revolution/pl.md), [wyciągnięcie przez profile](PartDesign_AdditiveLoft/pl.md), [wyciągnięcie po ścieżce](PartDesign_AdditivePipe/pl.md).
    -   Profilowanie odejmowalne   * [kieszeń](PartDesign_Pocket/pl.md), [otwór](PartDesign_Hole/pl.md), [rowek](PartDesign_Groove/pl.md), [Subtraktywne wyciągnięcie przez profile](PartDesign_SubtractiveLoft/pl.md), [Subtraktywne wyciągnięcie po ścieżce](PartDesign_SubtractivePipe/pl.md).
-   [funkcje logiczne](PartDesign_Boolean/pl.md), w tym łączenie, cięcie i część wspólna.
-   Ulepszenia
    -   [fazka](PartDesign_Chamfer/pl.md)
    -   [rysunek roboczy](PartDesign_Draft/pl.md)
    -   [zaokrąglenie](PartDesign_Fillet/pl.md)
    -   [grubość](PartDesign_Thickness/pl.md)
-   Transformacja.
    -   [szyk liniowy](PartDesign_LinearPattern/pl.md)
    -   [odbicie lustrzane](PartDesign_Mirrored/pl.md)
    -   [transformacja wielokrotna](PartDesign_MultiTransform/pl.md)
    -   [szyk kołowy](PartDesign_PolarPattern/pl.md)
    -   [skalowanie](PartDesign_Scaled/pl.md)

## Dziedziczenie

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami programu. Obiekty `PartDesign   *   *Feature* są używane do budowania parametrycznych brył 3D, a więc pochodzą z podstawowego obiektu {{incode|Part   *   *Feature`..}}

## Tworzenie skryptów 


**Zobacz również   ***

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty tworzone skryptami](Scripted_objects/pl.md).

Zobacz stronę [cechy części](Part_Feature/pl.md), aby uzyskać ogólne informacje na temat dodawania obiektów z [konsoli Python](Python_console/pl.md).

Zobacz stronę [zawartość Projektu części](PartDesign_Body/pl.md) aby uzyskać ogólne informacje na temat dodawania Zawartości. Gdy istnieje już bryła, można do niej dołączyć cechy za pomocą metody `addObject()` tej bryły.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign   *   *Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign   *   *AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign   *   *SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/pl
