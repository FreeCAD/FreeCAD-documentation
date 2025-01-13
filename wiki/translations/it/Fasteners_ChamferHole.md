---
 GuiCommand:
   Name: Fasteners ChamferHole
   Name/it: Fasteners: Smusso per foro
   MenuLocation: Fasteners , Make countersunk
   Workbenches: Fasteners_Workbench/it
---

# Fasteners ChamferHole/it



## Descrizione

Il comando <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:24px;"> **Fasteners ChamferHole** smussa i fori per le viti a testa svasata.

![](images/Fasteners_ChamferHole_Example.png ) 
*Fori smussati per viti a testa svasata*



## Utilizzo

1.  Il comando può rilevare automaticamente i diametri delle viti. Affinché ciò funzioni, i fori devono avere il diametro corretto. Ad esempio, una vite M5 richiede un foro passante da 5 mm o un foro filettato da 4,2 mm. Il comando <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:16px;"> [Fasteners ScrewCalculator](Fasteners_ScrewCalculator/it.md) può essere utilizzato per determinare i diametri dei fori maschiati.
2.  Selezionare una parte con fori circolari.
3.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Fasteners_ChamferHole.svg" width=16px> [Make countersunk](Fasteners_ChamferHole/it.md)**.
    -   Selezionare l\'opzione **Fasteners → <img src="images/Fasteners_ChamferHole.svg" width=16px> Make countersunk** dal menu.
4.  Si apre il pannello delle attività **Chamfer holes for countersunk screws**.
5.  L\'elenco **Edges to chamfer** mostra tutti i bordi circolari della parte selezionata.
6.  Selezionare i bordi che si desidera smussare effettuando una delle seguenti operazioni:
    -   Fare clic su singoli bordi circolari o facce con bordi circolari nella [vista 3D](3D_view/it.md):
        -   Non è necessario tenere premuto il tasto **Ctrl**.
        -   Ogni bordo selezionato viene controllato nell\'elenco **Edges to chamfer**.
        -   Il diametro della vite per ciascun bordo viene rilevato automaticamente.
        -   I bordi non possono essere deselezionati nella [vista 3D](vista_3D/it.md).
    -   Selezionare o deselezionare i bordi selezionandoli o deselezionandoli nell\'elenco **Edges to chamfer**:
        -   In questo caso il diametro della vite non viene rilevato automaticamente.
7.  Facoltativamente, modificare il diametro della vite dei singoli bordi nell\'elenco **Edges to chamfer** facendo doppio clic sul campo **Diameter** e selezionando un nuovo valore dall\'elenco a discesa visualizzato.
8.  Facoltativamente, modificare il diametro della vite di tutti i bordi selezionati impostando un nuovo valore dall\'elenco a discesa **Diameter** sotto l\'elenco **Edges to chamfer**.
9.  Facoltativamente specificare un **Screw type**.
10. Premere il pulsante **OK**.
11. Viene creato un oggetto svasatura con un incavo smussato per ciascun bordo selezionato.
12. Facoltativamente, fissare le viti. Vedere l\' [Ambiente Fasteners](Fasteners_Workbench/it#Utilizzo.md).



## Note

-   Gli oggetti Countersunk sono parametrici. Un oggetto svasato esistente può essere modificato facendo doppio clic su di esso nella [Vista ad albero](Tree_view/it.md). Si aprirà il pannello delle attività **Chamfer holes for countersunk screws**. È possibile aggiungere o rimuovere bordi circolari e modificare i parametri dei bordi.




{{Fasteners_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > Fasteners ChamferHole/it
