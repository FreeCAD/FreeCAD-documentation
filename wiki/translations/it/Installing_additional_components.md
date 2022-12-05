# Installing additional components/it
{{TOCright}}

## Introduzione

Dopo aver installato FreeCAD sul tuo sistema operativo ([Windows](Installing_on_Windows/it.md), [Linux](Installing_on_Linux/it.md) o [Mac](Installing_on_Mac/it.md)), si può prendere in considerazione l\'installazione di uno o più dei seguenti componenti aggiuntivi.

# File di aiuto 

Vedere [Installazione del file della Guida](Installing_Helpfile/it.md).

# Ambienti di lavoro esterni 

Oltre ai pacchetti degli [ambienti di lavoro](workbenches/it.md) forniti di default con FreeCAD, vi è un\'ampia collezione di utili [ambienti complementari](External_workbenches/it.md) realizzati dai membri della comunità.

## Software di terze parti 

FreeCAD supporta molti pacchetti software di terze parti pronti all\'uso. In molti casi l\'unica cosa da fare è installare il software e quando FreeCAD viene riavviato lo troverà automaticamente e sarà in grado di usarlo. Questa sezione intende fornire un elenco di tali pacchetti software, insieme ad alcune informazioni su dove vengono utilizzati in FreeCAD e da dove possono essere scaricati.

## Supporti

### GitPython

