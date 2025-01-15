---
 GuiCommand:
   Name: FCGear CycloidGear
   Name/it: Ingranaggio cicloidale
   MenuLocation: Gear , Cycloid Gear
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: v0.16
   SeeAlso: FCGear_InvoluteGear/it
---

# FCGear CycloidGear/it



## Descrizione

Gli ingranaggi cicloidali sono molto sensibili agli errori nell\'interasse, che portano ad una variazione del rapporto di trasmissione. Per questi motivi gli ingranaggi cicloidali non si trovano quasi mai nell\'ingegneria meccanica, ma vengono utilizzati solo in casi speciali come nell\'industria orologiera, per le pompe a lobi o per l\'azionamento di cremagliere.

![](images/Cycloid-Gear_example_1.png ) 
*Da sinistra a destra: ingranaggio cilindrico, ingranaggio elicoidale, ingranaggio elicoidale doppio*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_CycloidGear.svg style="width:16px"> [Cycloid Gear](FCGear_CycloidGear/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_CycloidGear.svg style="width:16px"> Cycloid Gear** dal menu.
3.  Modificare il parametro dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).



## Proprietà



### Dati

Un oggetto FCGear CycloidGear deriva da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: L\'impostazione predefinita è {{Value|15}}. Diverso rispetto al profilo dell\'evolvente. La modifica del valore può portare a risultati imprevisti.


{{Properties_Title|base}}

-    **height|Length**: Il valore predefinito è {{Value|5 mm}}. Valore della larghezza dell\'ingranaggio.

-    **module|Length**: L\'impostazione predefinita è {{Value|1 mm}}. Il modulo è il rapporto tra il diametro di riferimento dell\'ingranaggio diviso per il numero di denti (vedere [Note](#Note.md)).

-    **teeth|Integer**: il valore predefinito è {{Value|15}}. Numero dei denti.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (sola lettura)

-    **dw|Length**: (sola lettura) Diametro primitivo di lavoro.


{{Properties_Title|cycloid}}

-    **inner_diameter|Float**: (sola lettura) Diametro del cerchio di rotolamento dell\'ipocicloide, normalizzato da **module** (vedere [Note](#Note.md)).

-    **outer_diameter|Float**: L\'impostazione predefinita è {{Value|7.5}}. Diametro del cerchio di rotolamento dell\'epicicloide, normalizzato da **module** (vedere [Note](#Note.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: L\'impostazione predefinita è {{Value|0 mm}}.

-    **root_fillet|Float**: L\'impostazione predefinita è {{Value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: L\'impostazione predefinita è {{Value|0 °}}. Con l\'angolo dell\'elica β viene creato un ingranaggio elicoidale -- valore positivo → senso di rotazione destra, valore negativo → senso di rotazione sinistra.

-    **double_helix|Bool**: Il valore predefinito è {{False}}, {{True}} crea un ingranaggio a doppia elica (vedere [Notes](#Notes.md)).


{{Properties_Title|tolerance}}

-    **backlash|Length**: L\'impostazione predefinita è {{Value|0}}. Il gioco, chiamato anche aria o margine, è la distanza tra i denti di una coppia di ingranaggi.

-    **clearance|Float**: Il valore predefinito è {{Value|0,25}} (vedere [Note](#Note.md)).

-    **head|Float**: L\'impostazione predefinita è {{Value|0}}. Lunghezza aggiuntiva della testa dei denti, normalizzata da **module**.


{{Properties_Title|version}}

-    **version|String**:



## Note

-   Gli ingranaggi cicloidali devono sempre essere abbinati in modo speciale tra loro e generalmente non possono essere scambiati a piacimento: in una coppia di ingranaggi, il valore di **inner_diameter** su un ingranaggio deve essere uguale a **outer_diameter** sull\'altro , e viceversa. Vedere anche le informazioni nella **rappresentazione dei parametri della cicloide** qui di seguito.

-    **clearance**: In una coppia di ingranaggi, il gioco è la distanza tra la punta del dente del primo ingranaggio e il piede del dente del secondo ingranaggio.

-    **double_helix**: Per utilizzare la doppia dentatura elicoidale è necessario prima inserire l\'angolo dell\'elica β (**beta**) per la dentatura elicoidale.

-    **module**: Secondo le linee guida ISO (Organizzazione internazionale per la standardizzazione), la dimensione del modulo è designata come l\'unità che rappresenta le dimensioni dei denti degli ingranaggi. Modulo (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Se si moltiplica il Modulo per Pi, si ottiene l\'Altezza (p). Il passo è la distanza tra i punti corrispondenti sui denti adiacenti.



## Casi particolari 



### La linea retta come ipocicloide 

Per ottenere una linea retta, diretta verso il centro, come ipocicloide, utilizzare la seguente [espressione](Expressions/ot.md) per **inner_diameter**: `teeth / 2`. Una tale forma del dente si trova spesso negli orologi storici e quindi viene chiamata \"dentatura dell\'orologio\". Un **clearance** maggiore rende l\'effetto ancora più visibile.



### Ipocicloide/epicicloide completo come dente 

Per ottenere un ingranaggio composto da curve ipocicloide ed epicicloide complete utilizzare le seguenti [espressioni](Expressions/it.md):

-    **inner_diameter**: `0.5 + 1e-6`

-    **outer_diameter**: `inner_diameter`

-    **clearance**: `(-1 + inner_diameter/1mm) * 2`

-    **head**: `(-1 + outer_diameter/1mm) * 2`

Il diametro di riferimento è *d = m \* z*, dove *m* è **module** e *z* è **teeth**. Per un ipocicloide completo, il diametro di rotolamento deve essere *d_i = d / (z\*2) = m\*z / (z\*2)*. E se ora lo normalizziamo con il modulo, otteniamo *d_in = m\*z / (z\*2) / m = 1 / 2*. Il valore di tolleranza esplicito aggiuntivo (`1e-6` nell\'espressione sopra) è necessario per superare i problemi di coincidenza.

Ora i diametri dei cerchi di rotolamento delle cicloidi devono corrispondere all\'addendum/dedendum dell\'ingranaggio. L\'addendum, cioè la lunghezza del dente sopra il cerchio di riferimento, è 1 + **head**. Il dedendum, cioè la lunghezza del dente sotto il cerchio di riferimento, è 1 + **clearance**. Entrambi sono normalizzati dal modulo, quindi abbiamo bisogno di un valore di prevalenza/gioco di *1 - d_in*. L\'ulteriore ` / 1mm` e ` *2` sono necessari per superare i difetti già risolti nella versione di sviluppo di FCGear Workbench, ma riportare tali correzioni alla versione stabile potrebbe danneggiare i modelli esistenti.

Tali \"ingranaggi\" consentono il numero di denti fino a \"due\" e vengono utilizzati come palette rotanti nelle pompe o nei compressori (cfr. [Roots -tipo Supercharger](https://en.wikipedia.org/wiki/Roots-type_supercharger)).



### Epicicloide infinitamente grande 

Se il raggio del cerchio di rotolamento dell\'epicicloide diventa infinitamente grande, diventa una linea retta rotante. Un epicicloide così degenerato si chiama evolvente. Gli ingranaggi con questa forma del dente vengono gestiti dal comando [involute gear](FCGear_InvoluteGear/it.md). È di gran lunga la forma di dentatura più comune ad oggi.



## Formule utili 

Vedere [Formule_utili](FCGear_InvoluteGear/it#Formule_utili.md).



## Rappresentazione dei parametri della cicloide 

<img alt="" src=images/CycloidGear_inner-outer-diameter_2.svg  style="width:400px;">



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear CycloidGear/it
