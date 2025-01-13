---
 TutorialInfo:t
   Topic: FEM
   Level: Intermediate
   Time: 1 hour
   Author: User:M42kus
   FCVersion: 0.17
---

# Extend FEM Module/it





L\'ambiente FEM supporta già molti vincoli diversi e diversi solutori. Nonostante ciò, gli utenti spesso necessitano di vincoli non ancora supportati da FreeCAD. Questa pagina è il punto di partenza per una serie di tutorial e altre risorse che descrivono come estendere l\'ambiente FEM utilizzando il framework esistente. Sebbene questa serie possa rivelarsi utile anche per gli sviluppatori di software, l\'idea è quella di consentire agli utenti FEM con un po\' di interesse per la codifica Python di aggiungere autonomamente le parti di cui hanno bisogno.

Aggiungere nuovi vincoli, equazioni o solutori è per lo più un lavoro di routine. Ma farlo per la prima volta non è così facile come potrebbe sembrare. È utile conoscere i seguenti argomenti:

-   Script Python in FreeCAD.
    -   [Tutorial sugli script di FreeCAD](Python_scripting_tutorial/it.md)
    -   [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md)
-   Estensione di FreeCAD con Python.
    -   [Script di oggetti](Scripted_objects/it.md)
-   Una solida conoscenza del risolutore per il quale devono essere aggiunti nuovi oggetti (ad es. CalculiX o Elmer) è importante.
-   Una conoscenza di base dei sistemi di compilazione, in particolare cmake (sistema di compilazione utilizzato da FreeCAD).



## Sistema di costruzione (cmake) 

Il sistema di build deve essere modificato indipendentemente da quali oggetti verranno aggiunti all\'ambiente FEM. Ogni modulo (file) Python deve essere registrato. Il workbench FEM richiede che ogni nuovo modulo Python sia registrato in `Mod/Fem/CMakeLists.txt`. Questo è necessario indipendentemente dal tipo di modulo Python (GUI o non GUI). Il punto esatto in cui deve essere inserito il modulo dipende dal ruolo del modulo. Risolutore, equazioni e vincoli utilizzano tutti elenchi diversi. La ricerca di file simili e l\'inserimento del nuovo file nello stesso elenco funziona nella maggior parte dei casi.


<div class="mw-translate-fuzzy">

Ad esempio, proviamo ad aggiungere un nuovo vincolo di pressione. Un nuovo vincolo richiede almeno i seguenti nuovi moduli: FemConstraint.py, ViewProviderFemConstraint.py, CommandFemConstraint.py. Questi tre file devono essere aggiunti a CMakeLists.txt ed anche a App/CMakeLists.txt.


</div>


**Mod/Fem/CMakeLists.txt**


{{code|code=
SET(FemObjects_SRCS
    femobjects/__init__.py
    femobjects/base_fempythonobject.py
    femobjects/constraint_bodyheatsource.py
    femobjects/constraint_electrostaticpotential.py
    femobjects/constraint_flowvelocity.py
    femobjects/constraint_initialflowvelocity.py
+   femobjects/constraint_initialflowpressure.py
    femobjects/constraint_selfweight.py
...
    femobjects/solver_ccxtools.py
)
...
SET(FemGuiViewProvider_SRCS
    femviewprovider/__init__.py
    femviewprovider/view_base_femconstraint.py
    femviewprovider/view_base_femobject.py
    femviewprovider/view_constraint_bodyheatsource.py
    femviewprovider/view_constraint_electrostaticpotential.py
    femviewprovider/view_constraint_flowvelocity.py
+   femviewprovider/view_constraint_flowpressure.py
    femviewprovider/view_constraint_initialflowvelocity.py
    femviewprovider/view_constraint_selfweight.py
...
    femviewprovider/view_solver_ccxtools.py
)
}}



## Organizzazione del codice sorgente 


<div class="mw-translate-fuzzy">

Per organizzare il codice Python il modulo FEM usa un approccio simile a quello usato per il codice C++ in FreeCAD. Il modulo è diviso in due pacchetti. PyObjects, che contiene tutti i proxy Python non-gui come gli oggetti del documento e PyGui che contiene tutto ciò che è collegato come proxy python per il provider di visualizzazione, i pannelli delle attività, i file ui e i comandi.


</div>


<div class="mw-translate-fuzzy">

Un pacchetto non segue questo modello: FemSolver. È posizionato allo stesso livello di PyObjects e PyGui (src/Mod/Fem/FemSolver). Il pacchetto contiene il solutore con i pacchetti relativi all\'equazione ed ai moduli ed è organizzato nel seguente modo:


</div>

    .femsolver
    .femsolver.elmer
    .femsolver.elmer.equations
    .femsolver.calculix
    .femsolver.calculix.equations
    .femsolver.z88
    .femsolver.z88.equations



## Solutore

In FreeCAD a solver can be split into two parts:

-   One is the document object used by the user to interact with the solver. Through it, solver parameters can be set and it is also used to control the solving process.
-   The other one are the so called tasks of a solver. The solving process is split into those tasks, namely: *check, prepare, solve and results*. Those do the actual work of exporting the analysis into a format understood by the solver executable, starting the executable and loading the results back into FreeCAD.


<div class="mw-translate-fuzzy">

La maggior parte dei file relativi a un solver si trovano in un sottopacchetto del pacchetto FemSolver (e.g. FemSolver.Elmer). La seguente lista elenca tutti i file relativi all\'implementazione di un risolutore. Questi sono i file che devono essere copiati e modificati per aggiungere il supporto per un nuovo risolutore in FreeCAD.


</div>

-   **femsolver/elmer/solver.py:** Document object visible in the tree-view. Implemented in python via a document proxy and view proxy.
-   **femsolver/elmer/tasks.py:** Module containing one task class per task required for a solver implementation. Those tasks divide the process of solving a analysis into the following steps: check, prepare, solve, results.
-   **femcommands/commands.py:** Adds the solver document object to the active document. Required to access the solver object from the GUI.



## Equazioni

Un\'equazione rappresenta una particolare fisica che deve essere considerata quando si risolve l\'analisi (ad esempio flusso, calore). Non tutti i solutori in FreeCAD supportano tutte le equazioni. Le equazioni sono rappresentate dagli oggetti figlio del corrispondente oggetto del risolutore. Nella vista ad albero questo assomiglia così:

-   elmer-solver
    -   elasticity
    -   heat
    -   flow
    -   electrostatics

Most solver specific options (e.g. max. iterations, method of solving, etc) are set via the equation objects. One consequence of this is that each solver must have it\'s own implementation of \"the same\" equation. CalculiX would have a different Heat-object that Elmer. To avoid having multiple buttons for the same physics in the GUI each solver object adds it\'s equations itself.

The actual implementation can be split into the generic and the solver specific part. The generic part can be found in the `femsolver.equationbase` module. The solver specific part resides inside individual Equations sub-packages of the solver packages (e.g. `femsolver/elmer/equations`).

Adding a new equations to Elmer should be very easy. For newcomers there exists a tutorial which shows how to add a new equation to Elmer by adding the existing elasticity solver to FreeCAD: [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md).



## Vincoli

Constraints define boundary conditions for the problem that shall be solved. In FreeCAD constraints aren\'t specific to a particular solver. A problem setup can be solved by all solver that support all conditions in the analysis.

Adding new constraints is quite straight forward. For newcomers there is a tutorial: [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md).



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Extend FEM Module/it
