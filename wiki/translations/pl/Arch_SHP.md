# Arch SHP/pl
## Opis

FreeCAD jest w stanie importować [pliki typu shapefiles](https://en.wikipedia.org/wiki/Shapefile).

Importer korzysta z biblioteki shapefile.py ze strony <https://github.com/GeospatialPython/pyshp>. Jeśli nie zostanie ona znaleziona w systemie przy pierwszym uruchomieniu, importer zaproponuje jej pobranie i zainstalowanie.

Obiekty Shapefiles składają się z 3 plików *(.shp, .shx i .dbf)*, z których każdy może być używany z tym importerem. Zawierają one obiekty 2D jednego typu geometrii, które mogą być wielokątami/powierzchniami, poliliniami lub chmurami punktów *(wszystkie 3 typy są obsługiwane przez ten importer)*, oraz pola niestandardowe, dla których każda powierzchnia, polilinia lub punkt w pliku shapefile ma wartość. Jest to prawdziwy klejnot GIS, umożliwiający powiązanie bazy danych z geometrią. Najczęstszym zastosowaniem jest posiadanie jednego pola reprezentującego współrzędne wysokości każdego kształtu w pliku. Po otwarciu pliku importer zapyta, z którego pola pobrać wysokość kształtu.

Z każdego pliku kształtu w programie FreeCAD zostanie utworzony jeden kształt.

Należy zauważyć, że kwestia jednostek georeferencyjnych, przy setkach systemów projekcyjnych używanych na całym świecie, nie jest obecnie rozpatrywana. Współrzędne z pliku są używane w stanie „takim, jakim są".



## Powiązane

-   Ogłoszenie na forum FreeCAD [Shapefile Importer](https://forum.freecadweb.org/viewtopic.php?f=9&t=46150)
-   Dyskusja na forum [OSArch](https://community.osarch.org/discussion/comment/578#Comment_578)
-   [Import Eksport](Import_Export/pl.md)
-   [FreeCAD Jak importować eksportować](FreeCAD_Howto_Import_Export.md)
-   [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Arch SHP/pl
