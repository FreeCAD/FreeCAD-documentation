# Macro Build Utility/it
{{Macro/it
|Name=Macro Build Utility
|Translate=Build Utility
|Description=Questa macro fornisce delle utilità di costruzione per assemblare più file di progetto in un unico file.
|Author=Piffpoof
|Version=1.0
|Date=2015-01-21
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/8/87/Macro_Build_Utility.png ToolBar Icon]
}}

## Descrizione

Questa macro è destinata ad essere utilizzata su grandi progetti, quelli che coinvolgono centinaia di oggetti. È inutile e superfluo utilizzarla su un piccolo progetto con un unico file. Su un grande progetto con molti oggetti e molti file da unire in quello finale, fa risparmiare tempo, evita le azioni ripetitive ed elimina gli errori umani.

## Installazione

Tutto il codice di buildUtility.FCMacro è contenuto in una macro, quindi per installarla basta copiare il suo codice nella appropriata directory delle Macro. Dopo, si può invocare Build Utility dal menu Macro, dalla console Python o da un pulsante della barra degli strumenti (il metodo preferito).

-   per informazioni su come installare il codice delle macro vedere la pagina [Come installare le macro](How_to_install_macros/it.md)
-   per informazioni su come installarla abbinata a un pulsante in una barra degli strumenti vedere la pagina [Personalizzare la barra degli strumenti](Customize_Toolbars/it.md)

## Uso

Build Utility lavora sugli stessi principi dei file di costruzione che vengono utilizzati per assemblare i grandi sistemi software (come FreeCAD). Si utilizza un editor di testo per creare un file di testo che aderisce ai formati richiesti da Build Utility, poi Build Utility legge semplicemente ogni riga del file di testo ed esegue le azioni specificate.

La macro chiede all\'utente un \"build file\", poi lo analizza, ci sono 3 tipi di righe lecite   *

-   le righe che iniziano con il carattere di commento \"\#\" che sono ignorate in quanto sono commenti o osservazioni
-   le righe che iniziano con il carattere sub-file \"@\" che sono ignorate
    Nota   * il carattere \"@\" è per una futura espansione, quando verranno trattati i sub-file
-   tutte le altre righe che possono essere di un file di progetto o di una sotto-directory

L\'estensione per il file Utility Build è \".FCBld\". Questo serve ad evitare che il file sia usato impropriamente da altre applicazioni.

Si presume che il file specificato nel file build abbia l\'estensione \".FCStd\". Se la riga inizia con una directory il file di progetto viene letto da quella sottocartella, in caso contrario, si presume la linea specifichi un file di progetto. Le directory all\'interno di directory sono supportate come nidificazione di profondità arbitraria. Il formato di specificazione del file è lo stile \"Unix\" con diversi livelli separati dal carattere barra \"/\".

Qualsiasi file mancante viene stampato nella Vista Report. Ogni directory mancante è stampata nella Vista Report.

Viene creato un nuovo documento e ogni progetto è un \"Project Merged\" posto in tale nuovo documento vuoto. Alla fine il documento non viene salvato, deve farlo l\'utente, se lo desidera. Quando il file non esiste, il suo nome viene stampato nella vista report

## Interfaccia utente 

Per questa macro non c\'è nessun tipo di GUI. La macro legge un file di testo che è stato preparato con un editor di testo e produce un modello in un documento di output. Basta fare clic sul pulsante nella barra degli strumenti per avviare il processo, non vi è alcuna interazione da parte dell\'utente.

## Opzioni

Non vi è alcuna interfaccia grafica quindi non ci sono opzioni. Esiste solo l\'alternativa di utilizzare uno dei 3 tipi di righe nel file di testo come descritto sopra.

## Osservazioni

Per ribadire quanto affermato all\'inizio, su un singolo file di un piccolo modello questa macro non è di alcuna utilità. Ma è molto utile per chi modella aerei, locomotive, navi, edifici, impianti o circuiti complessi. Si è scelto l\'estensione \".FCBld\" sperando che all\'interno di FreeCAD possa essere impostato questo standard per i file di compilazione . Si spera che il carattere \"@\" riservato per il prefisso nella definizione dei file di comando possa essere accettato in futuro e (se necessario) nello sviluppo.

