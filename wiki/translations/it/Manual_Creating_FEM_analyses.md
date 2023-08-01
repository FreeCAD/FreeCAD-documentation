# Manual:Creating FEM analyses/it
{{Manual:TOC/it}}

FEM sta per [Finite Element Method](https://en.wikipedia.org/wiki/Finite_element_method) (metodo degli elementi finiti). Si tratta di un vasto argomento di matematica, ma in FreeCAD possiamo riassumerlo come un modo per calcolare le propagazioni all\'interno di un oggetto 3D, tagliandolo in piccoli pezzi, e analizzando l\'impatto di ogni piccolo pezzo rispetto a quelli vicini. Questo ha diversi utilizzi nei campi dell\'ingegneria e dell\'elettromagnetismo, ma qui vedremo in modo più approfondito il suo utilizzo già ben sviluppato in FreeCAD, per simulare le deformazioni negli oggetti che sono sottoposti a forze e pesi.

In FreeCAD tale simulazione è fatta con l\'ambiente [FEM](FEM_Workbench/it.md). Si tratta di diverse fasi: preparare la geometria, impostare il suo materiale, eseguire la meshing, dividere in parti più piccole, come abbiamo fatto nel capitolo [Preparare gli oggetti per la stampa 3D](Manual:Preparing_models_for_3D_printing/it.md), ed infine calcolare la simulazione.

<img alt="" src=images/Exercise_fem_01.jpg  style="width:600px;">



### Preparare FreeCAD 

La simulazione vera e propria viene effettuata con un altro pezzo di software, che viene utilizzato da FreeCAD per ottenere i risultati. Dato che ci sono diverse interessanti applicazioni FEM open-source di simulazione disponibili, l\'ambiente [FEM](FEM_Workbench/it.md) è stato costruito in modo da poterne utilizzare più di una. Tuttavia, per ora è pienamente implementato solo [CalculiX](http://www.calculix.de/). È anche necessario un altro pezzo di software, chiamato [NetGen](https://sourceforge.net/projects/netgen-mesher/), che è responsabile della generazione della suddivisione in maglie. Le istruzioni dettagliate per l\'installazione di questi due componenti sono fornite nella [documentazione di FreeCAD](FEM_Install/it.md).



### Preparare la geometria 

Utilizzeremo la casa modellata nel capitolo [Modellazione BIM](Manual:BIM_modeling/it.md). Tuttavia, devono essere fatte alcune modifiche per rendere il modello adatto ai calcoli FEM. Si tratta, in sostanza, di scartare gli oggetti che non vogliamo includere nel calcolo, come ad esempio la porta e la finestra, e di unire tutti gli oggetti rimanenti in uno solo.

-   Caricare il [modello di casa](https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd) creato in precedenza
-   Eliminare o nascondere l\'oggetto pagina, i piani di sezione e le dimensioni, in modo che rimanga solo con il modello
-   Nascondere la finestra, la porta e la soletta del piano terra
-   Nascondere anche le travi di metallo del tetto. Dato che sono oggetti molto diversi dal resto della casa, non includendoli si semplifica il calcolo. Invece, considereremo il solaio di copertura come se fosse posto direttamente sulla parte superiore delle pareti.
-   Ora spostare la soletta del tetto verso il basso in modo che appoggi sulla parte superiore delle pareti: modificare l\'oggetto **Rettangolo** usato come base del solaio di copertura, e cambiare il suo valore **Placement-\>Position-\>X** da 3.18 m a 3.00 m
-   Ora il modello è ripulito:

:   <img alt="" src=images/Exercise_fem_02.jpg  style="width:600px;">

-   Attualmente l\'ambiente FEM può calcolare solo le deformazioni su un singolo oggetto. Pertanto, bisogna unire i due oggetti (il muro e la soletta). Passare nell\'ambiente [Part](Part_Workbench/it.md), selezionare i due oggetti, e premere il pulsante **<img src="images/Part_Fuse.svg" width=16px> [Unione](Part_Union/it.md)**. Ora abbiamo ottenuto un oggetto fuso:

:   <img alt="" src=images/Exercise_fem_03.jpg  style="width:600px;">



### Creare l\'analisi 

-   Ora siamo pronti per iniziare una analisi FEM. Passare all\'ambiente [FEM](FEM_Workbench/it.md)
-   Selezionare l\'oggetto fuso
-   Premere il pulsante **<img src="images/FEM_Analysis.svg" width=16px> [Nuova analisi](FEM_Analysis/it.md)
**
-   Viene creata una nuova analisi e si apre un pannello per le impostazioni. Qui è possibile definire i parametri di meshing da utilizzare per produrre la mesh FEM. L\'impostazione principale da modificare è il **Max Size** che definisce la dimensione massima (in millimetri) di ciascuna parte della mesh. Per ora, possiamo lasciare il valore predefinito di 1000:

:   <img alt="" src=images/Exercise_fem_04.jpg  style="width:600px;">

-   Dopo aver premuto **OK** e pochi secondi di calcolo, la mesh FEM è pronta:

:   <img alt="" src=images/Exercise_fem_05.jpg  style="width:600px;">

-   Ora possiamo definire il materiale da applicare alla mesh. Questo è importante perché secondo la resistenza del materiale,l\'oggetto reagisce in modo diverso alle forze ad esso applicate. Selezionare l\'oggetto Analisi e premere il pulsante **<img src="images/FEM_MaterialSolid.svg" width=16px> [Nuovo materiale](FEM_MaterialSolid/it.md)**.
-   Si apre un pannello delle attività che consente di scegliere un materiale. Nell\'elenco a discesa dei Materiali, scegliere **Concrete-generic**, e premere **OK**.

:   <img alt="" src=images/Exercise_fem_06.jpg  style="width:600px;">

-   Ora siamo pronti ad applicare le forze. Iniziamo specificando quali facce sono fissate nel terreno e, pertanto, non possono muoversi. Premere il pulsante **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Vincolo fissaggio](FEM_ConstraintFixed/it.md)**.
-   Cliccare sulla faccia inferiore dell\'edificio e premere **OK**. La faccia inferiore è indicata come inamovibile:

