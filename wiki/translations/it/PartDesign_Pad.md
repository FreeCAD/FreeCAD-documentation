---
- GuiCommand:
   Name: PartDesign Pad
   Name/it: PartDesign Estrusione
   MenuLocation: Part Design - Crea una funzione additiva - Estrusione
   Workbenches: [PartDesign](PartDesign_Workbench/it.md)
   SeeAlso: [PartDesign Tasca](PartDesign_Pocket/it.md)
---

# PartDesign Pad/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Estrusione](PartDesign_Pad/it.md)** crea uno solido da uno schizzo in una direzione normale al piano dello stesso. A partire dalla {{VersionPlus/it|0.17}}, è possibile utilizzare anche le facce di un solido.


</div>

![](images/PartDesign_Pad_example.svg )

*A sinistra è mostrato lo Schizzo (A); a destra il risultato finale dopo l\'operazione di estrusione (B).*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare lo schizzo da estrudere, a cui applicare l\'operazione di estrusione. In {{VersionPlus/it|0.17}} , come alternativa, può essere usata una faccia di un solido esistente.
2.  Premere il pulsante **<img src="images/PartDesign_Pad.svg" width=16px> '''Estrusione'''**.
3.  Impostare i parametri di estrusione, vedi le [opzioni](#Opzioni.md) qui sotto.
4.  Cliccare su **OK**.


</div>

When selecting a single sketch, it can have multiple enclosed profiles inside a larger one, for example a rectangle with two circles inside it. But the profiles may not intersect each other. <small>(v0.20)</small> 



## Opzioni


<div class="mw-translate-fuzzy">

Quando si crea un estrusione, la vista combinata passa automaticamente al riquadro delle attività, mostrando la finestra di dialogo **Parametri Prisma**.


</div>

![](images/pad_parameters_cropped_it.png )



### Tipo


<div class="mw-translate-fuzzy">

Tipo offre cinque diversi modi per specificare la lunghezza a cui il prisma sarà estruso.


</div>



#### Quota


<div class="mw-translate-fuzzy">

Inserire un valore numerico per la lunghezza dell\'estrusione. La direzione predefinita per l\'estrusione è rivolta verso l\'esterno del supporto, ma può essere invertita contrassegnando l\'opzione **Invertita**. Le estrusioni sono realizzate [normali](http://en.wikipedia.org/wiki/Surface_normal) al piano dello schizzo. Con l\'opzione **Simmetrica al piano** il solido viene esteso per metà della lunghezza data su entrambi i lati dal piano dello schizzo. Le dimensioni negative non sono possibili. In sostituzione utilizzare l\'opzione **Invertita**.


</div>



#### Fino all\'ultimo 

Il solido viene estruso fino all\'ultima faccia del supporto nella direzione di estrusione. Se non vi è alcun supporto, viene visualizzato un messaggio di errore.



#### Fino al primo 

Il solido viene estruso fino alla prima faccia del supporto nella direzione di estrusione. Se non vi è alcun supporto, viene visualizzato un messaggio di errore.



#### Fino alla faccia 


<div class="mw-translate-fuzzy">

Il solido verrà estruso fino a una faccia del supporto che può essere scelta cliccando su di essa. Se non c\'è un supporto, nessuna selezione sarà accettata.


</div>



#### Due dimensioni 


<div class="mw-translate-fuzzy">

Questo consente di inserire una seconda lunghezza per estendere l\'estrusione in direzioni opposte (nel supporto). Anche in questo caso la direzione può essere modificata barrando l\'opzione **Invertita**.


</div>



### Quota 


<div class="mw-translate-fuzzy">

Definisce la lunghezza dell\'estrusione. Si possono utilizzare diverse unità di misura, indipendentemente dalle unità definite nelle preferenze dell\'utente (m, cm, mm, nm, ft o \', in o \").


</div>



### Offset dalla faccia 


<div class="mw-translate-fuzzy">

Offset dalla faccia in cui terminerà l\'estrusione. Questa opzione è disponibile solo quando **Tipo** è **Fino all\'ultimo**, **Fino al primo** o **Fino alla faccia**.


</div>

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Sketch normal:** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...:** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion. <small>(v0.20)</small> 
-   **Custom direction:** The sketch is extruded along a direction that can be specified via vector values.




<div class="mw-translate-fuzzy">

### Utilizzare una direzione personalizzata 


</div>


<div class="mw-translate-fuzzy">


<small>(v0.19)</small> 

Se spuntato, la direzione del prisma non sarà il vettore normale dello schizzo ma il vettore dato. La lunghezza dell\'estrusione è comunque impostata secondo la direzione del vettore normale.


</div>




<div class="mw-translate-fuzzy">

### Lunghezza lungo la normale del disegno 


</div>

Se selezionata, la lunghezza del prisma è misurata lungo la normale dello schizzo, altrimenti lungo la direzione personalizzata. {{Version/it|0.20}}



### Simmetrica al piano 


<div class="mw-translate-fuzzy">

Estende la lunghezza data su entrambi i lati del piano di schizzo, simmetricamente al piano dello schizzo, metà per parte.


</div>



### Invertita

Inverte la direzione dell\'estrusione.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations:

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pad would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pad in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pad in the opposite extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.



## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Tipo}}: modalità in cui il solido sarà estruso, vedi [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Lunghezza}}: definisce la lunghezza del\'estrusione, vedi [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Seconda lunghezza}}: seconda lunghezza del solido nel caso in cui è usata l\'opzione {{PropertyData/it|Tipo}} **Due dimensioni**, vedi [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Usa direzione personalizzata}}: {{Version/it|0.19}} se spuntato, la direzione dell\'estrusione non sarà il vettore normale dello schizzo ma il vettore dato, vedi [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Direzione}}: {{Version/it|0.19}} vettore direzione se si usa {{PropertyData/it|Usa direzione personalizzata}}.

-    {{PropertyData/it|Lungo la normale dello schizzo}}: {{Version/it|0.20}} se *vero*, la lunghezza del solido è misurata lungo la normale dello schizzo. Altrimenti e se è selezionato {{PropertyData/it|Usa direzione personalizzata}} la lunghezza è misurata lungo la direzione personalizzata.

-    {{PropertyData/it|Fino alla faccia}}: Una faccia su cui il solido si estruderà, vedi [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Offset}}: Offset dalla faccia in cui finirà il solido. Questo viene preso in considerazione solo se l\'opzione {{PropertyData/it|Tipo}} usata è **Fino all\'ultimo**, **Fino al primo** o **Fino alla faccia**.