## Link

nessuno (fino ad ora)

## Script

ToolBar Icon ![](images/Macro_Build_Utility.png )

**Macro\_Build\_Utility.FCMacro**


{{MacroCode|code=
#
#                       Build Utility
#                       v 0.0 - build from files and files in sub-folders
#
#***********************************************************************************
# routine to read in a build file and merge all specified projects
"""
This function asks the user for a "build file". It then parses that build file, there
are 3 legal line types   *
- lines starting with the comment character "#" which are ignored
- lines starting with the subfile character "@" which are ignored
    Note   *   the "@" character is for future enhancement when sub-build files 
            will be handled
- all other lines which may be a project file or a subfolder (sub-directory)
If the line is a subfolder then the project file is read from that subfolder.
Otherwise it is assumed the line specifies a project file.
A new document is created and each project is "Project Merged" into that new and empty document.
The document is not saved at the end, this is left for the user if desired.
If the file does not exist then the file name is Printed to the Report view
"""
"""
Example file   *
#this is a sample build file
#==============================
@sub-build-files - not presently inplemented
# first the top-level file
metal
# now some misc files
./black/black
./blue/blue
# file does not exist
zebra 
# folder does not exist
/bear/bear
# multiple files in one sub-folder
./engineering/green
./engineering/grey
#multiple files in hierarchical folders
./externalModules/white
./externalModules/red/red
#./externalModules/red/stackerAssembly - commented out as not currently loading
./externalModules/red/orange
./externalModules/red/level3/yellow
"""
# import statements
import FreeCAD
import os.path
from PySide import QtGui

# UI Class definitions

# Class definitions

# Function definitionss

# Constant definitions
buildTargetDocument = "build_target"
commentTag = "#"
subfileTag = "@"
lineFeed = "\n"
subfolder = "./"
carriageReturn = "\r"
fileSeparator = "/"
fcFileExtension      = ".FCStd"
fcFileExtensionUC  = ".FCSTD"
fcFileExtensionLen = -6

# code ***********************************************************************************
buildFilePathName=QtGui.QFileDialog.getOpenFileName()[0]
if len(buildFilePathName) > 0   *
    # set up a new empty "build_target" document
    FreeCAD.newDocument(buildTargetDocument)
    FreeCAD.setActiveDocument(buildTargetDocument)
    FreeCAD.ActiveDocument=FreeCAD.getDocument(buildTargetDocument)
    guiDoc=FreeCADGui.ActiveDocument
    #
    lastFileSeparator = buildFilePathName.rindex(fileSeparator)
    buildFilePath = buildFilePathName[   * lastFileSeparator]
    buildFileName = buildFilePathName[lastFileSeparator +1   *]
    #
    buildFileContents = open(buildFilePathName,"r")
    buildFileLines = buildFileContents.readlines()
    buildFileContents.close()
    #
    for line in buildFileLines   *
        if line[0] == commentTag   *
            # line of internal comment
            pass
        elif line[0] == subfileTag   *
            # line of sub-build-file (not presently implemented)
            pass
        else   *
            # a line which should specify a FreeCAD project file
            # - may be preceded by a sub-directory e.g. "./subdir309/"
            # - project file may be missing file extension
            #
            # if line break at end of file spec then remove
            if line[-1   *] == lineFeed   *
                line = line[   *-1]
            if line[-1   *] == carriageReturn   *
                line = line[   *-1]
            # if no FreeCAD project file extension supplied then append one
            # make an uppercase comparison in case of mixed case
            tempLine = fcFileExtension + line.upper()
            if fcFileExtensionUC != tempLine[fcFileExtensionLen   *]   *
                line = line + fcFileExtension
            # if there is a leading subdirectory then remove "./" from beginning
            if subfolder[0   *2] == line[0   *2]   *
                line = line[2   *]
            projectFileSpec = str(buildFilePath) + str("/") + str(line)
            if os.path.exists(projectFileSpec)   *
                guiDoc.mergeProject(projectFileSpec)
            else   *
                FreeCAD.Console.PrintMessage('project file "' + projectFileSpec + '" not found' + "\n")

    # set view back to "build_target", it is up to user to save it (if they want)
    FreeCAD.setActiveDocument(buildTargetDocument)
    FreeCAD.ActiveDocument=FreeCAD.getDocument(buildTargetDocument)
    FreeCADGui.ActiveDocument=FreeCADGui.getDocument(buildTargetDocument)
    FreeCADGui.SendMsgToActiveView("ViewFit")
    FreeCADGui.activeDocument().activeView().viewAxometric()
#
#OS   * Mac OS X
#Word size   * 64-bit
#Version   * 0.14.3703 (Git)
#Branch   * releases/FreeCAD-0-14
#Hash   * c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version   * 2.7.5
#Qt version   * 4.8.6
#Coin version   * 3.1.3
#SoQt version   * 1.5.0
#OCC version   * 6.7.0
#
#thus ends the macro...
}}

