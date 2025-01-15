# <img alt="Icona dell\'ambiente Assembly" src=images/Workbench_Assembly.svg  style="width:64px;"> Assembly Workbench/it






## Introduzione


{{Version/it|1.0}}

L\'<img alt="" src=images/Workbench_Assembly.svg  style="width:24px;"> [Ambiente Assembly](Assembly_Workbench/it.md) è il nuovo ambiente di lavoro integrato di FreeCAD per la creazione di assiemi. Utilizza il risolutore open source [Ondsel](https://github.com/Ondsel-Development/OndselSolver).

<img alt="" src=images/Assembly_Workbench_Example.png  style="width:400px;">



## Strumenti



### Assieme

-   <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:32px;"> [Crea Assieme](Assembly_CreateAssembly/it.md): crea un assieme radice nel documento corrente o un sottoassieme in un assieme attivo preesistente.

-   <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Inserire:

  - <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"> [Inserisci componente](Assembly_InsertLink/it.md): inserisce un componente nell\'assembly attivo.

  - <img alt="" src=images/Assembly_InsertNewPart.svg  style="width:32px;"> [Inserisci una nuova parte](Assembly_InsertNewPart/it.md): Inserisce una nuova parte.

-   <img alt="" src=images/Assembly_SolveAssembly.svg  style="width:32px;"> [Risolvi l\'assieme](Assembly_SolveAssembly/it.md): risolve l\'assieme attualmente attivo.

-   <img alt="" src=images/Assembly_CreateView.svg  style="width:32px;"> [Crea Vista Esplosa](Assembly_CreateView/it.md): crea un contenitore di viste esplose nell\'assieme attivo che contiene una o più viste esplose.

-   <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:32px;"> [Crea una simulazione](Assembly_CreateSimulation/it.md): crea una simulazione per l\'assieme corrente. {{Version/it|1.1}}

-   <img alt="" src=images/Assembly_CreateBom.svg  style="width:32px;"> [Crea una distinta base](Assembly_CreateBom/it.md): crea una distinta dei materiali (BOM) da un assieme selezionato o dal documento.

-   <img alt="" src=images/Assembly_ExportASMT.svg  style="width:32px;"> [Esporta File ASMT](Assembly_ExportASMT/it.md): esporta l\'assieme attualmente attivo come file ASMT.



### Giunti

-   <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:32px;"> [Attiva\\disattiva fissaggio](Assembly_ToggleGrounded/it.md): fissa la posizione e l\'orientamento di una forma in relazione al sistema di coordinate dell\'assieme a cui appartiene.

-   <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:32px;"> [Crea un giunto fisso](Assembly_CreateJointFixed/it.md): crea un giunto che blocca tra di loro due parti dell\'assieme, impedendo qualsiasi movimento o rotazione, ma può essere utilizzato anche per definire altri tipi di giunti.

-   <img alt="" src=images/Assembly_CreateJointRevolute.svg  style="width:32px;"> [Crea giunto di rotazione](Assembly_CreateJointRevolute/it.md): crea un giunto incernierato, consentendo la rotazione attorno a un singolo asse tra le due parti selezionate.

-   <img alt="" src=images/Assembly_CreateJointCylindrical.svg  style="width:32px;"> [Crea giunto cilindrico](Assembly_CreateJointCylindrical/it.md): crea un giunto cilindrico tra le due parti selezionate, consentendo la rotazione attorno a un singolo asse e un movimento lungo lo stesso asse.

-   <img alt="" src=images/Assembly_CreateJointSlider.svg  style="width:32px;"> [Crea giunto di scorrimento](Assembly_CreateJointSlider/it.md): crea un giunto di scorrimento (prismatico) tra le due parti selezionate, consentendo un movimento lineare lungo un singolo asse e limitando la rotazione.

-   <img alt="" src=images/Assembly_CreateJointBall.svg  style="width:32px;"> [Crea giunto sferico](Assembly_CreateJointBall/it.md): crea un giunto sferico tra le due parti selezionate in un singolo punto, consentendo la libera rotazione attorno al punto e mantenendo entrambe le parti connesse in questo punto.

-   <img alt="" src=images/Assembly_CreateJointDistance.svg  style="width:32px;"> [Crea giunto di distanziamento](Assembly_CreateJointDistance/it.md): crea un giunto di distanziamento tra le due parti selezionate, fissando la distanza tra le due parti.

-   <img alt="" src=images/Assembly_CreateJointParallel.svg  style="width:32px;"> [Crea Vincolo di parallelismo](Assembly_CreateJointParallel/it.md): crea un giunto parallelo tra le due parti selezionate, impostando parallelamente gli assi Z dei sistemi di coordinate selezionati.

-   <img alt="" src=images/Assembly_CreateJointPerpendicular.svg  style="width:32px;"> [Crea Vincolo perpendicolare](Assembly_CreateJointPerpendicular/it.md): crea un giunto perpendicolare tra le due parti selezionate, impostando perpendicolarmente gli assi Z dei sistemi di coordinate selezionati.

-   <img alt="" src=images/Assembly_CreateJointAngle.svg  style="width:32px;"> [Crea Vincolo angolare](Assembly_CreateJointAngle/it.md): crea un vincolo angolare tra due parti selezionate, fissando l\'angolo tra gli assi Z dei sistemi di coordinate selezionati.

-   <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:32px;"> [Crea un vincolo Cremagliera e Pignone](Assembly_CreateJointRackPinion/it.md): crea un vincolo tra cremagliera e pignone che sincronizza la traslazione di una parte di un giunto scorrevole e la rotazione di una parte di un giunto rotante.

-   <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:32px;"> [Crea Vincolo di vite](Assembly_CreateJointScrew/it.md): crea un vincolo a vite (elicoidale) che accoppia la traslazione di una parte di un giunto scorrevole e la rotazione di una parte di un giunto rotante.

-   <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Crea Vincolo Ingranaggio/Cinghia:

  - <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:32px;"> [Crea Vincolo di ingranaggi](Assembly_CreateJointGears/it.md): crea un vincolo tra ingranaggi che accoppia la rotazione di due parti di due giunti rotanti diversi.

  - <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:32px;"> [Crea Vincolo di cinghia](Assembly_CreateJointBelt/it.md): crea un vincolo di cinghia che accoppia la rotazione di due parti di due giunti rotanti diversi.



## Preferenze

-   <img alt="" src=images/Preferences-assembly.svg  style="width:32px;"> [Preferenze](Assembly_Preferences/it.md): preferenze per l\'ambiente di lavoro Assembly.



## Esempio di manovella e slitta 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:80px;"> Questo esempio è provvisorio e potrebbe essere rimosso non appena saranno disponibili descrizioni/tutorial adeguati.


<div class="mw-collapsible-content">



### Assieme con manovella e slitta 

L\'assieme da creare è composto da quattro parti: una Base, un\'Asta Cursore, una Manovella e una Biella. Sono collegati con quattro giunti.

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:300px;">



*Parti assemblate: Base (ambra), Asta di scorrimento (azzurro chiaro), Manovella (rosso), Biella (verde)*



### Preparare le parti 

In questo esempio tutte le parti e l\'assieme vengono creati in un unico documento.

Le geometrie cilindriche degli oggetti sono parallele o perpendicolari, il resto delle forme non è rilevante per questo esempio a meno che non vi siano interferenze. Con questo presente si possono modellare gli oggetti o crearli con il codice Python seguente. Il codice creerà un nuovo documento con i quattro oggetti (più semplice rispetto alle immagini). Basta copiare e incollare le seguenti righe nella [Console Python](Python_console/it.md):


```python
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(140, 40, 7, App.Vector(0, -20, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(120, 0, 7))
box2 = Part.makeBox(20, 12, 10, App.Vector(5, -6, 7))
cyl2 = Part.makeCylinder(6, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(4, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
shape = box1.fuse([cyl1, box2, cyl2]).removeSplitter().cut(cyl3)
base = doc.addObject("Part::Feature", "Base")
base.Shape = shape

box1 = Part.makeBox(4, 12, 12, App.Vector(-12, -6, 0))
box2 = Part.makeBox(14, 12, 4, App.Vector(-8, -6, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(0, 0, 4))
cyl2 = Part.makeCylinder(4, 88, App.Vector(-12, 0, 6),App.Vector(-1, 0, 0))
shape = box1.fuse([box2, cyl1, cyl2]).removeSplitter()
slider_rod = doc.addObject("Part::Feature", "SliderRod")
slider_rod.Shape = shape
slider_rod.Placement.Base = App.Vector(100, -40, 0)

cyl1 = Part.makeCylinder(7.5, 4)
box1 = Part.makeBox(15, 30, 4, App.Vector(-7.5, 0, 0))
cyl2 = Part.makeCylinder(7.5, 4, App.Vector(0, 30, 0))
cyl3 = Part.makeCylinder(4, 6, App.Vector(0, 30, 4))
cyl4 = Part.makeCylinder(4, 4)
shape = cyl1.fuse([box1, cyl2]).removeSplitter().fuse(cyl3).cut(cyl4)
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = shape
crank.Placement.Base = App.Vector(125, -70, 0)

cyl1 = Part.makeCylinder(6, 4)
box1 = Part.makeBox(50, 12, 4, App.Vector(0, -6, 0))
cyl2 = Part.makeCylinder(6, 4, App.Vector(50, 0, 0))
cyl3 = Part.makeCylinder(4, 4)
cyl4 = Part.makeCylinder(4, 4, App.Vector(50, 0, 0))
shape = cyl1.fuse([box1, cyl2]).removeSplitter().cut(cyl3.fuse(cyl4))
connecting_rod = doc.addObject("Part::Feature", "ConnectingRod")
connecting_rod.Shape = shape
connecting_rod.Placement.Base = App.Vector(25, -70, 0)

mat = base.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
base.ViewObject.ShapeAppearance = (mat,)

mat = slider_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
slider_rod.ViewObject.ShapeAppearance = (mat,)

mat = crank.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
crank.ViewObject.ShapeAppearance = (mat,)

mat = connecting_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.0, 0.0)
connecting_rod.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Aggiungere un assieme 

Con lo strumento <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Crea Assieme](Assembly_CreateAssembly/it.md) aggiungere un assieme al documento.

<img alt="" src=images/Assembly_KinematicExample-01.png  style="width:200px;">



*Vista ad albero delle parti e dell'assieme*



### Spostare le parti in Assembly 

Nella [Vista albero](Vista_albero.md) trascinare e rilasciare le parti sull\'oggetto Assembly. Così possono essere gestiti dal risolutore di Assembly.

<img alt="" src=images/Assembly_KinematicExample-02.png  style="width:200px;">



*Le parti ora sono nel contenitore di Assembly*



### Fissare una parte 

Per fissare l\'assemblaggio nella posizione desiderata, la parte di base deve essere bloccata o fissata a terra, come si dice di seguito. Selezionare la base nella [Vista ad albero](Tree_view/it.md) o nella [Vista 3D](3D_view/it.md) e utilizzare lo strumento <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Attiva/disattiva fissaggio](Assembly_ToggleGrounded/it.md). Così si blocca la posizione della base in relazione al sistema di coordinate locale (LCS) del contenitore Assembly. Un oggetto GroundedJoint viene aggiunto al contenitore Joints.

<img alt="" src=images/Assembly_KinematicExample-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-04.png  style="width:240px;">



*Espandere il contenitore Joints per vedere l'oggetto GroundedJoint*



### Alternativa: Inserire il collegamento 

In alternativa ai due passaggi sopra menzionati è anche possibile utilizzare lo strumento <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Inserisci componente](Assembly_InsertLink/it.md) per posizionare gli oggetti all\'interno di un assieme. Il primo oggetto diventa automaticamente la parte fissata a terra. Ovvero è necessario iniziare con l\'oggetto Base. Lo strumento crea i collegamenti mentre gli oggetti originali rimangono all\'esterno dell\'assieme. Per evitare confusione è consigliabile renderli invisibili.



### Applicare i giunti 

Un giunto collega precisamente due elementi di due diverse parti. Facoltativamente possono essere selezionati prima che venga richiamato lo strumento giunto desiderato (qualsiasi numero di elementi selezionati diverso da due comporta una selezione vuota). Gli elementi definiscono la posizione e l\'orientamento di un LCS rappresentato da un cerchio pieno sul piano XY locale e tre linee lungo gli assi X (rosso), Y (verde) e Z (blu) locali.

-   Un giunto di rotazione tra base e manovella

<img alt="" src=images/Assembly_KinematicExample-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-06.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Crea giunto di rotazione](Assembly_CreateJointRevolute/it.md) → riposizionamento di Crank*

Muovere la **manovella** utilizzando il tasto sinistro del mouse. Dovrebbe essere possibile solo la rotazione attorno al perno.

-   Un giunto di scorrimento tra la base e il perno mobile

<img alt="" src=images/Assembly_KinematicExample-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-08.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointSlider.svg" width=24px> [Crea giunto di scorrimento](Assembly_CreateJointSlider/it.md) → perno mobile posizionato*

Spostare **SliderRod** utilizzando il tasto sinistro del mouse. Dovrebbe essere possibile il solo spostamento lungo l\'asse.

-   Un giunto di rotazione tra manovella e biella

<img alt="" src=images/Assembly_KinematicExample-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-10.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Crea giunto di rotazione](Assembly_CreateJointRevolute/it.md) → Biella posizionata*

Spostare **ConnectingRod** usando il tasto sinistro del mouse. Dovrebbe essere possibile solo una rotazione attorno al perno.

<img alt="" src=images/Assembly_KinematicExample-11.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-12.png  style="width:200px;">



*Se ci sono più giunti per un asse dobbiamo aiutare il risolutore a trovare la soluzione desiderata.<br>
Se necessario, cliccare e trascinare le parti in una posizione più facile da calcolare.*

-   Un Giunto cilindrico tra biella e perno scorrevole

<img alt="" src=images/Assembly_KinematicExample-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-14.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Crea giunto cilindrico](Assembly_CreateJointCylindrical/it.md) → assemblaggio completato*

Una volta completato l\'assemblaggio, utilizzare il puntatore del mouse per trascinare le parti in accordo con i giunti utilizzati.

#### Note

Il perno dello Slider Rod è orientato in modo ridondante. La sua linea centrale è parallela al perno della Base attraverso la catena cinematica dalla Base tramite Manovella e Biella, ovvero il suo asse Z locale non può ruotare attorno a nessun asse X o Y. Il giunto Slider impedisce anche la rotazione del suo asse Z attorno a due assi locali e quindi si traduce in due gradi di libertà ridondantemente vincolati. Un giunto Cilindrico al posto del giunto Slider bloccherebbe solo una rotazione, risultando in un solo grado di libertà vincolato ridondante.



### Azionare la manovella 

Per controllare il layout dell\'assemblaggio tramite l\'angolo tra la Base e la Manovella dobbiamo cambiare il giunto Revolute tra di loro in un giunto Fixed. Per farlo, fare doppio clic sull\'oggetto Revolute nella vista ad albero. Nella finestra di dialogo cambiare Revolute in Fixed e cambiare il valore Rotation come desiderato (il movimento dovrebbe seguire l\'azione della rotellina del mouse).

Notare che una modifica nel tipo di giunto cambierà l\'etichetta del giunto, ma non il suo nome. In questo caso l\'etichetta viene cambiata in \"Fixed\".

Per animare l\'assieme possiamo cambiare la Rotazione (Offset1.Angle) del giunto Fisso con del codice Python. Basta copiare e incollare le seguenti righe nella console Python:


```python
import math
import FreeCAD as App
import FreeCADGui as Gui

actuator = App.ActiveDocument.getObjectsByLabel("Fixed")[0]

for angle in range(0, 361, 10):
    # A full rotation of the Crank in steps of 10°
    actuator.Offset1.Rotation.Angle = math.radians(angle)
    App.ActiveDocument.recompute()
    Gui.updateGui()
```

Per includere anche questo angolo come risultato valido, la fine dell\'intervallo deve essere maggiore di 360.


</div>


</div>



## Esempio di giunto universale 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:80px;"> Questo esempio è temporaneo e potrebbe essere rimosso non appena saranno disponibili descrizioni/tutorial adeguati.


<div class="mw-collapsible-content">



### Assieme del giunto universale 

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:300px;">

In questo esempio viene creato un [giunto universale](https://en.wikipedia.org/wiki/Universal_joint).

L\'assieme è costituito da tre parti solide: due Forcelle identiche e una Croce. Sono necessari anche due elementi non solidi aggiuntivi, Axle1 e Axle2, che rappresentano gli assi angolati. Gli assi e le parti solide sono collegati con diversi giunti.



### Preparare le parti 

In questo esempio tutte le parti e l\'assieme vengono creati in un unico documento.

Il codice Python qui sotto crea un nuovo documento con quattro oggetti (solo 1 Fork). Basta copiare e incollare le seguenti righe nella [console Python](Python_console/it.md):


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = -80
axle1.Y2 = 0
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 80
axle2.Y2 = 0
axle2.Z2 = 0
axle2.Placement.Rotation.Angle = math.radians(20)

sph1 = Part.makeSphere(50, App.Vector(0, 0, 0), App.Vector(-1, 0, 0), 0, 90, 360)
box1 = Part.makeBox(50, 40, 80, App.Vector(-50, -20, -40))
cyl1 = Part.makeCylinder(20, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(20, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(30, 60, App.Vector(0, -30, 0), App.Vector(0, 1, 0))
box2 = Part.makeBox(30, 60, 60, App.Vector(0, -30, -30))
cyl4 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl5 = Part.makeCylinder(15, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
shape = sph1.common(box1).fuse([cyl1, cyl2]).cut(cyl3.fuse([box2, cyl4, cyl5]))
fork = doc.addObject("Part::Feature", "Fork")
fork.Shape = shape.removeSplitter()
fork.Placement.Base = App.Vector(0, 100, 0)

cyl1 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(15, 80, App.Vector(0, -40, 0), App.Vector(0, 1, 0))
shape = cyl1.fuse([cyl2])
cross = doc.addObject("Part::Feature", "Cross")
cross.Shape = shape.removeSplitter()
cross.Placement.Base = App.Vector(70, 100, 0)

mat = fork.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fork.ViewObject.ShapeAppearance = (mat,)

mat = cross.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cross.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Cambiare l\'angolo degli assi 

L\'angolo tra gli assi è impostato a 20 gradi. Se si vuole cambiare questo valore selezionare Axle2 e cambiare la proprietà Placement.Angle. Questa proprietà deve essere cambiata prima di spostare Axle2 nell\'assieme.

Attenzione: se l\'angolo è troppo grande, le parti potrebbero andare in collisione.



### Aggiungere un assieme 

Con lo strumento <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Crea Assieme](Assembly_CreateAssembly/it.md) aggiungere un assieme al documento.



### Spostare gli assi nell\'assieme 

Nella [Vista ad albero](Tree_view/it.md) trascinare e rilasciare gli assi sull\'oggetto Assembly.



### Fissare a terra gli assi 

Selezionare i due assi nella vista ad albero e usare lo strumento <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Attiva/disattiva fissaggio](Assembly_ToggleGrounded/it.md).



### Spostare i solidi nell\'assieme 

Per gli altri oggetti useremo lo strumento <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Inserisci componente](Assembly_InsertLink/it.md):

1.  Richiamare lo strumento.
2.  Nella finestra di dialogo che si apre fare clic una volta sull\'oggetto Cross, e sull\'oggetto Fork due volte.
3.  Premere il tasto **OK**.
4.  Rendere gli oggetti al di fuori dell\'assemblaggio invisibili.
5.  Se gli oggetti all\'interno dell\'assieme si sovrappongono troppo si possono trascinare in una nuova posizione.



### Applicare i giunti 

-   Un giunto di Rotazione tra Axle1 e Fork001

<img alt="" src=images/Assembly_UniversalJointExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-03.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Crea giunto di rotazione](Assembly_CreateJointRevolute/it.md) + Offset di +40mm or -40mm → riposizionamento di Fork001*

Se si richiama prima lo strumento e poi si selezionano gli elementi, è possibile fare clic vicino al punto finale corretto di Axle1 per evitare di dover inserire un offset.

-   Un giunto cilindrico tra Fork001 e Cross001

<img alt="" src=images/Assembly_UniversalJointExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-05.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Crea giunto cilindrico](Assembly_CreateJointCylindrical/it.md) → riposizionamento di Cross001*

-   Un giunto cilindrico tra Axle2 e Fork002

<img alt="" src=images/Assembly_UniversalJointExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-07.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Crea giunto cilindrico](Assembly_CreateJointCylindrical/it.md) → riposizionamento di Fork002*

Se richiesto invertire la direzione del giunto utilizzando il pulsante **<img src="images/_Button_sort.svg" width=16px>** nella barra degli strumenti.

-   Un giunto cilindrico tra Cross001 e Fork002

<img alt="" src=images/Assembly_UniversalJointExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-09.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Crea giunto cilindrico](Assembly_CreateJointCylindrical/it.md) → riposizionamento di Cross001 e di Fork002*



### Azionare il giunto universale 

Il giunto universale può essere movimentato spostando Fork001 con il mouse sinistro.

Se si desidera controllare la configurazione per diversi angoli di rotazione eseguire le seguenti operazioni:

1.  Modificare il giunto cilindrico tra Axle1 e Fork001 in un giunto fisso.
2.  Selezionare Offset1. Proprietà angolare del giunto fisso e ruotare la rotella del mouse.
3.  Il giunto universale può essere posizionato ad un angolo qualsiasi.


</div>


</div>



## Esempio di Morsa 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:80px;"> Questo esempio è temporaneo e potrebbe essere rimosso una volta che saranno disponibili descrizioni/tutorial appropriati.


<div class="mw-collapsible-content">



### Assieme della morsa 

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:300px;">

In questo esempio viene creata una [morsa](https://it.wikipedia.org/wiki/Morsa_(meccanica)).

L\'assieme è composto da tre parti solide: una ganascia fissa, una mobile e una vite con la leva. È anche necessario un ulteriore elemento non solido, una manovella. La manovella e le parti solide sono collegate con vari giunti.

Un giunto a vite accoppia la traslazione di una parte con un giunto di scorrimento alla rotazione di una parte con un giunto di rotazione. La parte vite deve fare sia una tralazione che un movimento di rotazione, quindi deve essere una parte con un giunto cilindrico. In questo assieme, la parte vite sarà accoppiata alla ganascia mobile con un giunto parallelo, alla manovella non solida con un giunto di parallelismo, e alla ganascia fissa con un giunto cilindrico.



### Preparare le parti 

In questo esempio tutte le parti e l\'assieme vengono creati in un unico documento.

Il codice Python qui sotto crea un nuovo documento con quattro oggetti. Basta copiare e incollare le seguenti righe nella [console Python](Python_console/it.md):


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(95, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box4 = Part.makeBox(35, 24, 24, App.Vector(0, -12, -12))
box5 = Part.makeBox(60, 34, 69, App.Vector(35, -17, -19))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
box7 = Part.makeBox(95, 90, 10, App.Vector(0, -45, -32))
shape = box1.fuse([cyl1, box2, box6, box7]).cut(cyl2.fuse([box3, cyl3, cyl4, cyl5, box4, box5]))
fixedJaw = doc.addObject("Part::Feature", "FixedJaw")
fixedJaw.Shape = shape.removeSplitter()
fixedJaw.Placement.Rotation.Axis = App.Vector(0, 0, 1)
fixedJaw.Placement.Rotation.Angle = math.radians(180)

box1 = Part.makeBox(35, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(160, 24, 24, App.Vector(-160, -12, -12))
box4 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box5 = Part.makeBox(160, 18, 18, App.Vector(-160, -9, -9))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
shape = box1.fuse([cyl1, box2, box3, box6]).cut(cyl2.fuse([box4, cyl3, cyl4, box5, cyl5]))
movableJaw = doc.addObject("Part::Feature", "MovableJaw")
movableJaw.Shape = shape.removeSplitter()
movableJaw.Placement.Base = App.Vector(150, 100, 0)

cyl1 = Part.makeCylinder(5, 190, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cyl2 = Part.makeCylinder(10, 20, App.Vector(190, 0, 0), App.Vector(1, 0, 0))
cyl3 = Part.makeCylinder(4, 100, App.Vector(200, 0, -50), App.Vector(0, 0, 1))
shape = cyl1.fuse([cyl2, cyl3])
leverScrew = doc.addObject("Part::Feature", "LeverScrew")
leverScrew.Shape = shape.removeSplitter()
leverScrew.Placement.Base = App.Vector(150, -100, 0)

wire1 = Part.makePolygon([App.Vector(0, 0, 100), App.Vector(0, 0, 0), App.Vector(100, 0, 0)])
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = wire1
crank.Placement.Base = App.Vector(0, -100, 0)

mat = fixedJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fixedJaw.ViewObject.ShapeAppearance = (mat,)

mat = movableJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
movableJaw.ViewObject.ShapeAppearance = (mat,)

mat = leverScrew.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
leverScrew.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Aggiungere un assieme 

Con lo strumento <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Crea Assieme](Assembly_CreateAssembly/it.md) aggiungere un assieme al documento.



### Spostare le parti in Assembly 

Nella [Vista albero](Tree_view/it.md) trascinare e rilasciare le parti sull\'oggetto Assembly. Così possono essere gestiti dal risolutore di Assembly.



### Fissare una parte 

Per mantenere l\'assemblaggio nella posizione desiderata, la parte FixedJaw deve essere bloccata, o messa a terra come viene chiamata qui. Selezionare il FixedJaw nella [Vista ad albero](Tree_view/it.md) o nella [Vista 3D](3D_view/it.md)\] ed utilizzare lo strumento <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> \[\[Assembly_ToggleGrounded/it\|Attiva/disattiva fissaggio\]. Un oggetto GroundedJoint viene aggiunto al contenitore dei Joints.



### Applicare i giunti 

-   Un giunto di rotazione tra FixedJaw e Crank

<img alt="" src=images/Assembly_ViseExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-03.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Crea giunto di rotazione](Assembly_CreateJointRevolute/it.md) → manovella posizionata*

-   Un giunto di scorrimento tra FixedJaw e MovableJaw

<img alt="" src=images/Assembly_ViseExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-05.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointSlider.svg" width=24px> [Crea giunto di scorrimento](Assembly_CreateJointSlider/it.md) → riposizionamento di MovableJaw*

Impostare la lunghezza minima a -77 mm e la lunghezza massima a -7 mm. Così si limita l\'apertura della morsa a 70 mm.

I successivi tre giunti sono necessari per forzare il LeverScrew a: traslare come il MovableJaw, ruotare come il Crank, e ruotare intorno all\'asse principale.

-   Un giunto di distanziamento tra LeverScrew e MovableJaw

<img alt="" src=images/Assembly_ViseExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-07.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointDistance.svg" width=24px> [Crea giunto di distanziamento](Assembly_CreateJointDistance/it.md) → riposizionamento di LeverScrew*

Seleziona due facce. Impostare il valore di distanza a 20 mm.

-   Un vincolo di parallelismo tra LeverScrew e Crank

<img alt="" src=images/Assembly_ViseExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-09.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointParallel.svg" width=24px> [Crea vincolo di parallelismo](Assembly_CreateJointParallel/it.md) → riposizionamento di LeverScrew*

-   Un giunto cilindrico tra LeverScrew e FixedJaw

<img alt="" src=images/Assembly_ViseExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-11.png  style="width:200px;">



*Elementi selezionati + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Crea un giunto cilindrico](Assembly_CreateJointCylindrical/it.md) → riposizionamento di LeverScrew*

-   Un giunto a vite tra MovableJaw e Crank

<img alt="" src=images/Assembly_ViseExample-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-13.png  style="width:200px;">



*Elementi selezionati (LeverScrew invisible) + <img src="images/Assembly_CreateJointScrew.svg" width=24px> [Create un vincolo di Vite](Assembly_CreateJointScrew/it.md) → meccanismo completo della morsa (LeverScrew è visibile)*

Se necessario rendere invisibile LeverScrew durante la selezione.

Impostare il raggio Pitch a 5 mm



### Azionare la morsa 

La morsa può essere movimentata spostando Crank o MovableJaw con il mouse sinistro.


</div>


</div>



## Esempio di ammortizzatore 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ShockAbsorberExample-01.png  style="width:80px;"> Questo esempio è temporaneo e potrebbe essere rimosso una volta che saranno disponibili descrizioni/tutorial appropriati.


<div class="mw-collapsible-content">



### Assieme dell\'ammortizzatore 

<img alt="" src=images/Assembly_ShockAbsorberExample.gif  style="width:300px;">

In questo esempio viene creato un [ammortizzatore](https://it.wikipedia.org/wiki/Ammortizzatore).

L\'assemblaggio è composto da tre parti solide: un pistone, un cilindro e una molla. Sono necessari altri tre elementi non solidi, due assi e un\'asta. Tutte le parti sono collegate con i relativi giunti.

La cerniera del pistone ruota intorno a Axle2, mentre la cerniera del cilindro si muove su un arco di cerchio incentrato su Axle1. Il Rod non solido è usato per questo movimento. La lunghezza del Rod è il raggio dell\'arco.



### Preparare le parti 

Il codice Python qui sotto creerà un nuovo documento con 6 oggetti. Creare una nuova [macro](Macros/it.md) e copiare il codice sottostante nell\'editor Python (non nella console Python). Quindi \[Std_DlgMacroExecuteDirect/it\|eseguire la macro\].

Il codice sottostante non può essere eseguito dalla console Python perché la molla deve essere un oggetto [Part:::FeaturePython](App_FeaturePython.md) definito da una classe con le funzioni di callback {{Incode|execute()}} e {{Incode|onChanged()}}. Solo allora la sua altezza può essere cambiata tramite la corrispondente proprietà.


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

class Spring():
    def __init__(self, spring):
        spring.addProperty("App::PropertyLength", "Height", "Spring", "Height of the helix").Height = 200.0
        spring.Proxy = self
        spring.ViewObject.Proxy = 0
        
    def execute(self, spring):
        helix = Part.makeHelix(spring.Height/8.5, spring.Height, 35)
        startPnt = helix.Edges[0].Curve.value(0)
        section = Part.Wire([Part.Circle(startPnt, App.Vector(0, 1, 0), 5).toShape()])
        hel1 = helix.makePipeShell([section], True, True)
        box1 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, -10))
        box2 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, spring.Height))
        shape = hel1.cut(box1).cut(box2)
        spring.Shape = shape
        
    def onChanged(self, spring, prop):
        if prop == "Height":
            self.execute(spring) 
            
spring = doc.addObject("Part::FeaturePython", "Spring")
Spring(spring)
spring.Placement.Base = App.Vector(0, 100, 0)

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = 0
axle1.Y2 = 80
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 0
axle2.Y2 = 80
axle2.Z2 = 0
axle2.Placement.Base = App.Vector(120, 0, -250)

rod = doc.addObject("Part::Line", "Rod")
rod.X2 = 100
rod.Y2 = 0
rod.Z2 = 0
rod.Placement.Base = App.Vector(0, -50, 0)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10, App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(5, 130)
cyl7 = Part.makeCylinder(20, 5,App.Vector(0, 0, 130))
shape = cyl1.fuse([tor1,cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, cyl7])
piston = doc.addObject("Part::Feature", "Piston")
piston.Shape = shape.removeSplitter()
piston.Placement.Base = App.Vector(200, 100, -200)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(25, 130)
tor2 = Part.makeTorus(20, 5,App.Vector(0, 0, 130))
cyl7 = Part.makeCylinder(20, 135)
cyl8 = Part.makeCylinder(20, 130)
cyl9 = Part.makeCylinder(5, 135)
shape = cyl1.fuse([tor1, cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, tor2, cyl7]).cut(cyl8.fuse([cyl9]))
cylinder = doc.addObject("Part::Feature", "Cylinder")
cylinder.Shape = shape.removeSplitter()
cylinder.Placement.Rotation.Axis = App.Vector(0, 1, 0)
cylinder.Placement.Rotation.Angle = math.pi
cylinder.Placement.Base = App.Vector(100, 100, 0)

mat = piston.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
piston.ViewObject.ShapeAppearance = (mat,)

mat = cylinder.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cylinder.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```



### Aggiungere un assieme 

Con lo strumento <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Crea Assieme](Assembly_CreateAssembly/it.md) aggiungere un assieme al documento.



