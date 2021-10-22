# Arch Schedule/it
---
- GuiCommand:/it   Name:Arch Schedule   Name/it:Scheda   Workbenches:[MenuLocation:Arch → Scheda   SeeAlso:[[Arch Equipment/it|Arredo](Arch_Workbench/it___Arch]].md)---

## Descrizione

Lo strumento Scheda consente di creare e compilare automaticamente un [foglio di calcolo](Spreadsheet_Workbench/it.md) con contenuti prelevati dal modello.

**Nota**: Questo strumento è stato riscritto in FreeCAD 0.17 e differisce dalle versioni precedenti.


<div class="mw-translate-fuzzy">

Per una soluzione più generale, consultare il _. Questo ambiente utilizza la sintassi SQL per estrarre informazioni dal documento.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Aprire o creare un documento di FreeCAD con alcuni oggetti.
2.  Premere il pulsante **<img src="images/Arch_Schedule.svg" width=16px> [Scheda](Arch_Schedule/it.md)**.
3.  Regolare le opzioni desiderate.
4.  Premere **OK**.


</div>

## Flusso di lavoro 

In primo luogo è necessario disporre di un modello. Ad esempio, qui c\'è un documento con una coppia di oggetti. Non è necessario che siano oggetti Arch, possono essere di qualsiasi tipo.

![](images/Arch_schedule_example01.jpg )


<div class="mw-translate-fuzzy">

Poi premere il pulsante <img alt="" src=images/Arch_Schedule.svg  style="width:16px;"> Scheda di Arch. Si ottiene un pannello delle Azioni come questo. È piuttosto ampio, quindi può essere necessario allargarlo.


</div>

![](images/Arch_schedule_example02.jpg )

Poi si può riempire riga per riga. Ogni riga è una \"query\" e restituisce una riga nel foglio di calcolo. Premere il pulsante **Aggiungi** per aggiungere una nuova riga e fare doppio clic su ciascuna cella di quella riga per inserire i valori. Il pulsante **Del** cancella la riga che contiene una cella selezionata, e **Clear** elimina tutte le righe. I valori che è possibile mettere nelle colonne sono:


<div class="mw-translate-fuzzy">

-   **Description**: Una descrizione per questa query. La colonna Descrizione è la prima colonna del foglio di calcolo risultante. Nella descrizione è obbligatorio avere una query rappresentata. Se si lascia la cella descrizione vuota, l\'intera riga viene saltata e lasciata vuota nel foglio di calcolo. Ciò consente di aggiungere delle righe \"separatrici\".
-   **Value**: Questa è la vera query che si desidera eseguire su tutti gli oggetti selezionati da questa query. Può essere di due tipi di cose: o la parola \'\' \'count\' \'\' (o Count o COUNT, è case-insensitive), che si limita a contare gli oggetti, oppure si può recuperare e sommare una proprietà, ad esempio `object.Shape.Volume` o `object.Length` o anche `object.Label`. Il nome utilizzato prima del primo punto (object) può essere qualsiasi cosa, si potrebbe anche scrivere `x.Shape.Volume`. La regola è: quello che viene dopo il primo punto verrà recuperato da ogni oggetto selezionato da questa query, se possibile (gli oggetti che non hanno la proprietà richiesta sono saltati), e i risultati vengono uniti. Ad esempio, se si utilizza `object.Shape.Volume`, si ottiene la somma di tutti i volumi di tutti gli oggetti selezionati da questa query.
-   **Unit**: Un\'unità opzionale per esprimere i risultati. Spetta all\'utente dare una unità che corrisponda alla query che si sta facendo, ad esempio, se si stanno recuperando i volumi, è necessario utilizzare una unità di volume, ad esempio `m^3`. Se si utilizza una unità sbagliata, per es. cm, si ottengono risultati errati.
-   **Objects**: È possibile lasciare questo campo vuoto, in questo caso tutti gli oggetti del documento sono considerati da questa query, o dare un elenco di nomi di oggetti (non le etichette) separato da punto e virgola (;). Se uno qualsiasi degli oggetti in questo elenco è un gruppo, sono selezionati pure i suoi figli. Quindi il modo più semplice per utilizzare questa funzione è quella di raggruppare gli oggetti del documento per significato, e qui dare solo il nome del gruppo. È inoltre possibile utilizzare il pulsante **Selezione** per aggiungere gli oggetti attualmente selezionati nel documento.
-   **Filter**: Qui è possibile aggiungere un elenco dei filtri separati da punto e virgola (;). Ogni filtro è scritto nella forma: Filtro:valore, dove il filtro può essere (è anche case-insensitive): Name, Label, Type, o Role (vedere sotto l\'elenco completo). Per esempio: name:door;type:window filtra gli oggetti ottenuti dal passaggio precedente, e mantiene solo quelli il cui nome contiene \"door\" E del tipo (restituito da Draft.getType) \"wall\". Tutto è case-insensitive. I filtri che inizia con ! sono invertiti. Per esempio, !name:wall mantiene solo gli oggetti che non hanno \"wall\" nel loro nome. \"Role\" è una proprietà che hanno tutti gli oggetti Arch.


</div>

Il pulsante **Importa** permette di costruire questa lista in un altro foglio di calcolo, e importarla qui come file CSV.

Quindi si può costruire una lista di query di questo tipo:

![](images/Arch_schedule_example03.jpg )

Dopo di che, premendo **OK**, al documento viene aggiunto un nuovo oggetto Scheda che contiene un foglio di calcolo con i risultati:

![](images/Arch_schedule_example04.jpg )

Facendo doppio clic sull\'oggetto Scheda, si ritorna al pannello delle Azioni e si può modificare i valori. Facendo doppio clic sul Foglio di calcolo, si ottengono i risultati nelle 3 colonne: la descrizione, il valore e l\'unità (se applicabile):

![](images/Arch_schedule_example05.jpg )

Dall\'ambiente Spreadsheet il foglio di calcolo può quindi essere esportato normalmente in formato CSV.

## Dynamic properties 

It is possible to add your own properties to objects. These are called [Dynamic properties](Property_editor#Actions.md). If they have been added with the **Prefix group name** option selected, their names will indeed start with the group name, but this prefix is not displayed in the [Property editor](Property_editor.md). Their names have this form: `NameOfGroup_NameOfProperty`. To reference them in a schedule this full name must be used.

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Schedule/it
