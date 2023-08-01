# Manual:Navigating in the 3D view/it
{{Manual:TOC/it}}



### Alcune parole sullo spazio 3D 

Se questo è il primo contatto con un\'applicazione 3D, prima è necessario familiarizzare con alcuni concetti. In caso contrario, si può tranquillamente saltare questa sezione.

Lo spazio 3D in FreeCAD è uno [spazio euclideo](https://en.wikipedia.org/wiki/Euclidean_space). Ha un punto di origine e tre assi: X, Y e Z. Se si guarda la scena dall\'alto, convenzionalmente, l\'asse X punta verso destra, l\'asse Y all\'indietro, e l\'asse Z verso l\'alto. Nell\'angolo in basso a destra della vista di FreeCAD, è sempre possibile vedere da dove si sta visualizzando la scena:

![](images/Axes_orientation.png )

Il punto in cui i tre assi si incontrano è l\'origine. È il punto in cui il valore di tutte le coordinate è zero. Per ogni dato asse, lo spostamento in una direzione aumenta il valore delle coordinate e lo spostamento nella direzione opposta diminuisce il valore delle coordinate. Ogni punto di ogni oggetto esistente nello spazio 3D può essere localizzato tramite le sue coordinate (x, y, z). Ad esempio, un punto con coordinate (2,3,1) si trova a +2 unità sull\'asse X, +3 unità sull\'asse Y e +1 unità sull\'asse Z:

![](images/3dspace_coordinates.jpg )

Si può guardare la scena da qualsiasi angolazione, come se si fosse in possesso di una fotocamera. Questa camera può essere spostata a sinistra, a destra, in alto e in basso (Sposta), oppure ruotata attorno a ciò che si sta guardando (Ruota) e portata più vicino o più lontano dalla scena (Zoom).



### La vista 3D di FreeCAD 



#### Navigazione con il mouse 

La navigazione nella [Vista 3D](3D_view/it.md) di FreeCAD può essere fatta con un mouse, un dispositivo Space Navigator, la tastiera, un touchpad, o una combinazione di questi. FreeCAD implementa diverse [modalità di navigazione](Mouse_navigation/it.md), che determinano come vengono eseguite le tre operazioni base di manipolazione della vista (panoramica, rotazione e zoom), nonché come viene eseguita la selezione degli oggetti sullo schermo. È possibile accedere alle modalità di navigazione dalla schermata Preferenze o direttamente facendo clic con il pulsante destro del mouse in qualsiasi punto della [Vista 3D](3D_view/it.md):

![](images/FreeCAD-v0-18-NavigationModePopup.png )

Ognuna di queste modalità attribuisce per queste quattro operazioni pulsanti diversi del mouse, o combinazioni di mouse + tastiera, o gesti del mouse. Nella tabella che segue sono riportate le principali modalità disponibili:

++++++
| Modalità          | Spostamento                                                                                                                                                                                                                                       | Rotazione                                                                                                                                                                                             | Zoom                                                                                                                                                                                             | Selezione                                                                                                              |
+===================+===================================================================================================================================================================================================================================================+=======================================================================================================================================================================================================+==================================================================================================================================================================================================+========================================================================================================================+
| OpenInventor      | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                                           | ![Click left button mouse](images/Select-mouse.svg )                                                                                                                                | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                           | Premere **Ctrl** + trascinare ![Click left button mouse](images/Select-mouse.svg ) |
++++++
| CAD **(default)** | ![Click middle button mouse](images/Pan-mouse.svg ) o ![Click right button mouse + CTRL key](images/Pan-mouse-CTRL.svg )                                                                        | ![Hold middle then left mouse button](images/Rotate-mouse.svg ) o ![Click right button mouse + SHIFT key](images/Rotate-mouse-SHIFT.svg ) | ![Roll middle button mouse](images/Zoom-mouse.svg ) o ![Click right button mouse + CTRL + SHIFT key](images/Zoom-mouse-CTRL-SHIFT.svg ) | ![Click left button mouse](images/Select-mouse.svg )                                                 |
++++++
| Blender           | Premere **Shift** + trascinare ![Click middle button mouse](images/Pan-mouse.svg ) o trascinare ![Click left + right button mouse and drag](images/Mouse_LMB%2BRMB.svg ) | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                               | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                           | ![Click left button mouse](images/Select-mouse.svg )                                                 |
++++++
| Touchpad          | Premere **Shift** + trascinare ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                             |                                                                                                                                                                                        |                                                                                                                                                                                   | ![Click touchpad (mouse) left button](images/Select-touchpad.png )                        |
|                   |                                                                                                                                                                                                                                                   | **Alt**                                                                                                                                                                                           | **PgUp**                                                                                                                                                                                     |                                                                                                                        |
|                   |                                                                                                                                                                                                                                                   |                                                                                                                                                                                                    |                                                                                                                                                                                               |                                                                                                                        |
|                   |                                                                                                                                                                                                                                                   | \+ ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                               | / **PgDn**                                                                                                                                                                     |                                                                                                                        |
++++++
| Gesture           | Trascinare ![Click right button mouse](images/Pan-mouse-Ctrl.svg )                                                                                                                                                             | Trascinare ![Click left button mouse](images/Select-mouse.svg )                                                                                                                     | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                           | ![Click left button mouse](images/Select-mouse.svg )                                                 |
++++++
| OpenCascade       | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                                           | ![Hold middle then right mouse button](images/Rotate-mouse-MMB+RMB.svg )                                                                                                | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                           | ![Click left button mouse](images/Select-mouse.svg )                                                 |
++++++



#### Navigazione da tastiera 

In alternativa, sono sempre disponibili alcuni comandi da tastiera, a prescindere dalla modalità di navigazione:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} per ingrandire e ridurre

