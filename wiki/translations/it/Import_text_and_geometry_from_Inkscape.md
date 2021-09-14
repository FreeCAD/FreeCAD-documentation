# Import text and geometry from Inkscape/it

 {{TutorialInfo/it
|Topic= Importare testo e  geometria da Inkscape
|Level= Base
|Time= 30 minuti
|Author=r-frank
|FCVersion=0.16.6704
|Files=
}}

## Introduzione

Questo tutorial si propone di mostrare come importare in FreeCAD testo o geometria creata con Inkscape nel formato svg.
Per queste operazioni sono utilizzati Inkscape 0.91 e FreeCAD 0.16.6704 in Windows.

## Consigli generali per importare da Inkscape 

-   l\'importatore SVG di FreeCAD non può gestire un file in formato SVG con una risoluzione superiore a 45 dpi, quindi controllare le impostazioni di Inkscape
-   se nella vista 3D in FreeCAD gli oggetti *tracciato* (path) importati non appaiono molto lisci questo può dipendere dalle impostazioni di FreeCAD per la vista della forma.
    -   in FreeCAD scegliere ** Edit** → ** Preferenze** → ** Part Design** → ** Visualizzazione della figura**
    -   per \"Tassellazione\", il valore della \"Deviazione massima secondo il riquadro di delimitazione del modello\" di default è \"0,5 %\"
    -   impostando questo ad un valore inferiore si aumenta la levigatezza del modello nella vista 3D (e si usano più risorse del PC)
    -   non utilizzare valori inferiori a \"0,01 %\", questo molto probabilmente blocca FreeCAD
    -   in tal caso la cancellazione di \"system.cfg\" e \"user.cfg\" nella directory utente di FreeCAD risolve questo problema

## Importare testo da Inkscape 

-   in Inkscape, dopo aver inserito il testo (e forse aver applicato ad esso degli effetti, come la piegatura o altro) fare in modo di
    -   selezionare il testo e scegliere **Tracciato** → ** Da oggetto a tracciato**
    -   separare gli oggetti con **Tracciato** → ** Separa**
    -   salvare nel formato \"SVG puro (\*.svg)\"
-   aprire il file in FreeCAD, e scegliere l\'opzione \"SVG as geometry (importSVG)\"
-   nella vista ad albero viene creato un oggetto *tracciato* (path) per ogni lettera, numero o segno
-   usare lo strumento [Promuovi](Draft_Upgrade/it.md) di Draft su ogni oggetto *tracciato* per creare le facce
-   utilizzare gli strumenti pad o [estrusione](Part_Extrude/it.md) sulle facce per ottenere solidi
-   si possono fondere gli oggetti o utilizzare dei loro composti, secondo le esigenze

## Importare geometria da Inkscape 

Dato che Inkscape e FreeCAD sembrano avere approcci diversi sul modo di applicare dimensioni a un oggetto svg, il flusso di lavoro consigliato sembra essere questo:

-   separare tutti gli oggetti in Inkscape
-   selezionare tutti gli oggetti in Inkscape
-   applicare per tutti gli oggetti uno stile di traccia con una larghezza di 0 mm (sì, zero millimetri)
-   salvare il file nel formato \"Inkscape SVG (\*.svg)\" o \"SVG puro (\*.svg)\"
-   aprire il file in FreeCAD, e scegliere l\'opzione \"SVG as geometry (importSVG)\"
-   in questo modo le dimensioni degli oggetti in Inkscape e in FreeCAD dovrebbero essere identiche

## Crediti

Grazie agli utenti \"freecad-heini-1\" e \"herbk\" per la verifica e per aver fornito un prezioso feedback.




