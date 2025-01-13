# Release notes 0.15/it
FreeCAD 0.15 è stato rilasciato il giorno 8 Aprile 2015. Questo è un riassunto dei cambiamenti più interessanti. L\'elenco completo delle modifiche è disponibile in [Mantis changelog](http://www.freecadweb.org/tracker/changelog_page.php). Versioni precedenti in: [0.14](Release_notes_0.14/it.md) - [0.13](Release_notes_0.13/it.md) - [0.12](Release_notes_0.12/it.md) - [0.11](Release_notes_0.11/it.md)

<img alt="" src=images/Spark-Plug-Plane.jpg  style="width:1024px;">


<center>

Spark Plug Plane by r-frank


</center>



## Aspetti generali 



### Casella di ricerca nella Vista Selezione 

La finestra Selezione permette agli utenti di cercare al suo interno gli oggetti selezionati. Inoltre ora si ha la possibilità di selezionare una sola entità, deselezionarla, adattare la vista all\'entità e evidenziarla nella vista ad albero.

![](images/FeatureSelectionView.jpg )



### Ampliamento del supporto delle unità 

Il nuovo sistema di [unità di misura](Quantity/it.md) di FreeCAD, introdotto con la versione 0.14, ora è utilizzato da quasi tutti i moduli, compresi [Sketcher](Sketcher_Workbench/it.md), [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md). Solo poche aree non ne fanno ancora uso, ma, in generale, ora si può contare sul supporto delle unità di misura in tutto il flusso di lavoro.



### Altre migliorie 

