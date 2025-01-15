# Topological data scripting/it
{{docnav/it
|[Script di Part](Part_scripting/it.md)
|[Oggetti creati da script](Scripted_objects/it.md)
}}






## Introduzione

Qui si spiega come controllare il modulo [Part](Part_Workbench/it.md) direttamente dall\'interprete Python di FreeCAD o da qualsiasi script esterno. Assicurarsi di sfogliare la sezione [Script](Scripting/it.md) e la sezione [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md) se hai bisogno di maggiori informazioni su come funziona lo scripting Python in FreeCAD. Se non conosci Python, è una buona idea leggere prima la [Introduzione a Python](Introduction_to_Python/it.md).



### Vedere anche 

-   [Script di Part](Part_scripting/it.md)
-   [OpenCASCADE](OpenCASCADE/it.md)



## Diagramma delle classi 

Questa è una panoramica delle classi del [Linguaggio di Modellazione Unificato (UML)](http://it.wikipedia.org/wiki/Unified_Modeling_Language) più importanti del modulo Parte:

![Python classes of the Part module](images/Part_Classes.jpg ) 

### Geometria

Gli oggetti geometrici sono le fondamenta per la costruzione di tutti gli oggetti topologici:

-   **Geom** Classe base degli oggetti geometrici
-   **Line** Linea retta in 3D, definita dal punto iniziale e dal punto finale
-   **Circle** Cerchio o arco definito dal centro, dal punto iniziale e dal punto finale
-   Ecc.


{{Top}}



### Topologia

Sono disponibili i seguenti tipi di dati topologici:

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



## Esempio: Creare una semplice topologia 

![Wire](images/Wire.png )

Creeremo ora una topologia tramite la costruzione della semplice geometria. Come caso di studio, utilizzeremo una forma come quella che si vede nella figura, composta da quattro vertici, due archi e due linee. 

### Creare la geometria 

Per prima cosa creiamo le parti geometriche distinte di questo wire. Assicurarsi che le parti, che devono essere collegate in seguito, condividano gli stessi vertici.

Quindi creiamo prima i punti:


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

Per creare un arco di cerchio prima creiamo un punto di supporto poi creiamo l\'arco di cerchio tramite tre punti:


```python
VC1 = App.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = App.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```


{{Top}}



### Linea

![Line](images/Line.png )

La linea (segmento) può essere creata molto semplicemente tramite due punti:


```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```


{{Top}}



### Unire tutto 

L\'ultimo passaggio consiste nell\'unire tutti gli elementi geometrici di base e produrre una forma topologica:


```python
S1 = Part.Shape([C1, L1, C2, L2])
```


{{Top}}



#### Creare un prisma 

Ora si può estrudere il contorno nella direzione voluta e creare una forma 3D reale:


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

Si possono creare facilmente gli oggetti topologici di base con i metodi `make...()` del modulo Part:


```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```

Alcuni metodi `make...()` disponibili:

-    `makeBox(l, w, h, [p, d])`Crea un riquadro situato in p e rivolto nella direzione d con le dimensioni (l,w,h).

-    `makeCircle(radius)`Crea un cerchio con un dato raggio.

-    `makeCone(radius1, raggio2, altezza)`Crea un cono dati i raggi e l\'altezza.

-    `makeCylinder(radius, height)`Crea un cilindro con un determinato raggio e altezza.

-    `makeLine((x1, y1, z1), (x2, y2, z2))`Crea una linea da due punti.

-    `makePlane(length, width)`Crea un piano con lunghezza e larghezza.

-    `makePolygon(list)`Crea un poligono da una serie di punti.

-    `makeSphere(radius)`Crea una sfera con un dato raggio.

-    `makeTorus(radius1, raggio2)`Crea un toro con i raggi dati.

Vedere la pagina [API di Part](Part_API/it.md) o [Documentazione Python Part API autogenerata](https://freecad-python-stubs.readthedocs.io/en/latest/autoapi/Part/) per un elenco completo dei metodi disponibili del modulo Part. 

### Importare i moduli necessari 

Per prima cosa dobbiamo importare i moduli di FreeCAD e Part in modo da poter utilizzare i loro contenuti in Python:


```python
import FreeCAD as App
import Part
```


{{Top}}



### Creare un vettore 

Per la costruzione di forme, i [Vettori](https://it.wikipedia.org/wiki/Vettore_(matematica)) sono una delle informazioni più importanti. Di solito contengono tre numeri (ma non necessariamente sempre): le coordinate cartesiane X, Y e Z. È possibile creare un vettore nel modo seguente:


```python
myVector = App.Vector(3, 2, 0)
```

Abbiamo appena creato un vettore alle coordinate X = 3, Y = 2, Z = 0. Nel modulo Part, i vettori sono usati ovunque. Le forme di Part utilizzano anche un altro tipo di rappresentazione del punto chiamata Vertice, che è semplicemente un contenitore per un vettore. Si accede al vettore di un vertice in questo modo:


```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```


{{Top}}



#### Creare un bordo 

Un bordo non è altro che una linea con due vertici:


```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

Nota: È anche possibile creare un bordo passando due vettori:


```python
vec1 = App.Vector(0, 0, 0)
vec2 = App.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

È possibile trovare la lunghezza e il centro di un bordo in questo modo:


```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```


{{Top}}



### Mostrare la forma sullo schermo 

Con le operazioni precedenti abbiamo creato un oggetto bordo, ma esso non è visibile da nessuna parte sullo schermo. Questo perché la scena 3D di FreeCAD mostra solo quello che gli si chiede di visualizzare. Per farlo, usiamo questo semplice metodo:


```python
Part.show(edge)
```

La funzione show crea un oggetto nel nostro documento FreeCAD e gli assegna la forma \"edge\". Utilizzare questo metodo ogni volta che si vuole visualizzare il proprio prodotto sullo schermo. 

### Creare un contorno 

Un contorno è una linea multi-spigolo e può essere creato da un elenco di bordi o anche da un elenco di contorni:


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


`Part.show(wire3)`

mostrerà i 4 bordi che compongono il nostro contorno. Altre informazioni utili possono essere facilmente recuperate con:


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

Sono valide solo le facce create da contorni chiusi. Nell\'esempio, wire3 è un contorno chiuso, ma wire2 non è un contorno chiuso (vedi esempio precedente)


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

Solamente le facce hanno un\'area, non i contorni né i bordi. 

### Creare una circonferenza 

Un cerchio può essere creato in questo semplice modo:


```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
```

Se si vuole crearlo in una determinata posizione e con una direzione prestabilita:


```python
ccircle = Part.makeCircle(10, App.Vector(10, 0, 0), App.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
```

ccircle verrà creato a distanza 10 dall\'origine di X e sarà rivolto verso l\'asse X. Nota: `makeCircle()` accetta solo `App.Vector()` per la posizione e le normali, ma non tuple. È inoltre possibile creare una parte di cerchio fornendo un angolo iniziale e un angolo finale come:


```python
from math import pi
arc1 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180, 360)
```

Unendo arc1 con arc2 (sono due semicerchi) si ottiene un cerchio completo. Gli angoli devono essere forniti in gradi; se avete angoli in radianti convertirli usando semplicemente la formula: `gradi <nowiki>=</nowiki> radianti * 180/pi` o utilizzando il modulo matematico `math` di Python:


```python
import math
degrees = math.degrees(radians)
```


{{Top}}



### Creare un arco attraverso dei punti 

Sfortunatamente non esiste una funzione `makeArc()`, ma abbiamo la funzione `Part.Arc()` per creare un arco attraverso tre punti. Crea un oggetto arco, che unisce il punto iniziale al punto finale attraverso il punto medio. La funzione `toShape()` dell\'oggetto arc deve essere chiamata per ottenere un oggetto edge, come quando si usa `Part.LineSegment` invece di `Part.makeLine`.


```python
arc = Part.Arc(App.Vector(0, 0, 0), App.Vector(0, 5, 0), App.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```


`Arc()`

accetta solo `App.Vector()` per i punti e non tuple. Si può anche ottenere un arco usando una porzione di cerchio:


```python
from math import pi
circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```

Gli archi sono bordi validi, come le linee, quindi possono essere usati anche nei contorni. 

### Creare un poligono 

Un poligono è semplicemente un contorno con più bordi dritti. La funzione `makePolygon()` prende una lista di punti e crea un contorno attraverso quei punti:


```python
lshape_wire = Part.makePolygon([App.Vector(0, 5, 0), App.Vector(0, 0, 0), App.Vector(5, 0, 0)])
```


{{Top}}



### Creare una curva di Bézier 

Le curve di Bézier vengono utilizzate per modellare curve morbide utilizzando una serie di poli (punti) e pesi opzionali. La funzione seguente crea un `Part.BezierCurve()` da una serie di punti `FreeCAD.Vector()`. Nota: quando si usano \"getting\" e \"setting\" per un singolo polo o peso, gli indici iniziano da 1, non da 0.


```python
def makeBCurveEdge(Points):
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```


{{Top}}



### Creare un piano 

Un piano è una superficie rettangolare piana. Il metodo utilizzato per crearne uno è `makePlane(length, width, [start_pnt, dir_normal])`. Per impostazione predefinita start_pnt = Vector(0, 0, 0) e dir_normal = Vector(0, 0, 1). Usando dir_normal = Vector(0, 0, 1) si creerà il piano rivolto nella direzione positiva dell\'asse Z, mentre dir_normal = Vector(1, 0, 0) si creerà il piano rivolto nella direzione positiva dell\'asse X:


```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, App.Vector(3, 0, 0), App.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```


`BoundBox`

è il parallelepipedo che racchiude il piano e la cui diagonale parte da (3,0,0) e termina in (5,0,2). Qui lo spessore di `BoundBox` sull\'asse y è zero, poiché la nostra forma è totalmente piatta.

Nota: 

### Creare una ellisse 

Per creare un\'ellisse ci sono diversi modi:


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

Crea un\'ellisse centrata sul punto Center, in cui il piano dell\'ellisse è definito da Center, S1 e S2, il suo asse maggiore è definito da Center e S1, il suo raggio maggiore è la distanza tra Center e S1, e il suo raggio minore è la distanza tra S2 e l\'asse maggiore.


```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```

Crea un\'ellisse con il raggio maggiore e il raggio minore MajorRadius e MinorRadius, situata nel piano definito da Center e la normale (0,0,1)


```python
eli = Part.Ellipse(App.Vector(10, 0, 0), App.Vector(0, 5, 0), App.Vector(0, 0, 0))
Part.show(eli.toShape())
```

Nel codice sopra abbiamo passato S1, S2 e il centro. Analogamente a `Arc`, `Ellipse` crea un oggetto ellisse, ma non un bordo, quindi dobbiamo convertirlo in un bordo usando `toShape()` per visualizzarlo.

Nota: `Ellipse()` accetta solo `App.Vector()` per i punti, ma non le tuple.


```python
eli = Part.Ellipse(App.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```

Per il costruttore Ellisse precedente abbiamo passato il centro, MajorRadius e MinorRadius. 

### Creare un toro 

Utilizzare il metodo `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])`. Per impostazione predefinita PNT=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=360 e angolo=360. Si consideri un toro, come un cerchio piccolo che si muove lungo un cerchio grande. Radius1 è il raggio del cerchio grande, radius2 è il raggio del cerchio piccolo, pnt è il centro del toro e dir è la direzione normale. angle1 e angle2 sono angoli in radianti per il cerchio piccolo cerchio, l\'ultimo parametro angolo serve per realizzare una porzione del toro:


```python
torus = Part.makeTorus(10, 2)
```

Il codice precedente creerà un toro con diametro 20 (raggio 10) e spessore di 4 (raggio del cerchio piccolo pari a 2)


```python
tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 180)
```

Il codice sopra creerà una fetta del toro.


```python
tor=Part.makeTorus(10, 5, App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0, 360, 180)
```

Il codice precedente creerà un semi toro; solo l\'ultimo parametro viene modificato vale a dire l\'angolo e gli angoli rimanenti sono predefiniti. Impostare il valore dell\'angolo a 180 creerà il toro da 0 a 180, cioè, un mezzo toro. 

### Creare un cubo o parallelepipedo 

Utilizzando `makeBox(length, width, height, [pnt, dir])`. Per impostazione predefinita pnt=Vector(0,0,0) e dir=Vector(0,0,1).


```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```


{{Top}}



### Creare una sfera 

Utilizzare `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. Per impostazione predefinita pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 e angle3 = 360. Angle1 e angle2 sono il minimo e il massimo verticale della sfera, angolo3 è il diametro della sfera.


```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, App.Vector(0, 0, 0), App.Vector(0, 0, 1), -90, 90, 180)
```


{{Top}}



### Creare un cilindro 

Utilizzare `makeCylinder(radius, height, [pnt, dir, angle])`. Per impostazione predefinita pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) e angle = 360.


```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
```


{{Top}}



### Creare un cono 

Utilizzare `makeCone(raggio1, raggio2, altezza, [pnt, dir, angolo])`. Per impostazione predefinita pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) e angle = 360.


```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, App.Vector(20, 0, 0), App.Vector(0, 0, 1), 180)
```


{{Top}}



## Modificare le forme 

Esistono diversi modi per modificare le forme. Alcuni sono semplici operazioni di trasformazione come lo spostamento o la rotazione di forme, altri sono più complessi, come l\'unione e la sottrazione di una forma da un\'altra. 

## Operazioni di trasformazione 



### Traslare una forma 

La traslazione è l\'atto di spostare una forma da un luogo all\'altro. Qualsiasi forma (bordo, faccia, cubo, ecc\...) può essere traslata allo stesso modo:


```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(App.Vector(2, 0, 0))
```

Questo sposterà la forma \"myShape\" di 2 unità nella direzione dell\'asse x. 

### Ruotare una forma 

Per ruotare una forma, è necessario specificare il centro, l\'asse e l\'angolo di rotazione:


```python
myShape.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 180)
```

Il codice precedente ruota la forma di 180 gradi attorno all\'asse z. 

### Trasformazioni matriciali 

Una matrice è un modo molto conveniente per memorizzare le trasformazioni nel mondo 3D. In un\'unica matrice è possibile impostare valori di traslazione, rotazione e ridimensionamento da applicare a un oggetto. Per esempio:


```python
myMat = App.Matrix()
myMat.move(App.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
```

Nota. Le matrici di FreeCAD lavorano in radianti. Inoltre, quasi tutte le operazioni di matrici che accettano un vettore possono anche accettare tre numeri, quindi le seguenti due linee fanno la stessa cosa:


```python
myMat.move(2, 0, 0)
myMat.move(App.Vector(2, 0, 0))
```

Una volta impostata la nostra matrice, possiamo applicarla alla nostra forma. FreeCAD fornisce due metodi per farlo: `transformShape()` e `transformGeometry()`. La differenza è che con il primo, sei sicuro che non si verificheranno deformazioni (vedi [Ridimensionare una forma](#Ridimensionare_una_forma.md) di seguito). Possiamo applicare la nostra trasformazione in questo modo:


```python
myShape.transformShape(myMat)
```

oppure


```python
myShape.transformGeometry(myMat)
```


{{Top}}



### Ridimensionare una forma 

Scalare (ridimensionare) una forma è una delle operazioni più pericolose perché, a differenza della traslazione o della rotazione, il ridimensionamento non uniforme (con valori diversi per gli assi x, y, z) può modificare la struttura della forma. Ad esempio, la scalatura di un cerchio con un valore in orizzontale diverso da quello in verticale lo trasformerà in un ellisse, forma che matematicamente si comporta in modo molto diverso. Per il ridimensionamento, non possiamo usare `transformShape()`, ma dobbiamo usare `transformGeometry()`:


```python
myMat = App.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```


{{Top}}



## Operazioni Booleane 



### Sottrazione

La sottrazione di una forma da un\'altra è chiamata \"cut\" in FreeCAD e viene eseguita in questo modo:


```python
cylinder = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
sphere = Part.makeSphere(5, App.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```


{{Top}}



### Intersezione

Allo stesso modo, l\'intersezione tra le due forme è chiamato \"common\" e viene eseguita così:


```python
cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```


{{Top}}



### Unione

L\'unione è chiamata \"fuse\" e funziona allo stesso modo:


```python
cylinder1 = Part.makeCylinder(3, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, App.Vector(5, 0, -5), App.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```


{{Top}}



### Sezione

Una \"section\" è l\'intersezione tra una forma solida e una forma piana. Restituirà una curva di intersezione, una curva composta composta da bordi.


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



### Estrusione

Estrusione è l\'atto di \"spingere\" una forma piatta in una certa direzione per produrre un corpo solido. Ad esempio, si pensi di \"spingere\" un cerchio e di produrre un tubo:


```python
circle = Part.makeCircle(10)
tube = circle.extrude(App.Vector(0, 0, 2))
```

Se il cerchio è vuoto (sola circonferenza), si ottiene un tubo (cavo). Se il cerchio è in realtà un disco, con una faccia piena, si ottiene un cilindro solido:


```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(App.Vector(0, 0, 2))
```


{{Top}}



## Esplorare le forme 

Si può facilmente esplorare la struttura dei dati topologici:


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

Digitando le righe sopra nell\'interprete Python, si otterrà una buona comprensione della struttura degli oggetti Part. Qui, il comando `makeBox()` crea una forma solida. Questo solido, come tutti i solidi Part, contiene delle facce. Le facce contengono sempre delle linee (polilinee), che sono lieste di bordi, che delimitano la faccia. Ogni faccia ha almeno un contorno chiuso (ne può avere più di uno se la faccia presenta dei fori). Nel contorno, possiamo guardare a ciascun bordo separatamente, e all\'interno di ogni bordo, possiamo vedere i vertici. I bordi dritti hanno solo due vertici, ovviamente.

Digitando le righe di cui sopra nell\'interprete Python, si otterrà una buona descrizione della struttura degli oggetti Parte. Qui, il nostro comando makeBox() crea una forma solida. Questo solido, come tutti i solidi Parte, contiene delle facce. Le facce contengono sempre delle linee (polilinee), che sono liste di bordi che delimitano la faccia. Ciascuna faccia ha almeno un contorno chiuso (ne può avere più di uno se la faccia presenta dei fori). Nel contorno, possiamo guardare a ciascun bordo separatamente, e all\'interno di ogni bordo, possiamo vedere i vertici. Ovviamente, i bordi diritti hanno solo due vertici. 

### Analizzare i bordi 

Nel caso di un bordo, che è una curva arbitraria, è molto probabile che si voglia fare una discretizzazione. In FreeCAD i bordi sono parametrizzati in base alla loro lunghezza. Ciò significa che si può percorrere un bordo/curva in base alla sua lunghezza:


```python
import Part
box = Part.makeBox(100, 100, 100)
anEdge = box.Edges[0]
print(anEdge.Length)
```

Ora è possibile accedere a molte proprietà del bordo usando la lunghezza come posizione. Ciò significa, che se il bordo è lungo 100 mm, la posizione iniziale è 0 e la posizione finale 100.


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



### Utilizzare una selezione 

Qui ora vediamo come possiamo usare una selezione che l\'utente ha fatto nel visualizzatore. Prima di tutto creiamo una scatola e la mostriamo nel visualizzatore.


```python
import Part
Part.show(Part.makeBox(100, 100, 100))
Gui.SendMsgToActiveView("ViewFit")
```

Ora selezioniamo alcune facce o bordi. Con questo script è possibile iterare sopra tutti gli oggetti selezionati e sui relativi elementi secondari:


```python
for o in Gui.Selection.getSelectionEx():
    print(o.ObjectName)
    for s in o.SubElementNames:
        print("name: ", s)
        for s in o.SubObjects:
            print("object: ", s)
```

Selezionate alcuni bordi e questo script calcolerà la lunghezza:


```python
length = 0.0
for o in Gui.Selection.getSelectionEx():
    for s in o.SubObjects:
        length += s.Length

print("Length of the selected edges: ", length)
```


{{Top}}



## Esempio completo: La bottiglia OCC 

Un esempio tipico si trova nella pagina [OpenCasCade Technology Tutorial](http://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html#sec1) che spiega come costruire una bottiglia. Questo è un buon esercizio anche per FreeCAD. In effetti, se si segue il nostro esempio qui sotto e la pagina di OCC contemporaneamente, si capisce bene come sono implementate le strutture di OCC in FreeCAD. Lo script completo è anche incluso nell\'installazione di FreeCAD (all\'interno della cartella Mod/Part) e può essere chiamato dall\'interprete python digitando:


```python
import Part
import MakeBottle
bottle = MakeBottle.makeBottle()
Part.show(bottle)
```


{{Top}}



### Lo script 

Ai fini di questo tutorial considereremo una versione ridotta dello script. In questa versione la bottiglia non sarà svuotata e il collo della bottiglia non sarà filettato.


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



### Spiegazione dettagliata 


```python
import FreeCAD as App
import Part, math
```

Ovviamente, avremo bisogno dei moduli `FreeCAD` e `Part`.


```python
def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=App.Vector(-myWidth / 2., 0, 0)
    aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=App.Vector(0, -myThickness / 2., 0)
    aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=App.Vector(myWidth / 2., 0, 0)
```

Qui definiamo la nostra funzione `makeBottleTut`. Questa funzione può essere chiamata senza argomenti, come abbiamo fatto in precedenza, nel qual caso si utilizzano i valori di default per la larghezza, l\'altezza e lo spessore. Poi, si definisce un paio di punti che verranno utilizzati per costruire il nostro profilo base.


```python
    ...
    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)
```

Qui definiamo la geometria: un arco, creato da tre punti, e due segmenti di linea, creati da due punti.


```python
    ...
    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
```

Ricordate la differenza tra geometria e forme? Qui costruiremo forme partendo dalla nostra geometria di costruzione. Prima costruiremo tre bordi (i bordi possono essere dritti o curvi), poi costruiremo un contorno con quei tre bordi.


```python
    ...
    aTrsf=App.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])
