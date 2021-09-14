# Spreadsheet Workbench/it

 

<img alt="L\'icona dell\'ambiente Spreadsheet" src=images/Workbench_Spreadsheet.svg  style="width:128px;">

## Introduzione

L\'ambiente <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> Spreadsheet consente di creare e modificare fogli di calcolo, utilizzare i dati del foglio di calcolo come parametri in un modello, riempire il foglio di calcolo con i dati ricavati da un modello, eseguire calcoli ed esportare i dati in altre applicazioni di fogli di calcolo come LibreOffice o Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Un foglio di calcolo con alcune celle compilate con testo e quantità*

## Strumenti

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Crea un foglio di calcolo](Spreadsheet_CreateSheet/it.md): crea un nuovo foglio di calcolo.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Importa un foglio di calcolo](Spreadsheet_Import/it.md): importa un file con valori separati da virgola (CSV) in un foglio di calcolo.
-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Esporta il foglio di calcolo](Spreadsheet_Export/it.md): esporta un file di valori separati da virgola (CSV) da un foglio di calcolo.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Unisci le celle](Spreadsheet_MergeCells/it.md): unisce le celle selezionate.
-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Dividi la cella](Spreadsheet_SplitCell/it.md): divide le celle precedentemente unite.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Allinea a sinistra](Spreadsheet_AlignLeft/it.md): allinea a sinistra il contenuto delle celle selezionate.
-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Allinea in centro orizzontale](Spreadsheet_AlignCenter/it.md): allinea al centro in orizzontale il contenuto delle celle selezionate.
-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Allinea a destra](Spreadsheet_AlignRight/it.md): allinea a destra il contenuto delle celle selezionate.
-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Allinea in alto](Spreadsheet_AlignTop/it.md): allinea in alto il contenuto delle celle selezionate.
-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Allinea in centro verticale](Spreadsheet_AlignVCenter/it.md): allinea al centro in verticale il contenuto delle celle selezionate.
-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Allinea in basso](Spreadsheet_AlignBottom/it.md): allinea in basso il contenuto delle celle selezionate.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Grassetto](Spreadsheet_StyleBold/it.md): imposta il contenuto delle celle selezionate in grassetto.
-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Corsivo](Spreadsheet_StyleItalic/it.md): imposta il contenuto delle celle selezionate in corsivo.
-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Sottolineato](Spreadsheet_StyleUnderline/it.md): imposta il contenuto delle celle selezionate su sottolineato.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Alias](Spreadsheet_SetAlias/it.md): imposta un alias per le celle selezionate.

-    **Nero**e **Bianco** impostano i colori di primo piano e di sfondo delle celle selezionate.

-   menu contestuale delle righe e colonne del foglio di calcolo: cliccate con il tasto destro del mouse sull\'intestazione di una riga o colonna per inserire una nuova riga sopra o una nuova colonna a sinistra, o per cancellare la riga/colonna corrente. Si possono anche selezionare più righe o colonne al fine di cancellarle.{{Versione|0.20}} È anche possibile selezionare dove verranno inserite le nuove righe/colonne. Inoltre, per inserire ad esempio 3 nuove colonne in una volta sola, selezionate 3 colonne e usate il menu contestuale che vi offrirà ora di inserire 3 colonne.

### Proprietà delle celle 

Le proprietà di una cella del foglio possono essere modificate con un clic destro su una cella. Si apre la seguente finestra:

![](images/SpreadsheetCellPropDialog.png )

Come indicato dalle schede, è possibile modificare le seguenti proprietà:

