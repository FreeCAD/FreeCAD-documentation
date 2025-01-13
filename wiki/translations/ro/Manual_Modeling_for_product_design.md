# Manual:Modeling for product design/ro
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

[Product design](https://en.wikipedia.org/wiki/Product_design) este inițial un termen comercial, dar în lumea 3D, adesea înseamnă a modela ceva cu ideea de a o avea [3D-printed](https://en.wikipedia.org/wiki/3D_printing) sau, în general, fabricate de o mașină unealtă, de exemplu o imprimantă 3D sau o [CNC machine](https://en.wikipedia.org/wiki/Numerical_control).


</div>


<div class="mw-translate-fuzzy">

Când tipăriți obiecte în 3D, este foarte important ca obiectele dvs. să fie**solid**. As they will become real, obiecte solide, asta este evident. Nimic nu le împiedică să fie goale în interior, bineînțeles. Dar trebuie să aveți întotdeauna o idee clară despre care punct este în interiorul materialului și care este punctul afară, deoarece imprimanta 3D sau mașina CNC trebuie să știe exact ce este material de umplutură și ce nu. Pentru acest motiv, in FreeCAD, Atelierul [PartDesign Workbench](PartDesign_Workbench.md) are instrumentul perfect pentru a construi astfel de piese, deoarece se va avea grijă ca obiectele să fie solide și construibile.


</div>


<div class="mw-translate-fuzzy">

Pentru a ilustra cum Atelierul PartDesign funcționează, aideți să modelăm această bine cunoscută piesă [Lego](https://en.wikipedia.org/wiki/Lego):


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_01.jpg )


</div>


<div class="mw-translate-fuzzy">

Partea cool la ​​piesele Lego este că dimensiunile sunt ușor de obținut pe Internet, cel puțin pentru piesele standard. Acestea sunt destul de ușor de modelat și tipărite pe o imprimantă 3D și, cu puțină răbdare (tipărirea 3D necesită adesea multe ajustări și reglaj fin), puteți face piese care sunt complet compatibile și se îmbină cu un click caracteristic perfect în blocurile originale Lego. În exemplul de mai jos, vom face o piesă care este de 1,5 ori mai mare decât originalul.


</div>


<div class="mw-translate-fuzzy">

Vom folosi acum exclusiv instrumentele: [Sketcher](Sketcher_Workbench.md) și [PartDesign](PartDesign_Workbench.md). Deoarece toate instrumentele de la Sketcher Workbench sunt de asemenea incluse în Workbench Part Design, putem să rămânem în Design Part și nu va trebui să basculăm înainte și înapoi între ele.


</div>

A sketch is considered fully constrained when every point is locked into position by the appropriate number of constraints, meaning no part of the sketch can be moved freely. Achieving a fully constrained sketch is ideal because it ensures the design is well-defined and stable, allowing for predictable changes later in the design process. On the other hand, if more constraints are added than necessary---referred to as an over-constrained sketch---this can cause conflicts in the geometry. FreeCAD will alert you to any redundant or conflicting constraints, as over-constraining can cause issues in further operations like extrusions or cuts.


<div class="mw-translate-fuzzy">

Obiectele Part Design sunt bazate în întregime pe **Sketches**. O schiță(Sketch) este un obiect 2D, format din elemente lineare (linii, sau segmente de dreaptă, arce de cerc sau elipse) și constrângeri. Aceste constrângeri pot fi aplicate fie pe segmente de dreaptă, fie pe punctele lor finale sau puncte centrale, și vor forța geometria să adopte anumite reguli. De exemplu, puteți plasa o constrângere verticală pe un segment de linie pentru ao forța să rămână verticală sau o constrângere de poziție (blocare) pentru un punct extrem pentru a interzice mutarea acestuia. Atunci când o schiță are o cantitate exactă de constrângeri care interzic mișcarea oricărui punct al schiței, vorbim despre o schiță complet constrânsă. Când există constrângeri redundante, care ar putea fi eliminate fără a permite mutarea geometriei, se numește supra-constrânsă. Acest lucru ar trebui evitat, iar FreeCAD vă va notifica dacă apare un astfel de caz.


</div>


<div class="mw-translate-fuzzy">

Schițele dispun de un mod de editare, unde geometria lor și constrângerile lor pot fi modificate. Când ați terminat editarea și ați ieșit din modul editare, schițele se comportă ca orice alt obiect FreeCAD și pot fi folosite ca elemente de construcție pentru toate instrumentele de proiectare a pieselor, dar și în alte ateliere de lucru, cum ar fi [Part](Part_Workbench.md) or [Arch](Arch_Workbench.md). Atelierul [Draft workbench](Draft_Workbench.md) dispune, de asemenea, de un instrument care convertește obiectele Draft în Schițe și invers.


</div>


<div class="mw-translate-fuzzy">

-   Să începem prin modelarea unei forme cubice (de fapt paralelipipedice) va fi baza cărămizii noastre Lego. Mai târziu, vom sculpta/excava interiorul și vom adăuga cele 8 puncte deasupra. Deci, să începem acest lucru făcând o schiță dreptunghiulară pe care o vom extruda:
-   Comuntați pe Atelierul [PartDesign Workbench](PartDesign_Workbench.md)
-   Faceți Click pe butonul <img alt="" src=images/Sketcher_NewSketch.png  style="width:16px;"> [New Sketch](Sketcher_NewSketch.md).Va apărea o casetă de dialog care vă întreabă unde doriți să puneți schița, alegeți planul \"XY\", care este planul \"la sol\". Schița va fi creată și va fi imediat schimbată în modul de editare, iar vizualizarea va fi rotită și orientată pentru a putea privi după normala la planul de lucru.
-   Acum putem desena un dreptunghi, selectând instrumentul <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:16px;"> [Rectangle](Sketcher_CreateRectangle/ro.md) și făcând clicl pe 2 vârfuri diagonal opuse. Puteți plasa cele două puncte oriunde, deoarece locația lor corectă va fi definită în pasul următor
-   Veți observa că o serie de constrângeri au fost adăugate automat dreptunghiului nostru: segmentele verticale au primit o constrângere verticală, cele orizontale o constrângere orizontală și fiecare colț o constrângere punct-pe-punct care leagă segmentele împreună. Puteți experimenta mișcarea dreptunghiului prin tragerea liniilor cu mouse-ul, toată geometria va respecta constrângerile.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_02.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Now, let\'s add three more constraints:
    -   Select one of the vertical segments and add a <img alt="" src=images/Constraint_VerticalDistance.png  style="width:16px;"> [Vertical Distance Constraint](Sketcher_ConstrainDistanceY.md). Give it a size of 23.7mm.
    -   Select one of the horizontal segments and add a <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> [Horizontal Distance Constraint](Sketcher_ConstrainDistanceX.md). Make it 47.7mm.
    -   Finally, select one of the corner points, then the origin point (which is the dot at the crossing of the red and green axes), then add a <img alt="" src=images/Constraint_PointOnPoint.png  style="width:16px;"> [Coincident Constraint](Sketcher_ConstrainCoincident.md). The rectangle will then jump to the origin point, and your sketch will turn green, meaning it is now fully constrained. You can try moving its lines or points, nothing will move anymore.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_03.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Our base sketch is now ready, we can leave edit mode by pressing the **Close** button on top of its task panel, or simply by pressing the **Escape** key. If needed later on, we can reenter edit mode anytime by double-clicking the sketch in the tree view.
-   Let\'s extrude it by using the <img alt="" src=images/PartDesign_Pad.png  style="width:16px;"> [Pad](PartDesign_Pad.md) tool, and giving it a distance of 14.4mm. The other options can be left at their default values:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_04.jpg )


</div>


<div class="mw-translate-fuzzy">

The **Pad** behaves very much like the [Extrude](Part_Extrude.md) tool that we used in the previous chapter. There are a couple of differences, though, the main one being that a pad cannot be moved. It is attached forever to its sketch. If you want to change the position of the pad, you must move the base sketch. In the current context, where we want to be sure nothing will move out of position, this is an additional security.


</div>


<div class="mw-translate-fuzzy">

-   We will now carve the inside of the block, using the <img alt="" src=images/PartDesign_Pocket.png  style="width:16px;"> [Pocket](PartDesign_Pocket.md) tool, which is the PartDesign version of [Part Cut](Part_Cut.md). To make a pocket, we will create a sketch on the bottom face of our block, which will be used to remove a part of the block.
-   With the bottom face selected, press the <img alt="" src=images/Sketcher_NewSketch.png  style="width:16px;"> [New sketch](Sketcher_NewSketch.md) button.
-   Draw a rectangle on the face.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_05.jpg )


