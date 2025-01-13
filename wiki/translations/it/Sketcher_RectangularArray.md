---
 GuiCommand:
   Name: Sketcher RectangularArray
   Name/it: Serie rettangolare
   MenuLocation: Schizzo , Strumenti , Serie rettangolare
   Workbenches: Sketcher_Workbench/it
   Shortcut: **Z** **A**
   Version: 0.16
---

# Sketcher RectangularArray/it



## Descrizione

Il comando <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:16px;"> [Serie rettangolare](Sketcher_RectangularArray/it.md) crea una serie con gli elementi dello schizzo selezionati.



## Utilizzo

1.  Selezionare gli elementi dello schizzo nella [vista combinata](Task_panel/it.md) o nella [Vista 3D](3D_view/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/Sketcher_RectangularArray.svg style="width:16px"> [Serie rettangolare](Sketcher_RectangularArray/it.md)**.
    -   Selezionare dal menu la voce **Schizzo → Strumenti → [<img src=images/Sketcher_RectangularArray.svg style="width:16px"> Serie rettangolare**.
3.  Specificare le opzioni per la serie nella finestra di dialogo che si apre.
4.  Premere il pulsante **OK**.
5.  Spostare il mouse nella [Vista 3D](3D_view/it.md) verso il punto di riferimento desiderato.Tenendo premuto **Ctrl**, l\'angolo rispetto al punto di riferimento può essere fissato in passi di 5°. {{Version/it|0.20}}
6.  Fare clic con il pulsante sinistro del mouse nella vista 3D per creare l\'array.
7.  Per impostare le distanze tra gli elementi dell\'array, modificare i vincoli dimensionali dell\'array.



## Opzioni

![](images/Sketcher_RectangularArray_Options.jpg )

**Serie rettangolare** ha le seguenti opzioni:

-   **Colonne**: il numero di colonne per la serie.
-   **Righe**: il numero di righe per la serie.
-   **Spaziatura verticale/orizzontale uguale**: Se la distanza verticale tra gli elementi dell\'array deve essere uguale alla distanza orizzontale.
-   **Vincola la distribuzione degli elementi**: Quando questa opzione è selezionata, la distanza tra gli elementi dell\'array sarà vincolata.Se ad esempio si sa solo che c\'è bisogno di un array di 23 x 15 mm, usare questa opzione per poter successivamente modificare questi vincoli alle dimensioni necessarie.
-   **Clona**: Se selezionato, i vincoli dimensionali vengono sostituiti da vincoli geometrici nelle copie, in modo che qualsiasi modifica nell\'elemento originale si rifletta anche nelle copie.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RectangularArray/it
