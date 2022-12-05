---
- GuiCommand:/it
   Name:Arch Structure
   Name/it:Struttura
   Workbenches:[Arch](Arch_Workbench/it.md)
   MenuLocation:Arch → Struttura
   Shortcut:**S** **T**
   SeeAlso:[Muro](Arch_Wall/it.md), [Armature](Arch_Rebar/it.md)
---

# Arch Structure/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **Struttura** permette di costruire elementi strutturali quali colonne o travi, specificando la loro larghezza, lunghezza e altezza, o derivandoli da un profilo 2D di base (faccia, contorno o schizzo).


</div>

Se non viene fornito alcun profilo, è disponibile una serie di modelli predefiniti per creare rapidamente un elemento strutturale da un profilo standard predefinito.

![](images/Arch_Structure_example.jpg ) 
*Colonna basata su un profilo di base 2D; una colonna e un raggio definiti dalla loro altezza, lunghezza e larghezza, senza un profilo di base; una struttura metallica basata su una faccia 2D*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare una forma 2D (oggetto di Draft, area o schizzo) (opzionale)
-   Premere il pulsante **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)
**, oppure premere i tasti **S** e poi **T**
-   Regolare le proprietà come desiderate


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Quando non è selezionato alcun oggetto 2D di base, lo strumento struttura ha 2 modalità di disegno: Colonna e Trave:
    -   In modalità colonna, viene chiesto di selezionare un punto sullo schermo o di immettere le sue coordinate. Il nuovo oggetto strutturale viene posizionato in quel punto.
    -   In modalità trave, viene chiesto di selezionare due punti sullo schermo o di immettere le loro coordinate. Il nuovo oggetto strutturale si estende tra questi due punti.
-   Gli elementi strutturali condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)
-   La lunghezza, la larghezza e l\'altezza di una struttura possono essere regolate dopo la creazione
-   Premere **Esc** o premere il pulsante **Cancella** per uscire dal comando attivo.
-   Facendo doppio clic sulla struttura nella vista ad albero dopo la sua creazione permette di accedere alla modalità di modifica e di accedere e modificare le sue addizioni e sottrazioni
-   In modalità di modifica, è anche possibile aggiungere un [sistema di assi](Arch_Axis/it.md) per l\'elemento strutturale. Quando si aggiunge un sistema di assi, l\'elemento strutturale viene copiato una volta su ciascun asse del sistema. Quando si aggiungono due sistemi assi, l\'elemento strutturale viene copiato una volta su ciascuna intersezione dei due sistemi.


</div>

## Proprietà

### Dati


<div class="mw-translate-fuzzy">

-    **Tool**: un percorso di estrusione opzionale, che può essere qualsiasi tipo di linea. Se questa proprietà è vuota, l\'estrusione è diritta e viene creata nella direzione indicata dalla proprietà Normal

-    **Normal**: specifica la direzione in cui la faccia di base di questa struttura è estrusa. Se questa proprietà viene mantenuta su (0,0,0), la direzione è automaticamente impostata sulla direzione normale della faccia di base.

-    **Face Maker**: specifica il tipo di algoritmo di generazione della faccia da utilizzare per creare il profilo. Le scelte sono None, Simple, Cheese e Bullseye.

-    **Length**: la lunghezza della struttura (utilizzata solo se non si basa su un profilo)

-    **Width**: la larghezza della struttura (utilizzata solo se non si basa su un profilo)

-    **Height**: l\'altezza della struttura (o la lunghezza di estrusione quando si basa su un profilo). Se l\'altezza non è data, e la struttura viene inserita in un oggetto [piano](Arch_Floor/it.md) la cui altezza è definita, la struttura assume automaticamente il valore dell\'altezza del piano.

-    **Nodes Offset**: un offset opzionale tra la linea centrale e la linea dei nodi


</div>

### Vista

-    **Nodes Type**: il tipo di nodi strutturali di questo oggetto, lineare o area.

-    **Show Nodes**: mostra o nasconde i nodi strutturali.

## Preset

Lo strumento Struttura dispone anche di una serie di preset che permettono di creare rapidamente dei profili metallici standard o degli elementi prefabbricati in calcestruzzo.

![](images/Arch_presets_example.jpg ) 
*Alcuni preset per strutture in acciaio*

