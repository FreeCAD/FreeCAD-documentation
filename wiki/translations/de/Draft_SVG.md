# Draft SVG/de
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Beschreibung

Draft SVG ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> _ und <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export/de.md) Befehlen verwendet wird, um das [SVG](SVG/de.md) Dateiformat handzuhaben.

![](images/Screenshot_inkscape.jpg ) 
*Inkscape Zeichnung in SVG exportiert, die anschließend in FreeCAD geöffnet wird*

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


<div class="mw-translate-fuzzy">

Beim Importieren werden die Attribute Breite, Höhe und Ansichtskasten beachtet. Alle Elemente werden auf ihre Größe in Millimeter skaliert, was der internen FreeCAD Einheit entspricht. Wenn das SVG keine Informationen über seine physikalische Größe enthält, wird angenommen, dass es eine Auflösung von 90 DPI hat. Die Verwendung von absoluten Einheiten in den Attributen innerhalb der SVG sollte vermieden werden. Relative Einheiten wie em,ex und % werden derzeit nicht unterstützt.


</div>


<div class="mw-translate-fuzzy">

Der [Inkscape](https://inkscape.org/) SVG Editor arbeitet derzeit nur mit **90 DPI** Dokumenten. Unabhängig davon, welche Einheit in Inkscape ausgewählt ist. Die gesamte Ausgabe muss als in 90 DPI konvertiert und **gerundet** auf 6 Dezimalstellen betrachtet werden. Da FreeCAD (und der SVG Standard) die Genauigkeit der Rundung in Inkscape nicht berücksichtigt, werden diese Werte bei der Eingabe nicht gerundet. Und ungerade Werte in Millimeter bleiben erhalten. Wenn du möchtest, dass der SVG Import nicht gerundet wird, arbeite mit Anwendereinheiten (px) in Inkscape. Die Skalierung kann nach dem Import in FreeCAD oder durch Ändern der Breiten-, Höhen- und Ansichtskasten Attribute erfolgen.


</div>

## Einstellungen


<div class="mw-translate-fuzzy">

Für weitere Informationen siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).


</div>

## Skripten


<div class="mw-translate-fuzzy">


**Siehe auch:**

[Entwurf API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Du kannst Elemente durch die folgende Funktion nach DXF exportieren:


</div>


```python
importSVG.export(exportList, filename)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

Beispiel:


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


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft SVG/de
