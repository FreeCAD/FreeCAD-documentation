---
 GuiCommand:
   Name: FCGear WormGear
   Name/it: Vite senza fine
   MenuLocation: Gear , Worm Gear
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: v0.16
   SeeAlso: PartDesign_InvoluteGear/it
---

# FCGear WormGear/it



## Descrizione

La vite senza fine può essere considerata un caso speciale di ingranaggio elicoidale. Si immagini che ci sia solo un dente su un ingranaggio cilindrico. Ora si supponga di aumentare l\'angolo dell\'elica in modo tale che il dente si avvolga più volte attorno all\'ingranaggio cilindrico prima di emergere dal lato opposto. Il risultato è la vite senza fine ad un principio.

Per una vite senza fine a principio singolo, ogni giro completo (360 gradi) della vite senza fine fa avanzare l\'ingranaggio di un dente. Quindi un ingranaggio con 24 denti fornirà una riduzione di 24:1. Per una vite senza fine a più principi, la riduzione dell\'ingranaggio è pari al numero di denti dell\'ingranaggio, diviso per il numero di principi della vite senza fine.

Una vite senza fine può essere utilizzata solo con una ruota elicoidale. Questo si chiama trasmissione a vite senza fine con ruota elicoidale. Come altre disposizioni di ingranaggi, una trasmissione a vite senza fine può ridurre la velocità di rotazione o trasmettere una coppia maggiore. Uno dei principali vantaggi delle unità di trasmissione a vite senza fine è che possono trasferire il movimento a 90 gradi. Anche la trasmissione a vite senza fine è autobloccante.

![](images/Worm-Gear_example.png ) 
*Vite senza fine (N° di denti 3)*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_WormGear.svg style="width:16px"> [Worm Gear](FCGear_WormGear/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_WormGear.svg style="width:16px"> Worm Gear** dal menu.
3.  Modificare il parametro dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).



## Proprietà

Un oggetto FCGear WormGear deriva da un oggetto [Part Feature](Part_Feature/IT.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|base}}

-    **diameter|Length**: Il valore predefinito è {{Value|5 mm}}. Diametro primitivo.

-    **height|Length**: Il valore predefinito è {{Value|5 mm}}. Valore della lunghezza della vite senza fine.

-    **module|Length**: L\'impostazione predefinita è {{Value|1 mm}}. Il modulo è il rapporto tra il diametro di riferimento dell\'ingranaggio diviso per il numero di denti (vedere [Note](#Note.md)).

-    **reverse_pitch|Bool**: L\'impostazione predefinita è {{False}}, {{True}} cambia la direzione di rotazione da destra a sinistra.

-    **teeth|Integer**: L\'impostazione predefinita è {{Value|3}}. Numero di denti (vedere [Note](#Note.md)).


{{Properties_Title|computed}}

-    **beta|Angle**: (sola lettura) Angolo di anticipo (vedere anche le informazioni in [Note](#Note.md) e [Formule utili](#Formule_utili.md)).


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Il valore predefinito è {{Value|20 °}} (vedere [Note](#Note.md)).


{{Properties_Title|tolerance}}

-    **clearance|Float**: Il valore predefinito è {{Value|0,25}} (vedere [Note](#Note.md)).

-    **head|Float**: L\'impostazione predefinita è {{Value|0}}. Questo valore viene utilizzato per modificare l\'altezza del dente.


{{Properties_Title|version}}

-    **version|String**:



## Note

-    **beta**: Se l\'angolo della vite è inferiore a 5° si tratta di un ingranaggio autobloccante. Un tipico esempio sono i piroli di una chitarra o di un ukulele.

-    **clearance**: In un ingranaggio a vite senza fine, il gioco è la distanza tra la punta del dente della vite senza fine e la radice del dente della ruota elicoidale.

-    **module**: Utilizzando le linee guida ISO (Organizzazione internazionale per la standardizzazione), la dimensione del modulo è designata come l\'unità che rappresenta le dimensioni dei denti degli ingranaggi. Modulo (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Se si moltiplica il Modulo per Pi, si può ottenere Lunghezza (p). Il passo è la distanza tra i punti corrispondenti sui denti adiacenti. Se si cambia il modulo, cambia anche l\'angolo della vite (**beta**).

-    **teeth**: Il numero di denti in una vite senza fine è chiamato numero di principi. Di conseguenza si parla di viti senza fine a un principio, a due o a multipli. In generale vengono prodotte principalmente viti senza fine ad un principio, ma in casi particolari il numero di principi può arrivare fino a quattro (a volte anche di più). Se si cambia il numero di principi, cambia anche **beta**.

-    **pressure_parameter**: Modificare il parametro solo se si dispone di una conoscenza sufficiente della geometria dell\'ingranaggio.



## Formule utili 

-    **beta (lead angle)**= arctan (**module** \* **teeth** : **pitchdiameter (diameter)**)

-    **axial pitch**= **pi** \* **module** \* **teeth**

-    **beta (lead angle)**= arctan (**axial pitch** : (**pitchdiameter (diameter)** \* **pi**))

-    **worm length**= 4,5 \* **module** \* **pi**



## Ruota elicoidale 

La ruota elicoidale deve essere progettata manualmente. A questo scopo [FCGear InvoluteGear](FCGear_InvoluteGear/it.md) può essere utilizzato per una costruzione semplice. In ogni caso è richiesta una conoscenza approfondita delle tipologie di ingranaggi.

![](images/Worm-Gear_example3.png ) 
*Vite senza fine con ruota elicoidale*



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear WormGear/it
