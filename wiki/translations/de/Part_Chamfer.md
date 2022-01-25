---
- GuiCommand:/de
   Name:Part Chamfer
   Name/de:Part Fase
   MenuLocation:Part → Fase...
   Workbenches:[Part Arbeitsbereich](Part_Workbench/de.md)
   SeeAlso:[Part Verrundung](Part_Fillet/de.md)
---

# Part Chamfer/de

## Beschreibung

Anfasen der gewählten Kante(n) eines Objekts. Ein Dialog erlaubt die Auswahl, welche Kante(n) betroffen sind, sowie die Anpassung verschiedener Anfasungsparameter.

![Anfasungsbeispiel](images/Chamfer-example.png )

## Anwendung


<div class="mw-translate-fuzzy">

1.  Rufe den Befehl Fase auf mehrere Arten im <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Formteil Arbeitsbereich](Part_Workbench/de.md)
    -   Drücke die **<img src="images/Part_Chamfer.svg" width=30px>** Schaltfläche in der Formteil Werkzeugleiste
    -   Verwende den **Part → Fase** Eintrag im Formteil Menü
2.  Wähle die anzufasende Form aus dem Dialogfeld aus.
3.  Wähle die anzufasenden Kanten aus, indem du das entsprechende Kästchen im Dialogfeld für Fasen anhakst oder indem du sie direkt am Modell auswählst.
4.  Bearbeite Fasenparameter.
5.  Drücke **OK**, um das Dialogfeld für die Fase zu schließen und die Fase anzuwenden.


</div>

## Optionen

![Dialog-chamfer](images/Dialog-chamfer.png )

-   Wenn du Kanten am Modell auswählst, hast du die Möglichkeit, nach Kante oder Fläche zu wählen. Die Auswahl nach Fläche wählt alle angrenzenden Kanten dieser Fläche aus.
-   Fase mit konstanter Länge oder Fase mit variabler Länge.
    -   Eine Fase mit konstanter Länge erzeugt eine Fase mit Kanten, die in dem angegebenen Abstand gleich weit von der Originalkante entfernt sind.
    -   Eine Fase mit variabler Länge hat Kanten, die in unterschiedlichen Abständen von der ursprünglichen Kante eingestellt werden können, so dass du eine Fase in einem variablen Winkel erstellen kannst.

## Eigenschaften

![Part\_Faseneigenschaften](images/Part_Chamfer-Properties.png ) 


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Basis}}: Die Form, auf die die Fase aufgebracht werden soll.

-    {{PropertyData/de|Placement}}: Gibt die Ausrichtung und Lage der Form im 3D Raum an.

-    {{PropertyData/de|Kennzeichen}}: Beschriftung des Objekts. Passe sie deinen Bedürfnissen an.




## Einschränkungen

Die Fase könnte nichts ausrichten, wenn das Ergebnis die nächste angrenzende Kante berühren oder überqueren würde. Wenn du also nicht das erwartete Ergebnis erhälst, versuche es mit einem kleineren Wert. Dies gilt auch für <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Verrundung](Part_Fillet/de.md).

Beachte auch, dass die Fasenfunktion von dem [Topologischen Benennungsproblem](Topological_naming_problem/de.md) betroffen ist, wenn die Änderung in einem Modellierungsschritt vorgenommen wird, der früher in der Kette liegt und die Anzahl der Facetten oder Eckpunkte beeinflusst. Dies kann zu unvorhersehbaren Ergebnissen führen. Bis dies gelöst ist (möglicherweise mit V0.20), wird empfohlen, die Operationen Fase und <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Verrundung](Part_Fillet/de.md) auf die letzten Schritte in der Kette anzuwenden.

## Skripten

Das Fasenwerkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus verwendet werden, indem dem Dokument ein Fasenobjekt hinzugefügt wird.

**Beispiel Skript:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
chmfr.Base = FreeCAD.ActiveDocument.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
FreeCADGui.ActiveDocument.myCube.Visibility = False
FreeCAD.ActiveDocument.recompute()
```

**Beispiel Skript Erklärung:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
```

-   Erzeugt einen 5 mm Würfel, auf den wir gefaste Kanten aufbringen können. Siehe [Part\_API](Part_API/de.md) für eine Erklärung der makeBox Methode.


```python
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
```

-   Fügt ein neues Objekt dem Dokument vom Typ Fase (aus dem Part Arbeitsbereich) mit der Bezeichnung \"myChamfer\" hinzu.


```python
chmfr.Base = FreeCAD.ActiveDocument.myCube
```

-   Legt fest, dass die Grundform des Fasenobjekts \"myCube\" sein soll.


```python
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
```

-   Erstellt ein leeres Feld \"myEdges\" und hängt dann das Feld mit den Fasenparametern jeder Kante an.
-   Die Syntax für jedes Element sollte sein (Kante\#, Fasenanfangslänge, Fasenendlänge)


```python
chmfr.Edges = myEdges
```

-   Setzt das Kantenattribut unseres Fasenobjekts gleich dem Feld, das wir gerade erstellt haben.


```python
FreeCADGui.ActiveDocument.myCube.Visibility = False
```

-   Diese Linie verbirgt einfach \"myCube\", so dass nur unser neu erstelltes \"myChamfer\" Objekt sichtbar ist.


```python
FreeCAD.ActiveDocument.recompute()
```

-   Berechnet alle geänderten Komponenten auf dem Bildschirm neu und aktualisiert die Anzeige.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Chamfer/de