:   <img alt="" src=images/Exercise_fem_07.jpg  style="width:600px;">

-   Ora aggiungeremo un carico sulla faccia superiore, che potrebbe rappresentare, per esempio, un peso massiccio distribuito sul tetto. Per questo useremo un vincolo pressione. Premere il pulsante **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Vincolo pressione](FEM_ConstraintPressure/it.md)**.
-   Fare clic sulla faccia superiore del tetto, impostare la pressione di **10MPa** (la pressione viene applicata per millimetro quadrato) e fare clic sul pulsante **OK**. Ora la forza è applicata:

:   <img alt="" src=images/Exercise_fem_08.jpg  style="width:600px;">

-   Ora siamo pronti per iniziare il calcolo. Selezionare l\'oggetto **CalculiX** nella vista ad albero, e premere il pulsante **<img src="images/FEM_SolverControl.svg" width=16px> [Calcola](FEM_SolverControl/it.md)**.
-   Nel pannello delle attività che si apre, cliccare prima il pulsante **Write .inp file** per creare il file di input per CalculiX, poi il pulsante **Run CalculiX**. Pochi istanti dopo il calcolo viene eseguito:

:   <img alt="" src=images/Exercise_fem_09.jpg  style="width:600px;">

-   Ora possiamo guardare ai risultati. Chiudere il pannello delle attività, e vedere che all\'analisi è stato aggiunto un nuovo oggetto **Risultati** .
-   Fare doppio clic sull\'oggetto Risultati
-   Impostare il tipo di risultato che si desidera visualizzare sulla mesh, per esempio \"absolute displacement\", spuntare la casella di controllo **show** sotto **Displacement**, e spostare il cursore accanto ad essa. È possibile vedere che la deformazione aumenta man mano che si applica una forza maggiore:

:   <img alt="" src=images/Exercise_fem_10.jpg  style="width:600px;">

Naturalmente, i risultati visualizzati attualmente dall\'ambiente FEM non sono sufficienti per prendere delle decisioni reali sul dimensionamento delle strutture e sui materiali. Tuttavia, essi possono già dare preziose informazioni su come le forze fluiscono attraverso una struttura, e quali sono le aree deboli maggiormente sottoposte allo stress.

**Download**

-   Il file creato durante questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/fem.FCStd>

**Approfondimenti**

-   [L\'ambiente FEM](FEM_Workbench/it.md)
-   [Installazione dei componenti richiesti da FEM](FEM_Install/it.md)
-   [CalculiX](http://www.calculix.de)
-   [NetGen](https://sourceforge.net/projects/netgen-mesher)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Creating FEM analyses/it
