# Topological data scripting/sv
{{TOCright}}


<div class="mw-translate-fuzzy">

## Introduktion

Här kommer vi att förklara hur du kontrollerar [Del Modulen](Part_Workbench/sv.md) direkt från FreeCADs python tolk, eller från ett externt skript. Titta igenom [Skript](scripting/sv.md) avsnittet och [FreeCAD Skript grunder](FreeCAD_Scripting_Basics/sv.md) sidorna om du behöver mer information om hur python skript fungerar i FreeCAD.

För att kunna använda Delmodulens funktioner så måste du ladda Del modulen i tolken:

import Part


</div>

Here we will explain to you how to control the [Part](Part_Workbench.md) module directly from the FreeCAD Python interpreter, or from any external script. Be sure to browse the [Scripting](Scripting.md) section and the [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) pages if you need more information about how Python scripting works in FreeCAD. If you are new to Python, it is a good idea to first read the [Introduction to Python](Introduction_to_Python.md).

### See also 

-   [Part scripting](Part_scripting.md)
-   [OpenCASCADE](OpenCASCADE.md)


<div class="mw-translate-fuzzy">

### Klass Diagram 

Detta är en UML översikt över de viktigaste klasserna i Del modulen:

![Python klasser i Del modulen](images/Part_Classes.jpg )


</div>

