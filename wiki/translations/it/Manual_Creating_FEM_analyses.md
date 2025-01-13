# Manual:Creating FEM analyses/it
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FEM sta per [Finite Element Method](https://en.wikipedia.org/wiki/Finite_element_method) (metodo degli elementi finiti). Si tratta di un vasto argomento di matematica, ma in FreeCAD possiamo riassumerlo come un modo per calcolare le propagazioni all\'interno di un oggetto 3D, tagliandolo in piccoli pezzi, e analizzando l\'impatto di ogni piccolo pezzo rispetto a quelli vicini. Questo ha diversi utilizzi nei campi dell\'ingegneria e dell\'elettromagnetismo, ma qui vedremo in modo più approfondito il suo utilizzo già ben sviluppato in FreeCAD, per simulare le deformazioni negli oggetti che sono sottoposti a forze e pesi.


</div>


<div class="mw-translate-fuzzy">

In FreeCAD tale simulazione è fatta con l\'ambiente [FEM](FEM_Workbench/it.md). Si tratta di diverse fasi: preparare la geometria, impostare il suo materiale, eseguire la meshing, dividere in parti più piccole, come abbiamo fatto nel capitolo [Preparare gli oggetti per la stampa 3D](Manual:Preparing_models_for_3D_printing/it.md), ed infine calcolare la simulazione.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Exercise_fem_01.jpg  style="width:600px;">


</div>

This workbench allows for the integration of other FreeCAD workbenches, enabling seamless model preparation and analysis. It also provides powerful post-processing tools to visualize and interpret simulation results, such as stress, deformation, and thermal distributions. The workflow follows these steps:

-   **Preparing the Geometry**: The model must be simplified or optimized for FEM analysis. This often includes removing unnecessary details or features that don\'t contribute to the simulation but could make it computationally expensive. You can use tools from other workbenches, like <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench.md) or <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench.md), to prepare your 3D geometry.

-   **Assigning Material Properties** :Material definitions are critical for accurate simulations. Properties such as Young\'s modulus, Poisson's ratio, and density are assigned for structural simulations, or thermal conductivity and specific heat capacity for thermal analysis. Materials can be selected from FreeCAD's material library or customized as needed.

-   **Meshing**: Meshing divides the geometry into finite elements, allowing the solver to analyze the object. Mesh quality is crucial, as finer meshes result in more accurate simulations but require more computational power. Tools are available to refine the mesh locally, focusing on areas where stress or deformation is expected to be higher.

-   **Applying Loads and Constraints**: In this step, physical conditions such as forces, pressures, moments, or thermal loads are applied to the model. Boundary conditions are also defined, such as fixing points, applying symmetry constraints, or restricting movement, depending on the scenario being simulated.

-   **Running the Solver**: Once the setup is complete, the solver calculates the model\'s response to the applied conditions. Solvers like CalculiX compute displacements, stresses, and other quantities, depending on the type of analysis performed. The process can take varying amounts of time depending on the mesh density and model complexity.

-   **Post-Processing**: After the simulation, results are visualized using tools in the FEM Workbench. Stress, strain, and displacement fields are represented as color maps and deformation plots can be generated. These visualizations allow for a thorough analysis of the model\'s performance, highlighting areas of high stress or deformation.

<img alt="" src=images/FreeCAD_FEMBeam.png  style="width:600px;">



### Preparare FreeCAD 


<div class="mw-translate-fuzzy">

La simulazione vera e propria viene effettuata con un altro pezzo di software, che viene utilizzato da FreeCAD per ottenere i risultati. Dato che ci sono diverse interessanti applicazioni FEM open-source di simulazione disponibili, l\'ambiente [FEM](FEM_Workbench/it.md) è stato costruito in modo da poterne utilizzare più di una. Tuttavia, per ora è pienamente implementato solo [CalculiX](http://www.calculix.de/). È anche necessario un altro pezzo di software, chiamato [NetGen](https://sourceforge.net/projects/netgen-mesher/), che è responsabile della generazione della suddivisione in maglie. Le istruzioni dettagliate per l\'installazione di questi due componenti sono fornite nella [documentazione di FreeCAD](FEM_Install/it.md).


</div>



### Preparare la geometria 


<div class="mw-translate-fuzzy">

Utilizzeremo la casa modellata nel capitolo [Modellazione BIM](Manual:BIM_modeling/it.md). Tuttavia, devono essere fatte alcune modifiche per rendere il modello adatto ai calcoli FEM. Si tratta, in sostanza, di scartare gli oggetti che non vogliamo includere nel calcolo, come ad esempio la porta e la finestra, e di unire tutti gli oggetti rimanenti in uno solo.


</div>


<div class="mw-translate-fuzzy">

-   Caricare il [modello di casa](https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd) creato in precedenza
-   Eliminare o nascondere l\'oggetto pagina, i piani di sezione e le dimensioni, in modo che rimanga solo con il modello
-   Nascondere la finestra, la porta e la soletta del piano terra
-   Nascondere anche le travi di metallo del tetto. Dato che sono oggetti molto diversi dal resto della casa, non includendoli si semplifica il calcolo. Invece, considereremo il solaio di copertura come se fosse posto direttamente sulla parte superiore delle pareti.
-   Ora spostare la soletta del tetto verso il basso in modo che appoggi sulla parte superiore delle pareti: modificare l\'oggetto **Rettangolo** usato come base del solaio di copertura, e cambiare il suo valore **Placement-\>Position-\>X** da 3.18 m a 3.00 m
-   Ora il modello è ripulito:


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_02.jpg  style="width:600px;">


</div>



### Creare l\'analisi 


<div class="mw-translate-fuzzy">

-   Ora siamo pronti per iniziare una analisi FEM. Passare all\'ambiente [FEM](FEM_Workbench/it.md)
-   Selezionare l\'oggetto fuso
-   Premere il pulsante **<img src="images/FEM_Analysis.svg" width=16px> [Nuova analisi](FEM_Analysis/it.md)
**
-   Viene creata una nuova analisi e si apre un pannello per le impostazioni. Qui è possibile definire i parametri di meshing da utilizzare per produrre la mesh FEM. L\'impostazione principale da modificare è il **Max Size** che definisce la dimensione massima (in millimetri) di ciascuna parte della mesh. Per ora, possiamo lasciare il valore predefinito di 1000:


</div>


<div class="mw-translate-fuzzy">

-   Dopo aver premuto **OK** e pochi secondi di calcolo, la mesh FEM è pronta:


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_05.jpg  style="width:600px;">


</div>

-   Our mesh is ready.


<div class="mw-translate-fuzzy">

-   Ora possiamo definire il materiale da applicare alla mesh. Questo è importante perché secondo la resistenza del materiale,l\'oggetto reagisce in modo diverso alle forze ad esso applicate. Selezionare l\'oggetto Analisi e premere il pulsante **<img src="images/FEM_MaterialSolid.svg" width=16px> [Nuovo materiale](FEM_MaterialSolid/it.md)**.
-   Si apre un pannello delle attività che consente di scegliere un materiale. Nell\'elenco a discesa dei Materiali, scegliere **Concrete-generic**, e premere **OK**.


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_06.jpg  style="width:600px;">


</div>

<img alt="" src=images/FreeCAD_FEM_material.png  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Ora siamo pronti ad applicare le forze. Iniziamo specificando quali facce sono fissate nel terreno e, pertanto, non possono muoversi. Premere il pulsante **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Vincolo fissaggio](FEM_ConstraintFixed/it.md)**.
-   Cliccare sulla faccia inferiore dell\'edificio e premere **OK**. La faccia inferiore è indicata come inamovibile:


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_07.jpg  style="width:600px;">


