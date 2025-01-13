---
 GuiCommand:
   Name: Arch Wall
   Name/it: Muro
   MenuLocation: Architettura , Muro
   Workbenches: Arch_Workbench/it
   Shortcut: **W** **A**
   SeeAlso: Arch_Structure/it
---

# Arch Wall/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento crea un oggetto Muro utilizzando come base una [forma](Part_Workbench/it.md) o oggetto [mesh](Mesh_Workbench/it.md). Un muro può essere costruito anche senza alcun oggetto di base, nel qual caso si comporta come un *volume cubico*, utilizzando le proprietà lunghezza, larghezza e altezza. Quando è costruito usando una forma esistente, un muro può essere basato su:


</div>

-   Un **oggetto lineare 2D**, come ad esempio una linea, un arco, una spezzata o uno schizzo, in questo caso è possibile modificarne lo spessore, l\'allineamento (a destra, a sinistra o al centro) e l\'altezza. La proprietà length non ha alcun effetto.
-   Una **faccia** o una superficie piana, nel qual caso si può modificare solo l\'altezza. Le proprietà Lunghezza e larghezza non hanno alcun effetto. Se la faccia di base è verticale, invece, il muro utilizza la proprietà larghezza invece di altezza, e consente di costruire pareti usando lo spazio come oggetto o studi della massa.
-   Un **solido**, nel qual caso non è possibile cambiare nulla. Il muro utilizza semplicemente il solido base come sua forma.
-   Un **mesh**, nel qual caso il mesh deve essere un solido chiuso, cioè un solido manifold.

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Pareti costruite su un segmento, su una spezzata, su una faccia, su un solido e su uno schizzo.*

Agli oggetti Muro si possono anche applicare *Aggiunte* o *Sottrazioni*. Le Aggiunte sono altri oggetti le cui forme sono unite alla forma Muro in lavorazione, mentre le Sottrazioni sono forme che vengono eliminate.

Le Aggiunte e le Sottrazioni si eseguono con gli strumenti [Aggiungi componente](Arch_Add/it.md) e [Rimuovi componente](Arch_Remove/it.md). Le Aggiunte e le Rimozioni non hanno alcuna influenza sui parametri del muro, tipo altezza e larghezza, che possono ancora essere modificati.

I muri possono anche avere l\'altezza automatica, se sono incluse in un oggetto di livello superiore, tipo il [Piano](Arch_Floor/it.md). L\'altezza deve essere impostata a 0, così il muro adotta l\'altezza specificata per l\'oggetto genitore.

Quando più muri devono essere intersecati, è necessario inserirli in un [piano](Arch_Floor/it.md) per ottenere la loro geometria intersecata.



## Utilizzo



### Disegnare un muro dall\'inizio 


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Arch_Wall.svg" width=16px> [Muro](Arch_Wall/it.md)**, oppure premere i tasti **W** e poi **A**.
2.  Definire un primo punto nella vista 3D, o digitare le sue coordinate.
3.  Definire un secondo punto nella vista 3D, o digitare le sue coordinate.


</div>



### Disegnare un muro su un oggetto selezionato 


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti per la geometria di base (oggetti Draft, schizzi, etc)
2.  Premere il pulsante **<img src="images/Arch_Wall.svg" width=16px> [Muro](Arch_Wall/it.md)
**, oppure premere i tasti **W** e poi **A**
3.  Regolare, se necessario, le proprietà, come altezza o larghezza.


</div>



## Opzioni

-   Gli elementi Muro condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)
-   L\'altezza, la larghezza e l\'allineamento di un muro può essere impostato durante il disegno, tramite il pannello delle Azioni.
-   Quando aggancia una parete di una parete esistente, entrambe le pareti si uniscono in una sola. Il modo in cui sono unite le due pareti dipende dalle loro proprietà. Se hanno la stessa larghezza, altezza e orientamento, la parete risultante sarà un oggetto basato su uno schizzo composto da più segmenti. Altrimenti, l\'ultima parete verrà unita alla prima come oggetto aggiunta.
-   Premere **X**, **Y** o **Z** dopo il primo punto per vincolare il secondo punto su un dato asse.
-   Per inserire le coordinate manualmente, è sufficiente inserire il valore, quindi premere **Invio** tra ogni componente X, Y e Z .
-   Premere **R** oppure fare clic sulla casella di controllo per selezionare o deselezionare la modalità **Relativo**. In modalità Relativo, le coordinate del secondo punto sono relative al primo. In caso contrario sono assolute, a partire dal punto di origine (0,0,0).
-   Premere **Maiusc** mentre si disegna per [vincolare](Draft_Constrain/it.md) orizzontalmente o verticalmente il secondo punto rispetto al primo.
-   Premere **Esc** o premere il pulsante **Cancella** per uscire dal comando attivo.
-   Facendo doppio clic sul muro nella vista ad albero dopo la sua creazione si attiva la modalità di modifica che permette di accedere alle sue addizioni e sottrazioni e di modificarle .
-   I muri multistrato possono essere facilmente creati costruendo diversi muri sulla stessa linea base. Impostando la proprietà Align a destra o a sinistra e specificando un valore di offset, si possono costruire efficacemente i diversi strati della parete. Inserendo una finestra in uno degli strati della parete l\'apertura si propaga in tutti gli strati della parete creati con la stessa linea base.
-   I muri possono anche utilizzare i [ Multi-Materiali](Arch_MultiMaterial/it.md). Quando si utilizza un multi-materiale, la parete diventa multistrato, utilizzando gli spessori specificati nel multi-materiale. A qualsiasi strato con uno spessore pari a zero viene assegnato lo spessore definito automaticamente dallo spazio rimanente definito dal valore Width della parete meno gli altri strati.
-   I muri possono essere fatti per mostrare blocchi, invece di un singolo solido, attivando la proprietà **Make Blocks**. La dimensione e l\'offset dei blocchi possono essere configurati con proprietà diverse e la quantità di blocchi viene calcolata automaticamente.