### Spostare le parti in Assembly 

Nella [Vista albero](Tree_view/it.md) trascinare e rilasciare le parti sull\'oggetto Assembly. Così possono essere gestiti dal risolutore di Assembly.



### Fissare i due assi 

Per mantenere l\'assieme nella posizione desiderata, i due assi devono essere bloccati, o a terra come viene detto qui. Selezionare i due assi nella [Vista ad albero]([Tree_view/it.md)\] o nella [Vista 3D](3D_view/it.md)\] ed utilizzare lo strumento <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> \[\[Assembly_ToggleGrounded/it\|Attiva/disattiva fissaggio\]. I due oggetti GroundedJoint vengono aggiunti al contenitore Joints.



### Applicare i giunti 

-   Un giunto di Rotazione tra Axle2 e Piston

<img alt="" src=images/Assembly_ShockAbsorberExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-03.png  style="width:200px;">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Crea giunto di rotazione](Assembly_CreateJointRevolute/it.md) + Elementi selezionati → riposizionamento di Piston*

-   Un giunto di scorrimento tra Piston e Cylinder

<img alt="" src=images/Assembly_ShockAbsorberExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-05.png  style="width:200px;">



*<img src="images/Assembly_CreateJointSlider.svg" width=24px> [Crea giunto di scorrimento](Assembly_CreateJointSlider/it.md) + Elementi selezionati → riposizionamento e spostamento di Cylinder*

