# Manual:Navigating in the 3D view/it
<div class="mw-translate-fuzzy">





</div>


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


<div class="mw-translate-fuzzy">

La navigazione nella vista 3D di FreeCAD può essere fatta con un mouse, un dispositivo Space Navigator, la tastiera, un touchpad, o una combinazione di questi. FreeCAD implementa diversi [modi di navigazione](http://www.freecadweb.org/wiki/index.php?title=Mouse_Model/it), che determinano come sono eseguite le tre fondamentali operazioni di manipolazione della vista (spostamento, zoom e rotazione), e determinano anche il modo per selezionare gli oggetti sullo schermo. Le modalità di navigazione sono accessibili dalla schermata Preferenze, o direttamente facendo clic destro in qualsiasi punto della vista 3D:


</div>

![](images/FreeCAD-v0-18-NavigationModePopup.png )

Ognuna di queste modalità attribuisce per queste quattro operazioni pulsanti diversi del mouse, o combinazioni di mouse + tastiera, o gesti del mouse. Nella tabella che segue sono riportate le principali modalità disponibili:


<div class="mw-translate-fuzzy">

  Modalità            Spostamento                                                                                                                                                                                                             Rotazione                                                                                                                                                                                                        Zoom                                                                                                                                                                                                        Selezione
      
  OpenInventor        ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                 ![Click left button mouse](images/Select-mouse.svg )                                                                                                                                           ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                      hold CTRL + drag ![Click left button mouse](images/Select-mouse.svg )
  CAD **(default)**   ![Click middle button mouse](images/Pan-mouse.svg ) or ![Click right button mouse + CTRL key](images/Pan-mouse-CTRL.svg )                                     ![Hold middle then left mouse button](images/Rotate-mouse.svg ) or ![Click right button mouse + SHIFT key](images/Rotate-mouse-SHIFT.svg )   ![Roll middle button mouse](images/Zoom-mouse.svg ) or ![Click right button mouse + CTRL + SHIFT key](images/Zoom-mouse-CTRL-SHIFT.svg )   ![Click left button mouse](images/Select-mouse.svg )
  Blender             hold SHIFT + drag ![Click middle button mouse](images/Pan-mouse.svg ) or drag ![Click left + right button mouse and drag](images/Mouse_LMB%2BRMB.svg )   ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                          ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                      ![Click left button mouse](images/Select-mouse.svg )
  Touchpad            hold SHIFT + drag ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                              ALT + ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                                   PGUP / PGDOWN                                                                                                                                                                                               ![Click touchpad (mouse) left button](images/Select-touchpad.png )
  Gesture             drag ![Click right button mouse](images/Pan-mouse-Ctrl.svg )                                                                                                                                     drag ![Click left button mouse](images/Select-mouse.svg )                                                                                                                                  ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                      ![Click left button mouse](images/Select-mouse.svg )
  OpenCascade         ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                 ![Hold middle then right mouse button](images/Rotate-mouse-MMB+RMB.svg )                                                                                                           ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                      ![Click left button mouse](images/Select-mouse.svg )


</div>

#### Navigazione da tastiera 

In alternativa, sono sempre disponibili alcuni comandi da tastiera, a prescindere dalla modalità di navigazione:


<div class="mw-translate-fuzzy">

-   **CTRL +** e **CTRL -** per ingrandire e ridurre
-   I **tasti freccia** per spostare la vista alto/basso e destra/sinistra
-   **SHIFT + freccia sinistra** e **SHIFT + freccia destra** per ruotare la vista di 90 gradi
-   I tasti numerici, *\' da 0 a 6*\', per le sette viste standard, assonometrica, anteriore, superiore, destra posteriore, inferiore, e sinistra
-   **O** per impostare la fotocamera in modalità ortografica,
-   **P** per impostare la modalità prospettiva.
-   **CTRL** permette di selezionare più di un oggetto o elemento


</div>


<div class="mw-translate-fuzzy">

Questi controlli sono anche disponibili dal menu Visualizza e alcuni dalla barra degli strumenti Vista.


</div>

#### Utilizzo del cubo di navigazione 

Nella configurazione predefinita, compare un [cubo di navigazione](Navigation_Cube/it.md) nell\'angolo in alto a destra della finestra 3D. Può essere utilizzato per ruotare l\'oggetto visualizzato di un valore prestabilito, ripristinare la visualizzazione su una delle diverse viste standard e cambiare la modalità di visualizzazione.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

Quando si utilizza il cubo di navigazione, e si passa il puntatore su un\'area sensibile del cubo appare un controllo di colore azzurro. Se l\'area sotto il puntatore non cambia colore, fare clic su di essa non ha alcun effetto. Al momento della stesura di questo documento (v0.18), ci sono alcuni problemi di registrazione che impediscono l\'attivazione di tutti i controlli.


<div class="mw-translate-fuzzy">

Facendo clic su una faccia si commuta la vista diventa frontale a tale faccia; facendo clic su un angolo la vista diventa perpendicolare a quell\'angolo.


</div>

Facendo clic su uno dei quattro triangoli, la vista ruota di 45 gradi nella direzione indicata. Facendo clic su una delle due frecce curve in alto, la vista ruota di 45 gradi nella direzione indicata attorno a una linea che punta verso l\'osservatore.

Il cubo di navigazione può essere spostato in qualsiasi parte dell\'area 3D trascinandolo. Il pulsante di trascinamento (sinistro) del mouse deve essere premuto all\'interno del cubo stesso per avviare un trascinamento. La struttura non si muove finché il puntatore non viene trascinato fuori dal cubo.

C\'è un cubo più piccolo, nella parte inferiore destra del cubo, che attiva un menu a discesa per cambiare la modalità di visualizzazione.

### Selezionare gli oggetti 

Gli oggetti nella vista 3D possono essere selezionati cliccandoli con il corrispondente tasto del mouse, secondo la modalità di navigazione descritte sopra. Un singolo clic seleziona l\'oggetto, e una delle sue sotto-componenti (bordo, faccia, vertice). Facendo doppio click si seleziona l\'oggetto e tutte le sue sotto-componenti. Premendo il tasto CTRL è possibile selezionare più di un sotto-componente, o anche diversi sotto-componenti da diversi oggetti. Facendo clic con il pulsante di selezione su una parte vuota della visualizzazione 3D si deseleziona tutto.

Si può anche aprire un pannello chiamato \"Selezione\", disponibile dal menu Visualizza, che mostra ciò che attualmente è selezionato:

![](images/Selection_view.jpg )

Inoltre è possibile utilizzare Selezione per selezionare gli oggetti attraverso la ricerca di un particolare oggetto.

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [Le modalità di navigazione di FreeCAD](Mouse_Model/it.md)
-   [Il cubo di navigazione](Navigation_Cube/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:Navigating in the 3D view/it
