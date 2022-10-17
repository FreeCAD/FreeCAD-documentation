# Macro FCTreeView/it
{{Macro/it
|Name=Macro FCTreeView
|Icon=Macro_FCTreeView.png
|Translate=Macro FCTree Vista
|Description={{ColoredText|#ff0000|#ffffff|Nuova versione GUI modificata per HD dpi (QGridLayout) run only FC version 0.18 and more (PySide2 Qt5)}} <br/> <br/>Questa macro visualizza tutti gli oggetti del progetto in un elenco con le opzioni ordinate per etichetta del nome...<br/> <br/>Per la precedente versione vedi [https   *//gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/0a92d7f591a0a179f84b2fc417046723b4d7b0e6/Macro_FCTreeView.FCMacro Macro_FCTreeView.FCMacro] e installa la macro manuelamente.
|Author=Mario52
|Version=00.09
|Date=2020-09-24
|FCVersion=0.18 ed inferiori
|Download=[https   *//forum.freecadweb.org/download/file.php?id=70498 Macro FCTreeView Icon package] decomprimere il file .zip e copiare le icona nella directory delle macro.
}}

## Descrizione

Macro per elencare tutti gli oggetti nel progetto in una lista senza gerarchia, opzioni per ordinare per nome, etichetta, visibilità, gruppo, con opzioni di ricerca per nome, etichetta \.... senza distinzione tra maiuscole e minuscole o con distinzione tra maiuscole e minuscole e selezionare tutti gli oggetti visualizzati nella finestra macro. {{Codeextralink|https   *//gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/59bc2028978c82744c83c6b138ab3ef30e0bf6f3/Macro_FCTreeView.FCMacro}}

## Utilizzo

![Macro FCTreeView](images/FCTreeView.gif ) 

### Sezione **Window** 

Il titolo visualizza l\'opzione, il numero e il tipo di oggetti visualizzati

-   **O** = Oggetto
-   **N** = Nome
-   **L** = Etichetta
-   **T** = Totale
-   **G** = Gruppo
-   **S** = Singolo
-   **V** = Visibile
-   **H** = Nascosto

Se viene selezionato un oggetto   * viene visualizzata la Base di posizionamento, Rotazione e Centro di massa (se disponibile!) ![Icona utilizzata per il nome dell\'oggetto](images/Macro_FCTreeView_00.png ) Icona utilizzata per il nome dell\'oggetto (la barra di scorrimento è colorata in blu)

![Icon used for the Label of object](images/Macro_FCTreeView_05.png ) Icona utilizzata per l\'etichetta dell\'oggetto (la barra di scorrimento è di colore blu chiaro)

![Icon used for visualise if the object is status Visible (mouse click for Hidden)](images/Macro_FCTreeView_01.png )Icona utilizzata per visualizzare se l\'oggetto è in stato Visibile (clic del mouse per Nascosto) (la barra di scorrimento è colorata in verde)

![Icon used for visualise if the object is status Hidden (mouse click for Visible)](images/Macro_FCTreeView_02.png ) Icona utilizzata per visualizzare se l\'oggetto è in stato Nascosto (clic del mouse per Visibile) (la barra di scorrimento è colorata in rosso)

![icona utilizzata per il nome contiene oggetti (o gruppo di cartelle)](images/Macro_FCTreeView_17.png ) L\'icona utilizzata per il nome contiene oggetti (o gruppo di cartelle)

![Icona usata per informare l\'oggetto in un gruppo, gli oggetti numerici sono visualizzati nel gruppo in alto (la barra di scorrimento è colorata in rosso)](images/Macro_FCTreeView_03.png ) Icona usata per informare l\'oggetto in un gruppo, gli oggetti numerici sono visualizzati nel gruppo in alto (la barra di scorrimento è colorata in rosso)

![Icona utilizzata per visualizzare il singolo oggetto (non il gruppo)](images/Macro_FCTreeView_04.png ) Icona utilizzata per visualizzare il singolo oggetto (non il gruppo)

### Section **Ordina per    *** 


**[<img src=images/Macro_FCTreeView_10.png style="width   *18px"> Name**

Icona usata per il flip/flop normale/invertire la lista dei dati ordinata per nome


**[<img src=images/Macro_FCTreeView_11.png style="width   *18px"> Label**

Icona usata per il flip/flop normale/invertire la lista dei dati ordinata per etichetta


**[<img src=images/Macro_FCTreeView_12.png style="width   *18px"> Visible**

Icona usata per il flip/flop normale/rovescia l\'ordinamento della lista dei dati per Visibile/Nascosto


**[<img src=images/Macro_FCTreeView_13.png style="width   *18px"> Group**

Icona usata per il flip/flop normale/inverte l\'ordinamento della quotazione dei dati per Gruppo/Oggetto singolo


**[<img src=images/Macro_FCTreeView_19.png style="width   *18px"> Length**

Se questa casella di controllo è selezionata, l\'ordinamento viene creato in base alla lunghezza con il pulsante su cui è stato fatto clic (Nome, Etichetta \...)

### Section **Global** 


**[<img src=images/Macro_FCTreeView_21.png style="width   *18px"> Split**

flip/flop Dividi la lista dei nomi


**[<img src=images/Macro_FCTreeView_22.png style="width   *18px"> Split**

flip/flop Dividi il nome e l\'elenco delle etichette


**[<img src=images/Macro_FCTreeView_14.png style="width   *18px"> Expend**

flip/flop l\'elenco dei dati Fold/Expend


**[<img src=images/Macro_FCTreeView_15.png style="width   *18px"> Expend**

capovolgere/flopare l\'elenco di dati Spiega/Piega


**[<img src=images/Macro_FCTreeView_06.png style="width   *18px"> Visibility**

flip/flop normal/Visibility


**[<img src=images/Macro_FCTreeView_07.png style="width   *18px"> Group**

flip/flop normal/Group


**[<img src=images/Macro_FCTreeView_16.png style="width   *18px"> Reload**

Ricarica i dati nel progetto


**[<img src=images/Macro_FCTreeView_18.png style="width   *18px"> Original**

ritorno nell\'organizzazione originale dopo l\'operazione visibilità/Nascosto


**[<img src=images/Macro_FCTreeView_01.png style="width   *18px"> All Visible**

visualizza se l\'oggetto è stato Visibile


**[<img src=images/Macro_FCTreeView_02.png style="width   *18px"> All Hidden**

visualizza se l\'oggetto è stato Nascosto

### Section **Search** 


**[<img src=images/Macro_FCTreeView_20.png style="width   *18px"> Clear**

Cancella la modifica della riga di ricerca

#### The radioButton options **Search**   * 

-   **(\"NLwc\")**   * Cerca per nome ed etichetta **W** senza rispettare il sensibile **C** \'ase

-   **(\"Nsc\")**    * Cerca per nome e rispettando il **S**ensitive **C**ase

-   **(\"Lwc\")**    * Cerca per etichetta **W**ithout rispettando il sensibile **C**ase

-   **(\"NLsc\")**    * Cerca per nome e etichetta e rispettando il **S**ensitive **C**ase

-   **(\"NLwsc\")**    * Cerca per nome ed etichetta in Word e rispettando il **S**ensitive **C**ase (selezione del pannello stesso di FreeCAD)

-   **(Nu)**    * Cerca per valore numerico (raggio, lunghezza, angolo \.....) vedi la sezione versione


**[<img src=images/Macro_FCTreeView_23.png style="width   *18px"> Select**

flip/flop per Selezionati tutti gli oggetti visualizzati nella finestra


**[<img src=images/Macro_FCTreeView_24.png style="width   *18px"> Unselected**

flip/flop per Selezionati tutti gli oggetti visualizzati nella finestra


**[<img src=images/Macro_FCTreeView_25.png style="width   *18px"> S Sheet**

accesso nelle opzioni del foglio di calcolo

### Le opzioni SpreadSheet   * 

![Macro FCTreeView](images/TreeView_SpeadSheet.gif ) 

![](images/Macro_FCTreeView_001.png )

![](images/Macro_FCTreeView_002.png )

-   Opzioni CheckBox per selezionare i dati da salvare nel foglio di calcolo


**[<img src=images/Macro_FCTreeView_28.png style="width   *18px"> Select**

   * Seleziona tutta l\'opzione checkBox per salvare


**[<img src=images/Macro_FCTreeView_29.png style="width   *18px"> Select**

   * unSeleziona tutta l\'opzione checkBox per salvare

![](images/Macro_FCTreeView_003.png )

-   **Value**    * da solo il valore viene salvato nella cella
    -   Ex    * 10.00 ![](images/Macro_FCTreeView_30.png )
-   **Val Gr**    * il valore e l\'unità vengono salvati in una cella univoca
    -   Ex    * 10.00 mm ![](images/Macro_FCTreeView_31.png )
-   **Val Gr Ph**    * il valore, l\'unità e i dati fisici vengono salvati in una cella univoca
    -   Ex    * 10.00 mm Length ![](images/Macro_FCTreeView_32.png )
-   **Split**    * se la casella di controllo Dividi è selezionata, i dati vengono tagliati salvati in una cella separata
    -   Ex    * 10.00 \| mm \| length ![](images/Macro_FCTreeView_33.png )

![](images/Macro_FCTreeView_004.png )

-   Combobox **mm**    * seleziona la lunghezza dell\'unità desiderata. Il valore è convertito nell\'unità selezionata. The units length available are   *
    -   km, hm, dam, m, dm, cm, **mm**, um, nm, pm, fm, in, lk, ft, yd, rd, ch, fur, mi, lea, nmi
-   Combobox **gram**    * selezionare il peso unitario desiderato. Il valore è convertito nell\'unità selezionata. Le unità di peso disponibili sono   *
    -   t, q, kg, hg, dag, **g**, dg, cg, mg, µg, ng, pg, fg, gr, dr, oz, oz t, lb, t lb, st, qtr, cwt, tonneau fr, ct
-   Spinbox **Densite**    * dare la densità di dm3 del materiale utilizzato (Predefinito    * 1.0000)
-   Spinbox **Round**    * dare il valore rotondo desiderato (Predefinito    * 3)

![](images/Macro_FCTreeView_005.png )

-   Combobox **Name spreadSheet**    * Elenca il foglio di calcolo nel documento
-   Line edit **Name spreadSheet**    * Visualizza il foglio di calcolo effettivo o indica il nome per il nuovo foglio di lavoro

![](images/Macro_FCTreeView_006.png )


**[<img src=images/Macro_FCTreeView_28.png style="width   *18px"> Select**

seleziona tutte le opzioni della casella di controllo


**[<img src=images/Macro_FCTreeView_29.png style="width   *18px"> Unselect**

deselezionate tutte le opzioni della casella di controllo


**[<img src=images/Macro_FCTreeView_27.png style="width   *18px"> Save**

salva i dati nel foglio di calcolo visualizzato. se nessun foglio di calcolo è attivo, viene creato il foglio di calcolo denominato **FCSpreadSheet**


**[<img src=images/Macro_FCTreeView_26.png style="width   *18px"> Quit**

esci dalle opzioni del foglio di calcolo

### Icons

L\'icona deve essere copiata nella stessa directory della macro [Macro_FCTreeView_Icon](https   *//forum.freecadweb.org/download/file.php?id=70498)

![Icon used for the Name of object](images/Macro_FCTreeView_00.png ) ![Icon used for visualise if the object is status Visible (mouse click for Hidden)](images/Macro_FCTreeView_01.png ) ![Icon used for visualise if the object is status Hidden (mouse click for Visible)](images/Macro_FCTreeView_02.png ) ![Icon used for inform the object in a group the number objects is displayed in top group](images/Macro_FCTreeView_03.png ) ![Icon used for displayed the single object (not group)](images/Macro_FCTreeView_04.png ) ![Icon used for the Label of object](images/Macro_FCTreeView_05.png ) ![Icon used for flip/flop normal/Visibility](images/Macro_FCTreeView_06.png ) ![Icon used for flip/flop normal/Group](images/Macro_FCTreeView_07.png ) ![Icon used for Reverse the data listing (momentarily not used)](images/Macro_FCTreeView_08.png ) ![Icon used for quit Macro FCTreeView (momentarily not used)](images/Macro_FCTreeView_09.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Name](images/Macro_FCTreeView_10.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Label](images/Macro_FCTreeView_11.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Visibility/Hidden](images/Macro_FCTreeView_12.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Grout/Single object](images/Macro_FCTreeView_13.png ) ![Icon used for flip/flop the data listing Fold/Expend](images/Macro_FCTreeView_14.png ) ![Icon used for flip/flop the data listing Expend/Fold](images/Macro_FCTreeView_15.png ) ![Icon used for reload the data in the project](images/Macro_FCTreeView_16.png ) ![Icon used for the Name contains objects (or folder Group)](images/Macro_FCTreeView_17.png ) ![Icon used for return in original organisation after operation visibility/Hidden](images/Macro_FCTreeView_18.png ) ![If this check Box is checked the sort is created by length with the button clicked (Name, Label \...)](images/Macro_FCTreeView_19.png ) ![Icon used for Clear the search line edit](images/Macro_FCTreeView_20.png ) ![Icon used for flip/flop Split the Name list](images/Macro_FCTreeView_21.png ) ![Icon used for flip/flop Split the Name and Label list](images/Macro_FCTreeView_22.png ) ![Icon used for Selected all object(s) displayed in the window](images/Macro_FCTreeView_23.png ) ![Icon used for Unselected all object(s)](images/Macro_FCTreeView_24.png ) ![Icon used for access in Spreadsheet options](images/Macro_FCTreeView_25.png ) ![Icon used for quit the Spreadsheet options](images/Macro_FCTreeView_26.png ) ![Icon used for save the data in Spreadsheet](images/Macro_FCTreeView_27.png ) ![Icon used for select all checkbox options](images/Macro_FCTreeView_28.png ) ![Icon used for unselected all checkbox options](images/Macro_FCTreeView_29.png ) ![Icon used for save the value data in Spreadsheet](images/Macro_FCTreeView_30.png ) ![Icon used for save the value and Unit data in Spreadsheet](images/Macro_FCTreeView_31.png ) ![Icon used for save the value, Unit and type data in Spreadsheet](images/Macro_FCTreeView_32.png ) ![Icon used for split the value, Unit and type in cell separate in Spreadsheet](images/Macro_FCTreeView_33.png )

## Script

Per evitare molte istanze il clic sul pulsante Barra degli strumenti è effetto flip/flop (nascondi/visibili)

La macro si trova nella parte destra del dock per la modifica, modifica la riga di valore numero 133 **testing = 0** (o la modifica con il mouse come normale di un widget)

The icon ToolBar ![Macro FCTreeView](images/Macro_FCTreeView.png )

**Macro_FCTreeView.FCMacro**


{{CodeDownload|https   *//gist.github.com/mario52a/67517ef758ff20005d0a6adcfd8c9190|Macro_FCTreeView.FCMacro}}

## Da fare 

~~Docked the macro~~

## Version

ver 00.09 (2020-09-24)    * corretto il \"**freeze**\" macro dopo la chiamata al **assembly4 workbench** provato ad attivare \"**Class SelObserver**\" e funziona ???


```python
class SelObserver   *
    def addSelection(self, document, object, element, position)   *  # Selection
        global sourisPass
        global listeSorted
        global ui

        None
```

ver 00.08 (2020-02-25)    * upgrade con i Layout

ver 00.07 (06/05/2018)    * modificare la procedura per cercare l\'ultima cella utilizzata

ver 00.06 (13/12/2017)    * corretto piccolo bug line del line num 1881 \"del listeSortedBis \[doublon\] \[4   *] \# supprime le fond inutile\" grazie renatorivo

ver 00.05 (27/11/2017)    * aggiungi foglio di calcolo per la creazione e molte opzioni per lui

ver 00.04 (29-09-2017)    * aggiungi ricerca per valore numerico (lunghezza, raggio \....)

valori ricercati    *


```python
global impost                 ; impost = ["Angle","Angle0","Angle1","Angle2","Angle3","ChamferSize","Circumradius","Columns","Degree",
                                          "FilletRadius","FirstAngle","Growth","Height","LastAngle","Length","Length2","MajorRadius",
                                          "MinorRadius","Pitch","Polygon","Radius","Radius1","Radius2","Radius3","Rows","Size","Width",
                                          "X","X1","X2","Xmax","Xmin","X2max","X2min",
                                          "Y","Y1","Y2","Ymax","Ymin","Y2max","Y2min",
                                          "Z","Z1","Z2","Zmax","Zmin","Z2max","Z2min"]
```

ver 00.03 (23/09/2017)    * aggiungi ricerca per tipo oggetto

ver 00.02 (11/09/2017)    * modifica per ancorare e impedire molte istanze il clic sul pulsante è effetto flip/flop (macro nascondi/visibile)

ver 00.01 (08/09/2017)    *



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCTreeView/it
