# Download/it
{{TOCright}}



## Versione stabile attuale 

La versione 0.20.2 di FreeCAD (29410) è stata pubblicata il 07-12-2022. Per scoprire le novità, consultare le [note di rilascio](Release_notes_0.20/it.md).

Il checksum SHA256 per verificare l\'integrità del download si trova [nella pagina di rilascio 0.20.2](https://github.com/FreeCAD/FreeCAD/releases/tag/0.20.2).

Le versioni precedenti possono essere scaricate dalla pagina di [rilascio](https://github.com/FreeCAD/FreeCAD/releases)

+::+::+::+
| ![](images/Windows.png )                                                                                         | ![](images/Mac.png )                                                                                                             | ![](images/Linux_with_text.png )     |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                 | [Install on Mac](Installing_on_Mac.md)                                                                                     | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD-0.20.2-WIN-x64-installer-3.exe) | [macOS 64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD_0.20.2-2022-12-27-conda-macOS-x86_64-py310.dmg) | [AppImage 64-bit](AppImage.md)             |
++++

### Note per gli utenti di Windows 

-   Le seguenti versioni di Windows sono supportate:64-bit 7/8/10/11. La versione 32-bit Windows non è supportata.
-   Una versione portatile che non necessita di installazione si trova nella pagina di [rilascio](https://github.com/FreeCAD/FreeCAD/releases/).
-   Il pacchetto può anche essere installato dal gestore [Chocolatey](https://chocolatey.org/packages/freecad).

### Note per gli utenti di macOS 

macOS 10.12 Sierra è la versione minima supportata.



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
![](images/Right_arrow.png) [documentation index](../README.md) > Download/it
