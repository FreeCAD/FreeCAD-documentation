# FEM Shear of a Composite Block/it
---
 TutorialInfo:t
   Topic:  Analisi agli elementi finiti
   Level:  Base/Intermedio
   Time:  30 minuti
   Author: http://www.freecadweb.org/wiki/index.php?title=User: HarryvL
   FCVersion: 0.17.12960 o superiore
}}

## Introduzione

In questo tutorial si analizza la deformazione di taglio di un blocco composito costituito da un nucleo rigido incorporato in una matrice morbida. Dimostra l\'uso di BooleanFragments e CompoundFilter per creare solidi per il blocco e la matrice da due cubi concentrici. Questo flusso di lavoro assicura che MeshRegions, Materiali e Condizioni Limite separate possano essere definite per il blocco e la matrice circostante. Per selezionare le regioni interne, viene usata la macro di Markus Hovorka . I risultati CalculiX mostrano chiaramente l\'effetto del nucleo rigido sulla risposta del blocco composito.

## Geometria

Per prima cosa creare due cubetti concentrici, uno di 10 mm e l\'altro di 5 mm. Questo viene fatto nel ambiente \"Part\". Per impostazione predefinita, il cubo viene posizionato all\'origine \0, 0, 0\, quindi il cubo più piccolo deve essere ridimensionato e spostato modificando le impostazioni nella scheda Dati del pannello delle proprietà. Per rendere visibile il nucleo, la Trasparenza del blocco esterno è impostata su 50 nella scheda Visualizza del pannello delle proprietà. Il risultato è mostrato sotto.

!{width="700"}

Quindi evidenziare i due blocchi nell\'albero e creare un oggetto BooleanFragments . Nella \"Finestra delle proprietà - Scheda dati\" cambiare la Modalità in CompSolid. Ora evidenziare i BooleanFragments nella struttura ad albero degli oggetti e creare un CompoundFilter .

!{width="700"}

## Mesh e Regioni di Mesh 

Dall\'ambiente FEM crere un Contenitore di analisi. Questo conterrà tutte le definizioni richieste per l\'analisi CalculiX e i suoi risultati. Notare che questo contenitore di analisi deve essere attivato  ogni volta che si carica nuovamente il file o si torna indietro da altre analisi. Per avviare il processo di mesh, evidenziare CompoundFilter nella struttura ad albero e attivare la finestra di dialogo mesh \"Mesh , FEM mesh da forma con Gmsh\". Uscire dalla finestra di dialogo facendo clic su OK.

Viene creato un oggetto Mesh nell\'albero degli oggetti. Evidenziare questo oggetto e creare un oggetto Regione Mesh tramite \"Mesh , Regione di mesh FEM\". Aprire la finestra di dialogo per questa regione mesh facendo doppio clic e selezionare il pulsante di opzione per Solid. Quindi fare clic sul pulsante \"Aggiungi riferimento\" e selezionare l\'oggetto CompoundFilter nella finestra grafica. Questo dovrebbe aggiungere un riferimento a \"CompoundFilter:Solid1\" nell\'elenco degli oggetti della regione mesh. Infine, specificare la dimensione massima dell\'elemento per questa regione . Uscire dalla finestra di dialogo facendo clic su OK.

!{width="700"}

Quindi creare un nuovo oggetto mesh come sopra e usare la macro di selezione  per selezionare l\'oggetto Cube_Core nella finestra grafica. Questa volta la lista di riferimento dovrebbe mostrare \"CompoundFilter: Solid2\", come sotto. Scegliere una dimensione massima dell\'elemento di 1 mm.

Nota1: La selezione di \"CompoundFilter:Solid2\" richiede la selezione di una delle sue facce.

Nota2: Se si hanno difficoltà a selezionare \"CompoundFilter:Solid2\" può essere perché ci si è dimenticati di impostare la modalità BooleanFragments su CompSolid.

!{width="700"}



## Assegnazione del materiale 

Il materiale viene assegnato alle regioni mesh tramite un oggetto SolidMaterial. In questo tutorial assegniamo due materiali; uno per il contenitore e uno per il contenuto.

Iniziare selezionando il CompoundFilter nell\'albero degli oggetti. Quindi creare un oggetto SolidMaterial tramite l\'opzione di menu \"Modello , Materiale FEM per solido\". Aprire la finestra di dialogo e spuntare il pulsante di opzione per Solid, premere \"Aggiungi riferimento\" e selezionare l\'oggetto CompoundFilter dalla finestra grafica. L\'elenco dei riferimenti ora dovrebbe mostrare \"CompoundFilter:Solid1\", come primo. Assegnare il materiale ABS al contenitore, con un modulo di Young che è circa l\'1% di quello dell\'acciaio.

!{width="700"}

Ripetere la procedura precedente per il contenuto  con l\'aiuto della macro di selezione. Questa volta assegnare CalculiX-Steel, che è molto più rigido del materiale ABS del contenitore.



## Supporto scorrevole 

Per creare una condizione di \"taglio semplice\" per il blocco composito, le deformazioni ai margini devono essere non vincolate. Per ottenere ciò, il blocco viene posizionato su un supporto scorrevole. Questo lascia tre gradi di libertà nel piano del supporto  e questi saranno vincolati in seguito. . Per creare una condizione del contorno scorrevole, aggiungere un oggetto FemConstraintDisplacement . Con la finestra di dialogo aperta, selezionare prima la faccia a cui applicare le condizioni al contorno e quindi fare clic sul pulsante Aggiungi. Poiché il blocco può scorrere sul piano x-y, selezionare solo il pulsante di opzione \"Fixed\" per \"Displacement z\" e lasciare \"Free\" gli altri pulsanti di opzione.

