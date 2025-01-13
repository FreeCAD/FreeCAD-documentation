---
 GuiCommand:
   Name: Mesh_Evaluation
   Name/it: Valuta e ripara la mesh
   MenuLocation: Mesh , Analizza , Valuta e ripara la mesh...
   Workbenches: Mesh_Workbench/it
---

# Mesh Evaluation/it



## Descrizione

Il comando **Valuta e ripara la mesh\...** valuta e ripara un oggetto mesh.

<img alt="" src=images/Mesh_Evaluation_dialog.png  style="width:300px;"> 
*La finestra di dialogo Valuta e ripara la mesh con l'opzione Folds on surface abilitata*



## Utilizzo

1.  Facoltativamente, seleziona un singolo oggetto mesh.
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Mesh_Evaluation.svg" width=16px> [Valuta e ripara la mesh...](Mesh_Evaluation.md)**.
    -   Selezionare l\'opzione **Meshes → Analizza → <img src="images/Mesh_Evaluation.svg" width=16px> Valuta e ripara la mesh...** dal menu.
3.  Si apre la finestra di dialogo **Valuta e ripara mesh**.
4.  Facoltativamente, premere il pulsante **Impostazioni...** per modificare le seguenti opzioni:
    -   
        **Verifica la presenza di punti non-manifold**
        

    -   
        **Verifica la presenza di pieghe sulla superficie**
        

    -   
        **Considera come degenerate solo le facce con area zero**
        
5.  Se non si ha ancora selezionato un oggetto mesh: selezionane uno dall\'elenco a discesa nella parte superiore della finestra di dialogo.
6.  La finestra di dialogo contiene le opzioni di verifica 7 o 8 (se l\'opzione **Pieghe sulla superficie** è abilitata).
7.  Non utilizzare le caselle di spunta, verranno attivate automaticamente se vengono rilevati errori.
8.  Premere uno qualsiasi dei pulsanti **Analizza** per avviare il relativo test.
9.  Oppure utilizza il pulsante **Analizza** dall\'opzione **Tutti i test insieme** per eseguire i test 7 e 8 insieme.
10. Gli errori verranno indicati nella finestra di dialogo e anche, con indicatori gialli e rossi, nella [Vista 3D](Vista_3D/it.md).
11. Facoltativamente, premere uno o più pulsanti **Ripara** per riparare gli errori rilevati.
12. Facoltativamente, premere il pulsante **Ripristina** per ripristinare tutti i risultati del test. Ciò ripristinerà la finestra di dialogo e rimuoverà gli indicatori colorati dalla vista 3D. Se si desidera ripetere lo stesso test o eseguire tutti i test insieme, non è necessario farlo.
13. Facoltativamente, selezionare un oggetto mesh diverso dall\'elenco a discesa per continuare ad analizzare e riparare.
14. Premere il pulsante **Chiudi** per chiudere la finestra di dialogo e terminare il comando.
15. Il pulsante **Aggiorna** non funziona correttamente in questo momento.



## Note

-   Riparare una mesh può comportare che gli elementi problematici vengono eliminati dalla mesh causando buchi. I buchi possono essere chiusi con i comandi [Mesh Riempi i buchi](Mesh_FillupHoles.md), [Mesh Chiudi il foro](Mesh_FillInteractiveHole.md) e [Mesh Aggiungi triangolo](Mesh_AddFacet.md).
-   Vedere [questo post nel forum](https://forum.freecadweb.org/viewtopic.php?f=3&p=533252#p533252) per una spiegazione della struttura dei dati mesh. Queste informazioni possono aiutare a capire perché una mesh presenta problemi.



## Preferenze

-   L\'impostazione **Check for non-manifold points** è memorizzata in: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Evaluation → CheckNonManifoldPoints**.
-   L\'impostazione **Enable check for folds on surface** è memorizzata in: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Evaluation → EnableFoldsCheck**.
-   L\'impostazione **Only consider zero area faces as degenerated** è memorizzata in: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Evaluation → StrictlyDegenerated**.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Evaluation/it
