# Manual:Creating and manipulating geometry/de
{{Manual:TOC}}

In den vorangegangenen Kapiteln haben wir die verschiedenen Arbeitsbereiche von FreeCAD kennengelernt, und wie jede von ihnen ihre eigenen Werkzeuge und Geometrietypen implementiert. Das gleiche Konzept gilt für die Arbeit mit Python-Code.

Wir haben auch gesehen, dass die große Mehrheit der FreeCAD-Arbeitsbereiche von einem sehr grundlegenden Arbeitsbereich abhängt: dem Arbeitsbereich [Part](Part_Workbench/de.md). Tatsächlich tun viele andere Arbeitsbereiche, wie z.B. [Draft](Draft_Workbench/de.md) und [Arch](Arch_Workbench/de.md), genau das, was wir in diesem Kapitel tun werden: Python-Code verwenden, um Part-Geometrie zu erstellen und handzuhaben.

Das erste, was wir tun müssen, um mit der Part-Geometrie zu arbeiten, ist das Python-Äquivalent zum Wechsel zum Arbeitsbereich Part: Das Part-Modul importieren:


```python
import Part 
```

Nimm dir eine Minute Zeit, um den Inhalt des Part-Moduls zu erkunden, indem du Part. eingibst und die verschiedenen verfügbaren Methoden durchgehst. Das Part-Modul bietet mehrere praktische Funktionen wie makeBox, makeCircle usw., die dir sofort ein Objekt erstellen. Probiere zum Beispiel dies aus:


```python
Part.makeBox(3,5,7) 
```

Wenn du nach der Eingabe der obigen Zeile die Eingabetaste drückst, wird in der 3D-Ansicht nichts angezeigt, aber auf der Python-Konsole wird etwas wie das Folgende ausgegeben


```python
<Solid object at 0x5f43600> 
```

An dieser Stelle kommt ein wichtiges Konzept zum Tragen. Was wir hier erstellt haben, ist eine Part-Form. Es handelt sich (noch) nicht um ein FreeCAD-Dokumentenobjekt. In FreeCAD sind Objekte und ihre Geometrie unabhängig. Stelle dir ein FreeCAD-Dokumentenobjekt als einen Behälter vor, der eine Form beherbergt. Parametrische Objekte haben auch Eigenschaften wie Länge und Breite und berechnen ihre Form \"spontan\" neu, wenn sich eine der Eigenschaften ändert. Wir haben hier eine Form manuell berechnet.

Wir können nun ganz einfach ein \"unspezifisches\" Dokumentobjekt im aktuellen Dokument erstellen (stelle sicher, dass du mindestens ein neues Dokument geöffnet hast) und ihm eine Kastenform wie die eben erstellte gibst:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Beachte, wie wir myObj.Shape gehandhabt haben, und beachte, dass wir es genauso gemacht haben wie im vorherigen Kapitel, als wir andere Eigenschaften eines Objekts geändert haben, z. B. box.Height = 5 . In der Tat ist **Form** ebenfalls eine Eigenschaft, genau wie **Höhe**. Nur dass sie eine Part-Form und nicht eine Zahl annimmt. Im nächsten Kapitel werden wir uns genauer ansehen, wie diese parametrischen Objekte aufgebaut sind.

Lasse uns nun unsere Part-Formen genauer untersuchen. Am Ende des Kapitels über [Traditionelle Modellierung mit dem Arbeitsbereich Part](Manual:Traditional_modeling,_the_CSG_way/de.md) haben wir eine Tabelle gezeigt, die erklärt, wie Part-Formen konstruiert werden und aus welchen Komponenten sie bestehen (Knoten, Kanten, Flächen, usw.). Die gleichen Komponenten sind auch hier vorhanden und können über Python abgerufen werden. Part-Formen haben immer die folgenden Attribute: Knoten, Kanten, Drähte, Flächen, Schalen und Volumenkörper. Alle sind Listen, die eine beliebige Anzahl von Elementen enthalten oder leer sein können:


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```

Lasse uns zum Beispiel den Flächeninhalt jeder Fläche unseres obigen boxShape(-Objekts) bestimmen:(Nicht vergessen die zweite Zeile einzurücken, wie unten dargestellt. Nach der letzten Zeile zweimal die Eingabetaste (Enter) drücken, um den Python-Befehl zu starten.)


```python
for f in boxShape.Faces:
   print(f.Area)
```

Oder für jede Kante ihren Anfangs- und Endpunkt:


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```

Wie du siehst, wenn unser boxShape ein Attribut \"Vertexes\" (Knoten) hat, hat jede Kante des boxShape auch ein Attribut \"Vertexes\". Wie zu erwarten, wird das boxShape 8 Knoten haben, während die Kante nur 2 hat, die beide zur Liste von 8 gehören.

