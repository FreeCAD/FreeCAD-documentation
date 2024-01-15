---
 GuiCommand:
   Name: Draft Wire
   Name/de: Draft Polylinie
   MenuLocation: Zeichnen , Polyline
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **P** **L**
   Version: 0.7
   SeeAlso: Draft_Line/de, Draft_BSpline/de
---

# Draft Wire/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> **Draft Polylinie** [erstellt](#Erstellen.md) eine Polylinie, eine Folge von mehreren Liniensegmenten (Linienzug). Der Befehl kann auch verwendet werden um [Draft-Linien](Draft_Line/de.md) und Draft-Polylinien zu [verbinden](#Verbinden.md).

Die Ecken einer Draft-Polylinie können verrundet oder mit einer Fase versehen werden, indem ihre {{PropertyData/de|Fillet Radius}} oder **Chamfer Size** geändert wird. Außerdem ist es möglich die Kanten einer Polylinie zu unterteilen, indem ihre {{PropertyData/de|Subdivisions}} geändert wird.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Eine durch mehrere Punkte festgelegte Polylinie (Linienzug)*



## Erstellen



### Anwendung

Siehe auch: [Draft Ablage](Draft_Tray/de.md), [Draft Einrasten](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Wire.svg" width=16px> [Polylinie](Draft_Wire/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_Wire.svg" width=16px> Polylinie** auswählen.
    -   Das Tastaturkürzel **P** dann **L**.

2.  Der Aufgaben-Bereich **Polylinie** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.

3.  Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) festlegen, oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.

4.  Weitere Punkte in der [3D-Ansicht](3D_view/de.md) festlegen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.

5.  
    **Esc**drücken oder die Schaltfläche **Close**, um den Befehl abzuschließen.



### Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 0.22).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam den Mauszeiger außerhalb der [3D-Ansicht](3D_view/de.md) zu plazieren, bevor man Koordinaten eingibt.

-    **R**drücken oder die Checkbox **Relative** anklicken, um den Relativ-Modus umzuschalten. Bei eingeschaltetem Relativ-Modus beziehen sich Koordinaten auf den letzten Punkt, falls vorhanden, andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** anklicken, um den Global-Modus umzuschalten. Bei eingeschaltetem Global-Modus beziehen sich Koordinaten auf des globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordiatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **F**drücken oder die Checkbox **Filled** anklicken, um den Füll-Modus umzuschalten. Bei eingeschaltetem Füll-Modus wird die {{PropertyData/de|Make Face}} (Fläche erstellen) des erstellten Kantenzuges (Wire) auf `True` gesetzt und eine Fläche erstellt, vorausgesetzt er ist geschlossen und nicht selbstdurchdringend. Man beachte, dass ein selbstdurchdringender Kantenzug mit einer Fläche nicht vernünftig dargestellt wird. Für solche Kantenzüge muss die {{PropertyData/de|Make Face}} auf `False` gesetzt werden.

-    **N**drücken oder die Checkbox **Fortsetzen** anklicken, um den Fortsetzen-Modus umzuschalten. Bei eingeschaltetem Fortsetzen-Modus wird der Befehl nach dem Drücken von **<img src="images/Draft_FinishLine.svg" width=16px> Fertigstellen** oder **<img src="images/Draft_CloseLine.svg" width=16px> Schließen** fortgesetzt oder nach der Erstellung eines geschlossenen Kantenzuges durch Einrasten auf dem ersten Punkt. Dies ermöglicht, mit der Erstellung weiterer Kantenzüge fortzufahren.

