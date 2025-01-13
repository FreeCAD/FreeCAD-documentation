# Manual:Creating and manipulating geometry/de
{{Manual:TOC}}

In früheren Kapiteln haben wir die verschiedenen Arbeitsbereiche in FreeCAD untersucht und wie jeder seinen eigenen Satz an Werkzeugen und Geometrietypen einführt. Die gleichen Prinzipien gelten bei der Arbeit mit FreeCAD über Python-Skripte.

Wir haben auch festgestellt, dass die meisten FreeCAD-Workbenches auf einem grundlegenden Workbench basieren: dem <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md). Viele andere Workbenches, wie der <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft Workbench](Draft_Workbench.md), verwenden die Werkzeuge und Geometrie des Part Workbench, und genau das werden wir in diesem Kapitel tun -- Python verwenden, um die Part-Geometrie zu erstellen und zu bearbeiten.

Um mit der Teilegeometrie in Python arbeiten zu können, müssen wir das Skript-Äquivalent zum Wechsel zur Teile-Workbench durchführen: das Importieren des Teilemoduls.


```python
import Part 
```

Nimm dir einen Moment Zeit, um das Part-Modul zu erkunden, indem du **Part.** in die Python-Konsole eingibst und die verfügbaren Methoden und Attribute im Autovervollständigungsfenster durchsuchst. Dies ist eine großartige Möglichkeit, sich mit der Funktionalität des Moduls vertraut zu machen. Du findest eine Vielzahl praktischer Funktionen wie makeBox und makeCircle, mit denen du mit nur einem einzigen Befehl schnell geometrische Formen und Objekte erstellen kannst. Viele dieser Funktionen bieten auch optionale Parameter, mit denen du Abmessungen und Platzierung präzise steuern kannst.

Wenn du dir etwas Zeit nimmst, um die Inhalte des Moduls zu durchsuchen, erfährst du nicht nur, welche Werkzeuge dir zur Verfügung stehen, sondern du erhälst auch einen Einblick in die Funktionsweise des Part Workbench. Dieses grundlegende Wissen wird sich als von unschätzbarem Wert erweisen, wenn wir weitermachen und beginnen, Geometrie programmgesteuert zu erstellen und zu bearbeiten. Gib den folgenden Befehl ein


```python
Part.makeBox(3,5,7) 
```

Dieser Befehl erstellt eine 3D-Box, auch als rechteckiges Prisma bekannt, mit bestimmten Abmessungen. Der erste Parameter, 3, definiert die Länge der Box entlang der X-Achse. Der zweite Parameter, 5, legt die Breite entlang der Y-Achse fest und der dritte Parameter, 7, gibt die Höhe entlang der Z-Achse an. Während diese Funktion die Geometrie der Box generiert, fügt sie diese nicht automatisch dem aktiven FreeCAD-Dokument hinzu. In der Python-Konsole siehst du Folgendes:


```python
<Solid object at 0x5f43600> 
```

Die Ausgabe **\<Solid object at 0x5f43600\>** zeigt an, dass eine Teilform im Speicher erstellt wurde. Dies ist ein geometrisches Objekt, das an einer bestimmten Speicheradresse gespeichert ist, wie der Hexadezimalwert (0x5f43600) zeigt. Es ist jedoch wichtig zu verstehen, dass das, was wir hier erstellt haben, noch kein FreeCAD-Dokumentobjekt ist -- es existiert nur als rohe geometrische Form im Speicher.

Diese Unterscheidung unterstreicht ein grundlegendes Konzept in FreeCAD: Objekte und ihre Geometrie sind unabhängig. Ein FreeCAD-Dokumentobjekt dient als Container, der eine Form enthält. Diese Dokumentobjekte können zusätzliche Eigenschaften wie Länge, Breite und Höhe haben und parametrisch sein. Parametrische Objekte berechnen ihre Geometrie (oder Form) dynamisch neu, wenn sich eine ihrer Eigenschaften ändert. Wenn du beispielsweise die Länge einer parametrischen Box änderst, wird ihre Form automatisch mit dem aktualisierten Wert neu generiert.

