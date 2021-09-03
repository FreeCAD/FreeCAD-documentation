 {{TOCright}}

## Creare una Mesh FE {#creare_una_mesh_fe}

L\'analisi agli elementi finiti (FEA) viene eseguita su una mesh composta da più elementi finiti triangolari e quadrilaterali che suddividono un corpo originale. Più la mesh è raffinata, più accurati saranno i risultati numerici, ma anche il tempo di calcolo sarà maggiore. Un equilibrio tra la dimensione della mesh, il tempo di calcolo e la precisione dei risultati è una caratteristica importante di un\'analisi degli elementi finiti ben definita.

Ci sono diverse possibilità di creare una mesh nell\'ambiente [FEM](FEM_Workbench/it.md):

-   Lo strumento [Gmsh](FEM_MeshGmshFromShape/it.md) dall\'interfaccia grafica utente.
-   Lo strumento [Netgen](FEM_MeshNetgenFromShape/it.md) dall\'interfaccia grafica utente.
-   Importare una mesh da un altro programma. In particolare, Gmsh e Netgen possono essere utilizzati da soli al di fuori di FreeCAD per creare mesh di corpi solidi come i file Step.
-   Creazione manuale della mesh tramite uno script [Python](Python/it.md).

Gli strumenti Gmsh e Netgen supportano i corpi mesh creati in [Part](Part_Workbench/it.md) e [PartDesign](PartDesign_Workbench/it.md), nonché le copie semplici di questi solidi. In generale, qualsiasi ambiente di lavoro che genera oggetti solidi, come [Arch](Arch_Workbench.md), può essere utilizzato come base da cui creare delle mesh. Notare che una mesh utilizzata per FEA è diversa da una mesh creata o importata dall\'ambiente [Mesh](Mesh_Workbench/it.md).

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">


*L'ambiente FEM chiama lo strumento esterno Gmsh per ottenere una mesh da un corpo solido creato con qualsiasi ambiente in FreeCAD; può anche importare una mesh creata esternamente*

<img alt="" src=images/FEM_Mesh.png  style="width:600px;">


*(1) Corpo solido creato con PartDesign; (2) mesh prodotta dallo strumento Gmsh all'interno di FEM (tutti triangoli); e (3) mesh prodotta esternamente da Gmsh, esportata nel formato Abaqus {{FileName|.inp*, e poi importata in FreeCAD (tutti quadrangoli)}}

Gli strumenti [Gmsh](FEM_MeshGmshFromShape/it.md) e [Netgen](FEM_MeshNetgenFromShape/it.md) sono strumenti utili per rendere rapidamente mesh un corpo, ma non espongono le funzionalità complete di questi programmi; essi normalmente creano mesh triangolari, che potrebbero non essere l\'ideale per alcuni tipi di analisi. Se si vuole avere più controllo sulla mesh creata (usare solo quadrilateri, numero e dimensione di elementi precisi, risoluzione variabile della mesh, ecc.), si dovrebbe usare questi programmi esternamente, produrre un file mesh in un formato supportato ( {{FileName|.inp}}, {{FileName|.unv}}, {{FileName|.vtk}}, {{FileName|.z88}}) e importare questo file in FreeCAD.

Precedentemente, Netgen era incluso in FreeCAD e poteva essere utilizzato immediatamente. Ora, sia Netgen che Gmsh devono essere installati prima di poter essere utilizzati da [FEM](FEM_Workbench/it.md). Per le istruzioni fare riferimento a [Installare FEM](FEM_Install/it.md).

## Software di mesh {#software_di_mesh}

Il software di mesh funziona su corpi solidi che possono essere in diversi formati, come Step e Brep. Questi programmi possono essere utilizzati indipendentemente da FreeCAD e in genere dispongono di molte opzioni per controllare gli algoritmi di meshing, la dimensione dell\'elemento e le condizioni del contorno.

[FEM](FEM_Workbench/it.md) ha sviluppato semplici interfacce di comunicazione per utilizzare Gmsh e Netgen direttamente in FreeCAD. Altri programmi non hanno un\'interfaccia, ma potrebbero cambiare in futuro se c\'è un interesse da parte della comunità e se tali applicazioni sono facili da integrare. Il software di meshing può essere compilato e distribuito insieme a FreeCAD solo se la sua licenza è compatibile con la licenza LGPL2; altrimenti, il programma deve essere usato come un binario esterno, come viene usato Gmsh (GPL2).

