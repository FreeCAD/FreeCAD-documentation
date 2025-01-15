# Draft SVG/pl
## Opis

Draft SVG jest modułem oprogramowania używanym przez polecenia <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Otwórz](Std_Open/pl.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Importuj](Std_Import/pl.md) i <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Eksportuj](Std_Export/pl.md) do obsługi plików w formacie [SVG](SVG/pl.md).

![](images/Screenshot_inkscape.jpg ) 
*Rysunek Inkscape wyeksportowany do SVG, który jest następnie otwierany w FreeCAD.*



## Importowanie

Importowane mogą być następujące obiekty SVG:

-   obiekty ścieżki,
-   obiekty linii,
-   obiekty kwadratów,
-   Obiekty okręgów,
-   obiekty elips,
-   obiekty prostokątów,
-   obiekty polilinii.



## Ograniczenia

FreeCAD nie zaimportuje obiektów ścieżek, które mają tylko jeden punkt *([dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=43856))*.



## Eksportowanie

Eksportowane mogą być następujące obiekty FreeCAD:

-   Linie i polilinie,
-   łuki i okręgi,
-   ściany,
-   teksty,
-   wymiary.



## Ograniczenia 

SVG jest formatem 2D, więc wszystkie informacje o osi Z zostaną pominięte *(wszystkie obiekty zostaną spłaszczone)*.



## Obsługa jednostek 

Podczas eksportowania jednostka użytkownika *(px)* jest równa jednemu milimetrowi.

Podczas importowania przestrzegane są atrybuty szerokości, wysokości i viewBox. Wszystkie elementy są skalowane do ich rozmiaru w milimetrach, co jest wewnętrzną jednostką FreeCAD. Jeśli SVG nie zawiera informacji o jego fizycznym rozmiarze, przyjmuje się, że ma rozdzielczość 90 DPI. Należy unikać używania jednostek bezwzględnych w atrybutach wewnątrz SVG. Jednostki względne, takie jak em, ex i % nie są obecnie obsługiwane.

Edytor SVG [Inkscape](https://inkscape.org/) działa obecnie tylko z dokumentami o rozdzielczości 90 DPI. Nie ma znaczenia, która jednostka jest wybrana w Inkscape. Wszystkie dane wyjściowe muszą zostać przekonwertowane do 90 DPI i zaokrąglone do 6 miejsc po przecinku. Ponieważ FreeCAD *(i standard SVG)* jest niezależny od precyzji zaokrąglania wykonanego w Inkscape, wartości te nie będą zaokrąglane na wejściu. Nieparzyste wartości w milimetrach pozostaną. Jeśli import SVG nie ma być zaokrąglany, należy pracować na jednostkach użytkownika *(px)* w Inkscape. Skalowanie można wykonać po zaimportowaniu we FreeCAD lub poprzez zmianę atrybutów szerokości, wysokości i pola widoku.



## Ustawienia

Aby uzyskać więcej informacji zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby wyeksportować obiekty do SVG, użyj metody `export` modułu importSVG.


```python
importSVG.export(exportList, filename)
```

-   Dla systemu operacyjnego Windows: użyj **/** *(ukośnik do przodu)* jako separatora ścieżki w {{Incode|filename}}.

Przykład:


```python
import FreeCAD as App
import Draft
import importSVG

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importSVG.export(objects, "/home/user/Pictures/myfile.svg")
```



---
⏵ [documentation index](../README.md) > [File Formats](Category_File%20Formats.md) > [Draft](Draft_Workbench.md) > Draft SVG/pl