-   Ora Importa/Exporta dispone di una propria tabella nella sezione in Modifica \> Preferenze. Tutti i formati di file sono raggruppati nella propria scheda per agevolare la definizione delle opzioni.
-   Le scorciatoie da tastiera personalizzate ora accettano combinazioni fino a 4 tasti.
-   Ora FreeCAD [supporta VR Occulus Rift device](http://forum.freecadweb.org/viewtopic.php?f=9&t=7715).
-   Supporto di barre degli strumenti personalizzate globali: Oltre ad aggiungere delle barre degli strumenti personalizzate con i propri strumenti per ogni ambiente di lavoro, ora è anche possibile aggiungere barre degli strumenti personalizzate che rimangono presenti in tutti gli ambienti.
-   Nuovo Lib Pack per Windows, con l\'ultima versione di OCE 0.17



## Ambiente Part 

-   Sono stati aggiunti alcuni nuovi elementi geometrici: Parabola, Arco di parabola, Iperbole e Arco di iperbole



## Ambienti Part Design e Sketcher 



### Ellissi

Ora [Sketcher](Sketcher_Workbench/it.md) possiede un adeguato supporto per le ellissi. Esse possono essere costruite in vari modi, e possono essere utilizzate per qualsiasi tipo di operazione successiva.

![](images/Ellipse-example.png )



### Strumenti di selezione avanzati 

In Sketcher è stata implementata una serie di nuovi strumenti per facilitare la diagnosi, ottimizzare o risolvere i problemi negli schizzi. Ora è possibile, ad esempio, selezionare facilmente gli elementi associati a un vincolo, o selezionare il vincolo associato ad un elemento, oppure trovare i vincoli in conflitto o ridondanti.

All\'interfaccia utente di Sketcher sono stati aggiunti alcuni nuovi pannelli, e ora è visibile un elenco selezionabile degli elementi dello schizzo.



### Unire schizzi 

Ora è possibile unire diversi schizzi in uno solo cliccando semplicemente su un pulsante.



### Maggiori proprietà di schizzo 

La visualizzazione delle proprietà degli oggetti di Schizzo è stata migliorata e i vincoli del disegno denominati Dati (distanza, distanza orizzontale, distanza verticale) ora appaiono nella scheda delle proprietà e sono modificabili direttamente, senza dover entrare nella modalità di modifica.



### Altre migliorie minori 

-   Sono stati aggiunti diversi poligoni regolari a schizzo
-   Sono stati aggiunti dei nuovi vincoli: il vincolo Simmetria perpendicolare agli assi di simmetria



## Ambiente Spreadsheet 

L\'ambiente [Spreadsheet](Spreadsheet_Workbench/it.md) è stato completamente ricodificato. Ora FreeCAD possiede un editor di fogli di calcolo a regola d\'arte, robusto e ricco di funzionalità. Un paio di funzionalità presenti nella versione precedente di questo ambiente sono state rimosse, come ad esempio il controller di proprietà, ma questo è un problema complesso che richiede altro tempo per progettarlo correttamente. Al momento, tuttavia, il nuovo foglio di calcolo offre già delle possibilità di gran lunga migliori delle precenti per raccogliere i dati dal modello.

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:640px;">



## Ambiente Draft 



### Consente di incollare i caratteri in ShapeString 

Per i nostalgici del vecchio software CAD, ora con lo strumento [Forma da testo](Draft_ShapeString/it.md) si possono utilizzare i font adesivi (in cui le lettere sono composte da semplici linee, e non da forme piene).

![](images/Stickyfonts.jpg )



### Altre migliorie minori 

-   Le [Linee](Draft_Line/it.md) possono essere definite dalla loro lunghezza e dall\'angolo nel piano di lavoro attuale
-   Linee di estensione relative per la [Quotatura](Draft_Snap_Dimensions/it.md)
-   Supporto per [schizzo ellissi](Sketcher_CompCreateConic/it.md)
-   Gli oggetti [Array](Draft_Array/it.md) (Schiere) possono essere fusi



## Ambiente Draft 



### Esportare le pagine di Disegno in DXF 

Il sistema utilizzato fino ad ora per esportare le pagine di Disegno in DXF era un trucco molto complicato per convertire prima il codice SVG dell\'oggetto FreeCAD e poi convertirlo in DXF con l\'esportatore di Draft. Ora, l\'esportazione avviene all\'interno del modulo Drawing, più velocemente e con risultati più affidabili. L\'eportazione DXF ora utilizza un modello di sistema simile a quello dei fogli SVG. Se la pagina di Disegno utilizza un dato modello SVG, e nella stessa posizione è disponibile un modello DXF con lo stesso nome, esso viene utilizzato per generare il file DXF.

![](images/Drawing-dxf-export.jpg )

Nel file DXF, le diverse viste sono collocate come blocchi scalati. Questo consente di ripristinare rapidamente la scala 1: 1.



### Altre migliorie minori 

-   Ora è possibile riutilizzare le impostazioni della proiezione di una vista esistente durante la creazione di nuove viste.



## Ambiente Arch 



### Aggiornato l\'importatore/esportatore IFC 

L\'importatore [IFC](Arch_IFC/it.md) di FreeCAD ha ricevuto un sacco di lavoro e test, e un aggiornamento massivo. Il vecchio importatore, basato su python, è stato disabilitato, ma è ancora utilizzabile dalla console python, e FreeCAD ora utilizza esclusivamente e intensamente quello nuovo, bleeding-edge [version 5](http://ifcopenshell.org/python.html) ([read more](http://ifcopenshell.org/pythonOCC/example1/) about it) di [IfcOpenShell](http://ifcopenshell.org/) che ora è disponibile per tutte le piattaforme principali (assicuratevi di scaricare la versione che corrisponde alla versione di python utilizzata per l\'installazione di FreeCAD). Ora beneficiamo di una importazione o esportazione molto più veloce e affidabile, di un codice molto più semplice e più chiaro (leggi: più semplice da estendere), e anche di alcuni prodotti aggiuntivi, come un miglior supporto per gli oggetti basati su curve e proprietà IFC.



### Nuova funzionalità: Tagliare un oggetto con piano 

La nuova funzionalità [Taglia con un piano](Arch_CutPlane/it.md) permette di tagliare un oggetto secondo un piano definito dalla faccia di un altro oggetto. È possibile tagliare l\'oggetto dietro o davanti al piano scelto.

![](images/Arch_CutPlane_example.jpg )



### Lo strumento Tetto è stato rinnovato 

Lo strumento [Tetto](Arch_Roof/it.md) è stato completamente rifatto e ora rende possibile definire pendenze diverse per ogni falda del tetto. Inoltre è possibile definire lo spessore di copertura e la larghezza del cornicione.

![](images/RoofExample.png )



### Pannelli

All\'ambiente [Architettura](Arch_Workbench/it.md) è stato aggiunto un nuovo oggetto [Pannello](Arch_Panel/it.md). Esso consente di creare tutti i tipi di oggetti simili a dei pannelli, ed è particolarmente utile per la costruzione di pannelli come quelli dei progetti [wikihouse](http://www.wikihouse.cc/) oppure [popup house](http://www.popup-house.com/).

<img alt="" src=images/Arch_Panel_example.jpg  style="width:640px;">



### Arredamento

Il nuovo oggetto [Arredo](Arch_Equipment/it.md) è stato progettato per aggiungere ai progetti architettonici tutti i tipi di oggetti indipendenti, non strutturali, come gli apparecchi di illuminazione, le attrezzature sanitarie o i mobili.



### Altre migliorie minori 

-   Ora il Punto base (Basepoint) di un oggetto [Telaio](Arch_Frame/it.md) può essere impostato su un determinato vertice del profilo.



## Moduli esterni 

C\'è anche stato un lavoro molto interessante su nuovi ambienti e sulle macro, che non sono (ancora!) integrati nel codice sorgente di FreeCAD, ma che sono facili da installare su una installazione di FreeCAD 0,15 esistente. Le istruzioni sono disponibili sulle seguenti pagine:

### Assembly2

L\'ambiente [Assembly 2 workbench](https://github.com/hamish2014/FreeCAD_assembly2) fornisce gli strumenti per creare degli assemblaggi di più parti, ed è una buona alternativa all\'ambiente ufficiale di Assemblaggio che è ancora in fase di sviluppo (vedere [questa discussione nel forum](http://forum.freecadweb.org/viewtopic.php?f=10&t=8577)).

![](images/Assembly2_example.jpg )

### Drawing Dimensioning 

L\'ambiente [Drawing dimensioning](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) aggiunge dei potenti strumenti di quotatura e di annotazione per l\'ambiente Disegno (vedere [questa discussione nel forum](http://forum.freecadweb.org/viewtopic.php?f=10&t=8395)).

![](images/Drawing_Dimensioning_example.jpg )

### Work Features 

La macro [WorkFeature](https://github.com/Rentlau/WorkFeature) aggiunge una vasta gamma di oggetti di aiuto, come i piani di allineamento e gli assi, e gli strumenti che consentono di posizionare e allineare gli oggetti lungo tali oggetti di supporto (vedere [questa discussione nel forum](http://forum.freecadweb.org/viewtopic.php?f=22&t=9056)).

<img alt="" src=images/WF.png  style="width:640px;">



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.15/it
