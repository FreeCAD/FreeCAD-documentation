# Placement/it
## Panoramica

**Posizionamento** è il modo in cui FreeCAD specifica la posizione e l\'orientamento di un oggetto nello spazio. Il posizionamento può essere specificato in più forme e manipolato tramite [scripting](Python_scripting_tutorial#Vectors_and_placements.md), l\'[editor di proprietà](Property_editor/it.md) o selezionando **Modifica → Posizionamento...** per aprire [Pannello azioni di Posizionamento](Std_Placement/it.md).



### Accesso all\'Attributo di Posizionamento 

È possibile accedere e modificare gli attributi di Posizionamento di un oggetto in 3 modi:

![Posizionamento nell\'editor delle proprietà](images/PlacementPropertiesv10-800x800.png ) 

![Script Placement con y/p/r, Matrix e la sua [API](images/Placement_API.md).](PlacePyConv10.png ) 

![Pannello azioni di Posizionamento](images/PlacementDialogv10.png ) 



## Forme di posizionamento 

Il posizionamento viene memorizzato internamente come posizione e rotazione (asse di rotazione e angolo trasformati in un [quaternione](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). Sebbene esistano diversi moduli per specificare una rotazione, ad esempio con un centro di rotazione, questo viene utilizzato solo per influenzare il calcolo della rotazione e non viene memorizzato per operazioni successive. Allo stesso modo, se viene specificato un asse di rotazione di (1,1,1), può essere normalizzato quando memorizzato nel quaternione e apparire come (0.58, 0.58, 0.58) quando si esplora successivamente l\'oggetto.



### Angolo, Asse e Posizione 

**Placement=\[Angle, Axis, Position\]**

La prima forma di **Placement** stabilisce la Posizione di un oggetto nello spazio e descrive il suo orientamento come una singola rotazione attorno ad un asse.

**Angle = r** è uno scalare che indica la quantità di rotazione dell\'oggetto attorno all**Asse**. Inserito come gradi, ma memorizzato internamente come radianti.

**Axis = (ax,ay,az)** : è un vettore unitario che descrive un asse di rotazione (vedere [Nota](#Note.md) relativa all\'asse di rotazione). Esempi:

   (1,0,0)       ==> sull'asse **X**
   (0,1,0)       ==> sull'asse **Y**
   (0,0,1)       ==> sull'asse **Z**
   (0.71,0.71,0) ==> sulla linea **y=x**

Notare che è anche possibile traslare (spostare) un oggetto lungo questo asse di rotazione (movimento assiale) inserendo la distanza dello spostamento nella casella di selezione {{SpinBox|Axial: 0.0mm}} e facendo clic sul pulsante **Applica assiale**. Un modo per immaginare lo spostamento assiale è pensare a un aeroplano con un\'elica che gira sul suo naso - l\'elica gira **attorno** a un asse di rotazione mentre l\'aereo si sposta **lungo** quello stesso asse . I valori nel vettore possono essere pensati come la quantità relativa di movimento che deve essere applicata in quella direzione. Ad esempio, nel caso y = x (0,71,0,71,0) il valore contenuto nello spinbox assiale viene applicato in misura uguale alle direzioni X e Y, e non si applica nessun movimento nella direzione Z.

**Position = (x,y,z)** è un vettore che descrive il punto da cui sarà calcolata la geometria dell\'oggetto (di fatto, una \"origine locale\" per l\'oggetto). Notare che negli script, Placement.Base è usato per indicare il componente di Posizione di un Placement. L\'Editor delle Proprietà chiama questo valore \"Posizione\" e la finestra di dialogo Placement lo chiama \"Traslazione\".



### Posizione e Imbardata, Beccheggio e Rollio 

![Pannello azioni di Posizionamento: {{ComboBox|Angoli di Eulero}} selezionato](images/PlacementDialogv10b.png ) 

**Posizionamento = \[Posizione, Imbardata-Beccheggio-Rollio\]**

La seconda forma di **Placement** fissa la posizione di un oggetto nello spazio con **Position** (come nella prima forma), ma descrive il suo orientamento con gli angoli di imbardata, beccheggio e rollio ([Yaw, Pitch, Roll](http://en.wikipedia.org/wiki/Yaw,_pitch,_and_roll)). Questi angoli sono anche denominati [angoli di Eulero](http://it.wikipedia.org/wiki/Angoli_di_Eulero) o angoli **Tait-Bryan**. Imbardata, beccheggio e rollio sono termini comuni nel settore dell\'aviazione per descrivere l\'orientamento (assetto) del corpo.

**Position = (x,y,z)** è un vettore che descrive il punto da cui sarà calcolata la geometria dell\'oggetto (di fatto, una \"origine locale\" per l\'oggetto).

**Yaw-Pitch-Roll = (y,p,r)** è una tupla che specifica l\'assetto dell\'oggetto. I valori per y,p,r specificano i gradi di rotazione attorno a ciascuno degli assi z,y,x (vedi nota).


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



### Matrice

**Placement = Matrix**

La terza forma di **Placement** descrive la posizione dell\'oggetto e l\'orientamento con una matrice 4x4 di [Trasformazione Affine](http://it.wikipedia.org/wiki/Trasformazione_affine).

**Matrix** =

 ((r11,r12,r13,t1),
   (r21,r22,r23,t2),
   (r31,r32,r33,t3),
   (0,0,0,1)) , dove rij specifica la rotazione e ti specifica la traslazione.






## La finestra di dialogo Posizionamento 

La finestra di dialogo Posizionamento viene richiamata dal menu **Modifica**. E\' utilizzata per ruotare o traslare con precisione gli oggetti. E\' anche usata quando si deve creare uno schizzo su un piano \"non standard\" o per modificare l\'orientamento di un disegno in un nuovo piano.

La sezione **Traslazione** regola la posizione degli oggetti nello spazio.

La sezione **Centro** imposta singolarmente gli assi di rotazione che non passano attraverso il punto di riferimento dell\'oggetto.

La sezione **Rotazione** imposta l\'angolo, o gli angoli di rotazione e il metodo per specificare tali angoli.

Ma mentre gli elementi all\'interno di ciascuna sezione si applicano generalmente alle finalità di quella sezione, ci sono anche alcuni elementi in una sezione che possono influenzare gli elementi in un\'altra sezione. Ad esempio, facendo clic sul pulsante Punti selezionati nella sezione **Centro** con 2 punti selezionati nella vista 3D si ottiene non solo il popolamento delle caselle di selezione delle coordinate **Centro** con le coordinate del punto medio tra i 2 punti selezionati, ma nella sezione **Rotazione** si crea anche un asse personalizzato lungo la linea definita dai 2 punti selezionati. In un altro esempio, posizionando un valore nella casella di selezione Assiale e facendo clic sul pulsante Applica assiale nella sezione **Traslazione** si trasla (sposta) l\'oggetto lungo l\'asse definito nella sezione **Rotazione**.

Selezionare la casella **Applica le modifiche incrementali al posizionamento dell\'oggetto** è utile quando le traslazioni o le rotazioni devono essere effettuate rispetto alla posizione o all\'assetto relativo corrente dell\'oggetto, invece che rispetto alla posizione o all\'assetto originale. Quando questa casella viene selezionata i valori dei campi di input della finestra di dialogo vengono reimpostati a zero, ma non si modifica l\'orientamento dell\'oggetto o la sua posizione. Successivi reimpostamenti modificano l\'orientamento o la posizione, ma vengono applicati a partire dalla posizione corrente dell\'oggetto. L\'attivazione di questa casella di controllo è utile anche quando si utilizza il pulsante Punti selezionati in quanto a volte può impedire modifiche indesiderate al posizionamento.

PS: poiché la versione 0.17 introduce un nuovo oggetto Part, questo oggetto ha un suo Posizionamento e l\'oggetto Posizionamento creato nell\'oggetto Part viene incrementato con il Posizionamento di Part. {{Version/it|0.17}}

Per ottenere il posizionamento di un oggetto Part usare questo codice:


```python
import Draft, Part
sel = FreeCADGui.Selection.getSelection()
print(sel[0].Placement)
print(sel[0].getGlobalPlacement())   # return the GlobalPlacement
print(sel[0].getParentGeoFeatureGroup()) # return the GeoFeatureGroup, ex:  Body or a Part.
print("____________________")
```

Il pulsante **Punti selezionati** viene utilizzato per popolare le coordinate nelle caselle di selezione delle coordinate di **Centro** e (quando sono selezionati 2 o 3 punti) in aggiunta per creare un asse di rotazione personalizzato (definito dall\'utente) nella sezione **Rotazione**. Un punto può essere un vertice, ma può anche essere qualsiasi punto lungo un bordo o su una faccia. Quando si seleziona un bordo o una faccia, viene selezionato l\'intero bordo o la faccia, ma FreeCAD ricorda anche il punto su quella faccia o bordo su cui era posizionato il puntatore del mouse quando quel bordo o quella faccia era selezionata. Sono le coordinate di questo punto che vengono utilizzate nella finestra di dialogo Posizionamento quando si fa clic sul pulsante **Punti selezionati**. Si può pensare che questo non sia un modo molto preciso di selezionare un punto ed è vero, ma in molti casi è sufficiente che il punto selezionato sia sicuramente su quel bordo o faccia. Nei casi in cui è necessario designare con precisione un punto da utilizzare, è necessario selezionare un vertice. Quando non è presente alcun vertice nella posizione desiderata, prendere in considerazione la possibilità di crearne uno, magari in uno schizzo temporaneo attaccato a quella faccia o bordo, magari utilizzando un oggetto Draft, come una linea o un punto, ecc.

Consideriamo innanzitutto il caso semplice di selezione di 1 punto. Il flusso di lavoro consiste innanzitutto nel selezionare il punto desiderato, quindi fare clic sul pulsante **Punti selezionati**. Le coordinate del punto selezionato vengono utilizzate per popolare i campi X, Y e Z all\'interno della sezione **Centro**. Ora qualsiasi rotazione fatta sull\'oggetto sarà fatta attorno a questo centro di rotazione.

Ora consideriamo il caso in cui si selezionano 2 punti. Bisogna selezionare i 2 punti desiderati, quindi fare clic sul pulsante **Punti selezionati**. Le coordinate del punto medio tra i 2 punti selezionati vengono posizionate nei campi X, Y e Z all\'interno della sezione **Centro**. Ora qualsiasi rotazione fatta sull\'oggetto sarà fatta attorno a questo centro di rotazione. Ma oltre a impostare le coordinate della sezione **Centro** viene aggiunto un asse personalizzato (definito dall\'utente) all\'elemento **Asse** all\'interno della sezione **Rotazione**. (Nota: se si era in modalità Eulero, la modalità viene commutata su asse di rotazione con angolo e il nuovo asse personalizzato viene selezionato come asse di rotazione corrente.) Ora qualsiasi rotazione eseguita utilizzando il nuovo asse personalizzato riguarderà questo asse di rotazione. Come bonus aggiuntivo, la distanza viene misurata tra i 2 punti selezionati e queste informazioni vengono fornite nella vista report. (Nota: tenere premuto il tasto Maiusc mentre si fa clic sul pulsante **Punti selezionati** per copiare la misurazione della distanza negli Appunti.) Inserendo questa distanza nella casella di selezione assiale nella sezione **Traslazione** e facendo clic sul pulsante **Applica assiale** è possibile traslare (spostare) l\'oggetto in modo che il primo punto selezionato occupi ora le coordinate occupate dal secondo punto selezionato (al momento in cui è stato fatto clic sul pulsante **Punti selezionati** ).

Ora consideriamo il caso di selezione di 3 punti. Bisogna selezionare i 3 punti desiderati, quindi fare clic sul pulsante **Punti selezionati**. Le coordinate del primo punto selezionato (qui l\'ordine di selezione è molto importante) vengono posizionate nei campi X, Y e Z all\'interno della sezione **Centro**. Poiché 3 punti definiscono un piano FreeCAD è in grado di trarne vantaggio e di utilizzare i 3 punti per creare un nuovo asse di rotazione personalizzato (definito dall\'utente) che è normale (perpendicolare) al piano definito. Come per 2 punti selezionati, la distanza tra i punti viene mostrata nella vista report, ma questa volta è la distanza tra il 2o e il 3o punto selezionato. (Nota: tenere premuto il tasto Maiusc mentre si fa clic sul pulsante **Punti selezionati** - Maiusc + clic - per copiare la misurazione dell\'angolo negli Appunti.) Inoltre, viene misurato anche l\'angolo tra il 2o e il 3o punto e visualizzato nella vista report. Inserendo questo angolo nella casella **Angolo** all\'interno della sezione **Rotazione** si può ruotare con precisione l\'oggetto in modo tale che ora il secondo punto selezionato sia allineato con le coordinate occupate dal terzo punto selezionato . (Nota: per aumentare il numero di cifre utilizzate andare nel menu Modifica -\> Preferenze -\> Generale -\> Unità -\> Numero di decimali se si desidera maggiore precisione.)



## Esempi

Rotazione su un singolo asse:

<img alt="Before Rotation" src=images/RotationAboutZBefore.png  style="width:600px;"> Prima della Rotazione (top view) 

<img alt="After Rotation about Z" src=images/RotationAboutZAfter.png  style="width:600px;"> Dopo la rotazione attorno a Z (top view) 

<img alt="After Rotation about y=x" src=images/RotationAboutYXAfter.png  style="width:600px;"> Dopo la rotazione attorno a y=x (right view) 

Rotazione con punto centrale spostato:

<img alt="Before Rotation" src=images/RotationOffsetBefore.png  style="width:600px;"> Prima della Rotazione (top view) 

<img alt="After Rotation about Z" src=images/RotationOffsetAfter.png  style="width:600px;"> Dopo la rotazione attorno a Z (top view) 

Rotazione utilizzando gli angoli di Eulero:

<img alt="Before Rotation" src=images/RotationEulerBefore.png  style="width:600px;"> Prima della Rotazione 

<img alt="After Rotation" src=images/RotationEulerAfter.png  style="width:600px;"> Dopo la Rotazione 



## Posizionamento.Base vs Definizione Forma 

Placement non è l\'unico modo per posizionare una forma nello spazio. Notare la console Python in questa immagine:

![2 Forme con Stesso Placement](images/2Placements800.png ) 

Entrambi i cubi hanno lo stesso valore per il Placement, ma si trovano in luoghi diversi! Questo perché le due forme sono definite da differenti vertici (curve in forme complesse). Per le due forme della figura sopra:

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

I Vertici (o Vettori) che definiscono la forma utilizzano l\'attributo Placement.Base come origine. Quindi, se si vuole spostare una forma di 10 unità lungo l\'asse **X**, si può aggiungere 10 alle coordinate **X** di tutti i vertici oppure si può impostare Placement.Base su (10,0,0).



## Utilizzo del \"Centro\" per Controllare l\'Asse di Rotazione 

Per impostazione predefinita, l\'asse di rotazione non è effettivamente l\'asse x/y/z. Si tratta di una linea parallela all\'asse selezionato che passa per il punto definito da **Placement.Base** dell\'oggetto da ruotare. Questa impostazione può essere modificata utilizzando i campi **Centro** della finestra di dialogo **Posizionamento** oppure, negli script, utilizzando il parametro **Center** nella costruzione di **FreeCAD.Placement**.

Si supponga, ad esempio, di avere un cubo (figura sotto) posizionato in (20,20,10).

![Prima della rotazione](images/LocalZBefore2.png ) 

Volendo ruotare il cubo attorno al proprio asse verticale (l\'asse locale Z), mantenendolo nella stessa posizione. E\' possibile ottenere facilmente questo specificando nei campi Centro un valore corrispondente alle coordinate del punto centrale del cubo (25,25,15).

![Dopo la Rotazione](images/LocalZAfter2.png ) 

In uno script, faremmo:


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



## Utilizzo del Posizionamento nelle espressioni 

Nelle espressioni è possibile utilizzare le componenti del posizionamento, ad esempio per accedere al componente x dell\'oggetto etichettato \"Cubo\":


```python
<<Cube>>.Placement.Base.x
```

È possibile accedere all\'angolo di rotazione tramite


```python
<<Cube>>.Placement.Rotation.Angle
```

È possibile accedere all\'asse di rotazione con


```python
<<Cube>>.Placement.Rotation.Axis.x
<<Cube>>.Placement.Rotation.Axis.y
<<Cube>>.Placement.Rotation.Axis.z
```

dove spesso uno di questi valori è 1 mentre gli altri sono 0.

Sipuò anche utilizzare l\'intero Posizionamento in un\'unica espressione:

Fare clic con il pulsante destro del mouse sulla proprietà Posizionamento nell\'Editor delle Proprietà, selezionare \"mostra tutto\", quindi verranno visualizzate le proprietà aggiuntive. Se poi si fa nuovamente clic con il pulsante destro del mouse su Posizionamento, il menu contestuale includerà Espressione, selezionare Espressione, quindi si aprirà la finestra di dialogo Espressione e qualunque cosa viene digitata verrà inserita nella proprietà Posizionamento anziché nelle sue proprietà secondarie.

Per rendere il posizionamento di \"Schizzo\" uguale a quello di \"Cilindro\", si inserirebbe in questo modo per Schizzo l\'espressione


```python
<<Cube>>.Placement
```

![Impostazione dell\'intero Posizionamento in un\'unica espressione](images/PlacementInExpression.png ) 

**NOTA:** è anche possibile *creare* oggetti Placement nelle espressioni. Consultare la pagina [Expressioni](Expressions/it#Posizionamento.md) per i dettagli.



## Note

-   Le proprietà di Posizionamento nella scheda Dati sono disabilitate per gli oggetti associati a qualche altro oggetto. È pertanto necessario modificare l\'Offset dell\'oggetto associato.
-   Asse e angolo possono anche essere espressi come un [quaternione](http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation).
-   Il punto di riferimento di un oggetto varia a seconda dell\'oggetto. Alcuni esempi di oggetti comuni:

  Object                           Reference Point
   
  Part.Box                         left (minx), front (miny), bottom (minz) vertex
  Part.Sphere                      center of the sphere (ie centre of bounding box)
  Part.Cylinder                    center of the bottom face
  Part.Cone                        center of bottom face (or apex if bottom radius is 0)
  Part.Torus                       center of the torus
  Features derived from Sketches   the Feature inherits the Position of the underlying Sketch. Sketches always start with Position = (0,0,0). This position corresponds to the origin in the sketch.



## Per saperne di più 

-   Questo tutorial: [Aeroplano](Aereo/it.md) copre ampiamente i meccanismi di modifica del Posizionamento di un oggetto.
-   Questo [articolo di FreeCAD News](https://blog.freecad.org/2023/01/16/the-rotation-api-in-freecad/?preview_id=343) discute l\'API di rotazione.



---
⏵ [documentation index](../README.md) > Placement/it
