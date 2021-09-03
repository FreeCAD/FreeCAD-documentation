---
- GuiCommand:/de
   Name:Draft Label
   Name/de:Entwurf Etikett
   MenuLocation:Entwurf → Etikett
   Workbenches:[Entwurf](Draft_Module/de.md), [Arch](Arch_Module/de.md)
   Shortcut:**D** **L**
   SeeAlso:[Entwurf Text](Draft_Text/de.md), [Entwurf FormZeichenfolge](Draft_ShapeString/de.md)
   Version:0.17
---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Etikettenwerkzeug fügt ein mehrzeiliges Textfeld mit einer 2-teiligen Führungslinie und einem Pfeil ein. Wenn beim Starten des Befehls ein Objekt oder ein Unterelement (Fläche, Kante oder Knoten) ausgewählt wird, kann das Etikett veranlasst werden, ein bestimmtes Attribut des ausgewählten Elements anzuzeigen, einschließlich Position, Länge, Fläche, Volumen oder Material.


</div>

If an object or a sub-element (face, edge or vertex) is selected when starting the command, the text can be made to display one or two attributes of the selected element, including position, length, area, volume and material. The text will then be linked to the attributes and will update if their values change.


<div class="mw-translate-fuzzy">

Um ein einfacheres Textelement ohne Pfeil einzufügen, verwende [Entwurf Text](Draft_Text/de.md). Um feste Textformen zu erstellen, verwende [Entwurf FormZeichenfolge](Draft_ShapeString/de.md) mit [Part extrudieren](Part_Extrude/de.md).


</div>

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Verschiedene Etiketten mit unterschiedlichen Ausrichtungen, Hinweissymbolen und Informationen*


</div>

## Anwendung

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/Draft_Label.svg" width=16px> [Entwurf Etikett](Draft_Label/de.md)** Schaltfläche oder drücke **D** und dann **L** Schaltflächen.
2.  Klicke auf einen ersten Punkt in der 3D Ansicht oder gib eine [Koordinate](Draft_Coordinates/de.md) ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** Schaltfläche. Dieser Punkt gibt das Ziel (Pfeilspitze) an. Dies kann überall sein, es muss kein Element sein.
3.  Klicke auf einen zweiten Punkt in der 3D Ansicht, oder gib eine [Koordinate](Draft_Coordinates/de.md) ein, und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt  hinzufügen](Draft_AddPoint/de.md)** Schaltfläche. Dieser Punkt zeigt den Beginn einer horizontalen oder vertikalen Führungslinie an.
4.  Klicke auf einen dritten Punkt in der 3D Ansicht, oder gib eine [Koordinate](Draft_Coordinates/de.md) ein, und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt  hinzufügen](Draft_AddPoint/de.md)** Schaltfläche. Dieser Punkt gibt den Basispunkt des Textes an.


</div>

## Optionen

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Klicke auf **Etikettentyp**, um die Art der anzuzeigenden Informationen auszuwählen, einschließlich \"Benutzerdefiniert\", \"Name\", \"Etikett\", \"Position\", \"Länge\", \"Bereich\", \"Volumen\", \"Tag\" und \"Material\". (Siehe Erklärung der [Labeltypen](#Label_types/de.md) unten)
-   Um Koordinaten manuell einzugeben, gib einfach die Zahlen ein und drücke dann **Eingabe** zwischen jeder X, Y und Z Komponente. Du kannst die **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** Schaltfläche drücken wenn du die gewünschten Werte zum Einfügen des Punktes hast.
-   Halte **Strg** gedrückt, während der Platzierung der Beschriftung, um [Fang](Draft_Snap/de.md) deinen Punkt unabhängig von der Entfernung an die nächstgelegene Fangposition zu zwingen.
-   Drücke **Esc** oder die **Schließen** Schaltfläche, um den aktuellen Befehl abzubrechen.


</div>

## Notes


<div class="mw-translate-fuzzy">


**Hinweis:**

