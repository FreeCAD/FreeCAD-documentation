---
- GuiCommand:
   Name: Draft BezCurve
   Name/de: Entwurf BezKurve
   MenuLocation: Entwurf -> Bézierwerkzeuge -> BézKurve
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **B** **Z**
   Version: 0.14
   SeeAlso: Draft_CubicBezCurve/de, Draft_BSpline/de
---

# Draft BezCurve/de



## Beschreibung

Der <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> **Entwurf BezKurve** Befehl erstellt eine [Bézierkurve](https://de.wikipedia.org/wiki/B%C3%A9zierkurve) aus einigen Punkten.

Der Befehl erstellt eine einzelne Bézierkurve mit einem **Grad** der `Anzahl_der_Punkte - 1` ist. Es kann in eine stückweise Bézierkurve durch reduzieren dieser Eigenschaft geändert werden.

Der Entwurf BezKurve und [Entwurf KubischeBezKurve](Draft_CubicBezCurve/de.md) Befehl verwendet **Kontrollpunkte**, um die Position und Krümmung des Splines zu definieren. Der [Entwurf BSpline](Draft_BSpline.md) Befehl andererseits legt die **exakten Punkte** fest, durch die die Kurve verlaufen soll.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Bézierkurve definiert durch mehrere Punkte*



## Anwendung

Siehe auch: [Entwurf Ablage](Draft_Tray/de.md), [Entwurf Fang](Draft_Snap/de.md) und [Entwurf beschränken](Draft_Constrain/de.md).


<div class="mw-translate-fuzzy">

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_BezCurve.svg" width=16px> [Entwurf BezKurve](Draft_BezCurve/de.md)** Schaltfläche.
    -   Wähle die **Entwurf → Bézier Werkzeuge → <img src="images/Draft_BezCurve.svg" width=16px> Bézier Kurve** Option aus dem Menü.
2.  Das **Bézier Kurve** Aufgabenpaneel wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Nimm den ersten Punkt in der [3D Ansicht](3D_view/de.md) oder gib die Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
4.  Nimm weitere Punkte in der [3D Ansicht](3D_view/de.md) oder gib die Koordinaten ein und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche.
5.  Drücke **Esc** oder die **Schließen** Schaltfläche zum Beenden des Befehls.


</div>



## Optionen

Die im Aufgabenpaneel verfügbaren Einzelzeichen Tastaturkürzel können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.


<div class="mw-translate-fuzzy">

-   Um die Koordinaten manuell einzugeben, gib die X, Y und Z Komponente ein und drücke nach jeder Eingabe **Eingabe**. Oder du kannst die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** Schaltfläche drücken, wenn du die gewünschten Werte hast. Es ist ratsam, vor der Eingabe der Koordinaten, den Mauszeiger aus der [3D Ansicht](3D_view/de.md) zu bewegen.
-   Drücke **R** oder klicke auf das Kontrollkästchen **Relativ**, um den relativen Modus einzuschalten. Wenn der relative Modus eingeschaltet ist, sind die Koordinaten relativ zum letzten Punkt, falls vorhanden, ansonsten relativ zum Ursprung des Koordinatensystems.
-   Drücke **G** oder klicke auf das Kontrollkästchen **Global**, um den globalen Modus umzuschalten. Wenn der globale Modus eingeschaltet ist, sind die Koordinaten relativ zum globalen Koordinatensystem, ansonsten sind sie relativ zum Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). <small>(v0.20)</small> 
-   Drücke **L** oder klicke auf das Kontrollkästchen **Gefüllt**, um den gefüllten Modus umzuschalten. Wenn der Füllmodus eingeschaltet ist, hat die erzeugte Kurve **Mache Fläche** auf `True` gesetzt und hat eine gefüllte Fläche, vorausgesetzt, sie ist geschlossen und schneidet sich nicht selbst. Beachte, dass eine sich selbst schneidende Kurve mit einer Fläche nicht richtig angezeigt wird, für eine solche Kurve muss **Mache Fläche** auf `False` gesetzt werden.
-   Drücke **T** oder klicke auf das Kontrollkästchen **Weiter**, um den Fortsetzungsmodus umzuschalten. Wenn der Fortsetzungsmodus eingeschaltet ist, wird der Befehl nach Betätigung von **[16px](IMage:Draft_FinishLine.svg.md) Beenden** oder **<img src="images/Draft_CloseLine.svg" width=16px> Schließen**, oder nach dem Erstellen einer geschlossenen Kurve, durch fangen des ersten Punkts der Kurve, kannst du mit dem Erstellen von Kurven fortfahren.
-   Drücke die **<img src="images/Draft_UndoLine.svg" width=16px> Rückgängig** Schaltfläche, um den letzten Punkt rückgängig zu machen. Das **Strg**+**Z** Tastaturkürzel funktioniert derzeit nicht.
-   Drücke **A** oder die **<img src="images/Draft_FinishLine.svg" width=16px> Fertigstellen** Schaltfläche, um den Befehl zu beenden und die Kurve offen zu lassen.
-   Drücke **O** oder die **<img src="images/Draft_CloseLine.svg" width=16px> Schließen** Schaltfläche, um den Befehl zu beenden und die Kurve zu schließen. Eine geschlossene Kurve kann auch durch Fangen am ersten Punkt der Kurve erstellt werden.
-   Drücke **W** oder die **<img src="images/Draft_Wipe.svg" width=16px> Wischen** Taste, um die bereits platzierten Segmente zu löschen, aber vom letzten Punkt aus weiterzuarbeiten.
-   Drücke die **U** oder den **<img src="images/Draft_SelectPlane.svg" width=16px> [Festelegen AE](Draft_SelectPlane/de.md)**, um die aktuelle Arbeitsebene in der durch den letzten und den vorherigen Punkt definierten Ausrichtung anzupassen.
-   Drücke **S** um [Entwurf Fangen](Draft_Snap/de.md) ein- oder auszuschalten.
-   Drücke **Esc** oder die Schaltfläche **Schliessen**, um den Befehl zu beenden.


