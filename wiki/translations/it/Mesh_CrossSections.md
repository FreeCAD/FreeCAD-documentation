---
- GuiCommand:
   Name: Mesh_CrossSections
   Name/it: Sezioni
   MenuLocation: Mesh - Taglio - Sezioni...
   Workbenches: [Mesh](Mesh_Workbench/it.md)
   Version: 0.19
   SeeAlso: [Sezione da mesh e piano](Mesh_SectionByPlane/it.md)
---

# Mesh CrossSections/it



## Descrizione

Il comando **Sezioni** crea più sezioni trasversali tra gli oggetti mesh. Le sezioni trasversali vengono prese parallelamente a uno dei principali piani globali (XY, XZ o YZ). Per ogni serie di sezioni trasversali viene creata una singola [Part Feature](Part_Feature/it.md).



## Utilizzo

1.  Selezionare uno o più oggetti mesh.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Mesh_CrossSections.svg" width=16px> [Sezioni...](Mesh_CrossSections/it.md)**.
    -   Selezionare l\'opzione **Mesh → Taglio → <img src="images/Mesh_CrossSections.svg" width=16px> Sezioni...** dal menu.
3.  Si apre il pannello delle azioni **Sezioni**.
4.  I piani che verranno utilizzati per creare le sezioni trasversali sono indicati nella [vista 3D](3D_view/it.md) e verranno aggiornati in base agli input del pannello delle azioni.
5.  Selezionare il **Piano guida**:
    -   
        **XY**
        

    -   
        **XZ**
        

    -   
        **YZ**
        
6.  Specificare la **Posizione** del piano guida dall\'origine. La posizione predefinita si basa sul centro del cuboide contenitore degli oggetti mesh selezionati. La scelta di un diverso **Piano guida** o la selezione della casella di controllo **Sezioni** reimposta la **Posizione** a questo valore predefinito.
7.  Se necessario, selezionare la casella di controllo **Sezioni** per creare più sezioni trasversali:
    -   
        **Su entrambi i lati**
        
        : se selezionata, le sezioni trasversali vengono create su entrambi i lati del piano di guida.

    -   
        **Numero di sezioni**
        
        : il numero di sezioni trasversali.

    -   
        **Distanza**
        
        : la distanza tra le sezioni trasversali. Il valore predefinito si basa sulle dimensioni del riquadro di delimitazione, sull\'opzione **Su entrambi i lati** e sul valore di **Numero di sezioni**. La modifica del valore di **Numero di sezioni** reimposta la **Distanza** a questo valore predefinito. La modifica dell\'opzione **Su entrambi i lati** ricalcola la **Distanza** ({{value|*2.0}} o {{value|*0.5}}). Notare che la casella di immissione potrebbe essere disattivata, ma il valore può essere effettivamente modificato.

    -   Facoltativamente, selezionare la casella di controllo **Collega bordi se la distanza è inferiore a** e specificare un valore.
8.  Premere il pulsante **Applica** per creare l\'insieme di sezioni trasversali.
9.  Facoltativamente, modificare una o più impostazioni e creare set aggiuntivi di sezioni trasversali.
10. Premere il pulsante **OK** o il pulsante **Annulla** per chiudere il pannello delle attività e terminare il comando.



## Proprietà

Vedere: [Funzioni Part](Part_Feature/it.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh CrossSections/it
