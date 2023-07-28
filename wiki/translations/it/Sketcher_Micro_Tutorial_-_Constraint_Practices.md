---
- TutorialInfo:/it   Topic:Modellazione   Level:Principiante   Author:Mark Stephen ([[User:Quick61   Quick61]])|Time:Meno di 15 minuti   FCVersion:0.15.4671 o successiva
---

# Sketcher Micro Tutorial - Constraint Practices/it




<div class="mw-translate-fuzzy">




</div>




<div class="mw-translate-fuzzy">

## Benvenuto

Benvenuto. Questo tutorial è stato progettato per aiutare i nuovi utenti di FreeCAD a familiarizzare con le tecniche e i modi migliori per vincolare uno schizzo. Questo micro tutorial è fondamentalmente una copia migliorata di un post del forum di FreeCAD su questo argomento. Viene messo qui per consentirne l\'accesso a un maggior numero di utenti in modo più agevole.


</div>

This tutorial was originally written by Quick61, and it was rewritten and reillustrated by vocx.

This tutorial is designed to help the new user become familiar with the best practices of constraining a [Sketch](Sketch.md) in the workflow of the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md).


<div class="mw-translate-fuzzy">

## Una spiegazione sintetica 

Con i vincoli di sketch in FreeCAD vale una regola generale: meno vincoli dimensionali ci sono, meglio è. Se possibile, è sempre preferibile utilizzare un vincolo geometrico al posto di uno dimensionale. Questo è legato al funzionamento interno del risolutore di Sketcher.


</div>

It is preferable to use a **geometric constraint** in place of a dimensional one if possible. This has to do with the internal workings of the Sketcher\'s constraint solver.

## Setup

1\. Open FreeCAD, create a new empty document with **File → [<img src=images/Std_New.svg style="width:16px"> [New](Std_New.md)**.

:   1.1. Switch to the [Sketcher Workbench](Sketcher_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **[View](Std_View_Menu.md) → Workbench → Sketcher**.

Some actions to remember:

-   Press the right mouse button, or press **Esc** in the keyboard once, to deselect the active tool in edit mode.
-   To exit the sketch edit mode, press the **Close** button in the [task panel](task_panel.md), or press **Esc** twice in the keyboard.
-   To enter again edit mode, double click on the sketch in the [tree view](tree_view.md), or select it, and then click on **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [Edit sketch](Sketcher_EditSketch.md)**.

## Create a sketch 

2\. Click on **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [New sketch](Sketcher_NewSketch.md)**.

:   2.1. Choose the sketch orientation, that is, one of the base XY, XZ, or YZ planes. We will use the default plane and options.
:   2.2. Click **OK** to start constructing the sketch.


**Note:**

in the [task panel](task_panel.md) expand the **Edit controls** section, and make sure the **Auto constraints** option is disabled. Also turn off the grid snap, and hide the grid.




<div class="mw-translate-fuzzy">

## Primo approccio 

A titolo di esempio, prendiamo lo schizzo di un quadrato. Nella prima schermata, il disegno è completamente vincolato, ma solo con vincoli dimensionali, cioè distanze. Questo sistema è valido, ma troppo complicato, ingombra, e inoltre impegna il risolutore con intensiva matematica. Anche se questo non è un problema per un esempio semplice come questo, può diventarlo con schizzi più complessi.


</div>

3\. We will draw a fully constrained square, centered at the origin.

:   3.1. Click on **<img src="images/Sketcher_CreatePolyline.svg‎‎" width=16px> [Create polyline](Sketcher_CreatePolyline.md)**, then trace four lines in the general shape of a rectangle around the origin.

<img alt="" src=images/01a_Sk02_Sketcher_Rectangle_unconstrained.png  style="width:" height="400px;"> 
*Unconstrained rectangular sketch.*

:   3.2. Select one horizontal line, and press **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)**, then enter {{Value|20 mm}}.
:   3.3. Select the other horizontal line, and repeat the constraint with the same distance.
:   3.4. Select one vertical line, and press **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)**, then enter {{Value|20 mm}}.
:   3.5. Select the other vertical line, and repeat the constraint with the same distance.
:   3.6. Select one bottom corner point (a), and the origin of the sketch, and press **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)**, then enter {{Value|10 mm}}.
:   3.7. Select the top corner point (b) above the previous corner point (a), and the origin of the sketch, and repeat the horizontal constraint with the same distance.
:   3.8. Select the other bottom corner point (c), and the origin of the sketch, and press **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)**, then enter {{Value|10 mm}}.
:   3.9. Select the top corner point (b) again, and the origin of the sketch, and repeat the vertical constraint with the same distance.

<img alt="" src=images/01b_Sk02_Sketcher_Rectangle_constrained_lengths_1.png  style="width:" height="400px;"> <img alt="" src=images/01c_Sk02_Sketcher_Rectangle_constrained_lengths_2.png  style="width:" height="400px;"> 
*Left: datum constraints for the sides. Right: additional datum constraints for the interior distances.*

Looking at the **Constraints** section in the [task panel](task_panel.md), we see that the constraints are too many; they also clutter the view of the sketch. These constraints are also computationally intensive for the solver; while this is not an issue with a simple shape, it can become one with more complex shapes.




<div class="mw-translate-fuzzy">

## Un modo migliore 

La schermata successiva mostra lo stesso quadrato, vincolato utilizzando alcuni vincoli geometrici, usando i vincoli geometrici orizzontale e verticale con quelli dimensionali. Si può vedere che utilizzando i vincoli geometrici orizzontale e verticale il numero di vincoli dimensionali richiesti si è ridotto. Questo schizzo è vincolato meglio del primo, ma non è ancora il modo ottimale di vincolare il quadrato.


