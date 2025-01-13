# Manual:Creating and manipulating geometry/it
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

Nei capitoli precedenti, abbiamo imparato a conoscere i diversi ambienti di FreeCAD, e come ciascuno di essi implementa i suoi propri strumenti e tipi di geometria. Gli stessi concetti si applicano quando si lavora con il codice Python.


</div>


<div class="mw-translate-fuzzy">

Abbiamo anche visto che la grande maggioranza degli ambienti di FreeCAD dipendono da uno fondamentale: l\'ambiente [Part](Part_Workbench/it.md). Infatti, molti altri ambienti di lavoro, come ad esempio [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md), fanno esattamente quello che faremo in questo capitolo: usano del codice Python per creare e manipolare della geometria Part.


</div>


<div class="mw-translate-fuzzy">

Quindi la prima cosa da fare per lavorare con la geometria Part, è di fare l\'equivalente in Python passando all\'ambiente Parte: importare il modulo Parte:


</div>


```python
import Part 
```

import Part


<div class="mw-translate-fuzzy">

Dedicare un minuto per esplorare il contenuto del modulo parte, digitando Part. e navigare attraverso i diversi metodi disponibili. Il modulo Parte offre diversi funzioni di convenienza, come makeBox, makeCircle, ecc \... che costruiscono immediatamente un oggetto. Provare questo, come esempio:


</div>


```python
Part.makeBox(3,5,7) 
```


<div class="mw-translate-fuzzy">

Quando si preme Invio dopo aver digitato la linea precedente, nella vista 3D non appare nulla, ma nella console di Python viene stampato qualcosa di simile:


</div>


```python
<Solid object at 0x5f43600> 
```


<div class="mw-translate-fuzzy">

Questo è dove avviene un concetto importante. Quello che abbiamo creato qui è una forma parte, una Part Shape. Non si tratta ancora di un document object di FreeCAD. In FreeCAD, gli oggetti e loro geometria sono indipendenti. Pensiamo a un document object di FreeCAD come un contenitore, destinato a ospitare una forma. Gli oggetti parametrici hanno anche delle proprietà, come lunghezza e larghezza, e la loro forma viene **ricalcolata** al-volo, ogni volta che cambia una delle proprietà. Quì abbiamo calcolato una forma manualmente.


</div>


<div class="mw-translate-fuzzy">

Ora possiamo creare facilmente un \"generico\" document object nel documento corrente (assicuratevi di avere almeno un nuovo documento aperto), e assegnargli la forma box che abbiamo appena creato:


</div>

boxShape = Part.makeBox(3,5,7)

myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()


<div class="mw-translate-fuzzy">

Notare come abbiamo gestito myObj.Shape, vedere che abbiamo fatto esattamente come abbiamo fatto nel capitolo precedente, quando abbiamo cambiato altre proprietà di un oggetto, come ad esempio box.Height = 5. Infatti, **Shape** è anche una proprietà, proprio come **Height**. Solo che prende una Part Shape, non un numero. Nel prossimo capitolo daremo uno sguardo più approfondito su come sono costruiti tali oggetti parametrici.


</div>

We can now easily create a \"generic\" document object in the current document (make sure you have at least one new document open), and give it a box shape like the one we just made:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Here is a breakdown of the previous commands:

-   **boxShape = Part.makeBox(3,5,7)**: Creates a 3D box with dimensions 3x5x7 (length, width, and height) and stores it as a Part Shape in the variable boxShape. This shape exists only in memory and is not yet part of the FreeCAD document.

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::Feature\", \"MyNewBox\")**: Adds a new Part::Feature object named \"MyNewBox\" to the active FreeCAD document and assigns it to the variable myObj. The new object will appear in the FreeCAD document tree.

-   **myObj.Shape = boxShape**: Links the boxShape geometry to the Shape property of myObj, integrating the geometry into the FreeCAD document.

-   **FreeCAD.ActiveDocument.recompute()**: Updates the document to reflect the changes, ensuring that the new object and its geometry appear in the graphical interface.

print(boxShape.Vertexes)

print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)


<div class="mw-translate-fuzzy">

Per esempio, troviamo l\'area di ogni faccia della nostra forma box: (Assicuratevi di rientrare la seconda riga, come appare sotto. Premete Invio due volte dopo l\'ultima riga per eseguire il comando Python).


</div>

-   **Vertexes**: Points in 3D space that define the corners or endpoints of geometry.
-   **Edges**: Straight or curved lines connecting two vertexes.
-   **Wires**: Closed or open loops formed by one or more connected edges.
-   **Faces**: Surfaces enclosed by one or more wires.
-   **Shells**: Groups of connected faces, forming a continuous surface.
-   **Solids**: 3D volumes enclosed by one or more shells.

for f in boxShape.Faces:

  print(f.Area)


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```


<div class="mw-translate-fuzzy">

Oppure, il punto iniziale e il punto finale di ogni lato:


</div>


```python
for f in boxShape.Faces:
   print(f.Area)
```

for e in boxShape.Edges:

  print("New edge")
  print("Start point:")
  print(e.Vertexes[0].Point)
  print("End point:")
  print(e.Vertexes[1].Point)


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```


<div class="mw-translate-fuzzy">

Come si vede, se il nostro boxShape ha un attributo \"Vertexes\", ogni Bordo del boxShape ha anche un attributo \"Vertexes\". Come ci si può aspettare, il boxShape ha 8 vertici, mentre il Bordo ne ha solo 2, che sono entrambi parte della lista degli 8.


</div>

Possiamo sempre controllare il tipo di una forma:


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

print(boxShape.ShapeType)

