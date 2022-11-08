# Part scripting/it
{{TOCright}}

## Introduzione

La struttura dati principale utilizzata nel modulo Parte è il tipo di dati [BRep](https   *//it.wikipedia.org/wiki/B-Rep) da [OpenCASCADE](OpenCASCADE/it.md). Quasi tutti i contenuti e i tipi di oggetti del modulo Part sono disponibili per lo scripting con [Python](Python/it.md). Ciò include le primitive geometriche, come linee, cerchi e archi, e l\'intera gamma di forme topografiche, come vertici, bordi, fili, facce, solidi e composti. Per ciascuno di questi oggetti esistono diversi metodi di creazione e per alcuni di essi, in particolare TopoShapes, sono disponibili anche operazioni avanzate come unione/differenza/intersezione booleana. Si possono esplorare i contenuti del modulo Parte, come descritto nella pagina [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), per saperne di più.

L\'oggetto più semplice che può essere creato è [Part](Part_Feature/it.md), che ha una semplice proprietà **Placement** e le proprietà di base per definirne il colore e l\'aspetto.

Un altro oggetto semplice utilizzato negli oggetti geometrici 2D è il [Part Part2DObject](Part_Part2DObject/it.md), che è la base di [Sketcher SketchObject](Sketcher_SketchObject/it.md) e della maggior parte dei [Draft elements](Draft_Workbench.md).

### Vedere anche 

-   [Script di dati topologici](Topological_data_scripting/it.md)
-   [OpenCASCADE](OpenCASCADE/it.md)

## Script di test 

Testare la creazione di [Primitive Part](Part_Primitives/it.md) con uno script. {{Version/it|0.19}}


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Questo script si trova nella cartella d\'installazione del programma e può essere esaminato per vedere come vengono costruite le primitive di base.


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

## Esempi

### Linea

Per creare un elemento di linea, passa alla [console Python](Python_console/it.md) e inserisci   *


```python
import FreeCAD as App
import Part

doc = App.newDocument()

line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
obj = doc.addObject("Part   *   *Feature", "Line")
obj.Shape= line.toShape()

doc.recompute()
```

Esaminiamo passo dopo passo l\'esempio Python sopra   *


```python
import FreeCAD as App
import Part
doc = App.newDocument()
```

Questo carica i moduli di FreeCAD e Part e crea un nuovo documento.


```python
line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
```

La linea è in realtà un segmento di retta, quindi ha un inizio e un punto finale.


```python
obj = doc.addObject("Part   *   *Feature", "Line")
obj.Shape= line.toShape()
```

Questo aggiunge un tipo di oggetto Parte al documento e assegna la rappresentazione della forma del segmento di linea alla proprietà {{Incode|Shape}} dell\'oggetto aggiunto. È importante capire qui che usiamo una primitiva geometrica (il {{Incode|Part.LineSegment}}) per creare un TopoShape da esso (con il metodo {{Incode|toShape()}}). Solo le forme possono essere aggiunte al documento. In FreeCAD le primitive geometriche sono usate come \"strutture edilizie\" per le forme.


```python
doc.recompute()
```

Aggiorna il documento. Questo prepara anche la rappresentazione visiva del nuovo oggetto Part.

Si noti che un segmento di linea può anche essere creato specificandone l\'inizio e il punto finale direttamente nel costruttore, ad esempio {{Incode|Part.LineSegment(point1, point2)}}, oppure possiamo creare una linea predefinita e impostarne le proprietà in seguito, come abbiamo fatto qui.

È inoltre possibile creare una linea utilizzando   *


```python
import FreeCAD as App
import Part

def my_create_line(pt1, pt2, obj_name)   *
    obj = App.ActiveDocument.addObject("Part   *   *Line", obj_name)
    obj.X1 = pt1[0]
    obj.Y1 = pt1[1]
    obj.Z1 = pt1[2]

    obj.X2 = pt2[0]
    obj.Y2 = pt2[1]
    obj.Z2 = pt2[2]

    App.ActiveDocument.recompute()
    return obj

line = my_create_line((0, 0, 0), (0, 10, 0), "LineName")
```

### Cerchio

Un cerchio può essere creato in modo simile   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

circle = Part.Circle() 
circle.Radius = 10.0  
obj = doc.addObject("Part   *   *Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

oppure usando   *


```python
import FreeCAD as App
import Part

def my_create_circle(rad, obj_name)   *
    obj = App.ActiveDocument.addObject("Part   *   *Circle", obj_name)
    obj.Radius = rad

    App.ActiveDocument.recompute()
    return obj

circle = my_create_circle(5.0, "CircleName")
```

In alternativa possiamo creare un cerchio definendone il centro, l\'asse e il raggio   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

center = App.Vector(1, 2, 3)
axis = App.Vector(1, 1, 1)
radius = 10
circle = Part.Circle(center, axis, radius)
obj = doc.addObject("Part   *   *Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Oppure definendo tre punti sulla sua circonferenza   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(0, 0, 10)
circle = Part.Circle(p1, p2, p3)
obj = doc.addObject("Part   *   *Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Si noti ancora, che abbiamo usato il cerchio (primitiva geometrica) per costruire una forma. Ovviamente possiamo ancora accedere alla nostra geometria di costruzione in seguito, facendo   *


```python
shape = obj.Shape
edge = shape.Edges[0]
curve = edge.Curve
```

Qui prendiamo il {{Incode|Shape}} del nostro oggetto {{Incode|obj}} e poi la sua lista di {{Incode|Edges}}. In questo caso ci sarà un solo bordo perché abbiamo ricavato la forma da un unico cerchio. Quindi prendiamo solo il primo elemento nell\'elenco {{Incode|Edges}}, successivamente prendiamo la sua curva. Ogni bordo ha un {{Incode|Curve}}, che è la primitiva geometrica su cui si basa.

### Arco

Un arco può essere creato in questo modo   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
arc = Part.Arc(p1, p2, p3)
obj = doc.addObject("Part   *   *Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

Così si disegna un semicerchio. Il centro è a (0, 0, 0). Il raggio è 10. P1 è il punto iniziale sull\'asse +X. P2 è il punto medio sull\'asse +Y e P3 è il punto finale sull\'asse -X.

Possiamo anche creare un arco da un cerchio   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
circle = Part.Circle(p1, p2, p3)
arc = Part.ArcOfCircle(circle, 0.0, 0.7854)
obj = doc.addObject("Part   *   *Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

È necessario un cerchio, un angolo iniziale e un angolo finale in radianti.





 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Part](Part_Workbench.md) > Part scripting/it
