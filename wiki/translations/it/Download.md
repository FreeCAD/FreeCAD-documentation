# Download/it
## Versione stabile attuale 

La versione 1.0 di FreeCAD è stata pubblicata il 18-11-2024. Per scoprire le novità, consulta le [note di rilascio](Release_notes_1.0/it.md).

Il checksum SHA256 per verificare l\'integrità del download si trova [nella pagina di rilascio 1.0.0](https://github.com/FreeCAD/FreeCAD/releases/tag/1.0.0).

Le versioni precedenti possono essere scaricate dalla pagina di [rilascio](https://github.com/FreeCAD/FreeCAD/releases)

+::+::+::+
| ![](images/Windows.png )                                                                                                          | ![](images/Mac.png )                                                                                                            | ![](images/Linux_with_text.png )                                                                                  |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [Install instructions](Installing_on_Windows.md)                                                                                | [Install instructions](Installing_on_Mac.md)                                                                              | [Install instructions](Installing_on_Linux.md)                                                                          |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-installer-1.exe)       | [ARM (M-series) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-arm64-py311.dmg) | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage)   |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-py311.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-x86_64-py311.dmg)         | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-aarch64-py311.AppImage) |
++++



### Note per gli utenti di Windows 

-   Le seguenti versioni di Windows sono supportate: 64-bit 8/10/11.
-   Il pacchetto può anche essere installato dal gestore [Chocolatey](https://chocolatey.org/packages/freecad). Il pacchetto Chocolatey al momento non è aggiornato.



### Note per gli utenti di macOS 

-   MacOS 10.12 Sierra è la versione minima supportata.



### Note per gli utenti GNU/Linux 

La maggior parte delle distribuzioni contiene FreeCAD nei propri repository ufficiali, tuttavia, se la distribuzione non segue un modello di rilascio progressivo, la versione fornita potrebbe non essere aggiornata. Invece si può scaricare l\'AppImage sopra, contrassegnarla come eseguibile e avviarla senza installazione.

Si prega di consultare la pagina [Installare in Linux](Installing_on_Linux/it.md) per ulteriori opzioni di installazione, inclusi i pacchetti giornalieri per Ubuntu e derivate.

Una versione portatile che non necessita di installazione può essere ottenuta avviando FreeCAD con questi comandi:


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Maggiori informazioni sulle variabili d\'ambiente di FreeCAD sono disponibili sulla [ pagina di configurazione](Start_up_and_Configuration/it#Environment_variables.md).



## Versioni di sviluppo 

Lo sviluppo di FreeCAD è sempre attivo.

-   Per build di sviluppo e codice sorgente di sviluppo, vedere la pagina [build settimanali](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).

Qui sono disponibili build settimanali per Linux, MacOS e Windows. Per Linux, sono disponibili anche build giornaliere: utilizzare il canale edge di [snap package](Ubuntu_Snap/it.md) o il [PPA giornaliero di FreeCAD](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (quest\'ultimo solo per le distribuzioni basate su Debian).

-   Per compilare il codice sorgente più recente, consultare la pagina [compilazione](Compiling/it.md).



## Moduli aggiuntivi e macro 

La comunità di FreeCAD offre numerosi moduli e macro aggiuntivi. Possono essere facilmente installati direttamente da FreeCAD usando l\'<img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md).



---
⏵ [documentation index](../README.md) > Download/it