-   Color: Colore del testo e colore di sfondo
-   Alignment: Allineamento orizzontale e verticale del testo
-   Style: Stile del testo: grassetto, corsivo, sottolineato
-   Units: Mostra le unità di misura per questa cella. Per favore leggi la sezione [ Unità di misura](#Unità_di_misura.md) sottostante.
-   Alias: Definisce un nome [alias](Spreadsheet_SetAlias/it.md) per questa cella. Questo alias può essere utilizzato nelle formule della cella e in generale anche nelle [espressioni](Expressions/it.md); per maggiori informazioni guarda la sezione [Espressioni nelle celle](#Espressioni_nelle_celle.md) .

## Espressioni nelle celle 

Una cella del foglio di calcolo può contenere un testo arbitrario o un\'espressione. Tecnicamente, le espressioni devono iniziare con un segno \"=\" uguale. Tuttavia, il foglio elettronico tenta di essere intelligente; se si inserisce qualcosa che sembra un\'espressione senza il segno \'=\', lo aggiunge automaticamente.

Le espressioni inserite nelle celle possono contenere numeri, funzioni, riferimenti ad altre celle e riferimenti alle proprietà del modello (Ma vedere sotto le [ Limitazioni attuali](#Limitazioni_attuali.md)). Le celle sono referenziate dalla loro colonna (lettera maiuscola) e riga (numero). Una cella può anche essere referenziata dal suo [ alias](#Riferimento_ai_dati_CAD.md) (sottostante). Esempio: B4 + A6

Le espressioni inserite nelle celle sono trattate da FreeCAD come codice di programmazione. Pertanto, quando modifichi una cella il contenuto che vedi non segue le tue impostazioni di visualizzazione:

-   il separatore dei decimali è sempre un punto
-   il numero di decimali visualizzati può differire dalle tue [impostazioni](Preferences_Editor/it#Unità.md)

I riferimenti agli oggetti nel modello sono spiegati in seguito in [Riferimento ai dati CAD](#Riferimento_ai_dati_CAD.md). L\'utilizzo dei valori delle celle del foglio di calcolo per definire le proprietà del modello è spiegato in seguito in [Dati del foglio di calcolo nelle espressioni](#Dati_dei_fogli_di_calcolo_nelle_espressioni.md). Per ulteriori informazioni sulle espressioni e sulle funzioni dipsonibili, consultare la pagina [Espressioni](Expressions/it.md).

## Interazione tra fogli di calcolo e modello CAD 

I dati nelle celle di un foglio di calcolo possono essere utilizzati nelle espressioni dei parametri del modello CAD. Pertanto, un foglio di calcolo può essere utilizzato come origine per i valori dei parametri utilizzati in un modello, raccogliendo efficacemente i valori in un\'unica posizione. Quando i valori vengono modificati nel foglio di calcolo, le modifiche si propagano nel modello.

Allo stesso modo, le proprietà degli oggetti del modello CAD possono essere utilizzate nelle espressioni nelle celle del foglio di calcolo. Ciò consente l\'uso di proprietà dell\'oggetto, come il volume o l\'area, nel foglio di calcolo. Se nel modello CAD viene cambiato il nome di un oggetto, la modifica viene automaticamente propagata a qualsiasi riferimento nelle espressioni del foglio di calcolo utilizzando il nome che è stato modificato.

In un documento si possono utilizzare più fogli di calcolo. Un foglio di calcolo può essere identificato tramite sia il suo nome che la sua etichetta.

FreeCAD assegna automaticamente un nome univoco ad un foglio di calcolo quando questo viene creato. Questi nome seguono il modello `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` e così via. Il nome non può essere modificato manualmente e non è visibile nelle proprietà del foglio di calcolo. Può essere utilizzato per fare riferimento al foglio di calcolo in un [ Espressione](Expressions/it.md) (vedere [ Dati del foglio di calcolo nelle espressioni](#Dati_dei_fogli_di_calcolo_nelle_espressioni.md) di seguito).

L\'etichetta di un foglio di calcolo viene automaticamente impostata sul nome del foglio di calcolo al momento della creazione. A differenza del nome, l\'etichetta può essere modificata, ad esempio nel pannello delle proprietà o utilizzando l\'azione del menu contestuale Rinomina. Notare che l\'etichetta di un foglio di calcolo all\'interno di un documento deve essere univoca; se provi a cambiare l\'etichetta con un\'etichetta già utilizzata da un altro foglio di calcolo, FreeCAD non accetterà la nuova etichetta.

FreeCAD verifica le dipendenze cicliche. Vedere [Limitazioni attuali](Spreadsheet_Workbench/it#Limitazioni_attuali.md).

### Riferimento ai dati CAD 

Come indicato sopra, è possibile fare riferimento ai dati del modello CAD nelle espressioni del foglio di calcolo.

Le espressioni calcolate nelle celle del foglio di calcolo iniziano con un segno di uguale (\'=\'). Comunque, il meccanismo di immissione del foglio di calcolo tenta di essere intelligente. Un\'espressione può essere inserita senza il segno \'=\'; se la stringa inserita è un\'espressione valida, un \'=\' viene aggiunto automaticamente quando si premere **Enter** finale. Se la stringa inserita non è un\'espressione valida (spesso il risultato di una digitazione sbagliata, ad es. \"MyCube.length\" anziché \"MyCube.Length\"), non viene aggiunto il segno \'=\' e viene trattato semplicemente come una stringa di testo.

**Nota:** il comportamento precedente (inserimento automatico di \'=\') ha alcune spiacevoli conseguenze:

-   se si desidera mantenere una colonna di nomi corrispondenti ai nomi [alias-names](#alias_name.md) in una colonna di valori adiacente, è necessario immettere il nome nella colonna dell\'etichetta prima di quello assegnato alla cella nella colonna del valore come nome alias. Altrimenti, quando inserisce il nome alias nella colonna dellle etichette il foglio di calcolo assume che è un\'espressione e lo cambia in \"= \"; e il testo visualizzato è il valore dalla cella .
-   Se si commette un errore quando si inserisce il nome nella colonna dell\'etichetta e si desidera correggerlo, non si può semplicemente cambiar con il nome alias. Invece, bisogna prima cambiare il nome alias in qualcos\'altro, quindi correggere il nome del testo nella colonna dell\'etichetta, quindi cambiare il nome alias nella colonna con il suo originale.

Un modo per aggirare questi problemi è prefissare le etichette di testo corrispondenti ai nomi di alias con una stringa fissa, rendendoli così diversi. Notare che \"\_\" non funziona, poiché viene convertito in \"=\". Tuttavia, un spazio, anche se invisibile, funziona.

La tabella seguente mostra alcuni esempi assumendo che il modello abbia una figura denominata \"MyCube\":

  Dati CAD                                    Chiamata nel foglio di calcolo   Risultato
  ------------------------------------------- -------------------------------- ------------------------------------------
  Lunghezza parametrica di un Cubo di Part    =MyCube.Length                   Lunghezza in mm
  Volume del Cubo                             =MyCube.Shape.Volume             Volume in mm³ senza unità
  Tipo di forma del Cubo                      =MyCube.Shape.ShapeType          String: Solid
  Etichetta del Cubo                          =MyCube.Label                    String: Cube
  coordinata x del centro di massa del Cubo   =MyCube.Shape.CenterOfMass.x     coordinata x in mm senza unità di misura

### Dati dei fogli di calcolo nelle espressioni 

Per utilizzare i dati del foglio di calcolo in altre parti di FreeCAD, di solito creerai un [ Espressione](Expressions/it#Espressioni.md) che si riferisce al foglio di calcolo e alla cella che contiene i dati che desideri utilizzare. Puoi identificare i fogli di calcolo per nome o per etichetta e puoi identificare le celle per posizione o per alias. Il completamento automatico è disponibile per tutti i tipi di riferimento.

+---------------------+-----------------------------------------------------+--------------------------------------------------------+
|                     | Foglio di calcolo per nome                          | Foglio di calcolo per etichetta                        |
+=====================+=====================================================+========================================================+
| Cella per Posizione |                                      |                                         |
|                     | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                     |                                                  |                                                     |
+---------------------+-----------------------------------------------------+--------------------------------------------------------+
| Cella per Alias     |                                      |                                         |
|                     | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                     |                                                  |                                                     |
+---------------------+-----------------------------------------------------+--------------------------------------------------------+


<div class = "mw-collapsible mw-collapsed">

Il modo consigliato per fare riferimento ai dati del foglio di calcolo è utilizzare l\'etichetta del foglio di calcolo e il nome dell\'alias della cella. Per una spiegazione più approfondita dei pro e dei contro delle modalità di indirizzamento, vedere la sezione espansa di seguito.


<div class = "mw-collapsible-content">

L\'utilizzo dell\'etichetta del foglio di calcolo ha il vantaggio che può essere liberamente modificata per descrivere il contenuto del foglio di calcolo. È anche più semplice identificare il foglio di calcolo in uso poiché il testo nell\'espressione corrisponde all\'etichetta mostrata nelle viste del modello e delle proprietà. Se decidi di modificare l\'etichetta di un foglio di lavoro, i riferimenti esistenti ai contenuti del foglio di lavoro verranno aggiornati, in modo da non interrompere le tue espressioni rinominando il foglio di lavoro. Il nome interno del foglio di calcolo non è immediatamente disponibile da nessuna parte tranne che nell\'editor delle espressioni, quindi se utilizzi il nome interno e successivamente decidi di rinominare i fogli di calcolo, potresti avere difficoltà a risalire alla fonte dei dati dell\'espressione.

Tieni presente che quando crei un nuovo foglio di lavoro, il nome e l\'etichetta sono gli stessi, quindi è facile utilizzare accidentalmente il nome del foglio di lavoro invece dell\'etichetta. Un modo semplice per evitarlo è dare al foglio di calcolo un nome significativo prima di iniziare a usarlo nelle espressioni.

Sebbene sia possibile utilizzare il numero di riga e di colonna in un\'espressione per fare riferimento a una cella, è consigliabile assegnare alla cella un nome alias e utilizzarlo. Vedi [ Proprietà delle celle](#Proprietà_delle_celle.md) sopra per informazioni su come impostare l\'alias. Ad esempio, se i dati nella cella B1 contenessero il parametro di lunghezza per un oggetto, un nome alias di {{incode | MyObject_Length}} consentirebbe di fare riferimento al valore come {{incode | <<MyParams>> .MyObject_Length}} invece di {{incode | Spreadsheet.B1}}. Oltre ad essere molto più facili da leggere e capire, i nomi alias sono anche molto più facili da modificare se decidi di modificare la struttura del tuo foglio di calcolo. L\'uso di un alias ha anche il vantaggio che è più facile vedere quali celle vengono utilizzate per controllare altre parti del documento. Nota che FreeCAD regola automaticamente i riferimenti posizionali nelle espressioni se inserisci o rimuovi righe e colonne nel foglio di calcolo, quindi anche se usi numeri di riga e di colonna in un\'espressione, puoi inserire righe e colonne senza interrompere i riferimenti alle celle circostanti.


</div>


</div>

### Modelli complessi e ricalcoli 

La modifica di un foglio di calcolo attiverà un ricalcolo del modello 3D, anche se le modifiche non influiscono sul modello. Per un modello complesso un ricalcolo può richiedere molto tempo e dover attendere dopo ogni singola modifica è ovviamente piuttosto fastidioso.


<div class="mw-translate-fuzzy">

Ci sono tre soluzioni per affrontare questo problema:

1.  Nella [Vista ad albero](Tree_view/it.md) fai clic con il tasto destro del mouse sul documento <img alt="" src=images/Document.svg  style="width:24px;"> che contiene il foglio di calcolo.
    -   Selezionare l\'opzione {{MenuCommand | Salta il ricalcolo}} dal menu contestuale.
    -   C\'è un grosso svantaggio in questa soluzione. I nuovi valori immessi nel foglio di calcolo non verranno visualizzati finché il documento non viene ricalcolato. Viene invece mostrato {{incode | #PENDING}}.
    -   Puoi ricalcolare manualmente, usando il comando [ Modifica: Aggiorna](Std_Refresh/it.md), o disabilitare {{MenuCommand | Salta il ricalcolo}} quando hai finito di modificare.
2.  Usare una macro per saltare automaticamente i ricalcoli durante la modifica di un foglio di calcolo:
    -   Scarica ed esegui [skipSheet.FCMacro](https://forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301).
    -   Questa soluzione consente di risparmiare alcuni passaggi rispetto alla prima soluzione, ma presenta anche lo svantaggio menzionato.
3.  Mettere il ​​foglio di calcolo in un file separato:
    -   Puoi fare riferimento ai dati di un foglio di calcolo da un file esterno con questa sintassi: {{incode | <nowiki> = NameOfFile#<<MySpreadsheet>>.MyAlias​​</nowiki>}}.
    -   Il vantaggio di avere il foglio di calcolo in un altro file rispetto alla disattivazione dei ricalcoli è che il foglio di calcolo stesso viene ricalcolato.
    -   Lo svantaggio è che il modello non verrà ricalcolato automaticamente dopo le modifiche al foglio di calcolo.
    -   Nello scenario in cui apri prima il file \"foglio di calcolo\", modifichi uno o più valori e quindi apri il file \"modello\", non ci sarà alcuna indicazione che il modello debba essere ricalcolato. Tuttavia, se entrambi i file sono aperti, l\'icona [ Aggiorna](Std_Refresh/it.md) aggiornerà correttamente il file \"modello\" dopo le modifiche al file \"foglio di calcolo\".


</div>

## Unità di misura 

Il foglio di calcolo ha il concetto dimensione (unità di misura) associata ai valori delle celle. Un numero inserito senza un\'unità associata non ha dimensione. L\'unità di misura deve essere immessa immediatamente dopo il valore numerico, senza spazio intermedio. Se un numero ha un\'unità di misura associata, quell\'unità sarà utilizzata in tutti i calcoli. Ad esempio, la moltiplicazione di due lunghezze con l\'unità mm fornisce un\'area con l\'unità in mm².

Se una cella contiene un valore che rappresenta una dimensione, esso deve essere inserito con la relativa unità associata. Anche se molti casi semplici possono essere gestiti con un valore adimensionale, è sconsigliato non inserire l\'unità. Se un valore che rappresenta una dimensione viene inserito senza la relativa unità associata, alcune sequenze di operazioni costringono FreeCAD a segnalare l\'incompatibilità delle unità in un\'espressione quando sembra che dovrebbe essere convalidata. (Questo può essere compreso meglio compreso guardando [questa discussione](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) nel forum di FreeCAD).

È possibile modificare le unità visualizzate per un valore di cella utilizzando la finestra di dialogo delle [ Proprietà delle celle](#Proprietà_delle_celle.md) (sopra). Questo non modifica il valore contenuto nella cella; converte solo il valore esistente per la visualizzazione. Il valore utilizzato per i calcoli non cambia, ed i risultati delle formule che utilizzano il valore non cambiano. Ad esempio, una cella contenente il valore \"5.08cm\" può essere visualizzata come \"2in\" modificando il valore della scheda delle unità su \"in\".

Un numero adimensionale non può essere modificato in un numero con un\'unità tramite la finestra di dialogo delle proprietà della cella. Si può inserire una stringa di unità e tale stringa verrà visualizzata; ma la cella contiene ancora un numero adimensionale. Per modificare un valore adimensionale in un valore con una dimensione, è necessario reinserire il valore stesso con l\'unità associata.

Occasionalmente può essere desiderabile sbarazzarsi di una dimensione in un\'espressione. Questo può essere fatto moltiplicando per 1 con un\'unità reciproca.

## Importazione ed esportazione 

I fogli possono essere importati ed esportati nel formato [csv](https://en.wikipedia.org/wiki/Comma-separated_values) che può anche essere letto e scritto da molte altre applicazioni di fogli di calcolo come Microsoft Excel o LibreOffice Calc. Durante l\'importazione dei file in FreeCAD, il delimitatore (il carattere che viene utilizzato per separare le colonne) deve essere il carattere di tabulazione (questo può essere impostato durante l\'esportazione da altre applicazioni). L\'importazione di un file CSV è disponibile tramite il menu **Spreadsheet → Import Spreadsheet** o facendo clic sull\'icona <img alt="" src=images/SpreadsheetImport.svg  style="width:24px;">. Questa funzione di importazione non apre file Excel o altri formati di fogli di calcolo.

I fogli di calcolo in formato Excel \"xlsx\" possono essere importati in un documento FreeCAD tramite il menu **File → Importa...**. I fogli di calcolo Excel possono anche essere aperti da FreeCAD facendo clic nel menu **File → Apri...** o facendo clic sull\'icona <img alt="" src=images/Document-open.svg  style="width:24px;">. In questi casi si crea un nuovo documento con all\'interno un foglio di calcolo. Sono supportate le seguenti caratteristiche:

-   tutte le funzioni che sono disponibili anche nel foglio di calcolo FreeCAD. Le altre funzioni danno un errore nella cella corrispondente dopo l\'importazione.
-   i nomi alias per le celle
-   più di una foglio nei fogli di calcolo Excel. In questo caso viene creato un foglio di calcolo di FreeCAD per ogni foglio di Excel.

Le altre funzionalità non vengono importate nel foglio di calcolo di FreeCAD. L\'importazione di Excel è disponibile dalla {{Version/it|0.17}} di FreeCAD.

## Stampa

Per gestire l\'impostazione della pagina necessaria per la stampa, i fogli di calcolo di FreeCAD vengono stampati inserendoli in una [ Vista foglio di calcolo di TechDraw](TechDraw_SpreadsheetView/it.md).

## Limitazioni attuali 

FreeCAD verifica le dipendenze cicliche. Per come è concepita, tale verifica si arresta al livello dell\'oggetto foglio di calcolo. Di conseguenza, non si dovrebbe avere un foglio di calcolo che contiene contemporaneamente le celle i cui valori sono utilizzati per specificare parametri nel modello e sia celle i cui valori utilizzano l\'output del modello. Ad esempio, non è possibile avere celle che specificano la lunghezza, la larghezza e l\'altezza di un oggetto e un\'altra cella che fa riferimento al volume totale della forma risultante. Questa limitazione può essere superata creando due fogli di calcolo: uno utilizzato come origine dati per i parametri di input per il modello e l\'altro usato per il risultato dei calcoli basati sui dati geometrici.

Quando le celle vengono copiate, viene copiato solo il contenuto (espressione o valore). Le [Proprietà delle celle](Spreadsheet_Workbench/it#Proprietà_delle_celle.md) descritte sopra non sono copiate.

## Script di base 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet::Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}} 

[Category:Workbenches](Category:Workbenches.md)
