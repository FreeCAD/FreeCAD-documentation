---
- TutorialInfo:/es
   Topic:Modeling
   Level:Beginner
   Author:[EmmanuelG](User_EmmanuelG.md)
   Time:1 hour
   FCVersion:0.16 or greater
   Files:[https://www.thingiverse.com/thing:2403310 Thingiverse 2403310]
---

# Toothbrush Head Stand/es




<div class="mw-translate-fuzzy">




</div>



## Un problema de la vida diaria 

Los cepillos de dientes eléctricos rara vez vienen con un soporte para el cabezal, mientras que en una familia a menudo se ven varios cabezales utilizados con un solo cuerpo. Muchas personas que se enfrentan a un problema común nos llevan a una variedad de soluciones, como se puede ver en Thingiverse (200-800 proyectos están relacionados con eso). Aquí está la primera respuesta y cómo diseñarla.


<div class="mw-translate-fuzzy">

Este tutorial le llevará a través de los pasos necesarios para modelar la pieza que se muestra en la imagen de abajo utilizando las herramientas básicas del [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/de.md). (muchas de las herramientas y capacidades no están cubiertas).


</div>

![](images/TBHS-model.png )

## First idea : a plate 


<div class="mw-translate-fuzzy">

## Primera idea : una placa 

-   Desde la página de inicio, seleccione ![](images/Workbench_PartDesign.svg ) *DiseñoPieza*, o crea un nuevo documento y selecciona el ambiente de trabajo *DiseñoPieza*.

![](images/TBHS-0.png )


</div>

![](images/TBHS-0.png )

### Create a sketch 


<div class="mw-translate-fuzzy">

### Crear un croquis 

-   Haz clic en <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [**Nuevo croquis**](Sketcher_NewSketch/es.md). Ya sea desde el menú contextual de tareas de la izquierda, o desde la barra de herramientas de arriba o desde el menú Diseño Pieza de la parte superior.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">


</div>

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

Un cuadro de diálogo le pide que elija la orientación del croquis y que proporcione un desplazamiento.

-   Elegiremos el Plano XY como se muestra en la imagen de arriba (esa orientación corresponde a la placa de construcción común de la mayoría de las impresoras 3D), luego haz clic en OK.

<img alt="" src=images/TBHS-2.JPG  style="width:800px;">

Ahora se encuentra frente al plano XY desde arriba, y tiene acceso a las herramientas de dibujo.

-   Haz clic en <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [**Rectangle**](Sketcher_CreateRectangle/es.md).
-   Haz clic para colocar un primer punto.
-   Haz clic para colocar la esquina opuesta.
-   Pulsa **ESC** o haz clic con el botón derecho del ratón para dejar de usar la herramienta.

<img alt="" src=images/TBHS-3.JPG  style="width:800px;">

Ahora tiene un rectángulo flotante de dimensiones no especificadas.


<div class="mw-translate-fuzzy">

-   Haga clic en una línea del rectángulo, ahora tiene acceso a las herramientas de restricción a la derecha de la barra de herramientas (dependiendo del tamaño de su pantalla puede que tenga que arrastrarlas a la izquierda para verlas todas)
-   Haga clic en <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distancia**](Sketcher_ConstrainDistance/es.md)
-   Un diálogo le pide que establezca una dimensión. Insertar 80mm, haga clic en OK.
-   Repite con el otro lado del rectángulo, también 80mm.


</div>

<img alt="" src=images/TBHS-4.JPG  style="width:800px;">

Ahora tienes un cuadrado flotante.

-   Haga clic en el punto inferior izquierdo del cuadrado.
-   Haga clic en el origen del plano XY (en la intersección de las dos líneas gruesas).
-   Haga clic en <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Coincidente**](Sketcher_ConstrainCoincident/es.md).

<img alt="" src=images/TBHS-5.JPG  style="width:800px;">


<div class="mw-translate-fuzzy">

Ahora tiene un boceto totalmente restringido, como le indica el solucionador de la izquierda y el cambio de color. Es una buena práctica tener siempre un croquis totalmente restringido.


</div>


<div class="mw-translate-fuzzy">

Un boceto poco restringido puede dejar espacio para cambios no deseados, si se modifica algo más tarde. Por el contrario, un croquis con demasiadas restricciones tampoco es bueno. En ese caso, el solucionador le advierte de las restricciones redundantes y debe eliminar algunas de ellas.


</div>

On the opposite, an over-constrained sketch is also not good. In that case the solver warn you of redundant constraints and you should remove some of them.

-   To leave the sketch, click either on the \"Close\" button on the left, or the <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> icon in the toolbar, or press **ESC**.

<img alt="" src=images/TBHS-6.JPG  style="width:800px;">

