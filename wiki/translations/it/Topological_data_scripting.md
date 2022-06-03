# Topological data scripting/it
<div class="mw-translate-fuzzy">


{{docnav/it|[Script per Mesh](Mesh_Scripting/it.md)|[Da Mesh a Parte e viceversa](Mesh_to_Part/it.md)}}


</div>


{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

Qui si spiega come controllare il [Modulo Parte](Part_Workbench/it.md) direttamente tramite l\'interprete Python di FreeCAD, o tramite degli script esterni.

Se avete bisogno di ulteriori informazioni su come funzionano gli script in FreeCAD, potete consultare la sezione [Script](Scripting/it.md) e la sezione [Concetti base sugli script in FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

### Vedere anche 

-   [Script di Part](Part_scripting/it.md)
-   [OpenCASCADE](OpenCASCADE/it.md)

## Diagramma delle classi 

Questa è una panoramica delle classi [Linguaggio di Modellazione Unificato (UML)](http   *//it.wikipedia.org/wiki/Unified_Modeling_Language) più importanti del modulo Parte   *

![Python classes of the Part module](images/Part_Classes.jpg ) {{Top}}

### Geometria


<div class="mw-translate-fuzzy">

Gli oggetti geometrici sono le fondamenta per la costruzione di tutti gli oggetti topologici   *

-   **Geom** Classe base degli oggetti geometrici
-   **Line** Linea retta in 3D, definita dal punto iniziale e dal punto finale
-   **Circle** Cerchio o arco definito dal centro, dal punto iniziale e dal punto finale
-   **\...\...** E presto ancora altro


</div>


{{Top}}

### Topologia

Sono disponibili i seguenti tipi di dati topologici   *

-   **compound** Un gruppo di qualsiasi tipo di oggetto topologico.
-   **compsolid** Un solido composito è un insieme di solidi collegati dalle loro facce. E\' una estensione dei concetti *wire* e *shell* ai solidi.
-   **solid** Una parte di spazio limitato da shell. E\' tridimensionale
-   **shell** Una serie di facce connesse nei loro bordi. Una shell (guscio) può essere aperta o chiusa.
-   **face** In 2D è una parte di un piano; in 3D è una parte di una superficie. La sua geometria è vincolata (delimitata/tagliata) dai suoi bordi.
-   **wire** Una serie di bordi (una polilinea) collegati tra di loro nei vertici. Può essere un profilo aperto o chiuso, secondo se i bordi sono interamente concatenati oppure no.
-   **edge** Un elemento topologico corrispondente ad una curva limitata. Un bordo è generalmente delimitato dai vertici. Ha una dimensione.
-   **vertex** Un elemento topologico corrispondente ad un punto. Esso non ha dimensioni.
-   **shape** Un termine generico che comprende tutti i precedenti.


{{Top}}

## Esempio   * Creare una semplice topologia 

=

![Wire](images/Wire.png )


<div class="mw-translate-fuzzy">

Creeremo ora una topologia tramite la costruzione della semplice geometria. Come caso di studio, utilizzeremo una forma come quella che si vede nella figura, composta da quattro vertici, due archi e due linee.


</div>


{{Top}}

### Creare la geometria 


<div class="mw-translate-fuzzy">

Per prima cosa dobbiamo creare le singole parti geometriche di questo contorno (wire). È necessario che le parti che devono essere collegate in seguito condividere gli stessi vertici.


</div>

Quindi creiamo prima i punti   *


```python
import FreeCAD as App
import Part
V1 = App.Vector(0, 10, 0)
V2 = App.Vector(30, 10, 0)
V3 = App.Vector(30, -10, 0)
V4 = App.Vector(0, -10, 0)
```


{{Top}}

### Arco

![Circle](images/Circel.png )

Per creare un arco di cerchio prima creiamo un punto di supporto poi creiamo l\'arco di cerchio tramite tre punti   *


```python
VC1 = App.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = App.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```


{{Top}}

### Linea

![Line](images/Line.png )

La linea (segmento) può essere creata molto semplicemente tramite due punti   *


```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```


{{Top}}

### Unire tutto 


<div class="mw-translate-fuzzy">

L\'ultimo passaggio consiste nell\'unire tutti gli elementi geometrici di base e produrre una forma topologica   *


</div>


```python
S1 = Part.Shape([C1, L1, C2, L2])
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creare un prisma 

Ora si può estrudere il contorno nella direzione voluta e creare una forma 3D reale   *


</div>

Ora si può estrudere il contorno nella direzione voluta e creare una forma 3D reale   *


```python
W = Part.Wire(S1.Edges)
P = W.extrude(App.Vector(0, 0, 10))
```


{{Top}}

### Mostra tutto 


```python
Part.show(P)
```


{{Top}}

## Creare forme di base 


<div class="mw-translate-fuzzy">

Con i metodi \"make\...()\" del Modulo Parte è possibile creare facilmente oggetti topologici di base (chiamati anche forme primitive). Ad esempio, si può creare un cubo con   *


</div>


```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```


<div class="mw-translate-fuzzy">

Altri metodi make\...() disponibili sono   *

-   makeBox(l,w,h) \-- Produce un box situato in p e rivolto nella direzione d con le dimensioni (l,w,h)
-   makeCircle(raggio) \-- Crea un cerchio con un raggio dato
-   makeCone(raggio1,raggio2,altezza) \-- Restituisce un cono con raggio e altezza dati
-   makeCylinder(raggio,altezza) \-- Crea un cilindro con raggio e l\'altezza prestabilite
-   makeLine((x1,y1,z1),(x2,y2,z2)) \-- Crea una linea tra due punti
-   makePlane(lunghezza,larghezza) \-- Crea un piano con lunghezza e larghezza
-   makePolygon(lista) \-- Restituisce un poligono da una serie di punti
-   makeSphere(raggio) \-- Crea una sfera di raggio dato
-   makeTorus(raggio1,raggio2) \-- Crea un toro con raggi determinati

Per avere un elenco completo dei metodi disponibili con il modulo Parte consultare la pagina [API di Parte](Part_API/it.md) ([Part API in inglese](Part_API.md)).


</div>


{{Top}}

### Importare i moduli necessari 

First we need to import the FreeCAD and Part modules so we can use their contents in Python   *


```python
import FreeCAD as App
import Part
```


{{Top}}

### Creare un vettore 


<div class="mw-translate-fuzzy">

Per la costruzione di forme, i [Vettori](http   *//en.wikipedia.org/wiki/Euclidean_vector) sono una delle parti di informazione più importanti. Di solito, ma non necessariamente sempre, essi contengono 3 numeri che sono le coordinate cartesiane x, y e z. È possibile creare un vettore nel modo seguente   *


</div>


```python
myVector = App.Vector(3, 2, 0)
```


<div class="mw-translate-fuzzy">

Abbiamo appena creato un vettore nelle coordinate X=3, Y=2, Z=0. Nel modulo Parte, i vettori sono usati in tutte le parti. Le forme Parte usano anche un altro tipo di rappresentazione del punto, chiamato Vertex (Vertice), che in realtà non è altro che un contenitore per un vettore. Si accede al vettore di un vertice in questo modo   *


</div>


```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```


{{Top}}

#### Creare un bordo 

Un bordo non è altro che una linea con due vertici   *


```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

Nota   * È anche possibile creare un bordo passando due vettori   *


```python
vec1 = App.Vector(0, 0, 0)
vec2 = App.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

È possibile trovare la lunghezza e il centro di un bordo in questo modo   *


```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```


{{Top}}

### Mostrare la forma sullo schermo 


<div class="mw-translate-fuzzy">

Con le operazioni precedenti abbiamo creato un oggetto bordo, ma esso non è visibile da nessuna parte sullo schermo. Questo perché la scena 3D di FreeCAD mostra solo quello che gli si chiede di visualizzare. Per farlo, usiamo questo semplice metodo   *


</div>


```python
Part.show(edge)
```


<div class="mw-translate-fuzzy">

La funzione show crea un oggetto nel nostro documento FreeCAD e gli assegna la forma \"edge\". Utilizzare questo metodo ogni volta che si vuole visulizzare il proprio prodotto sullo schermo.


</div>


{{Top}}

### Creare un contorno 


<div class="mw-translate-fuzzy">

Un contorno è una polilinea e può essere creato da una serie di bordi o anche da una serie di contorni   *


</div>


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


`Part.show(wire3)`

serve per visualizzare i 4 bordi che compongono il nostro contorno. Si possono facilmente recuperare altre informazioni utili con   *


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

### Creare una faccia 


<div class="mw-translate-fuzzy">

Sono valide solo le facce create da contorni chiusi. Nell\'esempio, wire3 è un contorno chiuso, ma wire2 non è un contorno chiuso (vedi esempio precedente)


</div>


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

Solamente le facce hanno un\'area, non i contorni né i bordi. {{Top}}

### Creare una circonferenza 

Un cerchio può essere creato in questo semplice modo   *


```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius    * 10, Position    * (0, 0, 0), Direction    * (0, 0, 1))
```

Se si vuole crearlo in una determinata posizione e con una direzione prestabilita   *


```python
ccircle = Part.makeCircle(10, App.Vector(10, 0, 0), App.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius    * 10, Position    * (10, 0, 0), Direction    * (1, 0, 0))
```


<div class="mw-translate-fuzzy">

ccircle verrà creato a distanza 10 dall\'origine di X e sarà rivolto verso l\'asse X. Nota   * `makeCircle()` accetta solo `Base.Vector()` per la posizione e le normali, ma non tuple. È inoltre possibile creare una parte di cerchio fornendo un angolo iniziale e un angolo finale come   *


</div>


```python
from math import pi
arc1 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180, 360)
```

Unendo arc1 con arc2 (sono due semicerchi) si ottiene un cerchio completo. Gli angoli devono essere forniti in gradi; se avete angoli in radianti convertirli usando semplicemente la formula   * `gradi <nowiki>=</nowiki> radianti * 180/pi` o utilizzando il modulo matematico `math` di Python   *


```python
import math
degrees = math.degrees(radians)
```


{{Top}}

### Creare un arco attraverso dei punti 


<div class="mw-translate-fuzzy">

Purtroppo, per creare un arco lungo tre punti non esiste una funzione makeArc ma si deve usare la funzione Part.Arc. Fondamentalmente si può pensare come un arco che unisce il punto iniziale e finale passando per il punto medio. Part.Arc crea un oggetto arco nel quale deve essere chiamato .toShape() per ottenere un oggetto bordo, allo stesso modo di quando si usa Part.LineSegment al posto di Part.makeLine.


</div>


```python
arc = Part.Arc(App.Vector(0, 0, 0), App.Vector(0, 5, 0), App.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```


<div class="mw-translate-fuzzy">


`Arc()`

accetta solo punti `Base.Vector()` , ma non tuple. Inoltre è possibile ottenere un arco utilizzando una porzione di un cerchio   *


</div>


```python
from math import pi
circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```

Gli archi sono bordi validi, come le linee, quindi possono essere usati anche nei contorni. {{Top}}

### Creare un poligono 


<div class="mw-translate-fuzzy">

Un poligono è semplicemente un contorno composto da diversi bordi diritti. La funzione makePolygon prende una lista di punti e crea un contorno attraverso questi punti   *


</div>


```python
lshape_wire = Part.makePolygon([App.Vector(0, 5, 0), App.Vector(0, 0, 0), App.Vector(5, 0, 0)])
```


{{Top}}


<div class="mw-translate-fuzzy">

### Creare una curva di Bézier 


</div>


<div class="mw-translate-fuzzy">

Le curve di Bézier sono utilizzate per modellare delle curve *morbide* utilizzando una serie di Poles (punti) e weight (pesi) opzionali. La funzione sottostante crea una Part.BezierCurve da una serie di punti FreeCAD.Vector. (Notare che gli indici di pole e di weight partono da 1, non da 0.)


</div>


```python
def makeBCurveEdge(Points)   *
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```


{{Top}}

### Creare un piano 


<div class="mw-translate-fuzzy">

Un Piano è semplicemente una superficie piana rettangolare. Il metodo utilizzato per crearlo è questo   * **makePlane(lunghezza, larghezza, \[start\_pnt, dir\_normal\])**. Per impostazione predefinita start\_pnt=Vector (0,0,0) e dir\_normal=Vector(0,0,1). Utilizzando dir\_normal=Vector(0,0,1) creeremo il piano orientato come l\'asse z positivo, mentre con dir\_normal=Vector(1,0,0) creeremo il piano orientato come l\'asse x positivo   *


</div>


```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, App.Vector(3, 0, 0), App.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```


<div class="mw-translate-fuzzy">


`BoundBox`

è il parallelepipedo che racchiude il piano e la cui diagonale parte da (3,0,0) e termina in (5,0,2). Qui lo spessore di `BoundBox` sull\'asse y è zero, poiché la nostra forma è totalmente piatta.


</div>


<div class="mw-translate-fuzzy">

Nota   * `makePlane()` accetta solo `Base.Vector()` per start\_pnt e dir\_normal e non tuple.


</div>


{{Top}}

### Creare una ellisse 

Per creare un\'ellisse ci sono diversi modi   *


```python
Part.Ellipse()
```

Crea un\'ellisse con raggio maggiore 2 e raggio minore 1 con centro in (0,0,0).


```python
Part.Ellipse(Ellipse)
```

Crea una copia dell\'ellisse data.


```python
Part.Ellipse(S1, S2, Center)
```


<div class="mw-translate-fuzzy">

Crea un\'ellisse centrato sul punto Center, in cui il piano dell\'ellisse è definito da Center, S1 e S2, il suo asse maggiore è definito da Center e S1, il suo raggio maggiore è la distanza tra Center e S1, e il suo raggio minore è la distanza tra S2 e l\'asse maggiore.


</div>


```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```


<div class="mw-translate-fuzzy">

Crea un\'ellisse con il raggio maggiore e il raggio minore MajorRadius e MinorRadius, situata nel piano definito da Center e la normale (0,0,1)


</div>


```python
eli = Part.Ellipse(App.Vector(10, 0, 0), App.Vector(0, 5, 0), App.Vector(0, 0, 0))
Part.show(eli.toShape())
```


<div class="mw-translate-fuzzy">

Nel codice precedente abbiamo passato S1, S2 e il centro. Analogamente a Arco, Ellisse crea un oggetto ellisse ma non un bordo, quindi, per visualizzarlo è necessario di convertirlo in bordo utilizzando toShape().


</div>


<div class="mw-translate-fuzzy">

Nota   * `Ellipse()` accetta solo `Base.Vector()` per i punti, ma non le tuple.


</div>


```python
eli = Part.Ellipse(App.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```

Per il costruttore Ellisse precedente abbiamo passato il centro, MajorRadius e MinorRadius. {{Top}}

### Creare un toro 


<div class="mw-translate-fuzzy">

Utilizzando il metodo **makeTorus(radius1,radius2,\[pnt,dir,angle1,angle2,angle\])**. Per impostazione predefinita PNT=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=360 e angolo=360. Si consideri un toro, come un cerchio piccolo che si muove lungo un cerchio grande. Radius1 è il raggio del cerchio grande, radius2 è il raggio del cerchio piccolo, pnt è il centro del toro e dir è la direzione normale. angle1 e angle2 sono angoli in radianti per il cerchio piccolo cerchio, l\'ultimo parametro angolo serve per realizzare una porzione del toro   *


</div>


```python
torus = Part.makeTorus(10, 2)
```


<div class="mw-translate-fuzzy">

Il codice precedente creerà un toro con diametro 20 (raggio 10) e spessore di 4 (raggio del cerchio piccolo 2)


</div>


```python
tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
```

Il codice sopra creerà una fetta del toro.


```python
tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 360, 180)
```


<div class="mw-translate-fuzzy">

Il codice precedente creerà un semi toro; solo l\'ultimo parametro viene modificato vale a dire l\'angolo e gli angoli rimanenti sono predefiniti. Impostare il valore dell\'angolo a 180 creerà il toro da 0 a 180, cioè, un mezzo toro.


</div>


{{Top}}

### Creare un cubo o parallelepipedo 

Utilizzando `makeBox(length, width, height, [pnt, dir])`. Per impostazione predefinita pnt=Vector(0,0,0) e dir=Vector(0,0,1).


```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creare una sfera 

Utilizzando **makeSphere(radius,\[pnt, dir, angle1,angle2,angle3\])**. Per impostazione predefinita pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=-90, angle2=90 e angle3=360. angle1 e angle2 sono il minimo e il massimo in verticale della sfera, angle3 è il diametro della sfera stessa.


</div>

Using `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 and angle3 = 360. Angle1 and angle2 are the vertical minimum and maximum of the sphere, angle3 is the sphere diameter.


```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), -90, 90, 180)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creare un cilindro 

