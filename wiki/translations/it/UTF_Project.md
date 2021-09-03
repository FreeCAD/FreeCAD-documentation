


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Questa è la pianificazione del progetto per la parte del [Piano di sviluppo](Development_roadmap/it.md) di FreeCAD.

## Finalità e principi 

Migliorare la capacità di utilizzare più lingue in FreeCAD implementando il supporto per i caratteri UTF all\'interno dell\'interfaccia Coin3D.

Nonostante ora Coin3D sia passato a una piattaforma di sviluppo più aperta, è ancora molto difficile contribuire a questo progetto.

(mrlukeparry) Ho ricevuto una risposta in merito al contributo e per ora sembra più opportuno mantenerlo nell\'ambito del progetto FreeCAD e che ci permettono di consentire agli utenti di fare dei test senza la necessità di lavorare con le versioni di sviluppo di Coin3D. Vorrei raggiungere questo obiettivo con la 0.14 considerando che aumentare l\'accessibilità di FreeCAD per gli utenti non inglesi è una grande priorità.

## Organizzazione

-   Fornire una funzionalità base di gestione di stringhe UTF che sia indipendente dalle principali biblioteche, tranne STL.

-   Implementare i campi di Coin3D e i nodi di testo 3D per la gestione della memorizzazione dei nuovi dati UTF.

-   Migrazione dei moduli per utilizzare i nuovi nodi testuali.

-   Test rigorosi

## Azioni successive 

-   Implementare la classe di gestione delle stringhe UTF Classe (WIP)

-   Gestione di font e glifi.

-   Implementare campi di testo e nodi di Coin3D da utilizzare nel progetto.

-   Eseguire la migrazione dei moduli che utilizzano SoText2 e SoText3 per utilizzare i nuovi nodi



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
