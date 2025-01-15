# Draft OCA/de
## Beschreibung

Entwurf OCA ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open/de.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import/de.md) und <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export/de.md) Befehle, um das [OCA Dateiformat](http://groups.google.com/group/open_cad_format) zu verarbeiten.

Das OCA-Dateiformat ist eine Gemeinschaftsanstrengung zur Erstellung eines freien, einfachen und offenen CAD-Dateiformats. OCA basiert weitgehend auf dem GCAD-Dateiformat, das von [gCAD3D](http://www.gcad3d.org/) erzeugt wird. Beide Formate können in FreeCAD importiert werden, und die von FreeCAD exportierten OCA-Dateien können in gCAD3D geöffnet werden.



## Importieren

Die folgenden OCA-Objekte können importiert werden:

-   Linien
-   Bögen und Kreise
-   Geschlossene Flächenbereiche



## Exportieren

Die folgenden FreeCAD-Objekte können exportiert werden:

-   Linien und Drähte (Polylinien)
-   Bögen und Kreise
-   Flächen



## Einstellungen

Siehe [Import-Export-Einstellungen](Import_Export_Preferences/de.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um Objekte in eine OCA-Datei zu exportieren, wird die Methode `export` des Moduls importSVG verwendet.


```python
importOCA.export(exportList, filename)
```

-   Für Windows: **/** (forward slash) wird als Pfad-Trennzeichen in {{Incode|filename}} verwendet.

Beispiel:


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
⏵ [documentation index](../README.md) > [File Formats](Category_File%20Formats.md) > [Draft](Draft_Workbench.md) > Draft OCA/de
