# Draft OCA/de
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Beschreibung

Entwurf OCA ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open/de.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import/de.md) und <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export/de.md) Befehle, um das [OCA Dateiformat](http://groups.google.com/group/open_cad_format) zu verarbeiten.


<div class="mw-translate-fuzzy">

Das OCA Dateiformat ist eine Gemeinschaftsanstrengung zur Erstellung eines freien, einfachen und offenen CAD Dateiformats. OCA basiert weitgehend auf dem GCAD Dateiformat, das von [gCAD3D](http://www.gcad3d.org/) erzeugt wird. Beide Formate können in FreeCAD importiert werden, und die von FreeCAD exportierten OCA Dateien können in gCAD3D geöffnet werden.


</div>

## Importieren

Die folgenden OCA Objekte können importiert werden:

-   Linien
-   Bögen und Kreise
-   Geschlossene Flächen

## Exportieren

Die folgenden FreeCAD Objekte können exportiert werden:

-   Linien und Drähte (Polylinien)
-   Bögen und Kreise
-   Flächen

## Einstellungen


<div class="mw-translate-fuzzy">

Für weitere Informationen siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Scripting 


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripte](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Du kannst Elemente mit der folgenden Funktion nach OCA exportieren:


</div>


```python
importOCA.export(exportList, filename)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

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


<div class="mw-translate-fuzzy">





</div>


 

[Category:File Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OCA/de
