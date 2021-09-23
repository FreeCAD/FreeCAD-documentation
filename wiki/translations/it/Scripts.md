# Scripts/it
{{TutorialInfo/it
|Topic=Scripting
|Level=Base
|Time=
|Author=onekk Carlo
|FCVersion=0.19
|Files=
}}

## Introduzione

Per Scripting si intende l\'uso dell\'interprete Python interno di FreeCAD per generare oggetti. FreeCAD può essere usato come \"ottimo\" sostituto di OpenSCAD, perché possiede un vero e proprio interprete Python, con il pieno supporto per tutti i costrutti di un linguaggio di programmazione, quasi tutto quello che si può realizzare con l\'interfaccia grafica è possibile realizzarlo anche attraverso uno script Python.

Le informazioni sullo scripting sono però sparse nella documentazione di FreeCAD, non c\'è una uniformità di \"scritture\" e alcune cose sono spiegate in maniera complicata per chi comincia.

## Primo assaggio 

Il primo ostacolo ad un semplice approccio allo scripting deriva dal fatto che non esiste un modo per accedere direttamente all\'editor Python interno a FreeCAD, con un comando di menu od un\'icona nella barra degli strumenti, sapendo però che FreeCAD apre un file con estensione `.py` nell\'editor Python interno, il trucco più semplice è quello di creare usando il proprio editor di testo preferito, un file e poi aprirlo in FreeCAD con **File → Apri**.


<div class="mw-translate-fuzzy">

Per fare le cose con un minimo di stile, lo script deve essere scritto con un certo ordine. L\'editor di FreeCAD possiede una buona \"evidenziazione di sintassi\" che manca a molti editor come Windows Notepad o altri editor di Linux di base, per cominciare basta scrivere queste poche righe:


</div>


```python
"""script.py

   Primo script per FreeCAD

"""

```

Salvatele con un nome significativo e con estensione `.py` e caricate il file ottenuto in FreeCAD, con il comando **File → Apri**.

Un esempio minimale ma che contiene tutto quanto necessario per uno script è mostrato in questa porzione di codice, che potete usare come modello per quasi ogni vostro futuro script:


```python
"""filename.py

   Here a short but significant description of what the script do 

"""


import FreeCAD
from FreeCAD import Base, Vector
import Part
from math import pi, sin, cos

DOC = FreeCAD.activeDocument()
DOC_NAME = "Pippo"

def clear_doc():
    """
    Clear the active document deleting all the objects
    """
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)

def setview():
    """Rearrange View"""
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()

else:

    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

```

Nel codice qui sopra sono presenti alcuni trucchi:


<div class="mw-translate-fuzzy">

-    `import FreeCAD`Questa linea serve per importare FreeCAD all\'interno dell\'interprete Python, può sembrare superfluo, ma non lo è.

-    `from FreeCAD import Base, Vector`Base e Vector sono molto usati negli script in FreeCAD, importando questi due metodi in questo modo vi evita di scrivere `FreeCAD.Vector` oppure `FreeCAD.Base` al posto di `Base` oppure `Vector`, vi risparmiano quindi molto lavoro di battitura e rendono il codice più compatto.


</div>

Cominciamo con un piccolo script che fa un piccolo lavoro, ma mostra la potenza di questo approccio.


```python
def cubo(nome, lung, larg, alt):
    obj_b = DOC.addObject("Part::Box", nome)
    obj_b.Length = lung
    obj_b.Width = larg
    obj_b.Height = alt

    DOC.recompute()

    return obj_b

# objects definition

obj = cubo("test_cube", 5, 5, 5)

setview()

```

Mettetelo dopo il codice di esempio e premete la freccia verde della **Barra di strumenti Macro**

Accadranno alcune magie, si apre un nuovo documento chiamato \"Pippo\" e si visualizza un [Cubo](Part_Box/it.md) nella Vista 3D, che dovrebbe assomigliare all\'immagine qui sotto.

![Test Cube](images/Cubo.png )

## Qualcosa di più\... 

Niente di eccezionale? Vero, ma da qualcosa dobbiamo pure incominciare, possiamo fare la stessa cosa con un [Cilindro](Part_Cylinder/it.md), aggiungete queste linee dopo il metodo `cubo(` e prima della riga `# objects definition`.


```python
def base_cyl(nome, ang, rad, alt ):
    obj = DOC.addObject("Part::Cylinder", nome)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = altDOC.recompute()

    return obj   

```

Anche qui nulla di eccezionale, notiamo alcune nella costruzione del codice:


