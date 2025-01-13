# <img alt="Ikonka FreeCAD dla zewnętrznego środowiska pracy DynamicData" src=images/DynamicData_workbench_icon.svg  style="width:64px;"> DynamicData Workbench/pl






## Informacje ogólne 

DynamicData to [zewnętrzne środowisko pracy](External_workbenches/pl.md), za pomocą którego można utworzyć obiekt kontenera do przechowywania niestandardowych właściwości.

Za pomocą tego środowiska pracy można utworzyć nową niestandardową [właściwość](Property/pl.md) dowolnego typu obsługiwanego przez FreeCAD. Na przykład właściwość Length lub [umiejscowienie](Placement/pl.md). Te niestandardowe właściwości mogą być następnie używane w [Wyrażeniach](Expressions/pl.md) tak jak każda inna właściwość. Na przykład można utworzyć właściwość Length o nazwie \"Szerokość\" i odwoływać się do niej podczas związania elementu szkicu. Następnie, gdy właściwość \"Szerokość\" zostanie zmieniona, wiązanie szkicu zostanie automatycznie zaktualizowane. Jest to podobne do sposobu, w jaki można korzystać z arkusza kalkulacyjnego, ale jest bardziej interaktywne, ponieważ właściwości mogą być zmieniane przy jednoczesnym zachowaniu [widoku 3D](3D_view/pl.md), a także pozwala na szerszą gamę typów właściwości.

Niektóre funkcje obejmują:

-   Możliwość importowania nazwanych więzów ze szkicu.
-   Możliwość kopiowania właściwości lub ustawiania wartości właściwości z jednego obiektu do drugiego.
-   Obiekty kontenerowe pozostają kompatybilne z instalacjami FreeCAD, które nie mają zainstalowanego środowiska roboczego.



## Instalacja

To środowisko robocze można zainstalować z [Menedżera dodatków](Std_AddonMgr/pl.md). W celu ręcznej instalacji zobacz poradnik [Instalacja większej ilości środowisk pracy](Installing_more_workbenches/pl.md).



## Odnośniki internetowe 

-   Kod źródłowy hostowany w GitHub: [github.com](https://github.com/mwganson/DynamicData)
-   Oficjalna pełna dokumentacja [1](https://github.com/mwganson/DynamicData/blob/master/README.md)



## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe środowiska pracy wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > DynamicData Workbench/pl
