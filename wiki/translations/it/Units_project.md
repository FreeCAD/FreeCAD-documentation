


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Questo progetto è volto a implementare in FreeCAD un adeguato Sistema di Unità di misura. Esso segue le regole della metodologia \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\] (metodo per l\'organizzazione delle proprie azioni, per la gestione del tempo e dei progetti per \'fare in modo che le cose vengano fatte\'). I progetti sono raccolti nel [Piano di sviluppo](Development_roadmap/it.md) (Development roadmap).

## Finalità e principi 

Questo è un progetto di sviluppo del software il cui scopo è di implementare in FreeCAD un ambiente per un Sistema di Unità di misura.

Le fasi dello sviluppo sono pianificate qui (nelle Azioni successive) e sono monitorate nel sistema di gestione delle modifiche per conservare un registro storico delle modifiche ben strutturato in: [Issue Tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Risultati

Consentire a FreeCAD di gestire i Sistemi di misura collegati, quali il sistema imperiale, e i componenti delle unità complesse del [Sistema Internazionale SI](http://it.wikipedia.org/wiki/Sistema_internazionale_di_unità_di_misura).
Gestire anche l\'importazione e l\'esportazione dei formati che sono in grado di trasportare unità (come STEP).
Permettere la scalatura basata sulla assunzione di Unità (mm→m, m→in).

## Riflessioni

Le numerose discussioni che sono state fatte in: <http://forum.freecadweb.org/viewtopic.php?f=10&t=1616>

Inoltre molte delle informazioni che si trovano nell\'articolo [ Unità di misura](Units/it.md).

## Organizzazione

### Aggiornare l\'analizzatore delle unità 

Aggiornare il parser (l\'analizzatore) per gestire e generare le firme come discusso nell\'articolo [ Unità di misura](Units/it.md).

### Propietà

Cambiare la forma delle proprietà, ad esempio passare da PropertyLength a PropertyUntit, con una firma di unità.

Creare eventualmente un editor delle proprietà per le PropertyUntit.

### Ambienti

-   Aggiornare gli ambienti di lavoro per consentire di utilizzare la struttura Unità. Vorrei iniziare dagli ambienti Schizzo e PartDesign e proseguire in ordine \...
-   Documentare questo processo di aggiornamento in modo che altri possono fare lo stesso lavoro con altri ambienti di lavoro \--[Yorikvanhavre](User:Yorikvanhavre.md) 13:13, 28 November 2011 (UTC)

## Azioni successive 

-   Aggiornare l\'analizzatore delle Unità (jriegel)



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