Ai preset si accede scegliendo una **Categoria** dal pannello Opzioni struttura. Le categorie disponibili sono **Prefabbricato in cemento** o uno qualsiasi dei profili metallici standard del settore, come **HEA**, **HEB** o **INP**. Per ciascuna di queste categorie sono disponibili una serie di preset. Dopo aver scelto il preset, si possono regolare i singoli parametri quali **Lunghezza**, **Larghezza** o **Altezza** . Al contrario, per i profili metallici, le dimensioni del profilo sono definite dalla preimpostazione e non possono essere modificate.

Il pulsante **Switch L/H** può essere utilizzato per scambiare i valori lunghezza in altezza, e quindi costruire una trave orizzontale anziché una colonna verticale.

<img alt="" src=images/Arch_precast_example.jpg  style="width:960px;"> 
*Alcuni preset per strutture prefabbricate in calcestruzzo*

## Nodi strutturali 

Gli oggetti struttura hanno anche la possibilità di visualizzare i nodi strutturali. I nodi strutturali sono una sequenza di punti 3D memorizzati nella proprietà \"Nodes\". Commutando on/off la proprietà vista \"Show Nodes\", si possono vedere i nodi strutturali di un elemento struttura:

<img alt="" src=images/Arch_structural_nodes.jpg  style="width:960px;"> 
*Nodi strutturali resi visibili in un insieme di strutture*


<div class="mw-translate-fuzzy">

-   I nodi vengono calcolati e aggiornati automaticamente, a meno che non siano modificati manualmente. Se invece sono stati modificati manualmente, essi non sono più aggiornati automaticamente quando la forma dell\'oggetto strutturale cambia, a meno che in seguito non si utilizzi lo strumento \"Reset nodi\".
-   Oltre ai nodi lineari, le strutture Arch possono anche avere dei nodi planari. Per questo, 1- Ci devono essere almeno 3 vettori nella proprietà \"Nodi\" dell\'oggetto, 2- La proprietà \"NodesType\" del loro ViewObject deve essere impostata su \"Area\".
-   Quando il calcolo dei nodi è automatico (cioè, non sono stati modificati manualmente), e si imposta la proprietà Role di una struttura su \"Slab\" (Soletta), i suoi nodi diventano automaticamente nodi planari (ci sono almeno 3 vettori e il NodesType è impostato su \"Area\").
-   Quando si modifica un oggetto Struttura (con doppio clic), nella vista Azioni sono disponibili alcuni strumenti nodo per:
    -   Ripristinare il calcolo automatico dei nodi, nel caso in cui siano stati modificati manualmente
    -   Modificare i nodi graficamente, che funziona nello stesso modo di [Modifica di Draft](Draft_Edit/it.md)
    -   Prolungare i nodi dell\'oggetto modificato fino a toccare il nodo di un altro oggetto
    -   Rendere il nodo di un oggetto coincidente con quello di un altro oggetto
    -   Commutare on/off la visualizzazione di tutti i nodi di tutti gli oggetti strutturali del documento


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Struttura può può essere utilizzato nelle [macro](macros/it.md) e dalla [console Python](FreeCAD_Scripting_Basics/it.md) utilizzando la seguente funzione:


</div>


```python
Structure = makeStructure(baseobj=None, height=None)
Structure = makeStructure(baseobj=None, length=None, width=None, height=None, name="Structure")
```

-   Crea un oggetto `Struttura` dal `baseobj` dato, che è un profilo chiuso, e dalla `altezza` di estrusione data.
    -   Se non viene fornito un `baseobj`, si possono fornire i valori numerici per `length`, `width`, e `height` per creare una struttura a blocchi.
    -   Il `baseobj` può anche essere qualsiasi oggetto solido esistente.

Esempio: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(200, 300)
Structure1 = Arch.makeStructure(Rect, height=2000)
FreeCAD.ActiveDocument.recompute()

Structure2 = Arch.makeStructure(None, length=500, width=1000, height=3000)
Draft.move(Structure2, FreeCAD.Vector(2000, 0, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/it
|[Muro](Arch_Wall/it.md)
|[Armatura](Arch_CompRebarStraight/it.md)
|[Arch](Arch_Workbench/it.md)
|IconC=Workbench_Arch.svg
|IconL=Arch_Wall.svg
|IconR=Arch CompRebarStraight.png
}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Structure/it
