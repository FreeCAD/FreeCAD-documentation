---
 GuiCommand:
   Name: Std ToggleNavigation
   Name/it: Attiva/disattiva la modalità modifica
   MenuLocation: Visualizza , Attiva/disattiva la modalità modifica
   Workbenches: Tutti
   Shortcut: **Esc**
---

# Std ToggleNavigation/it



## Descrizione

Il comando **Attiva/disattiva la modalità modifica** è destinato a determinate operazioni di ispezione ed a determinate operazioni interattive di modifica della mesh. Queste operazioni sono abbastanza \"onerose\" e quindi si basano su una modalità di modifica durante la quale la maggior parte delle opzioni di navigazione sono disabilitate. Con questo comando è possibile passare temporaneamente dalla modalità di modifica alla modalità di navigazione e, dopo aver modificato la [Vista 3D](3D_view/it.md), tornare alla modalità di modifica.

Non confondere questo comando con il comando [Modalità modifica](Std_Edit/it.md).



## Utilizzo

*Un esempio per dimostrare il comando:*

1.  Passare all\'ambiente <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh](Mesh_Workbench/it.md).
2.  Selezionare l\'opzione **Mesh → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Solido regolare...** dal menu.
3.  Si apre la finestra di dialogo Solido regolare.
4.  Scegliere **Ellissoide** dall\'elenco a discesa.
5.  Premere il pulsante **Crea**.
6.  Premere il pulsante **Chiudi** per chiudere la finestra di dialogo.
7.  Selezionare l\'oggetto mesh.
8.  Premere il pulsante **<img src="images/Mesh_PolyCut.svg" width=16px> [Taglia la mesh](Mesh_PolyCut/it.md)**.
9.  Scegliere i punti nella vista 3D per definire un poligono che si sovrapponga a metà della mesh.
10. Fare clic con il tasto destro e scegli **Interno** dal menu contestuale.
11. Il risultato è una mesh aperta con un contorno.
12. Assicurarsi che la mesh sia ancora selezionata.
13. Selezionare l\'opzione **Meshes → <img src="images/Mesh_AddFacet.svg" width=16px> Aggiungi triangolo** dal menu per invocare il comando [Aggiungi triangolo](Mesh_AddFacet/it.md).
14. Se si passa con il mouse su un punto di confine, apparirà un indicatore giallo e un clic sinistro lo selezionerà.
15. Facoltativamente, selezionare altri due punti e aggiungere un triangolo alla mesh.
16. Ora ci si trova in modalità di modifica ed è impossibile ruotare o eseguire una panoramica della vista 3D, sebbene lo zoom funzioni ancora.
17. Invocare il comando **Attiva/disattiva la modalità modifica** per passare alla modalità di navigazione:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_ToggleNavigation.svg" width=16px> Attiva/disattiva navigazione/Modifica** dal menu.
    -   Oppure usare la scorciatoia da tastiera: **Esc**.
18. Ora si può ruotare e spostare la vista 3D, ma non si può selezionare i punti per aggiungere triangoli.
19. Invocare il comando **Attiva/disattiva la modalità modifica** per tornare alla modalità di modifica:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_ToggleNavigation.svg" width=16px> Attiva/disattiva navigazione/Modifica** dal menu.
    -   Oppure usa la scorciatoia da tastiera: **Esc**.
20. Si può nuovamente selezionare punti ed aggiungere triangoli.
21. Fare clic con il pulsante destro del mouse nella vista 3D e scegliere **Termina** dal menu contestuale per terminare il comando [Aggiungi triangolo](Mesh_AddFacet/it.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleNavigation/it
