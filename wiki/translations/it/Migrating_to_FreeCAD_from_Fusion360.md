 {{TOCright}}

## Sfondo

Questa pagina è destinata agli utenti che sono interessati a migrare a FreeCAD dal mondo di Fusion 360.

## Cosa devo fare? 

1.  La prima cosa che vuoi fare è togliere i tuoi file dai formati e dagli archivi proprietari. Iniziate esportando i vostri modelli dal cloud alla vostra macchina locale.
    -   Un metodo popolare è l\'utilizzo di questo script [Fusion360 total exporter](https://github.com/Jnesselr/fusion-360-total-exporter).
2.  Si consiglia di esportare in formato STEP.

## Glossario


{{VeryImportantMessage|Si prega di fare riferimento anche al progetto in corso [CAD Rosetta Stone](CAD_Rosetta_Stone.md) per imparare i nomi analoghi che i popolari CAD proprietari usano}}

.

Fate riferimento alla pagina del [Glossario](Glossary/it.md) in generale, ma qui c\'è una breve lista di termini specifici che la gente di F360 può trovare particolarmente utile:


<div class="mw-translate-fuzzy">

-   Vincolo tangente - la forma di FreeCAD di **Vincolo Collineare**. Vedi <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Sketcher\_VincoloTangente](Sketcher_ConstrainTangent/it#Tra_due_linee_.28collineari.29.md).
-   Pad - La funzione **estrudi** in FreeCAD. Leggi il <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad/it.md) per saperne di più.
-   Toponaming - Abbreviazione di [Problema di denominazione topologica](Topological_naming_problem/it.md). Coperto molto bene in [Brodie Fairhall\'s youtube clip](https://www.youtube.com/watch?v=6p2vqEEmWq4)\].
--   


</div>

## DOMANDE FREQUENTI 

1.  Quali formati sono supportati in FreeCAD?
    -   Il formato di file nativo in FreeCAD è BREP, [rappresentazione per contorni](https://it.wikipedia.org/wiki/B-rep), fornito dal kernel geometrico interno [OpenCASCADE (OCCT)](OpenCASCADE/it.md).
    -   FreeCAD supporta tutti i formati supportati da OCCT, quindi almeno STEP e IGES.
2.  Quali formati dovrei usare per migrare a FreeCAD?
    -   STEP è il miglior formato perché è un formato solido [Forma](Shape/it.md), al contrario di un [Mesh](Mesh/it.md) (STL, OBJ, DAE). Esempio, [Importazione del passo con i colori](https://forum.freecadweb.org/viewtopic.php?f=3&t=50308).
    -   Importare un STL è possibile, ma questo formato di mesh sarà difficile da modificare ulteriormente. Si consiglia di convertire le mesh importate in forme solide usando **<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part ShapeFromMesh](Part_ShapeFromMesh/it.md)**. Rimodellare l\'oggetto in FreeCAD, usando la mesh come riferimento, è il miglior consiglio.

## Suggerimenti

-   \@MPetrika ([twitter](https://twitter.com/MPetrikas/status/1362051484704264198)) raccomanda di installare il [ModernUI Workbench](ModernUI_Workbench/it.md) di HakanSeven12

## Risorse di apprendimento 


<div class="mw-translate-fuzzy">

-   [Fusion360 a FreeCAD - Introduzione](https://www.youtube.com/watch?v=_GxJkB23ZHM), video di Brodie Fairhall.
-   [Fusion360 a FreeCAD - Parte 2](https://www.youtube.com/watch?v=IESZD4QS3P8), video di Brodie Fairhall.
-   [V0.19 Benchmarking\--2019 Sfide Mensili](https://forum.freecadweb.org/viewtopic.php?f=36&t=50492), una serie di oggetti creati con Fusion360 vengono rimodellati usando FreeCAD, dall\'utente esperto ppemawm.
-   [Tutorial scritto per principianti: dalla prima parte al disegno tecnico](https://github.com/macdroid53/LearningFreeCAD).
-   [Una risorsa online per noi utenti abituali di FreeCAD](https://www.freecad.info/).


</div>

## Video comparativi 

-   [Modellare una turbina del compressore in FreeCAD e Fusion360](https://www.youtube.com/watch?v=kirDbZd0dvI&feature=youtu.be)

## Aiuto

A questa pagina wiki manca qualcosa. Fai una richiesta per [permessi wiki](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) sul forum per modificare questa pagina.

## Relativo

-   [Migrare a FreeCAD da OnShape](Migrating_to_FreeCAD_from_OnShape/it.md)