!{width="700"}



## Nodi fissi 

Per evitare movimenti del corpo rigido nel piano di scorrimento, è necessario eliminare tre gradi di libertà indipendenti. Per ottenere ciò, vincolare un vertice nel piano di scorrimento in direzione x e y  e un vertice nella direzione x . A tale scopo creare due ulteriori oggetti FemConstraintDisplacement e si ottiene il risultato mostrato sotto.

!{width="700"}

## Forze di taglio 

Il passo finale nella definizione dell\'analisi è l\'applicazione dei carichi. Per creare una condizione di taglio semplice, applicare una serie di carichi di taglio come mostrato sotto. Ogni carico viene scelto come 1000 N e considerando le direzioni di applicazione, l\'equilibrio di forza e momento viene raggiunto per tutti i gradi di libertà di traslazione e rotazionali. In FreeCAD ciò richiede l\'aggiunta di quattro oggetti FemConstraintForce  - uno per ogni faccia. Con la finestra di dialogo aperta, premere prima il pulsante Aggiungi riferimento e quindi selezionare la faccia a cui applicare la condizione al contorno . Di default, questo crea un insieme di forze perpendicolari alla faccia . Per modificare questo valore in una forza di taglio, premere il pulsante di direzione e selezionare un bordo del cubo che è nella direzione desiderata. Se la forza risultante punta in direzione opposta a quella richiesta, selezionare il pulsante di opzione \"Direzione invertita\".

!{width="700"}



## Analisi CalculiX 

Ora sono state definite tutte le regioni di mesh, il materiale e le condizioni al contorno, siamo pronti ad analizzare la deformazione del blocco con CalculiX. Attivare l\'analisi facendo clic con il pulsante destro del mouse su \"Attiva analisi\", aprire la finestra di dialogo CalculiX facendo doppio clic sull\'oggetto CalculiXccxTools e selezionare una directory per i file temporanei creati da FC e CCX. Scrivere il file di input CCX e controllare eventuali avvisi o messaggi di errore.

!{width="700"}

Successivamente l\'analisi può essere avviata premendo il pulsante RunCalculiX. Se tutto va bene, la finestra di output CCX dovrebbe mostrare i seguenti messaggi.

!{width="700"}



## Risultati di CalculiX 

Al termine dell\'analisi, fare doppio clic sull\'oggetto \"CalculiX_static_results\" e selezionare l\'opzione \"Abs displacement\". Lo spostamento massimo di \~ 0.08mm vene visualizzato nella relativa casella di output. Poiché lo spostamento massimo è relativamente piccolo rispetto alle dimensioni del blocco , gli spostamenti devono essere ridimensionati. Questo può essere fatto sotto il titolo \"Displacement\" spuntando il pulsante di opzione \"Show\" e ridimensionando lo spostamento di un fattore di \"diciamo\" 20. Lo spostamento massimo ora è esagerato a circa il 20% delle dimensioni del cubo. Dopo aver chiuso la finestra di dialogo, la mesh deformata può essere resa nuovamente visibile evidenziando l\'oggetto Result_mesh e premendo la barra spaziatrice.

!{width="700"}

Per studiare la deformazione del nucleo bisogna tagliare il blocco. Questo può essere fatto creando un filtro clip. Per attivare questa funzionalità, bisogna prima creare una \"pipeline di post processing\" evidenziando l\'oggetto \"CalculiX_static_results\" e scegliendo \"Risultati , Pubblica pipeline dal risultato\" dal menu. Successivamente, con la Pipeline selezionata creare un filtro Warp , impostare Vector=Displacement e Value=20 per ridimensionare lo spostamento e Display Mode = \"Surface with Edges\", Coloring Field = \"Displacement\", Vector = \"Magnitude\" per mostrare i contorni di spostamento colorati. Premere Applica e OK. Come passaggio finale, aggiungere un filtro clip  e creare un piano con origine \5.0,2.5,5.0\ e normale \0,1,0\, cioè su una faccia centrale con la normale nella direzione y. Selezionare il pulsante di opzione \"Cut Cells\" per creare una superficie piatta. Come prima impostare Display Mode = \"Surface with Edges\", Coloring Field = \"Displacement\", Vector = \"Magnitude\" per mostrare i contorni di spostamento colorati. Premere Applica e OK. Infine, attivare il filtro Warp su invisibile per mostrare solo il blocco tagliato.

!.png "Figure12_Deformed_Mesh_Clipped_View_.png"){width="700"}

Dal risultato è chiaro che il nucleo rimane in gran parte indeformato e aiuta il contenitore morbido a resistere alla deformazione . Ciò che evidenzia, tuttavia, è che, in condizioni di taglio semplice, le facce del blocco composito si deformano, il che implica che la condizione al contorno scorrevole alla base del cubo fornisce un vincolo eccessivo.



## Ulteriori lavori 

Le seguenti sfide possono essere interessanti da svolgere come ulteriore esercizio:

1\) Correggere il vincolo eccessivo imposto dalla condizione al contorno scorrevole

2\) Provare a creare le condizioni al contorno del contatto tra il nucleo e la matrice per vedere se avviene la separazione

Il file FC per questo tutorial è riportato sotto, come punto di partenza.

<https://forum.freecadweb.org/viewtopic.php?f=18&t=26517&start=20>

Divertiti !


{{FEM Tools navi

}} {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Shear of a Composite Block/it
