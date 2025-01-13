---
 GuiCommand:
   Name: Draft BezCurve
   Name/de: Draft Bézierkurve
   MenuLocation: Zeichnen , Bézierwerkzeuge , Bézierkurve<br>2D-Entwurf , Bézierkurve
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **B** **Z**
   Version: 0.14
   SeeAlso: Draft_CubicBezCurve/de, Draft_BSpline/de
---

# Draft BezCurve/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> **Draft Bézierkurve** erstellt eine [Bézierkurve](https://de.wikipedia.org/wiki/B%C3%A9zierkurve) aus einigen Punkten.

Der Befehl erstellt eine einzelne Bézierkurve mit einer {{PropertyData/de|Grad}}, die der `Anzahl_der_Punkte - 1` entspricht. Sie kann in eine stückweise Bézierkurve geändert werden, durch veringern dieser Eigenschaft .

Die Befehle Draft Bézierkurve und [Draft KubischeBézierkurve](Draft_CubicBezCurve/de.md) verwenden **Kontrollpunkte**, um die Position und Krümmung des Splines zu definieren. Der Befehl [Draft BSpline](Draft_BSpline/de.md) andererseits legt die **exakten Punkte** fest, durch die die Kurve verlaufen soll.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Bézierkurve definiert durch mehrere Punkte*



## Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_BezCurve.svg" width=16px> [Bézierkurve](Draft_BezCurve/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen → Bézierwerkzeuge → <img src="images/Draft_BezCurve.svg" width=16px> Bézierkurve** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **2D-Entwurf → <img src="images/Draft_BezCurve.svg" width=16px> Bézierkurve** auswählen.
    -   Das Tastaturkürzel **B** dann **Z**.

2.  Der Aufgaben-Bereich **Bézierkurve** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.

3.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.

4.  Weitere Punkte in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.

5.  
    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl zu beenden.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Um die Koordinaten manuell einzugeben, werden die X-, Y- und Z-Komponente eingegeben und nach jeder Eingabe **Eingabe** (Enter) gedrückt. Man kann auch die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken, wenn die gewünschten Werte vorhanden sind. Es ist ratsam, vor der Eingabe der Koordinaten, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen.

-    **R**drücken oder das Kontrollkästchen **Relativ** anklicken, um den Relativ-Modus umzuschalten. Wenn der Relativ-Modus eingeschaltet ist, sind die Koordinaten relativ zum letzten Punkt, falls vorhanden, ansonsten beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder das Kontrollkästchen **Global** anklicken, um den Global-Modus umzuschalten. Wenn der Global-Modus eingeschaltet ist, beziehen sich die Koordinaten auf das globale Koordinatensystem, ansonsten auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **F**drücken oder das Kontrollkästchen **Füllen** anklicken, um den Füllmodus umzuschalten. Wenn der Füllmodus eingeschaltet ist, wird die {{PropertyData/de|Make Face}} der erstellten Kurve auf `True` gesetzt und die Kurve erhält eine gefüllte Fläche, vorausgesetzt, dass sie geschlossen ist und sich nicht selbst schneidet. Beachte, dass eine sich selbst schneidende Kurve mit einer Fläche nicht richtig angezeigt wird, für eine solche Kurve muss die {{PropertyData/de|Make Face}} auf `False` gesetzt werden.

-    **N**drücken oder das Kontrollkästchen **Fortsetzen** anklicken, um den Fortsetzungsmodus umzuschalten. Wenn der Fortsetzungsmodus eingeschaltet ist, wird der Befehl nach Betätigung von **[16px](IMage:Draft_FinishLine.svg.md) Fertigstellen** oder **<img src="images/Draft_CloseLine.svg" width=16px> Schließen**, und auch nach dem Erstellen einer geschlossenen Kurve, durch Einrasten aufden ersten Punkt der Kurve, erneut gestartet, und es kann mit dem Erstellen von Kurven fortgefahren werden.