</div>

4\. We will draw the same square fully constrained, and centered at the origin. When you create the new sketch, make sure the **Auto constraints** option is disabled.

:   4.1. Click on **<img src="images/Sketcher_CreatePolyline.svg‎‎" width=16px> [Create polyline](Sketcher_CreatePolyline.md)**, then trace four lines in the general shape of a rectangle around the origin.
:   4.2. Select one horizontal line, and press **[<img src=images/Constraint_Horizontal.svg style="width:16px"> [Horizontal](‎Sketcher_ConstrainHorizontal.md)**.
:   4.3. Select the other horizontal line, and repeat the constraint.
:   4.4. Select one vertical line, and press **[<img src=images/Constraint_Vertical.svg style="width:16px"> [Vertical](‎Sketcher_ConstrainVertical.md)**.
:   4.5. Select the other vertical line, and repeat the constraint.

<img alt="" src=images/02a_Sk02_Sketcher_Rectangle_constrained_horizontal-vertical.png  style="width:" height="400px;"> 
*Geometrical horizontal and vertical constraints.*

:   4.6. Select one horizontal line, and press **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)**, then enter {{Value|20 mm}}. We see that the other horizontal line changes size at the same time.
:   4.7. Select one vertical line, and press **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)**, then enter {{Value|20 mm}}. We see that the other vertical line changes size at the same time.
:   4.8. Select one bottom corner point (a), and the origin of the sketch, and press **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)**, then enter {{Value|10 mm}}.
:   4.9. Select the top corner point (b) above the previous corner point (a), and the origin of the sketch, and press **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)**, then enter {{Value|10 mm}}.

<img alt="" src=images/02b_Sk02_Sketcher_Rectangle_constrained_lengths_1.png  style="width:" height="400px;"> <img alt="" src=images/02c_Sk02_Sketcher_Rectangle_constrained_lengths_2.png  style="width:" height="400px;"> 
*Left: datum constraints for only two sides. Right: additional datum constraints for only two interior distances.*

This is a better constrained sketch than the first one. The horizontal and vertical geometric constraints allow us to use fewer datum constraints, so our sketch looks less cluttered.




<div class="mw-translate-fuzzy">

## Schema ottimo 

Ora, in questa ultima schermata, è rimasto un solo vincolo dimensionale, e i vincoli rimanenti sono geometrici. Questo è il modo migliore per vincolare lo schizzo. Anche se con uno schizzo semplice come questo, sia un modo che l\'altro non creano grossi problemi, negli schizzi più grandi e complessi attenersi alla regola delle \"dimensioni al minimo\" si rivelerà utile a voi e ai vostri sforzi per costruire delle geometria con gli schizzi. I vincoli geometrici utilizzati in questo schizzo sono orizzontale, verticale, uguali e simmetria.


</div>

5\. We will draw the same square fully constrained, and centered at the origin. When you create the new sketch, make sure the **Auto constraints** option is disabled.

:   5.1. Click on **<img src="images/Sketcher_CreatePolyline.svg‎‎" width=16px> [Create polyline](Sketcher_CreatePolyline.md)**, then trace four lines in the general shape of a rectangle around the origin.
:   5.2. Select one horizontal line, and press **[<img src=images/Constraint_Horizontal.svg style="width:16px"> [Horizontal](‎Sketcher_ConstrainHorizontal.md)**.
:   5.3. Select the other horizontal line, and repeat the constraint.
:   5.4. Select one vertical line, and press **[<img src=images/Constraint_Vertical.svg style="width:16px"> [Vertical](‎Sketcher_ConstrainVertical.md)**.
:   5.5. Select the other vertical line, and repeat the constraint.

<img alt="" src=images/03a_Sk02_Sketcher_Rectangle_constrained_horizontal-vertical.png  style="width:" height="400px;"> 
*Geometrical horizontal and vertical constraints.*

:   5.6. Select one bottom corner point (a), then the top corner point that is diagonally opposite, and then the origin of the sketch; then press **[<img src=images/Constraint_Symmetric.svg style="width:16px"> [Symmetric](Sketcher_ConstrainSymmetric.md)**. The two selected points will be equidistant from the origin.
:   5.7. Select two adjacent sides of the rectangle (connected at one corner), and press **[<img src=images/Constraint_EqualLength.svg style="width:16px"> [Equal length](Sketcher_ConstrainEqual.md)**. Notice that due to the symmetry of the corner points, all sides are now of the same size.

<img alt="" src=images/03b_Sk02_Sketcher_Rectangle_constrained_symmetric.png  style="width:" height="400px;"> <img alt="" src=images/03c_Sk02_Sketcher_Rectangle_constrained_equal_length.png  style="width:" height="400px;"> 
*Left: symmetric constraint for only two corner points. Right: additional equal length distances for only two adjacent sides.*

:   5.8. Select one horizontal line, and press **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)**, then enter {{Value|20 mm}}. Due to the symmetric and length equality constraints previously added, we see that all sides become equal at the same time.

<img alt="" src=images/03d_Sk02_Sketcher_Rectangle_constrained_length.png  style="width:" height="400px;"> 
*All geometric constraints applied, and a single datum constraint for a side.*

This is the best way to constrain this sketch, as we only used one datum (dimensional) constraint.




<div class="mw-translate-fuzzy">

## Risorse aggiuntive 


</div>


<div class="mw-translate-fuzzy">

[Sketcher](Sketcher_Workbench/it.md)


</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Micro Tutorial - Constraint Practices/it