You now only see the square, and the contextual task menu on the left show you more options than before.

### Create a pad 


<div class="mw-translate-fuzzy">

### Crear una pastilla 

-   Haga clic en <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonométrico** entre las vistas estándar, para ver mejor lo que ocurrirá.
-   Haga clic en <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Pastilla**.
-   Introduzca 4mm y haga clic en OK.


</div>

<img alt="" src=images/TBHS-7.JPG  style="width:800px;">

Your sketch is now in volume !

### Create a sketch on it 


<div class="mw-translate-fuzzy">

### Crear un croquis en él 

-   Selecciona la cara superior


</div>

<img alt="" src=images/TBHS-8.JPG  style="width:800px;">

The color of the face change and you have more options in the contextual task menu.

-   Click on <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **New sketch**. As a face was selected it will not ask you to choose a plane.

<img alt="" src=images/TBHS-9.JPG  style="width:800px;">

-   Click on <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Circle**](Sketcher_CreateCircle.md), click to place the center, move the pointer and click to define the radius.
-   Draw 4 circles on the pad (of any size)
-   Press **ESC** or click the right mouse button to stop using the tool.

<img alt="" src=images/TBHS-10.JPG  style="width:800px;">

-   Select the circles
-   Click on <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [**Equal Length**](Sketcher_ConstrainEqual.md)

<img alt="" src=images/TBHS-11.JPG  style="width:800px;">

Now the circles share the same radius.

-   Click on <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [**External geometry**](Sketcher_External.md).
-   Click on the four sides of the square, it add lines, color magenta.

<img alt="" src=images/TBHS-12.JPG  style="width:800px;">

Theses lines will serve as reference to position the circles.

-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md).
-   Click on a center of a circle.
-   Click on a magenta line.
-   Set distance (20mm from each side).

<img alt="" src=images/TBHS-13.JPG  style="width:800px;">

-   Click on a circle
-   Click on <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [**Radius**](Sketcher_ConstrainRadius.md) and set it at 1,5mm.

<img alt="" src=images/TBHS-14.JPG  style="width:800px;">

-   To leave the sketch, click either on the \"Close\" button on the left, or the <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> icon in the toolbar, or press **ESC**.

<img alt="" src=images/TBHS-15.JPG  style="width:800px;">

### Create a pad 


<div class="mw-translate-fuzzy">

### Crear una pastilla 

-   Haga clic en <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonométrico** entre las vistas estándar, para ver mejor lo que ocurrirá.
-   Haga clic en <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Pastilla**.
-   Insertar 25mm y haga clic en OK.


</div>

<img alt="" src=images/TBHS-16.JPG  style="width:800px;">

You have the basic shape, it just need final touches.

### Rounding the corners 

-   Holding **CTRL** click on the vertical edge at each corner to select the four of them.

Don\'t hesitate to help you by switching the display mode (just at the left of the Axonometric View) between <img alt="" src=images/DrawStyleWireFrame.svg  style="width:32px;"> **Wireframe** and <img alt="" src=images/DrawStyleFlatLines.svg  style="width:32px;"> **Wireframe and shadow**.

<img alt="" src=images/TBHS-17.JPG  style="width:800px;">

-   Click on <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [**Fillet**](PartDesign_Fillet.md).
-   Set the radius at 20mm.

<img alt="" src=images/TBHS-18.JPG  style="width:800px;">

Much better.

### Making it more robust 

We need to add material at the base of the cylinders to make them less prone to snap. Because of the printing orientation these small surfaces will be fragile at the junction with the base.

-   Select the circles at the base of the cylinders

<img alt="" src=images/TBHS-19.JPG  style="width:800px;">

-   Click on <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [**Chamfer**](PartDesign_Chamfer.md).
-   Set it to 2mm.

<img alt="" src=images/TBHS-20.JPG  style="width:800px;">

### Chamfer the edges 

-   Select the face under the base, add a <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Chamfer** of 0,5mm.

The first layer of plastic is often being squashed a little too much, this will compensate that and save you time in cleaning the model. If the first layer is ok that will make it only nicer

<img alt="" src=images/TBHS-21.JPG  style="width:800px;">

-   Select the edges at the border of the upper face (holding **CTRL** ).

<img alt="" src=images/TBHS-23.JPG  style="width:800px;">

-   Add a <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Chamfer** of 1mm. This one is only aesthetic.

<img alt="" src=images/TBHS-22.JPG  style="width:800px;">

Tadaa !

## Export as a .STL 

-   In the Combo View on the left, select the tree view instead of the contextual task menu, click on the last feature (the chamfer).

<img alt="" src=images/TBHS-24.JPG  style="width:800px;">

