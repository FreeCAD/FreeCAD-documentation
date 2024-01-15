---
 TutorialInfo:t
   Topic:  Product design
   Level:  Base
   Time: 30 minuti
   Author: r-frank e vocx
   FCVersion: 0.17 o superiore
   Files: https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true Draft_Shapestring_Text
---

# Draft ShapeString tutorial/it







## Introduzione

Questo tutorial è stato originariamente scritto da Roland Frank (†2017, r-frank) ed è stato riscritto e ri-illustrato da vocx.

Questo tutorial descrive un metodo per creare testo 3D e utilizzarlo con oggetti solidi in <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md). Si seguano le seguenti indicazioni

-   inserire il testo da tracciare con lo strumento **<img src="images/Draft_ShapeString.svg" width=16px> [Forma da testo](Draft_ShapeString/it.md)**,
-   estruderlo in modo che diventi un solido 3D con **[<img src=images/Part_Extrude.svg style="width:16px"> [Estrudi di Part](Part_Extrude/it.md)**,
-   posizionarlo nello spazio 3D utilizzando [Placement](Placement/it.md) e **[<img src=images/Draft_Move.svg style="width:16px"> [Sposta di Draft](Draft_Move/it.md)** (utilizzare uno schizzo come geometria ausiliaria) e
-   incidere il testo applicando in Part una **[<img src=images/Part_Cut.svg style="width:16px"> [Sottrazione booleana](Part_Cut/it.md)**.

Per utilizzare ShapeString all\'interno di <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md), il processo è essenzialmente lo stesso dell\'ambiente Part, ma ShapeString viene posizionato all\'interno del [Corpo di PartDesign](PartDesign_Body/it.md) per estruderlo. Andare alla fine di questo tutorial per ulteriori informazioni.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Aspetto finale del testo inciso.*

Per disegnare una linea ausiliaria viene utilizzato l\'ambiente [Sketcher](Sketcher_Workbench/it.md). Maggiori informazioni sugli strumenti di questo workbench sono disponibili in

-   [Tutorial base di Sketcher](Basic_Sketcher_Tutorial/it.md)
-   [Manuale di riferimento per Sketcher](Sketcher_reference/it.md)



## Impostazione

1\. Aprire FreeCAD, creare un nuovo documento vuoto con **File → [<img src=images/Std_New.svg style="width:16px"> [Nuovo](Std_New/it.md)** e passare a [Part](Part_Workbench/it.md).

:   1.1. Premere il pulsante **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [Isometrica](Std_ViewIsometric/it.md)** o premere **0** sul tastierino numerico della tastiera per modificare la visualizzazione in isometrica per visualizzare meglio i solidi 3D.
:   1.2. Premere il pulsante **[<img src=images/Std_ViewFitAll.svg style="width:16px"> [Visualizza tutto](Std_ViewFitAll/it.md)** ogni volta che si aggiungono oggetti per eseguire la panoramica e lo zoom della [Vista 3D](3D_view/it.md) in modo che tutti gli elementi siano visibili nella vista.
:   1.3. Tenere premuto **Ctrl** mentre si clicca per selezionare più elementi. Se si è sbagliato a selezionare qualcosa o si desidera deselezionare tutto, semplicemente fare clic sullo spazio vuoto nella [Vista 3D](3D_view/it.md).



## Creare la forma di base 

2\. Inserire una primitva cubo cliccando su **<img src="images/Part_Box.svg" width=16px> [Cubo](Part_Box/it.md)**.

:   2.1. Selezionare `Cubo` nella [vista ad albero](Tree_view/it.md).
:   2.2. Modificare le dimensioni nella scheda **Dati** dell\'[editor delle proprietà](Property_editor/it.md).
:   2.3. Cambiare **Width** in `31 mm`.

3\. Creare uno smusso.

:   3.1. Selezionare il bordo superiore (`Edge6`) sulla faccia anteriore del `Cubo` nella [vista 3D](3D_view/it.md).
:   3.2. Cliccare **<img src="images/Part_Chamfer.svg" width=16px> [Smussa](Part_Chamfer/it.md)**.
:   3.3. Nel [pannello](Task_panel/it.md) **Smussa spigoli** andare su **Selezione**, scegliere **Seleziona spigoli**. Come **Modalità smusso** scegliere `Uguale distanza`, quindi impostare **Lunghezza** su `5 mm`.
:   3.4. Premere **OK**. Questo creerà un oggetto `Chamfer`.
:   3.5. Nella [vista ad albero](Tree_view/it.md), selezionare `Chamfer` e nella scheda **Vista** modificare il valore di **Line Width** in `2.0`.

![](images/01_T04_Part_Cube_base_long.png ) 
*Oggetto di base creato da un cubo e da un'operazione di smusso.*



## Inserire il testo con lo strumento ShapeString di Draft 

4\. Passare a [Draft](Draft_Workbench/it.md).

:   4.1. Assicurarsi che non sia selezionato nulla nella [vista ad albero](Tree_view/it.md).
:   4.2. Stabilire il piano di lavoro su XY (Dall\'alto) facendo clic su **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Seleziona piano](Draft_SelectPlane/it.md)** e cliccando **[<img src=images/View-top.svg style="width:16px"> [Dall'alto (XY)](Std_ViewTop/it.md)**.

5\. Inserire il testo \"FreeCAD\".

:   5.1. Fare clic su **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Forma da testo](Draft_ShapeString/it.md)**.
:   5.2. Impostare **X** in `0 mm`.
:   5.3. Impostare **Y** in `0 mm`.
:   5.4. Impostare **Z** in `0 mm`.
:   5.5. Oppure cliccare **Reimposta punto**.
:   5.6. Scrivere in **Stringa** `FreeCAD`; cambiare **Altezza** in `5 mm`.
:   5.7. Assicurarsi che **Font file** punti ad un carattere valido, ad esempio `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`. Premere i puntini di sospensione **...** per aprire la finestra di dialogo del sistema operativo e trovare un font di carattere.

    :   
        **Nota:**
        
        per ulteriori dettagli sull\'utilizzo dei caratteri fare riferimento alla sezione [Note in Forma da testo](Draft_ShapeString/it#Note.md).
:   5.8. Cliccare **OK**. Questo creerà un oggetto `ShapeString`.
:   5.9. Ricalcolare il documento cliccando **[<img src=images/Std_Refresh.svg style="width:16px"> [Aggiorna](Std_Refresh/it.md)**.
:   5.10. Nella [vista ad albero](Tree_view/it.md), selezionare `ShapeString`, nella scheda **Vista** modificare il valore di **Line Width** in `2.0`.
:   5.11. Nella [vista ad albero](Tree_view/it.md), selezionare `Chamfer`, nella scheda **Vista** cambiare il valore di **Visibility** in `false`, oppure premere **Spazio** sulla tastiera. Questo nasconderà l\'oggetto, così si potrà vedere meglio la `ShapeString`.
:   5.12. Per vedere la ShapeString dall\'alto, cambiare la vista cliccando **[<img src=images/View-top.svg style="width:16px"> [Dall'alto](Std_ViewTop/it.md)** o premere **2** sulla tastiera.
:   5.13. Per ripristinare la vista isometrica, cliccare **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [Isometrica](Std_ViewIsometric/it.md)** o premere **0** sulla tastiera.

![](images/02_T04_Part_ShapeString.png ) 
*Testo creato come ShapeString, ovvero come raccolta di linee su un piano.*



## Creare il testo solido 3D 

6\. Tornare in [Part](Part_Workbench.md).

:   6.1. Nella [vista ad albero](Tree_view/it.md), selezionare `ShapeString`, quindi cliccare **[<img src=images/Part_Extrude.svg style="width:16px"> [Estrudi](Part_Extrude/it.md)**.
:   6.2. Nel [panelllo](Task_panel/it.md) **Estrudi** andare su **Direzione**, scegliere **Lungo la normale**; in **Lunghezza**, impostare **Nello stesso verso** a `1 mm`; selezionare anche l\'opzione **Crea solido**.
:   6.3. Cliccare **OK**. Questo creerà un oggetto `Extrude`.
:   6.4. Nella [vista ad albero](Tree_view/it.md), selezionare `Extrude` e nella scheda **Vista** cambiare il valore di **Line Width** in `2.0`.

![](images/03_T04_Part_ShapeString_Extrude.png ) 
*Testo creato come ShapeString e trasformato in un solido mediante estrusione.*



## Inserire lo schizzo ausiliario per il posizionamento 

Ora si disegnerà un semplice schizzo che verrà utilizzato come geometria ausiliaria per posizionare l\'estrusione ShapeString.

7\. Nella [vista ad albero](Tree_view/it.md), selezionare `Extrude` e premere **Spazio** sulla tastiera per renderlo invisibile.

8\. Passare a [Sketcher](Sketcher_Workbench/it.md).

9\. Nella [vista ad albero](Tree_view/it.md), selezionare `Chamfer` e premere **Spazio** sulla tastiera per renderlo visibile.

:   9.1. Scegliere la faccia inclinata creata dall\'operazione di smusso (`Face3`).
:   9.2. Fare clic sul pulsante **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Crea uno schizzo](Sketcher_NewSketch/it.md)**. Nella finestra di dialogo **Collegamento dello schizzo**, selezionare `Piano della faccia` e cliccare **OK**.
:   9.3. La vista dovrebbe regolarsi automaticamente in modo che la fotocamera sia parallela al volto selezionato.
:   9.4. Disegnare una linea orizzontale in una posizione generale sulla parte superiore della faccia. La lunghezza non è importante; interessa solo la sua posizione.
:   9.5. Vincolare il punto inizale sinistro in modo che sia ad una distanza di `2,5 mm` dall\'asse X locale e dall\'asse Y locale, utilizzando **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) ** e **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md)**.
:   9.6. Poiché lo schizzo è solo un oggetto ausiliario, non è necessario che sia completamente vincolato. Si può farlo se si vuole, assegnando una distanza fissa, ad esempio, `20 mm`, sempre con **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md)** .
:   9.7. Chiudere lo schizzo.

<img alt="" src=images/04_T04_Part_ShapeString_support_sketch.png  style="width:500px;"> 
*Linea creata in sketcher con i vincoli.*

<img alt="" src=images/05_T04_Part_ShapeString_support_sketch_3D.png  style="width:500px;"> 
*Linea di schizzo creata sopra la faccia solida, da utilizzare come guida di riferimento per il posizionamento del testo estruso.*



## Posizionare il testo 3D nello spazio 3D 

10\. Nella [vista ad albero](Tree_view/it.md), selezionare `Extrude` e premere **Spazio** sulla tastiera per renderlo visibile.

11\. Con `Extrude` ancora selezionato, nella scheda **Dati** dell\'[editor delle proprietà](property_editor/it.md), fare clic sul campo valore di **Placement** in modo che il pulsante con i puntini di sospensione {{ Button\|\...}} appaia sulla destra e quindi fare clic su quel pulsante.

:   11.1. Selezionare l\'opzione **Applica le modifiche incrementali**.
:   11.2. Impostare in **Rotazione** `Asse di rotazione con angolo` l\'**Asse** `Z` (impostando i valori `X`, `Y` e `Z` delle caselle di input dell\'asse su {{ incode\|0}}, `0` e `1` rispettivamente, `Z` è la terza casella di input) e per **Angolo** `90 deg`, quindi fare clic su **Applica**. Così si applicherà una rotazione attorno all\'asse Z e si ripristinerà il campo **Angolo** a zero.
:   11.3. Impostare in **Rotazione** `Asse di rotazione con angolo` l\'**Asse** `Y` (impostando i valori `X`, `Y` e `Z` delle caselle di input dell\'asse su {{ incode\|0}}, `1` e `0` rispettivamente) e per **Angolo** `45 gradi`, quindi fare clic su **Appica **. In questo modo si applicherà una rotazione attorno all\'asse Y e si ripristinerà il campo **Angolo** a zero.
:   11.4. Fare clic su **OK** per chiudere la finestra di dialogo.

12\. Passare nuovamente a [Draft](Draft_Workbench/it.md).

:   12.1. Passare allo stile di disegno \"Reticolo\" con **Visualizza → [Stile di disegno](Std_DrawStyle/it.md) → [<img src=images/DrawStyleWireFrame.svg style="width:16px"> Reticolo**, oppure cliccare **[<img src=images/DrawStyleWireFrame.svg style="width:16px"> [Reticolo](Std_DrawStyle/it.md)** nella barra degli strumenti della vista. Ciò consentirà di vedere gli oggetti dietro altri oggetti.
:   12.2. Assicurarsi che il metodo [Snap](Draft_Snap/it.md) \"Snap punto finale\" sia attivo. Questo può essere attivato dal menu **Drafting → Snap → [<img src=images/Draft_Snap_Lock.svg style="width:16px">[Snap blocca](Draft_Snap_Lock/it.md)**, e poi ** → [<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Snap punto finale](Draft_Snap_Endpoint/it.md)**, o cliccando **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Snap blocca](Draft_Snap_Lock/.md)** e poi **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Snap Punto finale](Draft_Snap_Endpoint/it.md)** nella barra degli strumenti di Snap.

13\. Nella [vista ad albero](Tree_view.md), selezionare `Extrude`.

:   13.1. Cliccare su **[<img src=images/Draft_Move.svg style="width:16px"> [Sposta](Draft_Move/it.md)**.
:   13.2. Nella [Vista 3D](3D_view/it.md) fare clic sul punto dell\'angolo in alto a sinistra dell\'oggetto `Extrude` (1), quindi fare clic sul punto più a sinistra nella linea disegnata con lo sketcher (2).
:   13.3. Se **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Snap Punto Finale](Draft_Snap_Endpoint/it.md)** è attivo, non appena si sposta il ​​puntatore vicino a un vertice, si dovrebbe notare che si attacca esattamente ad esso.
:   
    **Nota:**se si incontrano problemi con lo snap ai vertici, assicurarsi che solo il metodo **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Snap Punto finale](Draft_Snap_Endpoint/it.md)** sia abilitato. Avere più metodi di snap attivi contemporaneamente può rendere difficile la selezione della funzione giusta.
:   13.4. Il testo estruso dovrebbe ora trovarsi all\'interno del corpo dell\'oggetto `Chamfer`.

![](images/06_T04_Part_ShapeString_move.svg ) 
*La ShapeString estrusa deve essere spostata nella posizione della linea di schizzo che si trova sulla faccia del corpo di base.*

![](images/07_T04_Part_ShapesString_Extrude_in_place.png ) 
*ShapeString estruso posizionato sul `Chamfer*.`



## Creare il testo inciso 

14\. Tornare a [Part](Part_Workbench/it.md).

:   14.1. Passare allo stile di disegno \"Come è\" con **Visualizza → [Stile di disegno](Std_DrawStyle/it.md) → [<img src=images/DrawStyleAsIs.svg style="width:16px"> Come è**, oppure premere il **[16px](File_:DrawStyleAsIs.svg.md) [Come è](Std_DrawStyle/it.md)** nella barra degli strumenti della vista. Questo mostrerà tutti gli oggetti con l\'ombreggiatura e il colore normali.
:   14.2. Nella [vista ad albero](Tree_view/it.md), selezionare `Sketch` e premere **Spazio** sulla tastiera per renderlo invisibile.

15\. Nella [vista ad albero](Tree_view/it.md) selezionare prima `Chamfer` e poi `Extrude`.

:   15.1. Quindi premere **[<img src=images/Part_Cut.svg style="width:16px"> [Taglio](Part_Cut/it.md)**. Verrà creato un oggetto `Cut`. Questo è l\'oggetto finale.
:   
    **Nota:**l\'ordine in cui si selezionano gli oggetti è importante per l\'operazione di taglio. L\'oggetto di base viene selezionato per primo e l\'oggetto da sottrarre arriva alla fine.
:   15.2. Nella [vista ad albero](Tree_view/it.md), selezionare `Cut` e nella scheda **Vista** modificare il valore di **Line Width** in `2.0`.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Modello finale di un cubo raccordato, con testo scavato creato da operazioni ShapeString, Estrusione e Taglio booleano.*



## Incisione di testo 3D con l\'ambiente PartDesign 

Un processo simile a quello descritto sopra può essere eseguito con [PartDesign](PartDesign_Workbench/it.md).

1.  Prima creare il **[<img src=images/Draft_ShapeString.svg style="width:16px"> [ShapeString](Draft_ShapeString/it.md)**.
2.  Creare un **[<img src=images/PartDesign_Body_Tree.svg style="width:16px"> [Corpo](PartDesign_Body/it.md)**, renderlo attivo e inserire un solido di base aggiungendo primitive o utilizzando uno schizzo ed estrudendolo con **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Estrusione](PartDesign_Pad/it.md)**.
3.  Spostare l\'oggetto `ShapeString` nel corpo attivo.
4.  Attaccare l\'oggetto `ShapeString` a una delle facce del solido o a un **[<img src=images/PartDesign_Plane.svg style="width:16px"> [Piano](PartDesign_Plane/it.md)**, utilizzando **[<img src=images/Part_EditAttachment.svg style="width:16px"> [Associazione](Part_EditAttachment/it.md)**.
5.  Ora creare una **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Estrusione](PartDesign_Pad/it.md)** o una **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [Tasca](PartDesign_Pocket/it.md)** da `ShapeString`, per produrre rispettivamente una [feature](PartDesign_Feature/it.md) additiva o sottrattiva del corpo base.

Vedere il thread del forum, [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623).



## Note

-   Per creare un testo curvo si può utilizzare la <img alt="" src=images/FCCircularTextButtom.png  style="width:32px;"> [Macro FCCircularText](Macro_FCCircularText/it.md).
-   Per importare testo da un file SVG guardare il tutorial [Import text and geometry from Inkscape](Import_text_and_geometry_from_Inkscape/it.md).


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Draft](Draft_Workbench.md) > Draft ShapeString tutorial/it