```

Prima abbiamo costruito solo metà profilo. È più facile che costruire tutto l\'intero profilo nello stesso modo, successivamente possiamo semplicemente rispecchiare quello che abbiamo costruito, e poi unire le due parti. Per prima cosa è necessario creare una matrice. Una matrice è un modo molto comune per applicare trasformazioni agli oggetti nel mondo 3D, in quanto essa può contenere in un\'unica struttura tutte le trasformazioni di base che gli oggetti 3D possono subire (spostamento, rotazione e scalatura). Dopo aver creato la matrice, la specchiamo e creiamo una copia del nostro contorno applicando ad esso quella matrice di trasformazione. Ora abbiamo due contorni, e con essi possiamo produrre un terzo profilo, dal momento che i contorni sono in realtà liste di bordi.


```python
    ...
    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=App.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
```

Ora che abbiamo un contorno chiuso, esso può essere trasformato in una faccia. Una volta che abbiamo una faccia, possiamo estruderla. In questo modo, abbiamo effettivamente creato un solido. Poi si applica un piccolo arrotondamento al nostro oggetto, perché vogliamo ottenere una forma graziosa, non è vero?


```python
    ...
    neckLocation=App.Vector(0, 0, myHeight)
    neckNormal=App.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
```

A questo punto, il corpo della nostra bottiglia è creato, ma abbiamo ancora bisogno di creare un collo. Così facciamo un nuovo solido, con un cilindro.


```python
    ...
    myBody = myBody.fuse(myNeck)