</div>


<div class="mw-translate-fuzzy">

-   We will now constrain the rectangle in relation to the bottom face. To do this, we need to \"import\" some edges of the face with the <img alt="" src=images/Sketcher_External.png  style="width:16px;"> [External geometry](Sketcher_External.md) tool. Use this tool on the two vertical lines of the bottom face:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_06.jpg )


</div>


<div class="mw-translate-fuzzy">

You will notice that only edges from the base face can be added by this tool. When you create a sketch with a face selected, a relation is created between that face and the sketch, which is important for further operations. You can always remap a sketch to another face later with the <img alt="" src=images/Sketcher_MapSketch.png  style="width:16px;"> [Map sketch](Sketcher_MapSketch.md) tool.


</div>


<div class="mw-translate-fuzzy">

-   The external geometry is not \"real\", it will be hidden when we leave edit mode. But we can use it to place constraints. Place the 4 following constraints:
    -   Select the top left point of the rectangle and the top point of the imported line and add a <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> [Horizontal Distance Constraint](Sketcher_ConstrainDistanceX.md) of 1.8mm
    -   Select again the top left point of the rectangle and the top point of the imported line and add a <img alt="" src=images/Constraint_VerticalDistance.png  style="width:16px;"> [Vertical Distance Constraint](Sketcher_ConstrainDistanceY.md) of 1.8mm
    -   Select the bottom right point of the rectangle and the bottom point of the right imported line and add a <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:16px;"> [Horizontal Distance Constraint](Sketcher_ConstrainDistanceX.md) of 1.8mm
    -   Select again the bottom right point of the rectangle and the bottom point of the right imported line and add a <img alt="" src=images/Constraint_VerticalDistance.png  style="width:16px;"> [Vertical Distance Constraint](Sketcher_ConstrainDistanceY.md) of 1.8mm


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_07.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Leave edit mode and we can now perform the pocket operation: With the sketch selected, press the <img alt="" src=images/PartDesign_Pocket.png  style="width:16px;"> [Pocket](PartDesign_Pocket.md) button. Give it a length of 12.6mm, which will leave the upper face of our pad with a thickness of 1.8mm (remember, the total height of our pad was 14.4mm).


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_08.jpg )