In diesem Fall haben wir manuell eine Form mit der Funktion **Part.makeBox()** erstellt. Diese Form ist ein nicht parametrisches Objekt, d. h. sie wird nicht automatisch basierend auf irgendwelchen Eigenschaften aktualisiert -- sie ist statisch, sofern wir sie nicht programmgesteuert bearbeiten. Um diese Form zu einem Teil des aktiven FreeCAD-Dokuments zu machen, müsste sie einem Dokumentobjekt (wie einem **Part::Feature**) zugewiesen werden, das sie mit der grafischen Benutzeroberfläche verknüpft und sie in der FreeCAD-Umgebung sichtbar und verwaltbar macht.

Diese Trennung zwischen Formen und Dokumentobjekten macht FreeCAD äußerst vielseitig und ermöglicht es Benutzern, Formen programmgesteuert zu bearbeiten und sie nach Bedarf in einen parametrischen Modellierungsworkflow zu integrieren.

Wir können jetzt ganz einfach ein „generisches" Dokumentobjekt im aktuellen Dokument erstellen (stelle sicher, dass mindestens ein neues Dokument geöffnet ist) und ihm eine Kastenform geben, wie wir sie gerade erstellt haben:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Hier ist eine Aufschlüsselung der vorherigen Befehle:

-   **boxShape = Part.makeBox(3,5,7)**: Erstellt eine 3D-Box mit den Abmessungen 3x5x7 (Länge, Breite und Höhe) und speichert sie als Teilform in der Variablen boxShape. Diese Form existiert nur im Speicher und ist noch nicht Teil des FreeCAD-Dokuments.

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::Feature\", \"MyNewBox\")**: Fügt dem aktiven FreeCAD-Dokument ein neues Part::Feature-Objekt mit dem Namen \"MyNewBox\" hinzu und weist es der Variable myObj zu. Das neue Objekt wird im FreeCAD-Dokumentenbaum angezeigt.

-   **myObj.Shape = boxShape**: Verknüpft die boxShape-Geometrie mit der Shape-Eigenschaft von myObj und integriert die Geometrie in das FreeCAD-Dokument.

-   **FreeCAD.ActiveDocument.recompute()**: Aktualisiert das Dokument, um die Änderungen widerzuspiegeln und stellt sicher, dass das neue Objekt und seine Geometrie in der grafischen Benutzeroberfläche angezeigt werden.

Beachte wie wir **myObj.Shape** behandelt haben. Dies geschah auf die gleiche Weise wie im vorherigen Kapitel, wo wir andere Eigenschaften eines Objekts geändert haben, wie z. B. **box.Height = 5**. Tatsächlich ist **Shape** ebenso wie **Height** eine Eigenschaft. Anstatt jedoch eine Zahl anzunehmen, erfordert **Shape** eine Teilform. Im nächsten Kapitel werden wir uns genauer ansehen, wie diese parametrischen Objekte konstruiert werden.

Lass uns zunächst die Teilformen genauer untersuchen. Im Kapitel über traditionelles Modellieren mit der Part Workbench haben wir eine Tabelle eingeführt, die erklärt, wie Teilformen aufgebaut sind und aus welchen verschiedenen Komponenten sie bestehen, wie z. B. **Vertexes**, **Kanten** und **Flächen**. Dieselben Komponenten sind bei der Arbeit mit Teilformen in Python verfügbar und ermöglichen eine detaillierte Untersuchung und Bearbeitung der Geometrie. Teilformen in FreeCAD haben immer die folgenden Attribute:

