---
 TutorialInfo:
   Topic: Sketcher
   Level: Iniciante
   Time: 30 minutos
   Author: Mark Stephen  e vocx
   FCVersion: 0.19
   Files: https://forum.freecadweb.org/viewtopic.php?f=36&p=371659#p371659 Sketcher Constraints practices
---

# Sketcher Micro Tutorial - Constraint Practices/pt-br







## Introdução

Este tutorial foi originalmente escrito por Quick61, e reescrito e reilustrado por vocx.

Este tutorial foi composto para ajudar o novo usuário a se familiarizar com as melhores práticas de restrição de [esboço](Sketch.md) no fluxo de trabalho da <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench/pt-br.md).

Existe uma regra geral para as restrições: quanto menor a quantidade de **restrições de dados** (cotas ou dimensões), melhor.

É preferível usar uma **restrição geométrica** em vez de uma dimensional, se possível. Isso tem a ver com o funcionamento interno do solucionador de restrições do Sketcher.



## Configuração

1\. Abra o FreeCAD, crie um novo documento em branco com **Arquivo → [<img src=images/Std_New.svg style="width:16px"> [Novo](Std_New.md)**.

:   1.1. Switch to the [Sketcher Workbench](Sketcher_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **[View](Std_View_Menu.md) → Workbench → Sketcher**.

Some actions to remember:

-   Press the right mouse button, or press **Esc** in the keyboard once, to deselect the active tool in edit mode.
-   To exit the sketch edit mode, press the **Close** button in the [task panel](task_panel.md), or press **Esc** twice in the keyboard.
-   To enter again edit mode, double click on the sketch in the [tree view](tree_view.md), or select it, and then click on **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [Edit sketch](Sketcher_EditSketch.md)**.



## Crie um Esboço 

2\. Click on **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [New sketch](Sketcher_NewSketch.md)**.

:   2.1. Choose the sketch orientation, that is, one of the base XY, XZ, or YZ planes. We will use the default plane and options.
:   2.2. Click **OK** to start constructing the sketch.


**Note:**

in the [task panel](task_panel.md) expand the **Edit controls** section, and make sure the **Auto constraints** option is disabled. Also turn off the grid snap, and hide the grid.



## Primeira Abordagem: Restrições de Referência 

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



## Uma Maneira Melhor: Referência e Restrições Geométricas 

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



## Esquema Ótimo: Principalmente Restrições Geométricas 

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



## Recursos Adicionais 

-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md)
-   [Sketcher Lecture](Sketcher_Lecture.md)
-   [Sketcher Tutorial](Sketcher_Tutorial.md)


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Micro Tutorial - Constraint Practices/pt-br
