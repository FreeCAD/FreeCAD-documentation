---
 GuiCommand:
   Name: Sketcher Snap
   Name: Sketcher Aggancio
   Workbenches: Sketcher_Workbench/it
   Version: 0.21
   SeeAlso: Sketcher_Grid/it
---

# Sketcher Snap/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_Snap.svg  style="width:16px;"> [Aggancio](Sketcher_Snap/it.md) attiva/disattiva l\'aggancio (snap) in tutti gli schizzi. I singoli agganci e le impostazioni possono essere modificati nel relativo menu.

L\'aggancio funziona solo durante la creazione della geometria. Tenere presente che l\'aggancio è solo un aiuto per il disegno e non produce vincoli aggiuntivi.



## Utilizzo

1.  Premere il pulsante **<img src="images/Sketcher_Snap.svg" width=16px> [Attiva/disattiva aggancio](Sketcher_Snap/it.md)** per attivare/disattivare l\'aggancio.
2.  Facoltativamente fare clic sulla freccia giù a destra del pulsante per aprire il menu. Le impostazioni in questo menu possono essere modificate solo se lìaggancio è attivato:
    ![](images/Sketcher_Snap_Menu.png )
    -   Se la casella di controllo **Allinea alla griglia** è selezionata, il cursore si aggancerà alle linee e alle intersezioni della griglia. L\'aggancio avviene se la distanza del cursore da una linea della griglia è pari o inferiore al 20% della spaziatura della griglia. L\'aggancio funziona anche se la griglia è invisibile.

    -   Se la casella di controllo **Aggancia agli oggetti** è selezionata, il cursore si aggancerà ai bordi della geometria e ai punti medi di linee e archi.

    -   
        **Angolo di aggancio**
        
        specifica l\'angolo per l\'aggancio angolare. L\'aggancio avverrà a multipli di questo valore a partire dalla direzione dell\'asse X positivo dello schizzo. Il tasto **Ctrl** deve essere tenuto premuto per questo aggancio. L\'aggancio angolare funziona solo quando si crea una determinata geometria.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Snap/it
