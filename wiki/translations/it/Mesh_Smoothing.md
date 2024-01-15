---
 GuiCommand:
   Name: Mesh_Smoothing
   Name/it: Mesh Smoothing
   MenuLocation: Mesh , Leviga...
   Workbenches: Mesh_Workbench/it
---

# Mesh Smoothing/it



## Descrizione

Il comando **Leviga** smussa gli oggetti mesh cambiando la posizione dei loro vertici.

<img alt="" src=images/Meshes_Smooth.jpg  style="width:350px;"> 
*Il pannello delle azioni Leviga dopo aver scelto l'opzione Solo selezione*



## Utilizzo

1.  Se si prevede di levigare solo alcune aree, tenere presente che il comando utilizza il colore rosso per contrassegnare le facce selezionate per questa opzione. Per vederli correttamente:
    -   
        **Display Mode**
        
        degli oggetti mesh idealmente dovrebbe essere {{Value|Flat lines}}, e dovrebbe almeno mostrare le facce. Se necessario, utilizzare il comando [Stile di disegno](Std_DrawStyle/it.md) per sovrascrivere questa proprietà.

    -   
        **Shape Color**
        
        degli oggetti mesh non deve essere rosso.
2.  Selezionare uno o più oggetti mesh.
3.  Esistono diversi modi per richiamare il comando:
    -   Premi il pulsante **<img src="images/Mesh_Smoothing.svg" width=16px> [Leviga](Mesh_Smoothing/it.md)**.
    -   Selezionare l\'opzione **Meshe → <img src="images/Mesh_Smoothing.svg" width=16px> Leviga** dal menu.
4.  Si apre il pannello delle attività **Leviga**.
5.  Se si desidera smussare solo le aree selezionate: scegliere l\'opzione **Solo selezione**:
    -   Il pannello **Selezione** viene aggiunto al pannello delle attività.
    -   Specificare le opzioni della selezione:
        -   
            **Seleziona solo i triangoli visibili**
            

        -   
            **Seleziona solo i triangoli con le normali in direzione verso lo schermo**
            
    -   Premere il pulsante **Aggiungi** e mentre si tiene premuto il pulsante sinistro del mouse disegnare una regione, una spline chiusa, nella [Vista 3D](3D_view/it.md). Verranno selezionate le facce che corrispondono alle opzioni della selezione e che rientrano (parzialmente) all\'interno della selezione.
    -   Eventualmente, premere il pulsante **Clear** per cancellare la selezione.
6.  Seleziona il **Metodo** di levigatura:
    -   
        **Taubin**
        

    -   
        **Laplace**
        
7.  Specificare i **Parametri**:
    -   
        **Iterazioni**
        
        : maggiore è questo numero, più fluido sarà il risultato finale. Il valore ha anche un impatto sul tempo di elaborazione totale del comando. Evitare valori elevati se gli oggetti mesh hanno molti punti.

    -   
        **λ**
        
        : il valore deve essere compreso nell\'intervallo {{Value|0}} - {{Value|1}}.

    -   
        **μ**
        
        : il valore deve essere compreso nell\'intervallo {{Value|0}} - {{Value|1}}.
8.  Premere il pulsante **OK** per terminare il comando.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Smoothing/it