-   **Vertexes**: Punkte im 3D-Raum, die die Ecken oder Endpunkte der Geometrie definieren.
-   **Kanten**: Gerade oder gekrümmte Linien, die zwei Scheitelpunkte verbinden.
-   **Drähte**: Geschlossene oder offene Schleifen, die durch eine oder mehrere verbundene Kanten gebildet werden.
-   **Flächen**: Oberflächen, die von einem oder mehreren Drähten umschlossen sind.
-   **Schalen**: Gruppen verbundener Flächen, die eine kontinuierliche Oberfläche bilden.
-   **Festkörper**: 3D-Volumina, die von einer oder mehreren Schalen umschlossen sind.

Alle diese Attribute werden in Python als Listen dargestellt. Jede Liste kann eine beliebige Anzahl von Elementen enthalten oder leer sein, je nachdem, welche Form untersucht wird. Eine Box hat beispielsweise acht **Vertexes**, zwölf **Kanten**, sechs **Flächen**, eine **Schale** und einen **Vollkörper**, während eine Linie nur zwei **Scheitelpunkte** und eine **Kante** hat und alle anderen Attribute leer sind. Diese Komponenten sind grundlegende Bausteine ​​der Teilegeometrie und können programmgesteuert aufgerufen und bearbeitet werden. Wenn man versteht, wie sie interagieren, erhält man eine leistungsstarke Kontrolle über die Erstellung und Änderung von 3D-Modellen. Wir können auf diese Listen wie folgt zugreifen:


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```

Berechnen wir die Fläche jeder Seite unseres oben gezeigten Kastens: (Achte darauf, die zweite Zeile einzurücken, wie sie unten angezeigt wird. Drücke nach der letzten Zeile zweimal die Eingabetaste, um den Python-Befehl auszuführen.)


```python
for f in boxShape.Faces:
   print(f.Area)
```

Oder für jede Kante deren Start- und Endpunkt:


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```

Wie du siehst, hat jede Kante der Boxform auch ein „Vertexes"-Attribut, wenn unsere Boxform ein „Vertexes"-Attribut hat. Wie zu erwarten, hat die Boxform 8 Vertices, während die Kante nur 2 hat, die beide Teil der Liste von 8 sind.

Wir können jederzeit überprüfen, von welchem Typ eine Form ist:


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Hier ist eine kurze Erklärung der obigen Befehle:

-   **print(boxShape.ShapeType)**: Zeigt den Typ der Form der obersten Ebene an, die durch **boxShape** dargestellt wird. In diesem Fall lautet die Ausgabe „Solid", da **boxShape** mit **Part.makeBox** als Box erstellt wurde, was bedeutet, dass die Form ein 3D-Festkörperobjekt ist.

-   **print(boxShape.Faces\[0\].ShapeType)**: Greift auf die erste Fläche in der Liste **Faces** von **boxShape** (Index 0) zu und druckt ihren Formtyp. Bei einer Box ist jede Fläche eine flache Oberfläche, daher lautet die Ausgabe „Face".

-   **print(boxShape.Vertexes\[2\].ShapeType)**: Greift auf den dritten Vertex in der Liste **Vertexes** von **boxShape** (Index 2) zu und druckt seinen Formtyp. Da dies ein bestimmter Punkt im 3D-Raum ist, lautet die Ausgabe „Vertex".

Um das Konzept der Teilformen zusammenzufassen: Alles beginnt mit **Vertexes**, den grundlegendsten Elementen der Geometrie. Mit einem oder zwei **Vertexes** kannst du eine **Kante** erstellen (beachte, dass für vollständige Kreise nur ein **Vertex** erforderlich ist). Eine oder mehrere **Kanten** können dann einen **Draht** bilden, der entweder offen oder geschlossen sein kann. Wenn du einen oder mehrere geschlossene **Drähte** hast, kannst du eine **Fläche** erstellen. Zusätzliche **Drähte** innerhalb des Haupt-**Drahtes** fungieren als „Löcher" in der **Fläche**. Durch die Kombination einer oder mehrerer **Flächen** kannst du eine **Schale** konstruieren, die im Wesentlichen eine Sammlung verbundener Oberflächen ist. Wenn eine **Schale** vollständig geschlossen und wasserdicht ist, kann sie verwendet werden, um einen **Festkörper** zu bilden -- ein 3D-Objekt mit Volumen. Schließlich können beliebig viele Formen jeden Typs, einschließlich **Vertexes**, **Kanten**, **Drähte**, **Flächen**, **Schalen** oder **Festkörper**, zu einer **Verbindung** zusammengefasst werden, die als Container für mehrere Formen fungiert.

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