</div>


<div class="mw-translate-fuzzy">

-   We will now attack the 8 dots on the top face. To do this, since they are a repetition of a same feature, we will use the handy <img alt="" src=images/PartDesign_LinearPattern.png  style="width:16px;"> [Linear pattern](PartDesign_LinearPattern.md) tool of the Part Design Workbench, which allows to model once and repeat the shape.
-   Start by selecting the top face of our block
-   Create a <img alt="" src=images/Sketcher_NewSketch.png  style="width:16px;"> [New sketch](Sketcher_NewSketch.md).
-   Create two <img alt="" src=images/Sketcher_Circle.png  style="width:16px;"> [circles](Sketcher_CreateCircle.md).
-   For each circle, select it and add a <img alt="" src=images/Constraint_Radius.png  style="width:16px;"> [Radius Constraint](Sketcher_ConstrainRadius.md) of 3.6mm to each of them
-   Import the left edge of the base face with the <img alt="" src=images/Sketcher_External.png  style="width:16px;"> [External geometry](Sketcher_External.md) tool.
-   Place two vertical constraints and two horizontal constraints of 6mm between the center point of each circle and the corner points of the imported edge, so each circle has its center at 6mm from the border of the face:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_09.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Notice how, once again, when you lock the position and dimension of everything in your sketch, it becomes fully constrained. This always keeps you on the safe side. You could change the first sketch now, everything we did afterwards would keep tight.
-   Leave edit mode, select this new sketch, and create a <img alt="" src=images/PartDesign_Pad.png  style="width:16px;"> [Pad](PartDesign_Pad.md) of 2.7mm:


</div>

-   By choosing the completed sketch use the <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) tool setting the length to 12 mm.

![](images/FreeCAD_Exercise1_BottomPad.png )

-   This is it. Our brick is ready. If you wish to change its color, you can do so by going to the **View tab**.


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_10.jpg )


</div>


<div class="mw-translate-fuzzy">

You will notice that our modeling history (what appears in the tree view) has become quite long. This is precious because every single step of what we did can be changed later on. Adapting this model for another kind of brick, for example one with 2x2 dots, instead of 2x4, would be a piece of cake, we would just need to change a couple of dimensions and the number of occurrences in linear patterns. We could as easily create bigger pieces that don\'t exist in the original Lego game.


</div>


<div class="mw-translate-fuzzy">

But we could also want to get rid of the history, for example if we are going to model a castle with this brick, and we don\'t want to have this whole history repeated 500 times in our file.


</div>


<div class="mw-translate-fuzzy">

There are two simple ways to get rid of the history, one is using the [Create simple copy](Part_SimpleCopy.md) tool from the [Part Workbench](Part_Workbench.md), which will create a copy of our piece that doesn\'t depend anymore on the history (you can delete the whole history afterwards), the other way is exporting the piece as a STEP file and reimporting it.


</div>

**Downloads**

-   Modelul produs pe durata acestui exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**Read more**


<div class="mw-translate-fuzzy">

-   [The Sketcher](Sketcher_Workbench.md)
-   [The Part Design Workbench](PartDesign_Workbench.md)
-   [The Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2)


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design/ro
