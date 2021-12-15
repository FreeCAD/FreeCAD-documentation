---
- GuiCommand:/de
   Name:Draft Text
   Name/de:Draft Text
   MenuLocation:Entwurf → Text
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**T** **E**
   SeeAlso:[Draft Label](Draft_Label/de.md), [Draft ShapeString](Draft_ShapeString/de.md)
   Version:0.7
---

# Draft Text/de


</div>

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

== Das Textwerkzeug fügt an einer bestimmten Stelle eine mehrzeilige Textbox ein. Es wird das [Draft Linestyle](Draft_Linestyle/de.md) verwendet, das auf dem [Draft Tray](Draft_Tray/de.md) eingestellt ist.


</div>


<div class="mw-translate-fuzzy">

Um ein Textfeld mit einem Führungszeichen und einem Pfeil zu erstellen, verwenden Sie [Draft Label](Draft_Label.md). Um Volltext oder 3D Buchstaben zu erstellen, verwende [Draft ShapeString](Draft_ShapeString/de.md) mit [Part Extrude](Part_Extrude/de.md).


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Einzelner Punkt erforderlich zum Positionieren der Text-Box*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

## Anwendung

1.  Drücke die Schaltfläche **<img src="images/Draft_Text.png" width=16px> [Draft Text](Draft_Text/de.md)** oder drücke **T**, dann **E** Tasten.
2.  Klicke auf einen Punkt in der 3D Ansicht oder gib eine Koordinate ein und drücke die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen**.
3.  Gib den gewünschten Text ein, drücke **Enter** zwischen jeder Zeile.
4.  Drücke **Enter** zweimal , um den Vorgang abzuschließen.


</div>

## Optionen

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Um Koordinaten manuell einzugeben, gib einfach die Zahlen ein und drücke dann **Enter** zwischen jeder X, Y und Z Komponente. Du kannst den **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Schaltfläche drücken, wenn Du die gewünschten Werte zum Einfügen des Punktes hast.
-   Halte **Ctrl** gedrückt, während du den Text platzierst, um [Fang](Draft_Snap/de.md) deinen Punkt unabhängig von der Entfernung an die nächste Fangposition zu zwingen.
-   Drücke **Enter** oder **↓ Pfeil nach unten**, um eine neue Textzeile einzugeben.
-   Drücke **↑ Pfeil nach oben**, um die vorherige Textzeile zu bearbeiten.
-   Drücke zweimal **Enter** oder **↓ Pfeil nach unten**, um die Bearbeitung des Textes abzuschließen.
-   Drücke **Esc** oder die Taste **Close**, um den aktuellen Befehl abzubrechen.


</div>

## Notes


<div class="mw-translate-fuzzy">

**Warnung:** Die mit [version 0.18](Release_notes_0.18.md) erstellten Texte sind nicht abwärtskompatibel, sichern Sie also Ihre Arbeit, wenn Sie versuchen, mit 0.18 erstellte Dateien mit älteren Versionen zu öffnen.


</div>

## Eigenschaften

See also: [Property editor](Property_editor.md).

A Draft Text object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated.

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

### Daten

-    {{PropertyData/de|Text}}: gibt den Inhalt des Textblocks als Liste von Zeichenketten an; jedes Element auf der Liste, durch ein Komma getrennt, zeigt eine neue Zeile an.

-    {{PropertyData/de|Position}}: gibt den Basispunkt der ersten Zeile des Textblocks an.

-    {{PropertyData/de|Winkel}}: gibt die Rotation der Grundlinie der ersten Zeile des Textblocks an.

-    {{PropertyData/de|Achse}}: gibt die Achse an, die für die Rotation verwendet werden soll.


</div>

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the text. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the text.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by its **Placement**. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}


<div class="mw-translate-fuzzy">

### Ansicht

-    {{PropertyView/de|Ansichtsmodus}}: wenn es sich um \"3D Text\" handelt, wird der Text an den Szenenachsen ausgerichtet, wobei er zunächst auf der XY Ebene liegt; wenn es sich um \"2D Text\" handelt, wird der Text immer der Kamera zugewandt sein.

-    {{PropertyView/de|Schriftartname}}: gibt die Schriftart an, die zum Zeichnen des Textes verwendet werden soll. Es kann ein Schriftname wie \"Arial\", ein Standardstil wie \"sans\", \"serif\" oder \"mono\", eine Familie wie \"Arial, Helvetica, sans\" oder ein Name mit einem Stil wie \"Arial:Bold\" sein. Wenn die angegebene Schriftart nicht auf dem System gefunden wird, wird stattdessen eine generische Schriftart verwendet.

-    {{PropertyView/de|Schriftgröße}}: gibt die Größe der Buchstaben an. Wenn das Textobjekt in der Baumansicht erstellt wird, aber kein Text sichtbar ist, erhöhe die Größe des Textes, bis er sichtbar ist.

-    {{PropertyView/de|Ausrichtung}}: gibt an, ob der Text links, rechts oder in der Mitte des Basispunktes ausgerichtet ist.

-    **Zeilenabstand**: gibt den Abstand zwischen den Textzeilen an.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Textwerkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


</div>


```python
text = make_text(string, placement=None, screen=False)
```


<div class="mw-translate-fuzzy">

-   Erstellt ein `Text` Objekt, an einem `Punkt`, der durch einen `FreeCAD.Vector` definiert ist.

-    `Liste Zeichenkette`ist eine Zeichenkette oder eine Liste von Zeichenketten; wenn es eine Liste ist, wird jedes Element in einer eigenen Zeile angezeigt.

-   Wenn `screen` `True` ist, ist der Text immer in Blickrichtung der Kamera ausgerichtet, andernfalls richtet er sich nach den Szenenachsen aus und liegt auf der XY Ebene.


</div>


<div class="mw-translate-fuzzy">

Die Ansichtseigenschaften von `Text` können durch Überschreiben seiner Attribute geändert werden; z.B. überschreibe `ViewObject.FontSize` mit der neuen Größe in Millimetern.


</div>

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/de
