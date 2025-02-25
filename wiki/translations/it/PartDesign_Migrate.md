---
 GuiCommand:
   Name: PartDesign Migrate
   Name/it: Migra
   MenuLocation: Part Design , Migra
   Workbenches: PartDesign_Workbench/it
   Version: 0.17
---

# PartDesign Migrate/it



## Descrizione

PartDesign in FreeCAD v0.17 introduce nuovi strumenti ed elementi che non sono riconosciuti dalle vecchie versioni di FreeCAD (0.16 e precedenti). I documenti di FreeCAD creati con versioni precedenti possono ancora essere aperti e modificati. Per beneficiare delle nuove funzionalità, è necessario migrarle tramite il menu PartDesign → Migra.


{{Version/it|0.17}}



## Utilizzo

1.  Aprire un documento di FreeCAD creato con {{VersionMinus/it|0.16}}
2.  Passare a **<img src="images/Workbench_PartDesign.svg" width=16px> [PartDesign](PartDesign_Workbench/it.md)**.
3.  Andare al menu **Part Design** → **Migra**.
4.  Se la migrazione funziona, viene creato un <img alt="" src=images/Std_Part.svg  style="width:24px;"> [contenitore Part](Std_Part/it.md) che contiene uno o più <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpi](PartDesign_Body/it.md), ognuno dei quali ospita una catena di funzioni.



## Limitazioni

-   Prima di iniziare il processo di migrazione, verificare se il modello è stato creato con le opzioni di affinamento automatico abilitate (in **Modifica → Preferenze → Part design → Generale**) e impostare le preferenze di conseguenza. Ciò può essere facilmente determinato commutando successivamente la visibilità delle funzioni nell\'albero del modello. Se non sono rimasti bordi residui tra funzioni come Pad e Tasche, le opzioni di affinazione automatica sono state disabilitate.
-   Se un documento da migrare contiene solo schizzi e funzionalità di PartDesign, è probabile che il processo di migrazione abbia esito positivo. Alcune funzionalità come smussi e raccordi possono richiedere la ricostruzione.
-   Se il documento da migrare ha un flusso di lavoro misto Parte/Part Design/Draft, la conversione molto probabilmente fallisce o, al massimo, produce risultati imprevisti, e il documento deve essere migrato manualmente.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Migrate/it