### Interfacce implementate in FreeCAD {#interfacce_implementate_in_freecad}

-   Gmsh: [main website](http://gmsh.info/), [code repository](https://gitlab.onelab.info/gmsh/gmsh)
-   Netgen: [main website](https://ngsolve.org/), [code repository](https://github.com/NGSolve/netgen)

### Nessuna interfaccia in FreeCAD {#nessuna_interfaccia_in_freecad}

-   ENigMA, [forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=33048), [code repository](https://github.com/bjaraujo/ENigMA)
-   libMesh, [main website](http://libmesh.github.io/), [code repository](https://github.com/libMesh/libmesh), [forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=33621); it\'s a very active project, and it\'s C++ only
-   PythonOCC, [main website](http://www.pythonocc.org/)
-   SnappyHexMesh, [main website](https://openfoamwiki.net/index.php/SnappyHexMesh)
-   Tetgen, [main website](http://wias-berlin.de/software/tetgen/)

## Elementi Mesh in FreeCAD {#elementi_mesh_in_freecad}

FreeCAD supporta vari tipi di elementi. Il seguente articolo spiega la loro differenza e quando devono essere utilizzati: [Meshing Your Geometry: When to Use the Various Element Types](https://www.comsol.com/blogs/meshing-your-geometry-various-element-types/).

<table><caption>Import and export of mesh elements</caption><thead><tr class="header"><th><p>Element</p></th><th><p>Element</p></th><th><p>FreeCAD API</p></th><th><p>FreeCAD GUI</p></th><th><p>med</p></th><th><p>unv</p></th><th><p>inp</p></th><th><p>frd</p></th><th><p>txt</p></th><th><p>xml</p></th></tr></thead><tbody><tr class="odd"><td><p>Med</p></td><td><p>CalculiX</p></td><td><p>Python</p></td><td><p>FEM Mesh</p></td><td><p>SMESH</p></td><td><p>IDEAS/FreeCAD</p></td><td><p>Abaqus/CalculiX</p></td><td><p>Result Mesh</p></td><td><p>Z88</p></td><td><p>Fenics</p></td></tr><tr class="even"><td><p>Name</p></td><td><p>Name</p></td><td><p>create elements</p></td><td><p>view elements</p></td><td><p>import/export</p></td><td><p>import/export</p></td><td><p>import/export</p></td><td><p>import</p></td><td><p>import/export</p></td><td><p>import/export</p></td></tr><tr class="odd"><td><p>seg 2</p></td><td><p>B31</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td></tr><tr class="even"><td><p>seg 3</p></td><td><p>B32</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><p>NI</p></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="odd"><td><p>tria 3</p></td><td><p>S3</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td></tr><tr class="even"><td><p>tria 6</p></td><td><p>S6</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="odd"><td><p>quad 4</p></td><td><p>S4</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td></tr><tr class="even"><td><p>quad 8</p></td><td><p>S8</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="odd"><td><p>tetra 4</p></td><td><p>C3D4</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td></tr><tr class="even"><td><p>tetra 10</p></td><td><p>C3D10</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="odd"><td><p>hexa 8</p></td><td><p>C3D8</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><p>(<img src="Edit_Cancel.svg" title="fig:Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />) the format allows it,<br />
but it's not readable or writable by fenics</p></td></tr><tr class="even"><td><p>hexa 20</p></td><td><p>C3D20</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="odd"><td><p>penta 6</p></td><td><p>C3D6</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><p>?</p></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="even"><td><p>penta 15</p></td><td><p>C3D15</p></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><p>?</p></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="odd"><td><p>pyra 5</p></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr><tr class="even"><td><p>pyra 13</p></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="" /><figcaption>Edit_OK.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td><td><figure><img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="" /><figcaption>Edit_Cancel.svg</figcaption></figure></td></tr></tbody></table>

: Import and export of mesh elements

-   \"NI\" significa che il tipo di elemento non è implementato in FreeCAD ma il formato lo supporterebbe.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:20px;"> \"-\" significa che le specifiche del formato non supportano questo tipo di elemento, quindi FreeCAD non può supportarlo.
-   \"?\" significa che non è noto se il formato supporta questo tipo di elemento.

## Tipi di elementi FEM {#tipi_di_elementi_fem}

Maggiori informazioni sui tipi di elementi FEM e la loro struttura dei dati all\'interno di FreeCAD si trovano nella pagina [Tipi di elementi FEM](FEM_Element_Types/it.md).

### Elemento Segmento {#elemento_segmento}

<img alt="" src=images/FEM_mesh_elements_1_segment.svg  style="width:600px;">

### Elemento Triangolo {#elemento_triangolo}

<img alt="" src=images/FEM_mesh_elements_2_triangle.svg  style="width:600px;">

### Elemento Quadrangolo {#elemento_quadrangolo}

<img alt="" src=images/FEM_mesh_elements_3_quadrangle.svg  style="width:600px;">

### Elemento Tetraedro {#elemento_tetraedro}

<img alt="" src=images/FEM_mesh_elements_4_tetrahedron.svg  style="width:600px;">

### Elemento Esaedro {#elemento_esaedro}

<img alt="" src=images/FEM_mesh_elements_5_hexahedron.svg  style="width:600px;">

### Elemento Pentaedro (prisma) {#elemento_pentaedro_prisma}

<img alt="" src=images/FEM_mesh_elements_6_pentahedron.svg  style="width:600px;">

### Elemento Piramide {#elemento_piramide}

<img alt="" src=images/FEM_mesh_elements_7_pyramid.svg  style="width:600px;">

## Script

### Creare una mesh FEM interamente con Python {#creare_una_mesh_fem_interamente_con_python}


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

L\'API Python consente all\'utente di definire una mesh di elementi finiti aggiungendo direttamente singoli nodi e definendo bordi, facce e volumi.

La mesh stessa è di tipo `Fem::FemMesh`, che deve essere collegata a un oggetto documento appropriato di tipo `Fem::FemMeshObject`.


```python
App.ActiveDocument.Mesh_object.TypeId = Fem::FemMeshObject
                              .
                              .
                              .FemMesh.TypeId = Fem::FemMesh
```

#### Creazione di una mesh con un elemento Tet-10 {#creazione_di_una_mesh_con_un_elemento_tet_10}

Creare un FemMesh vuoto, popolarlo con i nodi, creare il volume e infine chiamare `Fem.show()` per creare l\'oggetto documento con la mesh corrispondente.


```python
import FreeCAD, Fem

m = Fem.FemMesh()

m.addNode(0,    1,    0)
m.addNode(0,    0,    1)
m.addNode(1,    0,    0)
m.addNode(0,    0,    0)
m.addNode(0,    0.5,  0.5)
m.addNode(0.5,  0.03, 0.5)
m.addNode(0.5,  0.5,  0.03)
m.addNode(0,    0.5,  0)
m.addNode(0.03, 0,    0.5)
m.addNode(0.5,  0,    0)

m.addVolume([1,2,3,4,5,6,7,8,9,10])
Fem.show(m)
obj = FreeCAD.ActiveDocument.ActiveObject
```

Se si desidera avere la numerazione predefinita di nodi e elementi, passare l\'ID appropriato ai metodi di nodo e volume.

Per creare un oggetto documento attuale, invece di `Fem.show()` si può anche usare il metodo `addObject()`; quindi collegare la mesh creata all\'attributo `FemMesh` di questo oggetto. 
```python
a = Fem.FemMesh()

a.addNode(0,    1,    0,    1)
a.addNode(0,    0,    1,    2)
a.addNode(1,    0,    0,    3)
a.addNode(0,    0,    0,    4)
a.addNode(0,    0.5,  0.5,  5)
a.addNode(0.5,  0.03, 0.5,  6)
a.addNode(0.5,  0.5,  0.03, 7)
a.addNode(0,    0.5,  0,    8)
a.addNode(0.03, 0,    0.5,  9)
a.addNode(0.5,  0,    0,   10)

a.addVolume([1,2,3,4,5,6,7,8,9,10], 1)
obj_2 = FreeCAD.ActiveDocument.addObject("Fem::FemMeshObject")
obj_2.Placement.Base = FreeCAD.Vector(2, 0, 0)
obj_2.FemMesh = a
```

#### Proprietà visive {#proprietà_visive}

Una volta che un oggetto FemMesh è stato creato con `Fem.show()`, alcune delle sue proprietà visive possono essere modificate modificando i diversi attributi del suo `ViewObject`. Questo può essere utile per postelaborare la mesh dopo aver ottenuto una soluzione ad elementi finiti.

Evidenziare alcuni nodi nella mesh 
```python
Fem.show(m)
obj = FreeCAD.ActiveDocument.ActiveObject

obj.ViewObject.HighlightedNodes = [1, 2, 3]
``` I singoli elementi di una mesh possono essere modificati passando un dizionario con le coppie `key:value` appropriate.

Impostare il volume 1 su rosso 
```python
obj.ViewObject.ElementColor = {1:(1,0,0)}
``` Impostare i nodi 1, 2 e 3 su un determinato colore; le facce tra i nodi acquisiscono un colore interpolato 
```python
obj.ViewObject.NodeColor = {1:(1,0,0), 2:(0,1,0), 3:(0,0,1)}
``` Spostare i nodi 1 e 2 in base alla grandezza e alla direzione definite da un vettore 
```python
obj.ViewObject.NodeDisplacement = {1:FreeCAD.Vector(0,1,0), 2:FreeCAD.Vector(1,0,0)}
``` Raddoppiare il fattore dello spostamento mostrato (**Nota per i redattori: rimosso nelle versioni più recenti?**) 
```python
obj.ViewObject.animate(2.0)
```

## Esempi di script di ciascun tipo di elemento supportato {#esempi_di_script_di_ciascun_tipo_di_elemento_supportato}

### Beam, 2 node line, seg2 (linear) {#beam_2_node_line_seg2_linear}


```python
import Fem

seg2 = Fem.FemMesh()
seg2.addNode( 0, 0, 0, 1)
seg2.addNode(10, 0, 0, 2)
seg2.addEdge(1, 2)
print(seg2)

obj = FreeCAD.ActiveDocument.addObject("Fem::FemMeshObject", "seg2")
obj.FemMesh = seg2
obj.Placement.Base = FreeCAD.Vector(0, 110, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

### Beam, 3 node line, seg3 (quadratic) {#beam_3_node_line_seg3_quadratic}


```python
import Fem

seg3 = Fem.FemMesh()
seg3.addNode( 0, 0, 0, 1)
seg3.addNode(10, 0, 0, 2)
seg3.addNode( 5, 0, 0, 3)
seg3.addEdge([1, 2, 3])
print(seg3)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "seg3")
obj.FemMesh = seg3
obj.Placement.Base = FreeCAD.Vector(30, 110, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

### Shell, 3 node triangle, tria3 (linear) {#shell_3_node_triangle_tria3_linear}


```python
import Fem

tria3 = Fem.FemMesh()
tria3.addNode( 0,  0, 0, 1)
tria3.addNode( 6, 12, 0, 2)
tria3.addNode(12,  0, 0, 3)
tria3.addFace([1, 2, 3])
print(tria3)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tria3")
obj.FemMesh = tria3
obj.Placement.Base = FreeCAD.Vector(0, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Aggiungere una faccia con il numero di elementi. 
```python
elemtria3 = Fem.FemMesh()
nodes = tria3.Nodes
for n in nodes:
    elemtria3.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtria3.addFace([1, 2, 3], 88)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtria3")
obj.FemMesh = elemtria3
obj.Placement.Base = FreeCAD.Vector(200, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemtria3.Faces)
```

### Shell, 6 node triangle, tria6 (quadratic) {#shell_6_node_triangle_tria6_quadratic}


```python
import Fem

tria6 = Fem.FemMesh()
tria6.addNode( 0,  0, 0, 1)
tria6.addNode( 6, 12, 0, 2)
tria6.addNode(12,  0, 0, 3)
tria6.addNode( 3,  6, 0, 4)
tria6.addNode( 9,  6, 0, 5)
tria6.addNode( 6,  0, 0, 6)
tria6.addFace([1, 2, 3, 4, 5, 6])
print(tria6)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tria6")
obj.FemMesh = tria6
obj.Placement.Base = FreeCAD.Vector(30, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Aggiungere una faccia con il numero di elementi. 
```python
elemtria6 = Fem.FemMesh()
nodes = tria6.Nodes
for n in nodes:
    elemtria6.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtria6.addFace([1, 2, 3, 4, 5, 6], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtria6")
obj.FemMesh = elemtria6
obj.Placement.Base = FreeCAD.Vector(230, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemtria6.Faces)
```

### Shell, 4 node quadrangle, quad4 (linear) {#shell_4_node_quadrangle_quad4_linear}


```python
import Fem

quad4 = Fem.FemMesh()
quad4.addNode( 0, 10, 0, 1)
quad4.addNode(10, 10, 0, 2)
quad4.addNode(10,  0, 0, 3)
quad4.addNode( 0,  0, 0, 4)
quad4.addFace([1, 2, 3, 4])
print(quad4)

obj = FreeCAD.ActiveDocument.addObject("Fem::FemMeshObject", "quad4")
obj.FemMesh = quad4
obj.Placement.Base = FreeCAD.Vector(60, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Aggiungere una faccia con il numero di elementi. 
```python
elemquad4 = Fem.FemMesh()
nodes = quad4.Nodes
for n in nodes:
    elemquad4.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemquad4.addFace([1, 2, 3, 4], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemquad4")
obj.FemMesh = elemquad4
obj.Placement.Base = FreeCAD.Vector(260, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemquad4.Faces)
```

### Shell, 8 node quadrangle, quad8 (quadratic) {#shell_8_node_quadrangle_quad8_quadratic}


```python
import Fem

quad8 = Fem.FemMesh()
quad8.addNode( 0, 10, 0, 1)
quad8.addNode(10, 10, 0, 2)
quad8.addNode(10,  0, 0, 3)
quad8.addNode( 0,  0, 0, 4)
quad8.addNode( 5, 10, 0, 5)
quad8.addNode(10,  5, 0, 6)
quad8.addNode( 5,  0, 0, 7)
quad8.addNode( 0,  5, 0, 8)
quad8.addFace([1, 2, 3, 4, 5, 6, 7, 8])
print(quad8)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "quad8")
obj.FemMesh = quad8
obj.Placement.Base = FreeCAD.Vector(90, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Aggiungere una faccia con il numero di elementi. 
```python
elemquad8 = Fem.FemMesh()
nodes = quad8.Nodes
for n in nodes:
    elemquad8.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemquad8.addFace([1, 2, 3, 4, 5, 6, 7, 8], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemquad8")
obj.FemMesh = elemquad8
obj.Placement.Base = FreeCAD.Vector(290, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemquad8.Faces)
```

### Volume, 4 node tetrahedron, tetra4 (linear) {#volume_4_node_tetrahedron_tetra4_linear}


```python
import Fem

tetra4 = Fem.FemMesh()
tetra4.addNode( 6, 12, 18, 1)
tetra4.addNode( 0,  0, 18, 2)
tetra4.addNode(12,  0, 18, 3)
tetra4.addNode( 6,  6,  0, 4)
tetra4.addVolume([1, 2, 3, 4])
print(tetra4)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tetra4")
obj.FemMesh = tetra4
obj.Placement.Base = FreeCAD.Vector(0, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elemtetra4 = Fem.FemMesh()
nodes = tetra4.Nodes
for n in nodes:
    elemtetra4.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtetra4.addVolume([1, 2, 3, 4], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtetra4")
obj.FemMesh = elemtetra4
obj.Placement.Base = FreeCAD.Vector(200, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemtetra4.Volumes)
```

### Volume, 10 node tetrahedron, tetra10 (quadratic) {#volume_10_node_tetrahedron_tetra10_quadratic}


```python
import Fem

tetra10 = Fem.FemMesh()
tetra10.addNode( 6, 12, 18, 1)
tetra10.addNode( 0,  0, 18, 2)
tetra10.addNode(12,  0, 18, 3)
tetra10.addNode( 6,  6,  0, 4)

tetra10.addNode( 3,  6, 18, 5)
tetra10.addNode( 6,  0, 18, 6)
tetra10.addNode( 9,  6, 18, 7)

tetra10.addNode( 6,  9,  9, 8)
tetra10.addNode( 3,  3,  9, 9)
tetra10.addNode( 9,  3,  9,10)
tetra10.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(tetra10)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tetra10")
obj.FemMesh = tetra10
obj.Placement.Base = FreeCAD.Vector(30, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elemtetra10 = Fem.FemMesh()
nodes = tetra10.Nodes
for n in nodes:
    elemtetra10.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtetra10.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtetra10")
obj.FemMesh = elemtetra10
obj.Placement.Base = FreeCAD.Vector(230, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemtetra10.Volumes)
```

### Volume, 8 node hexahedron, hexa8 (linear) {#volume_8_node_hexahedron_hexa8_linear}


```python
import Fem

hexa8 = Fem.FemMesh()
hexa8.addNode( 0, 10, 10, 1)
hexa8.addNode( 0,  0, 10, 2)
hexa8.addNode(10,  0, 10, 3)
hexa8.addNode(10, 10, 10, 4)
hexa8.addNode( 0, 10,  0, 5)
hexa8.addNode( 0,  0,  0, 6)
hexa8.addNode(10,  0,  0, 7)
hexa8.addNode(10, 10,  0, 8)
hexa8.addVolume([1, 2, 3, 4, 5, 6, 7, 8])
print(hexa8)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "hexa8")
obj.FemMesh = hexa8
obj.Placement.Base = FreeCAD.Vector(60, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elemhexa8 = Fem.FemMesh()
nodes = hexa8.Nodes
for n in nodes:
    elemhexa8.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemhexa8.addVolume([1,  2,  3, 4, 5, 6, 7, 8], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemhexa8")
obj.FemMesh = elemhexa8
obj.Placement.Base = FreeCAD.Vector(260, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemhexa8.Volumes)
```

### Volume, 20 node hexahedron, hexa20 (quadratic) {#volume_20_node_hexahedron_hexa20_quadratic}


```python
import Fem

hexa20 = Fem.FemMesh()
hexa20.addNode( 0, 10, 10,  1)
hexa20.addNode( 0,  0, 10,  2)
hexa20.addNode(10,  0, 10,  3)
hexa20.addNode(10, 10, 10,  4)
hexa20.addNode( 0, 10,  0,  5)
hexa20.addNode( 0,  0,  0,  6)
hexa20.addNode(10,  0,  0,  7)
hexa20.addNode(10, 10,  0,  8)

hexa20.addNode( 0,  5, 10,  9)
hexa20.addNode( 5,  0, 10, 10)
hexa20.addNode(10,  5, 10, 11)
hexa20.addNode( 5, 10, 10, 12)

hexa20.addNode( 0,  5,  0, 13)
hexa20.addNode( 5,  0,  0, 14)
hexa20.addNode(10,  5,  0, 15)
hexa20.addNode( 5, 10,  0, 16)

hexa20.addNode( 0, 10,  5, 17)
hexa20.addNode( 0,  0,  5, 18)
hexa20.addNode(10,  0,  5, 19)
hexa20.addNode(10, 10,  5, 20)
hexa20.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(hexa20)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "hexa20")
obj.FemMesh = hexa20
obj.Placement.Base = FreeCAD.Vector(90, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elemhexa20 = Fem.FemMesh()
nodes = hexa20.Nodes
for n in nodes:
    elemhexa20.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemhexa20.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemhexa20")
obj.FemMesh = elemhexa20
obj.Placement.Base = FreeCAD.Vector(290, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemhexa20.Volumes)
```

### Volume, 6 node pentahedron, penta6 (linear) {#volume_6_node_pentahedron_penta6_linear}


```python
import Fem

penta6 = Fem.FemMesh()
penta6.addNode(10, 10, 10, 1)
penta6.addNode( 0,  0, 10, 2)
penta6.addNode(20,  0, 10, 3)
penta6.addNode(10, 10,  0, 4)
penta6.addNode( 0,  0,  0, 5)
penta6.addNode(20,  0,  0, 6)
penta6.addVolume([1, 2, 3, 4, 5, 6])
print(penta6)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "penta6")
obj.FemMesh = penta6
obj.Placement.Base = FreeCAD.Vector(0, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elempenta6 = Fem.FemMesh()
nodes = penta6.Nodes
for n in nodes:
    elempenta6.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempenta6.addVolume([ 1, 2, 3, 4, 5, 6], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempenta6")
obj.FemMesh = elempenta6
obj.Placement.Base = FreeCAD.Vector(200, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempenta6.Volumes)
```

### Volume, 15 node pentahedron, penta15 (quadratic) {#volume_15_node_pentahedron_penta15_quadratic}


```python
import Fem

penta15 = Fem.FemMesh()
penta15.addNode(10, 10, 10,  1)
penta15.addNode( 0,  0, 10,  2)
penta15.addNode(20,  0, 10,  3)
penta15.addNode(10, 10,  0,  4)
penta15.addNode( 0,  0,  0,  5)
penta15.addNode(20,  0,  0,  6)

penta15.addNode( 5,  5, 10,  7)
penta15.addNode(10,  0, 10,  8)
penta15.addNode(15,  5, 10,  9)

penta15.addNode( 5,  5,  0, 10)
penta15.addNode(10,  0,  0, 11)
penta15.addNode(15,  5,  0, 12)

penta15.addNode(10, 10,  5, 13)
penta15.addNode( 0,  0,  5, 14)
penta15.addNode(20,  0,  5, 15)
penta15.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(penta15)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "penta15")
obj.FemMesh = penta15
obj.Placement.Base = FreeCAD.Vector(40, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elempenta15 = Fem.FemMesh()
nodes = penta15.Nodes
for n in nodes:
    elempenta15.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempenta15.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempenta15")
obj.FemMesh = elempenta15
obj.Placement.Base = FreeCAD.Vector(240, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempenta15.Volumes)
```

### Volume, 5 node pyramid, pyra5 (linear) {#volume_5_node_pyramid_pyra5_linear}


```python
import Fem

pyra5 = Fem.FemMesh()
pyra5.addNode( 0, 20,  0, 1)
pyra5.addNode(20, 20,  0, 2)
pyra5.addNode(20,  0,  0, 3)
pyra5.addNode( 0,  0,  0, 4)
pyra5.addNode(10, 10, 10, 5)
pyra5.addVolume([1, 2, 3, 4, 5])
print(pyra5)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "pyra5")
obj.FemMesh = pyra5
obj.Placement.Base = FreeCAD.Vector(80, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elempyra5 = Fem.FemMesh()
nodes = pyra5.Nodes
for n in nodes:
    elempyra5.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempyra5.addVolume([1, 2, 3, 4, 5], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempyra5")
obj.FemMesh = elempyra5
obj.Placement.Base = FreeCAD.Vector(280, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempyra5.Volumes)
```

### Volume, 13 node pyramid, pyra13 (quadratic) {#volume_13_node_pyramid_pyra13_quadratic}


```python
import Fem

pyra13 = Fem.FemMesh()
pyra13.addNode( 0, 20,  0,  1)
pyra13.addNode(20, 20,  0,  2)
pyra13.addNode(20,  0,  0,  3)
pyra13.addNode( 0,  0,  0,  4)
pyra13.addNode(10, 10, 10,  5)

pyra13.addNode(10, 20,  0,  6)
pyra13.addNode(20, 10,  0,  7)
pyra13.addNode(10,  0,  0,  8)
pyra13.addNode( 0, 10,  0,  9)

pyra13.addNode( 5, 15,  5, 10)
pyra13.addNode(15, 15,  5, 11)
pyra13.addNode(15,  5,  5, 12)
pyra13.addNode( 5,  5,  5, 13)
pyra13.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(pyra13)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "pyra13")
obj.FemMesh = pyra13
obj.Placement.Base = FreeCAD.Vector(120, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Aggiungere una faccia con il numero di elementi. 
```python
elempyra13 = Fem.FemMesh()
nodes = pyra13.Nodes
for n in nodes:
    elempyra13.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempyra13.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempyra13")
obj.FemMesh = elempyra13
obj.Placement.Base = FreeCAD.Vector(320, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempyra13.Volumes)
```

## Esempi di scripting per gruppi {#esempi_di_scripting_per_gruppi}

Vedere per esempio <https://forum.freecadweb.org/viewtopic.php?f=18&t=37304&start=20#p318823>


{{FEM Tools navi

}}  