-    **/**oder die Schaltfläche **<img src="images/Draft_UndoLine.svg" width=16px> Rückgängig** drücken, um den letzten Punkt wieder zu entfernen.

-    **A**oder die Schaltfläche **<img src="images/Draft_FinishLine.svg" width=16px> Fertigstellen** drücken, um die Ausführung des Befehls abzuschließen und den Kantenzug offen zu lassen.

-    **O**oder die Schaltfläche **<img src="images/Draft_CloseLine.svg" width=16px> Schließen** drücken, um die Ausführung des Befehls abzuschließen und den Kantenzug zu schließen. Ein geschlossener Kantenzug kann auch durch Einrasten auf dem ersten Punkt des Kantenzuges erstellt werden.

-    **W**oder die Schaltfläche **<img src="images/Draft_Wipe.svg" width=16px> Wipe** drücken, um schon positionierte Abschnitte zu entfernen, aber trotzdem vom letzten Punkt aus weiterzumachen.

-    **U**oder die Schaltfläche **<img src="images/Draft_SelectPlane.svg" width=16px> [Arbeitsebene auswählen](Draft_SelectPlane/de.md)** drücken, um die Ausrichtung der Arbeitsebene an die Richtung des letzten Abschnitts anzupassen.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl abzuschließen.



## Verbinden



### Anwendung 

1.  Die Endpunkte der [Draft Linie](Draft_Line/de.md) und/oder des Draft-Kantenzuges, die verbunden werden sollen, müssen exakt deckungsgleich sein. Falls erforderlich, werden zuerst die Punkte angepasst, um dies sicherzustellen.
2.  Zwei oder mehr [Draft Linien](Draft_Line/de.md) und/oder Draft-Kantenzüge auswählen.
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Wire.svg" width=16px> [Draft Polylinie](Draft_Wire/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_Wire.svg" width=16px> Polyline** auswählen.
    -   Das Tastaturkürzel **P** dann **L**.



## Hinweise

-   Ein Draft Kantenzug (Wire) kann mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) bearbeitet werden.
-   Ein Draft Kantenzug kann mit dem Befehl [Draft KantenzugZuBSpline](Draft_WireToBSpline/de.md) in einen [Draft-B-Spline](Draft_BSpline/de.md) umgewandelt werden.
-   [Draft-Linien](Draft_Line/de.md) und Draft-Kantenzüge können auch mit den Befehlen [Draft Verbinden](Draft_Join/de.md) oder [Draft Hochstufen](Draft_Upgrade/de.md) verbunden werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Polylinie-Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    {{PropertyData/de|Area|Area}}: (nur Lesezugriff) gibt dem Flächeninhalt der Fläche eines Kantenzuges an. Der Wert ist {{value|0.0}}, wenn die {{PropertyData/de|Make Face}} auf `False` gesetzt ist oder die Fläche nicht erstellt werden kann.

-    {{PropertyData/de|Base|Link}}
    

-    {{PropertyData/de|Chamfer Size|Length}}: gibt die Länge der Fasen an den Ecken des Kantenzuges an.

-    {{PropertyData/de|Closed|Bool}}: spezifiziert, ob der Draht geschlossen ist oder nicht. Wenn der Kantenzug zu Beginn offen ist, ist dieser Wert `False`; wird er auf `True` gesetzt, wird ein Liniensegment hinzugefügt, um den Kantenzug zu schließen. Wenn der Kantenzug ursprünglich geschlossen ist, ist dieser Wert `True`; wird er auf `False` gesetzt, wird das letzte Liniensegment entfernen, und der Kantenzug wird geöffnet.

-    {{PropertyData/de|End|VectorDistance}}: gibt den Endpunkt des Kantenzuges an.

-    {{PropertyData/de|Fillet Radius|Length}}: gibt den Radius der Verrundungen an den Ecken eines Kantenzuges an.

-    {{PropertyData/de|Length|Length}}: (nur Lesezugriff) gibt die Länge des gesamten Kantenzuges an.

-    {{PropertyData/de|Make Face|Bool}}: gibt an, ob der Draht eine Fläche bildet oder nicht. Wenn sie `True` ist, wird eine Fläche erstellt, andernfalls werden nur die Kanten als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn die {{PropertyData/de|Closed}} auf `True` gesetzt ist und wenn der Kantenzug sich nicht selbst überschneidet.

-    **Points|VectorList**: gibt die Punkte des Kantenzuges in seinem lokalen Koordinatensystem an.

-    {{PropertyData/de|Start|VectorDistance}}: gibt den Startpunkt des Kantenzuges an.

-    {{PropertyData/de|Subdivisions|Integer}}: gibt die Anzahl der Unterteilungen für jede Kante des Kantenzuges an. Ist ihr Wert {{value|1}}, wird jede Kante in {{value|2}} gleichgroße Abschnitte aufgeteilt. Unterteilungen werden vor Fasen und Verrundungen angewendet.

-    {{PropertyData/de|Tool|Link}}
    



### Ansicht


{{TitleProperty|Draft}}

-    {{PropertyView/de|Arrow Size|Length}}: gibt die Größe des Symbols an, das am Ende des Kantenzuges angezeigt wird.

-    {{PropertyView/de|Arrow Type|Enumeration}}: gibt die Art des Symbols an, das am Ende des Kantenzuges angezeigt wird; es stehen {{value|Dot}} (Punkt), {{value|Circle}} (Kreis), {{value|Arrow}} (Pfeil), {{value|Tick}} (Schrägstrich) oder {{value|Tick-2}} (Schrägstrich-2) zur Auswahl.

-    {{PropertyView/de|End Arrow|Bool}}: gibt an, ob ein Symbol am Ende des Kantenzuges angezeigt werden soll, damit es als Beschriftungszeile verwendet werden kann.

-    {{PropertyView/de|Pattern|Enumeration}}: gibt das [Draft Schraffurmuster](Draft_Pattern/de.md) an, mit dem die Fläche des geschlossenen Kantenzuges gefüllt werden soll. Diese Eigenschaft funktioniert nur, wenn {{PropertyData/de|Make Face}} auf `True` gesetzt ist und wenn die {{PropertyView/de|Display Mode}} den Wert {{value|Flat Lines}} enthält.

-    {{PropertyView/de|Pattern Size|Float}}: gibt die Größe des [Draft Schraffurmusters](Draft_Pattern/de.md) an.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Draft-Polylinie wird die Methode `make_wire` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeWire`.


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Erzeugt ein `Wire`-Objekt (Kantenzug) mit der angegebenen Liste von Punkten, `pointslist`.
    -   Jeder Punkt in der Liste wird durch seinen `FreeCAD.Vector` definiert, mit Einheiten in Millimetern.
    -   Alternativ kann die Eingabe ein `Part.Wire` sein, aus dem die Punkte extrahiert werden.
-   Wenn `closed` `True` ist, oder wenn der erste und letzte Punkt identisch sind, wird der Kantenzug geschlossen.
-   Wenn ein `placement` (Position) angegeben wird, wird dieses verwendet; andernfalls wird die Form im Ursprung erzeugt.
-   Wenn `face` `True` ist und der Kantenzug geschlossen ist, wird der Kantenzug eine Fläche bilden, d.h. er wird gefüllt erscheinen.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/de
