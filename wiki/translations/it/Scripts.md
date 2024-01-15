---
 TutorialInfo:t
   Topic: Scripting
   Level: Base
   Time: 
   Author: onekk Carlo
   FCVersion: 0.19
   Files: 
---

# Scripts/it










## Introduzione

Per Scripting intendiamo la creazione di oggetti topologici mediante l\'uso dell\'interprete Python interno di FreeCAD. FreeCAD può essere usato come \"ottimo\" sostituto di OpenSCAD, principalmente perché possiede un vero interprete Python, questo vuol dire che ha un intero linguaggio di programmazione \"a bordo\", quasi tutto quello che si può realizzare con l\'interfaccia grafica è possibile realizzarlo anche attraverso uno script Python.

Purtroppo le informazioni che riguardano lo scripting nella documentazione di FreeCAD, e anche in questo wiki sono disperse e mancano di una uniformità di \"scrittura\" e molte di esse sono spiegate in maniera troppo tecnica.




<div class="mw-translate-fuzzy">

## Primo assaggio 


</div>

Il primo ostacolo ad un semplice approccio allo scripting deriva dal fatto che non esiste un modo per accedere direttamente all\'editor Python interno a FreeCAD, con un comando di menù od un\'icona nella barra degli strumenti, sapendo però che FreeCAD apre un file con estensione `.py` nell\'editor Python interno, il trucco più semplice è quello di creare usando il proprio editor di testo preferito, un file e poi aprirlo in FreeCAD con **File → Apri**.

Per fare le cose con un minimo di stile, il file deve essere scritto con un certo ordine. L\'editor di FreeCAD possiede una buona \"Evidenziazione di Sintassi\" che manca a molti editor come Windows Notepad o altri editor di Linux di base, per cominciare basta scrivere queste poche righe:


```python
"""filename.py

   A short description of what the script does

"""
```


<div class="mw-translate-fuzzy">

Salvatele con un nome significativo e con estensione `.py` e caricate il file ottenuto in FreeCAD, con il comando **File → Apri**.


</div>

Un esempio minimale che contiene tutto quanto necessario per uno script è mostrato in questa porzione di codice, che potete usare come modello per quasi ogni vostro futuro script:


```python
"""filename.py

   First FreeCAD Script

"""

import FreeCAD
from FreeCAD import Placement, Rotation, Vector

DOC = FreeCAD.activeDocument()
DOC_NAME = "Wiki_Example"

# Helpers methods

def clear_doc():
    """Clear activeDocument deleting all the objects."""
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)

def setview():
    """Rearrange View."""
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()

if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

ROT0 = Rotation(0, 0, 0)
VEC0 = Vector(0, 0, 0)
```

Nel codice qui sopra sono presenti alcuni trucchi:


<div class="mw-translate-fuzzy">

-    `import FreeCAD`Questa linea serve per importare FreeCAD all\'interno dell\'interprete Python, può sembrare superfluo, ma non lo è.

-    `from FreeCAD import Base, Vector`Base e Vector sono molto usati negli script in FreeCAD, importando questi due metodi in questo modo vi evita di scrivere `FreeCAD.Vector` oppure `FreeCAD.Base` al posto di `Base` oppure `Vector`, vi risparmiano quindi molto lavoro di battitura e rendono il codice più compatto.


</div>

Cominciamo con un piccolo script che fa un piccolo lavoro, ma mostra la potenza di questo approccio.


```python
# Script methods

def my_box(name, len, wid, hei):
    """Create a box."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    DOC.recompute()

    return obj_b

# objects definition

obj = my_box("test_cube", 5, 5, 5)

setview()
```


<div class="mw-translate-fuzzy">

Mettetelo dopo il codice di esempio e premete la freccia verde della **Barra di strumenti Macro**


</div>


<div class="mw-translate-fuzzy">

Accadranno alcune magie, si apre un nuovo documento chiamato \"Pippo\" e si visualizza un [Cubo](Part_Box/it.md) nella Vista 3D, che dovrebbe assomigliare all\'immagine qui sotto.


</div>

![Test cube](images/Cubo.png )




<div class="mw-translate-fuzzy">

## Qualcosa di più\... 


</div>