Wir können jederzeit überprüfen, von welchem Typ eine Form ist:


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Um das Thema der Part-Formen wieder aufzunehmen: Alles beginnt mit Knoten. Mit einem oder zwei Knoten bildet man eine Kante (Vollkreise haben nur einen Knoten). Mit einer oder mehreren Kanten bildet man einen Draht. Mit einem oder mehreren geschlossenen Drähten bildet man eine Fläche (die zusätzlichen Drähte werden zu \"Löchern\" in der Fläche). Mit einer oder mehreren Flächen bildet man eine Schale. Wenn eine Schale vollständig geschlossen (wasserdicht) ist, kann man daraus einen Festkörper bilden. Und schließlich kann eine beliebige Anzahl von Formen beliebigen Typs miteinander verbunden werden, was dann als Verbund bezeichnet wird.

Wir können nun versuchen, komplexe Formen von Grund auf neu zu erstellen, indem wir alle ihre Komponenten nacheinander konstruieren. Versuchen wir zum Beispiel, ein Volumen wie dieses zu erstellen:

![](images/Exercise_python_03.jpg )

Wir beginnen mit der Erstellung einer ebenen Form wie dieser:

![](images/Wire.png )

Erstellen wir zunächst die vier Basispunkte:


```python
V1 = FreeCAD.Vector(0,10,0)
V2 = FreeCAD.Vector(30,10,0)
V3 = FreeCAD.Vector(30,-10,0)
V4 = FreeCAD.Vector(0,-10,0)
```

Dann können wir die beiden linearen Segmente erstellen:

![](images/Line.png )


```python
L1 = Part.LineSegment(V1,V2)
L2 = Part.LineSegment(V4,V3)
```

Beachte, dass wir keine Knoten erstellen müssen. Wir konnten sofort Part.LineSegments aus FreeCAD-Vektoren erstellen. Das liegt daran, dass wir hier noch keine Kanten erstellt haben. Ein Part.LineSegment (ebenso wie Part.Circle, Part.Arc, Part.Ellipse oder Part.BSpline) erzeugt keine Kante, sondern eine Basisgeometrie, aus der eine Kante erzeugt wird. Kanten werden immer aus einer solchen Basisgeometrie erstellt, die in ihrem Attribut Kurve gespeichert ist. Wenn du also eine Kante hast, tippe ein:


```python
print(Edge.Curve) 
```

Es zeigt dir, um welche Art von Kante es sich handelt, d. h. ob sie auf einer Linie, einem Bogen usw. basiert. Aber kommen wir zurück zu unserer Übung und bauen wir die Bogensegmente. Dazu benötigen wir einen dritten Punkt, damit wir den praktischen Part.Arc verwenden können, der 3 Punkte benötigt:

![](images/Circel.png )


```python
VC1 = FreeCAD.Vector(-10,0,0)
C1 = Part.Arc(V1,VC1,V4)
VC2 = FreeCAD.Vector(40,0,0)
C2 = Part.Arc(V2,VC2,V3)
```

Jetzt haben wir 2 Linien (L1 und L2) und 2 Bögen (C1 und C2). Wir müssen sie in Kanten umwandeln:


```python
E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)
```

Alternativ dazu verfügen Basisgeometrien auch über eine Funktion toShape(), die genau das Gleiche bewirkt:


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```

Sobald wir eine Reihe von Kanten haben, können wir nun einen Draht bilden, indem wir ihm eine Liste von Kanten geben. Dabei müssen wir die Reihenfolge beachten und auch die Klammern.


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

Und wir können überprüfen, ob unser Draht richtig verstanden wurde und ob er richtig geschlossen ist:


```python
print( W.isClosed() ) 
```

Es wird \"True\" oder \"False\" ausgegeben. Um eine Fläche zu erstellen, brauchen wir geschlossene Drähte, also ist es immer eine gute Idee, dies zu überprüfen, bevor wir die Fläche erstellen. Jetzt können wir eine Fläche erstellen, indem wir ihr einen einzelnen Draht geben (oder eine Liste von Drähten, wenn wir Löcher wollen):


```python
F = Part.Face(W) 
```

Dann wird es extrudiert:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Beachte, dass P bereits ein Festkörper ist:


```python
print(P.ShapeType) 
```

Das liegt daran, dass wir beim Extrudieren einer einzelnen Fläche immer einen Festkörper erhalten. Dies wäre zum Beispiel nicht der Fall, wenn wir stattdessen den Draht extrudieren würden:


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
```

Dadurch erhalten wir natürlich eine hohle Schale, bei der die Ober- und Unterseite fehlen.

Jetzt, wo wir unser endgültige Form haben, sind wir gespannt darauf, sie auf dem Bildschirm zu sehen! Erstellen wir also ein allgemeines Objekt und weisen ihm unseren neuen Festkörper zu:


```python
myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","My_Strange_Solid")
myObj2.Shape = P
FreeCAD.ActiveDocument.recompute()
```

Alternativ bietet das Teil Modul auch einen Kurzbefehl, mit dem der oben beschriebene Vorgang schneller ausgeführt werden kann (allerdings kannst du den Namen des Objekts nicht auswählen):


```python
Part.show(P) 
```

All dies und noch viel mehr wird auf der Seite [Topologische Daten Skripten](Topological_data_scripting/de.md) im Detail erklärt und mit Beispielen versehen.

**Mehr lesen**:

-   [Der Part Arbeitsbereich](Part_Workbench/de.md)
-   [Part skripten](Topological_data_scripting/de.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/de