This is a [Unified Modeling Language (UML)](http://en.wikipedia.org/wiki/Unified_Modeling_Language) overview of the most important classes of the Part module: ![Python classes of the Part module](images/Part_Classes.jpg ) {{Top}}


<div class="mw-translate-fuzzy">

### Geometri

De geomtriska objekten är byggblocken för alla topologiska objekt:

-   **GEOM** Basklass för geometriska objekt

-   **LINE** En rak linje i 3D, definierad av en start- och en slutpunkt

-   **CIRCLE** Cirkel eller cirkelsegment som definieras av en centrumpunkt, start- och en slutpunkt

-   **\...\...** Och snart lite mer


</div>

The geometric objects are the building blocks of all topological objects:

-   **Geom** Base class of the geometric objects.
-   **Line** A straight line in 3D, defined by starting point and end point.
-   **Circle** Circle or circle segment defined by a center point and start and end point.
-   Etc.


{{Top}}


<div class="mw-translate-fuzzy">

### Topologi

Följande topologiska datatyper finns tillgängliga:

-   **COMPOUND** En grupp av valfri typ av topologiska objekt.
-   **COMPSOLID** En kompositsolid är ett set av solider ihopkopplade genom dess ytor. Det expanderar begreppen WIRE och SHELL till solider.
-   **SOLID** En rymd som är begränsad av skal. Den är tredimensionell.
-   **SHELL** Ett set av ytor ihopkopplade genom dess kanter. Ett skal kan vara öppet eller slutet.
-   **FACE** I 2D så är det en del av ett plan; i 3D är det en del av en yta. Dess geometri är begränsad (trimmad) av konturer. Den är tvådimensionell.
-   **WIRE** Ett set av kanter som är ihopkopplade genom dess hörn. Det kan vara en öppen eller sluten kontur beroende på om kanterna är ihoplänkade eller inte.
-   **EDGE** Ett topologiskt element som motsvarar en begränsad kurva. En kant är vanligtvis begränsad av hörn. Det har en dimension.
-   **VERTEX** Ett topologiskt element som motsvarar en punkt. Dess dimension är noll.
-   **SHAPE** En allmän term som täcker allt ovan.


</div>

The following topological data types are available:

-   **Compound** A group of any type of topological objects.
-   **Compsolid** A composite solid is a set of solids connected by their faces. It expands the notions of WIRE and SHELL to solids.
-   **Solid** A part of space limited by shells. It is three dimensional.
-   **Shell** A set of faces connected by their edges. A shell can be open or closed.
-   **Face** In 2D it is part of a plane; in 3D it is part of a surface. Its geometry is constrained (trimmed) by contours. It is two dimensional.
-   **Wire** A set of edges connected by their vertices. It can be an open or closed contour depending on whether the edges are linked or not.
-   **Edge** A topological element corresponding to a restrained curve. An edge is generally limited by vertices. It has one dimension.
-   **Vertex** A topological element corresponding to a point. It has zero dimension.
-   **Shape** A generic term covering all of the above.


{{Top}}


<div class="mw-translate-fuzzy">

## Exempel

### Skapa simpel topologi 


</div>


<div class="mw-translate-fuzzy">

![Wire](images/Wire.png )


</div>


<div class="mw-translate-fuzzy">

Vi ska nu skapa en topologi genom att konstruera den utifrån enklare geometri. Som ett studiefall så använder vi en del som syns i bilden vilken består av fyra hörn, två cirklar och två linjer.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Skapa Geometri 

Först så måste vi skapa de distinkt geometriska delarna av denna tråd. Och vi måste ta hänsyn till att hörnen på de geometriska delarna är på **samma** position. Annars kanske vi inte kan koppla ihop de geometriska delarna till en topologi!


</div>

First we create the distinct geometric parts of this wire. Making sure that parts that have to be connected later share the same vertices.


<div class="mw-translate-fuzzy">

Så vi skapar punkterna först:


</div>


```python
import FreeCAD as App
import Part
V1 = App.Vector(0, 10, 0)
V2 = App.Vector(30, 10, 0)
V3 = App.Vector(30, -10, 0)
V4 = App.Vector(0, -10, 0)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Cirkelbåge


</div>


<div class="mw-translate-fuzzy">

![Circle](images/Circel.png )


</div>


<div class="mw-translate-fuzzy">

För att skapa en cirkelbåge så skapar vi en hjälppunkt och skapar cirkelbågen genom tre punkter:


</div>


```python
VC1 = App.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = App.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Linje


</div>


<div class="mw-translate-fuzzy">

![Line](images/Line.png )


</div>


<div class="mw-translate-fuzzy">

Linjen kan skapas mycket lätt ur punkterna:


</div>


```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Sätta ihop allt 

Det sista steget är att sätta ihop den geometriska grundelementen och baka en topologisk form:


</div>

The last step is to put the geometric base elements together and bake a topological shape:


```python
S1 = Part.Shape([C1, L1, C2, L2])
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Skapa ett prisma 

Extrudera nu tråden i en riktning och skapa en äkta 3D form:


</div>

Now extrude the wire in a direction and make an actual 3D shape:


```python
W = Part.Wire(S1.Edges)
P = W.extrude(App.Vector(0, 0, 10))
```


{{Top}}

### Show it all 


```python
Part.show(P)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Skapa grundtyper 

### Kort beskrivning 

Du kan lätt skapa enkla topologiska objekt med \"make\...()\" metoden från Del Modulen:


</div>

You can easily create basic topological objects with the `make...()` methods from the Part module:


```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```


<div class="mw-translate-fuzzy">

Några andra make\...() metoder fom finns:

-   makeBox(l,w,h,\[p,d\]) \-- Skapa en låda placerad i p och pekar i riktningen d med dimensionerna (l,w,h). Som standard är p Vektor(0,0,0) och d är Vektor(0,0,1)
-   makeCircle(radius,\[p,d,angle1,angle2\]) \-- Skapa en cirkel med en given radie. Som standard är p Vektor(0,0,0), d är Vektor(0,0,1) angle1=0 och angle2=360
-   makeCompound(list) \-- Skapar en compound från en lista med former (shapes)
-   makeCone(radius1,radius2,height,\[p,d,angle\]) \-- Skapa en kon med given radie och höjd. Som standard är p Vektor(0,0,0), d är Vektor(0,0,1) och angle=360
-   makeCylinder(radius,height,\[p,d,angle\]) \-- Skapa en cylinder med given radie och höjd. Som standard är p Vektor(0,0,0), d är Vektor(0,0,1) och angle=360
-   makeLine((x1,y1,z1),(x2,y2,z2)) \-- Skapa en linje mellan två punkter
-   makePlane(length,width,\[p,d\]) \-- Skapa ett plan med längd och bredd. med given radie och höjd. Som standard är p Vektor(0,0,0), och d är Vektor(0,0,1)
-   makePolygon(list) \-- Skapa en polygon från en lista med punkter
-   makeSphere(radius,\[p,d,angle1,angle2,angle3\]) \-- Skapa en sfär med given radie. Som standard är p Vektor(0,0,0), d Vektor(0,0,1), angle1=0, angle2=90 och angle3=360
-   makeTorus(radius1,radius2,\[p,d,angle1,angle2,angle3\]) \-- Skapa en torus med given radie. Som standard är p Vektor(0,0,0), d Vektor(0,0,1), angle1=0, angle2=360 och angle3=360

See the [Part API](Part_API.md) page for a complete list of available methods of the Part module.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Detaljerade förklaringar 

Importera först följande:


</div>

First we need to import the FreeCAD and Part modules so we can use their contents in Python:


```python
import FreeCAD as App
import Part
```


{{Top}}

### Create a vector 

[Vectors](http://en.wikipedia.org/wiki/Euclidean_vector) are one of the most important pieces of information when building shapes. They usually contain three numbers (but not necessarily always): the X, Y and Z cartesian coordinates. You create a vector like this:


```python
myVector = App.Vector(3, 2, 0)
```

We just created a vector at coordinates X = 3, Y = 2, Z = 0. In the Part module, vectors are used everywhere. Part shapes also use another kind of point representation called Vertex which is simply a container for a vector. You access the vector of a vertex like this:


```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en kant? 

En kant är inget annat än en linje med två hörn:


</div>

An edge is nothing but a line with two vertices:


```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

Notera: Du kan inte skapa en kant som passerar två hörn.


```python
vec1 = App.Vector(0, 0, 0)
vec2 = App.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

Du kan hitta en kants längd och centrum så här:


```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```


{{Top}}

### Put the shape on screen 

So far we created an edge object, but it doesn\'t appear anywhere on the screen. This is because the FreeCAD 3D scene only displays what you tell it to display. To do that, we use this simple method:


```python
Part.show(edge)
```

The show function creates an object in our FreeCAD document and assigns our \"edge\" shape to it. Use this whenever it is time to display your creation on screen. {{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en tråd? 

en tråd kan skapas från en lista med kanter eller en lista med trådar:


</div>

A wire is a multi-edge line and can be created from a list of edges or even a list of wires:


```python
edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
wire1 = Part.Wire([edge1, edge2]) 
edge3 = Part.makeLine((10, 10, 0), (0, 10, 0))
edge4 = Part.makeLine((0, 10, 0), (0, 0, 0))
wire2 = Part.Wire([edge3, edge4])
wire3 = Part.Wire([wire1, wire2])
wire3.Edges
> [<Edge object at 016695F8>, <Edge object at 0197AED8>, <Edge object at 01828B20>, <Edge object at 0190A788>]
Part.show(wire3)
```


<div class="mw-translate-fuzzy">

Part.show(wire3) kommer att visa fyra linjer som bildar en kvadrat:


</div>


```python
wire3.Length
> 40.0
wire3.CenterOfMass
> Vector (5, 5, 0)
wire3.isClosed()
> True
wire2.isClosed()
> False
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en yta? 

Endast ytor som skapats av stängda trådar är giltiga.

I detta exempel, så är wire3 en stängd tråd men wire2 är inte det (se ovan)


</div>

Only faces created from closed wires will be valid. In this example, wire3 is a closed wire but wire2 is not (see above):


```python
face = Part.Face(wire3)
face.Area
> 99.99999999999999
face.CenterOfMass
> Vector (5, 5, 0)
face.Length
> 40.0
face.isValid()
> True
sface = Part.Face(wire2)
sface.isValid()
> False
```


<div class="mw-translate-fuzzy">

Endast ytor har en area, inte trådar eller kanter.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en cirkel? 

circle = Part.makeCircle(radius,\[center,dir_normal,angle1,angle2\]) \-- Skapa en cirkel med en given radie

Som standard är, center=Vektor(0,0,0), dir_normal=Vektor(0,0,1), angle1=0 och angle2=360.

En cirkel kan skapas så här:


</div>

A circle can be created like this:


```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
```


<div class="mw-translate-fuzzy">

Om du vill skapa den vid en viss position och med en viss riktning


</div>


```python
ccircle = Part.makeCircle(10, App.Vector(10, 0, 0), App.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
```


<div class="mw-translate-fuzzy">

cirkeln kommer att skapas med en distans 10 från nollpunkten i x och kommer att vara vänd mot x axeln.

Notera: makeCircle accepterar endast Base.Vector() men inte tupler.

Du kan också skapa en cirkelbåge genom att ge start- och slutvinkel:


</div>


```python
from math import pi
arc1 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180, 360)
```


<div class="mw-translate-fuzzy">

Både arc1 och arc2 kommer tillsammans skapa en cirkel.

Vinklar ska anges i grader, om du har radianer, konvertera det genom att använda formeln:

Grader = radianer \* 180/PI

eller genom att använda python\'s math modul (efter att du importerat math, förstås):

grader = math.degrees(radianer)


</div>


```python
import math
degrees = math.degrees(radians)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en cirkelbåge längs punkter? 

Olyckligtvis så finns det ingen makeArc funktion men vi har Part.Arc funktionen för att skapa en cirkelbåge längs tre punkter.

Det kan antas vara en cirkelbåge som förenar start- och slutpunkt genom mittenpunkten.

Part.Arc skapar ett arc objekt på vilken .toShape() måste kallas för att få kant objektet,

vilket i allmänhet skapas av makeLine eller makeCircle


</div>

Unfortunately there is no `makeArc()` function, but we have the `Part.Arc()` function to create an arc through three points. It creates an arc object joining the start point to the end point through the middle point. The arc object\'s `toShape()` function must be called to get an edge object, the same as when using `Part.LineSegment` instead of `Part.makeLine`.


```python
arc = Part.Arc(App.Vector(0, 0, 0), App.Vector(0, 5, 0), App.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```


<div class="mw-translate-fuzzy">

Notera: Arc accepterar endast Base.Vector() för punkter men inte tupler.

arc_edge är vad vi vill ha, vilken vi kan visa med Part.show(arc_edge).

Om du vill ha en liten del av en cirkel som en cirkelbåge, så är det också möjligt:


</div>


```python
from math import pi
circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```

Arcs are valid edges like lines, so they can be used in wires also. {{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en polygon eller linje längs punkter? 

En linje längs multipla punkter är inget annat än att skapa en tråd med multipla kanter.

makePolygon funktionen tar en lista med punkter och skapar en tråd längs dessa punkter:


</div>

A polygon is simply a wire with multiple straight edges. The `makePolygon()` function takes a list of points and creates a wire through those points:


```python
lshape_wire = Part.makePolygon([App.Vector(0, 5, 0), App.Vector(0, 0, 0), App.Vector(5, 0, 0)])
```


{{Top}}

### Create a Bézier curve 

Bézier curves are used to model smooth curves using a series of poles (points) and optional weights. The function below makes a `Part.BezierCurve()` from a series of `FreeCAD.Vector()` points. Note: when \"getting\" and \"setting\" a single pole or weight, indices start at 1, not 0.


```python
def makeBCurveEdge(Points):
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man ett plan? 

Ett plan är en platt yta, alltså en yta i 2D

makePlane(length,width,\[start_pnt,dir_normal\]) \-- Skapa ett plan

Som standard start_pnt=Vector(0,0,0) och dir_normal=Vector(0,0,1).

dir_normal=Vector(0,0,1) kommer att skapa ett plan vinkelrätt mot z axeln.

dir_normal=Vector(1,0,0) kommer att skapa ett plan vinkelrätt mot x axeln:


</div>

A Plane is a flat rectangular surface. The method used to create one is `makePlane(length, width, [start_pnt, dir_normal])`. By default start_pnt = Vector(0, 0, 0) and dir_normal = Vector(0, 0, 1). Using dir_normal = Vector(0, 0, 1) will create the plane facing in the positive Z axis direction, while dir_normal = Vector(1, 0, 0) will create the plane facing in the positive X axis direction:


```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, App.Vector(3, 0, 0), App.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```


<div class="mw-translate-fuzzy">

BoundBox är en kub som omsluter planet med en diagonal som startar vid (3,0,0) och slutar vid (5,0,2).

Här ar BoundBox tjockleken i y axeln noll.


</div>


<div class="mw-translate-fuzzy">

Notera: makePlane accepterar endast Base.Vector() för start_pnt och dir_normal men inte tupler


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en ellips? 

För att skapa en ellips så finns det flera sätt:


</div>

There are several ways to create an ellipse:


```python
Part.Ellipse()
```


<div class="mw-translate-fuzzy">

Skapar en ellips med majorradie 2 och minorradie 1 med

centrum i (0,0,0)


</div>


```python
Part.Ellipse(Ellipse)
```


<div class="mw-translate-fuzzy">

skapa en kopia på den givna ellipsen


</div>


```python
Part.Ellipse(S1, S2, Center)
```


<div class="mw-translate-fuzzy">

Skapar en ellips centrerad på punkten Center, där ellipsens plan är definierad av Center, S1 och S2, dess majoraxel är definierad av Center och S1, dess majorradie är avståndet mellan Center och S1, och dess minorradie är avståndet mellan S2 och majoraxeln.


</div>


```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```


<div class="mw-translate-fuzzy">

Skapar en ellips med major och minor radierna MajorRadius och MinorRadius, och är placerad i det plan som definieras av Center och normalen (0,0,1)


</div>


```python
eli = Part.Ellipse(App.Vector(10, 0, 0), App.Vector(0, 5, 0), App.Vector(0, 0, 0))
Part.show(eli.toShape())
```


<div class="mw-translate-fuzzy">

I koden ovan så har vi gett S1, S2 och centrum. I likhet med Arc, så skapar Ellipse också ett ellipsobjekt men inte kant, så vi behöver konvertera den till en kant genom att använda toShape() för att visa den


</div>


<div class="mw-translate-fuzzy">

Note: Arc accepterar endast Base.Vector() för punkter men inte tupler


</div>


```python
eli = Part.Ellipse(App.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```


<div class="mw-translate-fuzzy">

För Ellipse konstruktören ovan så har vi gett center, MajorRadius och MinorRadius


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en Torus? 

makeTorus(radius1,radius2,\[pnt,dir,angle1,angle2,angle\]) \-- Skapa en torus med given radie och vinklar.

Som standard är pnt=Vector(0,0,0),dir=Vector(0,0,1),angle1=0,angle1=360 och angle=360

anse torus som en liten cirkel som sveper längs en stor cirkel:

radius1 den stora cirkelns radie, radius2 är den lilla cirkelns radie, pnt torusens centrum och dir är normalriktningen. angle1 och angle2 är vinklar i radianer för den lilla cirkeln, för att skapa en cirkelbåge den sista parametervinkeln är för att sektionera torusen:


</div>

Using `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = 0, angle2 = 360 and angle = 360. Consider a torus as small circle sweeping along a big circle. Radius1 is the radius of the big circle, radius2 is the radius of the small circle, pnt is the center of the torus and dir is the normal direction. angle1 and angle2 are angles in degrees for the small circle; the last angle parameter is to make a section of the torus:


```python
torus = Part.makeTorus(10, 2)
```


<div class="mw-translate-fuzzy">

Ovanstående kod kommer att skapa en torus med diametern 20(radie 10) och tjocklek 4(lilla cirkelradien 2)


</div>


```python
tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
```


<div class="mw-translate-fuzzy">

Ovanstående kod kommer att skapa en bit av en torus


</div>


```python
tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 360, 180)
```


<div class="mw-translate-fuzzy">

Ovanstående kod kommer att skapa en semi torus, endast den sista parametern är ändrad d.v.s. vinkeln och de kvarvarande vinklarna är standardvärden.

Genom att ge vinkeln 180 så kommer en halvtorus att skapas


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en låda eller en kub? 

makeBox(length,width,height,\[pnt,dir\]) \-- Skapar en låda placerad i pnt med dimensionerna (längd,bredd,höjd)

Som standard är pnt=Vektor(0,0,0) och dir=Vektor(0,0,1)


</div>

Using `makeBox(length, width, height, [pnt, dir])`. By default pnt = Vector(0, 0, 0) and dir = Vector(0, 0, 1).


```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en sfär? 

makeSphere(radius,\[pnt, dir, angle1,angle2,angle3\]) \-- Skapa en sför med given radie.

Som standard är pnt=Vektor(0,0,0), dir=Vektor(0,0,1), angle1=-90, angle2=90 och angle3=360.

angle1 och angle2 är sfärens vertikala minimum och maximum ,

angle3 sfärdiametern


</div>

Using `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 and angle3 = 360. Angle1 and angle2 are the vertical minimum and maximum of the sphere, angle3 is the sphere diameter.


```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), -90, 90, 180)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar men en Cylinder? 

makeCylinder(radius,height,\[pnt,dir,angle\]) \-- skapa en cylinder med given radie och höjd

Som standard är pnt=Vektor(0,0,0),dir=Vektor(0,0,1) och angle=360


</div>

Using `makeCylinder(radius, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360.


```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur skapar man en Kon? 

makeCone(radius1,radius2,height,\[pnt,dir,angle\]) \-- skapa en kon med given radie och höjd

Som standard är pnt=Vector(0,0,0), dir=Vector(0,0,1) och angle=360


</div>

Using `makeCone(radius1, radius2, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360.


```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
```


{{Top}}

## Modify shapes 

There are several ways to modify shapes. Some are simple transformation operations such as moving or rotating shapes, others are more complex, such as unioning and subtracting one shape from another. {{Top}}

## Transform operations 

### Translate a shape 

Translating is the act of moving a shape from one place to another. Any shape (edge, face, cube, etc\...) can be translated the same way:


```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(App.Vector(2, 0, 0))
```

This will move our shape \"myShape\" 2 units in the X direction. {{Top}}

### Rotate a shape 

To rotate a shape, you need to specify the rotation center, the axis, and the rotation angle:


```python
myShape.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 180)
```

The above code will rotate the shape 180 degrees around the Z Axis. {{Top}}

### Matrix transformations 

A matrix is a very convenient way to store transformations in the 3D world. In a single matrix, you can set translation, rotation and scaling values to be applied to an object. For example:


```python
myMat = App.Matrix()
myMat.move(App.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
```

Note: FreeCAD matrixes work in radians. Also, almost all matrix operations that take a vector can also take three numbers, so these two lines do the same thing:


```python
myMat.move(2, 0, 0)
myMat.move(App.Vector(2, 0, 0))
```

Once our matrix is set, we can apply it to our shape. FreeCAD provides two methods for doing that: `transformShape()` and `transformGeometry()`. The difference is that with the first one, you are sure that no deformations will occur (see [Scaling a shape](#Scaling_a_shape.md) below). We can apply our transformation like this:


```python
myShape.transformShape(myMat)
```

or


```python
myShape.transformGeometry(myMat)
```


{{Top}}

### Scale a shape 

Scaling a shape is a more dangerous operation because, unlike translation or rotation, scaling non-uniformly (with different values for X, Y and Z) can modify the structure of the shape. For example, scaling a circle with a higher value horizontally than vertically will transform it into an ellipse, which behaves mathematically very differently. For scaling, we cannot use the `transformShape()`, we must use `transformGeometry()`:


```python
myMat = App.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```


{{Top}}


<div class="mw-translate-fuzzy">

### Booleska Operationer 


</div>


<div class="mw-translate-fuzzy">

#### Hur klipper man ut en form från en annan? 

cut(\...)

Skillnaden mellan denna och en given topografisk form.


</div>

Subtracting a shape from another one is called \"cut\" in FreeCAD and is done like this:


```python
cylinder = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
sphere = Part.makeSphere(5, App.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur får man det gemensamma mellan två former? 

common(\...)

Skärning mellan denna och en given topografisk form.


</div>

The same way, the intersection between two shapes is called \"common\" and is done this way:


```python
cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur förenar man två former? 

fuse(\...)

Förening av denna och en given topografisk form.


</div>

Union is called \"fuse\" and works the same way:


```python
cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Hur man sektionerar en solid med given form? 

section(\...)

Sektionering av denna med en given topografisk form.

Kommer att returnera en skärningskurva, en compound med kanter


</div>

A \"section\" is the intersection between a solid shape and a plane shape. It will return an intersection curve, a compound curve composed of edges.


```python
cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
section = cylinder1.section(cylinder2)
section.Wires
> []
section.Edges
> [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
 <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
 <Edge object at 0D8F4BB0>]
```


{{Top}}

### Extrusion

Extrusion is the act of \"pushing\" a flat shape in a certain direction, resulting in a solid body. Think of a circle becoming a tube by \"pushing it out\":


```python
circle = Part.makeCircle(10)
tube = circle.extrude(App.Vector(0, 0, 2))
```

If your circle is hollow, you will obtain a hollow tube. If your circle is actually a disc with a filled face, you will obtain a solid cylinder:


```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(App.Vector(0, 0, 2))
```


{{Top}}


<div class="mw-translate-fuzzy">

## Utforska former 

du kan lätt utforska den topologiska datastrukturen:


</div>

You can easily explore the topological data structure:


```python
import Part
b = Part.makeBox(100, 100, 100)
b.Wires
w = b.Wires[0]
w
w.Wires
w.Vertexes
Part.show(w)
w.Edges
e = w.Edges[0]
e.Vertexes
v = e.Vertexes[0]
v.Point
```


<div class="mw-translate-fuzzy">

Genom att skriva in ovanstående rader i python tolken, kommer du att få en god förståelse av Del objektens struktur . Här skapade vårt makeBox() kommando en solid form. Denna solid, liksom alla Del solider, innehåller ytor. Ytor innehåller alltid trådar, vilka är listor på kanter som gränsar till ytan. Varje yta har exakt en stängd tråd. I tråden, så kan vi titta på varje kant separat, och inuti varje kant, så kan vi se hörnen. Raka kanter har förstås endast två hörn. Del Hörn är OCC former, men de har ett punktattribut vilket returnerar en snygg FreeCAD Vektor.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Utforska Kanter 

I fallet Kanter, vilken är en godtycklig kurva, så är det mycket troligt att du vill göra en diskretisering. I FreeCAD så är kanterna parametriserade av dess längder. Det innebär att du kan gå en kant/kurva genom dess längd:


</div>

In case of an edge, which is an arbitrary curve, it\'s most likely you want to do a discretization. In FreeCAD the edges are parametrized by their lengths. That means you can walk an edge/curve by its length:


```python
import Part
box = Part.makeBox(100, 100, 100)
anEdge = box.Edges[0]
print(anEdge.Length)
```


<div class="mw-translate-fuzzy">

Nu kan du komma åt många av kantens egenskaper genom att använda längden som en position. Det betyder att om

kanten är 100mm lång så är startpositionen 0 och slutpositionen 100.


</div>


```python
anEdge.tangentAt(0.0)          # tangent direction at the beginning
anEdge.valueAt(0.0)            # Point at the beginning
anEdge.valueAt(100.0)          # Point at the end of the edge
anEdge.derivative1At(50.0)     # first derivative of the curve in the middle
anEdge.derivative2At(50.0)     # second derivative of the curve in the middle
anEdge.derivative3At(50.0)     # third derivative of the curve in the middle
anEdge.centerOfCurvatureAt(50) # center of the curvature for that position
anEdge.curvatureAt(50.0)       # the curvature
anEdge.normalAt(50)            # normal vector at that position (if defined)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Använda valet 

Här ser vi nu hur vi kan använda det val som användaren gjorde i visaren.

Först av allt så skapar vi en låda och visar den i visaren


</div>

Here we see now how we can use a selection the user did in the viewer. First of all we create a box and show it in the viewer.


```python
import Part
Part.show(Part.makeBox(100, 100, 100))
Gui.SendMsgToActiveView("ViewFit")
```


<div class="mw-translate-fuzzy">

Välj nu några ytor eller kanter. Med detta skript kan du

iterera alla valda objekt och deras delelement:


</div>


```python
for o in Gui.Selection.getSelectionEx():
    print(o.ObjectName)
    for s in o.SubElementNames:
        print("name: ", s)
        for s in o.SubObjects:
            print("object: ", s)
```

Välj några kanter och detta skript kommer att beräkna längden:


```python
length = 0.0
for o in Gui.Selection.getSelectionEx():
    for s in o.SubObjects:
        length += s.Length

print("Length of the selected edges: ", length)
```


{{Top}}


<div class="mw-translate-fuzzy">

### OCC flaskan 

Ett typiskt exempel som finns på [OpenCasCade Startsida](http://www.opencascade.org/org/gettingstarted/appli/) är hur man bygger en flaska.

Detta är en god övning även för FreeCAD. Du kan faktiskt följa vårt exempel nedan och OCC sidan samtidigt , du kommer att få en god förståelse om hur OCC strukturer är implementerade i FreeCAD.

Hela skriptet nedan är även inkluderat i FreeCAD installationen (i Mod/Part mappen) och kan anropas från python tolken genom att skriva:


</div>

A typical example found on the [OpenCasCade Technology website](https://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html) is how to build a bottle. This is a good exercise for FreeCAD too. In fact, if you follow our example below and the OCC page simultaneously, you will see how well OCC structures are implemented in FreeCAD. The script is included in the FreeCAD installation (inside the **Mod/Part** folder) and can be called from the Python interpreter by typing:


```python
import Part
import MakeBottle
bottle = MakeBottle.makeBottle()
Part.show(bottle)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Det kompletta skriptet 

Här är det kompletta MakeBottle skriptet:


</div>

For the purpose of this tutorial we will consider a reduced version of the script. In this version the bottle will not be hollowed out, and the neck of the bottle will not be threaded.


```python
import FreeCAD as App
import Part, math

def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=App.Vector(-myWidth / 2., 0, 0)
    aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=App.Vector(0, -myThickness / 2., 0)
    aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=App.Vector(myWidth / 2., 0, 0)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])

    aTrsf=App.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])

    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=App.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)

    neckLocation=App.Vector(0, 0, myHeight)
    neckNormal=App.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    myBody = myBody.fuse(myNeck)

    return myBody

el = makeBottleTut()
Part.show(el)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Detaljerad förklaring 


</div>


```python
import FreeCAD as App
import Part, math
```


<div class="mw-translate-fuzzy">

Vi kommer förstås behöva Del modulen, men också FreeCAD.Base modulen, vilken innehåller grundläggande FreeCAD strukturer som vektorer och matriser.


</div>


```python
def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=App.Vector(-myWidth / 2., 0, 0)
    aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=App.Vector(0, -myThickness / 2., 0)
    aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=App.Vector(myWidth / 2., 0, 0)
```


<div class="mw-translate-fuzzy">

Här definierar vi vår makeBottle funktion. Denna funktion kan anropas utan argument, som vi gjorde ovan, i vilket fall standardvärden för bredd, höjd, och tjocklek kommer att användas. Sedan så definierar vi ett par punkter som kommer att användas för att bygga vår grundprofil.


</div>


```python
    ...
    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)
```


<div class="mw-translate-fuzzy">

Här definierar vi själva geometrin: en cirkelbåge, gjord av 3 punkter, och två linjesegment, gjorda av 2 punkter.


</div>


```python
    ...
    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
```


<div class="mw-translate-fuzzy">

Kommer du ihåg skillnaden mellan geometri och former? Här bygger vi former utifrån vår konstruktionsgeometri. 3 kanter (kanter kan vara raka eller krökta), sedan en tråd av dessa tre kanter.


</div>


```python
    ...
    aTrsf=App.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])
```


<div class="mw-translate-fuzzy">

Tills nu så har vi bara byggt en halv profil. Lättare än att bygga hela profilen på samma sätt, så behöver vi bara spegla det vi har gjort, och limma ihop båda halvorna. Så vi skapar först en matris. En matris är ett mycket vanligt sätt att tillämpa omvandlingar på objekt i 3D världen, eftersom den i en struktur kan innehålla alla grundläggande omvandlingar som 3D objekt kan påtvingas (flytta, rotera och skala). Här, efter att vi skapat matrisen, så speglar vi den, och vi skapar en kopia av vår tråd med tillämpning av vår omvandlingsmatris. Vi har nu två trådar, och vi kan göra en tredje tråd från dem, eftersom trådar egentligen är listor med kanter.


</div>


```python
    ...
    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=App.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
```


<div class="mw-translate-fuzzy">

Nu när vi har en stängd tråd, så kan den omvandlas till en yta. När vi väl har en yta, så kan vi extrudera den. Genom att göra så, så skapar vi en solid. Sedan tillämpar vi en snygg liten fasning på vårt objekt för vi vill ha en bra design, eller hur?


</div>


```python
    ...
    neckLocation=App.Vector(0, 0, myHeight)
    neckNormal=App.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
```


<div class="mw-translate-fuzzy">

När vår flaskas kropp är skapad, så behöver vi fortfarande skapa en hals. Så vi gör en ny solid, med en cylinder.


</div>


```python
    ...
    myBody = myBody.fuse(myNeck)
```


<div class="mw-translate-fuzzy">

Ihopsmältningsoperationen, vilket i andra applikationer ibland kallas för förening, är mycket kraftfull. Den kommer att limma ihop det som behövs, och ta bort de delar som inte behövs.


</div>


```python
    ...
    return myBody
```


<div class="mw-translate-fuzzy">

Sedan så får vi tillbaka vår Del solid som ett resultat av vår funktion. Denna Del solid, liksom andra Del former, kan tillskrivas ett objekt i ett FreeCAD dokument, med:


</div>


```python
el = makeBottleTut()
Part.show(el)
```


<div class="mw-translate-fuzzy">

eller, mer enkelt:


</div>


{{Top}}

## Example: Pierced box 

Here is a complete example of building a pierced box.

The construction is done one side at a time. When the cube is finished, it is hollowed out by cutting a cylinder through it.


```python
import FreeCAD as App
import Part, math

size = 10
poly = Part.makePolygon([(0, 0, 0), (size, 0, 0), (size, 0, size), (0, 0, size), (0, 0, 0)])

face1 = Part.Face(poly)
face2 = Part.Face(poly)
face3 = Part.Face(poly)
face4 = Part.Face(poly)
face5 = Part.Face(poly)
face6 = Part.Face(poly)
     
myMat = App.Matrix()

myMat.rotateZ(math.pi / 2)
face2.transformShape(myMat)
face2.translate(App.Vector(size, 0, 0))

myMat.rotateZ(math.pi / 2)
face3.transformShape(myMat)
face3.translate(App.Vector(size, size, 0))

myMat.rotateZ(math.pi / 2)
face4.transformShape(myMat)
face4.translate(App.Vector(0, size, 0))

myMat = App.Matrix()

myMat.rotateX(-math.pi / 2)
face5.transformShape(myMat)

face6.transformShape(myMat)               
face6.translate(App.Vector(0, 0, size))

myShell = Part.makeShell([face1, face2, face3, face4, face5, face6])   
mySolid = Part.makeSolid(myShell)

myCyl = Part.makeCylinder(2, 20)
myCyl.translate(App.Vector(size / 2, size / 2, 0))

cut_part = mySolid.cut(myCyl)

Part.show(cut_part)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Ladda och spara 

Det finns flera sätt att spara ditt arbetet i Del modulen. Du kan förstås spara ditt FreeCAD dokument, men du kan också spara Del objekt direkt till vanliga CAD format, som BREP, IGS, STEP och STL.


</div>

There are several ways to save your work. You can of course save your FreeCAD document, but you can also save [Part](Part_Workbench.md) objects directly to common CAD formats, such as BREP, IGS, STEP and STL.


<div class="mw-translate-fuzzy">

Att spara en form till en fil är lätt. det finns exportBrep(), exportIges(), exportStl() och exportStep() metoder tillgängliga för alla form objekt. Så genom att göra:


</div>


```python
import Part
s = Part.makeBox(10, 10, 10)
s.exportStep("test.stp")
```


<div class="mw-translate-fuzzy">

detta kommer att spara vår låda i en STEP fil. För att ladda en BREP, IGES eller STEP fil, gör bara motsatsen:


</div>


```python
import Part
s = Part.Shape()
s.read("test.stp")
```

To convert a STEP file to an IGS file:


```python
 import Part
 s = Part.Shape()
 s.read("file.stp")       # incoming file igs, stp, stl, brep
 s.exportIges("file.igs") # outbound file igs
```


{{Top}}


<div class="mw-translate-fuzzy">


{{docnav/sv|Mesh Scripting/sv|Mesh to Part/sv}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Topological data scripting/sv
