---
 GuiCommand:
   Name: FCGear InternalInvoluteGear
   Name/it: Ingranaggio ad evolvente interno
   MenuLocation: Gear , Internal Involute Gear
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: 1.0
   SeeAlso: FCGear_InvoluteGear/it
---

# FCGear InternalInvoluteGear/it



## Descrizione

<img alt="" src=images/FCGear_InternalInvoluteGear-01.png  style="width:300px;">



*Ingranaggi ad evolventi interni da sinistra a destra: ingranaggi cilindrici, ingranaggi elicoidali, ingranaggi elicoidali doppi*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> [Internal Involute Gear](FCGear_InternalInvoluteGear/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> Internal Involute Gear** dal menu.
3.  Modificare il parametro dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).



## Proprietà

Un oggetto FCGear InternalInvoluteGear deriva da un oggetto [Part Feature](Part_Feature/it.md) ed eredita tutte le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: Il valore predefinito è {{value|6}}. Modifica del profilo dell\'evolvente. La modifica del valore può portare a risultati imprevisti.


{{Properties_Title|base}}

-    **height|Length**: Il valore predefinito è {{value|5 mm}}. Valore della larghezza dell\'ingranaggio.

-    **module|Length**: Il valore predefinito è {{value|1 mm}}. Il modulo è il rapporto tra il diametro primitivo dell\'ingranaggio diviso per il numero di denti (vedere [Note](FCGear_InvoluteGear/it#Note.md)).

-    **teeth|Integer**: Il valore predefinito è {{value|15}}. Numero di denti (vedere [Note](FCGear_InvoluteGear/it#Note.md)).

-    **thickness|Length**: Il valore predefinito è {{value|5 mm}}. Spessore della parte esterna non tagliata dell\'ingranaggio.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (sola lettura)

-    **da|Length**: (sola lettura) Diametro interno, misurato all\'addendum (la testa dei denti).

-    **df|Length**: (sola lettura) Diametro di fondo, misurato al piede dei denti.

-    **dw|Length**: (sola lettura) Diametro primitivo di lavoro.

-    **outside_diameter|Length**: (sola lettura) Diametro esterno.

-    **transverse_pitch|Length**: (sola lettura) Passo nel piano di rotazione.


{{Properties_Title|fillets}}

-    **head_fillet|Float**: Il valore predefinito è {{value|0 mm}}.

-    **root_fillet|Float**: Il valore predefinito è {{value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: L\'impostazione predefinita è {{value|0 °}}. Con l\'angolo dell\'elica β viene creato un ingranaggio elicoidale -- valore positivo → senso di rotazione destra, valore negativo → senso di rotazione sinistra (vedere [Note](FCGear_InvoluteGear/it#Note.md)).

-    **double_helix|Bool**: L\'impostazione predefinita è {{false}}, {{true}} crea un ingranaggio a doppia elica (vedere [Note](FCGear_InvoluteGear/it#Note.md)).

-    **properties_from_tool|Bool**: L\'impostazione predefinita è {{false}}. Se {{true}} e **beta** non è zero, i parametri dell\'ingranaggio vengono ricalcolati internamente per l\'ingranaggio ruotato.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Il valore predefinito è {{value|20 °}} (vedere [Note](FCGear_InvoluteGear/it#Note.md)).

-    **shift|Float**: Il valore predefinito è {{value|0}}. Genera uno spostamento del profilo positivo o negativo (vedere [Note](FCGear_InvoluteGear/it#Note.md)).


{{Properties_Title|precision}}

-    **simple|Bool**: Il valore predefinito è {{false}}, {{true}} genera una visualizzazione semplificata (senza denti e col solo cilindro del diametro primitivo).


{{Properties_Title|tolerance}}

-    **backlash|Length**: Il valore predefinito è {{value|0 mm}}. Il gioco, chiamato anche aria o spazio, è la distanza tra i denti di una coppia di ingranaggi.

-    **clearance|Float**: Il valore predefinito è {{value|0.25}} (vedere [Note](FCGear_InvoluteGear/it#Note.md)).

-    **head|Float**: il valore predefinito è {{value|-0,4 mm}}. Questo valore viene utilizzato per modificare l\'altezza del dente.

-    **reversed_backlash|Bool**: {{true}} diminuzione del gioco o {{false}} (predefinito) aumento del gioco (vedere [Note](FCGear_InvoluteGear/it#Note.md)).


{{Properties_Title|version}}

-    **version|String**:



## Note

Vedere [Ingranaggio ad evolvente esterno](FCGear_InvoluteGear/it#Note.md).



## Formule utili 

Vedere [Ingranaggio ad evolvente esterno](FCGear_InvoluteGear/it#Useful_formulas.md).



## Script



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear InternalInvoluteGear/it
