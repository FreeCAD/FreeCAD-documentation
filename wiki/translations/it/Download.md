# Download/it

 {{TOCright}}

## Versione stabile attuale 


<div class="mw-translate-fuzzy">

La prima versione 0.18 di FreeCAD (16093) è stata pubblicata il 2019-03-12. Dopo è stata pubblicata una versione di correzione di bug, l\'ultima versione di correzione di bug è la **0.18.4 (0.18.16146)** ed è stata pubblicata il 2019-10-26. Per scoprire le novità, consultare le [note di rilascio](Release_notes_0.18/it.md).


</div>


<div class="mw-translate-fuzzy">

Il checksum SHA256 per verificare l\'integrità del download si trova in [0.18.4 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.4).


</div>

Previous versions can be downloaded from the [releases](https://github.com/FreeCAD/FreeCAD/releases) page

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| [64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-installer1.exe) (includes installer) |   | [macOS](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD_0.19-24291-macOS-x86_64-conda.dmg) 64-bit |   | [AppImage](AppImage.md) 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+


<div class="mw-translate-fuzzy">

### Note per gli utenti di Windows 

-   L\'installatore 32-bit (x86) supporta le seguenti versioni di Windows: 7/8/10.
-   L\'installatore 64-bit (x64) supporta le seguenti versioni di Windows: 7/8/10.
-   Una versione portatile (64 bit) che non necessita di installazione si trova nella pagina di rilascio.
-   Il pacchetto può anche essere installato dal gestore [Chocolatey](https://chocolatey.org/packages/freecad).


</div>


<div class="mw-translate-fuzzy">

### Note per gli utenti di Mac 

Mac OS X 10.11 *El Capitan* è la versione minima supportata.


</div>

### Note per gli utenti GNU/Linux 

La maggior parte delle distribuzioni contiene FreeCAD nei propri repository ufficiali, tuttavia, se la distribuzione non segue un modello di rilascio progressivo, la versione fornita potrebbe non essere aggiornata. Invece si può scaricare l\'AppImage sopra, contrassegnarla come eseguibile e avviarla senza installazione.


<div class="mw-translate-fuzzy">

Per ulteriori opzioni di installazione, incluso come ottenere i pacchetti aggiornati per Ubuntu e derivate, si prega di consultare la pagina [Compilazione in Linux](Compile_on_Linux/it.md).


</div>

A portable version that doesn\'t need installation can be achieved by starting FreeCAD with these commands: <small>(v0.19)</small>  
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```

More information about FreeCAD\'s environment variables can be found on [the configuration page](Start_up_and_Configuration#Environment_variables.md).


<div class="mw-translate-fuzzy">

## Versioni di sviluppo 

Lo sviluppo di FreeCAD è sempre attivo.

-   Per gli utenti Linux, controllare lo sviluppo in [AppImage](AppImage/it.md).
-   Per le build di sviluppo di MacOS e Windows e il codice sorgente di sviluppo, consultare la pagina [FreeCAD/releases](https://github.com/FreeCAD/FreeCAD/tags).
-   Per compilare il codice sorgente più recente, consultare la pagina [compilazione](Compiling/it.md).


</div>

## Moduli aggiuntivi e macro 

La comunità di FreeCAD offre numerosi moduli e macro aggiuntivi. Dalla versione 0.17 essi possono essere facilmente installati direttamente da FreeCAD usando il [Gestore delle estensioni (Addon manager)](Addon_Manager/it.md) <img alt="" src=images/AddonManager.svg  style="width:22px;">.



