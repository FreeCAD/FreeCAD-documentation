# FEM CalculiX/it
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

Questa pagina raccoglie le informazioni sul risolutore di elementi finiti [CalculiX](http   *//www.calculix.de/), il risolutore predefinito per l\'analisi strutturale e termo-meccanica nell\'ambiente **<img src="images/Workbench_FEM.svg" width=24px> [FEM](FEM_Workbench/it.md)** a partire da FreeCAD 0.17. A seconda del sistema operativo su cui si sta lavorando, è necessario installare CalculiX prima di eseguire la prima simulazione. Si prega di consultare [Installare FEM](FEM_Install/it.md).


</div>

Il risolutore è in grado di eseguire calcoli lineari e non lineari, per problemi statici, dinamici e termici. Il risolutore funziona su un file di input Abaqus (`.inp`), il che significa che può essere utilizzato con diversi pre-processori che supportano questo formato. Il programma include un proprio preprocessore grafico che, tuttavia, non viene utilizzato da FreeCAD, ma solo dal risolutore.

CalculiX è progettato per funzionare su piattaforme Unix come Linux e Irix ma anche su MS-Windows. CalculiX è stato sviluppato dagli ingegneri di MTU Aero Engines, Monaco di Baviera, Germania, per assisterli nella progettazione di macchinari come le turbine a getto. Il software è attualmente rilasciato al pubblico secondo i termini della GPL versione 2.

## Integration with FreeCAD 


<div class="mw-translate-fuzzy">

## Integrazione con FreeCAD 

L\'interazione tra l\'ambiente [FEM](FEM_Workbench/it.md) e CalculiX avviene attraverso la scrittura e la lettura di file di testo. La sequenza delle operazioni è la seguente   *


</div>

1.  Viene creato un file di input CalculiX con i dettagli necessari per eseguire la simulazione.
2.  Viene avviato il risolutore CalculiX con questo file di input.
3.  Viene registrato l\'output del solutore.
4.  Vengono letti i file di output del risolutore, se disponibili.


<div class="mw-translate-fuzzy">

Lo strumento [FEM Control Solver](FEM_SolverControl/it.md) gestisce l'intero processo. L'interazione dell'utente nel processo è possibile.


</div>

## Preprocessing interface 


<div class="mw-translate-fuzzy">

## Interfaccia di Pre-processo 

Il file di input che CalculiX utilizza può essere preparato e modificato prima dell\'avvio del solver. Le unità utilizzate nel file di input sono indipendenti dalle unità impostate in FreeCAD; sono sempre millimetri (mm) e Newton (N).


</div>


**(Da fare   * controllare questo. Cosa succede con la mesh se in FreeCAD si usa inch? Siccome è stata introdotta la densità, con questo abbiamo kg e s, e non più N?! Cosa ne pensate di questo?!)**

L\'interfaccia di CalculiX supporta i seguenti oggetti   *

### FEM Elements 


<div class="mw-translate-fuzzy">

### Elementi FEM 

-   Tet4 and Tet10
-   S3 and S6
-   B31 and B32
-   e quelli descritti in [FEM Mesh CalculiX](FEM_Mesh_CalculiX/it.md)


</div>

### Analysis


<div class="mw-translate-fuzzy">

### Analisi

-   Analisi statica lineare
-   Analisi delle frequenze
-   Analisi termo-strutturale accoppiata


</div>

### Materials


<div class="mw-translate-fuzzy">

### Materiali

-   Materiale isotropo elastico lineare (uniforme in tutte le direzioni)
-   Materiale multiplo è in fase di sviluppo


</div>

## Postprocessing interface 


<div class="mw-translate-fuzzy">

## Interfaccia di post-processo 

L\'ambiente FEM può leggere lo stress risultante (Von Mises) e tutti gli spostamenti.


</div>

Reaction forces can be found in ccx_dat_file which contains reaction force components (fx, fy, fz) for each Constraint fixed and for each Constraint displacement which constrains translation degrees of freedom.

## Related

-   [FEM Mesh CalculiX](FEM_Mesh_CalculiX.md)
-   [CalculiX preferences](FEM_Preferences#CalculiX.md) dialog menu in the FEM Workbench preferences menu


{{FEM Tools navi

}}

[Category   *Poweruser_Documentation](Category_Poweruser_Documentation.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [FEM](Category_FEM.md) > FEM CalculiX/it
