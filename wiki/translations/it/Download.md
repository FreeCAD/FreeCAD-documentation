# Download/it
## Versione stabile attuale 

La versione 0.21.2 di FreeCAD è stata pubblicata il 14-11-2023. Per scoprire le novità, consulta le [note di rilascio](Release_notes_0.21/it.md).

Il checksum SHA256 per verificare l\'integrità del download si trova [nella pagina di rilascio 0.21.2](https://github.com/FreeCAD/FreeCAD/releases/tag/0.21.2).

Le versioni precedenti possono essere scaricate dalla pagina di [rilascio](https://github.com/FreeCAD/FreeCAD/releases)

+::+::+::+
| ![](images/Windows.png )                                                                                                | ![](images/Mac.png )                                                                                                | ![](images/Linux_with_text.png )                                                                        |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [Install instructions](Installing_on_Windows.md)                                                                      | [Install instructions](Installing_on_Mac.md)                                                                  | [Install instructions](Installing_on_Linux.md)                                                                |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-WIN-x64-installer-1.exe)        | [ARM (M1/M2) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-arm64.dmg)  | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-x86_64.AppImage)   |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Windows-x86_64.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-intel-x86_64.dmg) | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-aarch64.AppImage) |
++++



### Note per gli utenti di Windows 

-   Le seguenti versioni di Windows sono supportate:64-bit 7/8/10/11. La versione 32-bit Windows non è supportata.
-   Il pacchetto può anche essere installato dal gestore [Chocolatey](https://chocolatey.org/packages/freecad). Il pacchetto Chocolatey al momento non è aggiornato.



### Note per gli utenti di macOS 

-   MacOS 10.12 Sierra è la versione minima supportata.
-   Per macOS 12 e versioni precedenti è necessario utilizzare l\'\"immagine disco Intel non firmata\", la versione firmata non funziona su tali sistemi.



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
-   Per compilare il codice sorgente più recente, consultare la pagina [compilazione](Compiling/it.md).



## Moduli aggiuntivi e macro 

La comunità di FreeCAD offre numerosi moduli e macro aggiuntivi. Dalla versione 0.17 essi possono essere facilmente installati direttamente da FreeCAD usando l\'<img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md).



---
⏵ [documentation index](../README.md) > Download/it
