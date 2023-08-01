# Part Extrude/it
---
- GuiCommand:   Name: Part_Extrude   Name/it: Estrusione   MenuLocation: Parte - Estrudi...   Workbenches: [SeeAlso: [[Draft Trimex/it|Tronca o estendi](Part_Workbench/it___Parte]].md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

**Estrusione** dell\'ambiente Parte estende una forma per una determinata distanza e in una direzione specifica. Il tipo di forma prodotta varia a seconda del tipo di forma in input e le opzioni selezionate.


</div>

Di solito, secondo il tipo di forma in ingresso, si ottiene le seguente forma:

-   Estrudere un Vertex (punto), produce un Edge (Linea)
-   Estrudere una linea aperta (es. linea, arco), produce una faccia aperta (es. piano)
-   Estrudere una linea chiusa (es. cerchio), produce a scelta una faccia chiusa (es. un fondo di un cilindro) oppure se il parametro \"solid\" è \"true\" produce un solido (es. un cilindro solido)
-   Estrudere un Wire aperto (es. un Draft Wire), produce un guscio aperto (diverse facce unite)
-   Estrudere un Wire chiuso (es. un Draft Wire), produce a scelta un guscio oppure se il parametro \"solid\" è \"true\" produce un solido
-   Estrudere una faccia (es. piano), produce un solido (es. Cuboide)
-   Estrudere una <img alt="" src=images/Draft_ShapeString.svg  style="width:16px;"> [Draft Shape String](Draft_ShapeString/it.md), produce un composto di solidi (la stringa è un composto di lettere che sono ciascuna un solido)
-   Estrudere una shell di facce, produce un Compsolid.

![600px](images/Part_Extrude_demo.png)



*Examples of extrusion*

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Selezionare la forma nella vista 3D o nell\'albero del modello
2.  Cliccare sull\'icona **<img src="images/Part_Extrude.svg" width=16px> '''Estrudi'''** nella barra degli strumenti, oppure andare nel menu Part → Estrudi
3.  Impostare la direzione e la lunghezza e opzionalmente altri parametri, per maggiori informazioni vedere la sezione [Parametri](#Parametri.md).
4.  Cliccare su OK.


</div>


<div class="mw-translate-fuzzy">

In alternativa, la selezione può essere fatta dopo aver avviato lo strumento, selezionando una o più forme della lista nel [pannello Azioni](Task_panel/it.md).


</div>

L\'albero del modello elenca tanti oggetti estrusi quante erano le forme selezionate. Ogni forma di partenza è posizionata sotto il suo oggetto estrusione.

## Parameters


<div class="mw-translate-fuzzy">

## Parametri

La forma Estrusione è definita dai seguenti parametri, che dopo la sua creazione possono essere modificati nella scheda Dati.


</div>


<div class="mw-translate-fuzzy">

-   **Base**: la forma di input (la forma su cui è stata applicata l\'estrusione Part)


</div>

-   **Dir**: la direzione in cui estendere la forma. Se **Dir Mode** è \'Custom\', si può modificare **Dir**. Altrimenti, **Dir** è di sola lettura ed è calcolata dalla forma collegata.


<div class="mw-translate-fuzzy">

-   **Dir Link**: collegamento parametrico a un bordo (linea) che imposta la direzione dell\'estrusione. Dalla v0.17, questa proprietà non è supportata dall\'editor delle proprietà.


</div>

-   **Dir Mode**: imposta il controllo di **Dir**. \'Custom\' significa che **Dir** è modificabile. \'Edge\' significa che Dir è ottenuta da un bordo (linea) collegato a **Dir Link**. \'Normal\' significa che Dir è perpendicolare al piano della forma di input.

-   **Length Fwd**: La lunghezza di estrusione. Se entrambi **Length Fwd** e **Length Rev** sono zero, viene utilizzata la lunghezza del vettore *\'Dir\'*.

-   **Length Rev**: Lunghezza aggiuntiva di estrusione in senso contrario a **Dir**.

-   **Solid**: se True, l\'estrusione di un bordo chiuso o di un contorno chiuso produce un solido. Se False, il risultato è un guscio.

-   **Reversed**: inverte l\'estrusione in senso contrario a **Dir**.

-   **Symmetric**: se True, l\'estrusione è centrata sulla forma di input e la lunghezza totale è **Length Fwd**. **Length Rev** viene ignorata.


<div class="mw-translate-fuzzy">

-   **Taper Angle** e **Taper Angle Rev**: applica un angolo all\'estrusione, in modo che i lati dell\'estrusione vengano disegnati secondo l\'angolo specificato. Un angolo positivo significa che la sezione trasversale si espande. **Taper Angle Rev** imposta la conicità per la parte invertita dell\'estrusione (la parte indicata da **Length Rev**). Dalla v0.17, l\'estrusione rastremata è supportata solo per i contorni senza fori. La conicità non funziona bene se la forma estrusa contiene delle B-spline.


</div>

-   **Face Maker Class**: imposta il nome della classe C++ del codice di creazione della faccia, che viene utilizzato quando si creano dei solidi dai contorni. Questa proprietà serve principalmente per mantenere la compatibilità con le versioni precedenti. Non toccare, a meno che non si sappia esattamente cosa si sta facendo.


<div class="mw-translate-fuzzy">

-   **Placement**: i parametri standard di [posizionamento](Placement/it.md).


</div>


<div class="mw-translate-fuzzy">

-   **Label**: etichetta da mostrare nell\'albero del modello (non disponibile nella creazione dell\'estrusione)


</div>



## Finestra di dialogo delle azioni 

![](images/Part_Extrude_dialog.png )

-    **OK**crea l\'estrusione e chiude la finestra di dialogo.

-    **Close**chiude il dialogo, senza fare nulla.

-    **Apply**crea l\'estrusione, ma non chiude la finestra di dialogo. È quindi possibile selezionare un\'altra forma nell\'elenco in basso e creare ulteriori estrusioni. Facendo clic su Applica più volte si creano molte estrusioni.

-   \'Direction\' pulsante di opzioni: imposta il modo in cui viene calcolata la direzione di estrusione.


<div class="mw-translate-fuzzy">

-    **Select**fare clic su di esso, quindi selezionare un bordo nella vista 3D. Questo bordo appare nel campo di testo accanto al pulsante, nel formato \"ObjectName:EdgeN\". Si può anche digitare il link manualmente. I valori X, Y, Z sono riempiti secondo la direzione del bordo.


</div>

-   pulsanti **X**, **Y**, **Z** fare clic sul pulsante X per impostare la direzione dell\'estrusione sull\'asse X positivo. Fare nuovamente clic per impostare l\'asse X negativo.

-   campi di input **X**, **Y**, **Z** imposta o visualizza il vettore di direzione dell\'estrusione. Se entrambe le lunghezze sono pari a zero, la lunghezza di questo vettore imposta la lunghezza dell\'estrusione ed i valori sono sempre espressi in mm, indipendentemente dalle preferenze dell\'unità di misura.

-   Length campi: impostano la lunghezza dell\'estrusione. Questi campi di input hanno il supporto dell\'unità di misura.

-   Symmetric: distribuisce l\'estrusione in entrambe le direzioni, in modo che il profilo rimanga nel mezzo.

-   Taper Outward Angle: angolo positivo indica che il profilo viene espanso all\'altra estremità dell\'estrusione.

-   Create Solid casella di controllo: se selezionata, l\'estrusione di un contorno o bordo chiuso produce una faccia. Se è stato preselezionato un contorno chiuso prima di richiamare l\'estrusione Part viene controllato di default.

-   Shape list: qui si seleziona quali forme estrudere. Se sono selezionati più oggetti, vengono creati più oggetti di estrusione.

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and to specify the direction. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

## Suggerimenti

La finestra di dialogo Part Extrude non offre ancora un\'anteprima. **Applica** crea un oggetto estrusione ogni volta che si fa clic su di esso, e questo può essere utile come anteprima, ma queste rimangono anche quando si fa clic su **OK** per creare la forma definitiva. Per pulire il modello può essere utile cliccare su [Annulla](Std_Undo/it.md) prima di fare clic su **OK**.


</div>




<div class="mw-translate-fuzzy">

## Comparazione con il [Pad di PartDesign](PartDesign_Pad/it.md) 


</div>


<div class="mw-translate-fuzzy">

Il Pad di PartDesign è anche una funzione di estrusione, ma ci sono delle differenze importanti.


</div>

-   Part Extrude always creates a standalone shape. PartDesign Pad fuses the extrusion result to the rest of the Body.
-   Part Extrude doesn\'t care where it is in model tree. PartDesign Pad can only live inside a [PartDesign Body](PartDesign_Body.md).
-   Part Extrude can extrude any object that has a Part geometry ([OpenCASCADE](OpenCASCADE.md) shape), except for solids and CompSolids.
-   Part Extrude can extrude individual faces of other objects. PartDesign Pad will only accept either Sketch or faces of PartDesign objects as a profile.


<div class="mw-translate-fuzzy">





</div>


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Extrude/it