print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)

-   **print(boxShape.Faces\[0\].ShapeType)**: Accesses the first face in the **Faces** list of **boxShape** (index 0) and prints its shape type. For a box, each face is a flat surface, so the output will be \"Face\".

-   **print(boxShape.Vertexes\[2\].ShapeType)**: Accesses the third vertex in the **Vertexes** list of **boxShape** (index 2) and prints its shape type. Since this is a specific point in 3D space, the output will be \"Vertex\".


<div class="mw-translate-fuzzy">

Quindi, per riassumere l\'intero schema di una Part Shapes: Tutto comincia con i Vertici. Con uno o due vertici, si forma un bordo (i cerchi completi hanno un solo vertice). Con uno o più bordi, si forma un contorno, un Wire. Con uno o più contorni chiusi, si forma una faccia (i bordi aggiuntivi diventano \"buchi\" in una faccia). Con una o più facce, si forma un Guscio, un Shell. Quando un Shell è completamente chiusa (stagno), è possibile formare da esso un solido. E, infine, è possibile unire qualsiasi numero di forme di qualsiasi tipo, e produrre un Compoud, un Composto.


</div>

Ora proviamo a creare da zero forme complesse, con la costruzione di tutte le loro componenti una per una. Per esempio, cerchiamo di creare un volume come questo:

![](images/Exercise_python_03.jpg )

Inizieremo con la creazione di una forma planare come questa:

![](images/Wire.png )

In primo luogo, creiamo i quattro punti di base:


```python
V1 = FreeCAD.Vector(0,10,0)
V2 = FreeCAD.Vector(30,10,0)
V3 = FreeCAD.Vector(30,-10,0)
V4 = FreeCAD.Vector(0,-10,0)
```

Poi possiamo creare i due segmenti lineari:

![](images/Line.png )


```python
L1 = Part.LineSegment(V1,V2)
L2 = Part.LineSegment(V4,V3)
```


<div class="mw-translate-fuzzy">

Notare che non è necessario creare dei vertici. Si può creare subito una Part.LineSegments dai vettori di FreeCAD. Questo è perché qui non abbiamo ancora creato un Edge. Una Part.LineSegment (così come una Part.Circle, Part.Arc, Part.Ellipse o Part.BSpline) non crea un bordo, ma piuttosto una geometria di base su cui viene creato un bordo. Gli Edges sono sempre costituiti su una tale geometria di base, che memorizza il suo attributo Curve. Quindi, se si dispone di un bordo, facendo:


</div>


```python
print(Edge.Curve) 
```


<div class="mw-translate-fuzzy">

mostra di che tipo di bordo si tratta, cioè, se si basa su una linea, un arco, ecc \... Ma torniamo all\'esercizio, e creiamo i segmenti di arco. Per questo, serve un terzo punto, in modo da poter utilizzare il comodo Part.Arc, che prende 3 punti:


</div>

![](images/Circel.png )


```python
VC1 = FreeCAD.Vector(-10,0,0)
C1 = Part.Arc(V1,VC1,V4)
VC2 = FreeCAD.Vector(40,0,0)
C2 = Part.Arc(V2,VC2,V3)
```

Ora abbiamo 2 linee (L1 e L2) e 2 archi (C1 e C2). Bisogna trasformarli in bordi:


```python
E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)
```


<div class="mw-translate-fuzzy">

In alternativa, le geometrie di base hanno anche una funzione toShape() che fa esattamente la stessa cosa:


</div>


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```


<div class="mw-translate-fuzzy">

Ottenuta una serie di bordi, si può formare un contorno, dandogli un elenco di bordi. Bisogna stare attenti all\'ordine. Inoltre, notare le parentesi.


</div>


```python
W = Part.Wire([E1,E4,E2,E3]) 
```


<div class="mw-translate-fuzzy">

E siamo in grado di verificare se il nostro contorno è stato compreso e chiuso correttamente:


</div>


```python
print( W.isClosed() ) 
```


<div class="mw-translate-fuzzy">

Che stampa \"True\" o \"False\". Per creare una faccia, servono dei contorni chiusi, quindi è sempre una buona idea controllare questo prima di creare la faccia. Ora possiamo creare una faccia, dandogli un unico Wire (o una lista di Wire se vogliamo dei fori):


</div>


```python
F = Part.Face(W) 
```

Poi la estrudiamo:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```


<div class="mw-translate-fuzzy">

Si noti che P è già un solido:


</div>


```python
print(P.ShapeType) 
```


<div class="mw-translate-fuzzy">

Questo perché quando si estrude una sola faccia, si ottiene sempre una solido. Non è così se, ad esempio, si estrude invece un contorno


</div>


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
```

Che ovviamente ci dà un guscio vuoto, con le facce superiore e inferiore mancanti.

Ora che abbiamo la forma finale, siamo ansiosi di vederla sullo schermo! Quindi creiamo un oggetto generico, a cui attribuire il nostro nuovo Solid:


```python
myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","My_Strange_Solid")
myObj2.Shape = P
FreeCAD.ActiveDocument.recompute()
```

In alternativa, il modulo Parte fornisce anche una scorciatoia che esegue più velocemente l\'operazione descritta sopra (ma non è possibile scegliere il nome dell\'oggetto):


```python
Part.show(P) 
```

Tutto quanto detto sopra, e molto altro ancora, è spiegato in dettaglio nella pagina [Script di Parti](Topological_data_scripting/it.md), insieme agli esempi.

**Approfondimenti**:

-   [L\'ambiente Parte](Part_Workbench/it.md)
-   [Script di Parti](Topological_data_scripting/it.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/it