Si presti attenzione alla posizione del sistema di coordinate prima di selezionare una faccia. Dovrebbe essere al centro di ognuna delle facce.

Trascinare il cilindro per creare una distanza tra questo e il pistone. Le facce di sostegno per la Spring dovrebbero essere visibili.

-   Un giunto di distanziamento tra Piston e Cylinder

<img alt="" src=images/Assembly_ShockAbsorberExample-06A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-06B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-07.png  style="width:200px;">



*<img src="images/Assembly_CreateJointDistance.svg" width=24px> [Crea Giunto di distanziamento](Assembly_CreateJointDistance/it.md) + Facce selezionate → riposizionamento di Cylinder Distance a 200 mm*

Impostare il valore di distanza a 200 mm.

I due vincoli successivi sono necessari per forzare la cerniera del cilindro a muoversi su un arco di cerchio.

-   Un giunto cilindrico tra Axle1 e Rod

<img alt="" src=images/Assembly_ShockAbsorberExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-09.png  style="width:200px;">



*<img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Crea giunto cilindrico](Assembly_CreateJointCylindrical/it.md) + Elementi selezionati → riposizionamento di Rod*

Assicurarsi che l\'asse Z del sistema di coordinate (blu) sia perpendicolare a Rod selezionando un punto finale.

