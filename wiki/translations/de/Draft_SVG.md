# Draft SVG/de
## Beschreibung

Draft SVG ist ein Softwaremodul, das von den Befehlen <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Öffnen](Std_Open/de.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import/de.md) und <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export/de.md) verwendet wird, um das [SVG](SVG/de.md)-Dateiformat zu verarbeiten.

![](images/Screenshot_inkscape.jpg ) 
*Inkscape-Zeichnung als SVG-Datei exportiert und anschließend in FreeCAD geöffnet*



## Importieren

Die folgenden SVG Objekte können importiert werden:

-   PATH-Objekte (Pfade)
-   LINE-Objekte (Linien)
-   RECT-Objekte (Rechtecke)
-   CIRCLE-Objekte (Kreise)
-   ELLIPSE-Objekte (Ellipsen)
-   POLYGON-Objekte (Vielecke)
-   POLYLINE-Objekte (Linienzüge)



### Einschränkungen

FreeCAD importiert keine Pfadobjekte, die nur einen Punkt beinhalten ([Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=43856)).



## Exportieren

Die folgenden FreeCAD-Objekte können exportiert werden:

-   Linien und Drähte (Polylinien)
-   Bögen und Kreise
-   Flächen
-   Texte
-   Maße



### Einschränkungen 

SVG ist ein 2D-Format, daher werden alle Z-Informationen ignoriert (alle Objekte werden geebnet).



## Umgang mit Maßeinheiten 

Beim Export ist eine Benutzereinheit (px) gleich einem Millimeter.

Beim Importieren werden die Attribute width (Breite), height (Höhe) und viewBox (Ansichtsrahmen) beachtet. Alle Elemente werden auf ihre Größe in Millimeter skaliert, FreeCADs interner Einheit. Wenn die SVG-Datei keine Information über ihre physikalische Größe enthält, wird angenommen, dass sie eine Auflösung von 90 DPI verwendet. Die Verwendung von absoluten Einheiten in den Attributen innerhalb der SVG-Datei sollte vermieden werden. Relative Einheiten wie em, ex und % werden derzeit nicht unterstützt.

Der [Inkscape](https://inkscape.org/)-SVG-Editor arbeitet derzeit nur mit 90-DPI-Dokumenten. Unabhängig von der in Inkscape ausgewählten Einheit. Die gesamte Ausgabe muss als in 90 DPI konvertiert und auf 6 Dezimalstellen gerundet angesehen werden. Da FreeCAD (und der SVG-Standard) die Genauigkeit der Rundung in Inkscape nicht berücksichtigt, werden diese Werte bei der Eingabe nicht gerundet. Und ungerade Werte in Millimeter bleiben erhalten. Wenn der SVG Import nicht gerundet werden darf, sollte man in Inkscape mit Benutzereinheiten (px) arbeiten. Das Skalieren kann nach dem Import in FreeCAD erfolgen oder durch Ändern der Attribute width, height und viewbox erfolgen.



## Einstellungen

Siehe [Import Export Einstellungen](Import_Export_Preferences/de.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um Objekte in eine SVG-Datei zu exportieren, verwendet man die Methode `export` des Moduls importSVG.


```python
importSVG.export(exportList, filename)
```

-   Für Windows: Man verwendet **/** (forward slash) als Pfad-Trennzeichen in {{Incode|filename}}.

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



---
⏵ [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft SVG/de