```

L\'operazione di fusione è molto potente. Si prenderà cura di incollare ciò che deve essere incollato e di rimuovere le parti che devono essere rimosse.


```python
    ...
    return myBody
```

Poi, otteniamo il nostro solido Parte come risultato della nostra funzione.


```python
el = makeBottleTut()
Part.show(el)
```

Infine, chiamiamo la funzione per creare effettivamente la parte, e quindi renderla visibile. 

## Cubo forato 

Ecco un esempio completo della costruzione di una scatola perforata.

La costruzione è fatta lato per lato. Quando il cubo è finito, viene scavato un foro con un cilindro che l\'attraversa.


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



## Caricare e salvare 

Ci sono diversi modi per salvare il tuo lavoro. Ovviamente puoi salvare il tuo documento FreeCAD, ma puoi anche salvare oggetti [Part](Part_Workbench.md) direttamente in formati CAD comuni, come BREP, IGS, STEP e STL.

Salvare una forma in un file è facile. Per tutti gli oggetti di forma sono disponibili i metodi `exportBrep()`, `exportIges()`, `exportStep()` and `exportStl()`. Così, facendo:


```python
import Part
s = Part.makeBox(10, 10, 10)
s.exportStep("test.stp")
```

salviamo il nostro box in un file STEP. Per caricare un file BREP, IGES o STEP basta fare:


```python
import Part
s = Part.Shape()
s.read("test.stp")
```

Per convertire un file STEP in un file IGS fare:


```python
 import Part
 s = Part.Shape()
 s.read("file.stp")       # incoming file igs, stp, stl, brep
 s.exportIges("file.igs") # outbound file igs
```


{{Top}}


{{docnav/it
|[Script di Part](Part_scripting/it.md)
|[Oggetti creati da script](Scripted_objects/it.md)
}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Topological data scripting/it