[GitPython](https://github.com/gitpython-developers/GitPython) è una libreria python che viene utilizzata per interagire con i repository Git. L\'[Addon Manager](Std_AddonMgr/it.md) può usare questa libreria. GitPython è incluso nei programmi di installazione di FreeCAD per Windows e Mac.

### GraphViz

[GraphViz](https://www.graphviz.org) è un software di visualizzazione di grafici open source. È utilizzato dallo strumento [Grafico delle dipendenze](Std_DependencyGraph/it.md).

### OpenCAMLib

[OpenCAMLib](http://www.anderswallin.net/CAM) è una libreria open source di algoritmi di produzione assistita da computer (CAM). È utilizzata nell\'ambiente [Path](Path_Workbench/it.md). Vedere la pagina [OpenCamLib](OpenCamLib/it.md) per le istruzioni d\'installazione.

### OpenSCAD

[OpenSCAD](https://www.openscad.org) è un modellatore solido 3D. L\'ambiente [OpenSCAD](OpenSCAD_Workbench/it.md) dipende da questo software e [Mesh Workbench](Mesh_Workbench/it.md) lo utilizza per i suoi strumenti booleani. È richiesto anche per l\'importazione di file SCAD con lo strumento [Std Import](Std_Import/it.md).

## Formati file 

Tutto il software in questa sezione viene utilizzato dagli strumenti [Importa](Std_Import/it.md) o [Esporta](Std_Export/it.md).

### CADExchanger

[CADExchanger](https://cadexchanger.com) è un\'applicazione commerciale per lo scambio di vari formati di file CAD. Esiste un [ambiente di lavoro esterno](https://github.com/yorikvanhavre/CADExchanger) per utilizzare questa applicazione in FreeCAD.

### DXF Importer 

FreeCAD ha un importatore ed esportatore nativo per file DXF, programmato in C++. Attualmente non implementa tutte le funzionalità del formato DXF. Per queste funzionalità sono ancora disponibili l\'importatore ed esportatore Python legacy. Questi richiedono la libreria Python [Draft-dxf-importer](https://github.com/yorikvanhavre/Draft-dxf-importer). Vedere la pagina [Importare i file DXF in FreeCAD](FreeCAD_and_DXF_Import/it.md) per maggiori informazioni.

### Convertitori DWG 

FreeCAD non può leggere e scrivere direttamente file DWG. Per convertire file DXF in file DWG e viceversa, FreeCAD si affida a convertitori esterni. È disponibile il supporto integrato per i seguenti convertitori DWG:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, manca il supporto per alcune entità DWG).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free, ma non open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commerciale). <small>(v0.20)</small> 

Vedere [Preferenze di Importa/Esporta](Import_Export_Preferences/it#DWG.md) e [Importare i file DWG in FreeCAD](FreeCAD_and_DWG_Import/it.md) per maggiori informazioni.

### IfcOpenShell

[IfcOpenShell](http://ifcopenshell.org) è una libreria per lavorare con il formato file Industry Foundation Classes (IFC) utilizzato nella progettazione architettonica. La libreria è utilizzata anche dagli strumenti [Arch IfcExplorer](Arch_IfcExplorer/it.md) ({{VersionMinus|0.18}}) e [BIM IfcExplorer](BIM_IfcExplorer/it.md). IfcOpenShell è incluso nei programmi di installazione di FreeCAD per Windows e Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) è una libreria necessaria per l\'esportazione nel formato file IFCJSON. IFCJSON è un nuovo formato IFC che non è ancora supportato da molte applicazioni.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), noto anche come python-collada, è una libreria Python per leggere e scrivere file Collada (DAE). Pycollada è incluso nei programmi di installazione di FreeCAD per Windows e Mac.

## Rendering

### LuxCoreRender

[LuxCoreRender](https://www.luxcorerender.org) è un motore di rendering, reboot del progetto [LuxRender](LuxRender/it.md). Ufficialmente non è supportato dall\'ambiente [Raytracing](Raytracing_Workbench/it.md), ma potrebbe valere la pena di provarlo. È ufficialmente supportato dal nuovo ambiente [Render](https://github.com/FreeCAD/FreeCAD-render), inteso come futuro sostituto dell\'ambiente Raytracing. Vedere la pagina [LuxCoreRender](LuxCoreRender/it.md) per ulteriori informazioni e istruzioni di installazione.

### LuxRender

[LuxRender](https://luxcorerender.org/history/) è uno dei due motori di rendering supportati dall\'ambiente [Raytracing](Raytracing_Workbench/it.md). Nel 2013 il progetto è stato riavviato diventando [LuxCoreRender/it](LuxCoreRender/it.md), con un\'importante riscrittura del codice e modifiche alla compatibilità. Ufficialmente l\'ambiente Raytracing supporta solo [LuxRender](LuxRender.md) che è stato dismesso (l\'ultima versione è la 1.6 del 28/12/2017), mentre il nuovo ambiente [Render](https://github.com/FreeCAD/FreeCAD-render) (destinato in futuro a sostituire l\'ambiente Raytracing) supporta LuxCoreRender ed ha abbandonato il supporto per LuxRender. Comunque, anche se ufficialmente non supportato, [LuxCoreRender](LuxCoreRender/it.md) potrebbe funzionare con l\'ambiente Raytracing, potrebbe valere la pena di provarlo. Vedere la pagina [LuxRender](LuxRender/it.md) per ulteriori informazioni e istruzioni di installazione e [LuxCoreRender](LuxCoreRender/it.md) se si desidera provare un software più moderno.

### POV-Ray 

[POV-Ray](https://www.povray.org) è un noto ray-tracer che può rendere immagini fotorealistiche. È uno dei due motori di rendering attualmente supportati dall\'ambiente [Raytracing](Raytracing_Workbench/it.md). Consulta la pagina [POV-Ray](POV-Ray/it.md) per ulteriori informazioni e istruzioni di installazione.

## Elementi finiti 

### CalculiX

[CalculiX](http://calculix.de) è una suite di due pacchetti di elementi finiti: CalculiX CrunchiX, un risolutore FEM, e CalculiX GraphiX, un frontend GUI. Solo il risolutore è supportato da FreeCAD. Viene utilizzato dallo strumento [Risolutore CalculiX](FEM_SolverCalculiX/it.md).

### Gmsh

[Gmsh](http://gmsh.info) è un generatore automatico di mesh agli elementi finiti. è utilizzato dagli strumenti [FEM MeshGmshFromShape](FEM_MeshGmshFromShape/it.md) e [Mesh FromPartShape](Mesh_FromPartShape/it.md).

### Elmer

[Elmer](https://www.csc.fi/web/elmer) è un software di simulazione multifisica, che è stato reso open source nel 2005. In FreeCAD i suoi moduli Grid e Solver sono utilizzati dallo strumento [FEM SolverElmer](FEM_SolverElmer/it.md).

### FEniCS

[FEniCS](https://fenicsproject.org) è una piattaforma di calcolo per risolvere equazioni differenziali alle derivate parziali (PDE), ampiamente utilizzate per la risoluzione di problemi FEM. Viene utilizzato dall\'ambiente [FEM](FEM_Workbench/it.md).

### Z88

[Z88](https://en.z88.de) è un altro programma FEM, contenente un mesher, un risolutore e convertitori. Viene utilizzato dallo strumento [FEM SolverZ88](FEM_SolverZ88/it.md). FreeCAD richiede il pacchetto open source Z88OS.

### OpenFOAM

[OpenFOAM](https://openfoam.org) è una vasta raccolta di librerie per simulazioni di fluidodinamica computazionale (CFD). OpenFOAM è utilizzato dall\'ambiente [Cfd](Cfd_Workbench/it.md) e [CfdOF](https://github.com/jaheyns/CfdOF) [external_workbench](external_workbench.md).

# Pagine correlate 

-   [Importazione ed Esportazione](Import_Export/it.md)
-   [Preferenze d\'Importazione ed Esportazione](Import_Export_Preferences/it.md)
-   [Librerie di terze parti](Third_Party_Libraries/it.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing additional components/it
