---
 GuiCommand:
   Name: Draft BSpline
   Name/de: Draft BSpline
   MenuLocation: Zeichnen , B-Spline
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **B** **S**
   Version: 0.7
   SeeAlso: Draft_Wire/de, Draft_BezCurve/de
---

# Draft BSpline/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> **Draft B-Spline** erstellt eine [B-Spline-Kurve](https://de.wikipedia.org/wiki/Spline#B-Splines) aus mehreren Punkten.

Der Befehl Draft B-Spline legt die **exakten Punkte** fest, durch die die Kurve verlaufen soll. Die Befehle [Draft Bézierkurve](Draft_BezCurve/de.md) und [Draft KubischeBézierkurve](Draft_CubicBezCurve/de.md) verwenden andererseits **Kontrollpunkte**, um die Position und Krümmung des Splines zu definieren.

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Spline festgelegt durch mehrere Punkte*



## Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:

2.  Die Schaltfläche **<img src="images/Draft_BSpline.svg" width=16px> [BSpline](Draft_BSpline/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_BSpline.svg" width=16px> B-Spline** auswählen.
    -   Das Tastaturkürzel: **B** dann **S**.

3.  Der Aufgaben-Bereich **B-spline** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.

4.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.

5.  Weitere Punkte in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.

6.  
    **Esc**oder die Schaltfläche **Schließen** drücken. um den Befehl zu beenden.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Um die Koordinaten manuell einzugeben, werden die X-, Y- und Z-Komponente eingegeben und nach jeder Eingabe **Eingabe** (Enter) gedrückt. Man kann auch die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken, wenn die gewünschten Werte vorhanden sind.Es ist ratsam, vor der Eingabe der Koordinaten, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen.

-    **R**drücken oder das Kontrollkästchen **Relativ** anklicken, um den Relativ-Modus umzuschalten. Wenn der Relativ-Modus eingeschaltet ist, sind die Koordinaten relativ zum letzten Punkt, falls vorhanden, ansonsten beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder das Kontrollkästchen **Global** anklicken, um den Global-Modus umzuschalten. Wenn der Global-Modus eingeschaltet ist, beziehen sich die Koordinaten auf das globale Koordinatensystem, ansonsten auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **F**drücken oder das Kontrollkästchen **Füllen** anklicken, um den Füllmodus umzuschalten. Wenn der Füllmodus eingeschaltet ist, wird die {{PropertyData/de|Make Face}} der erstellten Kurve auf `True` gesetzt und die Kurve erhält eine gefüllte Fläche, vorausgesetzt, dass sie geschlossen ist und sich nicht selbst schneidet. Beachte, dass eine sich selbst schneidende Kurve mit einer Fläche nicht richtig angezeigt wird, für eine solche Kurve muss die {{PropertyData/de|Make Face}} auf `False` gesetzt werden.

-    **N**drücken oder das Kontrollkästchen **Fortsetzen** anklicken, um den Fortsetzungsmodus umzuschalten. Wenn der Fortsetzungsmodus eingeschaltet ist, wird der Befehl nach Betätigung von **[16px](IMage:Draft_FinishLine.svg.md) Fertigstellen** oder **<img src="images/Draft_CloseLine.svg" width=16px> Schließen**, und auch nach dem Erstellen eines geschlossenen Splines, durch Einrasten auf den ersten Punkt des Splines, erneut gestartet, und es kann mit dem Erstellen von Splines fortgefahren werden.

-    **/**oder die Schaltfläche **<img src="images/Draft_UndoLine.svg" width=16px> Rückgängig** drücken, um den letzten Punkt rückgängig zu machen.

-    **A**oder die Schaltfläche **<img src="images/Draft_FinishLine.svg" width=16px> Fertigstellen** drücken, um den Befehl zu beenden und die Kurve offen zu lassen.

-    **O**oder die Schaltfläche **<img src="images/Draft_CloseLine.svg" width=16px> Schließen** drücken, um den Befehl zu beenden und den Spline zu schließen. Ein geschlossener Spline kann auch durch Einrasten auf den ersten Punkt des Splines erstellt werden.

-    **W**oder die Schaltfläche **<img src="images/Draft_Wipe.svg" width=16px> Radieren** drücken, um die bereits positionierten Kurvenabschnitte zu löschen, aber vom letzten Punkt aus weiterzuarbeiten.

-    **U**oder die Schaltfläche **<img src="images/Draft_SelectPlane.svg" width=16px> [Arbeitsebene festelegen](Draft_SelectPlane/de.md)** drücken, um die aktuelle Arbeitsebene der durch den letzten und den vorherigen Punkt definierten Ausrichtung anzupassen.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- oder auszuschalten.

-    **Esc**oder die Schaltfläche **Schliessen** drücken, um den Befehl zu beenden.



## Hinweise

-   Ein Draft BSpline kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.
-   Ein Draft BSpline kann mit dem Befehl [Draft DrahtZuBSpline](Draft_WireToBSpline/de.md) in eine [Draft Polylinie](Draft_Wire/de.md) umgewandelt werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-B-Spline (BSpline-Objekt) wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    {{PropertyData/de|Area|Area}}: (schreibgeschützt) gibt den Flächeninhalt der von dem Spline umschlossenen Fläche an. Der Wert ist {{value|0.0}}, wenn {{PropertyData/de|Make Face}} auf `False` gesetzt ist oder die Fläche nicht erstellt werden kann.

-    {{PropertyData/de|Closed|Bool}}: gibt an, ob der Spline geschlossen ist oder nicht. Wenn der Spline anfänglich offen ist, ist dieser Wert `False`, wenn er auf `True` gesetzt wird, wird ein Kurvensegment gezeichnet, um den Spline zu schließen. Wenn der Spline anfänglich geschlossen ist, ist dieser Wert `True`, wenn man ihn auf `False` setzt, wird das letzte Kurvensegment entfernt und der Spline geöffnet.

-    {{PropertyData/de|Make Face|Bool}}: gibt an, ob der Spline eine Fläche bildet oder nicht. Wenn es `True` ist, wird eine Fläche erstellt, ansonsten wird nur der Umriss als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Closed}} `True` ist und wenn der Spline sich nicht selbst schneidet.

-    {{PropertyData/de|Parameterization|Float}}: beeinflusst die Form des Splines.

-    {{PropertyData/de|Points|VectorList}}: gibt die Punkte des Splines in seinem lokalen Koordinatensystem an.



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Arrow Size|Length}}: legt die Größe des Symbols fest, das am Ende des Splines angezeigt wird.

-    {{PropertyView/de|Arrow Type|Enumeration}}: gibt die Art des Symbols an, das am Ende des Splines angezeigt wird; es kann die Werte {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} oder {{value|Tick-2}} annehmen.

-    {{PropertyView/de|End Arrow|Bool}}: gibt an, ob am Ende des Splines ein Symbol angezeigt werden soll, damit er als Hinweislinie für Beschritung verwendet werden kann.

-    {{PropertyView/de|Pattern|Enumeration}}: legt das [Draft Muster](Draft_Pattern/de.md) fest, mit dem die Fläche des geschlossenen Splines gefüllt werden soll. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Make Face}} auf `True` gesetzt und die {{PropertyView/de|Display Mode}} auf {{value|Flat Lines}} gesetzt ist.

-    {{PropertyView/de|Pattern Size|Float}}: legt die Größe des [Draft Musters](Draft_Pattern/de.md) fest.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-B-Splines (BSpline-Objekt) wird die Methode `make_bspline` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeBSpline`.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Erstellt ein `BSpline`-Objekt mit der vorgegebenen Liste von Punkten, `pointslist`.
    -   Jeder Punkt in der Liste wird durch seinen `FreeCAD.Vector` festgelegt, mit Einheiten in Millimetern.
    -   Alternativ kann die Eingabe auch ein `Part.Wire` sein, aus dem Punkte extrahiert werden.
-   Ist `closed` auf `True` gesetzt, oder wenn der erste und letzte Punkt identisch sind, ist der Spline geschlossen.
-   Ist `placement` auf `None` gesetzt, wird der Spline am Ursprung erstellt.
-   Ist `face` auf `True` gesetzt, und der Spline geschlossen, ergibt der Spline eine Fläche, d. h. er erscheint gefüllt.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/de
