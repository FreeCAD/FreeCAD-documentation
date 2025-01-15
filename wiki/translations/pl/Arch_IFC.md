# Arch IFC/pl
## Opis

Środowisko pracy <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [Build Information Modeling *(BIM)*](BIM_Workbench/pl.md) natywnie wspiera pliki [Industry Foundation Classes *(IFC)*](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) i posiada importer oraz eksporter. Format IFC jest stale rozwijanym, powszechnym formatem wymiany danych pomiędzy aplikacjami [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling), stosowanymi w architekturze i inżynierii.

Przeczytaj więcej o obsłudze plików IFC w FreeCAD na stronie [Natywne IFC](NativeIFC/pl.md).

#### IfcOpenShell

Cała funkcjonalność IFC zależy od biblioteki [IfcOpenShell](http://ifcopenshell.org), która może, ale nie musi być dołączona do Twojej wersji FreeCAD. Łatwym sposobem sprawdzenia, czy IfcOpenShell jest dostępny jest wprowadzenie następującej informacji w [konsoli Python](Python_console.md):


```python
import ifcopenshell
```

Jeśli nie pojawi się żaden komunikat o błędzie, wszystko jest w porządku, IfcOpenShell jest zainstalowany i możesz przystąpić do [otwierania](Std_Open/pl.md) plików IFC. W przeciwnym razie, będziesz musiał sam zainstalować IfcOpenShell. Przeczytaj stronę [IfcOpenShell](IfcOpenShell/pl.md), aby dowiedzieć się więcej o tym procesie.


**Uwaga:**

Narzędzie **[<img src=images/BIM_Setup.svg style="width:16px"> [BIM Setup](BIM_Setup.md)** również będzie poszukiwać IfcOpenShell i wyświetli powiadomienie, jeśli nie jest on zainstalowany.



## Otwieranie i importowanie 

Począwszy od wersji 1.0, FreeCAD otwiera i importuje pliki IFC natywnie. Przeczytaj więcej na stronie [Natywne IFC](NativeIFC/pl.md).



### Starsze importery 



#### Importer Arch 

Oryginalny importer IFC ze środowiska pracy Arch został wyłączony w FreeCAD w wersji 1.0, ale nadal jest dostępny z Pythona:


```python
from importers import importIFC
importIFC.open("C:\\Path\\To\\My\\File.ifc")
```

Wszystkie elementy [IfcProduct](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifckernel/lexical/ifcproduct.htm) z plików IFC2x3 lub IFC4 będą importowane do dokumentu FreeCAD. Ustawienia preferencji IFC pozwalają na określenie sposobu importowania obiektów IFC:

-   **pełne parametryczne obiekty Arch**, *(geometria będzie, w miarę możliwości, edytowalna w FreeCAD)*,
-   **nieparametryczne obiekty Arch**, *(obiekty będą posiadać informacje IFC i właściwości, ale nie będą edytowalne)*,
-   *\'nieparametryczne kształty części*,\' *(geometria będzie wiernie oddana, ale informacje IFC zostaną odrzucone)*,
-   **jeden kształt części na piętro**, *(jeden obiekt typu „wszystko w jednym", tylko w celach informacyjnych)*.

Każdy z tych typów traci pewne informacje w stosunku do poprzedniego, ale jest lżejszy od zasobów, co pozwala na otwieranie większych plików. Ostatni typ pozwala na całkowite odrzucenie importu obiektów Arch, co jest przydatne w modelach analityki strukturalnej.

Zazwyczaj, jeśli próbujesz otworzyć duży plik, a import do FreeCAD trwa zbyt długo, spróbuj użyć niższego trybu importu.

IfcOpenShell obsługuje wszystkie encje IFC2x3 i IFC4 *(IFC4-add1 i IFC4-add2 są implementowane w v0.6 i mogą być dostępne do czasu, kiedy to przeczytasz)*, ale nie wszystkie z nich mogą być przekonwertowane na obiekty [BIM](BIM_Workbench/pl.md), te, które nie mogą, zostaną importowane jako proste kształty [Część](Part_Workbench/pl.md). Importer IFC rozpoczyna od importowania wszystkich elementów IFC pochodzących z [IfcProduct](http://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm), czyli w zasadzie wszystkich obiektów, które składają się na budynek, takich jak ściany, okna lub rury. Wszystkie inne elementy wymagane przez jeden z tych obiektów, takie jak profile wyciągnięcia lub komponenty operacji logicznych, zostaną zaimportowane zgodnie z wymaganiami.

W przypadku zastosowania trybu importu wykorzystującego obiekty Arch, parametrycznego lub nie, wszystkie obiekty będą posiadały pełny zestaw [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) dołączony do każdego obiektu, pogrupowany według zestawu właściwości.

Konstrukcje budowlane takie jak witryny, budynki i kondygnacje są również wiernie importowane, a ich struktura jest prawidłowo odtworzona w programie FreeCAD. Konstrukcje grupowe *(przy użyciu IfcGroups)* są również importowane i renderowane w FreeCAD i mogą być łączone z konstrukcjami budowlanymi, np. posiadającymi grupy wewnątrz pięter lub kondygnacji wewnątrz grup.

Importowane są również obiekty [IfcAnnotation](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcproductextension/lexical/ifcannotation.htm), jak również obiekty liniowe i oparte na krzywych elementy [IfcStructuralItem](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralitem.htm).

Ilości określone w pliku IFC są importowane w formacie **NOT**. Ponieważ jednak geometria jest w pełni odtworzona w FreeCAD, większość wielkości takich jak długość, powierzchnia itp. jest łatwo dostępna dla każdego z obiektów.

Włączenie w ustawieniach preferencji IFC opcji **pokaż komunikaty o błędach** spowoduje wyświetlenie raportu informującego, czy jakiś obiekt z pliku IFC nie został zaimportowany.

Uwaga: Środowisko pracy BIM posiada narzędzie [IFC explorer](BIM_IfcExplorer.md), które pozwala na szybkie otwieranie pliku IFC w trybie tekstowym i importowanie tylko wybranych części.



#### Stary importer 

W przeszłości, w środowisku pracy Arch znajdował się prostszy importer IFC, który nie był zależny od IfcOpenShell. Ten starszy moduł jest nadal zawarty w kodzie źródłowym i dostępny z poziomu Pythona, ale nie jest w ogóle zalecany. Będzie mógł importować tylko bardzo mały podzbiór obiektów IFC i powinien być uznany za całkowicie przestarzały.

Stary importer jest dostępny z poziomu Pythona:


```python
from importers import importIFClegacy
importIFClegacy.open("C:\\Path\\To\\My\\File.ifc")
```



## Eksportowanie

Eksport do plików IFC wykona wyeksportowanie wszystkich wybranych obiektów i ich potomków. Obsługiwane są wszystkie obiekty Arch/BIM, jak również inne obiekty utworzone w innych Środowiskach pracy. Jedynymi nie w pełni obsługiwanymi obiektami są obecnie elementy **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Bodies](PartDesign_Body.md)**, **[<img src=images/Std_Part.svg style="width:16px"> [Std Parts](Std_Part.md)**, oraz nowe struktury, takie jak **[<img src=images/Link.svg style="width:16px"> [App: Links](Std_LinkMake.md)** i **[<img src=images/LinkGroup.svg style="width:16px"> LinkGroups**, więc trzeba będzie trochę przetestować ich użycie. [Arch: References](Arch_Reference.md) będzie obecnie eksportowane jako `IfcBuildingElementProxies`.

Aby wyeksportować cały obiekt lub budynek albo całe piętro lub grupę zawierającą inne obiekty, wystarczy wybrać tylko ten budynek lub piętro lub grupę. Obiekty Arch będą eksportowane z ustawionym typem we właściwości **Typ IFC**. Eksportowane są również ich [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm), a jeżeli obiekty te mają IFC UID z poprzedniego importu, to ten sam UID zostanie zachowany przy eksporcie. Obiekty, które nie są obiektami typu Arch, są eksportowane jako [IfcBuildingElementProxy](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcsharedbldgelements/lexical/ifcbuildingelementproxy.htm).

Pliki IFC są eksportowane jako IFC2x3 lub IFC4 w zależności od wersji programu IfcOpenShell, który może być skompilowany z dowolnym schematem IFC. Jeśli używasz IfcOpenShell v0.6 lub wyższej, zostanie użyta wersja IFC określona w preferencjach Arch.

Jeśli kształt eksportowanych obiektów opiera się na wyciskaniu lub operacji logicznej, operacja i komponenty zostaną poprawnie wyeksportowane do IFC. Jeśli nie, kształt obiektu jest eksportowany jako [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4x1/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm). Jeśli kształt zawiera krzywe, to będą one triangulowane. W przypadku IfcOpenShell v0.5 lub nowszych jest jednak dostępny serializer, który musi być włączony w preferencjach Import/Export → IFC. Jeśli opcja ta jest włączona, serializer może eksportować bardzo złożone obiekty krzywe, takie jak te oparte na NURBS, a tym samym unikać powierzchni triangulowanych. Jednak w momencie pisania tego tekstu niewiele innych aplikacji BIM obsługuje obiekty IFC NURBS, dlatego zaleca się trochę testów.



## Informacje dodatkowe 

-   [IfcOpenShell](IfcOpenShell.md), więcej informacji na temat instalacji tej biblioteki.



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [BIM](Category_BIM.md) > Arch IFC/pl
