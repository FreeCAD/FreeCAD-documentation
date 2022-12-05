# Navigation Cube/it
{{docnav/it
|[Metodi di selezione](Selection_methods/it.md)
|[Struttura del documento](Document_structure/it.md)
}}


{{TOCright}}

## Introduzione

Il **Cubo di Navigazione** dà un\'informazione visiva riguardo l\'orientamento della telecamera nella [vista 3D](3D_view/it.md) attuale e può essere utilizzato per cambiarla. Di default è visibile e si trova nell\'angolo in alto a destra della vista.

Il Cubo di Navigazione è stato aggiornato in FreeCAD versione 0.20 e il resto di questa pagina descrive questa versione. In FreeCAD versione 0.19 il comportamento principale è lo stesso ma mancano alcune funzionalità.

![](images/Navigation_Cube_Example.png )

Il Cubo di Navigazione consiste in un certo numero di parti:

-   Il [cubo principale](#Cubo_Principale.md)
-   Sei [freccie direzionali](#Frecce_Direzionali.md)
-   Il [bottone inversione vista](#Bottone_Inversione_Vista.md) (in alto a destra) {{Version/it|0.20}}
-   Il [menu mini-cubo](#Menu_Mini-Cubo.md) (in basso a destra)
-   Gli indicatori degli assi X, Y e Z

Tutte le parti, eccetto gli indicatori degli assi, possono essere cliccate.

## Utilizzo

### Cubo Principale 


<div class="mw-translate-fuzzy">

Il cubo principale ha 26 facce: 6 facce principali quadrate, 12 facce di bordo rettangolari ({{Version/it|0.20}}) e 8 facce d\'angolo triangolari. Facendo clic su uno di essi si riorienterà la telecamera in modo che la sua direzione sia perpendicolare alla faccia selezionata.


</div>

### Frecce Direzionali 

Ci sono sei frecce direzionali: quattro freccie con punte triangolari e due frecce curve. Facendo clic su una delle frecce triangolari, la [Vista 3D](3D_view/it.md) ruota attorno a una linea perpendicolare alla direzione della freccia. Facendo clic su una freccia curva, la [Vista 3D](3D_view/it.md) ruota attorno alla direzione della vista.

### Bottone Inversione Vista 

Facendo clic sul pulsante rotondo nell\'angolo in alto a destra del Cubo di navigazione, la [Vista 3D](3D_view/it.md) ruoterà di 180 gradi attorno all\'asse verticale della vista.

### Menu Mini-Cubo 

Facendo clic sul cubo nell\'angolo inferiore destro del Cubo di Navigazione verrà visualizzato un menu con le seguenti opzioni:

-    **[Ortografica](Std_OrthographicCamera/it.md)**: passa a una vista ortogonale.

-    **[Prospettica](Std_PerspectiveCamera/it.md)**: passa a una vista prospettica.

-    **[Isometrica](Std_ViewIsometric/it.md)**: passa a una vista isometrica.

-    **[Adatta alla finestra](Std_ViewFitAll/it.md)**: esegue lo zoom e lo spostamento della telecamera in modo che tutti gli oggetti visibili rientrino nella vista.

## Personalizzazione

### Muovere il Cubo di Navigazione 

L\'intero cubo di navigazione può essere spostato cliccando col mouse in un punto qualsiasi del cubo principale e trascinandolo. La struttura non inizierà a muoversi finché il cursore non si sposta oltre uno dei bordi del cubo principale.

### Preferenze

Il Cubo di navigazione è controllato da diverse preferenze: **Modifica → Preferenze... → Visualizzazione → Navigazione → Cubo di navigazione**. Vedere [Impostare le Preferenze](Preferences_Editor/it#Navigazione.md).

### Impostazioni Avanzate 

L\'ambiente di lavoro esterno [CubeMenu](Interface_Customization/it#CubeMenu.md) fornisce un accesso più semplice a diverse opzioni di personalizzazione più avanzate.


{{docnav/it
|[Metodi di selezione](Selection_methods/it.md)
|[Struttura del documento](Document_structure/it.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/it