-    {{PropertyData/it|Affina}}: {{VersionPlus/it|0.17}} vero o falso. Pulisce i bordi residui rimasti dopo l\'operazione. Questa proprietà viene inizialmente impostata in base alle impostazioni dell\'utente (disponibile in \"Preferenze → Part Design → Generale → Impostazioni del modello\"). In seguito può essere modificata manualmente. Questa proprietà viene salvata con il documento di FreeCAD.


</div>



## Limitazioni


<div class="mw-translate-fuzzy">

-   Come tutte le funzioni di Part Design, Estrusione crea un solido, quindi lo schizzo deve includere un profilo chiuso o l\'operazione fallisce con un errore *Impossibile convalidare la faccia guasta*. Possono esserci più profili racchiusi all\'interno di uno più grande, a condizione che nessuno si intersechi l\'un l\'altro (ad esempio, un rettangolo con due cerchi al suo interno).
-   L\'algoritmo utilizzato per **Fino al primo** e **Fino all\'ultimo** è:
    -   Creare una linea attraverso il centro di gravità del disegno
    -   Trovare tutte le facce del supporto attraversate da questa linea
    -   Scegliere la faccia in cui il punto di intersezione è più vicino o più lontano dal disegno

:   Questo significa che la faccia trovata potrebbe anche non essere quella attesa. Se succede questo, utilizzare il tipo **Fino alla faccia** e scegliere la faccia desiderata.
:   Nel caso speciale di estrusione di una superficie concava, in cui il disegno è più grande di questa superficie, l\'estrusione fallisce. Questo è un bug irrisolto

-    {{VersionMinus/it|0.16}}Non c\'è la pulizia automatica, ad esempio di superfici planari adiacenti in una singola superficie. È possibile risolvere questo manualmente nell\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Parte](Part_Workbench/it.md) con **<img src="images/Part_RefineShape.svg" width=16px> [Affina una forma](Part_RefineShape/it.md)** (che crea un solido non collegato, e non parametrico) o con **<img src="images/OpenSCAD_RefineShapeFeature.svg" width=16px> [Affina forma](OpenSCAD_RefineShapeFeature/it.md)** di <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:16px;"> [OpenSCAD](OpenSCAD_Workbench/it.md) che crea una funzione parametrica.


</div>





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/it
