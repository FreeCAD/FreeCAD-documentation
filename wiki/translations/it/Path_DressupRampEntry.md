# Path DressupRampEntry/it
---
- GuiCommand:   Name:Path DressupTag   Name/it:Rampa di ingresso   Workbenches:[MenuLocation:Path → Vesti percorso → Rampa di ingresso   SeeAlso:[[Path_DressupTag/it|DressupTag](Path_Workbench/it___Path]].md), [DressupDogbone](Path_DressupDogbone/it.md) , [DressupDragKnife](Path_DressupDragKnife/it.md) ---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento veste un percorso esistente per aggiungere una rampa


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un contorno o un oggetto profilo [Path](Path_Workbench/it.md)
2.  cliccare su <img alt="" src=images/Path_Dressup.png  style="width:16px;"> [Rampa](Path_DressupRampEntry/it.md)


</div>



## Proprietà


<div class="mw-translate-fuzzy">

-   **Ramp Feed Rate** può essere la velocità di avanzamento verticale o orizzontale corrente o qualche altro valore personalizzato
-   **Angle** della rampa contro l\'asse verticale. Un valore inferiore rende la rampa più ripida.
-   **Method** viene utilizzato per selezionare diverse modalità di rampa:
    -   RampMethod1 scende all\'angolo della rampa e le mosse orizzontali al punto di destinazione
    -   RampMethod2 va prima in orizzontale e poi in basso all\'angolo della rampa fino al punto di destinazione
    -   RampMethod3 scende a zig-zag
    -   L\'elica scende a spirale
-   **Dressup Start Depth** è la distanza sopra il livello target in cui inizia la rampa
-   **UseStartDepth** indica che la rampa non inizia sopra il livello del grezzo. Se non è impostato su true, la prima rampa può essere più ripida del previsto.


</div>

<img alt="" src=images/Ramp_method_1.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_2.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_3.png  style="width:" height="250px;"> 
*From left to right: Ramp method 1, 2 and 3*

<img alt="" src=images/Ramp_method_Helix.png  style="width:" height="250px;"> 
*Ramp method Helix*





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupRampEntry/it