Beachte, dass wir **Vertexes** nicht explizit erstellen mussten. Stattdessen konnten wir **Part.LineSegments** direkt mit **FreeCAD-Vektoren** erstellen. Dies liegt daran, dass wir in dieser Phase mit Basisgeometrie und nicht mit tatsächlichen **Kanten** arbeiten. **Part.LineSegment** sowie **Part.Circle**, **Part.Arc**, **Part.Ellipse** oder **Part.BSpline** definieren die zugrunde liegende Geometrie, erzeugen aber selbst keine Kante. In FreeCAD werden Kanten immer aus einer solchen Basisgeometrie erstellt, die im **Curve**-Attribut der **Kante** gespeichert ist. Dies bedeutet, dass eine Kante im Wesentlichen eine Hülle um die Basisgeometrie ist und deren Eigenschaften erbt. Wenn du eine Kante hast, kannst du auf ihre zugrunde liegende Geometrie zugreifen, indem du auf das Kurvenattribut verweist. Der folgende Befehl:


```python
print(Edge.Curve) 
```

ermöglicht es dir, die zugrunde liegende Struktur der Kante und ihre Konstruktion zu verstehen. Kehren wir nun zu unserer Übung zurück und fahren mit dem Erstellen der Bogensegmente fort. Um einen Bogen zu erstellen, benötigen wir drei Punkte: einen Startpunkt, einen Endpunkt und einen Mittelpunkt, der die Krümmung bestimmt. Zu diesem Zweck können wir die praktische Funktion **Part.Arc** verwenden, die diese drei Punkte als Eingabe verwendet und die Basisgeometrie für einen Bogen generiert.

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

Alternativ verfügen Basisgeometrien auch über eine Funktion **toShape()**, die genau dasselbe tut:


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```

Sobald wir eine Reihe von Kanten haben, können wir nun einen **Draht** bilden, indem wir ihm eine Liste von Kanten geben. Wir müssen auf die Reihenfolge achten. Beachte auch die Klammern.


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

Und wir können überprüfen, ob unser Draht richtig verstanden wurde und ob er richtig geschlossen ist:


```python
print( W.isClosed() ) 
```

Das gibt „True" oder „False" aus. Um eine **Fläche** zu erstellen, benötigen wir **geschlossene Drähte**, daher ist es immer eine gute Idee, dies vor dem Erstellen der Fläche zu überprüfen. Jetzt können wir eine Fläche erstellen, indem wir ihr einen einzelnen Draht zuweisen (oder eine Liste von Drähten, wenn wir Löcher wollen):


```python
F = Part.Face(W) 
```

Dann wird es extrudiert:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Beachte, dass P bereits ein **Festkörper** ist:


```python
print(P.ShapeType) 
```

Dies liegt daran, dass wir beim Extrudieren einer einzelnen Fläche immer einen Festkörper erhalten. Dies wäre beispielsweise nicht der Fall, wenn wir stattdessen den Draht extrudiert hätten:


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
```

Dadurch erhalten wir natürlich eine hohle Hülle, bei der Ober- und Unterseite fehlen.

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

All dies und noch viel mehr wird auf der Seite [Topologische Daten skripten](Topological_data_scripting/de.md) im Detail erklärt und mit Beispielen versehen.

**Mehr lesen**:

-   [Der Arbeitsbereich Part](Part_Workbench/de.md)
-   [Part skripten](Topological_data_scripting/de.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/de
