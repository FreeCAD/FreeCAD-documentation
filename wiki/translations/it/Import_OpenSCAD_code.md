---
 TutorialInfo:t
   Topic:  Importare codice OpenSCAD
   Level:  Base
   Time:  30 minuti
   Author: r-frank
   FCVersion: 0.16.6704
   Files: 
---

# Import OpenSCAD code/it







## Introduzione

OpenSCAD è un programma open source di CAD 3D, come FreeCAD. Ma mentre FreeCAD utilizza un approccio visivo, OpenSCAD utilizza un\'interfaccia di programmazione per eseguire le operazioni in 3D. L\'ambiente OpenSCAD di FreeCAD può essere utilizzato per importare il codice OpenSCAD dell\'oggetto e per accedere ad alcune delle operazioni sulle mesh possibili con OpenSCAD.



## Installare OpenSCAD 

-   Gli utenti Linux possono eseguire l\'installazione dai repository di distribuzione pertinenti, come Debian, openSUSE, Mint, Unbuntu, ecc. o dalla [di OpenSCAD](http://www.openscad.org/homepage).
-   Gli utenti Mac possono scaricare i file binari dalla [di OpenSCAD](http://www.openscad.org/homepage).
-   Gli utenti Windows possono scaricare il programma dalla [di OpenSCAD](http://www.openscad.org/homepage). Poiché FreeCAD necessita solo dell\'eseguibile OpenSCAD, gli utenti Windows possono installare la versione portatile, se lo desiderano.



## Configurare l\'ambiente OpenSCAD in FreeCAD 

-   Aprire FreeCAD.
-   Passare all\'[ambiente OpenSCAD](OpenSCAD_Workbench/it.md).
-   Scegliere Modifica → Preferenze → OpenSCAD dal menu principale.
    -   Far puntare FreeCAD all\'eseguibile OpenSCAD (sezione: Impostazioni generali di OpenSCAD).
    -   Tutti gli altri valori nella pagina delle impostazioni potrebbero essere lasciati ai valori predefiniti.



## Il modello di esempio 

Qui viene usato il file example005.scad dai (vecchi) esempi OpenSCAD, ma si può utilizzare, a piacere, qualsiasi file scad.

<img alt="" src=images/TutorialOpenSCAD_SampleFile.jpg  style="width:800px;">



## Importare il modello in FreeCAD 

-   In FreeCAD basta scegliere ** File** → ** Apri** e scegliere il file .scad che si desidera importare.
-   Non è importante quale ambiente di lavoro è attivo, l\'ambiente di lavoro OpenSCAD stesso è necessario solo quando si applicano funzionalità speciali al modello.
-   FreeCAD importerà il file OpenSCAD e creerà un albero con primitive e operazioni booleane
-   Tutorial terminato.

<img alt="" src=images/TutorialOpenSCAD_ImportFile.jpg  style="width:800px;">



## Correlazioni

-   [FreeCAD_Howto_Import_Export](FreeCAD_Howto_Import_Export.md)
-   [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md)



---
⏵ [documentation index](../README.md) > [OpenSCAD](Category_OpenSCAD.md) > [Import](Import_Workbench.md) > Import OpenSCAD code/it