## Aggancio

Con i muri dell\'ambiente Arch l\'aggancio funziona un po\' diversamente da come funziona con gli altri oggetti di Arch e di Draft. Quando un muro è basato su un oggetto l\'aggancio crea un ancoraggio all\'oggetto base, e non alla geometria muro, consentendo di allineare facilmente i muri tramite le loro linee base. Quando invece si desidera agganciare la geometria muro, premere **Ctrl** per trasferire l\'ancoraggio all\'oggetto muro.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Seconda parete che si collega perpendicolarmente alla prima*



## Proprietà

Gli oggetti muro ereditano le proprietà degli oggetti [Part](Part_Workbench/it.md) e hanno anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Blocks}}

-    {{PropertyData/it|Block Height}}: L\'altezza di ogni blocco.

-    {{PropertyData/it|Block Length}}: La lunghezza di ogni blocco.

-    {{PropertyData/it|Count Broken}}: Il numero di blocchi interrotti (sola lettura).

-    {{PropertyData/it|Count Entire}}: Il numero di blocchi interi (sola lettura).

-    {{PropertyData/it|Joint}}: La dimensione delle giunzioni tra ogni blocco, lo spazio vuoto tra i blocchi.

-    {{PropertyData/it|Make Blocks}}: Abilita la generazione dei blocchi.

-    {{PropertyData/it|Offset First}}:L\'offset orizzontale della prima fila e di ogni fila irregolare di blocchi.

-    {{PropertyData/it|Offset Second}}: L\'offset orizzontale della seconda fila e di ogni fila pari di blocchi.


{{TitleProperty|Componente}}

Vedere [Arch: Componente](Arch_Component/it#Proprietà.md).


{{TitleProperty|IFC}}

Vedere [Arch: Componente](Arch_Component/it#Proprietà.md).


{{TitleProperty|IFC Attributes}}

Vedere [Arch: Componente](Arch_Component/it#Proprietà.md).


{{TitleProperty|Muro}}


<div class="mw-translate-fuzzy">

-    **Align**: L\'allineamento del muro sulla sua linea di base: a sinistra, a destra o al centro.

-    **Area**: Area della parte interna del muro, la suddivisione in blocchi non fa alcuna differenza (sola lettura).

-    **Face**: L\'indice della faccia dell\'oggetto base da usare. Se il valore non è impostato o è 0, viene utilizzato l\'intero oggetto

-    **Height**: Ignorato se il muro è basato su un solido. Se impostato a zero, e il muro è all\'interno di un oggetto [piano](Arch_Floor/it.md) con la sua altezza definita, il muro assumerà automaticamente il valore dell\'altezza del pavimento.

-    **Length**: La lunghezza del muro (non utilizzato quando il muro è basato su un oggetto)

-    **Normal**: La direzione di estrusione per il muro. Se è impostata a (0,0,0), la direzione di estrusione è automatica.

-    **Offset**: La distanza tra il muro e la sua linea base. Funziona solo se la proprietà **Align** è impostata a destra o a sinistra.

-    **Override Align**:

-    **Override Width**: sovrascrive l\'attributo **Width** per impostare la larghezza di ciascun segmento di un muro. Ignorato se l\'oggetto **Base** fornisce informazioni sulla larghezza con il metodo {{Incode|getWidths()}}. Il primo valore sovrascrive **Width** per il primo segmento di muro, questo valore viene utilizzato anche al posto di qualsiasi valore zero nel resto dell\'elenco.

-    **Width**: La larghezza del muro. Ignorato se il muro è basato su una faccia o su un solido.


</div>

<img alt="" src=images/Sketch_vs_Wall.jpg  style="width:480px;">

## Scripting


**Vedere anche:**

[API Arch](Arch_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Muro può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Crea un oggetto `Wall` dal `baseobj` dato, che può essere un [oggetto Draft](Draft_Workbench/it.md), uno [Schizzo](Sketcher_Workbench/it.md), una faccia, o un solido.
    -   Se non viene dato un `baseobj`, si posssono fornire i valori numerici per `length`, `width` (thickness), e `height`.
    -   Se `face` è data, essa può essere usata per dare l\'indice della faccia a partire dall\'oggetto sottostante, invece di usare l\'intero oggetto per costruire il muro.

-    `align`può essere `"Center"`, `"Left"` o `"Right"`.

-   Se l\'operazione fallisce restituisce `None`.

Esempio:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Wall/it