<div class="mw-translate-fuzzy">

-   L\'assenza degli usuali riferimenti ad `App.`, presenti in molta documentazione che parla di scripting, è pienamente voluto, in futuro si potrà riusare il codice per accedere a FreeCAD come un modula da un interprete Python esterno, la cosa non è proprio facilissima da AppImage, ma con qualche accortezza è possibile. Di più facendo riferimento al motto di Python \"esplicito è meglio che implicito\", `App.` non indica molto bene da dove arrivano i metodi che si usano.
-   Notate l\'uso della \"costante\" DOC assegnata al documento attivo in `DOC` = `FreeCAD.activeDocument()`; `activeDocument()` ovviamente non è una \"costante\", ma dal punto di vista semantico è il nostro \"documento attivo\", da qui l\'uso della convenzione di Pyhton del nome \"TUTTO MAIUSCOLO\" per le \"costanti\", senza considerare che `DOC` è molto pià corto che `FreeCAD.activeDocument()`.
-   ogni metodo ritorna un geometria, questo diventerà importante fra poco.
-   la geometria viene creata senza definire una la proprietà `Placement`, questo è voluto perché se utilizzando geometrie semplici per creare geometrie più complesse, la gestione della proprietà `Placement` è una cosa \"delicata\".


</div>

Ora dobbiamo pur farci qualcosa con questi oggetti,

Introduciamo ora le operazioni booleane. Un esempio per cominciare, mettendo queste linee dopo `base_cyl(...`, si crea un metodo che esegue una operazione di \"Fusione\" conosciuta anche come \"Unione\":


```python
def fuse_obj(nome, obj_0, obj_1):
    obj = DOC.addObject("Part::Fuse", nome)
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

obj = cubo("cubo_di_prova", 5, 5, 5)

obj1 = base_cyl('primo cilindro', 360,2,10)

fuse_obj("Fusione", obj, obj1)

setview()

```

Lanciate lo script con la freccia verde e vedrete nella vista 3D, qualcosa che assomiglia all\'immagine qui sotto:

![cube and cylinder](images/Cucil.png )

## Posizionamento

Il concetto di Posizionamento è relativamente complesso, potete vedere [Tutorial Aeroplano](Aeroplane/it.md) per una spiegazione più approfondita.

In genere abbiamo bisogno di posizionare una geometria rispetto ad un\'altra geometria, cosa abbastanza frequente quando si creano geometrie complesse, il modo più comodo è quello di usare la proprietà `Placement` della geometria.

FreeCAD offre un\'ampia scelta di modi con cui specificare questa proprietà, molto dipende anche dalle conoscenze di fondo dell\'utente, quella più facile da comprendere è quella spiegata nel Tutorial citato, usa una particolare definizione della porzione `Rotation` all\'interno della definizione di `Placement`.


```python 
FreeCAD.Placement(Vector(0,0,0), FreeCAD.Rotation(10,20,30), Vector(0,0,0))
```

Comunque al di sopra di ogni ulteriore considerazione, una cosa è cruciale, il concetto di \"punto di riferimento\" della geometria. In altri termini, il punto dal quale l\'oggetto viene costruito da parte di FreeCAD, riportiamo in questa tabella, copiata direttamente da [Placement](Placement/it.md):

  Oggetto                                Punto di riferimento
  -------------------------------------- --------------------------------------------------------------------------------------------------------------------
  Part.Box                               vertice sinistro (minimo x), frontale (minimo y), in basso (minimo z)
  Part.Sphere                            centro della sfera (centro del suo contenitore cubico)
  Part.Cylinder                          centro della faccia di base
  Part.Cone                              centro della faccia di base (o superiore se il raggio della faccia di base vale 0)
  Part.Torus                             centro del toro
  Caratteristiche derivate ​​da Sketch   la caratteristica eredita la posizione dello schizzo sottostante. Lo schizzo inizia sempre con Position = (0,0,0).

Questa informazione va tenuta ben presente specie quando si applica una rotazione.

Qulche esempio ci aiuterà a capire meglio il concetto, cancellate le linee di codice dopo il metodo `base_cyl` ed inserite la porzione di codice qui sotto:


