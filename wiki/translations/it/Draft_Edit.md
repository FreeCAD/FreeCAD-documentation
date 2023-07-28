---
- GuiCommand:/it
   Name:Draft Edit
   Name/it:Modifica
   MenuLocation:Modifiche → Modifica
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**D** **E**
   SeeAlso:[Modalità modifica](Std_Edit/it.md)
---

# Draft Edit/it



## Descrizione

Il comando <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> **Modifica** mette gli oggetti selezionati in modalità Draft Modifica. In questa modalità le proprietà degli oggetti possono essere modificate graficamente. In genere i nodi possono essere spostati e in alcuni casi è possibile selezionare le opzioni del menu contestuale. Il comando può gestire la maggior parte degli oggetti Draft, ma anche alcuni altri oggetti. Vedi [Oggetti supportati](#Oggetti_supportati.md). Gli oggetti Draft supportati possono anche essere messi in modalità Draft Modifica con il comando [Modalità Modifica](Std_Edit/it.md).

![](images/Draft_Edit_example.png ) 
*4 oggetti in modalità Draft Modifica: Polilinea (rosso), Arco (nero), BSpline (verde) e BezCurve (magenta)*



## Utilizzo

Vedere anche: [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Opzionalmente selezionare uno o più oggetti. Si noti che sebbene più oggetti possano trovarsi in modalità Modifica, gli oggetti possono essere modificati solo uno alla volta.
2.  Esistono diversi modi per invocare il comando:
    -   Se non si ha ancora selezionato un oggetto: fare doppio clic su un oggetto nella [Vista ad albero](Tree_view/it.md). Funziona solo per gli oggetti Draft supportati.
    -   Premere il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**.
    -   Selezionare l\'opzione **Modifica → <img src="images/Draft_Edit.svg" width=16px> Modifica** dal menu.
    -   Usare la scorciatoia da tastiera: **D** poi **E**.
    -   Per un singolo oggetto: selezionare l\'opzione **Modifica** dal menu contestuale [Vista ad albero](Tree_view/it.md). Funziona solo per gli oggetti Draft supportati. {{Version/it|0.21}}
3.  Se non si ha ancora selezionato un oggetto: selezionare un oggetto nella [Vista 3D](3D_view/it.md).
4.  Gli oggetti selezionati vengono contrassegnati con nodi temporanei e si apre il [Pannello attività principale](#Main_task_panel/it.md). Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
5.  Facoltativamente, utilizzare un menu contestuale del nodo o del bordo. Questi menu contestuali sono disponibili solo per alcuni oggetti Draft. Vedi [Oggetti supportati](#Oggetti_supportati.md) per ulteriori informazioni.
    -   Effettuare una delle seguenti operazioni:
        -   Su tutti i sistemi operativi: tenere premuto **E** e fare clic sul nodo o sul bordo. Per utilizzare **E** potrebbe essere necessario fare clic nella [Vista 3D](3D_view/it.md) una volta per assicurarsi che abbia il focus.
        -   Su Windows: tenere premuto **Alt** e fare clic sul nodo o sul bordo.
        -   Su Linux: tenere premuto **Maiusc**+**Alt**, **Ctrl**+**Alt** o **Alt** e fare clic sul nodo o bordo.
        -   Su macOS: tenere premuto **Option** e fare clic sul nodo o sul bordo.
    -   Selezionare un\'opzione dal menu contestuale.
    -   Se l\'opzione selezionata richiede l\'inserimento di punti:
        -   Si apre il [Pannello attività modifica nodo](#Pannello_attività_modifica_nodo.md). Vediere [Opzioni](#Opzioni.md) per maggiori informazioni.
        -   Scegliere un punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
6.  Facoltativamente spostare un nodo:
    -   Fare clic sul nodo nella [Vista 3D](3D_view/it.md).
    -   Si apre il [Pannello attività modifica nodo](#Pannello_attività_modifica_nodo.md). Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
    -   Scegliere un punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
    -   Il risultato dipende dall\'oggetto e dal nodo selezionato.
7.  Premere **Esc** o il pulsante **Chiudi** (il pulsante nella parte superiore del pannello delle attività, senza l\'immagine) per terminare il comando.



## Opzioni

Le scorciatoie da tastiera a carattere singolo menzionate qui possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).



### Pannello attività principale 

-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



### Pannello attività modifica nodo 

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Invio** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando hai i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Per usare le coordinate polari inserire un valore per **Lunghezza** e un valore per **Angolo**, e premere **Enter** dopo ciascuno.
-   Selezionare la casella **Angolo** per vincolare il puntatore all\'angolo specificato.
-   Premere **G** o fai clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).



## Oggetti supportati 



### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Draft Linea](Draft_Line/it.md) e <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polilinea](Draft_Wire/it.md) 

-   Se il nodo iniziale o finale di una polilinea aperta viene spostato in modo che coincidano, la polilinea viene chiusa.
-   Menu contestuale del nodo: {{Value|Elimina punto}}. Devono rimanere almeno due punti.
-   Menu contestuale bordo: {{Value|Aggiungi punto}}, {{Value|Close/Apri polilinea}} ({{Version/it|0.21}}) e {{Value|Inverti polilinea}} ({{Version/it|0.20}}).



### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Draft Arco](Draft_Arc/it.md) e <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Draft Arco da tre punti](Draft_Arc_3Points/it.md) 

-   Menu contestuale del nodo centrale: {{Value|Sposta arco}}.
-   Avvia il menu contestuale del nodo: {{Value|Imposta primo angolo}}.
-   Menu contestuale del nodo finale: {{Value|Imposta ultimo angolo}}.
-   Menu contestuale del nodo centrale: {{Value|Imposta raggio}}.
-   Menu contestuale bordo: {{Value|Inverti arco}}.



### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Draft Cerchio](Draft_Circle/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Draft Ellisse](Draft_Ellipse/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rettangolo](Draft_Rectangle/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Draft Poligono](Draft_Polygon/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Draft BSpline](Draft_BSpline/it.md) 

-   Se il nodo iniziale o finale di una spline aperta viene spostato in modo che coincidano, la spline viene chiusa.
-   Menu contestuale del nodo: {{Value|Elimina punto}}. Per una spline aperta devono rimanere almeno due punti. Per una spline chiusa il numero minimo di punti è tre.
-   Menu contestuale bordo: {{Value|Aggiungi punto}}, {{Value|Chiudi/Apri spline}} ({{Version/it|0.21}}) e {{Value|Inverti spline}} ({{Version/it|0.21}} ).



### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Draft Curva di Bézier cubica](Draft_CubicBezCurve/it.md) e <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Draft Curva di Bézier](Draft_BezCurve/it.md) 

-   Se il nodo iniziale o finale di una curva aperta viene spostato in modo che coincidano, la curva viene chiusa.
-   Menu contestuale del nodo: {{Value|Cancella punto}}, {{Value|Rendi acuto}}, {{Value|Rendi tangente}} e {{Value|Rendi simmetrico}}.
-   Menu contestuale bordo: {{Value|Aggiungi punto}}, {{Value|Chiudi/Apri curva}} ({{Version/it|0.21}}) e {{Value|Inverti curva}} ({{Version/it|0.21}} ).



### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Quotatura](Draft_Dimension/it.md) 

-   Le quote angolari non possono essere modificate.
-   I nodi iniziale e finale delle quote parametriche non possono essere spostati.
-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Arch Muro](Arch_Wall/it.md) 

-   Un singolo nodo per controllare l\'altezza del muro viene visualizzato sopra **Placement** del muro.
-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Arch_Structure.svg  style="width:24px;"> [Arch Struttura](Arch_Structure/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Arch Finestra](Arch_Window/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Arch_Space.svg  style="width:24px;"> [Arch Spazio](Arch_Space/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Arch_Panel_Cut.svg  style="width:24px;"> [Arch Sagoma di pannello](Arch_Panel_Cut.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:24px;"> [Arch Foglio di pannello](Arch_Panel_Sheet/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cubo](Part_Box/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Part Cilindro](Part_Cylinder/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Part Sfera](Part_Sphere/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cono](Part_Cone/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Part Linea](Part_Line/it.md) 

-   Nessun menu contestuale per questo oggetto.



### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Schizzo](Sketcher_NewSketch/it.md) 

-   È possibile modificare solo gli schizzi che contengono una singola linea non vincolata.
-   Nessun menu contestuale per questo oggetto.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Il colore dei nodi temporanei è lo stesso del colore dei simboli di snap. Questo colore può essere modificato nelle preferenze: **Modifica → Preferenze... → Draft → Impostazioni visive → Impostazioni visive → Colore**. Si noti che questo colore non viene utilizzato per i nodi temporanei visualizzati per [Draft BezCurves](Draft_BezCurve/it.md). Questi nodi usano invece il **Line Color** della curva.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Non esiste un metodo Python per modificare gli oggetti Draft. Per emulare i risultati del comando è necessario modificare le proprietà geometriche degli oggetti.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/it