-   Un giunto di rotazione tra Rod e Cylinder

<img alt="" src=images/Assembly_ShockAbsorberExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-11.png  style="width:200px;">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Crea giunto di rotazione](Assembly_CreateJointRevolute/it.md) + Elementi selezionati → riposizionamento di Cylinder*

Ancora una volta assicurarsi che l\'asse Z del sistema di coordinate (blu) sia perpendicolare a Rod.

Si possono incontrare problemi con questo giunto. Se fosse questo il caso provare la seguente procedura:

1.  Eliminare il giunto.
2.  Passare alla [Vista frontale](Std_ViewFront/it.md).
3.  Ruotare l\'assieme (trascinando Piston) e ruotare Rod in modo che il centro del foro della cerniera del cilindro che si trova su Rod.
4.  Creare di nuovo il giunto.

I seguenti due giunti servono a fissare Spring alla faccia di supporto.

-   Un vincolo di parallelismo tra Spring e Piston

<img alt="" src=images/Assembly_ShockAbsorberExample-12A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-12B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-13.png  style="width:200px;">



*<img src="images/Assembly_CreateJointParallel.svg" width=24px> [Crea vincolo di parallelismo](Assembly_CreateJointParallel/it.md) + Facce selezionate → riposizionamento di Spring*

Selezionare il centro della faccia di supporto su Piston e il centro della faccia inferiore della molla. Tenere il valore di distanza pari a 0.

