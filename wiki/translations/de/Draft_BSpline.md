---
- GuiCommand:/de
   Name:Draft BSpline
   Name/de:Entwurf BSpline
   MenuLocation:Entwurf → BSpline
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Shortcut:**B** **S**
   Version:0.7
   SeeAlso:[Entwurf Polygonzug](Draft_Wire/de.md), [Entwurf Bézkurve](Draft_BezCurve/de.md)
---

# Draft BSpline/de

## Beschreibung

Der <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> **Entwurf BSpline** Befehl erstellt eine [B-Spline Kurve](https://de.wikipedia.org/wiki/Spline#B-Splines) aus mehreren Punkten.

Der Entwurf BSpline Befehl legt die **exakten Punkte** fest, durch die die Kurve verlaufen soll. Die [Entwurf BezKurve](Draft_BezCurve/de.md) und [Entwurf KubischeBezKurve](Draft_CubicBezCurve/de.md) Befehle hingegen verwenden **Kontrollpunkte**, um die Position und Krümmung des Splines zu definieren.

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Spline festgelegt durch mehrere Punkte*

## Anwendung

Siehe auch: [Entwurf Ablage](Draft_Tray/de.md), [Entwurf Fang](Draft_Snap/de.md) und [Entwurf beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
2.  Drücke die **<img src="images/Draft_BSpline.svg" width=16px> [ Entwurf BSpline](Draft_BSpline/de.md)** Schaltfläche.
    -   Wähle die **Entwerfen → <img src="images/Draft_BSpline.svg" width=16px> B-Spline** Option aus dem Menü.
    -   Verwende das Tastaturkürzel: **B** dann **S**.
3.  Das **B-spline** Aufgabenpaneel wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
4.  Nimm den ersten Punkt in der in der [3D Ansicht](3D_view/de.md) oder gib Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
5.  Nimm weitere Punkte in der [3D Ansicht](3D_view/de.md) oder gib Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
6.  Drücke **Esc** oder die **Schließen** Schaltfläche zum Beenden des Befehls.

## Optionen

Die im Aufgabenpaneel verfügbaren Einzelzeichen Tastaturkürzel können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.


<div class="mw-translate-fuzzy">

-   Um Koordinaten manuell einzugeben, gib die X, Y und Z Komponente ein und drücke jeweils die **Enter**. Oder du kannst die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken, wenn du die gewünschten Werte hast. Es ist ratsam, den Mauszeiger aus der [3D Ansicht](3D_view/de.md) zu bewegen, bevor Koordinaten eingegeben werden.
-   Drücke **R** oder klicke auf das Kontrollkästchen **Relativ**, um den relativen Modus zu aktivieren. Wenn der relative Modus eingeschaltet ist, sind die Koordinaten relativ zum letzten Punkt, falls vorhanden, ansonsten relativ zum Ursprung des Koordinatensystems.
-   Drücke **G** oder klicke auf das Kontrollkästchen **Global**, um den globalen Modus umzuschalten. Wenn der globale Modus eingeschaltet ist, beziehen sich die Koordinaten auf das globale Koordinatensystem, ansonsten auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}
-   Drücke **L** oder klicke auf das Kontrollkästchen **Gefüllt**, um den ausgefüllten Modus umzuschalten. Wenn der gefüllte Modus eingeschaltet ist, hat der erzeugte Spline **Make Face** auf `True` gesetzt und hat eine gefüllte Fläche, vorausgesetzt sie ist geschlossen und schneidet sich nicht selbst. Beachte, dass ein sich selbst schneidender Spline mit einer Fläche nicht richtig angezeigt wird, für einen solchen Spline muss **Make Face** auf `False` gesetzt werden.
-   Drücke **T** oder klicke auf das Kontrollkästchen **Weiter**, um den Fortsetzungsmodus zu aktivieren. Wenn der Fortsetzungsmodus eingeschaltet ist, wird der Befehl nach der Verwendung von **<img src="images/Draft_FinishLine.svg" width=16px> Beenden** oder **<img src="images/Draft_CloseLine.svg" width=16px> Schließen**, oder nach dem Erstellen eines geschlossenen Splines durch Fangen am ersten Punkt des Splines, so dass du weiter Splines erstellen kannst.
-   Drücke den **<img src="images/Draft_UndoLine.svg" width=16px> Rückgängig**, um den letzten Punkt rückgängig zu machen. Das Tastaturkürzel **Strg**+**Z** funktioniert derzeit nicht.
-   Drücke **A** oder die **<img src="images/Draft_FinishLine.svg" width=16px> Fertigstellen**, um den Befehl zu beenden und den Spline offen zu lassen.
-   Drücke **O** oder den **<img src="images/Draft_CloseLine.svg" width=16px> Schließen**, um den Befehl zu beenden und den Spline zu schließen. Ein geschlossener Spline kann auch durch Fangen am ersten Punkt des Splines erstellt werden.
-   Drücke **W** oder den **<img src="images/Draft_Wipe.svg" width=16px> Wischen** Taste, um die bereits platzierten Kurvensegmente zu löschen, aber vom letzten Punkt aus weiterzuarbeiten.
-   Drücke **U** oder den **<img src="images/Draft_SelectPlane.svg" width=16px> [Setze Arbeitsebene](Draft_SelectPlane/de.md)**, um die aktuelle Arbeitsebene in der durch den letzten und den vorherigen Punkt definierten Ausrichtung anzupassen.
-   Drücke **S**, um [Entwurf Fangen ](Draft_Snap/de.md) ein- oder auszuschalten.
-   Drücke **Esc** oder die Taste {{button|Schliessen}}, um den Befehl zu beenden.


</div>

## Hinweise

-   Ein Entwurf BSpline kann mit dem Befehl [Entwurf Editieren](Draft_Edit/de.md) bearbeitet werden.
-   Ein Entwurf BSpline kann mit dem Befehl [Entwurf Draht](Draft_Wire/de.md) in eine [Entwurf DrahtZuBSpline](Draft_WireToBSpline/de.md) umgewandelt werden.

## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen zu ändern, die bei der Eingabe von Koordinaten verwendet werden: **Bearbeiten → Einstellungen... → Allgemein → Einheiten → Einheiteneinstellungen → Anzahl der Dezimalstellen**.
-   Um den Anfangswert des Füllmodus zu ändern: **Bearbeiten → Einstellungen... → Entwurf → Allgemeine Einstellungen → Entwurf Werkzeuge Optionen → Objekte mit Flächen füllen, wann immer möglich**. Ändern des Füllmodus in einem Aufgabenpaneel, wird diese Voreinstellung für die aktuelle FreeCAD Sitzung überschreiben.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Entwurf BSpline Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{TitleProperty|Draft}}

