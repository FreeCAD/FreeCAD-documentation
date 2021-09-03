---
- GuiCommand:/de
   Name:Draft ShapeString
   Name/de:Entwurf FormZeichenfolge
   MenuLocation:Entwurf → Form aus Text ...
   Workbenches:[Entwurf](Draft_Module/de.md), [Architektur](Arch_Module/de.md)
   Shortcut:**S** **S**
   Version:0.14
   SeeAlso:[Entwurf Text](Draft_Text/de.md), [Part Extrudieren](Part_Extrude/de.md),
[Makro Schriftarten Win10 PYMP](Macro_Fonts_Win10_PYMP/de.md)
---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug **<img src="images/Draft_ShapeString.svg" width=16px> [Entwurf FormZeichenfolge](Draft_ShapeString/de.md)** fügt eine Verbundform ein, die eine TextZeichenfolge darstellt. Texthöhe, Laufweite und Schriftart können angegeben werden. Die resultierende Form kann mit dem Werkzeug <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Teil Extrusion](Part_Extrude/de.md) verwendet werden, um 3D Buchstaben zu erzeugen.


</div>


<div class="mw-translate-fuzzy">

**Alternativ**: Um ein einfacheres Textelement ohne geschlossene Form einzufügen, verwende <img alt="" src=images/Draft_Text.svg  style="width:24px;"> [Entwurf Text](Draft_Text/de.md). Um eine Textbeschriftung mit einem Anfang und einem Pfeil zu erstellen, verwende <img alt="" src=images/Draft_Label.svg  style="width:24px;">[Entwurf Beschriftung](Draft_Label/de.md)


</div>

![](images/Draft_ShapeString_Example400.png )


<div class="mw-translate-fuzzy">


*Einfacher Punkt zur Positionierung des Formzeichenfolge erforderlich*


</div>

## Anwendung


<div class="mw-translate-fuzzy">

Wenn der Entwurf Benutzeroberflächenmodus auf Aufgabenansicht eingestellt ist:

1.  Drücke den **![](images/)**_oder_drücke_die_Tasten_**S**_und_dann_**S**.
2.  Ein Dialogfeld erscheint, in dem Du deine Parameter angeben kannst.
3.  Drücke die Taste **OK**, um die Formfolge zu erstellen.


</div>

## Optionen


<div class="mw-translate-fuzzy">

-   Um Koordinaten von Hand einzugeben, gib einfach die Zahlen ein und drücke dann **Enter** zwischen jeder X-, Y- und Z-Komponente. Du kannst den **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügent](Draft_AddPoint/de.md)** drücken, wenn Du die gewünschten Werte zum Einfügen des Punktes hast.
-   Drücke die Taste **Esc** oder die Taste **Close**, um den aktuellen Befehl abzubrechen.


</div>

## Notes


<div class="mw-translate-fuzzy">

### Begrenzungen

-   Sehr kleine Texthöhen können durch Detailverlust bei der Skalierung zu verzerrten Zeichenformen führen.
-   Die aktuelle Version ist auf die von Links nach Rechts Schreiben begrenzt.
-   Um kreisförmig angeordneten Text zu erstellen, verwende den **<img src=images/FCCircularTextButtom.png style="width:24px"> [Rundtext](Macro_Circular_Text.md)**.


</div>

## Tutorien

-   [Entwurf FormFolge Tutorium](Draft_ShapeString_tutorial/de.md): einen ShapeString extrudieren, im 3D Raum positionieren und eine Gravur in einem anderen Körper erzeugen.
-   [Anwenden von Formfolgen in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The default font file can be changed in the preferences: {{MenuCommand|Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file}}. See [Draft Preferences](Draft_Preferences.md).

## Eigenschaften

See also: [Property editor](Property_editor.md).

A Draft ShapeString object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Position}}: gibt die Position des Basispunktes der verbundenen Form an.

-    {{PropertyData/de|Winkel}}: gibt die Rotation der Grundlinie der Form an.

-    {{PropertyData/de|Achse}}: gibt die Achse an, die für die Rotation verwendet werden soll.

-    {{PropertyData/de|Folge}}: gibt die anzuzeigende Textzeichenfolge an; im Gegensatz zum Werkzeug [Entwurf Text](Draft_Text/de.md) kann das Werkzeug [Entwurf FormFolge](Draft_ShapeString/de.md) nur eine einzelne Zeile anzeigen.

-    {{PropertyData/de|Größe}}: gibt die allgemeine Höhe der Buchstaben an.

-    {{PropertyData/de|Laufweite}}: gibt den zusätzlichen Abstand zwischen den Zeichen in der Zeichenkette an.

-    {{PropertyData/de|Schriftartdatei}}: gibt den vollständigen Pfad der Schriftdatei an, die zum Zeichnen der Zeichenkette verwendet wird.


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the text. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das FormFolge Werkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion benutzt werden:


</div>


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```


<div class="mw-translate-fuzzy">

-   Erzeugt eine {{incode/de|Formfolge}} verbundene Form unter Verwendung der angegebenen {{incode/de|Folge}} und des vollständigen Pfades einer unterstützten {{incode/de|Schriftartdatei}}.

-    {{incode/de|Größe}}ist die Höhe des resultierenden Textes in Millimetern.

-    {{incode/de|Laufweite}}ist der zusätzliche Zeichenabstand in Millimetern.


</div>

Die Platzierung der FormFolge kann durch Überschreiben seines `Placement` Attributs oder durch individuelles Überschreiben seiner `Placement.Base` und `Placement.Rotation` Attribute geändert werden.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
