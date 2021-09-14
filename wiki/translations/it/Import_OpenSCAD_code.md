# Import OpenSCAD code/it




{{TutorialInfo/it
|Topic= Importare codice OpenSCAD
|Level= Base
|Time= 30 minuti
|Author=r-frank
|FCVersion=0.16.6704
|Files=
}}

## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

OpenSCAD è un programma open source di CAD 3D, come FreeCAD. Ma mentre FreeCAD utilizza un approccio visivo, OpenSCAD utilizza un\'interfaccia di programmazione per eseguire le operazioni in 3D. L\'ambiente OpenSCAD di FreeCAD può essere utilizzato per importare il codice OpenSCAD dell\'oggetto e per accedere ad alcune delle operazioni sulle mesh possibili con OpenSCAD.


</div>

## Installing OpenSCAD 


<div class="mw-translate-fuzzy">

## Installare OpenSCAD 

Gli utenti Mac possono scaricare i file binari da [OpenSCAD homepage](http://www.openscad.org/).
Gli utenti Linux Ubuntu/Mint possono installarlo dai repository di sistema o da [OpenSCAD homepage](http://www.openscad.org/).
Gli utenti Windows possono scaricare il programma da [OpenSCAD homepage](http://www.openscad.org/).
Dato che è necessario solo l\'eseguibile OpenSCAD, gli utenti Windows di FreeCAD possono installare la versione portabile, se preferiscono.


</div>

## Configuring OpenSCAD workbench in FreeCAD 


<div class="mw-translate-fuzzy">

## Configurare l\'ambiente OpenSCAD in FreeCAD 

-   Avviare FreeCAD
-   Passare all\'ambiente [OpenSCAD](OpenSCAD_Workbench/it.md)
-   Scegliere Modifica → Preferenze → OpenSCAD dal menu principale
    -   Indirizzare FreeCAD all\'eseguibile di OpenSCAD (sezione: Impostazioni generali di OpenSCAD)
    -   Tutti gli altri valori nella pagina delle impostazioni possono essere lasciati di default


</div>

## The sample model 


<div class="mw-translate-fuzzy">

## Il modello di esempio 

Qui viene usato il file example005.scad dai (vecchi) esempi OpenSCAD, ma si può utilizzare, a piacere, qualsiasi file scad.
<img alt="" src=images/TutorialOpenSCAD_SampleFile.jpg  style="width:800px;">


</div>

<img alt="" src=images/TutorialOpenSCAD_SampleFile.jpg  style="width:800px;">

## Importing the model in FreeCAD 


<div class="mw-translate-fuzzy">

## Importare il modello in FreeCAD 

-   In FreeCAD scegliere ** File** → ** Apri** e scegliere il file .scad che si desidera importare.
-   Non è importante che l\'ambiente OpenSCAD sia attivato. L\'ambiente OpenSCAD è necessario solo quando si applicano specifiche funzioni al modello.
-   FreeCAD importa il file OpenSCAD e costruisce un albero con le primitive e le operazioni booleane.
-   Il tutorial è finito.

<img alt="" src=images/TutorialOpenSCAD_ImportFile.jpg  style="width:800px;">


</div>

<img alt="" src=images/TutorialOpenSCAD_ImportFile.jpg  style="width:800px;">

## Correlazioni

-   [FreeCAD\_Howto\_Import\_Export](FreeCAD_Howto_Import_Export.md)
-   [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md)

[Category:OpenSCAD](Category:OpenSCAD.md)
