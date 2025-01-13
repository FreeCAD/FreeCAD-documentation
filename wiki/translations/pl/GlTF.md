# GlTF/pl
## Opis

[GL Transmission Format](https://www.khronos.org/gltf/) *(glTF™)* to nieodpłatna specyfikacja wydajnego przesyłania i ładowania scen i modeli 3D przez aplikacje. Minimalizuje zarówno rozmiar zasobów 3D, jak i przetwarzanie w czasie wykonywania potrzebne do rozpakowania i wykorzystania tych zasobów.



## Instalacja

Zgodnie z tym [wątkiem na forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=31680&p=450917&#p450658), OCC musi zostać skompilowane z obsługą RapidJSON, aby móc korzystać z funkcji glTF. Dlatego należy ustawić opcję `USE_RAPIDJSON` w kroku konfiguracji CMake. Wymaga to pakietu rapidjson-dev.



## Importowanie

Obecnie nie jest obsługiwany przez FreeCAD.



## Eksportowanie

Od wersji FreeCAD 0.19.23074 polecenie [Std Eksport](Std_Export/pl.md) może eksportować również do formatu gITF.



### Alternatywne rozwiązania eksportu 

W przypadku wcześniejszych wersji można zastosować te obejścia:

1\. Eksportuj jako STEP → Importuj do CAD Assistant z Opencascade -\> Eksportuj do glTF.

lub

2\. Użyj biblioteki Python `cqparts` *([strona domowa](https://github.com/cqparts/cqparts))*: {{code|
import cqparts
cqparts.Assembly.importer('step')('myfile.stp').exporter('gltf')('myfile.gltf')
}}

Żródło: [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=31680&p=449977#p449977).



## Powiązane

-   [Import Eksport](Import_Export/pl.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export/pl.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > GlTF/pl