<div class="mw-translate-fuzzy">

Niente di eccezionale? Vero, ma da qualcosa dobbiamo pure incominciare, possiamo fare la stessa cosa con un [Cilindro](Part_Cylinder/it.md), aggiungete queste linee dopo il metodo `cubo()` e prima della riga `# objects definition`.


</div>


```python
def my_cyl(name, ang, rad, hei):
    """Create a Cylinder."""
    obj = DOC.addObject("Part::Cylinder", name)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = hei

    DOC.recompute()

    return obj
```

Anche qui nulla di eccezionale. Notiamo alcune cose nella costruzione del codice:


<div class="mw-translate-fuzzy">

-   L\'assenza degli usuali riferimenti ad `App.`, presenti in molta documentazione che parla di scripting, è pienamente voluto, in futuro si potrà riusare il codice per accedere a FreeCAD come un modula da un interprete Python esterno, la cosa non è proprio facilissima da AppImage, ma con qualche accortezza è possibile. Di più facendo riferimento al motto di Python \"esplicito è meglio che implicito\", `App.` non indica molto bene da dove arrivano i metodi che si usano.
-   Notate l\'uso della \"costante\" DOC assegnata al documento attivo in `DOC` = `FreeCAD.activeDocument()`; `activeDocument()` ovviamente non è una \"costante\", ma dal punto di vista semantico è il nostro \"documento attivo\", da qui l\'uso della convenzione di Pyhton del nome \"TUTTO MAIUSCOLO\" per le \"costanti\", senza considerare che `DOC` è molto pià corto che `FreeCAD.activeDocument()`.
-   Ogni metodo ritorna un geometria, questo diventerà importante fra poco.
-   La geometria viene creata senza definire una la proprietà `Placement`, questo è voluto perché se utilizzando geometrie semplici per creare geometrie più complesse, la gestione della proprietà `Placement` è una cosa \"delicata\".


</div>

Ora cosa dobbiamo fare con questi oggetti?


<div class="mw-translate-fuzzy">

Introduciamo ora le operazioni booleane. Un esempio per cominciare, mettendo queste linee dopo `base_cyl(...`, si crea un metodo che esegue una operazione di \"Fusione\" conosciuta anche come \"Unione\":


</div>


```python
def fuse_obj(name, obj_0, obj_1):
    """Fuse two objects."""
    obj = DOC.addObject("Part::Fuse", name)
    obj.Base = obj_0
    obj.Tool = obj_1
    obj.Refine = True
    DOC.recompute()

    return obj
```

Anche qui nulla di eccezionale, notate comunque l\'uniformità nel metodo di scrittura; Questo approccio è molto più lineare di quello usato in molti altri Tutorial, aiuta molto ad incrementare la leggibilità del codice e anche quando si vuole fare copia e incolla

Usiamo ora queste geometrie, cancellate le linee di codice dopo `# objects definition` e inserite queste linee:


```python
# objects definition

obj = my_box("test_cube", 5, 5, 5)

obj1 = my_cyl("test_cyl", 360, 2, 10)

fuse_obj("Fusion", obj, obj1)

setview()
```


<div class="mw-translate-fuzzy">

Lanciate lo script con la freccia verde e vedrete nella vista 3D, qualcosa che assomiglia all\'immagine qui sotto:


</div>

![Cube and cylinder](images/Cucil.png )



## Posizionamento

Il concetto di Posizionamento è relativamente complesso, potete vedere [Tutorial Aeroplano](Aeroplane/it.md) per una spiegazione più approfondita.

In genere abbiamo bisogno di posizionare una geometria rispetto ad un\'altra geometria, cosa abbastanza frequente quando si creano geometrie complesse, il modo più comodo è quello di usare la proprietà `Placement` della geometria.

FreeCAD offre un\'ampia scelta di modi con cui specificare questa proprietà, molto dipende anche dalle conoscenze di fondo dell\'utente, quella più facile da comprendere è quella spiegata nel Tutorial citato, usa una particolare definizione della porzione `Rotation` all\'interno della definizione di `Placement`.


```python
FreeCAD.Placement(Vector(0, 0, 0), FreeCAD.Rotation(10, 20, 30), Vector(0, 0, 0))
```