Utilizzando **makeCylinder(radius,height,\[pnt,dir,angle\])**. Per impostazione predefinita pnt=Vector(0,0,0),dir=Vector(0,0,1) e angle=360.


</div>

Using `makeCylinder(radius, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360.


```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Creare un cono 

Utilizzando **makeCone(radius1,radius2,height,\[pnt,dir,angle\])**. Per impostazione predefinita pnt=Vector(0,0,0), dir=Vector(0,0,1) e angle=360.


</div>

Using `makeCone(radius1, radius2, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360.


```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Modificare delle forme 

Ci sono diversi modi per modificare le forme. Alcuni sono semplici operazioni di trasformazione come lo spostamento o la rotazione di forme, altri sono più complessi, come ad esempio unire e sottrarre una forma da un\'altra.


</div>

There are several ways to modify shapes. Some are simple transformation operations such as moving or rotating shapes, others are more complex, such as unioning and subtracting one shape from another. {{Top}}


<div class="mw-translate-fuzzy">

### Operazioni di trasformazione 


</div>


<div class="mw-translate-fuzzy">

#### Traslare una forma 

Traslare è l\'atto di spostare una forma da un luogo all\'altro. Qualsiasi forma (bordo, faccia, cubo, ecc ..) può essere traslata in questo modo   *


