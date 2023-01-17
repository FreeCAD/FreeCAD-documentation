---
- GuiCommand:/de
   Name:Draft Label
   Name/de:Draft Notiz
   MenuLocation:Anmerkung → Bezeichnung
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**D** **L**
   Version:0.17
   SeeAlso:[Draft Text](Draft_Text/de.md), [Draft Textform](Draft_ShapeString/de.md)
---

# Draft Label/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Label.svg  style="width:24px;"> **Draft Notiz** erstellt einen mehrzeiligen Text an einer zweiteiligen Hinweislinie mit Pfeilspitze.

Wenn ein Objekt oder ein Teilelement (Fläche, Kante oder Knotenpunkt) ausgewählt ist, wenn der Befehl aufgerufen wird, kann der Text dazu verwendet werden ein oder zwei Attribute des ausgewählten Elements darzustellen, einschließlich Position, Länge, Volumen und Material. Der Text ist dann mit den Attributen verknüpft und wird aktualisiert, wenn sie ihre Werte ändern.

Um stattdessen ein Textelement ohne Hinweispfeil zu erstellen, verwendet man den Befehl [Draft Text](Draft_Text.md).

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;"> 
*Verschiedene Notizen mit unterschiedlichen Ausrichtungen, Hinweispfeilen und Informationen*



## Anwendung

