---
 GuiCommand:
   Name: Draft Text
   Name/de: Draft Text
   MenuLocation: Anmerkung , Text
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **T** **E**
   Version: 0.7
   SeeAlso: Draft_Label/de, Draft_ShapeString/de
---

# Draft Text/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Text.svg  style="width:24px;"> **Draft Text** erstellt einen mehrzeiligen Text an einem vorgegebenen Punkt.

Um stattdessen ein Textelement mit einem Hinweispfeil zu erstellen, verwendet man den Befehl [Draft Notiz](Draft_Label/de.md).

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Ein einzelner Punkt, den das Positionieren des Textes erfordert*



## Anwendung

Siehe auch: [Draft Fach](Draft_Tray/de.md) and [Draft Fangen](Draft_Snap/de.md).

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Text.svg" width=16px> [Text](Draft_Text/de.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_Text.svg" width=16px> Text** auswählen.
    -   Das Tastaturkürzel **T** dann **E**.
2.  Der Aufgabenbereich **Text** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
3.  Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
4.  Den gewünschten Text eingeben, **Enter** drücken, um eine neue Zeile zu beginnen.
5.  Zweimal **Enter** drücken oder die Schaltfläche **<img src="images/Button_valid.svg" width=16px> Text erstellen** drücken, um den Befehl abzuschließen.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **N**drücken oder die Checkbox **Fortsetzen** aktivieren, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet und ermöglicht so mit dem Erstellen von Texten fortzufahren. Das Tastaturkürzel funktioniert nicht im zweiten Aufgaben-Bereich. Diese Option steht in FreeCAD Version 0.19 oder davor im ersten Aufgaben-Bereich nicht zur Verfügung.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Ein Draft-Text kann durch Doppelklick in der [Baumansicht](Tree_view/de.md) zum Bearbeiten geöffnet werden. {{Version/de|0.20}}
-   Mit [FreeCAD Version 0.21](Release_notes_0.21/de.md) erstellte oder gesicherte Draft-Texte sind nicht abwärtskompatibel.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft Text-Objekt ist von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Die folgenden sind, wenn nicht anders angegeben, zusätzliche Eigenschaften:



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Placement|Placement}}: Legt die Position des Textes in der [3D-Ansicht](3D_view/de.md) fest. Siehe [Positionierung](Placement/de.md).

-    {{PropertyData/de|Text|StringList}}: Legt den Inhalt des Textes fest. Jeder Eintrag in der Liste entspricht einer neuen Textzeile.



### Ansicht


{{TitleProperty|Annotation}}

-    {{PropertyView/de|Annotation Style|Enumeration}}: Gibt den Beschriftungsstil an, der für den Text verwewendet wird. Siehe [Draft BeschriftungsstilEditor](Draft_AnnotationStyleEditor/de.md).

-    {{PropertyView/de|Scale Multiplier|Float}}: Gibt den allgemeinen Skalierungsfaktor an, der für den Text verwewendet wird.


{{TitleProperty|Display Options}}

-    {{PropertyView/de|Display Mode|Enumeration}}: Gibt an, wie der Text angezeigt wird. Ist es {{value|World}}, wird der Text auf einer Ebene angezeigt, die durch seine {{PropertyData/de|Placement}} festgelegt wird. Ist es {{value|Screen}}, wird der Text immer in Richtung Bildschirm angezeigt. Dies ist eine übernommene Eigenschaft. Die genannten Optionen sind die umbenannten Optionen ({{Version/de|0.21}}).


{{TitleProperty|Graphics}}

-    {{PropertyView/de|Line Color|Color}}: nicht verwendet.

-    {{PropertyView/de|Line Width|Float}}: nicht verwendet.


{{TitleProperty|Text}}

-    {{PropertyView/de|Font Name|Font}}: Gibt die Schriftart an, die zum Zeichnen des Textes verwendet werden soll. Es kann ein Schriftname wie {{value|Arial}} sein, ein Standardstil wie {{value|sans}}, {{value|serif}} oder {{value|mono}}, eine Familie wie {{value|Arial,Helvetica,sans}}, oder ein Name mit einem Stil wie {{value|Arial:Bold}}. Wenn die angegebene Schriftart nicht auf dem System gefunden wird, wird stattdessen eine Standardschriftart verwendet.

-    {{PropertyView/de|Font Size|Length}}: Gibt die Höhe der Schriftzeichen an. Der Text kann unsichtbar sein in der [3D-Ansicht](3D_view.md), wenn dieser Wert sehr klein ist.

-    {{PropertyView/de|Justification|Enumeration}}: Legt die Ausrichtung des Textes fest: {{value|Left}} (links), {{value|Center}} (zentriert) oder {{value|Right}} (rechts).

-    {{PropertyView/de|Line Spacing|Float}}: Legt den Faktor fest, der auf die voreingestellte Zeilenhöhe des Textes angewendet wird.

-    {{PropertyView/de|Text Color|Color}}: Legt die Farbe des Textes fest.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-Textes wird die Methode `make_text` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeText`.


```python
text = make_text(string, placement=None, screen=False)
```

-   Erstellt ein `text`-Objekt, an einer Position `placement`, die ein `FreeCAD.Placement` sein kann, aber auch eine `FreeCAD.Rotation` oder ein `FreeCAD.Vector`.

-    `string`ist eine Zeichenkette oder eine Liste von Zeichenketten. Wenn es eine Liste ist, wird jedes Element einer auf seiner eigenen Zeile angezeigt.

-   Wenn `screen` auf `True` gesetzt ist, wird der Text immer zur Kamera ausgerichtet, andernfalls wird er auf einer Ebene dargestellt, die von der {{PropertyData/de|Placement}} festgelegt wird.

Die Ansicht-Eigenschaften von `text` können durch Überschreiben seiner Attribute geändert werden; z.B. `ViewObject.FontSize` (Schrifthöhe) mit einem neuen Wert in Millimetern überschreiben.

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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/de
