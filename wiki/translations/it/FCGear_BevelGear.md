---
 GuiCommand:
   Name: FCGear BevelGear
   Name/it: Ingranaggio conico
   MenuLocation: Gear , Bevel Gear
   Workbenches: FCGear_Workbench/it
   Version: v0.16
---

# FCGear BevelGear/it



## Descrizione

Lo strumento <img alt="" src=images/FCGear_BevelGear.svg  style="width:24px;"> [FCGear BevelGear](FCGear_BevelGear/it.md) crea un ingranaggio conico di base, un oggetto solido che deve essere modificato per ottenere la forma finale corretta nei passaggi seguenti.

In parte a causa del rumore che generano, gli ingranaggi conici non vengono utilizzati così spesso come altri tipi di ingranaggi. Ma vengono ancora utilizzati in alcuni settori, come gli imballaggi alimentari e le conserve, le attrezzature per prati e giardini, macchine come trapani e frese, sistemi di compressione per il settore del gas e del petrolio e valvole di controllo del flusso.

Gli ingranaggi conici a spirale hanno denti curvi per fornire un innesto più morbido e un maggiore contatto dente a dente rispetto a un ingranaggio conico dritto. Ciò riduce le vibrazioni e il rumore. Possono essere utilizzati a velocità elevate e sono generalmente utilizzati nelle trasmissioni di motociclette e biciclette.

![](images/Bevel-Gear_example.png ) 
*Da sinistra a destra: ingranaggio cilindrico, ingranaggio a spirale*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_BevelGear.svg style="width:16px"> [Bevel Gear](FCGear_BevelGear/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_BevelGear.svg style="width:16px"> Bevel Gear** dal menu.
3.  Viene creato un oggetto BevelGear in base alle impostazioni predefinite.
4.  Modificare il parametro dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).



## Proprietà

Vedere anche: l\'[Editor delle proprietà](Property_editor/it.md).

Un oggetto FCGear BevelGear deriva da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|base}}

-    **height|Length**: L\'impostazione predefinita è {{Value|5}}. Valore della larghezza dell\'ingranaggio conico, misurato dal cerchio primitivo.

-    **module|Length**: L\'impostazione predefinita è {{Value|1}}. Il modulo è il rapporto tra il diametro primitivo dell\'ingranaggio diviso per il numero di denti (vedere [Note](#Note.md)).

-    **reset_origin|Bool**: Se {{True}} (predefinito) l\'origine dell\'ingranaggio è al centro del cerchio primitivo (parte inferiore dell\'ingranaggio) (vedere [Note](#Note.md)).

    :   Se {{False}} l\'origine dell\'ingranaggio è all\'estremità del cono primitivo.

-    **teeth|Integer**: L\'impostazione predefinita è {{Value|15}}. Numero di denti.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (sola lettura)

-    **dw|Length**: (sola lettura) Diametro primitivo di lavoro.


{{Properties_Title|helical}}

-    **beta|Angle**: il valore predefinito è {{Value|0 °}}. Con l\'angolo dell\'elica β viene creato un ingranaggio conico elicoidale -- valore positivo → senso di rotazione destra, valore negativo → senso di rotazione sinistra.


{{Properties_Title|involute}}

-    **pitch_angle|Angle**: L\'impostazione predefinita è {{Value|45 °}}. Angolo di apertura del cono primitivo..


{{Properties_Title|involute_parameter}}

-    **pressure_angle|Angle**: Il valore predefinito è {{Value|20 °}} (vedere [Note](#Note.md)).


{{Properties_Title|precision}}

-    **numpoints|Integer**: L\'impostazione predefinita è {{Value|6}}. Modifica del profilo dell\'evolvente. La variazione del valore può portare a risultati imprevisti.


{{Properties_Title|tolerance}}

-    **backlash|Length**: L\'impostazione predefinita è {{Value|0}}. Il gioco, chiamato anche spazio o aria, è la distanza tra i denti di una coppia di ingranaggi.

-    **clearance|Float**: Il valore predefinito è {{Value|0.1}} (vedere [Note](#Note.md)).


{{Properties_Title|version}}

-    **version|String**:



## Note


<div class="mw-translate-fuzzy">

-    **clearance**: In una coppia di ingranaggi, il gioco è la distanza tra la testa del dente del primo ingranaggio e il piede del dente del secondo ingranaggio.

-    **module**: Utilizzando le linee guida ISO (Organizzazione internazionale per la standardizzazione), la dimensione del modulo è designata come l\'unità che rappresenta le dimensioni dei denti degli ingranaggi. Modulo (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Se si moltiplica il Modulo per Pi, si può ottenere la Lunghezza (p). Il passo è la distanza tra i punti corrispondenti sui denti adiacenti.

-    **reset_origin**: Può essere vantaggioso per scopi di montaggio che il parametro sia impostato su **false**. L\'origine del corpo è quindi all\'estremità del passo del cono.

-    **pressure_parameter**: Modificare il parametro solo se si dispone di una conoscenza sufficiente della geometria dell\'ingranaggio.


</div>



## Formule utili 


<div class="mw-translate-fuzzy">

-    **pitch diameter**= **module** \* **teeth**

-    **addendum diameter**= **pitch diameter** + 2 \* **module** \* **cos reference cone angle**

-    **tip angle 1**= **(teeth 1 + 2)** \* **(cos reference cone angle 1)** : **(teeth 2 - 2)** \* **(sin reference cone angle 1)**

-    **tip angle 2**= **(teeth 2 + 2)** \* **(cos reference cone angle 2)** : **(teeth 1 - 2)** \* **(sin reference cone angle 2)**

-    **reference cone angle 1**= **(teeth 1)** : **(teeth 2)**

-    **reference cone angle 2**= **(teeth 2)** : **(teeth 1)**

-    **axis angle total**= **reference cone angle 1** + **reference cone angle 2**


</div>

Angolo del cono di riferimento \[TECH.\]


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear BevelGear/it
