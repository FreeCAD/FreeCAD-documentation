---
 GuiCommand:
   Name: TechDraw ToggleFrame
   Name/it: TechDraw Attiva o disattiva la cornice
   MenuLocation: TechDraw , Viste TechDraw , Attiva o disattiva la vista cornici
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_View/it
---

# TechDraw ToggleFrame/it



## Descrizione

Lo strumento**TechDraw Attiva o disattiva la cornice**, attiva o disattiva la visualizzazione dei riquadri della Vista, delle etichette e dei vertici.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width:400px;"> 
*Vista della proiezione di un solido con cornici attive e disattivate*



## Utilizzo

1.  Se nel documento sono presenti più pagine di disegno: facoltativamente attivare la pagina desiderata selezionandola nella [Vista ad albero](Tree_view/it.md).
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Attiva o disattiva la vista delle cornici](TechDraw_ToggleFrame/it.md)**.
    -   Seleziona l\'opzione **TechDraw → Viste TechDraw → <img src="images/TechDraw_ToggleFrame.svg" width=16px> Attiva o disattiva la vista delle cornici** dal menu.
    -   Se una pagina viene visualizzata nell\'[Area di visualizzazione principale](Main_view_area/it.md): fare clic con il pulsante destro del mouse sulla finestra della pagina e selezionare l\'opzione **Alterna cornici** dal menu contestuale.
3.  Se nel documento sono presenti più pagine di disegno e non si ha ancora attivato una pagina, si apre la finestra di dialogo **Scelta pagina**:
    1.  Selezionare la pagina desiderata.
    2.  Premere il pulsante **OK**.
4.  Le cornici di visualizzazione attualmente visibili scompariranno. Appariranno i riquadri di visualizzazione attualmente invisibili.
5.  È possibile per Viste diverse di trovarsi in stati diversi di visualizzazione della cornice. Se ciò accade, richiamare questo strumento una o due volte per risincronizzare le Viste.



## Quadro generale 

La cornice tratteggiata della vista ed i punti sui vertici sono solo di riferimento, non fanno effettivamente parte del disegno, quindi non si vedranno una volta esportata la pagina come PDF o SVG.

Il flusso di lavoro suggerito consiste nell\'utilizzare **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Attiva o disattiva la vista delle cornici](TechDraw_ToggleFrame/it.md)** per disattivare il riquadro che circonda la vista ed anche i punti aggiuntivi. Con i punti attivi, utilizzare gli strumenti di quotatura per selezionare i bordi corretti da quotare, quindi disattivare la cornice (e i punti) per vedere il risultato finale. Non si è soddisfatti? Attivare nuovamente la cornice (e i punti), selezionare altri vertici e creare nuove quotature, quindi disattiva nuovamente la cornice.

È possibile regolare la dimensione dei punti nella [Scheda Preferenze/Scala di TechDraw](TechDraw_Preferences/it#Scala.md). Si consiglia di non impostare la dimensione a zero, ma quanto basta piccola o grande in modo da poterli selezionare.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per ora lo strumento non ha un\'interfaccia di programmazione.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ToggleFrame/it