</div>



## Hinweise

-   Eine Entwurf BezKurve kann mit dem Befehl [Entwurf Bearbeiten](Draft_Edit/de.md) bearbeitet werden.
-   OpenCascade, und dadurch FreeCAD, unterstützt keine Bézierkurven mit einem Grad größer als 25. Dies sollte in der Praxis kein Problem sein, weil die meisten Benutzer typischerweise Bézierkurven vom Grad 3 bis 5 verwenden.



## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen, die bei der Eingabe von Koordinaten verwendet werden: **Bearbeiten → Einstellungen... → Allgemein → Einheiten → Einheiteneinstellungen → Anzahl der Dezimalstellen**.
-   Um den Anfangswert des Füllmodus zu ändern: **Bearbeiten → Einstellungen... → Entwurf → Allgemeine Einstellungen → Entwurf Werkzeuge Optionen → Objekte mit Flächen füllen, wann immer möglich**. Ändern des Füllmodus in einem Aufgabenpaneel, wird diese Einstellung für die aktuelle FreeCAD Sitzung überschreiben.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Entwurf BezKurve Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Entwurf}}

-    **Area|Area**: (schreibgeschützt) gibt die Fläche der Kurvenfläche an. Der Wert ist {{value|0.0}}, wenn **Make Face** auf `False` steht oder die Fläche nicht erstellt werden kann.

-    **Closed|Bool**: gibt an, ob die Kurve geschlossen ist oder nicht. Wenn die Kurve anfänglich offen ist, ist dieser Wert `False`, wenn er auf `True` gesetzt wird, wird ein Segment gezeichnet, um die Kurve zu schließen. Wenn die Kurve anfänglich geschlossen ist, ist dieser Wert `True`, wenn er auf `False` gesetzt wird, wird das letzte Segment entfernt und die Kurve wird offen.

-    **Continuity|IntegerList**: (schreibgeschützt) gibt die Kontinuität der Kurve an.

-    **Degree|Integer**: gibt den Grad der Kurve an.

-    **Length|Länge**: (schreibgeschützt) gibt die Gesamtlänge der Kurve an.

-    **Make Face|Bool**: legt fest, ob die Kurve eine Fläche bildet oder nicht. Wenn sie `True` ist, wird eine Fläche erzeugt, ansonsten wird nur der Umfang als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn **Closed** `True` ist und wenn die Kurve sich nicht selbst schneidet.

-    **Points|VectorList**: gibt die Kontrollpunkte der Kurve in ihrem lokalen Koordinatensystem an.



### Ansicht


{{TitleProperty|Entwurf}}

-    **Pfeilgröße|Länge**: legt die Größe des Symbols fest, das am Ende der Kurve angezeigt wird.

-    **Pfeiltyp|Aufzählung**: gibt den Typ des am Ende der Kurve angezeigten Symbols an, der {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} oder {{value|Tick-2}} sein kann.

-    **End Arrow|Bool**: gibt an, ob am Ende der Kurve ein Symbol angezeigt werden soll, damit sie als Anmerkungslinie verwendet werden kann.

-    **Pattern|Enumeration**: legt das [Draft Pattern](Draft_Pattern.md) fest, mit dem die Fläche der geschlossenen Kurve gefüllt werden soll. Diese Eigenschaft funktioniert nur, wenn **Make Face** `True` ist und wenn **Display Mode** {{value|Flat Lines}} ist.

-    **Pattern Size|Float**: legt die Größe des [Entwurf Muster](Draft_Pattern/de.md) fest.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um eine Entwurf Linie zu erstellen, verwende die Methode `make_bezcurve` (<small>(v0.19)</small> ) des Entwurf Moduls. Diese Methode ersetzt die veraltete Methode `makeBezCurve`.


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```

-   Erstellt ein `BézKurve` Objekt mit vorgegebener Liste von Punkten `Punkteliste`.
    -   Jeder Punkt in der Liste wird durch seinen `FreeCAD.Vector` definiert, mit Einheiten in Millimetern.
    -   Alternativ kann die Eingabe auch ein `Part.Wire` sein, aus dem Punkte extrahiert werden.
-   Wenn `closed` `True` ist, oder wenn der erste und letzte Punkt identisch sind, ist die Kurve geschlossen.
-   Wenn `Positionierung` ist `Keine`, wird die Kurve am Ursprung erzeugt.
-   Wenn `Fläche` `True` ist, und die Kurve geschlossen ist, macht die Kurve eine Fläche, d. h. er erscheint gefüllt.

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