-   Now you can select \"Export\...\" from the File menu at the top left, and select the file format .STL.
-   Just print it :-)

## Inspiration


<div class="mw-translate-fuzzy">

## Inspiración

El modelo anterior es un buen punto de partida para utilizar FreeCAD, pero como soporte de cabezal de cepillo de dientes tiene sus defectos: debido a la orientación de la impresión y a la pequeña superficie los palos son propensos a romperse.


</div>

Inspired by the variety of solutions other people came up with, we will make this second version which will be much better.

<img alt="" src=images/TBHS-v2.jpg  style="width:800px;">

Don\'t worry it is often needed to go through several revision for an idea (e.g. : once the prototype on the picture was used, we added more space between the heads so that they should not touch).

In this second part you will also learn to use more tools, like the powerful *Linear repetition*.

## Second idea : a band 

-   Create a new document and select the ![](images/Workbench_PartDesign.svg‎‎ ) *Part Design* workbench.

### Create a sketch 

-   Create a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **New sketch**, on the XY plane.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

-   Draw a <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Slot**](Sketcher_CreateSlot.md)
    -   Click to place the first center
    -   Move to define the length and radius
    -   Click to set the second center.

<img alt="" src=images/TBHS2-1.JPG  style="width:800px;">

You now have a floating slot of unspecified dimensions.

-   Click on one of the horizontal lines of the slot
-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md)
-   A dialog prompts you to set a dimension. Enter 75mm, click OK.
    -   that\'s for a 3 head stand, count 25mm for each, if you want more

<img alt="" src=images/TBHS2-2.JPG  style="width:800px;">

-   Click on one point of the horizontal line
-   Click on one point of the other horizontal line
-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md)
-   A dialog prompts you to set a dimension. Enter 29mm, click OK.

<img alt="" src=images/TBHS2-3.JPG  style="width:800px;">

-   Draw a <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Slot**](Sketcher_CreateSlot.md) around the first slot.

<img alt="" src=images/TBHS2-4.JPG  style="width:800px;">

-   Make the centers of the second slot coincident with the centers of the first slot with <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Coincident**](Sketcher_ConstrainCoincident_‎.md).

<img alt="" src=images/TBHS2-5.JPG  style="width:800px;">

-   Click on one point of the horizontal line of the first slot
-   Click on one point of the nearest horizontal line of the second slot
-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md)
-   A dialog prompts you to set a dimension. Enter 3mm, click OK.

<img alt="" src=images/TBHS2-6.JPG  style="width:800px;">

-   To make the sketch fully constrained
    -   Click on the lower left point of the second slot
    -   Click on the origin of the XY plan
    -   Click on <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Coincident**](Sketcher_ConstrainCoincident_‎.md)

<img alt="" src=images/TBHS2-7.JPG  style="width:800px;">

-   To leave the sketch, click either on the \"Close\" button on the left, or the <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> icon in the toolbar, or press **ESC**.

<img alt="" src=images/TBHS2-8.JPG  style="width:800px;">

### Create a pad 

-   Click on <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometric** among the standard views, to better see what will happen.
-   Click on <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Pad**.
-   Enter 30mm and click OK.

<img alt="" src=images/TBHS2-9.JPG  style="width:800px;">

### Create a sketch on it 

-   Select the upper face

<img alt="" src=images/TBHS2-10.JPG  style="width:800px;">

-   Create a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **New sketch**. As a face was selected it will not ask you to choose a plane.

<img alt="" src=images/TBHS2-11.JPG  style="width:800px;">

-   Draw an <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [**Hexagon**](Sketcher_CreateHexagon.md)
    -   Click to place the center
    -   Move to define the radius
    -   Click to set

<img alt="" src=images/TBHS2-12.JPG  style="width:800px;">

-   Click on an edge of the hexagon
-   Click on <img alt="" src=images/Constraint_Horizontal.svg  style="width:32px;"> [**Horizontal**](Sketcher_ConstrainHorizontal_‎.md)

<img alt="" src=images/TBHS2-13.JPG  style="width:800px;">

-   Click on the center of the hexagon
-   Click on the horizontal line of the XY plane
-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md)
-   A dialog prompts you to set a dimension. Enter 15mm, click OK.

<img alt="" src=images/TBHS2-14.JPG  style="width:800px;">

-   Click on the center of the hexagon
-   Click on the vertical of the XY plane
-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md)
-   A dialog prompts you to set a dimension. Enter 10mm, click OK.

<img alt="" src=images/TBHS2-15.JPG  style="width:800px;">

-   Click on the blue circle of the hexagon
-   Click on <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [**Radius**](Sketcher_ConstrainRadius.md)
-   A dialog prompts you to set a dimension. Enter 8mm, click OK.

