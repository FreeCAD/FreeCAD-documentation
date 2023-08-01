# Placement/it
## Overview


<div class="mw-translate-fuzzy">

## Descrizione

**Placement** (Posizionamento) è la funzione utilizzata da FreeCAD per specificare la localizzazione (dove si trova) e l\'assetto (orientamento) di un oggetto nello spazio. Placement può essere specificato in diversi modi e manipolato tramite [script](Python_scripting_tutorial/it#Vettori_e_posizionamenti.md), tramite la scheda delle Proprietà oppure il dialogo **Placement** del menu **Modifica**.

### Accedere agli attributi di Placement 

Gli attributi di Posizionamento di un oggetto sono accessibili in tre modi:


</div>

### Accessing the Placement Attribute 

An object\'s Placement attributes can be accessed and modified in 3 ways:


<div class="mw-translate-fuzzy">

![Placement nella scheda delle Proprietà](images/PlacementPropertiesv10-800x800.png ) 


</div>


<div class="mw-translate-fuzzy">

![Script Placement con y/p/r, Matrix e la sua [API](images/Placement_API.md).](PlacePyConv10.png ) 


</div>

![Placement task panel](images/PlacementDialogv10.png ) 

## Forms of Placement 


<div class="mw-translate-fuzzy">

Il menu Modifica Posizionamento <img alt="Il menu Modifica Posizionamento" src=images/FreeCAD_Menu_Edition_Positionnement.png  style="width:256px;">

che apre e mostra lo strumento **Azioni di Posizionamento**. ![La finestra di dialogo di Placement Rotazione con angolo](images/PlacementDialogv10.png ) 

## Tipi di posizionamento 

