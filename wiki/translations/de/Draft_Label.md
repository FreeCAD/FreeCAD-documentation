---
 GuiCommand:
   Name: Draft Label
   Name/de: Draft Hinweis
   MenuLocation: Anmerkung , Bezeichnung
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **D** **L**
   Version: 0.17
   SeeAlso: Draft_Text/de, Draft_ShapeString/de
---

# Draft Label/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Label.svg  style="width:24px;"> **Draft Hinweis** erstellt einen mehrzeiligen Text an einer zweiteiligen Hinweislinie mit Pfeilspitze.

Wenn ein Objekt oder ein Teilelement (Fläche, Kante oder Knotenpunkt) ausgewählt ist, wenn der Befehl aufgerufen wird, kann der Text dazu verwendet werden ein oder zwei Attribute des ausgewählten Elements darzustellen, einschließlich Position, Länge, Flächeninhalt, Volumen und Material. Der Text ist dann mit den Attributen verknüpft und wird aktualisiert, wenn sie ihre Werte ändern.

Um stattdessen ein Textelement ohne Hinweispfeil zu erstellen, verwendet man den Befehl [Draft Text](Draft_Text.md).

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;"> 
*Verschiedene Hinweise mit unterschiedlichen Ausrichtungen, Hinweispfeilen und Informationen*



## Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein Objekt oder ein Unterelement (Knotenpunkt, Kante oder Fläche) auswählen, dessen Attribute man anzeigen möchte.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Label.svg" width=16px> [Bezeichnung](Draft_Label/de.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_Label.svg" width=16px> Bezeichnung** auswählen.
    -   Das Tastaturkürzel **D** dann **L**.
