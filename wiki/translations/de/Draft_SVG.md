# Draft SVG/de










{{TOCright}}

## Beschreibung

Draft SVG ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Öffnen](Std_Open/de.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import/de.md) und <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export/de.md) Befehlen verwendet wird, um das [SVG](SVG/de.md) Dateiformat handzuhaben.

![](images/Screenshot_inkscape.jpg ) *Inkscape Zeichnung in SVG exportiert, die anschließend in FreeCAD geöffnet wird*

## Importieren

Die folgenden SVG Objekte können importiert werden:

-   PFAD Objekte
-   LINIE Objekte
-   RECHTWINKLIG Objekte
-   KREIS Objekte
-   ELLIPSE Objekte
-   POLYGON Objekte
-   POLYLINIE Objekte

### Begrenzungen

FreeCAD importiert keine Pfadobjekte, die nur einen Punkt haben ([Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=43856)).

## Exportieren

Die folgenden FreeCAD Objekte können exportiert werden:

-   Linien und Drähte (Polylinien)
-   Bögen und Kreise
-   Flächen
-   Texte
-   Abmessungen

### Begrenzungen 

SVG ist ein 2D Format, daher werden alle Z Informationen nicht berücksichtigt (alle Objekte werden abgeflacht).

## Einheiten Handhabung 

Beim Export ist eine Benutzereinheit (px) gleich einem Millimeter.

Beim Importieren werden die Attribute Breite, Höhe und Ansichtskasten beachtet. Alle Elemente werden auf ihre Größe in Millimeter skaliert, was der internen FreeCAD Einheit entspricht. Wenn das SVG keine Informationen über seine physikalische Größe enthält, wird angenommen, dass es eine Auflösung von 90 DPI hat. Die Verwendung von absoluten Einheiten in den Attributen innerhalb der SVG sollte vermieden werden. Relative Einheiten wie em,ex und % werden derzeit nicht unterstützt.

Der [Inkscape](https://inkscape.org/) SVG Editor arbeitet derzeit nur mit **90 DPI** Dokumenten. Unabhängig davon, welche Einheit in Inkscape ausgewählt ist. Die gesamte Ausgabe muss als in 90 DPI konvertiert und **gerundet** auf 6 Dezimalstellen betrachtet werden. Da FreeCAD (und der SVG Standard) die Genauigkeit der Rundung in Inkscape nicht berücksichtigt, werden diese Werte bei der Eingabe nicht gerundet. Und ungerade Werte in Millimeter bleiben erhalten. Wenn du möchtest, dass der SVG Import nicht gerundet wird, arbeite mit Anwendereinheiten (px) in Inkscape. Die Skalierung kann nach dem Import in FreeCAD oder durch Ändern der Breiten-, Höhen- und Ansichtskasten Attribute erfolgen.

## Einstellungen

Für weitere Informationen siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).

## Skripten


**Siehe auch:**

[Entwurf API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Du kannst Elemente durch die folgende Funktion nach DXF exportieren: 
```python
importSVG.export(exportList, filename)
```

Beispiel: 
```python
import Draft, importSVG

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importSVG.export(objects, "/home/user/Pictures/myfile.svg")
```





 

[Category:File Formats](Category:File_Formats.md)