Siehe auch: [Draft Fach](Draft_Tray/de.md), [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein Objekt oder ein Teilelement (Knotenpunkt, Kante oder Fläche) auswählen, dessen Attribute man darstellen möchte.
2.  Es gibt mehrere Möglichkeiten denBefehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Label.svg" width=16px> [Bezeichnung](Draft_Label/de.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_Label.svg" width=16px> Bezeichnung** auswählen.
    -   Das Tastaturkürzel **D** dann **L**.
3.  Der Aufgabenbereich **Bezeichnung** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
4.  Wenn ein Element ausgewählt wurde: Eine Möglichkeit aus dem Ausklappmenü **Label type** auswählen. Siehe [Notizarten](#Notizarten.md) weiter unten.
5.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken. Dieser Punkt bestimmt das Ziel (Pfeilspitze). Es kann irgendwo liegen und muss sich nicht auf einem Element befinden.
6.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken. Dieser Punkt bestimmt den Beginn des horizontalen bzw. vertikalen Abschnitts der Hinweislinie.
7.  Den dritten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**drücken. Dieser Punkt bestimmt den Basispunkt des Texts.



## Optionen

Die im Aufgabenbereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die voreingestellten Tastenkürzel.

-   Zur manuellen Eingabe der Koordinaten, werden die X-, Y- und Z-Komponenten einzeln eingegeben und jeweils mit **Enter** bestätigt. Es kann auch die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** gedrückt werden, wenn die gewünschten Werte vorhanden sind. Es ist ratsam den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **R**drücken oder die Checkbox **Relativ** aktivieren, um den Relativmodus ein- bzw. auszuschalten. Bei aktiviertem Relativmodus haben Koordinaten einen Bezug zum letzten Punkt, wenn vorhanden, andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Globalmodus ein- bzw. auszuschalten. Bei aktiviertem Globalmodus haben Koordinaten einen Bezug zum globalen Koordinatensystem, andernfalls beziehen sich Koordinaten auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **S**drücken, um [Draft Fangen](Draft_Snap.md) ein- oder auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Notizarten

Die folgenden Arten von Notizen stehen zur Verfügung:

-    {{Value|Custom}}: zeigt den Inhalt der {{PropertyData/de|Custom Text}} an.

-    {{Value|Name}}: zeigt den internen Namen des Zielobjekts an; der interne Name wird dem Objekt bei seiner Erstellung zugewiesen und ist während der gesamten Existenz des Objekts unveränderlich.

-    {{Value|Label}}: zeigt die Bezeichnung (Label) des Zielobjekts an; die Bezeichnung eines Objekts kann jederzeit vom Benutzer geändert werden.

-    {{Value|Position}}: zeigt die Koordinaten des Basispunktes des Zielobjekts, des Zielknotenpunktes oder des Schwerpunktes des Ziel-Teilelements an, falls vorhanden.

-    {{Value|Length}}: zeigt die Länge des Zielobjekts oder des Teilelements an, falls vorhanden.

-    {{Value|Area:}}zeigt die Fläche des Zielobjekts oder des Teilelements an, falls vorhanden.

-    {{Value|Volume}}: zeigt das Volumen des Zielobjekts an, falls vorhanden.

-    {{Value|Tag:}}zeigt das Attribut `Tag` des Zielobjekts an, falls vorhanden. Objekte, die mit dem Arbeitsbereich [Arch](Arch_Workbench/de.md) erstellte wurden, können dieses Attribut besitzen.

-    {{Value|Material:}}zeigt die Bezeichnung des Materials des Zielobjekts an, falls vorhanden



## Hinweise


<div class="mw-translate-fuzzy">

-   Die Richtung des zweiten Abschnitts der Hinweislinie bestimmt die Ausrichtung des Textes. Wenn der Abschnitt horizontal ist und nach rechts zeigt, wird der Text links (-bündig) ausgerichtet und umgekehrt. Wenn der zweite Abschnitt vertikal nach oben zeigt, wird der Text links ausgerichtet. Zeigt er vertikal nach unten, wird der Text rechts ausgerichtet.


</div>



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft Notiz-Objekt ist von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Die folgenden sind, wenn nicht anders angegeben, zusätzliche Eigenschaften:



### Daten


{{TitleProperty|Label}}

-    {{PropertyData/de|Custom Text|StringList}}: bestimmt den Inhalt des Textes, wenn die {{PropertyData/de|Label Type}} auf {{Value|Custom}} gesetzt ist. Jedes Element der Liste stellt eine neue Textzeile dar.

-    {{PropertyData/de|Label Type|Enumeration}}: bestimmt die Art der von der Notiz dargestellten Information. Siehe [Notizarten](#Notizarten.md).

-    {{PropertyData/de|Placement|Placement}}: bestimmt die Position des Textes in der [3D-Ansicht](3D_view/de.md) und, solange die {{PropertyData/de|Straight Direction}} nicht auf {{Value|Custom}} gesetzt ist, auch die des ersten Abschnitts der Hinweislinie, an dem der Text befestigt ist. Siehe [Positionierung](Placement/de.md).

-    {{PropertyData/de|Text|StringList}}: (read-only) bestimmt den Inhalt des Textes, der aktuell dargestellt wird. Jedes Element der Liste stellt eine neue Textzeile dar.


{{TitleProperty|Leader}}

-    {{PropertyData/de|Points|VectorList}}: Bestimmt die Punkte der Hinweislinie.

-    {{PropertyData/de|Straight Direction|Enumeration}}: Bestimmt die Richtung des ersten Abschnitts der HInweislinie: {{Value|Custom}}, {{Value|Horizontal}} oder {{Value|Vertikal}}.

-    {{PropertyData/de|Straight Distance|Distance}}: Bestimmt die Länge des ersten Abschnitts der Hinweislinie. Wird nur verwendet, wenn die {{PropertyData/de|Straight Direction}} auf {{Value|Horizontal}} oder {{Value|Vertical}} gesetzt wurde. Wenn der Abstand positiv ist, startet die Hinweislinie auf der rechten Seite des Textes und der Text wird nach rechts ausgerichtet. Andernfalls startet die Hinweislinie von der linken Seite des Textes und der Text wird nach links ausgerichtet


{{TitleProperty|Target}}

-    **Target|LinkSub**: specifies the object and optional subelement the label is linked to.

-    **Target Point|Vector**: specifies the position of the tip of the leader, which is where the arrow is attached.



### Ansicht


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the label. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the label.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Placement** of the label. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v1.0)</small> ).


{{TitleProperty|Graphics}}


<div class="mw-translate-fuzzy">

### Ansicht 

-    **Text  Schriftart**: gibt die Schriftart an, die zum Zeichnen des Textes verwendet werden soll. Es kann ein Schriftname sein, wie z. B. \"Arial\", ein Standardstil wie \"sans\", \"serif\" oder \"mono\", eine Familie wie \"Arial,Helvetica,sans\" oder ein Name mit einem Stil wie \"Arial:Bold\". Wenn die angegebene Schriftart nicht auf dem System gefunden wird, wird stattdessen eine generische Schriftart verwendet.

-    **Textgröße**: gibt die Größe des Textes an. Wenn das Etikettenobjekt in der Strukturansicht erstellt wird, aber kein Text in der 3D-Ansicht sichtbar ist, erhöhen Sie die Größe des Textes, bis er sichtbar ist.

-    **Textausrichtung**: legt die vertikale Ausrichtung der Grundlinie des Textes in Bezug auf die Führungslinie fest. Sie kann oben, mittig oder unten sein.

-    **Textfarbe**: gibt die Farbe des Textes in einem RGB-Tupel (R, G, B) an.

-    **Linienbreite**: gibt die Breite des Vorspanns an.

-    **Linienfarbe**: legt die Farbe der Führungslinie fest.

-    **Pfeilgröße**: legt die Größe des Symbols fest, das an der Spitze der Führungslinie angezeigt wird.

-    **Pfeiltyp**: gibt den Typ des Symbols an, das an der Spitze der Führungslinie angezeigt wird, z. B. Punkt, Kreis, Pfeil oder Häkchen.

-    **Rahmen**: wenn es \"Rectangle\" ist, wird ein Rahmen um den Text gezeichnet.

-    **Linie**: wenn es `True` ist, wird die Führungslinie angezeigt; andernfalls wird nur der Text und das Symbol an der Spitze angezeigt.

-    **Anzeigemodus**: wenn es \"3D-Text\" ist, wird der Text an den Szenenachsen ausgerichtet und liegt zunächst auf der XY-Ebene; wenn es \"2D-Text\" ist, zeigt der Text immer zur Kamera.


</div>


{{TitleProperty|Text}}

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead. <small>(v1.0)</small> 

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small. <small>(v1.0)</small> 

-    **Justification|Enumeration**: specifies the horizontal alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}. Only used if **Straight Direction** is {{Value|Custom}}. Otherwise the horizontal alignment is based on the sign (positive or negative) of **Straight Distance**.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Max Chars|Integer**: specifies the maximum number of characters on each line of the text.

-    **Text Alignment|Enumeration**: specifies the vertical alignment of the text: {{value|Top}}, {{value|Middle}} or {{value|Bottom}}.

-    **Text Color|Color**: specifies the color of the text.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Draft Notiz kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus mit der folgenden Funktion verwendet werden:


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/de