-   Un giunto fisso tra Spring e Piston

<img alt="" src=images/Assembly_ShockAbsorberExample-14A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-14B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-15.png  style="width:200px;">



*<img src="images/Assembly_CreateJointFixed.svg" width=24px> [Crea un giunto fisso](Assembly_CreateJointFixed/it.md) + Elementi selezionati → riposizionamento di Spring*

Selezionare il vertice inferiore della giunzione del cilindro nel pistone e il vertice dell\'angolo di Spring.

1.  Collegare la proprietà distance del giunto **Distance** alla proprietà \'\'\'Height\' di Spring utilizzando una [expressione](Espressions/it.md):




1.  Selezionare Spring nella [Vista ad albero](Tree_view/it.md).
2.  Selezionare l\'icona blu <img alt="" src=images/Bound-expression.svg  style="width:16px;"> nel campo di proprietà di Height.
3.  Inserire nell\'editor dell\'espressione: {{Incode|<<Distance>>.Distance}}



### Azionare l\'ammortizzatore 

Per farlo fare doppio clic sull\'oggetto Distance nella vista ad Albero e cambiare la sua proprietà Distance. Ricalcolare il documento. La Spring cambierà la sua lunghezza.


</div>


</div>





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Assembly](Category_Assembly.md) > Assembly Workbench/it