```python

def sfera(nome, rad):
    obj = DOC.addObject("Part::Sphere", nome)
    obj.Radius = radDOC.recompute()

    return obj   


def mfuse_obj(nome, objs):
    obj = DOC.addObject("Part::MultiFuse", nome)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj


def aeroplano():

    lung_fus = 30
    diam_fus = 5
    ap_alare = lung_fus * 1.75
    larg_ali = 7.5
    spess_ali = 1.5   
    alt_imp = diam_fus * 3.0  
    pos_ali = (lung_fus*0.70)
    off_ali = (pos_ali - (larg_ali * 0.5))

    obj1 = base_cyl('primo cilindro', 360, diam_fus, lung_fus)

    obj2 = cubo('ali', ap_alare, spess_ali, larg_ali, True, off_ali)

    obj3 = sfera("naso", diam_fus)
    obj3.Placement = FreeCAD.Placement(Vector(0,0,lung_fus), FreeCAD.Rotation(0,0,0), Vector(0,0,0))

    obj4 = cubo('impennaggio', spess_ali, alt_imp, larg_ali, False, 0)
    obj4.Placement = FreeCAD.Placement(Vector(0,alt_imp * -1,0), FreeCAD.Rotation(0,0,0), Vector(0,0,0))

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("Forma esempio", objs)
    obj.Placement = FreeCAD.Placement(Vector(0,0,0), FreeCAD.Rotation(0,0,-90), Vector(0,0,pos_ali))

    DOC.recompute()

    return obj

# objects definition

aeroplano()

setview()

```

Illustriamo meglio alcuni punti del codice:


<div class="mw-translate-fuzzy">

-   Abbiamo definito un metodo per creare una sfera, abbiamo usado la definizione più semplice, definendo solo il raggio.
-   Abbiamo introdotto una seconda forma per l**\'Unione** o la **Fusione** come dir si voglia, quella che permette di fondere più oggetti, niente di speciale rispetto a **Part::Fuse** viene definita come **Part:Multifuse**, notate che possiede solo una proprietà `Shapes` dove abbiamo messo una **tupla** contenente gli oggetti da fondere, avremmo potuto se necessario passare una **lista**.
-   Abbiamo definito una geometria complessa **aeroplano**, e lo abbiamo fatto in modo **\"parametrico\"**, cioè definendo alcuni parametri e calcolando in modo automatico, attraverso la definizione di alcune formule, molti dei valori che definiscono la geometria finale.
-   Abbiamo definito qualche proprietà `Placement` per i vari componenti base della geometria e abbiamo definito la parte `Rotation` della proprietà `Placement` usando la scrittura *Yaw-Pitch-Roll*. Notate l\'ultimo componente `Vector(0,0, pos_ali)`, questo definisce il \"centro di rotazione\" della geometria finale.


</div>

  ----------------------------------------------------- ---------------------------------------------- ----------------------------------------------------
  ![aeroplane example](images/Aereo.png )   ![aereo rotated](images/Aereo2.png )   ![Prop Placement](images/Aereo-prop.png )
  ----------------------------------------------------- ---------------------------------------------- ----------------------------------------------------

Potete facilmente notare che l\'aereo ruota attorno al suo \"baricentro\" detto anche \"centro di gravità\", che ho fissato nel centro delle ali, una posizione abbastanza \"naturale\", potete comunque piazzarlo dove più vi aggrada o vi serve.

Il primo `Vector(0,0,0)` della definizione di `Placement` è il vettore di Traslazione (o di posizionamento), che qui non abbiamo usato, se però sostituite la riga `aeroplano()` con le linee seguenti:


```python

obj_f = aeroplano()

print(obj_F.Placement)

```


<div class="mw-translate-fuzzy">

Potete leggere nella finestra Report questo testo:


</div>


```python
Placement [Pos=(0,-21,21), Yaw-Pitch-Roll=(0,0,-90)]
```

Cosa è successo?

FreeCAD ha \"tradotto\" il posizionamento passato con `Vector(0,0,0), FreeCAD.Rotation(0,0,-90), Vector(0,0,pos_ali)`, che specificava tre componenti **Translazione**, **Rotazione** e *centro di rotazione*\' nel suo valore \"interno\" che possiede solo due componenti, **Translazione** e **Rotazione**.

Potete facilmente inserire nel codice del metodo `aeroplano(...` una istruzione che stampi `pos_ali`, e vedrete che vale:


```python
pos ali =  21.0
```

In parole povere, il *\'centro di rotazione* della geometria è posizionato a `Vector(0,0,21)`, ma non è mostrato attraverso l\'interfaccia grafica nella vista Dati, può essere specificato come valore nella proprietà `Placement`, ma non può essere facilmente recuperato.


<div class="mw-translate-fuzzy">

Questo è il significato dell\'aggettivo \"delicato\" che ho usato precedentemente nel testo per definire la proprietà `Placement`.


</div>


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Scripts/it