<img alt="" src=images/TBHS2-16.JPG  style="width:800px;">

-   To leave the sketch, click either on the \"Close\" button on the left, or the <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> icon in the toolbar, or press **ESC**.

<img alt="" src=images/TBHS2-17.JPG  style="width:800px;">

### Create a hole 

-   Click on <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometric** among the standard views, to better see what will happen.
-   Click on <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [**Pocket**](PartDesign_Pocket.md).
-   Select *to the first* in the dropdown menu and click OK.

<img alt="" src=images/TBHS2-18.JPG  style="width:800px;">

### Linear repetition 

-   In the Combo View on the left, select the tree view instead of the contextual task menu, click on the pocket feature.
-   Click on <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**LinearPattern**](PartDesign_LinearPattern.md).
-   Set the length at 55mm and occurencies at 3, then click OK.

<img alt="" src=images/TBHS2-19.JPG  style="width:800px;">

### Create a sketch on it 

-   Select the inner face

<img alt="" src=images/TBHS2-20.JPG  style="width:800px;">

-   Create a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **New sketch**. As a face was selected it will not ask you to choose a plane.

<img alt="" src=images/TBHS2-21.JPG  style="width:800px;">

-   Click on <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Circle**](Sketcher_CreateCircle.md), click to place the center, move the pointer and click to define the radius.

<img alt="" src=images/TBHS2-22.JPG  style="width:800px;">

-   Click on the center of the circle
-   Click on the horizontal line of the XY plane
-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md)
-   A dialog prompts you to set a dimension. Enter 15mm, click OK.

<img alt="" src=images/TBHS2-23.JPG  style="width:800px;">

-   Click on the center of the circle
-   Click on the vertical of the XY plane
-   Click on <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distance**](Sketcher_ConstrainDistance.md)
-   A dialog prompts you to set a dimension. Enter 10mm, click OK.

<img alt="" src=images/TBHS2-24.JPG  style="width:800px;">

-   Click on the circle
-   Click on <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [**Radius**](Sketcher_ConstrainRadius.md)
-   A dialog prompts you to set a dimension. Enter 3.5mm, click OK.

<img alt="" src=images/TBHS2-25.JPG  style="width:800px;">

-   To leave the sketch, click either on the \"Close\" button on the left, or the <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> icon in the toolbar, or press **ESC**.

<img alt="" src=images/TBHS2-26.JPG  style="width:800px;">

### Create a pad 


<div class="mw-translate-fuzzy">

### Crear una pastilla 

-   Haz clic en <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonométrico** entre las vistas estándar, para ver mejor lo que ocurrirá.
-   Haga clic en <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Pastilla**.
-   Insertar 4mm y haga clic en OK.

<img alt="" src=images/TBHS2-27.JPG  style="width:800px;">


</div>

<img alt="" src=images/TBHS2-27.JPG  style="width:800px;">

### Linear repetition 

-   In the Combo View on the left, select the tree view instead of the contextual task menu, click on the pad feature.
-   Click on <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**LinearPattern**](PartDesign_LinearPattern.md).
-   Set the length at 55mm and occurencies at 3, then click OK.

<img alt="" src=images/TBHS2-28.JPG  style="width:800px;">

### Draft

-   Select the side of each round pads

<img alt="" src=images/TBHS2-29.JPG  style="width:800px;">

-   Click on <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [**Draft**](PartDesign_Draft.md).
-   Set the draft angle at 40°.
-   Click on \"Neutral plane\" and select the face on which the sketch is drawn.
-   Tick \"Invert the draft direction\".

<img alt="" src=images/TBHS2-30.JPG  style="width:800px;">

We could have used a chamfer to do something similar, but the draft is more appropriate in this case.

Chamfer = left / Draft = right

<img alt="" src=images/TBHS2-30-chamfer.JPG  style="width:200px;"><img alt="" src=images/TBHS2-30-draft.JPG  style="width:200px;">

### Finishes

-   Holding **CTRL** select the bottom and top faces.

<img alt="" src=images/TBHS2-31-bottom.JPG  style="width:200px;"><img alt="" src=images/TBHS2-31-top.JPG  style="width:200px;">

-   -   Add a <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Chamfer** of 0,5mm.

<img alt="" src=images/TBHS2-31.JPG  style="width:800px;">

Perfect !

## Export as a .STL 

-   In the Combo View on the left, select the tree view instead of the contextual task menu, click on the last feature (the chamfer).

<img alt="" src=images/TBHS2-32.JPG  style="width:800px;">

-   Now you can select \"Export\...\" from the File menu at the top left, and select the file format .STL.
-   Print it instead of the first version or to replace it if it eventually broke ;-)


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Toothbrush Head Stand/es