<div class="mw-translate-fuzzy">

Comunque al di sopra di ogni ulteriore considerazione, una cosa è cruciale, il concetto di \"punto di riferimento\" della geometria. In altri termini, il punto dal quale l\'oggetto viene costruito da parte di FreeCAD, riportiamo in questa tabella, copiata direttamente da [Placement](Placement/it.md):


</div>


<div class="mw-translate-fuzzy">

  Oggetto                              Punto di riferimento
   
  Part.Box                             vertice sinistro (minimo x), frontale (minimo y), in basso (minimo z)
  Part.Sphere                          centro della sfera (centro del suo contenitore cubico)
  Part.Cylinder                        centro della faccia di base
  Part.Cone                            centro della faccia di base (o superiore se il raggio della faccia di base vale 0)
  Part.Torus                           centro del toro
  Caratteristiche derivate ​​da Sketch   la caratteristica eredita la posizione dello schizzo sottostante. Lo schizzo inizia sempre con Position = (0,0,0).


</div>

Questa informazione va tenuta ben presente specie quando si applica una rotazione.


<div class="mw-translate-fuzzy">

Qulche esempio ci aiuterà a capire meglio il concetto, cancellate le linee di codice dopo il metodo `base_cyl` ed inserite la porzione di codice qui sotto:


</div>


```python
def my_sphere(name, rad):
    """Create a Sphere."""
    obj = DOC.addObject("Part::Sphere", name)
    obj.Radius = rad

    DOC.recompute()

    return obj

def my_box2(name, len, wid, hei, cent=False, off_z=0):
    """Create a box with an optional z offset."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    if cent is True:
        pos = Vector(len * -0.5, wid * -0.5, off_z)
    else:
        pos = Vector(0, 0, off_z)

    obj_b.Placement = Placement(pos, ROT0, VEC0)

    DOC.recompute()

    return obj_b

def mfuse_obj(name, objs):
    """Fuse multiple objects."""
    obj = DOC.addObject("Part::MultiFuse", name)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj

def airplane():
    """Create an airplane shaped solid."""
    fuselage_length = 30
    fuselage_diameter = 5
    wing_span = fuselage_length * 1.75
    wing_width = 7.5
    wing_thickness = 1.5
    tail_height = fuselage_diameter * 3.0
    tail_position = fuselage_length * 0.70
    tail_offset = tail_position - (wing_width * 0.5)

    obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)

    obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)

    obj3 = my_sphere("nose", fuselage_diameter)
    obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)

    obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
    obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("airplane", objs)
    obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))

    DOC.recompute()

    return obj

# objects definition

airplane()

setview()

```

Illustriamo meglio alcuni punti del codice:


<div class="mw-translate-fuzzy">

-   Abbiamo definito un metodo per creare una sfera, abbiamo usado la definizione più semplice, definendo solo il raggio.
-   Abbiamo introdotto una seconda forma per l**\'Unione** o la **Fusione** come dir si voglia, quella che permette di fondere più oggetti, niente di speciale rispetto a **Part::Fuse** viene definita come **Part:Multifuse**, notate che possiede solo una proprietà `Shapes` dove abbiamo messo una **tupla** contenente gli oggetti da fondere, avremmo potuto se necessario passare una **lista**.
-   Abbiamo definito una geometria complessa **aeroplano**, e lo abbiamo fatto in modo **\"parametrico\"**, cioè definendo alcuni parametri e calcolando in modo automatico, attraverso la definizione di alcune formule, molti dei valori che definiscono la geometria finale.
-   Abbiamo definito qualche proprietà `Placement` per i vari componenti base della geometria e abbiamo definito la parte `Rotation` della proprietà `Placement` usando la scrittura *Yaw-Pitch-Roll*. Notate l\'ultimo componente `Vector(0,0, pos_ali)`, questo definisce il \"centro di rotazione\" della geometria finale.


</div>

++++
| ![Airplane example](images/Aereo.png ) | ![Airplane rotated](images/Aereo2.png ) | ![Placement property](images/Aereo-prop.png ) |
++++


<div class="mw-translate-fuzzy">