-    **Area|Area**: (nur Lesezugriff) gibt den Bereich der Fläche des Splines an. Der Wert ist {{value|0.0}}, wenn **Make Face** auf `False` steht oder die Fläche nicht erstellt werden kann.

-    **Closed|Bool**: gibt an, ob der Spline geschlossen ist oder nicht. Wenn der Spline anfänglich offen ist, ist dieser Wert `False`, wenn er auf `True` gesetzt wird, wird ein Kurvensegment gezeichnet, um den Spline zu schließen. Wenn der Spline anfänglich geschlossen ist, ist dieser Wert `True`, wenn man ihn auf `False` setzt, wird das letzte Kurvensegment entfernt und der Spline wird offen.

-    **Make Face|Bool**: gibt an, ob der Spline eine Fläche bildet oder nicht. Wenn es `True` ist, wird eine Fläche erstellt, ansonsten wird nur der Umfang als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn **Closed** `True` ist und wenn der Spline sich nicht selbst schneidet.

-    **Parameterization|Float**: beeinflusst die Form des Splines.

-    **Points|VectorList**: gibt die Punkte des Splines in seinem lokalen Koordinatensystem an.

### Ansicht


{{TitleProperty|Draft}}

-    **Pfeilgröße|Länge**: legt die Größe des Symbols fest, das am Ende des Splines angezeigt wird.

-    **Pfeiltyp|Nummerierung**: gibt die Art des Symbols an, das am Ende des Splines angezeigt wird, das kann {{value|Punkt}}, {{value|Kreis}}, {{value|Pfeil}}, {{value|Häkchen}} oder {{value|Häkchen-2}} sein.

-    **Pfeilende|Bool**: gibt an, ob ein Symbol am Ende des Splines angezeigt werden soll, so dass er als Anmerkungslinie verwendet werden kann.

-    **Muster|Nummerierung**: legt das [Entwurf Muster](Draft_Pattern/de.md) fest, mit dem die Fläche des geschlossenen Splines gefüllt werden soll. Diese Eigenschaft funktioniert nur, wenn **Make Face** `True` ist und wenn **Display Mode** {{value|Flat Lines}} ist.

-    **Muster Größe|Float**: gibt die Größe des [Entwurf Muster](Draft_Pattern/de.md) an.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um einen Entwurf BSpline zu erstellen, verwende die Methode `make_bspline` ({{Version/de|0.19}}) des Entwurf Moduls. Diese Methode ersetzt die veraltete `makeBSpline` Methode.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Erstellt ein `bspline` Objekt aus der angegebenen Liste von Punkten `Punkteliste`.
    -   Jeder Punkt in der Liste ist durch seinen `FreeCAD.Vector` definiert, mit Einheiten in Millimetern.
    -   Alternativ kann die Eingabe auch ein `Part.Wire` sein, aus dem Punkte extrahiert werden.
-   Wenn `closed` `True` ist, oder wenn der erste und letzte Punkt identisch sind, ist der Spline geschlossen.
-   Wenn `placement` `None` ist, wird der Spline am Ursprung erstellt.
-   Wenn `face` `True` ist, und der Spline geschlossen ist, bildet der Spline eine Fläche, d. h. er erscheint gefüllt.

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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/de
