---
 GuiCommand:
   Name: Std_DrawStyle
   Name/it: Stile di disegno
   MenuLocation: Visualizza , Stile di disegno
   Workbenches: Tutti
   Shortcut: **V** **1** - **V** **7**
   SeeAlso: Std_SelBoundingBox/it
---

# Std DrawStyle/it



## Descrizione

Il comando **Stile di disegno** può sovrascrivere l\'effetto delle [proprietà](Property_editor/it.md) che definiscono la {{PropertyView/it|modalità di visualizzazione}} degli oggetti nella [vista 3D](3D_view/it.md).



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Fare clic sulla freccia nera verso il basso a destra del pulsante **<img src="images/Std_DrawStyleAsIs.svg" width=16px> [Stile di disegno](Std_DrawStyle/it.md)** e selezionare uno stile dal riquadro a comparsa.
    -   Andare nel menu **Visualizza → Stile di disegno** e scegliere uno stile.
    -   Nel menu contestuale [Vista 3D](3D_view/it.md) andare in **Stile di disegno** e selezionare uno stile.
    -   Usare una delle scorciatoie da tastiera: **V** e poi **1**, **2**, **3**, **4**, **5**, **6** o **7**.



## Stili di disegno disponibili 



### <img alt="" src=images/Std_DrawStyleAsIs.svg  style="width:24px;"> Come è 

Lo stile **Come è** non sovrascrive la proprietà **Display Mode** (Modalità di visualizzazione) degli oggetti.

![](images/Std_DrawStyleAsIs_example.png ) 
*4 oggetti identici ciascuno con una modalità di visualizzazione diversa (da sinistra a destra: 'Punti', 'Reticolo', 'Ombreggiato' e 'Facce piene') con lo stile di disegno 'Come è' applicato*



### <img alt="" src=images/Std_DrawStylePoints.svg  style="width:24px;"> Punti 

Lo stile **Punti** sovrascrive la proprietà **Display Mode** degli oggetti. Questo stile corrisponde alla modalità di visualizzazione \'Punti\'. I vertici sono visualizzati in tinta unita. I bordi e le facce non vengono visualizzati.

![](images/Std_DrawStylePoints_example.png ) 
*Gli stessi oggetti con lo stile di disegno 'Punti' applicato*



### <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> Reticolo 

Lo stile **Reticolo** sovrascrive la proprietà **Display Mode** degli oggetti. Questo stile corrisponde alla modalità di visualizzazione \'Wireframe\'. Vertici e bordi sono visualizzati in colori solidi. Le facce non vengono visualizzate.

![](images/Std_DrawStyleWireframe_example.png ) 
*Gli stessi oggetti con lo stile di disegno 'Reticolo' applicato*



### <img alt="" src=images/Std_DrawStyleHiddenLine.svg  style="width:24px;"> Linee nascoste 

Lo stile **Linee nascoste** sovrascrive la proprietà **Display Mode** degli oggetti. Gli oggetti vengono visualizzati come se fossero convertiti in mesh triangolari.

![](images/Std_DrawStyleHiddenLine_example.png ) 
*Gli stessi oggetti con lo stile di disegno 'Linee nascoste' applicato*



### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:24px;"> Senza ombre 

Lo stile **Senza ombre** sovrascrive la proprietà **Display Mode** degli oggetti. Vertici, bordi e facce sono visualizzati in colori solidi.

![](images/Std_DrawStyleNoShading_example.png ) 
*Gli stessi oggetti con lo stile di disegno 'Senza ombre' applicato*



### <img alt="" src=images/Std_DrawStyleShaded.svg  style="width:24px;"> Ombreggiato 

Lo stile **Ombreggiato** sovrascrive la proprietà **Display Mode** degli oggetti. Questo stile corrisponde alla modalità di visualizzazione \'Shaded\'. Vertici e bordi non vengono visualizzati. Le facce sono illuminate a seconda del loro orientamento.

![](images/Std_DrawStyleShaded_example.png ) 
*Gli stessi oggetti con lo stile di disegno 'Ombreggiato' applicato*



### <img alt="" src=images/Std_DrawStyleFlatLines.svg  style="width:24px;"> Facce piene 

Lo stile **Facce piene** sovrascrive la proprietà **Display Mode** degli oggetti. Questo stile corrisponde alla modalità di visualizzazione \'Flat lines\'. Vertici e bordi sono visualizzati in colori solidi. Le facce sono illuminate a seconda del loro orientamento.

![](images/Std_DrawStyleFlatLines_example.png ) 
*Gli stessi oggetti con lo stile di disegno 'Facce piene' applicato*



## Note

-   Gli oggetti nella [Vista 3D](3D_view/it.md) hanno anche una proprietà **Draw Style** (stile di disegno). Questa proprietà controlla il tipo di linea utilizzato per i bordi. Il comando Std DrawStyle non sostituisce questa proprietà.
-   Per una macro per alternare tra due stili di disegno, vedere: [Macro Stile di disegno](Macro_Toggle_Drawstyle/it.md).



---
⏵ [documentation index](../README.md) > Std DrawStyle/it
