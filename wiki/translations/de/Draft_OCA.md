# Draft OCA/de







<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Beschreibung

Entwurf OCA ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open/de.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import/de.md) und <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export/de.md) Befehle, um das [OCA Dateiformat](http://groups.google.com/group/open_cad_format) zu verarbeiten.

Das OCA Dateiformat ist eine Gemeinschaftsanstrengung zur Erstellung eines freien, einfachen und offenen CAD Dateiformats. OCA basiert weitgehend auf dem GCAD Dateiformat, das von [gCAD3D](http://www.gcad3d.org/) erzeugt wird. Beide Formate können in FreeCAD importiert werden, und die von FreeCAD exportierten OCA Dateien können in gCAD3D geöffnet werden.

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

Für weitere Informationen siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).

## Scripting


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripte](FreeCAD_Scripting_Basics/de.md).

Du kannst Elemente mit der folgenden Funktion nach OCA exportieren: 
```python
importOCA.export(exportList, filename)
```

Beispiel: 
```python
import FreeCAD, Draft, importOCA

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(1000, 1000, 0)
p3 = FreeCAD.Vector(2200, 1500, 0)
p4 = FreeCAD.Vector(2500, -100, 0)

obj1 = Draft.makeWire([p1, p2, p3, p4])
obj2 = Draft.makeWire([p1, -2.3*p2, -0.8*p3, -1.8*p4])

objects = [obj1, obj2]

importOCA.export(objects, "/home/user/Pictures/myfile.oca")
```


<div class="mw-translate-fuzzy">





</div>


 

[Category:File Formats](Category:File_Formats.md)