</div>

Translating is the act of moving a shape from one place to another. Any shape (edge, face, cube, etc\...) can be translated the same way   *


```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(App.Vector(2, 0, 0))
```


<div class="mw-translate-fuzzy">

Questo sposterà la forma \"myShape\" di 2 unità nella direzione dell\'asse x.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### Ruotare una forma 

Per ruotare una forma, è necessario specificare il centro di rotazione, l\'asse e l\'angolo di rotazione   *


</div>

To rotate a shape, you need to specify the rotation center, the axis, and the rotation angle   *


```python
myShape.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 180)
```

Il codice precedente ruota la forma di 180 gradi attorno all\'asse z. {{Top}}


<div class="mw-translate-fuzzy">

#### Trasformazioni generiche, con matrici 

Una matrice è un modo molto conveniente per memorizzare le trasformazioni nel mondo 3D. In una matrice singola, è possibile impostare valori di traslazione, rotazione e scala da applicare ad un oggetto. Ad esempio   *


</div>

A matrix is a very convenient way to store transformations in the 3D world. In a single matrix, you can set translation, rotation and scaling values to be applied to an object. For example   *


```python
myMat = App.Matrix()
myMat.move(App.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
```


<div class="mw-translate-fuzzy">

Nota. Le matrici di FreeCAD lavorano in radianti. Inoltre, quasi tutte le operazioni di matrici che accettano un vettore possono anche accettare tre numeri, quindi le seguenti due linee fanno la stessa cosa   *


