# Part ProjectionOnSurface/it
---
- GuiCommand:   Name: Part ProjectionOnSurface   Name/it: Proiezione su superficie   MenuLocation: Part - Crea proiezione su superficie...   |Workbenches: [[Part_Workbench/it   Part]]|SeeAlso:    Version: 0.19---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Proietta un logo, un testo o qualsiasi faccia, polilinea o bordo su una superficie.


</div>


<div class="mw-translate-fuzzy">

Con questa funzione è possibile creare un solido, una faccia o una polinea di proiezione. Con la forma creata è possibile, ad esempio, creare un taglio booleano.


</div>

<img alt="" src=images/Part_ProjectionOnSurface1.png  style="width:300px;"> <img alt="" src=images/Part_ProjectionOnSurface2.png  style="width:300px;">


<div class="mw-translate-fuzzy">



*Proiezione su una superficie curva*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare la faccia su cui si vuole proiettare.
2.  La direzione della proiezione
    -   Quando si accede alla funzione, per la direzione di proiezione viene utilizzata la direzione corrente della telecamera
    -   Per cambiare la direzione, utilizzare la direzione della videocamera per ottenere la direzione della proiezione e premere \"Ottieni direzione corrente della videocamera\"
    -   O premere **X:**,**Y:**,**Z:** per cambiare la direzione x=1,x=-1,y=1,y=-1,z=1,z=-1
3.  Scegli il tipo di forma che si desidera aggiungere all\'oggetto di proiezione.
    -   Aggiungi faccai: selezionare una faccia che si desidera aggiungere.
    -   Aggiungi wire: selezionare un bordo. L\'algoritmo prende la polilinea a cui appartiene il bordo e la aggiunge all\'oggetto di proiezione.
    -   Aggiungi bordo: selezionare un bordo. Il bordo selezionato viene aggiunto all\'oggetto di proiezione.
4.  Scegliere il tipo di forma che si desidera creare.
    -   Mostra tutto: mostra se possibile l\'oggetto solido proiettato.
    -   Mostra facce: mostra se possibile l\'oggetto faccia proiettato.
    -   Mostra bordi: mostra l\'oggetto bordo proiettato.
5.  L\'altezza di estrusione è il valore di estrusione del solido lungo la direzione di proiezione inversa.
6.  La profondità solida è il valore in cui l\'oggetto di proiezione viene spostato lungo la direzione di proiezione.
7.  Quando si ha finito con l\'oggetto proiezione, premere **OK** e l\'oggetto di proiezione viene creato.


</div>

Notes:

-   The projection direction is automatically taken from the camera direction in the [3D view](3D_view.md) at the moment the tool is launched.
-   To change the direction, move the camera, and press **Get current camera direction**.
-   Alternatively press the **X:**, **Y:**, or **Z:** buttons to set the projection direction to the main global axes, +X, -X, +Y, -Y, +Z, or -Z.
-   However, do notice that changing the projection direction won\'t automatically update the projection preview; in order to do this, you must re-select the geometry by pressing the **Add...** buttons and picking the subelements again.

## Opzioni


<div class="mw-translate-fuzzy">

1.  Altezza di estrusione
    -   Il valore altezza di un solido di proiezione valido viene estruso lungo la direzione di proiezione inversa
2.  Profondità solida
    -   Il valore profondità di un oggetto di proiezione valido viene spostato lungo la direzione di proiezione
3.  Camera / direzione di proiezione
    -   \"Ottieni direzione corrente della telecamera\" imposta la vista corrente della telecamera per la direzione di proiezione
    -   X: alternare la direzione di proiezione tra x=1 e x=-1
    -   Y: alternare la direzione di proiezione tra y=1 e y=-1
    -   Z: alternare la direzione di proiezione tra z=1 e z=-1


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

L\'algoritmo di proiezione a volte non è in grado di creare una faccia di proiezione valida. In questo caso, non è possibile creare un solido.


</div>


<div class="mw-translate-fuzzy">

Se questo accade:

1.  Controllare se la faccia iniziale è valida.
2.  Controllare se la direzione di proiezione è valida. (La faccia può essere proiettata sulla superficie? O non colpisce la superficie?)
3.  Provare a utilizzare l\'opzione \"Mostra bordi\". I bordi sono proiettati bene? Provare a creare a mano una faccia usando i bordi.


</div>

The projection done in the Part workbench is not parametric. If you need a parametric workflow, please consult with the [Projection class](https://gist.github.com/CsatiZoltan/f4fd10bf20923143ba0e0678ea1d3d61), which is a Python scripted object, intended for programmatic use.

## Link


<div class="mw-translate-fuzzy">

-   \"Project faces onto bended surface\" [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=9&t=33700)


</div>

## Esempi


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ProjectionOnSurface/it
