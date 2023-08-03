# Mesh RemoveComponents/it
---
 GuiCommand:
   Name: Mesh_RemoveComponents
   Name/it: Rimuovi componenti‏‎
   MenuLocation: Mesh , Rimuovi componenti...
   Workbenches: Mesh Workbench/it
   SeeAlso: Mesh_RemoveCompByHand/it, Arch_SplitMesh/it---



## Descrizione

Il comando **Rimuovi componenti** rimuove le facce dagli oggetti mesh.

![](images/Meshes_RemoveComponents.jpg ) 
*Il pannello delle azioni Rimuovi componenti*



## Utilizzo

1.  Il comando utilizza il colore rosso per contrassegnare le facce selezionate. Per vederle correttamente:
    -   La **Modalità di visualizzazione** degli oggetti mesh idealmente dovrebbe essere {{Value|Flat lines}}, ma dovrebbe almeno mostrare le facce. Se necessario, utilizzare il comando [Stile di disegno](Std_DrawStyle/it.md) per sovrascrivere questa proprietà.
    -   Il **Shape Color** degli oggetti mesh non dovrebbe essere rosso.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Mesh_RemoveComponents.svg" width=16px> [Rimuovi componente...](Mesh_RemoveComponents/it.md)**.
    -   Selezionare l\'opzione **Mesh → <img src="images/Mesh_RemoveComponents.svg" width=16px> Rimuovi componente...** dal menu.
3.  Si apre il pannello delle azioni **Rimuovi componenti**.
4.  Utilizzare una o più delle opzioni **Seleziona** per selezionare le facce:
    -   Premere il pulsante **Regione** e tenendo premuto il pulsante sinistro del mouse disegnare una regione, una spline chiusa, nella [vista 3D](3D_view/it.md). Verranno selezionate le facce che corrispondono alle **Opzioni regione** e rientrano (parzialmente) nella regione.
    -   Premere il pulsante **Tutto** per selezionare tutte le facce.
    -   Premere il pulsante **Componenti** per selezionare tutti i componenti con un numero di facce inferiore a quello massimo specificato. Qui un componente si riferisce a un gruppo completo di facce collegate. Di solito un oggetto mesh contiene un singolo componente. Ma, ad esempio, dopo aver utilizzato il comando [Unisci mesh](Mesh_Merge/it.md), un oggetto mesh può contenere più componenti.
    -   Premere il pulsante **Seleziona triangolo** per selezionare una singola faccia nella vista 3D. Se l\'opzione **Seleziona intero componente** è selezionata, la selezione di una faccia causa la selezione dell\'intero componente a cui appartiene la faccia.
5.  Se necessario, utilizzare una o più delle opzioni **Deseleziona** per deselezionare le facce. Queste opzioni sono identiche alle opzioni **Seleziona**, tranne per il fatto che il numero di facce per il pulsante **Componenti** è il numero minimo.
6.  Se necessario, premere il pulsante **Inverti** per invertire la selezione.
7.  Premere il pulsante **Elimina** per eliminare le facce selezionate.
8.  Premere il pulsante **Chiudi** per chiudere il pannello delle azioni e terminare il comando.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveComponents/it