-   I **tasti freccia** , {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, per spostare la sinistra/destra e alto/basso

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} per ruotare la vista di 90 gradi

-   I tasti numerici, {{ASCII|48}}{{ASCII|49}}{{ASCII|50}}{{ASCII|51}}{{ASCII|52}}{{ASCII|53}}{{ASCII|54}}, per le sette viste standard: <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Isometrica](Std_ViewIsometric/it.md), <img alt="" src=images/Std_ViewFront.svg  style="width:24px;"> [Frontale](Std_ViewFront/it.md), <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [Dall\'alto](Std_ViewTop/it.md), <img alt="" src=images/Std_ViewRight.svg  style="width:24px;"> [Laterale destra](Std_ViewRight/it.md), <img alt="" src=images/Std_ViewRear.svg  style="width:24px;"> [Da dietro](Std_ViewRear/it.md), <img alt="" src=images/Std_ViewBottom.svg  style="width:24px;"> [Dal basso](Std_ViewBottom/it.md), and <img alt="" src=images/Std_ViewLeft.svg  style="width:24px;"> [Laterale sinistra](Std_ViewLeft/it.md)

-    **V**
    **O**per impostare la fotocamera in <img alt="" src=images/View-isometric.svg  style="width:24px;"> [modalità Ortografica](Std_OrthographicCamera/it.md).

-    **V**
    **P**per impostare la fotocamera in <img alt="" src=images/View-perspective.svg  style="width:24px;"> [modalità Prospettiva](Std_PerspectiveCamera/it.md).

-    **Ctrl**permette di selezionare più di un oggetto o elemento

Questi controlli sono anche disponibili dal [menu Visualizza](Std_View_Menu/it.md) e alcuni dalla barra degli strumenti Vista.

#### Utilizzo del cubo di navigazione 

Nella configurazione predefinita, compare un [cubo di navigazione](Navigation_Cube/it.md) nell\'angolo in alto a destra della finestra 3D. Può essere utilizzato per ruotare la visualizzazione dell\'oggetto di un valore prestabilito, ripristinare la visualizzazione su una delle diverse viste standard e cambiare la modalità di visualizzazione.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

Quando si utilizza il cubo di navigazione, e si passa il puntatore su un\'area sensibile del cubo appare un controllo di colore azzurro. Se l\'area sotto il puntatore non cambia colore, fare clic su di essa non ha alcun effetto. Al momento della stesura di questo documento (v0.18), ci sono alcuni problemi di registrazione che impediscono l\'attivazione di tutti i controlli.

Facendo clic su una faccia si commuta la vista che diventa frontale a tale faccia; facendo clic su un angolo la vista diventa perpendicolare a quello\'angolo.

Facendo clic su uno dei quattro triangoli, la vista ruota di 45 gradi nella direzione indicata. Facendo clic su una delle due frecce curve in alto, la vista ruota di 45 gradi nella direzione indicata attorno a una linea che punta verso l\'osservatore.

Il cubo di navigazione può essere spostato in qualsiasi parte dell\'area 3D trascinandolo. Il pulsante di trascinamento (sinistro) del mouse deve essere premuto all\'interno del cubo stesso per avviare un trascinamento. La struttura non si muove finché il puntatore non viene trascinato fuori dal cubo.

C\'è un cubo più piccolo, nella parte inferiore destra del cubo, che attiva un menu a discesa per cambiare la modalità di visualizzazione.



### Selezionare gli oggetti 

Gli oggetti nella vista 3D possono essere selezionati cliccandoli con il corrispondente tasto del mouse, secondo la modalità di navigazione descritte sopra. Un singolo clic seleziona l\'oggetto, e una delle sue sotto-componenti (bordo, faccia, vertice). Facendo doppio click si seleziona l\'oggetto e tutte le sue sotto-componenti. Premendo il tasto CTRL è possibile selezionare più di un sotto-componente, o anche diversi sotto-componenti da diversi oggetti. Facendo clic con il pulsante di selezione su una parte vuota della visualizzazione 3D si deseleziona tutto.

Si può anche aprire un pannello chiamato \"Selezione\", disponibile dal menu Visualizza, che mostra ciò che attualmente è selezionato:

![](images/Selection_view.jpg )

Inoltre è possibile utilizzare Selezione per selezionare gli oggetti attraverso la ricerca di un particolare oggetto.

**Approfondimenti**

-   [Le modalità di navigazione di FreeCAD](Mouse_navigation/it.md)
-   [Il cubo di navigazione](Navigation_Cube/it.md)



---
⏵ [documentation index](../README.md) > Manual:Navigating in the 3D view/it
