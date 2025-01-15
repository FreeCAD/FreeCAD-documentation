---
 GuiCommand:
   Name: FCGear InvoluteRack
   Name/it: Cremagliera
   MenuLocation: Gear , Involute Rack
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: v0.16
   SeeAlso: FCGear_InvoluteGear/it
---

# FCGear InvoluteRack/it



## Descrizione

Le cremagliere vengono utilizzate per convertire un movimento rotatorio in un movimento lineare o viceversa. I seguenti sono esempi di alcune applicazioni:

-   Una cremagliera con ingranaggio inserito in uno sbarramento di contenimento.
-   Vari sistemi a cremagliera di trasporto con ingranaggi.
-   Sterzo a pignone più cremagliera in un veicolo.
-   Verricello a pignone e cremagliera come paranco meccanico (ad es. cric per auto).
-   Azionamenti pneumatici a pignone e cremagliera utilizzati per controllare le valvole nelle tubazioni delle condotte.

![](images/Involute-Rack_example.png ) 
*Da sinistra a destra: ingranaggi cilindrici, ingranaggi elicoidali, ingranaggi elicoidali doppi*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_InvoluteRack.svg style="width:16px"> [Involute Rack](FCGear_InvoluteRack/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_InvoluteRack.svg style="width:16px"> Involute Rack** dal menu.
3.  Modificare il parametro dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).



## Proprietà

Un oggetto FCGear InvoluteRack deriva da un oggetto [Part Feature](Part_Feature/it.md) ed eredita tutte le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|base}}

-    **add_endings|Bool**: Se {{True}} (predefinito), la lunghezza totale della cremagliera è denti \* passo. Se {{False}}, la cremagliera inizia con un fianco dentellato.

-    **height|Length**: Il valore predefinito è {{Value|5 mm}}. Valore della larghezza dell\'ingranaggio.

-    **module|Length**: L\'impostazione predefinita è {{Value|1 mm}}. Il modulo è il rapporto tra il diametro di riferimento dell\'ingranaggio diviso per il numero di denti (vedere [Note](#Note.md)).

-    **teeth|Integer**: L\'impostazione predefinita è {{Value|15}}. Numero di denti.

-    **thickness|Length**: L\'impostazione predefinita è {{Value|5}}. Altezza del piede del dente dal piano inferiore della cremagliera.


{{Properties_Title|computed}}

-    **transverse_pitch|Length**: (sola lettura) Inclinazione nel piano trasversale (vedere [Note](#Note.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: L\'impostazione predefinita è {{Value|0 mm}}.

-    **root_fillet|Float**: L\'impostazione predefinita è {{Value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: L\'impostazione predefinita è {{Value|0 °}}. Con l\'angolo dell\'elica β viene creato un ingranaggio elicoidale -- valore positivo → senso di rotazione destra, valore negativo → senso di rotazione sinistra.

-    **double_helix|Bool**: L\'impostazione predefinita è {{False}}, {{True}} crea un ingranaggio a doppia elica (vedere [Note](#Note.md)).

-    **properties_from_tool|Bool**: L\'impostazione predefinita è {{False}}. Se {{True}} e **beta** non sono zero, i parametri dell\'ingranaggio vengono ricalcolati internamente per l\'ingranaggio ruotato.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Il valore predefinito è {{Value|20°}} (vedere [Note](#Note.md)).


{{Properties_Title|precision}}

-    **simplified|Bool**: L\'impostazione predefinita è {{False}}, {{True}} genera una visualizzazione semplificata (senza denti).


{{Properties_Title|tolerance}}

-    **clearance|Float**: Il valore predefinito è {{Value|0,25}} (vedere [Note](#Note.md)).

-    **head|Float**: L\'impostazione predefinita è {{Value|0}}. Questo valore viene utilizzato per modificare l\'altezza del dente.


{{Properties_Title|version}}

-    **version|String**:



## Note

-    **transverse_pitch**: Il valore è il risultato della moltiplicazione di **module * pi**. Ciò significa per la cremagliera evolvente standard di FCGear: 15 (**teeth**) \* 3,14 (**transverse_pitch**) è 47,12 mm. Vedere anche **module** più avanti.

-    **clearance**: In una coppia di ingranaggi, il gioco è la distanza tra la testa del dente del primo ingranaggio e il piede del dente del secondo ingranaggio.

-    **double_helix**: Per utilizzare la doppia dentatura elicoidale è necessario prima inserire l\'angolo dell\'elica β (**beta**) per la dentatura elicoidale.

-    **module**: Utilizzando le linee guida ISO (Organizzazione internazionale per la standardizzazione), la dimensione del modulo è designata come l\'unità che rappresenta le dimensioni dei denti degli ingranaggi. Modulo (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Se si moltiplica il Modulo per Pigreco, si può ottenere il Passo (p). Il passo è la distanza tra i punti corrispondenti sui denti adiacenti. Il risultato della moltiplicazione viene visualizzato in **transverse_pitch**

-    **pressure_parameter**: Modificare questo parametro solo se si dispone di una conoscenza sufficiente della geometria dell\'ingranaggio.



## Formule utili 

Vedere [FCGear: Ingranaggio ad evolvente](FCGear_InvoluteGear/it#Formule_utili.md).



## Script

Utilizzare la potenza di Python per automatizzare la modellazione degli ingranaggi: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteRack.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear InvoluteRack/it