## Esempio

State lavorando con alcuni altri reparti della vostra azienda per usare FreeCAD per generare un grande modello CAD per un cliente esterno. Per preparare la presentazione imminente è necessario integrare i modelli rappresentati nei sottosistemi \'black\' e \'blue\', il dipartimento di ingegneria è responsabile dei sottosistemi \'green\' e \'grey\' e voi avete il sottosistema \'metal\' nel vostro computer. Anche il cliente utilizza FreeCAD e la progettazione deve integrarsi con i suoi sottosistemi \"red\', e \'yellow\'. Il cliente esterno vi ha detto che lo Stacker Assembly non è pronto per l\'uso e quindi dovete generare il modello in un vostro file build.

Ci sono un sacco di percorsi di directory da digitare perciò inserite i comandi nel file di testo in Build Utility e dopo potete eseguirli con un semplice clic su un pulsante della barra degli strumenti.

<img alt="" src=images/MacroBuildUtilityTreeDiagram.jpg  style="width   *500px;">

Il contenuto del seguente file di build \"buildFile.FCBld\" mostra la struttura del file per il progetto descritto sopra.


```python
#this is the build file for the complete assembly
#==============================
@sub-build-files - not presently implemented
# first the top-level file
metal
# now some misc files
./black/black
./blue/blue
# file does not exist
zebra 
# folder does not exist
/bear/bear
# multiple files in one sub-folder
./engineering/green
./engineering/grey
#multiple files in hierarchical folders
./externalModules/white
./externalModules/red/red
#./externalModules/red/stackerAssembly - commented out as not currently loading
./externalModules/red/orange
./externalModules/red/level3/yellow
```

Una sintesi del file e del modo in cui viene elaborato è   *

-   le prime due righe vengono trattate come commenti e tutto quello che segue il segno hash come carattere iniziale viene ignorato


```python
#this is the build file for the complete assembly
#==============================
```

-   anche la terza riga è ignorata perché il primo carattere è la \"e commerciale\" che è riservata per un uso futuro in cui i file di comando potranno richiamare altri file di comando


```python
@sub-build-files - not presently implemented
```

-   la quinta linea è la prima specificazione di un file, il file si trova nella stessa directory del file di build, non in una sottodirectory


```python
metal```

-   la settima e l\'ottava riga sono due specificazioni di file in cui il file è in una sotto-directory, notare che la sub-directory è del tipo \"./black/\" dove \"black\" è il nome della directory, quindi un file chiamato \"sheetFold.FCstd\" nella directory \"outsourcing\" appare \"./outsourcing/sheetFold\"


```python
./black/black
./blue/blue```

-   la diciannovesima riga mostra una specificazione di un file che esiste ma che non viene incluso in questa operazione di costruzione


```python
#./externalModules/red/stackerAssembly - commented out as not currently loading```

-   le ultime due righe mostrano la specificazione di file che si trova oltre un livello di sub-directory


```python
./externalModules/red/orange
./externalModules/red/level3/yellow
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Build Utility/it
