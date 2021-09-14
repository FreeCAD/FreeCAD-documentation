# Drawing Workbench/it

 


{{VeryImportantMessage|Lo sviluppo del modulo Drawing è stato interrotto in FreeCAD 0.16 con il proposito di sostituirlo con il nuovo modulo [TechDraw](TechDraw_Workbench/it.md) che sarà introdotto nella versione 0.17. Nella versione 0.17 sono forniti entrambi i moduli, ma il modulo Drawing potrebbe essere rimosso nelle versioni future.}}

<img alt="L\'icona di Drawing" src=images/Workbench_Drawing.svg  style="width:128px;">

## Introduzione

L\'ambiente Disegno (Drawing) consente di trasferire su carta il lavoro realizzato in 3D.

Permette di produrre delle viste (proiezioni sul piano) del modello, di posizionarle in una finestra 2D e di inserire la finestra in una tavola, ad esempio, in un foglio con il bordo, il titolo e il logo e, infine, di stampare la tavola.


{{TOCright}}

<img alt="" src=images/Drawing_extraction.png  style="width:600px;">

## Strumenti

Questi strumenti permettono di creare, configurare e esportare le proiezioni dei solidi come disegni 2D.

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Apri SVG](Drawing_Open_SVG/it.md): apre un foglio di disegno preventivamente salvato in un file SVG.

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Nuovo Disegno A3](Drawing_Landscape_A3/it.md): crea un nuovo disegno su un foglio di default A3 orizzontale di FreeCAD.

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Inserisci vista nel disegno](Drawing_View/it.md): inserisce nel foglio di lavoro attivo una vista in proiezione dell\'oggetto selezionato.

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotazione](Drawing_Annotation/it.md): aggiunge una annotazione al foglio di disegno corrente.

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip/it.md): aggiunge un gruppo di clip al foglio di disegno corrente.

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Apri finestra browser](Drawing_Openbrowser/it.md): apre un\'anteprima del foglio corrente nel browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Inserisci viste ortogonali](Drawing_Orthoviews/it.md): crea automaticamente le viste ortogonali di un oggetto nel foglio di disegno corrente

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Simbolo](Drawing_Symbol/it.md): aggiunge il contenuto di un file in formato SVG come un simbolo nel foglio di disegno corrente

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Vista Draft](Draft_Drawing/it.md): Inserisce una speciale vista Draft dell\'oggetto selezionato nel foglio del disegno corrente

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Vista foglio di calcolo](Drawing_SpreadsheetView/it.md): Inserisce una vista di un foglio di calcolo selezionato nel foglio del disegno corrente

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Esporta pagina](Drawing_Save/it.md): salva il progetto o le sue modifiche in un file SVG.

-   [Proietta le forme](Drawing_ProjectShape/it.md): proietta le forme su un piano, nella vista 3D.

-    **Nota:**lo strumento [Drawing di Draft](Draft_Drawing/it.md) è usabile con oggetti [Draft](Draft_Workbench/it.md). Ha alcune funzionalità aggiuntive rispetto agli strumenti di disegno e supporta oggetti specifici come le [dimensioni di Draft](Draft_Dimension/it.md).

## Flusso di lavoro 

Il documento contiene un oggetto di forma 3D (Schenkel) da si vuole produrre un disegno. Pertanto viene creata una \"Pagina\". Una pagina è istanziata da un modello, ad esempio il modello \"A3\_Landscape\". Il modello è un documento [SVG](SVG/i.md) che può contenere una cornice di pagina, un logo e altri elementi.

Nella pagina si possono inserire una o più viste. Ogni vista ha una posizione nella pagina, un fattore di scala (proprietà di scala) e delle proprietà aggiuntive. Ogni volta che la pagina, la vista o l\'oggetto a cui si fa riferimento subiscono delle modifiche, la pagina viene rigenerata e viene anche aggiornata la sua visualizzazione.

## Script

Per ora le funzioni offerte dall\'interfaccia grafica (GUI) sono molto limitate, quindi gli script API sono più interessanti.

Vedere la pagina [Esempi dell\'API di Drawing](Drawing_API_example/it.md) per una descrizione delle funzioni utilizzate per creare pagine e viste di disegno.

Lo script [Macro\_CartoucheFC](Macro_CartoucheFC/it.md) permette di compilare agevolmente la tabella del modello di tavola FreeCAD A3\_Landscape.

## Modelli di squadrature 

FreeCAD viene fornito con una serie di modelli di pagina predefiniti, ma si possono trovare altri modelli in [Modelli di squadrature](Drawing_templates/it.md).

## Estendere il modulo Drawing 

Alcune ulteriori note sulla programmazione del Modulo Disegno sono contenute nella pagina [Drawing Documentation (en)](Drawing_Documentation.md) [Drawing Documentation (it)](Drawing_Documentation/it.md). Dette note aiutano a capire rapidamente come lavora questo modulo e permettono ai programmatori di avviare rapidamente la programmazione per esso.

## Tutorial

-   [Drawing tutorial](Drawing_tutorial/it.md)

## Link esterni 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)





{{Drawing Tools navi

}} 

[Category:Obsolete Workbenches](Category:Obsolete_Workbenches.md)