</div>


<div class="mw-translate-fuzzy">

-   Ora aggiungeremo un carico sulla faccia superiore, che potrebbe rappresentare, per esempio, un peso massiccio distribuito sul tetto. Per questo useremo un vincolo pressione. Premere il pulsante **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Vincolo pressione](FEM_ConstraintPressure/it.md)**.
-   Fare clic sulla faccia superiore del tetto, impostare la pressione di **10MPa** (la pressione viene applicata per millimetro quadrato) e fare clic sul pulsante **OK**. Ora la forza è applicata:


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_08.jpg  style="width:600px;">


</div>


<div class="mw-translate-fuzzy">

-   Ora siamo pronti per iniziare il calcolo. Selezionare l\'oggetto **CalculiX** nella vista ad albero, e premere il pulsante **<img src="images/FEM_SolverControl.svg" width=16px> [Calcola](FEM_SolverControl/it.md)**.
-   Nel pannello delle attività che si apre, cliccare prima il pulsante **Write .inp file** per creare il file di input per CalculiX, poi il pulsante **Run CalculiX**. Pochi istanti dopo il calcolo viene eseguito:


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_09.jpg  style="width:600px;">


</div>


<div class="mw-translate-fuzzy">

-   Ora possiamo guardare ai risultati. Chiudere il pannello delle attività, e vedere che all\'analisi è stato aggiunto un nuovo oggetto **Risultati** .
-   Fare doppio clic sull\'oggetto Risultati
-   Impostare il tipo di risultato che si desidera visualizzare sulla mesh, per esempio \"absolute displacement\", spuntare la casella di controllo **show** sotto **Displacement**, e spostare il cursore accanto ad essa. È possibile vedere che la deformazione aumenta man mano che si applica una forza maggiore:


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_10.jpg  style="width:600px;">


</div>

Naturalmente, i risultati visualizzati attualmente dall\'ambiente FEM non sono sufficienti per prendere delle decisioni reali sul dimensionamento delle strutture e sui materiali. Tuttavia, essi possono già dare preziose informazioni su come le forze fluiscono attraverso una struttura, e quali sono le aree deboli maggiormente sottoposte allo stress.

**Approfondimenti**

-   [L\'ambiente FEM](FEM_Workbench/it.md)
-   [Installazione dei componenti richiesti da FEM](FEM_Install/it.md)
-   [CalculiX](http://www.calculix.de)
-   [NetGen](https://sourceforge.net/projects/netgen-mesher)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Creating FEM analyses/it