die Richtung des horizontalen geraden Segments, nach rechts oder links, richtet den Text automatisch in die entgegengesetzte Richtung aus. Wenn die Führungslinie vertikal nach oben geht, wird der Text nach links ausgerichtet; wenn sie vertikal nach unten geht, wird sie nach rechts ausgerichtet.


</div>

## Eigenschaften

See also: [Property editor](Property_editor.md).

A Draft Label object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data


{{TitleProperty|Label}}


<div class="mw-translate-fuzzy">

### Daten

-    **Etikettentyp**: legt die Art der von diesem Etikett angezeigten Informationen fest (siehe [Etikettentypen](#Etikett_typen.md) unten).

-    **Benutzerdefinierter Text**: gibt den Textblock an, der angezeigt werden soll, wenn **Etikettentyp** auf \"Benutzerdefiniert\" gesetzt ist oder das Etikett nicht parametrisiert ist. Der Text wird als Liste von Zeichenketten angegeben; jedes Element der Liste, getrennt durch ein Komma, zeigt eine neue Textzeile an.

-    **Text**: (schreibgeschützt) gibt den tatsächlichen Text an, der vom Etikett angezeigt wird, abhängig vom **Etikettentyp**.

-    **Zielpukt**: gibt die Position der Spitze des Vorspanns an.

-    **Gerade Richtung**: gibt die Richtung des geraden Segments der Führungslinie an, entweder horizontal oder vertikal.

-    **Gerader Abstand**: gibt die Länge des geraden Abschnitts der Führungslinie, ausgehend vom Basispunkt des Textes, an. Ist der Abstand positiv, beginnt der Vorspann an der rechten Seite des Textes und der Text wird rechtsbündig ausgerichtet; andernfalls beginnt der Vorspann an der linken Seite des Textes und der Text wird linksbündig ausgerichtet.

-    **Position**: gibt den Basispunkt der ersten Zeile des Textblocks an; er beeinflusst auch, wie der Vorspann gezeichnet wird.

-    **Winkel**: gibt die Drehung der Grundlinie der ersten Zeile des Textblocks an; beeinflusst auch die Zeichnung des Vorspanns, da dieser nicht mehr horizontal oder vertikal ist.

-    **Achse**: legt die Achse fest, die für die Drehung verwendet werden soll.


</div>


{{TitleProperty|Leader}}

-    **Points|VectorList**: specifies the points of the leader.

-    **Straight Direction|Enumeration**: specifies the direction of the first leader segment: {{Value|Custom}}, {{Value|Horizontal}} or {{Value|Vertical}}.

-    **Straight Distance|Distance**: specifies the length of the first leader segment. Only used if **Straight Direction** is {{Value|Horizontal}} or {{Value|Vertical}}. If the distance is positive, the leader starts from the right side of the text and the text aligns to the right. Otherwise the leader starts from the left side of the text and the text aligns to the left.


{{TitleProperty|Target}}

-    **Target|LinkSub**: specifies the object and optional subelement the label is linked to.

-    **Target Point|Vector**: specifies the position of the tip of the leader, which is where the arrow is attached.

#### Etikettentypen


<div class="mw-translate-fuzzy">

-    **Benutzerdefiniert:**zeigt den Inhalt von **Benutzerdefinierter Text** an.

-    **Name:**zeigt den internen Namen des Zielobjekts an; der interne Name wird dem Objekt zum Zeitpunkt seiner Erstellung zugewiesen und bleibt während der gesamten Existenz des Objekts fest.

-    **Etikett:**zeigt die Beschriftung des Zielobjekts an; die Beschriftung des Objekts kann jederzeit vom Benutzer geändert werden.

-    **Position:**zeigt die Koordinaten des Basispunkts des Zielobjekts, des Zielscheitelpunkts oder des Massenschwerpunkts des Zielunterelements an, falls zutreffend.

-    **Länge:**zeigt ggf. die Länge des Ziel Unterelements an.

-    **Fläche:**zeigt ggf. die Fläche des Ziel Unterelements an.

-    **Volumen:**zeigt das Volumen des Zielobjekts an, falls zutreffend.

-    **Tag:**zeigt das `Tag` Attribut des Zielobjekts an, wenn das Objekt eine solche Eigenschaft hat, z.B. mit der [Arch Arbeitsbereich](Arch_Workbench/de.md) erstellte Objekte.

-    **Material:**zeigt die Bezeichnung des Materials des Zielobjekts an, wenn das Zielobjekt eine solche Eigenschaft hat.


</div>

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the label. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the label.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by the **Placement** of the label. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}


<div class="mw-translate-fuzzy">

### Ansicht

-    **Text  Schriftart**: gibt die Schriftart an, die zum Zeichnen des Textes verwendet werden soll. Es kann ein Schriftname sein, wie z. B. \"Arial\", ein Standardstil wie \"sans\", \"serif\" oder \"mono\", eine Familie wie \"Arial,Helvetica,sans\" oder ein Name mit einem Stil wie \"Arial:Bold\". Wenn die angegebene Schriftart nicht auf dem System gefunden wird, wird stattdessen eine generische Schriftart verwendet.

-    **Textgröße**: gibt die Größe des Textes an. Wenn das Etikettenobjekt in der Strukturansicht erstellt wird, aber kein Text in der 3D-Ansicht sichtbar ist, erhöhen Sie die Größe des Textes, bis er sichtbar ist.

-    {{Eigenschaftsansicht|Textausrichtung}}: legt die vertikale Ausrichtung der Grundlinie des Textes in Bezug auf die Führungslinie fest. Sie kann oben, mittig oder unten sein.

-    **Textfarbe**: gibt die Farbe des Textes in einem RGB-Tupel (R, G, B) an.

-    **Linienbreite**: gibt die Breite des Vorspanns an.

-    {{Eigenschaftsansicht|Linienfarbe}}: legt die Farbe der Führungslinie fest.

-    {{Eigenschaftsansicht|Pfeilgröße}}: legt die Größe des Symbols fest, das an der Spitze der Führungslinie angezeigt wird.

-    {{Eigenschaftsansicht|Pfeiltyp}}: gibt den Typ des Symbols an, das an der Spitze der Führungslinie angezeigt wird, z. B. Punkt, Kreis, Pfeil oder Häkchen.

-    **Rahmen**: wenn es \"Rectangle\" ist, wird ein Rahmen um den Text gezeichnet.

-    **Linie**: wenn es `True` ist, wird die Führungslinie angezeigt; andernfalls wird nur der Text und das Symbol an der Spitze angezeigt.

-    **Anzeigemodus**: wenn es \"3D-Text\" ist, wird der Text an den Szenenachsen ausgerichtet und liegt zunächst auf der XY-Ebene; wenn es \"2D-Text\" ist, zeigt der Text immer zur Kamera.


</div>


{{TitleProperty|Text}}

-    **Justification|Enumeration**: specifies the horizontal alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}. Only used if **Straight Direction** is {{Value|Custom}}. Otherwise the horizontal alignment is based on the sign (positive or negative) of **Straight Distance**.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Max Chars|Integer**: specifies the maximum number of characters on each line of the text.

-    **Text Alignment|Enumeration**: specifies the vertical alignment of the text: {{value|Top}}, {{value|Middle}} or {{value|Bottom}}.

-    **Text Color|Color**: specifies the color of the text.

-    **Text Font|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Entwurf API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Etikett Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole mit der folgenden Funktion verwendet werden:


</div>


```python
label = make_label(target_point=App.Vector(0, 0, 0),
                   placement=App.Vector(30, 30, 0),
                   target_object=None, subelements=None,
                   label_type="Custom", custom_text="Label",
                   direction="Horizontal", distance=-10,
                   points=None)
```

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
doc.recompute()

p1 = App.Vector(-200, 1000, 0)
place1 = App.Placement(App.Vector(-1000, 1300, 0), App.Rotation())

label1 = Draft.make_label(p1, place1, target_object=rectangle, distance=500, label_type="Label")
label1.ViewObject.TextSize = 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.TextSize = 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.TextSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
