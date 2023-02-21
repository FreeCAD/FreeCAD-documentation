# Navigation Cube/it
{{docnav/it
|[Metodi di selezione](Selection_methods/it.md)
|[Struttura del documento](Document_structure/it.md)
}}


{{TOCright}}



## Introduzione

Il **Cubo di Navigazione** dà un\'informazione visiva riguardo l\'orientamento della telecamera nella [vista 3D](3D_view/it.md) attuale e può essere utilizzato per cambiarla. Di default è visibile e si trova nell\'angolo in alto a destra della vista.

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

Il cubo principale ha 26 facce: 6 facce principali quadrate, 12 facce di bordo rettangolari ({{Version/it|0.20}}) e 8 facce d\'angolo triangolari. Facendo clic su uno di essi si riorienterà la telecamera in modo che la sua direzione sia perpendicolare alla faccia selezionata.



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

### Advanced parameters 

Some advanced Navigation Cube parameters cannot be changed in the [Preferences Editor](Preferences_Editor#Navigation.md). These parameters can be set manually in the [Parameter editor](Std_DlgParameter.md) or via the [CubeMenu external workbench](Interface_Customization#CubeMenu.md). Changes will become visible when a new 3D view is created (with [Std New](Std_New.md), [Std Open](Std_Open.md) or [Std ViewCreate](Std_ViewCreate.md)).

To manually set colors:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New unsigned item** from the context menu.
4.  Enter the name of one of these colors:
    -   
        **BorderColor**
        
        : the lines separating the cube faces, default is {{Value|4281479730}} (hex: {{Value|ff323232}}).

    -   
        **ButtonColor**
        
        : all elements around the cube, default is {{Value|2162354671}} (hex: {{Value|80e2e9ef}}).

    -   
        **FrontColor**
        
        : all cube faces, default is {{Value|3236096495}} (hex: {{Value|c0e2e9ef}}).

    -   
        **HiliteColor**
        
        : the cube or arrow face that is currently highlighted, default is {{Value|4289389311}} (hex: {{Value|ffaae2ff}}).

    -   
        **TextColor**
        
        : the text on the cube faces, default is {{Value|4278190080}} (hex: {{Value|ff000000}}).
5.  The color value must be entered as a 32-bit unsigned integer. Translated to the hexadecimal format this integer has the form {{Value|AARRGGBB}}. Where {{Value|AA}} stands for the alpha channel (a measure for the transparency), and the other three digit pairs stand for red, green and blue. To convert a hexadecimal value to an unsigned integer you can use the [Python console](Python_console.md), enter for example {{Incode|int("ff323232", 16)}}, or an online service such as [this one](https://cryptii.com/pipes/integer-encoder).
6.  Optionally set more colors.
7.  Press the **Close** button.

To manually set the border width:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New float item** from the context menu.
4.  Enter the name **BorderWidth**, {{Value|default is 1.1}}.
5.  Enter the width.
6.  Press the **Close** button.


{{docnav/it
|[Metodi di selezione](Selection_methods/it.md)
|[Struttura del documento](Document_structure/it.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/it
