# Manual:Preparing models for 3D printing/it
{{Manual:TOC/it}}

Uno dei principali utilizzi di FreeCAD è quello di produrre oggetti del mondo reale. Questi possono essere progettati in FreeCAD, e poi essere resi reali in diversi modi, come ad esempio comunicati ad altre persone che poi li costruiscono, o, sempre più frequentemente, inviati direttamente ad una [stampante 3D](https://en.wikipedia.org/wiki/3D_printing) o ad una [macchina CNC](https://en.wikipedia.org/wiki/Milling_%28machining%29). In questo capitolo viene spiegato come ottenere dei modelli pronti per essere inviati a queste macchine.

Se siete stati oculati durante la modellazione, la maggior parte degli inconvenienti che si possono verificare durante la stampa in 3D del modello sono già stati evitati. Questo richiede fondamentalmente:

-   Fare in modo che gli oggetti 3D sono **solidi**. Gli oggetti del mondo reale sono solidi, anche il modello 3D deve essere solido. Abbiamo visto nei capitoli precedenti che FreeCAD aiuta molto in questo proposito, e che l\'ambiente [PartDesign](PartDesign_Workbench/it.md) vi avvisa se fate un\'operazione che impedisce al vostro modello di rimanere solido. L\'ambiente [Part](Part_Workbench/it.md) contiene anche lo strumento <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Controlla geometria](Part_CheckGeometry/it.md) che è comodo per controllare ulteriormente se ci sono difetti.
-   Essere sicuri delle **dimensioni** degli oggetti. Un millimetro sarà un millimetro nella realtà. Ogni dimensione è importante.
-   Controllare il **degrado**. Nessuna stampante 3D o nessun sistema di fresatura CNC può ricevere direttamente i file di FreeCAD. La maggior parte di essi capiranno solo un linguaggio macchina chiamato [G-Code](https://en.wikipedia.org/wiki/G-code). G-code ha decine di dialetti diversi, ogni macchina o venditore di solito utilizza il proprio. La conversione dei modelli in G-Code può essere facile e automatica, ma si può anche farla manualmente, con il controllo totale sull\'output. In ogni caso, durante il processo avverrà inevitabilmente una perdita di qualità del modello. Quando si stampa in 3D, è sempre necessario assicurarsi che questa perdita di qualità stia sotto i propri requisiti minimi.

Da qui in avanti, si suppone che i primi due criteri siano soddisfatti, e che ormai si è in grado di produrre oggetti solidi di dimensioni corrette. Vediamo ora come affrontare il terzo punto.



### Esportare nello slicer 

Questa è la tecnica più utilizzata per la stampa 3D. L\'oggetto 3D viene esportato in un altro programma ( lo slicer, l\'affettatrice) che genera il G-codice dall\'oggetto, affettando in strati sottili (da qui il nome), che riproducono i movimenti che la stampante 3D farà. Poiché molti di tali stampanti sono di tipo proprietario, ci sono spesso piccole differenze da una all\'altra. Questi programmi di solito offrono la possibilità di configurazioni avanzate che permettono di adattare l\'uscita esattamente per le funzioni della propria stampante 3D.

Anche se la stampa 3D è un soggetto troppo vasto per questo manuale, vedremo come esportare e utilizzare questi slicer per verificare che l\'uscita sia corretta.



### Convertire gli oggetti in mesh 

Alla data attuale, nessuno degli slicer è in grado di ricevere direttamente la geometria solida come viene prodotta in FreeCAD. Quindi è necessario convertire prima qualsiasi oggetto che si desideri stampare in 3D in un [mesh](https://en.wikipedia.org/wiki/Polygon_mesh), che apribile dallo slicer. Fortunatamente, anche se convertire un mesh in un solido è un\'operazione complicata, al contrario, convertire un solido in un mesh, è molto semplice. Tutto quello a cui bisogna stare attenti è che ora si verifica il degrado di cui abbiamo parlato in precedenza. Bisogna controllare che il degrado rimanga all\'interno di limiti accettabili.

Tutta la manipolazione delle mesh, in FreeCAD, è fatta da un\'altro specifico ambiente di lavoro, l\'ambiente [Mesh](Mesh_Workbench/it.md). Questo ambiente contiene, oltre a quelli più importanti, gli strumenti che convertono tra oggetti Parte e oggetti mesh, diverse utility per analizzare e riparare le mesh. Anche se si lavorare con le mesh non è il focus di FreeCAD, quando si lavora con la modellazione 3D, è spesso necessario aver a che fare con gli oggetti mesh, dato che il loro uso è molto diffuso tra le altre applicazioni. Questo ambiente di lavoro consente di gestirle completamente in FreeCAD.

-   Andiamo a convertire uno degli oggetti modellati nei capitoli precedenti, come ad esempio il pezzo di Lego (che può essere scaricato dal link posto dalla fine del capitolo precedente).
-   Aprire il file FreeCAD che contiene il pezzo lego.
-   Passare all\'ambiente [Mesh](Mesh_Workbench/it.md)
-   Selezionare il mattoncino Lego
-   Selezionare il menu **Meshes → Crea Mesh da Forma**
-   Si apre un pannello delle attività con diverse opzioni. Alcuni algoritmi di meshing aggiuntivi (Mefisto o NetGen) potrebbero non essere disponibili, secondo come è stata compilata la versione di FreeCAD. L\'algoritmo standard di meshing è sempre presente. Esso offre meno possibilità rispetto agli altri due, ma è del tutto sufficiente per oggetti di piccole dimensioni che rientrano nel massimo formato di stampa di una stampante 3D.

![](images/Exercise_meshing_01.jpg )

-   Selezionare il mesher **Standard**, e lasciare il valore della deviazione per il valore di default di **0.10**. Premere **Ok**.
-   Viene creato un oggetto mesh, esattamente sopra al nostro oggetto solido. Nascondere il solido, oppure spostare uno degli oggetti, in modo da poterli confrontare.
-   Cambiare la proprietà **View → Display Mode** del nuovo oggetto mesh in **Flat Lines**, per vedere che aspetto ha la triangolazione.
-   Se non si è soddisfatti, e si pensa che il risultato è troppo grossolano, è possibile ripetere l\'operazione, abbassando il valore dalla deviazione. Nell\'esempio che segue, nella mesh di sinistra si è utilizzato il valore di default di **0.10**, mentre in quella di destra si è utilizzato il valore **0.01**:

![](images/Exercise_meshing_02.jpg )

Nella maggior parte dei casi, però, i valori di default danno un risultato soddisfacente.

-   Ora possiamo esportare la mesh in un formato mesh, come [STL](https://en.wikipedia.org/wiki/STL_%28file_format%29), che è attualmente il formato più utilizzato nella stampa 3D, utilizzando il menu **File → Esporta** e scegliendo il formato di file STL.

Se non si possiede una stampante 3D, di solito è molto facile trovare dei servizi commerciali che stampano e inviano gli oggetti stampati per posta. Tra i più famosi ci sono [Shapeways](http://www.shapeways.com/) e [Sculpteo](http://www.sculpteo.com/), ma di solito è facile trovarne molti altri nella propria città. In tutte le grandi città al giorno d\'oggi si trovano i [Fab labs](https://en.wikipedia.org/wiki/Fab_lab), che sono negozi dotati di una serie di macchine per la produzione 3D, compresa quasi sempre almeno una stampante 3D. I laboratori Fab sono solitamente degli spazi comunitari, che vi permettono di utilizzare le loro macchine, a pagamento o gratuitamente a seconda dei Fab Lab, ma che vi insegnano anche come usarle, e che promuovono altre attività relative alla produzione 3D.



### Utilizzare Slic3r 

[Slic3r](http://slic3r.org/) è un\'applicazione che converte gli oggetti STL in G-code che possono essere inviati direttamente alle stampanti 3D. Come FreeCAD, è gratuito, open-source e funziona su Windows, Mac OS e Linux. Configurare correttamente le cose per la stampa 3D è un processo complicato, in cui è necessario avere una buona conoscenza della stampante 3D, quindi non è molto utile generare il codice G prima di poter realmente andare in stampa (il file G-code potrebbe non funzionare bene su un\'altra stampante), ma per noi è comunque utile, per controllare che il file STL possa essere stampato senza problemi.

Questo è il nostro file STL esportato e aperto in Slic3r. Usando il scheda **anteprima**, e spostando il cursore a destra, possiamo visualizzare il percorso che la testina di stampa 3D seguirà per costruire il nostro oggetto.

![](images/Exercise_meshing_03.jpg )



### Utilizzare l\'addon Cura 

[Cura](https://ultimaker.com/en/products/cura-software) è un\'altra applicazione slicer free e open-source per Windows, Mac e Linux, gestita dal produttore di stampante 3D [Ultimaker](https://ultimaker.com). Alcuni utenti di FreeCAD hanno creato un [Cura Workbench](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin) che utilizza Cura internamente. L\'ambiente Cura è disponibile dal repositorio [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons). Per utilizzare l\'ambiente Cura è necessario installare anche Cura stesso, che non è incluso nell\'ambiente.

Dopo aver installato sia Cura, sia l\'ambiente Cura, si è in grado di usarlo per produrre il file G-code direttamente dagli oggetti Parte, senza la necessità di convertirli in mesh, e senza la necessità di aprire un\'applicazione esterna. La produzione di un altro file G-code dal nostro mattoncino Lego, utilizzando questa volta l\'ambiente Cura, è fatta nel seguente modo:

-   Caricare il file che contiene il mattoncino Lego (può essere scaricato dal link posto alla fine del capitolo precedente)
-   Passare all\'ambiente [Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   Imposta lo spazio di stampa scegliendo il menu **3D printing -\> Create a 3D printer definition**. Dato che non stiamo stampando veramente, possiamo lasciare le impostazioni così come sono. Nella vista 3D viene mostrata la geometria del piano di stampa e lo spazio disponibile.
-   Spostare il mattoncino Lego in una posizione adatta, ad esempio il centro del piano di stampa. Ricordare che gli oggetti PartDesign non possono essere spostati direttamente, quindi è necessario spostare il suo primo schizzo (il primo rettangolo), oppure spostare (e stampare) una copia, che può essere fatta con lo strumento [Parte → Crea una copia semplice](Part_SimpleCopy/it.md). La copia può essere spostata, per esempio con <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft → Sposta](Draft_Move/it.md).
-   Selezionare l\'oggetto da stampare, e poi selezionare il menu **3D printing → Slice with Cura Engine**.
-   Nel pannello delle Azioni che si apre, assicurarsi che il percorso del file eseguibile Cura sia impostato correttamente. Dato che in realtà non abbiamo intenzione di stampare , possiamo lasciare tutte le altre opzioni come sono. Premere **Ok**. Nella stessa directory del file di FreeCAD vengono generati due file, un file STL e un file G-code.

![](images/Exercise_meshing_05.jpg )

-   Il G-code generato può anche essere re-importato in FreeCAD (utilizzando il preprocessore slic3r) per il controllo.

### Generare il G-code 


**'''Warning:''' Questa sezione è stata realizzata per FreeCAD 0.16. Sono stati apportati cambiamenti significativi alla creazione del percorso. Si prega di fare riferimento alla documentazione dell'ambiente [Path](Path_Workbench/it.md) in generale o al tutorial della [procedura per path](Path_Walkthrough_for_the_Impatient/it.md)!**

FreeCAD offre anche modi più avanzati per generare direttamente il G-code. Questo è spesso molto più complicato rispetto all\'utilizzo di strumenti automatici come abbiamo visto sopra, ma ha il vantaggio di permettere di controllare completamente l\'uscita. Di solito questo è non necessario quando si utilizzano stampanti 3D, ma diventa molto importante quando si tratta di fresatrici CNC, che sono macchine molto più complesse.

In FreeCAD la generazione del percorso G-code è fatta con l\'ambiente [Path](Path_Workbench/it.md). Esso è dotato di strumenti che generano percorsi macchina completi e altri che generano solo parti di un progetto G-code, che possono essere assemblati per formare delle operazioni complesse di fresatura.

La generazione di percorsi di fresatura CNC è un altro argomento troppo grande per essere affrontato in questo manuale, quindi vediamo ora come costruire un progetto Path semplice, senza preoccuparci molto della maggior parte dei dettagli di una vera lavorazione CNC.

-   Caricare il file che contiene il pezzo di Lego, e passare all\'ambiente [Path](Path_Workbench/it.md).
-   Dato che il pezzo finale non contiene più nessuna faccia piana rettangolare, nascondere il pezzo lego finale, e mostrare il primo pad cubico fatto, che ha la faccia superiore rettangolare.
-   Selezionare la faccia superiore e premere il pulsante <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Profilo](Path_Profile/it.md).
-   Impostare la sua proprietà **Offset** a 1mm.

![](images/Exercise_path_01.jpg )

-   Poi, duplichiamo questo primo ciclo alcune volte, in modo che lo strumento ritagli l\'intero blocco. Selezionare il percorso Profile, e premere il pulsante <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Matrice](Path_Array/it.md).
-   Impostare la proprietà **Copies** della matrice a 8, e il suo **Offset** a -2mm nella direzione Z , e spostare il posizionamento della matrice di 2 mm in direzione Z, in modo che il taglio inizi poco sopra il pad, e comprenda anche l\'altezza delle bugne.

![](images/Exercise_path_02.jpg )

-   Abbiamo definito un percorso che, quando seguita dalla fresatrice, intaglierà un volume rettangolare da un blocco di materiale. Ora bisogna intagliare lo spazio tra le bugne, per renderle evidenti. Nascondere il Pad, e mostrare di nuovo il pezzo finale, in modo che si possa selezionare la faccia che si trova tra le bugne.
-   Selezionare la faccia superiore, e premere il pulsante <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Tasca](Path_Pocket_Shape/it.md). Impostare la proprietà **Offset** a 1mm, e la **retraction height** a 20mm. Questo è l\'altezza a cui l\'utensile viaggerà nel passaggio da un ciclo all\'altro. Altrimenti, l\'utensile può tagliare una delle bugne:

![](images/Exercise_path_03.jpg )

-   Fare una nuova matrice. Selezionare l\'oggetto Pocket, e premere il pulsante <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Matrice](Path_Array/it.md). Impostare il numero di **Copies** a 1 e un **offset** di -2 mm nella direzione Z. Spostare il posizionamento della matrice di 2 mm in direzione Z. Le due operazioni svolte:

![](images/Exercise_path_04.jpg )

-   Ora tutto ciò che rimane da fare è unire queste due operazioni in una sola. Questo può essere fatto con una [Lavorazione](Path_Job/it.md). Premere il pulsante <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Lavorazione](Path_Job/it.md).
-   Impostare la proprietà **Usa Posizionamento** del progetto su True, perché cambiamo il posizionamento delle matrici, e vogliamo che questo sia preso in considerazione nel progetto.
-   Nella visualizzazione ad albero, trascinare e rilasciare i due array nel progetto. Se necessario, è possibile riordinare le matrici all\'interno del progetto facendo un doppio clic su di esso.
-   Il progetto può essere esportato in codice G, selezionandolo, scegliendo menù **File -\> Esporta**, selezionando il formato G-code, e nella finestra di pop-up che si apre, selezionando uno script di post-elaborazione in base alla macchina.

Per simulare il taglio vero sono molte disponibili applicazioni, una di queste, che è anche multi-piattaforma e open-source come FreeCAD, è [Camotics](http://camotics.org/).

**Download**

-   Il file STL generato in questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   Il file generato durante questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Il file G-code generato in questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Approfondimenti**

-   [L\'ambiente Mesh](Mesh_Workbench/it.md)
-   [The STL file format](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [The Cura Workbench](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [L\'ambiente Percorso](Path_Workbench/it.md)
-   [Camotics](http://camotics.org/)



### Video

-   [How To Use FreeCAD For 3D Printing \| Using The Realthunder Branch](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) Una playlist video di Maker Tales su come utilizzare FreeCAD per la stampa 3D.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Category_Path.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/it