Internamente il posizionamento viene memorizzato come una posizione, e una rotazione (asse di rotazione e angolo trasformati in un quaternione [1](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). Sebbene ci siano diversi modi di specificare una rotazione, per esempio con un centro di rotazione, questo è usato solo per influenzare il calcolo della rotazione e non viene memorizzato per le operazioni successive. Allo stesso modo, se viene specificato un asse di rotazione (1,1,1), esso può essere normalizzato se conservato nel quaternione e in seguito apparire nella forma (0.58, 0.58, 0.58) durante l\'esplorazione dell\'oggetto


</div>

### Angle, Axis and Position 


<div class="mw-translate-fuzzy">

### Angolo, Assi e Posizione 

**Placement=\[Angle, Axis, Position\]**


</div>


<div class="mw-translate-fuzzy">

La prima forma di **Placement** stabilisce la Posizione di un oggetto nello spazio e descrive il suo orientamento come una singola rotazione attorno ad un asse.

**Angle = r** : è uno scalare che indica la quantità di rotazione dell\'oggetto su Axis. Inserito in gradi, ma memorizzato internamente in radianti.


</div>

**Angle = r** is a scalar indicating the amount of rotation of the object about **Axis**. Entered as degrees, but stored internally as radians.


<div class="mw-translate-fuzzy">

**Axis = (ax,ay,az)** : è un vettore unitario che descrive un asse di rotazione (vedere [Nota](#Note.md) relativa all\'asse di rotazione).

Esempi:

   (1,0,0)       ==> sull'asse **X**
   (0,1,0)       ==> sull'asse **Y**
   (0,0,1)       ==> sull'asse **Z**
   (0.71,0.71,0) ==> sulla linea **y=x**


</div>

   (1,0,0)       ==> about **X** axis
   (0,1,0)       ==> about **Y** axis
   (0,0,1)       ==> about **Z** axis
   (0.71,0.71,0) ==> about the line **y=x**


<div class="mw-translate-fuzzy">

Notare che è anche possibile traslare (spostare) un oggetto lungo questo asse di rotazione (movimento assiale) inserendo la distanza dello spostamento nella casella di selezione Assiale e facendo clic sul pulsante Applica assiale. Un modo per immaginare lo spostamento assiale è pensare a un aeroplano con un\'elica che gira sul suo naso - l\'elica gira **attorno** a un asse di rotazione mentre l\'aereo si sposta **lungo** quello stesso asse . I valori nel vettore possono essere pensati come la quantità relativa di movimento che deve essere applicata in quella direzione. Ad esempio, nel caso y = x (0,71,0,71,0) il valore contenuto nello spinbox assiale viene applicato in misura uguale alle direzioni X e Y, e non si applica nessun movimento nella direzione Z.

**Position = (x,y,z)** è un vettore che descrive il punto da cui sarà calcolata la geometria dell\'oggetto (di fatto, una \"origine locale\" per l\'oggetto). Notare che negli script, Placement.Base è usato per indicare il componente di Posizione di un Placement. Il Property Editor chiama questo valore \"Position\" e la finestra di dialogo Placement lo chiama \"Traslazione\".


</div>

**Position = (x,y,z)** is a Vector describing the point from which the object\'s geometry will be calculated (in effect, a \"local origin\" for the object). Note that in scripts, Placement.Base is used to denote the Position component of a placement. The property editor calls this value **Position** and the Placement task panel calls it **Translation**.

### Position and Yaw, Pitch and Roll 


<div class="mw-translate-fuzzy">

#### Posizione con Imbardata, Beccheggio e Rollio 

![Placement Dialogo per gli Angoli di Eulero](images/PlacementDialogv10b.png ) 

**Placement = \[Position, Yaw-Pitch-Roll\]**


</div>

**Placement = \[Position, Yaw-Pitch-Roll\]**


<div class="mw-translate-fuzzy">

La seconda forma di **Placement** fissa la posizione di un oggetto nello spazio con Position (come nella prima forma), ma descrive il suo orientamento con gli angoli di imbardata, beccheggio e rollio. Questi angoli sono anche denominati angoli **Tait-Bryan** o [angoli di Eulero](http://it.wikipedia.org/wiki/Angoli_di_Eulero). Imbardata, beccheggio e rollio sono termini comuni nel settore dell\'aviazione per descrivere l\'orientamento (assetto) del veicolo.


</div>

**Position = (x,y,z)** è un vettore che descrive il punto da cui sarà calcolata la geometria dell\'oggetto (di fatto, una \"origine locale\" per l\'oggetto).


<div class="mw-translate-fuzzy">

**Yaw-Pitch-Roll = (y,p,r)** è una tupla che definisce l\'assetto dell\'oggetto. I valori di **y, p, r**, specificano i gradi di rotazione intorno agli assi **z, y, x**, vedere le Note.  
```python
>>> App.getDocument("Sans_nom").Cylinder.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(10,20,30), App.Vector(0,0,0))
```


</div>


```python
>>> App.ActiveDocument.Cylinder.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(10,20,30), App.Vector(0,0,0))
```

App.Rotation(10,20,30) = Angoli di Eulero

**Yaw** = 10 gradi (**Z**)

**Pitch** = 20 gradi (**Y**)

**Roll** = 30 gradi (**X**)

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Yaw** è la rotazione intorno all\'asse **Z**, destra sinistra e viceversa.
Angolo **Psi ψ**. 

![](images/Tache_Placement_Tangage_fr_Mini.gif )**Pitch** è la rotazione intorno all\'asse **Y**, alzare o abbassare il naso.
Angolo **Phi φ**. 

![](images/Tache_Placement_Roulis_fr_Mini.gif )**Roll** è la rotazione intorno all\'asse **X**, dondolare le ali.
Angolo **Thêta θ**. 

### Matrix


<div class="mw-translate-fuzzy">

#### Matrice

**Placement = Matrix**


</div>

La terza forma di **Placement** descrive la posizione dell\'oggetto e l\'orientamento con una matrice 4x4 di [Trasformazione Affine](http://it.wikipedia.org/wiki/Trasformazione_affine).

**Matrix** =


<div class="mw-translate-fuzzy">

((r11,r12,r13,t1),

   (r21,r22,r23,t2),
   (r31,r32,r33,t3),
   (0,0,0,1)) , dove rij specifica la rotazione e ti specifica la traslazione. 





</div>

## The Placement Dialog 


<div class="mw-translate-fuzzy">

### La finestra di dialogo Posizionamento 

La finestra di dialogo Posizionamento viene richiamata dal menu **Modifica**. E\' utilizzata per ruotare o traslare con precisione gli oggetti. E\' anche usata quando si deve creare uno schizzo su un piano \"non standard\" o per modificare l\'orientamento di un disegno in un nuovo piano.

La sezione **Traslazione** regola la posizione degli oggetti nello spazio.

La sezione **Centro** imposta singolarmente gli assi di rotazione che non passano attraverso il punto di riferimento dell\'oggetto.

La sezione **Rotazione** imposta l\'angolo, o gli angoli di rotazione e il metodo per specificare tali angoli.


</div>

-   The **Translation** section adjusts the object\'s location in space.
-   The **Center** section adjusts the rotational axis to one that does not pass through the object\'s reference point.
-   The **Rotation** section adjusts the rotational angle(s) and the method of specifying those angles.


<div class="mw-translate-fuzzy">

Ma mentre gli elementi all\'interno di ciascuna sezione si applicano generalmente alle finalità di quella sezione, ci sono anche alcuni elementi in una sezione che possono influenzare gli elementi in un\'altra sezione. Ad esempio, facendo clic sul pulsante Punti selezionati nella sezione **Centro** con 2 punti selezionati nella vista 3D si ottiene non solo il popolamento delle caselle di selezione delle coordinate **Centro** con le coordinate del punto medio tra i 2 punti selezionati, ma nella sezione **Rotazione** si crea anche un asse personalizzato lungo la linea definita dai 2 punti selezionati. In un altro esempio, posizionando un valore nella casella di selezione Assiale e facendo clic sul pulsante Applica assiale nella sezione **Traslazione** si trasla (sposta) l\'oggetto lungo l\'asse definito nella sezione **Rotazione**.

Selezionare la casella **Applica le modifiche incrementali al posizionamento dell\'oggetto** è utile quando le traslazioni o le rotazioni devono essere effettuate rispetto alla posizione o all\'assetto relativo corrente dell\'oggetto, invece che rispetto alla posizione o all\'assetto originale. Quando questa casella viene selezionata i valori dei campi di input della finestra di dialogo vengono reimpostati a zero, ma non si modifica l\'orientamento dell\'oggetto o la sua posizione. Successivi reimpostamenti modificano l\'orientamento o la posizione, ma vengono applicati a partire dalla posizione corrente dell\'oggetto. L\'attivazione di questa casella di controllo è utile anche quando si utilizza il pulsante Punti selezionati in quanto a volte può impedire modifiche indesiderate al posizionamento.


</div>

The **Apply incremental changes to object placement** tick box is useful when translations/rotations are to be made relative the object\'s current position/attitude, rather than to the original position/attitude. Ticking this box resets the dialogue input fields to zero, but does not change the object\'s orientation or location. Subsequent entries do change the orientation/location, but are applied from the object\'s current position. Enabling this checkbox is also useful when using the Selected points button as it can sometimes prevent undesired placement changes.


<div class="mw-translate-fuzzy">

PS: poiché la versione 0.17 introduce un nuovo oggetto Part, questo oggetto ha un suo Posizionamento e l\'oggetto Posizionamento creato nell\'oggetto Part viene incrementato con il Posizionamento di Part. {{Version/it|0.17}} Per ottenere il posizionamento di un oggetto Part usare questo codice:


</div>

To obtain the Part Placement use this code:


```python
import Draft, Part
sel = FreeCADGui.Selection.getSelection()
print(sel[0].Placement)
print(sel[0].getGlobalPlacement())   # return the GlobalPlacement
print(sel[0].getParentGeoFeatureGroup()) # return the GeoFeatureGroup, ex:  Body or a Part.
print("____________________")
```


<div class="mw-translate-fuzzy">

Il pulsante **Punti selezionati** viene utilizzato per popolare le coordinate nelle caselle di selezione delle coordinate di **Centro** e (quando sono selezionati 2 o 3 punti) in aggiunta per creare un asse di rotazione personalizzato (definito dall\'utente) nella sezione **Rotazione**. Un punto può essere un vertice, ma può anche essere qualsiasi punto lungo un bordo o su una faccia. Quando si seleziona un bordo o una faccia, viene selezionato l\'intero bordo o la faccia, ma FreeCAD ricorda anche il punto su quella faccia o bordo su cui era posizionato il puntatore del mouse quando quel bordo o quella faccia era selezionata. Sono le coordinate di questo punto che vengono utilizzate nella finestra di dialogo Posizionamento quando si fa clic sul pulsante **Punti selezionati**. Si può pensare che questo non sia un modo molto preciso di selezionare un punto ed è vero, ma in molti casi è sufficiente che il punto selezionato sia sicuramente su quel bordo o faccia. Nei casi in cui è necessario designare con precisione un punto da utilizzare, è necessario selezionare un vertice. Quando non è presente alcun vertice nella posizione desiderata, prendere in considerazione la possibilità di crearne uno, magari in uno schizzo temporaneo attaccato a quella faccia o bordo, magari utilizzando un oggetto Draft, come una linea o un punto, ecc.


</div>


<div class="mw-translate-fuzzy">

Consideriamo innanzitutto il caso semplice di selezione di 1 punto. Il flusso di lavoro consiste innanzitutto nel selezionare il punto desiderato, quindi fare clic sul pulsante **Punti selezionati**. Le coordinate del punto selezionato vengono utilizzate per popolare i campi X, Y e Z all\'interno della sezione **Centro**. Ora qualsiasi rotazione fatta sull\'oggetto sarà fatta attorno a questo centro di rotazione.


</div>


<div class="mw-translate-fuzzy">

Ora consideriamo il caso in cui si selezionano 2 punti. Bisogna selezionare i 2 punti desiderati, quindi fare clic sul pulsante **Punti selezionati**. Le coordinate del punto medio tra i 2 punti selezionati vengono posizionate nei campi X, Y e Z all\'interno della sezione **Centro**. Ora qualsiasi rotazione fatta sull\'oggetto sarà fatta attorno a questo centro di rotazione. Ma oltre a impostare le coordinate della sezione **Centro** viene aggiunto un asse personalizzato (definito dall\'utente) all\'elemento **Asse** all\'interno della sezione **Rotazione**. (Nota: se si era in modalità Eulero, la modalità viene commutata su asse di rotazione con angolo e il nuovo asse personalizzato viene selezionato come asse di rotazione corrente.) Ora qualsiasi rotazione eseguita utilizzando il nuovo asse personalizzato riguarderà questo asse di rotazione. Come bonus aggiuntivo, la distanza viene misurata tra i 2 punti selezionati e queste informazioni vengono fornite nella vista report. (Nota: tenere premuto il tasto Maiusc mentre si fa clic sul pulsante **Punti selezionati** per copiare la misurazione della distanza negli Appunti.) Inserendo questa distanza nella casella di selezione assiale nella sezione **Traslazione** e facendo clic sul pulsante **Applica assiale** è possibile traslare (spostare) l\'oggetto in modo che il primo punto selezionato occupi ora le coordinate occupate dal secondo punto selezionato (al momento in cui è stato fatto clic sul pulsante **Punti selezionati** ).


</div>


<div class="mw-translate-fuzzy">

Ora consideriamo il caso di selezione di 3 punti. Bisogna selezionare i 3 punti desiderati, quindi fare clic sul pulsante **Punti selezionati**. Le coordinate del primo punto selezionato (qui l\'ordine di selezione è molto importante) vengono posizionate nei campi X, Y e Z all\'interno della sezione **Centro**. Poiché 3 punti definiscono un piano FreeCAD è in grado di trarne vantaggio e di utilizzare i 3 punti per creare un nuovo asse di rotazione personalizzato (definito dall\'utente) che è normale (perpendicolare) al piano definito. Come per 2 punti selezionati, la distanza tra i punti viene mostrata nella vista report, ma questa volta è la distanza tra il 2o e il 3o punto selezionato. (Nota: tenere premuto il tasto Maiusc mentre si fa clic sul pulsante **Punti selezionati** - Maiusc + clic - per copiare la misurazione dell\'angolo negli Appunti.) Inoltre, viene misurato anche l\'angolo tra il 2o e il 3o punto e visualizzato nella vista report. Inserendo questo angolo nella casella **Angolo** all\'interno della sezione **Rotazione** si può ruotare con precisione l\'oggetto in modo tale che ora il secondo punto selezionato sia allineato con le coordinate occupate dal terzo punto selezionato . (Nota: per aumentare il numero di cifre utilizzate andare nel menu Modifica -\> Preferenze -\> Generale -\> Unità -\> Numero di decimali se si desidera maggiore precisione.)


</div>

## Examples


<div class="mw-translate-fuzzy">

## Esempi

Rotazione su un singolo asse:


</div>


<div class="mw-translate-fuzzy">


<center>

Image:RotationAboutZBefore.png\|Prima della rotazione (Vista dall\'alto)


</center>


<center>

Image:RotationAboutZAfter.png\|Dopo la rotazione rispetto all\'asse Z (Vista dall\'alto) Image:RotationAboutYXAfter.png\|Prima della rotazione rispetto a y=x (Vista da destra)


</center>

Rotazione con scostamento del punto centrale:


</div>

<img alt="After Rotation about Z" src=images/RotationAboutZAfter.png  style="width:600px;"> After Rotation about Z (top view) 

<img alt="After Rotation about y=x" src=images/RotationAboutYXAfter.png  style="width:600px;"> After Rotation about y=x (right view) 

Rotation with offset centre point:


<div class="mw-translate-fuzzy">


<center>

Image:RotationOffsetBefore.png\|Prima della rotazione (Vista dall\'alto) Image:RotationOffsetAfter.png\|Dopo la rotazione rispetto all\'asse Z (Vista dall\'alto)


</center>

Rotazione con impiego degli angoli di Eulero:


</div>

<img alt="After Rotation about Z" src=images/RotationOffsetAfter.png  style="width:600px;"> After Rotation about Z (top view) 

Rotation using Euler angles:

<img alt="Before Rotation" src=images/RotationEulerBefore.png  style="width:600px;"> Before Rotation 

<img alt="After Rotation" src=images/RotationEulerAfter.png  style="width:600px;"> After Rotation 

## Placement.Base vs Shape Definition 


<div class="mw-translate-fuzzy">


<center>

Image:RotationEulerBefore.png\|Prima della rotazione Image:RotationEulerAfter.png\|Dopo la rotazione


</center>

### Placement.Base vs Shape Definition 

Placement non è l\'unico modo per posizionare una forma nello spazio. Notare la console Python in questa immagine:


</div>


<div class="mw-translate-fuzzy">

![2 Forme con Stesso Placement](images/2Placements800.png )


</div>


<div class="mw-translate-fuzzy">

Entrambi i cubi hanno lo stesso valore per il Placement, ma si trovano in luoghi diversi! Questo perché le due forme sono definite da differenti vertici (curve in forme complesse). Per le due forme della figura sopra:


</div>

 >>> ev = App.ActiveDocument.Extrude.Shape.Vertexes
 >>> for v in ev: print(v.X,",",v.Y,",",v.Z)
 ...
 30.0,30.0,0.0
 30.0,30.0,10.0
 40.0,30.0,0.0
 40.0,30.0,10.0
 40.0,40.0,0.0
 40.0,40.0,10.0
 30.0,40.0,0.0
 30.0,40.0,10.0
 >>> e1v = App.ActiveDocument.Extrude001.Shape.Vertexes
 >>> for v in e1v: print(v.X,",",v.Y,",",v.Z)
 ...
 0.0,10.0,0.0
 0.0,10.0,10.0
 10.0,10.0,0.0
 10.0,10.0,10.0
 10.0,0.0,0.0
 10.0,0.0,10.0
 0.0,0.0,0.0
 0.0,0.0,10.0
 >>>

The Vertices (or Vectors) that define the shape use the Placement.Base attribute as their origin. So if you want to move a shape 10 units along the **X** axis, you could add 10 to the **X** coordinates of all the Vertices or you could set Placement.Base to (10,0,0).

## Using \"Center\" to Control Axis of Rotation 


<div class="mw-translate-fuzzy">

 >>> ev = App.ActiveDocument.Extrude.Shape.Vertexes
 >>> for v in ev: print v.X,",",v.Y,",",v.Z
 ... 
 30.0,30.0,0.0
 30.0,30.0,10.0
 40.0,30.0,0.0
 40.0,30.0,10.0
 40.0,40.0,0.0
 40.0,40.0,10.0
 30.0,40.0,0.0
 30.0,40.0,10.0
 >>> e1v = App.ActiveDocument.Extrude001.Shape.Vertexes
 >>> for v in e1v: print v.X,",",v.Y,",",v.Z
 ... 
 0.0,10.0,0.0
 0.0,10.0,10.0
 10.0,10.0,0.0
 10.0,10.0,10.0
 10.0,0.0,0.0
 10.0,0.0,10.0
 0.0,0.0,0.0
 0.0,0.0,10.0
 >>> 

I Vertices (o Vectors) che definiscono la forma usano gli attributi Placement.Base per la loro origine.

Quindi, se si desidera spostare una forma di 10 unità lungo l\'asse **X**, si può aggiungere 10 alla coordinata **X** di tutti i Vertices oppure è possibile impostare Placement.Base a (10,0,0).

### Controllare l\'asse di rotazione con **Centro** di **Posizionamento** 

Per impostazione predefinita, l\'asse di rotazione non è effettivamente l\'asse x, y o z. Si tratta di una linea parallela all\'asse selezionato che passa per il punto definito da **Placement.Base** dell\'oggetto da ruotare. Questa impostazione può essere modificata utilizzando i campi **Centro** della finestra di dialogo **Posizionamento** oppure, negli script, utilizzando il parametro **centre** nella costruzione di **FreeCAD.Placement**.


</div>


<div class="mw-translate-fuzzy">

Si supponga, ad esempio, di avere un cubo (figura sotto) posizionato in (20,20,10). ![Prima della rotazione](images/LocalZBefore2.png ) Volendo ruotare il cubo attorno al proprio asse verticale (l\'asse locale Z), mantenendolo nella stessa posizione. E\' possibile ottenere facilmente questo specificando nei campi Centro un valore corrispondente alle coordinate del punto centrale del cubo (25,25,15). ![Dopo la rotazione](images/LocalZAfter2.png )


</div>

![Before Rotation](images/LocalZBefore2.png ) 

We wish to spin the box around it\'s own vertical centre line (ie local Z), while keeping it the same position. We can easily achieve this by specifying a Center value equal to the coordinates of the box\'s central point (25,25,15).

![After Rotation](images/LocalZAfter2.png ) 

In a script, we would do:


```python
import FreeCAD
obj = App.ActiveDocument.Box                       # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)   # 45° about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)   # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                   # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X)
centre = FreeCAD.Vector(25,25,15)                  # central point of box
pos = obj.Placement.Base                           # position point of box
newplace = FreeCAD.Placement(pos,rot,centre)       # make a new Placement object
obj.Placement = newplace                           # spin the box
```

Alcuni script con i file di esempio: [RotateCoG2.fcstd](http://forum.freecadweb.org/download/file.php?id=1651) (discussion on the [forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3950#p31052))


```python
import FreeCAD
obj = App.ActiveDocument.Extrude                    # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)    # 45 about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)    # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                    # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X)
centre = FreeCAD.Vector(25,25,0)                    # "centre" of rotation (where local Z cuts XY)
pos = obj.Placement.Base                            # original placement of obj
newplace = FreeCAD.Placement(pos,rot,centre)        # make a new Placement object
obj.Placement = newplace                            # spin the box
```

## Using Placement in expressions 

In expressions it is possible to use the components of the placement for example to access the x-component of the object labeled \"Cube\":


```python
<<Cube>>.Placement.Base.x
```

You can access the angle of the rotation by


```python
<<Cube>>.Placement.Rotation.Angle
```

The axis of rotation can be accessed with


```python
<<Cube>>.Placement.Rotation.Axis.x
<<Cube>>.Placement.Rotation.Axis.y
<<Cube>>.Placement.Rotation.Axis.z
```

where often one of these values is 1 while the others are 0.

You can also use the whole Placement in a single expression:

Right click on Placement property in the property editor, select \"show all\" then extra properties will show. If you then right click on Placement again the context menu will include Expression, select Expression then the Expression dialogue will open and whatever you type will go into the Placement property rather than its child properties.

To make the placement of \"Sketch\" equal to that of \"Cylinder\", you would enter in that way for Sketch the expression


```python
<<Cube>>.Placement
```

![Setting the whole Placement in one expression](images/PlacementInExpression.png ) 

**NOTE:** It\'s also possible to *create* Placement objects in expressions. See the [Expressions](Expressions#Placement.md) page for details.

## Notes


<div class="mw-translate-fuzzy">

## Note

-   Assi e Angolo possono anche essere espressi con un [quaternione](http://it.wikipedia.org/wiki/Rotazioni_spaziali_con_i_quaternioni).
-   Il punto di riferimento di un oggetto varia a seconda dell\'oggetto. Alcuni esempi di oggetti di uso comune:

  Oggetto                              Punto di riferimento
   
  Part.Box                             vertice sinistro (minimo x), frontale (minimo y), in basso (minimo z)
  Part.Sphere                          centro della sfera (centro del suo contenitore cubico)
  Part.Cylinder                        centro della faccia di base
  Part.Cone                            centro della faccia di base (o superiore se il raggio della faccia di base vale **0**)
  Part.Torus                           centro del toro
  Caratteristiche derivate ​​da Sketch   la caratteristica eredita la posizione dello schizzo sottostante. Lo schizzo inizia sempre con Position = (0,0,0).


</div>

  Object                           Reference Point
   
  Part.Box                         left (minx), front (miny), bottom (minz) vertex
  Part.Sphere                      center of the sphere (ie centre of bounding box)
  Part.Cylinder                    center of the bottom face
  Part.Cone                        center of bottom face (or apex if bottom radius is 0)
  Part.Torus                       center of the torus
  Features derived from Sketches   the Feature inherits the Position of the underlying Sketch. Sketches always start with Position = (0,0,0). This position corresponds to the origin in the sketch.



## Per saperne di più 


<div class="mw-translate-fuzzy">

-   Il tutorial [Aeroplano](Aeroplane/it.md) tratta ampiamente sul meccanismo di modifica dell\'assetto di un oggetto.
-   Una descrizione dettagliata della funzione **Placement** si trova nella pagina [Azioni di Posizionamento](Tasks_Placement/it.md).


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > Placement/it
