# Draft DXF/pl
{{TOCright}}

## Opis

Funkcja DXF, środowiska Rysunek Roboczy jest modułem oprogramowania używanym przez polecenia <img alt="" src=images/Std_Open.svg  style="width:24px;"> _ i <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Eksportuj](Std_Export/pl.md) do obsługi formatu pliku DXF.

![](images/Screenshot_qcad.jpg ) 
*Rysunek Qcad wyeksportowany do DXF, który jest następnie otwierany w programie FreeCAD*

## Importowanie

Dostępne są dwa importery, który z nich będzie używany można określić w menu **Edycja → Preferencje → Import/Eksport → DXF**: Pierwszy jest wbudowany, oparty na C++ i szybki, drugi jest starszy, zakodowany w Pythonie, wolniejszy i wymaga instalacji dodatku, ale czasami lepiej radzi sobie z niektórymi wystąpieniami obiektów i potrafi tworzyć bardziej dopracowane obiekty FreeCAD. Oba obsługują wszystkie wersje DXF począwszy od R12.

Bryły 3D wewnątrz pliku DXF są przechowywane w binarnym bloku ACIS/SAT, który w tej chwili nie może być odczytany przez FreeCAD.

### Importer C++ 

Można importować następujące obiekty DXF:

-   linie
-   polilinie *(oraz długie polilinie)*
-   okręgi
-   łuki
-   splajny
-   elipsy
-   warstwy
-   teksty i meta teksty
-   wymiary
-   bloki *(tylko geometria, teksty, wymiary i atrybuty wewnątrz bloków będą pomijane)*
-   punkty
-   obiekty odniesienia
-   obiekty przestrzeni papierowej

### Starszy importer 

Importer ten może importować następujące obiekty DXF:

-   linie
-   polilinie *(i lwpolilinie)*
-   łuki
-   okręgi
-   elipsy
-   splajny
-   ściany 3D
-   teksty i mteksty
-   linie odniesienia
-   warstwy

## Eksportowanie

Istnieją również dwa eksportery. Starszy eksporter eksportuje do formatu R12 DXF, a eksporter C++ do formatu R14 DXF. Oba formaty mogą być obsługiwane przez wiele aplikacji.

### Eksporter C++ 

Niektóre z cech i ograniczeń tego eksportera to:

-   Eksportowana jest cała geometria FreeCAD 2D, z wyjątkiem [Draft CubicBezCurves](Draft_CubicBezCurve/pl.md), [Draft BezCurves](Draft_BezCurve/pl.md) i [Draft Points](Draft_Point/pl.md).
-   Proste krawędzie z powierzchni obiektów 3D są eksportowane, ale krawędzie zakrzywione tylko wtedy, gdy leżą na płaszczyźnie równoległej do płaszczyzny XY globalnego układu współrzędnych. Należy pamiętać, że DXF utworzony z obiektów 3D będzie zawierał zduplikowane linie.
-   Teksty i wymiary nie są eksportowane.
-   Kolory są ignorowane.
-   Warstwy są mapowane na podstawie nazw obiektów.

### Starszy eksporter 

Niektóre z cech i ograniczeń tego eksportera to:

-   Eksportowana jest cała geometria FreeCAD 2D, z wyjątkiem [Punktów](Draft_Point/pl.md) środowiska Rysunek Roboczy. Jednak elipsy, krzywe złożone i krzywe Béziera nie są eksportowane poprawnie.
-   Obiekty 3D są eksportowane jako spłaszczony widok 2D,
-   Obiekty złożone są eksportowane jako bloki,
-   teksty,
-   Kolory w DXF są oparte na kolorze linii obiektów. Czarny jest mapowany do \"ByBlock\", inne kolory są mapowane przy użyciu kolorów indeksu kolorów AutoCAD Color Index *(ACI)*.
-   Warstwy są odwzorowywane na podstawie nazw grup. Gdy grupy są zagnieżdżone, najgłębsza grupa nadaje nazwę warstwy\'

## Instalacja

Z powodów licencyjnych, wymagane biblioteki importu/eksportu _.

## Ustawienia

Aby uzyskać więcej informacji zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md).

## DWG

Ponieważ format DWG jest prawnie zastrzeżonym, zamkniętym i nieudokumentowanym formatem, trudno jest go wspierać w projektach open-source takich jak FreeCAD. Dlatego też FreeCAD polega na zewnętrznych konwerterach do odczytu i zapisu plików DWG. Aby zaimportować plik DWG używa się konwertera, który najpierw tworzy plik DXF, który następnie może być przetworzony przez importer FreeCAD DXF. Podczas eksportowania do DWG następuje odwrotna konwersja: DXF utworzony przez eksporter FreeCAD DXF jest zamieniany w DWG.

Należy pamiętać, że format DXF umożliwia konwersję 1:1 formatu DWG. Wszystkie aplikacje, które mogą odczytywać i zapisywać pliki DWG, mogą to samo robić z plikami DXF, bez utraty danych. Tak więc prośba o pliki DXF zamiast plików DWG, a następnie dostarczenie plików DXF z kolei, nie powinna powodować żadnych problemów.

Wbudowane jest wsparcie dla następujących konwerterów DWG:

-   [LibreDWG](https://www.gnu.org/software/libredwg) *(open-source, brak obsługi niektórych elementów DWG)*.
-   [Konwerter plików ODA](https://www.opendesign.com/guestfiles/oda_file_converter) *(bezpłatny)*.
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) *(komercyjny)*. {{Version/pl|0.20}}

Zobacz strony [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DWG.md) i [FreeCAD i import DWG](FreeCAD_and_DWG_Import/pl.md), aby uzyskać więcej informacji.

## Tworzenie skryptów 

Zobacz również: _.

Do eksportu obiektów do DXF użyj metody `export` modułu importDXF.


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   Dla systemu operacyjnego Windows: użyj {{FileName|/}} *(ukośnik do przodu)* jako separatora ścieżki w {{Incode|filename}}.

Przykład:


```python
import FreeCAD as App
import Draft
import importDXF

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```





 

_

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/pl
