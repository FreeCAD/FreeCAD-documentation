








{{TOCright}}

## Opis

Funkcja DXF, środowiska Rysunek Roboczy jest modułem oprogramowania używanym przez polecenia <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Otwórz](Std_Open/pl.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Importuj](Std_Import/pl.md) i <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Eksportuj](Std_Export/pl.md) do obsługi formatu pliku DXF.

![](images/Screenshot_qcad.jpg ) *Rysunek Qcad wyeksportowany do DXF, który jest następnie otwierany w programie FreeCAD*

## Importowanie

Importer posiada dwa tryby pracy, konfigurowane w menu **Edycja → Preferencje → Import/Eksport → DXF**: Pierwszy jest wbudowany, oparty na C++ i szybki, drugi jest starszy, zakodowany w Pythonie, wolniejszy i wymaga instalacji dodatku, ale czasami lepiej radzi sobie z niektórymi wystąpieniami obiektów i potrafi tworzyć bardziej dopracowane obiekty FreeCAD. Oba obsługują wszystkie wersje DXF począwszy od R12.

Obiekty 3D wewnątrz pliku DXF są przechowywane w binarnym bloku ACIS/SAT, który w tej chwili nie może być odczytany przez FreeCAD. Prostsze obiekty, takie jak 3DFACE, są jednak obsługiwane.

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

## Eksportowanie

Pliki są eksportowane w formacie R14 DXF, który może być obsługiwany przez wiele aplikacji.

Można eksportować następujące obiekty FreeCAD:

-   cała geometria 2D FreeCAD, taka jak obiekty środowiska Rysunek Roboczy lub Szkicownik,
-   Obiekty 3D są eksportowane jako spłaszczony widok 2D,
-   Obiekty złożone są eksportowane jako bloki,
-   teksty,
-   kolory są odwzorowywane z obiektów, kolory RGB na indeks kolorów autocad *(ACI)*. Czarny będzie zawsze \"według warstwy\"\'
-   warstwy są odwzorowywane na podstawie nazw grup. Gdy grupy są zagnieżdżone, najgłębsza grupa nadaje nazwę warstwy\'
-   wymiary, które są eksportowane ze stylem wymiarowania \"Standard\".

## Instalacja

Z powodów licencyjnych, wymagane biblioteki importu/eksportu [DXF](DXF/pl.md) potrzebne dla starszej wersji importera, nie są częścią kodu źródłowego programu FreeCAD. Aby uzyskać więcej informacji zobacz stronę: [FreeCAD i import DXF](FreeCAD_and_DXF_Import/pl.md).

## Ustawienia

Aby uzyskać więcej informacji zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md).

## Pisanie skryptów 


**Zobacz również:**

[Skrypty dla środowiska Rysunek Roboczy](Draft_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Elementy można eksportować do DXF za pomocą następującej funkcji: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Przykład: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```





 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
