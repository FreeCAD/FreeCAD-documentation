---
 GuiCommand:
   Name: FCGear TimingGear
   Name/it: Puleggia per cinghia dentata
   MenuLocation: Gear , Timing Gear
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: v0.16
   SeeAlso: 
---

# FCGear TimingGear/it



## Descrizione

Lo scopo degli ingranaggi di distribuzione è quello di consentire all\'albero a camme e all\'albero motore di far ruotare la catena di distribuzione. L\'albero motore gira per muovere i pistoni su e giù all\'interno dei cilindri. L\'albero a camme ruota per consentire l\'apertura e la chiusura delle valvole di aspirazione e di scarico sui cilindri. Questi componenti sono importanti per la corretta sincronizzazione del motore.

Gli ingranaggi di distribuzione sono collegati a una cinghia o catena di distribuzione.

![](images/Timing-Gear_example.png ) 
*Sopra: puleggia per cinghia dentata*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_TimingGear.svg style="width:16px"> [Timing Gear](FCGear_TimingGear/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_TimingGear.svg style="width:16px"> Timing Gear** dal menu.
3.  Modificare il parametro dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).



## Proprietà

Un oggetto FCGear TimingGear deriva da un oggetto [Part Feature](Part_Feature/it.md) ed eredita tutte le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|base}}

-    **height|Length**: Il valore predefinito è {{Value|5 mm}}. Valore della larghezza dell\'ingranaggio.

-    **teeth|Integer**: L\'impostazione predefinita è {{Value|15}}. Numero di denti.

-    **type|Enumeration**: L\'impostazione predefinita è {{Value|gt2}}. Tipo di ingranaggio -- passo del profilo per cinghie di distribuzione (vedere [Note](#Note.md)).


{{Properties_Title|computed}}

-    **h|Length**: (sola lettura) Altezza radiale dei denti.

-    **offset|Length**: (sola lettura) Offset X del punto medio del secondo arco.

-    **pitch|Length**: (sola lettura) Passo dell\'ingranaggio.

-    **r0|Length**: (sola lettura) Raggio del primo arco.

-    **r1|Length**: (sola lettura) Raggio del secondo arco.

-    **rs|Length**: (sola lettura) Raggio del terzo arco.

-    **u|Length**: (sola lettura) Differenza radiale tra passo... diametro e testa dell\'ingranaggio.


{{Properties_Title|version}}

-    **version|String**:



## Note

-    **type**: Il passo delle cinghie dentate (distanza dal centro del dente al centro del dente di denti consecutivi) è specificato in tipi. GT2 ha un passo di 2 mm, GT3 di 3 mm, GT5 di 5 mm ecc..



## Formule utili 

-    **addendum diameter**= **pitch diameter** + 2 \* **module**

-    **belt length**= 2 \* **axle base** + **belt tooth pitch** : 2 \* **(teeth 1 + 2)** + **belt tooth pitch²** : 4 \* pi² \* **axle base** \* **(teeth 1 - 2)²**

-    **axle base**= **belt length** : 4 - **belt tooth pitch** : 8 \* **(teeth 1+2)** + ¼ \* sqrt \[**belt length** - ½ \* **belt tooth pitch** \* **(teeth 1+2)²** - 2 \* **belt tooth pitch²** \* **(teeth 1+2)²** : pi²\]



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear TimingGear/it
