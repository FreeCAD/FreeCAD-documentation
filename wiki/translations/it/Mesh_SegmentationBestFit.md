---
 GuiCommand:
   Name: Mesh_SegmentationBestFit
   Name/it: Adatta i segmenti
   MenuLocation: Mesh , Adatta i segmenti...
   Workbenches: Mesh_Workbench/it
   SeeAlso: Mesh_Segmentation/it
---

# Mesh SegmentationBestFit/it



## Descrizione

Il comando **Adatta i segmenti** crea segmenti di mesh separati per i tipi di superficie specificati di un oggetto mesh. Il comando può anche identificare i loro parametri che possono essere utili quando si riprogetta un oggetto mesh.



## Utilizzo

1.  Se si intende identificare i parametri di un tipo di superficie, tenere presente che il comando utilizza il colore rosso per contrassegnare le facce selezionate per questa opzione. Per vederli correttamente:
    -   La proprietà **Display Mode** dell\'oggetto mesh idealmente dovrebbe essere {{Value|Flat lines}}, ma dovrebbe mostrare almeno le facce. Se necessario, utilizzare il comando [Stile di disegno](Std_DrawStyle.md) per sovrascrivere questa proprietà.
    -   La proprietà **Shape Color** dell\'oggetto mesh non deve essere rosso.
2.  Selezionare un singolo oggetto mesh.
3.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Mesh_SegmentationBestFit.svg" width=16px> [Adatta i segmenti...](Mesh_SegmentationBestFit/it.md)**.
    -   Selezionare l\'opzione **Mesh → <img src="images/Mesh_SegmentationBestFit.svg" width=16px> Adatta i segmenti...** dal menu.
4.  Si apre il pannello **Segmentazione della mesh**.
5.  Facoltativamente, premere uno dei pulsanti **Parametri...** per identificare i parametri di una superficie:
    -   Si apre la finestra di dialogo **Adattamento della superficie**.
    -   Selezionare una o più facce appartenenti alla superficie:
        -   Premere il pulsante **Regione** e mentre si tiene premuto il pulsante sinistro del mouse disegnare una regione con una spline chiusa nella [vista 3D](3D_view/it.md). Verranno selezionate le facce che (parzialmente) rientrano nella regione.
        -   Premere il pulsante **Triangolo** per selezionare le singole facce.
        -   Facoltativamente, premere il pulsante **Pulisci** per cancellare la selezione.
    -   Premere il pulsante **Calcola** per calcolare i parametri.
    -   Premere il pulsante **OK** o **Annulla** per chiudere la finestra di dialogo.
6.  Selezionare il/i tipo/i di superficie per cui si desidera creare segmenti mesh:
    -   
        **PIano**
        

    -   
        **Cilindro**
        

    -   
        **Sfera**
        
7.  Specificare i valori di **Tolleranza**.
8.  Specificare i valori di **Numero minimo di facce**.
9.  Premere il pulsante **OK**.
10. Il comando creerà un [gruppo](Std_Group/it.md) contenente oggetti mesh separati, uno per ogni segmento dell\'oggetto mesh originale.
11. Se il gruppo creato è vuoto provare a utilizzare nuovamente il comando modificando le impostazioni.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SegmentationBestFit/it