Potete facilmente notare che l\'aereo ruota attorno al suo \"baricentro\" detto anche \"centro di gravità\", che ho fissato nel centro delle ali, una posizione abbastanza \"naturale\", potete comunque piazzarlo dove più vi aggrada o vi serve.


</div>


<div class="mw-translate-fuzzy">

Il primo `Vector(0,0,0)` è il vettore di Traslazione (o di posizionamento), che qui non abbiamo usato, però se sostituite la riga `aeroplano()` con le linee seguenti:


</div>


```python
obj_f = airplane()

print(obj_F.Placement)
```

Potete leggere nella finestra Report questo testo:


```python
Placement [Pos=(0, -21, 21), Yaw-Pitch-Roll=(0, 0, -90)]
```

Cosa è successo?


<div class="mw-translate-fuzzy">

FreeCAD ha \"tradotto\" il posizionamento passato con `Vector(0, 0, 0), FreeCAD.Rotation(0, 0, -90), Vector(0, 0, pos_ali)`, che specificava tre componenti **Translazione**, **Rotazione** e *centro di rotazione**nel suo valore \"interno\" che possiede solo due componenti,**Translazione**e**Rotazione*\'.


</div>


<div class="mw-translate-fuzzy">

Potete facilmente inserire nel codice del metodo `aeroplano(...` una istruzione che stampi `pos_ali`, e vedrete che vale:


</div>


```python
tail_position = 21.0
```


<div class="mw-translate-fuzzy">

In parole povere, il *\'centro di rotazione* della geometria è posizionato a `Vector(0, 0, 21)`, ma non è mostrato attraverso l\'interfaccia grafica nella vista Dati, può essere specificato come valore nella proprietà `Placement`, ma non può essere facilmente recuperato.


</div>

Questo è il significato dell\'aggettivo \"delicato\" che ho usato precedentemente nel testo per definire la proprietà `Placement`.

This is the complete code example with a decent script docstring following [Google docstrings convention](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google):


```python
"""Sample code.

Filename:
   airplane.py

Author:
    Dormeletti Carlo (onekk)

Version:
    1.0

License:
    Creative Commons Attribution 3.0

Summary:
    This code is a sample code written for FreeCAD Wiki page.
    It create and airplane shaped solid made using standard "Part WB" built in shapes.

"""

import FreeCAD
from FreeCAD import Placement, Rotation, Vector

DOC = FreeCAD.activeDocument()
DOC_NAME = "Wiki_Example"

# Helpers methods

def clear_doc():
    """Clear activeDocument deleting all the objects."""
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)

def setview():
    """Rearrange View."""
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()

if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

ROT0 = Rotation(0, 0, 0)
VEC0 = Vector(0, 0, 0)

# Script methods

def my_cyl(name, ang, rad, hei):
    """Create a Cylinder."""
    obj = DOC.addObject("Part::Cylinder", name)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = hei

    DOC.recompute()

    return obj

def my_sphere(name, rad):
    """Create a Sphere."""
    obj = DOC.addObject("Part::Sphere", name)
    obj.Radius = rad

    DOC.recompute()

    return obj

def my_box2(name, len, wid, hei, cent=False, off_z=0):
    """Create a box with an optional z offset."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    if cent is True:
        pos = Vector(len * -0.5, wid * -0.5, off_z)
    else:
        pos = Vector(0, 0, off_z)

    obj_b.Placement = Placement(pos, ROT0, VEC0)

    DOC.recompute()

    return obj_b

def mfuse_obj(name, objs):
    """Fuse multiple objects."""
    obj = DOC.addObject("Part::MultiFuse", name)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj

def airplane():
    """Create an airplane shaped solid."""
    fuselage_length = 30
    fuselage_diameter = 5
    wing_span = fuselage_length * 1.75
    wing_width = 7.5
    wing_thickness = 1.5
    tail_height = fuselage_diameter * 3.0
    tail_position = fuselage_length * 0.70
    tail_offset = tail_position - (wing_width * 0.5)

    obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)

    obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)

    obj3 = my_sphere("nose", fuselage_diameter)
    obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)

    obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
    obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("airplane", objs)
    obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))

    DOC.recompute()

    return obj

# objects definition

airplane()

setview()
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripts/it
