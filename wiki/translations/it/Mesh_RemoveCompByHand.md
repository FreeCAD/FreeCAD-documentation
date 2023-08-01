---
- GuiCommand:/it
   Name:Mesh_RemoveCompByHand
   Name/it:Rimuovi componente a mano‏‎
   MenuLocation:Mesh → Rimuovi componente a mano...
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Rimuovi componente](Mesh_RemoveComponents/it.md), [Arch Suddividere un oggetto mesh](Arch_SplitMesh/it.md)
---

# Mesh RemoveCompByHand/it

## Descrizione

Il comando **Rimuovi componenti a mano** rimuove i componenti dagli oggetti mesh.

## Utilizzo

1.  Un componente si riferisce a un gruppo completo di facce connesse. Di solito un oggetto mesh contiene un singolo componente. Ma, ad esempio, dopo aver utilizzato il comando [Unisci mesh](Mesh_Merge/it.md), un oggetto mesh può contenere più componenti.
2.  Il comando utilizza il colore rosso per contrassegnare le facce selezionate. Per vederle correttamente:
    -   La **Modalità di visualizzazione** degli oggetti mesh idealmente dovrebbe essere {{Value|Flat lines}}, ma dovrebbe almeno mostrare le facce. Se necessario, utilizzare il comando [Stile di disegno](Std_DrawStyle/it.md) per sovrascrivere questa proprietà.
    -   Il **Shape Color** degli oggetti mesh non dovrebbe essere rosso.
3.  Selezionare l\'opzione **Mesh → <img src="images/Mesh_RemoveCompByHand.svg" width=16px> Rimuovi componenti a mano...** dal menu.
4.  Il cursore si trasforma in un\'icona mano.
5.  Selezionare i componenti che si desidera eliminare nella [vista 3D](3D_view/it.md).
6.  Se necessario selezionare **Cancella facce selezionate** dal menu contestuale della vista 3D per deselezionare tutti i componenti.
7.  Selezionare **Elimina le facce selezionate** dal menu contestuale della vista 3D per eliminare i componenti selezionati.
8.  Selezionare **Esci dalla modalità di rimozione** dal menu contestuale della vista 3D per terminare il comando.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveCompByHand/it
