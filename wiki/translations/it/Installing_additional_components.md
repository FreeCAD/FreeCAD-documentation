# Installing additional components/it
{{TOCright}}

## Introduzione

Dopo aver installato FreeCAD sul sistema operativo ([Windows](Installing_on_Windows/it.md), [Linux](Installing_on_Linux/it.md) o [Mac](Installing_on_Mac/it.md)), si può prendere in considerazione l\'installazione di uno o più dei seguenti componenti aggiuntivi.

# File di aiuto 

La documentazione offline non viene fornita con tutti i programmi di installazione, ma è disponibile come pacchetto separato. Vedere la pagina [installare file di aiuto](Installing_Helpfile/it.md) per maggiori informazioni.

# Ambienti di lavoro esterni 

Oltre ai pacchetti degli [ambienti di lavoro](workbenches/it.md) forniti di default con FreeCAD, vi è un\'ampia collezione di utili [ambienti complementari](External_workbenches/it.md) realizzati dai membri della comunità.

## Software di terze parti 

FreeCAD supporta molti pacchetti software di terze parti pronti all\'uso. In molti casi l\'unica cosa da fare è installare il software e quando FreeCAD viene riavviato lo troverà automaticamente e sarà in grado di usarlo. Questa sezione intende fornire un elenco di tali pacchetti software, insieme ad alcune informazioni su dove vengono utilizzati in FreeCAD e da dove possono essere scaricati.

## Supporti

### GitPython

_ può usare questa libreria. GitPython è incluso nei programmi di installazione di FreeCAD per Windows e Mac.

### GraphViz

_.

### OpenCAMLib

_. Vedere la pagina [OpenCamLib](OpenCamLib/it.md) per le istruzioni d\'installazione.

### OpenSCAD

_ dipende da questo software e [Mesh Workbench](Mesh_Workbench/it.md) lo utilizza per i suoi strumenti booleani. È richiesto anche per l\'importazione di file SCAD con lo strumento [Std Import](Std_Import/it.md).

## Formati file 

Tutto il software in questa sezione viene utilizzato dagli strumenti [Importa](Std_Import/it.md) o [Esporta](Std_Export/it.md).

### CADExchanger

[CADExchanger](https://cadexchanger.com) è un\'applicazione commerciale per lo scambio di vari formati di file CAD. Esiste un [ambiente di lavoro esterno](https://github.com/yorikvanhavre/CADExchanger) per utilizzare questa applicazione in FreeCAD.

### DXF Importer 

FreeCAD ha un importatore ed esportatore nativo per file DXF, programmato in C++. Attualmente non implementa tutte le funzionalità del formato DXF. Per queste funzionalità sono ancora disponibili l\'importatore ed esportatore Python legacy. Questi richiedono la libreria Python _ per maggiori informazioni.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

### IfcOpenShell

_ ({{VersionMinus|0.18}}) e [BIM IfcExplorer](BIM_IfcExplorer/it.md). IfcOpenShell è incluso nei programmi di installazione di FreeCAD per Windows e Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) è una libreria necessaria per l\'esportazione nel formato file IFCJSON. IFCJSON è un nuovo formato IFC che non è ancora supportato da molte applicazioni.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), noto anche come python-collada, è una libreria Python per leggere e scrivere file Collada (DAE). Pycollada è incluso nei programmi di installazione di FreeCAD per Windows e Mac.

## Rendering

### LuxCoreRender

_. Ufficialmente non è supportato dall\'ambiente _ per ulteriori informazioni e istruzioni di installazione.

### LuxRender

_. Nel 2013 il progetto è stato riavviato diventando _ potrebbe funzionare con l\'ambiente Raytracing, potrebbe valere la pena di provarlo. Vedere la pagina [LuxRender](LuxRender/it.md) per ulteriori informazioni e istruzioni di installazione e [LuxCoreRender](LuxCoreRender/it.md) se si desidera provare un software più moderno.

### POV-Ray 

_. Consulta la pagina [POV-Ray](POV-Ray/it.md) per ulteriori informazioni e istruzioni di installazione.

## Elementi finiti 

### CalculiX

_.

### Gmsh

_ e [Mesh FromPartShape](Mesh_FromPartShape/it.md).

### Elmer

_.

### FEniCS

_.

### Z88

_. FreeCAD richiede il pacchetto open source Z88OS.

### OpenFOAM

_ e _.

# Pagine correlate 

-   [Importazione ed Esportazione](Import_Export/it.md)
-   [Preferenze d\'Importazione ed Esportazione](Import_Export_Preferences/it.md)
-   [Librerie di terze parti](Third_Party_Libraries/it.md)




_

---
[documentation index](../README.md) > Installing additional components/it
