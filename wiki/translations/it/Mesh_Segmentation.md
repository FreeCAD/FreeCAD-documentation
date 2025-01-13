---
 GuiCommand:
   Name: Mesh_Segmentation
   Name/it: Crea segmenti di mesh
   MenuLocation: Mesh , Crea segmenti di mesh...
   Workbenches: Mesh_Workbench/it
   SeeAlso: Mesh_SegmentationBestFit/it
---

# Mesh Segmentation/it



## Descrizione

Il comando **Crea segmenti di mesh** crea segmenti di mesh separati per i tipi di superficie specificati di un oggetto mesh.



## Utilizzo

1.  Selezionare un singolo oggetto mesh.
2.  Ci sono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Mesh_Segmentation.svg" width=16px> [Crea segmenti di mesh...](Mesh_Segmentation/it.md)**.
    -   Selezionare dal menu l\'opzione **Mesh → <img src="images/Mesh_Segmentation.svg" width=16px> Crea segmenti di mesh...**.
3.  Si apre il pannello **Segmentazione della mesh**.
4.  Facoltativamente selezionare l\'opzione **Levigatura della mesh** e specificare un valore per la raccordatura della mesh. Più alto è il valore più liscia si presume che sia la maglia. Specificare {{Value|0}} ha lo stesso effetto di deselezionare questa opzione. Non selezionare questa opzione se si desidera creare segmenti planari.
5.  Selezionare il tipo di superficie per cui si desidera creare i segmenti della mesh. È possibile selezionare più di un tipo, ma questo può portare a risultati più approssimativi. I tipi di superficie disponibili sono:
    -   
        **Plane**
        

    -   
        **Cylinder**
        

    -   
        **Sphere**
        

    -   
        **Freeform**
        
6.  Specificare le impostazioni richieste. Assicurarsi che il valore di **Tolerance** non sia troppo basso, e che il numero **Minimum number of faces** non sia troppo elevato.
7.  Premere il pulsante **OK**.
8.  Il comando creerà un [gruppo](Std_Group/it.md) contenente oggetti mesh separati, ciascuno un segmento dell\'oggetto mesh originale.
9.  Se il gruppo creato è vuoto provare ad usare nuovamente il comando dopo aver modificato le impostazioni.



## Note

-   La versione attuale del comando presenta problemi nell\'identificazione delle facce ai bordi dei tipi di superficie.
-   In alcuni casi il comando [Adatta i segmenti](Mesh_SegmentationBestFit/it.md) produrrà risultati migliori.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Segmentation/it
