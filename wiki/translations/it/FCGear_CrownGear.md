---
 GuiCommand:
   Name: FCGear CrownGear
   Name/it: Corona dentata
   MenuLocation: Gear , Crown Gear
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: v0.16
   SeeAlso: FCGear_InvoluteGear/it
---

# FCGear CrownGear/it



## Descrizione

La ruota dentata ricorda una cremagliera curva a forma di anello. L\'angolo di pressione diminuisce continuamente dal diametro esterno a quello interno. In questo modo la velocità periferica variabile della corona dentata viene compensata con la velocità periferica costante del pignone. I denti esterni appuntiti e i fianchi ripidi del dente sul diametro interno limitano la larghezza utile del dente. Gli ingranaggi a corona raggiungono efficienze simili agli ingranaggi cilindrici. Una corona dentata può azionare più pignoni.

Campi di applicazione noti per le corone dentate:

-   Azionamenti dell\'asse posteriore per auto e moto
-   Meccanismo girevole per tavoli operatori
-   Teste per fresatura angolare
-   Sistemi di utensili motorizzati con pignoni multipli e corona dentata

![](images/Crown-Gear_example.png ) 
*Sopra: corona dentata*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_CrownGear.svg style="width:16px"> [Crown Gear](FCGear_CrownGear/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_CrownGear.svg style="width:16px"> Crown Gear** dal menu.
3.  Per default la corona dentata viene visualizzata senza denti. ({{Version/it|0.21}})
4.  Modificare i parametri dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).
5.  Impostare la proprietà **preview_mode** su {{false}} per visualizzare i denti (vedere [Note](#Note.md)).



## Proprietà

Un oggetto FCGear CrownGear deriva da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**: L\'impostazione predefinita è {{Value|4}}. Numero di profili utilizzati per il loft.

-    **preview_mode|Bool**: il valore predefinito è {{True}}.


{{Properties_Title|base}}

-    **height|Length**:L\'impostazione predefinita è {{Value|2 mm}}. Valore per la larghezza del dente.

-    **module|Length**: L\'impostazione predefinita è {{Value|1 mm}}. Il modulo è il rapporto tra il diametro di riferimento dell\'ingranaggio diviso per il numero di denti (vedere [Note](#Note.md)).

-    **other_teeth|Integer**: L\'impostazione predefinita è {{Value|15}}. Numero di denti dell\'ingranaggio da accoppiare (pignone) (vedere [Note](#Note.md)).

-    **teeth|Integer**: L\'impostazione predefinita è {{Value|15}}. Numero di denti.

-    **thickness|Length**: L\'impostazione predefinita è {{Value|5 mm}}. Altezza dalla punta del dente sul lato inferiore della corona dentata.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Il valore predefinito è {{Value|20 °}} (vedere [Note](#Note.md)).


{{Properties_Title|version}}

-    **version|String**:



## Note

-   La proprietà **preview_mode** è impostata su {{true}} per impostazione predefinita quando l\'ingranaggio viene creato apparirà questo messaggio nella visualizzazione del report:

    :   *Gear module: Crown gear created, preview_mode = true for improved performance. Set preview_mode property to false when ready to cut teeth.*

-    **modulo**: Utilizzando le linee guida ISO (Organizzazione internazionale per la standardizzazione), la dimensione del modulo è designata come l\'unità che rappresenta le dimensioni dei denti degli ingranaggi. Modulo (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Se si moltiplica il Modulo per Pi, si può ottenere la dimensione (p). Il passo è la distanza tra i punti corrispondenti sui denti adiacenti.

-    **other_teeth**: Su una corona dentata possono essere utilizzati più pignoni ma tutti con lo stesso numero di denti.

-    **pressure_parameter**: Modificare il parametro solo se si dispone di una conoscenza sufficiente della geometria dell\'ingranaggio.

-   La geometria della corona dentata è determinata principalmente dalla geometria del pignone cilindrico (**other_teeth**).

-   Creare un ingranaggio cilindrico con [Ingranaggio ad evolvente](FCGear_InvoluteGear/it.md). Il numero di denti deve essere identico al parametro **other_teeth** della corona dentata.

-   Le regolazioni per le caratteristiche di funzionamento ottimali possono essere effettuate con i parametri dell\'ingranaggio ad evolvente.



## Panoramica dell\'insieme corona e ingranaggio cilindrico 

![](images/Crown-spur-gear-set_example.png )

-   \(1\) Ingranaggio cilindrico
-   \(2\) Corona dentata
-   \(3\) Larghezza del dente
-   \(4\) Diametro interno
-   \(5\) Diametro esterno



## Formule utili 

-   **Inner diameter (4)**
    -   
        **diametro interno**
        
        = **modulo (ingranaggio cilindrico)** \* **denti (corona dentata)** \* **cos parametro_pressione (pignone)** : **cos parametro_pressione (corona dentata)**

-   **Outer diameter (5)**
    -   
        **diametro esterno**
        
        = **diametro interno** + **2x altezza (larghezza del dente della corona dentata)**



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CrownGear/it