</div>


```python
myMat.move(2, 0, 0)
myMat.move(App.Vector(2, 0, 0))
```


<div class="mw-translate-fuzzy">

Quando la matrice è impostata, possiamo applicarla alla nostra forma. FreeCAD fornisce due metodi per farlo   * transformShape() e transformGeometry(). La differenza è che con il primo, si è sicuri che non si verifichino deformazioni (vedi \"scalare una forma\" più avanti). Quindi possiamo applicare la nostra trasformazione in questo modo   *


</div>


```python
myShape.transformShape(myMat)
```

oppure


```python
myShape.transformGeometry(myMat)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Scalare una forma 

Scalare (ridimensionare) una forma è una delle operazioni più pericolose perché, a differenza della traslazione o della rotazione, il ridimensionamento non uniforme (con valori diversi per gli assi x, y, z) può modificare la struttura della forma. Ad esempio, la scalatura di un cerchio con un valore in orizzontale diverso da quello in verticale lo trasformerà in un ellisse, forma che matematicamente si comporta in modo molto diverso. Per il ridimensionamento, non possiamo usare transformShape, ma dobbiamo usare transformGeometry()   *


</div>

Scaling a shape is a more dangerous operation because, unlike translation or rotation, scaling non-uniformly (with different values for X, Y and Z) can modify the structure of the shape. For example, scaling a circle with a higher value horizontally than vertically will transform it into an ellipse, which behaves mathematically very differently. For scaling, we cannot use the `transformShape()`, we must use `transformGeometry()`   *


```python
myMat = App.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```


{{Top}}


<div class="mw-translate-fuzzy">

### Operazioni Booleane 


</div>


<div class="mw-translate-fuzzy">

#### Sottrazione

Nel gergo OCC/FreeCAD, la differenza (sottrazione) di una forma da un altra si chiama \"cut\" *taglia* e si esegue così   *


</div>

Subtracting a shape from another one is called \"cut\" in FreeCAD and is done like this   *


```python
cylinder = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
sphere = Part.makeSphere(5, App.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Intersezione

Allo stesso modo, l\'intersezione tra le due forme è chiamato \"common\" *intersezione* e viene eseguita in questo modo   *


</div>

The same way, the intersection between two shapes is called \"common\" and is done this way   *


```python
cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Unione

Unione è chiamata \"fuse\" *fusione* e funziona allo stesso modo   *


</div>

Union is called \"fuse\" and works the same way   *


```python
cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### Sezione

Una sezione è l\'intersezione tra una forma solida e una forma piana. Restituisce una curva di intersezione, un composto con i bordi   *


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


<div class="mw-translate-fuzzy">

#### Estrusione

Estrusione è l\'atto di \"spingere\" una forma piatta in una certa direzione per produrre un corpo solido. Ad esempio, pensate di \"spingere\" un cerchio e di produrre un tubo   *


</div>

Extrusion is the act of \"pushing\" a flat shape in a certain direction, resulting in a solid body. Think of a circle becoming a tube by \"pushing it out\"   *


```python
circle = Part.makeCircle(10)
tube = circle.extrude(App.Vector(0, 0, 2))
```


<div class="mw-translate-fuzzy">

Se il cerchio è vuoto (sola circonferenza), si ottiene un tubo (cavo). Se il cerchio è in realtà un disco, con una faccia piena, si ottiene un cilindro solido   *


</div>


```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(App.Vector(0, 0, 2))
```


{{Top}}


<div class="mw-translate-fuzzy">

## Esplorare le forme 

Si può facilmente esplorare la struttura dei dati topologici   *


</div>

You can easily explore the topological data structure   *


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

Digitando le righe di cui sopra nell\'interprete Python, si otterrà una buona descrizione della struttura degli oggetti Parte. Qui, il nostro comando makeBox() crea una forma solida. Questo solido, come tutti i solidi Parte, contiene delle facce. Le facce contengono sempre delle linee (polilinee), che sono liste di bordi che delimitano la faccia. Ciascuna faccia ha almeno un contorno chiuso (ne può avere più di uno se la faccia presenta dei fori). Nel contorno, possiamo guardare a ciascun bordo separatamente, e all\'interno di ogni bordo, possiamo vedere i vertici. Ovviamente, i bordi diritti hanno solo due vertici.


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### Analizzare i bordi 

Nel caso in cui il bordo è una curva arbitraria, è più probabile che si voglia fare una discretizzazione. In FreeCAD i bordi sono parametrizzati dalle loro lunghezze. Ciò significa che si può percorrere un bordo/curva con la sua lunghezza   *


</div>

In case of an edge, which is an arbitrary curve, it\'s most likely you want to do a discretization. In FreeCAD the edges are parametrized by their lengths. That means you can walk an edge/curve by its length   *


```python
import Part
box = Part.makeBox(100, 100, 100)
anEdge = box.Edges[0]
print(anEdge.Length)
```


<div class="mw-translate-fuzzy">

Ora è possibile accedere a un sacco di proprietà del bordo utilizzando la lunghezza come una posizione. Ciò significa che se il bordo è lungo 100 mm la posizione iniziale è 0 e la posizione finale è 100.


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

### Utilizzare la selezione 

Qui ora vediamo come possiamo usare la selezione che l\'utente ha nel visualizzatore. Prima di tutto creiamo una scatola e la mostriamo nel visualizzatore   *


</div>

Here we see now how we can use a selection the user did in the viewer. First of all we create a box and show it in the viewer.


```python
import Part
Part.show(Part.makeBox(100, 100, 100))
Gui.SendMsgToActiveView("ViewFit")
```


<div class="mw-translate-fuzzy">

Selezionate ora alcune facce o bordi. Con questo script è possibile iterare sopra tutti gli oggetti selezionati e i relativi elementi secondari   *


</div>


```python
for o in Gui.Selection.getSelectionEx()   *
    print(o.ObjectName)
    for s in o.SubElementNames   *
        print("name   * ", s)
        for s in o.SubObjects   *
            print("object   * ", s)
```

Selezionate alcuni bordi e questo script calcolerà la lunghezza   *


```python
length = 0.0
for o in Gui.Selection.getSelectionEx()   *
    for s in o.SubObjects   *
        length += s.Length

print("Length of the selected edges   * ", length)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Esempio completo   * La bottiglia OCC 

Un esempio tipico si trova nella pagina [OpenCasCade Technology Tutorial](http   *//www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html#sec1) che spiega come costruire una bottiglia. Questo è un buon esercizio anche per FreeCAD. In effetti, se si segue il nostro esempio qui sotto e la pagina di OCC contemporaneamente, si capisce bene come sono implementate le strutture di OCC in FreeCAD. Lo script completo è anche incluso nell\'installazione di FreeCAD (all\'interno della cartella Mod/Part) e può essere chiamato dall\'interprete python digitando   *


</div>

A typical example found on the [OpenCasCade Technology website](https   *//www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html) is how to build a bottle. This is a good exercise for FreeCAD too. In fact, if you follow our example below and the OCC page simultaneously, you will see how well OCC structures are implemented in FreeCAD. The script is included in the FreeCAD installation (inside the **Mod/Part** folder) and can be called from the Python interpreter by typing   *


```python
import Part
import MakeBottle
bottle = MakeBottle.makeBottle()
Part.show(bottle)
```


{{Top}}


<div class="mw-translate-fuzzy">

### Lo script completo 

Questo è lo script completo MakeBottle   *


</div>

For the purpose of this tutorial we will consider a reduced version of the script. In this version the bottle will not be hollowed out, and the neck of the bottle will not be threaded.


```python
import FreeCAD as App
import Part, math

def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0)   *
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

### Spiegazione dettagliata 


</div>


```python
import FreeCAD as App
import Part, math
```


<div class="mw-translate-fuzzy">

Avremo bisogno, naturalmente, del modulo Parte, ma anche del modulo FreeCAD.Base, che contiene le strutture base di FreeCAD come vettori e matrici.


</div>


```python
def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0)   *
    aPnt1=App.Vector(-myWidth / 2., 0, 0)
    aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=App.Vector(0, -myThickness / 2., 0)
    aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=App.Vector(myWidth / 2., 0, 0)
```


<div class="mw-translate-fuzzy">

Qui definiamo la nostra funzione makeBottle. Questa funzione può essere chiamata senza argomenti, come abbiamo fatto in precedenza, nel qual caso si utilizzano i valori di default per la larghezza, l\'altezza e lo spessore. Poi, si definisce un paio di punti che verranno utilizzati per costruire il nostro profilo base.


</div>


```python
    ...
    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)
```


<div class="mw-translate-fuzzy">

Qui definiamo la geometria effettiva   * un arco, creato da tre punti, e due segmenti di linea, creati da due punti.


</div>


```python
    ...
    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
```


<div class="mw-translate-fuzzy">

Ricordate la differenza tra geometria e forme? Qui costruiremo forme partendo dalla nostra geometria di costruzione. Prima costruiremo tre bordi (i bordi possono essere dritti o curvi), poi costruiremo un contorno con quei tre bordi.


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

Prima abbiamo costruito solo metà profilo. È più facile che costruire tutto l\'intero profilo nello stesso modo, successivamente possiamo semplicemente rispecchiare quello che abbiamo costruito, e poi unire le due parti. Per prima cosa è necessario creare una matrice. Una matrice è un modo molto comune per applicare trasformazioni agli oggetti nel mondo 3D, in quanto essa può contenere in un\'unica struttura tutte le trasformazioni di base che gli oggetti 3D possono subire (spostamento, rotazione e scalatura). Dopo aver creato la matrice, la specchiamo e creiamo una copia del nostro contorno applicando ad esso quella matrice di trasformazione. Ora abbiamo due contorni, e con essi possiamo produrre un terzo profilo, dal momento che i contorni sono in realtà liste di bordi.


</div>


```python
    ...
    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=App.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
```


<div class="mw-translate-fuzzy">

Ora che abbiamo un contorno chiuso, esso può essere trasformato in una faccia. Una volta che abbiamo una faccia, possiamo estruderla. In questo modo, abbiamo effettivamente creato un solido. Poi si applica un piccolo arrotondamento al nostro oggetto, perché vogliamo ottenere una forma graziosa, non è vero?


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

A questo punto, il corpo della nostra bottiglia è creato, ma abbiamo ancora bisogno di creare un collo. Così facciamo un nuovo solido, con un cilindro.


</div>


```python
    ...
    myBody = myBody.fuse(myNeck)
```


<div class="mw-translate-fuzzy">

L\'operazione di fusione, che in altre applicazioni a volte è chiamata unione, è molto potente. Si prenderà cura di incollare ciò che deve essere incollato e di rimuovere le parti che devono essere rimosse.


</div>


```python
    ...
    return myBody
```

Poi, otteniamo il nostro solido Parte come risultato della nostra funzione.


```python
el = makeBottleTut()
Part.show(el)
```

Infine, chiamiamo la funzione per creare effettivamente la parte, e quindi renderla visibile. {{Top}}


<div class="mw-translate-fuzzy">

## Cubo forato 

Ecco un esempio completo della costruzione di una scatola perforata.


</div>

Here is a complete example of building a pierced box.


<div class="mw-translate-fuzzy">

La costruzione è fatta lato per lato e quando il cubo è finito, viene scavato un foro con cilindro che l\'attraversa.


</div>


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

## Caricare e salvare 

Nel modulo Parte ci sono diversi modi per salvare il proprio lavoro. Naturalmente, è possibile salvare il documento in formato FreeCAD, ma è anche possibile salvare gli oggetti Parte direttamente nei comuni formati CAD, come ad esempio BREP, IGS, STEP e STL.


</div>

There are several ways to save your work. You can of course save your FreeCAD document, but you can also save [Part](Part_Workbench.md) objects directly to common CAD formats, such as BREP, IGS, STEP and STL.


<div class="mw-translate-fuzzy">

Salvare una forma in un file è facile. Per tutti gli oggetti di forma sono disponibili i metodi exportBrep(), exportIges(), exportStl() e exportStep(). Così, facendo   *


</div>


```python
import Part
s = Part.makeBox(10, 10, 10)
s.exportStep("test.stp")
```


<div class="mw-translate-fuzzy">

salviamo il nostro box in un file STEP. Per caricare un file BREP, IGES o STEP basta fare   *


</div>


```python
import Part
s = Part.Shape()
s.read("test.stp")
```


<div class="mw-translate-fuzzy">

Per convertire un file **.stp** in un file **.igs** fare   *


</div>


```python
 import Part
 s = Part.Shape()
 s.read("file.stp")       # incoming file igs, stp, stl, brep
 s.exportIges("file.igs") # outbound file igs
```


{{Top}}


<div class="mw-translate-fuzzy">


{{docnav/it|[Script per Mesh](Mesh_Scripting/it.md)|[Da Mesh a Parte e viceversa](Mesh_to_Part/it.md)}}


</div>




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Topological data scripting/it