-    **/**oder die Schaltfläche **<img src="images/Draft_UndoLine.svg" width=16px> Rückgängig** drücken, um den letzten Punkt rückgängig zu machen.

-    **A**oder die Schaltfläche **<img src="images/Draft_FinishLine.svg" width=16px> Fertigstellen** drücken, um den Befehl zu beenden und die Kurve offen zu lassen.

-    **O**oder die Schaltfläche **<img src="images/Draft_CloseLine.svg" width=16px> Schließen** drücken, um den Befehl zu beenden und die Kurve zu schließen. Eine geschlossene Kurve kann auch durch Einrasten auf den ersten Punkt der Kurve erstellt werden.

-    **W**oder die Schaltfläche **<img src="images/Draft_Wipe.svg" width=16px> Radieren** drücken, um die bereits positionierten Abschnitte zu löschen, aber vom letzten Punkt aus weiterzuarbeiten.

-    **U**oder die Schaltfläche **<img src="images/Draft_SelectPlane.svg" width=16px> [Arbeitsebene festelegen](Draft_SelectPlane/de.md)** drücken, um die aktuelle Arbeitsebene der durch den letzten und den vorherigen Punkt definierten Ausrichtung anzupassen.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- oder auszuschalten.

-    **Esc**oder die Schaltfläche **Schliessen** drücken, um den Befehl zu beenden.



## Hinweise

-   Eine Draft Bézierkurve kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.
-   OpenCascade, und dadurch FreeCAD, unterstützt keine Bézierkurven mit einem Grad größer als 25. Dies sollte in der Praxis kein Problem sein, weil die meisten Benutzer typischerweise Bézierkurven vom Grad 3 bis 5 verwenden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft Bézierkurven-Objekt (BezCurve object) wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    {{PropertyData/de|Area|Area}}: (schreibgeschützt) gibt den Flächeninhalt der von der Kurve umschlossenen Fläche an. Der Wert ist {{value|0.0}}, wenn {{PropertyData/de|Make Face}} auf `False` gesetzt ist oder die Fläche nicht erstellt werden kann.

-    {{PropertyData/de|Closed|Bool}}: gibt an, ob die Kurve geschlossen ist oder nicht. Wenn die Kurve anfänglich offen ist, ist dieser Wert `False`, wenn er auf `True` gesetzt wird, wird ein Segment gezeichnet, um die Kurve zu schließen. Wenn die Kurve anfänglich geschlossen ist, ist dieser Wert `True`, wenn er auf `False` gesetzt wird, wird das letzte Segment entfernt und die Kurve geöffnet.

-    {{PropertyData/de|Stetigkeit|IntegerList}}: (schreibgeschützt) gibt die Stetigkeit der Kurve an.

-    {{PropertyData/de|Degree|Integer}}: gibt den Grad der Kurve an.

-    {{PropertyData/de|Length|Length}}: (schreibgeschützt) gibt die Gesamtlänge der Kurve an.

-    {{PropertyData/de|Make Face|Bool}}: legt fest, ob die Kurve eine Fläche bildet oder nicht. Wenn auf `True` gesetzt, wird eine Fläche erzeugt, ansonsten wird nur der Umriss als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Closed}} auf `True` gesetzt ist und wenn die Kurve sich nicht selbst schneidet.

-    {{PropertyData/de|Points|VectorList}}: gibt die Kontrollpunkte der Kurve in ihrem lokalen Koordinatensystem an.



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Arrow Size|Length}}: legt die Größe des Symbols fest, das am Ende der Kurve angezeigt wird.

-    {{PropertyView/de|Arrow Type|Enumeration}}: gibt die Art des Symbols an, das am Ende der Kurve angezeigt wird; es kann die Werte {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} oder {{value|Tick-2}} annehmen.

-    {{PropertyView/de|End Arrow|Bool}}: gibt an, ob am Ende der Kurve ein Symbol angezeigt werden soll, damit sie als Hinweislinie für Beschritung verwendet werden kann.

-    {{PropertyView/de|Pattern|Enumeration}}: legt das [Draft Muster](Draft_Pattern/de.md) fest, mit dem die Fläche der geschlossenen Kurve gefüllt werden soll. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Make Face}} auf `True` gesetzt und die {{PropertyView/de|Display Mode}} auf {{value|Flat Lines}} gesetzt ist.

-    {{PropertyView/de|Pattern Size|Float}}: legt die Größe des [Draft Musters](Draft_Pattern/de.md) fest.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Draft-Bézierkurve (BezCurve-Objekt) wird die Methode `make_bezcurve` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeBezCurve`.


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```

-   Erstellt ein `BezCurve`-Objekt mit der vorgegebenen Liste von Punkten, `pointslist`.
    -   Jeder Punkt in der Liste wird durch seinen `FreeCAD.Vector` festgelegt, mit Einheiten in Millimetern.
    -   Alternativ kann die Eingabe auch ein `Part.Wire` sein, aus dem Punkte extrahiert werden.
-   Ist `closed` auf `True` gesetzt, oder wenn der erste und letzte Punkt identisch sind, ist die Kurve geschlossen.
-   Ist `placement` auf `None` gesetzt, wird die Kurve am Ursprung erzeugt.
-   Ist `face` auf `True` gesetzt, und die Kurve geschlossen, ergibt die Kurve eine Fläche, d. h. sie erscheint gefüllt.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)
p4 = App.Vector(1500, -2000, 0)

bezcurve1 = Draft.make_bezcurve([p1, p2, p3, p4], closed=True)
bezcurve2 = Draft.make_bezcurve([p4, 1.3*p2, p1, 4.1*p3], closed=True)
bezcurve3 = Draft.make_bezcurve([1.7*p3, 1.5*p4, 2.1*p2, p1], closed=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/de
