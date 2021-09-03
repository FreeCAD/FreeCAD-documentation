


<div class="mw-translate-fuzzy">





</div>


{{TOCright}}


<div class="mw-translate-fuzzy">

## Scegliere il proprio sistema operativo 


</div>


<div class="mw-translate-fuzzy">

FreeCAD è realmente una applicazione multi-piattaforma, sviluppata sul noto ambiente [Qt](http://en.wikipedia.org/wiki/Qt_(framework)). Ciò significa che FreeCAD ha lo stesso aspetto e si comporta allo stesso modo sia su Windows che su Linux o su Mac. Tuttavia, secondo il sistema operativo, la procedura di installazione è diversa. Scegliere sotto il proprio sistema operativo per avere maggiori dettagli su come installare FreeCAD.

  ---------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------
   ![ alt=\'Windows\' \| link= Install on Windows/it](images/Windows.png )   ![ alt=\'Linux\' \| link= Install on Linux/it](images/Linux.png )   ![ alt=\'Mac\' \| link= Install on Mac/it](images/Mac.png )
                            [Installazione in Windows](Install_on_Windows/it.md)                                                  [Installazione in Linux](Install_on_Linux/it.md)                                            [Installazione in Mac](Install_on_Mac/it.md)
  ---------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------


</div>

# Help files 

The offline documentation is not shipped with all installers, but it is available as a separate package. See the [Installing Helpfile](Installing_Helpfile.md) page for more information.

# External workbenches 


<div class="mw-translate-fuzzy">

Oltre ai pacchetti degli [ambienti di lavoro](workbenches/it.md) forniti di default con FreeCAD, vi è una crescente collezione di utili ambienti e moduli aggiuntivi realizzati dai membri della comunità sul web. Numerosi sforzi sono in corso per raccoglierli e renderli disponibili in un modo comodo. Essi sono elencati in seguito.


</div>


<div class="mw-translate-fuzzy">

## Software esterno supportato da FreeCAD 


</div>


<div class="mw-translate-fuzzy">

FreeCAD supporta molti pacchetti software esterni pronti all\'uso. Ciò significa che basta installare il software e, al prossimo avvio, esso è automaticamente disponibile. Non è necessario ricompilarlo. Questa sezione ha lo scopo di fornire un elenco di tutti questi pacchetti software, insieme ad alcune informazioni su dove sono utilizzati in FreeCAD e dove è possibile prelevarli.


</div>


<div class="mw-translate-fuzzy">

### Supporti


</div>


<div class="mw-translate-fuzzy">

#### GitPython


</div>


<div class="mw-translate-fuzzy">

È una libreria python che viene utilizzata per interagire con i repository Git. [Addon Manager](Addon_Manager/it.md) può usare questa libreria per importare gli addon da un repository Git. Il progetto è ospitato su GitHub all\'indirizzo <https://github.com/gitpython-developers/GitPython>.


</div>


<div class="mw-translate-fuzzy">

#### GraphViz


</div>


<div class="mw-translate-fuzzy">

GraphViz è un software di visualizzazione di grafici open source. In FreeCAD è usato per generare i grafici delle dipendenza attraverso **Strumenti → Grafico delle dipendenze ...**. La sua homepage è su <https://www.graphviz.org>


</div>


<div class="mw-translate-fuzzy">

#### OpenCAMLib


</div>


<div class="mw-translate-fuzzy">

[OpenCAMLib](OpenCamLib/it.md) è una libreria open source che mira a fornire algoritmi di produzione assistita da computer (CAM). È utilizzato in FreeCAD nell\'ambiente [Path](Path_Workbench/it.md). Vedere [la sua pagina](OpenCamLib/it.md) per le istruzioni di installazione.


</div>


<div class="mw-translate-fuzzy">

#### OpenSCAD


</div>


<div class="mw-translate-fuzzy">

OpenSCAD è un modellatore 3D solido basato sul paradigma della [geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG), in cui il modello viene creato tramite uno script. Ciò significa che non può gestire le mesh, ma opera esclusivamente sulla geometria solida. FreeCAD può importare ed esportare i file creati da OpenSCAD tramite gli strumenti [Std Importa](Std_Import/it.md) e [Esporta](Std_Export/it.md) selezionando il formato **OpenSCAD CSG** o il tipo di file **OpenSCAD**. È possibile ottenere OpenSCAD da <https://www.openscad.org>.


</div>

## File formats 

All software in this section will be used by the [Std Import](Std_Import.md) or [Std Export](Std_Export.md) tools.


<div class="mw-translate-fuzzy">

### CAD Exchanger 

Un\'applicazione proprietaria e closed source per lo scambio di vari formati di file utilizzati in CAD. Si può usare per convertire i formati proprietari e chiusi in un formato accessibile da FreeCAD. La homepage è <https://cadexchanger.com/> dove è possibile scaricare una versione di valutazione o acquistare una licenza per l\'applicazione.


</div>

[CADExchanger](https://cadexchanger.com) is a commercial application for exchanging various CAD file formats. There is an [external workbench](https://github.com/yorikvanhavre/CADExchanger) to use this application in FreeCAD.


<div class="mw-translate-fuzzy">

### DXF Importer 

Per file DXF, FreeCAD ha un importatore ed esportatore nativo, programmato in C ++. Attualmente questo importatore non implementa tutte le funzionalità del formato DXF. Si può abilitare un importatore / esportatore più vecchio basato su Python tramite **Modifica → Preferenze → Import-Export** attivando l\'opzione **Usa il vecchio importatore python**. È quindi possibile scegliere di consentire a FreeCAD di scaricare automaticamente i file necessari o di recuperarli da <https://github.com/yorikvanhavre/Draft-dxf-importer>. L\'importatore / esportatore scelto viene utilizzato selezionando **File → Importa** o **File → Esporta** e scegliendo il formato file **AutoDesk DXF 2D**.


</div>

FreeCAD has a native importer and exporter for DXF files, programmed in C++. Currently they do not implement all features of the DXF format. For those features the legacy Python importer and exporter are still available. These require the [Draft-dxf-importer](https://github.com/yorikvanhavre/Draft-dxf-importer) Python library. See the [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md) page for more information.


<div class="mw-translate-fuzzy">

### ifcOpenShell

IfcOpenShell è una libreria per lavorare con il formato di file IFC (Industry Foundation Classes) utilizzato nella progettazione architettonica. Vi si può accedere dall\'ambiente [Arch](Arch_Workbench/it.md) tramite **Arch → Utilità → Ifc Explorer**. La sua homepage è su <http://ifcopenshell.org>


</div>

[IfcOpenShell](http://ifcopenshell.org) is a library for working with the Industry Foundation Classes (IFC) file format used in architectural design. The library is also used by the [Arch IfcExplorer](Arch_IfcExplorer.md) ({{VersionMinus|0.18}}) and [BIM IfcExplorer](BIM_IfcExplorer.md) tools. IfcOpenShell is included in the FreeCAD installers for Windows and Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) is a library required for exporting to the IFCJSON file format. IFCJSON is a new IFC format that is not yet supported by many applications.

### LibreDWG

Support for [LibreDWG](https://www.gnu.org/software/libredwg) is still experimental. Like the ODA File Converter it can convert DWG to DXF files which FreeCAD can then import. See the [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) page for more information.


<div class="mw-translate-fuzzy">

### ODA File Converter 

Il convertitore di file ODA è un\'applicazione proprietaria, closed source, binaria e liberamente disponibile per importare ed esportare i file DWG e DXF. In FreeCAD può essere utilizzato dai menu **File → Importa** e **File → Esporta**, quando si seleziona il tipo di file **AutoDesk DWG 2D**. Può essere scaricato da <https://www.opendesign.com/guestfiles/oda_file_converter>.


</div>

The [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) is a free application to convert between several versions of DWG and DXF files. FreeCAD requires this converter, or LibreDWG, to import DWG files. See the [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) page for more information.


<div class="mw-translate-fuzzy">

### pycollada

Pycollada, noto anche come `python-collada`, è una libreria Python per leggere e scrivere documenti COLLADA, uno standard per lo scambio di scene ed elementi 3D. Se è installato, si può importare ed esportare scene da e verso i file COLLADA attraverso i comandi **File → Importa** e **File → Esporta** selezionando il tipo di file COLLADA. Il progetto è ospitato su GitHub all\'indirizzo <https://pycollada.github.io/> e si possono scaricare le versioni da <https://github.com/pycollada/pycollada/releases/>


</div>

[Pycollada](https://github.com/pycollada/pycollada/releases), also known as python-collada, is a Python library to read and write Collada (DAE) files. Pycollada is included in the FreeCAD installers for Windows and Mac.

## Rendering

### LuxCoreRender

[LuxCoreRender](https://www.luxcorerender.org) is a render engine, reboot of the [LuxRender](LuxRender.md) project. Officially it is not supported by the [Raytracing Workbench](Raytracing_Workbench.md), but it might be worth to give it a try. It is officially supported by the new [Render Workbench](https://github.com/FreeCAD/FreeCAD-render), intended as a future replacement of the Raytracing Workbench. See the [LuxCoreRender](LuxCoreRender.md) page for more information and installation instructions.

### LuxRender

[LuxRender](https://luxcorerender.org/history/) is one of the two render engines supported by the [Raytracing Workbench](Raytracing_Workbench.md). In 2013 the project has been rebooted becoming [LuxCoreRender](LuxCoreRender.md), with a major code rewriting and compatibility breaking changes. Officially the Raytracing Workbench only supports the abandoned [LuxRender](LuxRender.md) (latest version is 1.6, 2017-12-28), while the new [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) (intended as a future replacement of the Raytracing Workbench) supports instead LuxCoreRender and has dropped the support for LuxRender. Anyway, even if officially not supported, [LuxCoreRender](LuxCoreRender.md) may work with the Raytracing Workbench, it might be worth to give it a try. See the [LuxRender](LuxRender.md) page for more information and installation instructions, and the [LuxCoreRender](LuxCoreRender.md) if you want to try a more modern software.


<div class="mw-translate-fuzzy">

### POVRay

POVRay è un noto raytracer in grado di riprodurre immagini fotorealistiche. È uno dei due raytracer attualmente supportati da FreeCAD nell\'ambiente [Raytracing](Raytracing_Workbench/it.md). Si può scaricare POVRay da <https://www.povray.org>.


</div>

[POV-Ray](https://www.povray.org) is a well-known ray-tracer which can render photo-realistic images. It is one of two render engines currently supported by the [Raytracing Workbench](Raytracing_Workbench.md). See the [POV-Ray](POV-Ray.md) page for more information and installation instructions.


<div class="mw-translate-fuzzy">

### Elementi finiti 


</div>


<div class="mw-translate-fuzzy">

#### CalculiX


</div>


<div class="mw-translate-fuzzy">

CalculiX è una suite di due pacchetti di elementi finiti:

-   CalculiX CrunchiX, o `calculix-ccx`, è un solver FEM.
-   CalculiX GraphiX, o `calculix-cgx`, è una interfaccia grafica per visualizzare i risultati del risolutore.


</div>


<div class="mw-translate-fuzzy">

#### Gmsh


</div>


<div class="mw-translate-fuzzy">

Gmsh è un generatore automatico di mesh ad elementi finiti. Può essere utilizzato in FreeCAD dall\'ambiente [FEM](FEM_Module/it.md) tramite **Mesh → [FEM mesh da shape con gmsh](FEM_MeshGmshFromShape/it.md)**. La homepage di gmsh è su <http://www.geuz.org/gmsh>


</div>


<div class="mw-translate-fuzzy">

#### Elmer


</div>


<div class="mw-translate-fuzzy">

Elmer è un software di simulazione multi-fisica, che è stato aperto nel 2005. In FreeCAD i suoi moduli Grid e Solver possono essere utilizzati da [FEM](FEM_Workbench/it.md) tramite **Risolvi → [Solver Elmer](FEM_SolverElmer/it.md)**. La homepage del progetto è su <https://www.elmerfem.org> e il software può essere scaricato da GitHub all\'indirizzo <https://github.com/ElmerCSC/elmerfem/releases>.


</div>


<div class="mw-translate-fuzzy">

### FEniCS

FEniCS è una piattaforma di calcolo per risolvere equazioni differenziali parziali (PDE), che sono ampiamente utilizzate quando si risolvono i problemi FEM. Come tale può essere usato dall\'ambiente [FEM](FEM_Module/it.md). FreeCAD può importare ed esportare mesh FEniCS tramite **File → Importa** e **File → Esporta** selezionando il formato file **FEM mesh fenics**. La homepage di FEniCS è <https://fenicsproject.org>.


</div>

[FEniCS](https://fenicsproject.org) is a computing platform to solve partial differential equations (PDEs), which are widely used when solving FEM problems. It is used by the [FEM workbench](FEM_Workbench.md)


<div class="mw-translate-fuzzy">

### Z88

Z88 è un altro programma FEM, contenente un mesher, un risolutore e dei convertitori, che può essere utilizzato dall\'ambiente \[\[FEM\_Module/it\|FEM\] di FreeCAD\]. È possibile accedervi tramite **Solve-Solver Z88**. Z88 distribuisce diversi pacchetti, che sono tutti liberamente disponibili, ma sono closed source. Tuttavia, lo Z88OS, pubblicato sotto una licenza open source, è ciò che serve a FreeCAD. La homepage è su <https://en.z88.de/>. Z88OS è anche ospitato su GitHub all\'indirizzo <https://github.com/LSCAD/Z88OS> se si vuole compilarlo da soli.


</div>

[Z88](https://en.z88.de) is another FEM program, containing a mesher, a solver and converters. It is used by the [FEM SolverZ88](FEM_SolverZ88.md) tool. FreeCAD requires the open source Z88OS package.


<div class="mw-translate-fuzzy">

### OpenFOAM

Una libreria per Field Operation and Manipulation (FOAM), necessaria per le simulazioni di fluidodinamica computazionale (CFD). Come tale, OpenFOAM è richiesto dall\'ambiente [FEM](FEM_Module/it.md) di FreeCAD. Si accede tramite il sottomenu **Modello → Fluid constraints**. Il progetto risiede in <https://openfoam.org>.


</div>

[OpenFOAM](https://openfoam.org) is a large collection of libraries for computational fluid dynamics (CFD) simulations. OpenFOAM is used by the [Cfd](Cfd_Workbench.md) and [CfdOF](https://github.com/jaheyns/CfdOF) [external workbenches](external_workbenches.md).


<div class="mw-translate-fuzzy">

## Pagine correlate 

-   [Librerie di terze parti](Third_Party_Libraries/it.md)


</div>

-   [Import Export](Import_Export.md)
-   [Import Export Preferences](Import_Export_Preferences.md)
-   [Third Party Libraries](Third_Party_Libraries.md)


<div class="mw-translate-fuzzy">





</div>

[Category:User Documentation/it](Category:User_Documentation/it.md)