3.  Der Aufgaben-Bereich **Beschriftung** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
4.  Wenn ein Element ausgewählt wurde: Einen Eintrag aus dem Ausklappmenü **Labeltyp** auswählen. Siehe [Hinweisarten](#Hinweisarten.md) weiter unten.
5.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken. Dieser Punkt bestimmt das Ziel (Pfeilspitze). Es kann irgendwo liegen und muss sich nicht auf einem Element befinden.
6.  Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken. Dieser Punkt bestimmt den Beginn des horizontalen bzw. vertikalen Abschnitts der Hinweislinie.
7.  Den dritten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken. Dieser Punkt bestimmt den Basispunkt des Texts.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel.

-   Zur manuellen Eingabe der Koordinaten, werden die X-, Y- und Z-Komponenten einzeln eingegeben und jeweils mit **Enter** bestätigt. Es kann auch die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** gedrückt werden, wenn die gewünschten Werte vorhanden sind. Es ist ratsam den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **R**drücken oder die Checkbox **Relativ** aktivieren, um den Relativmodus ein- bzw. auszuschalten. Bei aktiviertem Relativmodus haben Koordinaten einen Bezug zum letzten Punkt, wenn vorhanden, andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Globalmodus ein- bzw. auszuschalten. Bei aktiviertem Globalmodus haben Koordinaten einen Bezug zum globalen Koordinatensystem, andernfalls beziehen sich Koordinaten auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **S**drücken, um [Draft Fangen](Draft_Snap.md) ein- oder auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweisarten

Die folgenden Arten von Hinweisen stehen zur Verfügung:

-    {{Value|Benutzerdefiniert}}(Custom): zeigt den Inhalt der {{PropertyData/de|Custom Text}} an.

-    {{Value|Name}}: zeigt den internen Namen des Zielobjekts an; der interne Name wird dem Objekt bei seiner Erstellung zugewiesen und ist während der gesamten Existenz des Objekts unveränderlich.

-    {{Value|Benennung}}(Label): zeigt die Benennung des Zielobjekts an; die Benennung eines Objekts kann jederzeit vom Benutzer geändert werden.

-    {{Value|Position}}: zeigt die Koordinaten des Basispunktes des Zielobjekts oder des Zielknotenpunktes an.

-    {{Value|Length}}: zeigt die Länge des Zielobjekts oder des Unterelements an.

-    {{Value|Area}}: zeigt den Flächeninhalt des Zielobjekts oder des Unterelements an.

-    {{Value|Volume}}: zeigt das Volumen des Zielobjekts an.

-    {{Value|Kennzeichen}}(Tag): zeigt das Attribut `Tag` des Zielobjekts an. Objekte, die mit dem Arbeitsbereich [BIM](BIM_Workbench/de.md) erstellt wurden, können dieses Attribut besitzen.

-    {{Value|Material}}: zeigt die Benennung des Materials des Zielobjekts an.

-    {{Value| Benennung + Position}}
    

-    {{Value| Benennung + Länge}}
    

-    {{Value| Benennung + Flächeninhalt}}
    

-    {{Value| Benennung + Volumen}}
    

-    {{Value| Benennung + Material}}
    



## Hinweise

-   Die Richtung des zweiten Abschnitts der Hinweislinie bestimmt die Ausrichtung des Textes. Wenn der Abschnitt horizontal ist und nach rechts zeigt, wird der Text links (-bündig) ausgerichtet und umgekehrt. Wenn der zweite Abschnitt vertikal nach oben zeigt, wird der Text links ausgerichtet. Zeigt er vertikal nach unten, wird der Text rechts ausgerichtet.
-   Draft-Notizen, die mit [FreeCAD Version 0.21](Release_notes_0.21/de.md) erstellt oder gespeichert werden, sind nicht abwärtskompatibel.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Hinweis (Label-Objekt) ist von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Die folgenden sind, wenn nicht anders angegeben, zusätzliche Eigenschaften:



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

-    {{PropertyData/de|Target|LinkSub}}(Ziel): Gibt das Objekt und wahlweise das Unterelement an, mit dem der Hinweis verknüpft ist .

-    {{PropertyData/de|Target Point|Vector}}(Zielpunkt): Gibt die Position der Spitze der Hinweislinie an, d.h. wo der Pfeil befestigt wird.



### Ansicht


{{TitleProperty|Annotation}}

-    {{PropertyView/de|Annotation Style|Enumeration}}: Gibt den Beschriftungsstil an, der für den Hinweis verwewendet wird. Siehe [Draft BeschriftungsstilEditor](Draft_AnnotationStyleEditor/de.md).

-    {{PropertyView/de|Scale Multiplier|Float}}: Gibt den allgemeinen Skalierungsfaktor an, der für den Hinweis verwewendet wird. Siehe


{{TitleProperty|Display Options}}

-    {{PropertyView/de|Display Mode|Enumeration}}: Gibt an, wie der Text angezeigt wird. Ist es {{value|World}}, wird der Text auf einer Ebene angezeigt, die durch die {{PropertyData/de|Placement}} des Hinweises festgelegt wird. Ist es {{value|Screen}}, wird der Text immer in Richtung Bildschirm angezeigt. Dies ist eine übernommene Eigenschaft. Die genannten Optionen sind die umbenannten Optionen ({{Version/de|0.21}}).


{{TitleProperty|Graphics}}

-    {{PropertyView/de|Arrow Size|Length}}: Legt die Größe des Symbols fest, das der Spitze der Hinweislinie angezeigt wird.

-    {{PropertyView/de|Arrow Type|Enumeration}}: Legt die Art des Symbols fest, das der Spitze der Hinweislinie angezeigt wird und die Werte {{value|Dot}} (Punkt), {{value|Circle}} (Ring), {{value|Arrow}} (Pfeil), {{value|Tick}} (Schrägstrich) oder {{value|Tick-2}} (Schrägstrich-2) annehmen kann.

-    {{PropertyView/de|Frame|Enumeration}}: Legt fest, welche Art Rahmen um den Text herum gezeichnet wird. Die Optionen sind zurzeit {{Value|None}} (keiner) oder {{Value|Rectangle}} (Rechteck).

-    {{PropertyView/de|Line|Bool}}: Legt fest, ob die Hinweislinie angezeigt wird. Auf `False` gesetzt, werden nur der Pfeil und der Text angezeigt.

-    {{PropertyView/de|Line Color|Color}}: Legt die Farbe von Hinweislinie und Pfeil fest. Diese wird auch für den Rahmen verwendet.

-    {{PropertyView/de|Line Width|Float}}: Legt die Breite der Hinweisliie fest. Diese wird auch für den Rahmen verwendet.


{{TitleProperty|Text}}

-    {{PropertyView/de|Font Name|Font}}: Bestimmt die Schriftart, die zum Zeichnen des Textes verwendet wird. Dies kann ein Schriftname sein, wie {{value|Arial}}, eine Stilbezeichnung, wie {{value|sans}}, {{value|serif}} oder {{value|mono}}, eine Familie, wie {{value|Arial,Helvetica,sans}}, oder ein Name mit Stilangabe, wie {{value|Arial:Bold}}. Wird die angegebene Schriftart im System nicht gefunden, wird stattdessen eine Standardschrift verwendet. {{Version/de|0.21}}

-    {{PropertyView/de|Font Size|Length}}: Bestimmt die Größe der Buchstaben. Der Text kann in der [3D-Ansicht](3D_view/de.md) unsichtbar sein, wenn dieser Wert sehr klein ist. {{Version/de|0.21}}

-    {{PropertyView/de|Justification|Enumeration}}: Bestimmt die horizontale Ausrichtung des Textes: {{value|Left}} (links), {{value|Center}} (Mitte) oder {{value|Right}} (rechts). Wird nur verwendet, wenn {{PropertyData/de|Straight Direction}} auf {{Value|Custom}} gesetzt ist. Andernfalls basiert die horizontale Ausrichtung auf dem Vorzeichen (positiv oder negativ) der {{PropertyData/de|Straight Distance}}.

-    {{PropertyView/de|Line Spacing|Float}}: Bestimmt den Faktor, der für den Standardzeilenhöhe des Textes verwendet wird.

-    {{PropertyView/de|Max Chars|Integer}}: Bestimmt die maximale Anzahl von Schriftzeichen in jeder Zeile des Textes.

-    {{PropertyView/de|Text Alignment|Enumeration}}: Bestimmt die vertikale Ausrichtung des Textes: {{value|Top}} (oben), {{value|Middle}} (Mitte) oder {{value|Bottom}} (unten).

-    {{PropertyView/de|Text Color|Color}}: Bestimmt die Farbe des Textes.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Draft-Hinweis kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus mit der folgenden Funktion verwendet werden:


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
label1.ViewObject.FontSize= 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.FontSize= 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.FontSize= 200

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/de
