# TechDraw API/de
**(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die [https://www.freecadweb.org/api autogenerierte API Dokumentation].** Diese Funktionen sind Teil des [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) und können in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus verwendet werden, sobald das `TechDraw` Modul importiert wurde.

Gute Beispiele für grundlegendes TechDraw Skripten findest Du in den [unit test scripts](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/TDTest).

Siehe die [TechDrawGui API](TechDrawGui_API/de.md) für weitere Funktionen.

Beispiel: 
```python
import FreeCAD
import TechDraw

page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage', 'Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate', 'Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart', 'View')
rc = page.addView(view)
```


{{APIFunction|EdgeWalker|listOfEdges, [bool]|Erzeugt Drähte aus Kanten in der Eingabe durch planare Graphenquerung.  Schließe den ÄußerenDraht optional aus, indem Du den optionalen Parameter auf false setzen. |Liste der Drähte sortiert nach Größe (absteigend)}}


{{APIFunction|findOuterWire|listOfEdges|Findet den ÄußerenDraht (größten) einer Liste von Kanten (die einen planaren Graphen bilden).|Outer wire}}


{{APIFunction|findShapeOutline|TopoShape, Maßstab, Richtung|Projektform in Richtung und finde den äußeren Draht des Ergebnisses.|Outline Draht}}


{{APIFunction|viewPartAsDxf|DrawViewPart|Return the edges of a DrawViewPart in Dxf format.|String}}

Example: 
```python
fileSpecDxf = "fcOut.dxf"
v = App.ActiveDocument.View
s = TechDraw.viewPartAsDxf(v)
dxfEnd = "0\nEOF\n"
dxfFile = open(fileSpecDxf, "w")
dxfFile.write(s)
dxfFile.write(dxfEnd)
dxfFile.close()
```


{{APIFunction|viewPartAsSvg|DrawViewPart|Return the edges of a DrawViewPart in Svg format.|String}}

Example: 
```python
fileSpecSvg = "fcOut.svg"
v = App.ActiveDocument.View
s = TechDraw.viewPartAsSvg(v)
head = '<svg\n' + \
       '    xmlns="http://www.w3.org/2000/svg" version="1.1" \n' + \
       '    xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace">\n'
tail = '\n</svg>'
svgFile = open(fileSpecSvg, "w")
svgFile.write(head)
svgFile.write(s)
svgFile.write(tail)
svgFile.close()
```


{{APIFunction|writeDXFView|DrawViewPart, FileName|Save the DrawViewPart in Dxf.|File}}

Example: 
```python
import TechDraw
TechDraw.writeDXFView(myPart,myFileName)
```


{{APIFunction|writeDXFPage|DrawPage, FileName|Save the DrawPage in Dxf.|File}}

Example: 
```python
import TechDraw
TechDraw.writeDXFPage(myPage,myFileName)
```

### ZeichneAnsichtPart Kosmetik 

#### CosmeticVertex (CV) Routinen, die von Python aus zugänglich sind 

dvp = App.ActiveDocument.View #CV\'s gehören zu Ansichten
füge einen KosmetikKnoten bei p1 (Ansichtskoordinaten) hinzu. Gibt einen eindeutigen Tag zurück.
tag = dvp.makeCosmeticVertex(vector p1)

füge einen Kosmetikknoten bei p1 (3D Modellkoordinaten) hinzu. Gibt ein eindeutiges Tag zurück.
tag = dvp.makeCosmeticVertex3d(vector p1)

gibt Kosmetikknoten mit eindeutiger ID zurück.
cv = dvp.getCosmeticVertex(string id)

gibt KosmetikKnoten mit Namen zurück (Vertex6). In Auswahlen verwendet.
cv = dvp.getCosmeticVertexBySelection(Zeichenfolgennamen)

KosmetikKnoten aus der Ansicht entfernen. Gibt nichts zurück.
dvp.removeCosmeticVertex(object cv)

alle KosmetikKnoten aus der Ansicht entfernen. Gibt nichts zurück.
dvp.clearCosmeticVertices()

KosmetikAnsicht Merkmale
Tag: eindeutiger Bezeichner. Zeichenfolge.
Punkt: Standort innerhalb der Ansicht. Vektor.

-   -   


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Py CosmeticVertex demo
import FreeCAD
import TechDraw

v = App.ActiveDocument.View
p = App.Vector(-3.0, -3.0, 0.0)

#make CV
tag = v.makeCosmeticVertex(p)
print("t: {}".format(tag))

#retrieve CV
cv = v.getCosmeticVertex(tag)
print("cv: {}".format(cv))
print("Tag: {}".format(cv.Tag))


cv2 = v.getCosmeticVertexBySelection("Vertex4")
print("New Point: {}".format(cv2.Point))

#make CV from 3d
p3d = App.Vector(2.0, 2.0, 2.0)
print("3d point in: {}".format(p3d))
tag3d = v.makeCosmeticVertex3d(p3d)
cv3 = v.getCosmeticVertex(tag3d)
print("3d point out: {}".format(cv3.Point))
```

#### CosmeticEdge (CE) Routinen, die von Python aus zugänglich sind 

dvp = App.ActiveDocument.View #CE\'s gehören zu Ansichten
Erzeuge ein CosmeticEdge von p1 nach p2(Ansicht Koordinaten). Gibt eine Kennung zurück.
tag = dvp.makeCosmeticLine(p1, p2)

Erzeuge ein CosmeticEdge bei center mit dem Radius radius (Ansicht Koordinaten). Gibt eine Kennung zurück.
tag = dvp.makeCosmeticCircle(center, radius)

Erzeuge ein CosmeticEdge bei center mit dem Radius radius (Ansicht Koordinaten) vom Startwinkel start zum Endwinkel end. Gibt eine Kennung zurück.
tag = dvp.makeCosmeticCircleArc(center, radius, start, end)

Gibt das CosmeticEdge mit der Identitätsnummer id zurück.
ce = dvp.getCosmeticEdge(id)

Gibt das CosmeticEdge mit dem Namen (\'Edge25\') zurück. Wird in Auswahlen verwendet.
ce = dvp.getCosmeticEdgeBySelection(\'Edge25\')

Löscht das CosmeticEdge ce aus der Ansicht. Hat keine Rückgabe.
dvp.removeCosmeticEdge(ce)

Löscht alle CosmeticLines aus der Ansicht. Hat keine Rückgabe.
dvp.clearCosmeticEdges()

CosmeticEdge Attribute
Tag: eindeutige Kennung. String.
Format: Darstellung Attribute (Stil, Farbe, Linienbreite, Durchsichtigkeit). Tuple.

-   -   


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Py CosmeticEdge demo
import FreeCAD
import TechDraw

#points
org = App.Vector(0.0, 0.0, 0.0)
midTop = FreeCAD.Vector (1.0, 5.0, 0.0)   # middle, top
midBot = FreeCAD.Vector(2.0, -5.0, 0.0)      # middle, bottom
stdZ = FreeCAD.Vector(0.0, 0.0, 1.0)
center = FreeCAD.Vector(0.0, 0.0, 0.0)
arcCenter = FreeCAD.Vector(3.0, 3.0, 0.0)
vPt = FreeCAD.Vector(-3.0, 3.0, 0.0)
topRight = FreeCAD.Vector(5.0, 5.0, 0.0)
bottomLeft = FreeCAD.Vector(-5.0, -5.0, 0.0)

#angles
arcStart = -45
arcEnd = 45

#styles
solid = 1 
dashed = 2
dotted = 3
#weights
weight15 = 0.15
weight75 = 0.75
#colors
pyRed = (1.0, 0.0, 0.0, 0.0)
pyBlue = (0.0, 1.0, 0.0, 0.0)
pyGreen = (0.0, 0.0, 1.0, 0.0)
pyBlack = (0.0, 0.0, 0.0, 0.0)
shadow = (0.1, 0.1, 0.1, 0.0)

radius = 5.0
style = dashed
weight = weight75

dvp = App.ActiveDocument.View

print(dvp)

print("making line")
tag = dvp.makeCosmeticLine(midTop,midBot,style, weight, pyBlue)
ce = dvp.getCosmeticEdge(tag)
print("line tag: {}".format(tag))

print("making diagonal")
dvp.makeCosmeticLine(bottomLeft,topRight,solid, weight, pyGreen)

print("making circle")
tag2 = dvp.makeCosmeticCircle(center, radius, style, weight, pyRed)
ce2 = dvp.getCosmeticEdge(tag2)

print("making circleArc")
dvp.makeCosmeticCircleArc(arcCenter, radius, arcStart, arcEnd, style, weight, shadow)

#replace
print("making new format")
oldFormat = ce.Format
newFormat = (dotted,oldFormat[1], pyRed, True)
ce.Format = newFormat

print("removing CE with tag: {}".format(tag2))
dvp.removeCosmeticEdge(tag2)

print("finished")
```

#### MittelLinien (ML) Routinen, die über Python zugänglich sind 

Erzeuge eine neue CenterLine
tag = dvp.makeCenterLine(subObjs, mode)
Abrufen einer CenterLine mit der Kennung tag.
cl = dvp.getCenterLine(tag)

Abrufen einer CenterLine mit ihrem Namen. Wird in Auswahlen verwendet.
cl = dvp.getCenterLine(\"Edge5\")

Lösche die CenterLine cl aus der Ansicht. Hat keine Rückgabe.
dvp.removeCenterLine(cl)

CenterLine Attribute
Tag: eindeutige Kennung. String. ReadOnly.
Type: 0 - Fläche, 1 - 2 Linie, 2 - 2 Punkt. Integer. ReadOnly.
Mode: 0 - Vertikal, 1 - Horizontal, 2 - Verbunden. Integer.
Format: Sichtbarkeits Attribute (Stil, Farbe, Linienbreite, Durchsichtigkeit). Tuple.
HorizShift: links/rechts Abstand. Float.
VertShift: hoch/tief Abstand. Float.
Rotation: Verdrehwinkel in Grad. Float.
Extension: Zusätzliche Länge die angefügt wird. Float.
Flip: Vertauschen der Reihenfolge der Punkte bei 2 Punkt Mittellinie. Boolean.
Edges: Namen der Quelllinien. List of string.
Faces: Namen der Quellflächen. List of string.
Points: Namen der Quellpunkte (Vertices). List of string.

-   -   


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Py CenterLine demo
import FreeCAD
import Part
import TechDraw

start = FreeCAD.Vector (1.0, 5.0, 0.0)   # middle, top
end = FreeCAD.Vector(1.0, -5.0, 0.0)      # middle, bottom
faceNames = ["Face0"]
edgeNames = ["Edge2", "Edge3"]
vertNames = ["Vertex1", "Vertex2"]
vMode = 0   #vertical
hMode = 1   #horizontal
aMode = 2   #aligned
#styles
solid = 1 
dashed = 2
dotted = 3
#weights
weight15 = 0.15
weight75 = 0.75
#colors
pyRed = (1.0, 0.0, 0.0, 0.0)
pyBlue = (0.0, 1.0, 0.0, 0.0)
pyBlack = (0.0, 0.0, 0.0, 0.0)
#adjustments
hShift = 1.0
vShift = 1.0
extend = 4.0
rotate = 30.0
flip = False;

dvp = App.ActiveDocument.View

print("making face CenterLine")
tag = dvp.makeCenterLine(faceNames,vMode)
cline = dvp.getCenterLine(tag)
print("cline tag: {}".format(tag))

#replace
print("making new format")
oldFormat = cline.Format
newFormat = (dotted,oldFormat[1], pyRed, True)
cline.Format = newFormat
cline.Extension = 10.0

print("making edgeCenterLine")
cline2 = dvp.makeCenterLine(edgeNames,hMode)

print("making vertexCenterLine")
cline3 = dvp.makeCenterLine(vertNames,aMode)

print("finished")
```

### DrawViewPart Geometry 

\[topoShapeEdge\] = dvp.getVisibleEdges()

\[topoShapeEdge\] = dvp.getHiddenEdges()

topoShapeEdge = dvp.getEdgeByIndex(i)
topoShapeEdge = dvp.getEdgeBySelection(\"Edge1\")

topoShapeVertex = dvp.getVertexByIndex(i)
topoShapeVertex = dvp.getVertexBySelection(\"Vertex1\")

dvp.requestPaint() Neu zeichnen der Graphik für diese Ansicht.


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw API/de
