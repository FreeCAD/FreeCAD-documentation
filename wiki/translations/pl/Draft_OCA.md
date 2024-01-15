# Draft OCA/pl
## Opis

Draft OCA jest modułem oprogramowania używanym przez <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std: Otwórz](Std_Open/pl.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std: Importuj](Std_Import/pl.md) i <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std: Eksportuj](Std_Export/pl.md) polecenia do obsługi formatu pliku [OCA](http://groups.google.com/group/open_cad_format).

Format pliku OCA to wysiłek społeczności mający na celu stworzenie bezpłatnego, prostego i otwartego formatu pliku CAD. OCA jest w dużej mierze oparty na formacie pliku GCAD wygenerowanym z [gCAD3D](http://www.gcad3d.org/). Oba formaty mogą być importowane do FreeCAD, a pliki OCA eksportowane przez FreeCAD mogą być otwierane w gCAD3D.



## Importowanie

Importowane mogą być następujące obiekty OCA:

-   linie,
-   łuki i okręgi,
-   obszary zamknięte.



## Eksportowanie

Eksportowane mogą być następujące obiekty FreeCAD:

-   linie i polilinie,
-   łuki i okręgi,
-   ściany.



## Ustawienia

Aby uzyskać więcej informacji zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Do eksportu obiektów do DXF użyj metody `export` modułu importOCA.


```python
importOCA.export(exportList, filename)
```

-   Dla systemu operacyjnego Windows: użyj **/** *(ukośnik do przodu)* jako separatora ścieżki w {{Incode|filename}}.

Przykład:


```python
import FreeCAD as App
import Draft
import importOCA

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importOCA.export(objects, "/home/user/Pictures/myfile.oca")
```



---
⏵ [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft OCA/pl
