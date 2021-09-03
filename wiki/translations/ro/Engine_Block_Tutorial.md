 {{UnfinishedDocu}}


<div class="mw-translate-fuzzy">


{{TutorialInfo/ro
|Topic= Part Workbench
|Level= Beginner
|Time=
|Author=Andrewbuck40
|FCVersion=0.14.3700
|Files=
}}


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

Acesta este un tutorial introductiv de modelare în FreeCAD. Scopul acestui tutorial este să vă prezentăm tipurile de date primitive pentru obiecte parametrice, operații booleene, desene 2D și procesul de conversie a proiectelor 2D în modele 3D. Ca exemplu de lucru vom modela un bloc de motor simplu și carterul său prezentat în partea dreaptă.


</div>


<div class="mw-translate-fuzzy">

## Demarajul Modelării {#demarajul_modelării}

Pentru început, deschideți FreeCAD, mergeți la *File-\>New* pentru a crea un document nou, apoi *File-\>Save* pentru a o salva undeva pe computer, mi-am numit proiectul \'Engine\'. Veți observa că după salvarea proiectului, vederea arborescentă *tree view* în partea stângă a ecranului vă va arăta numele proiectului la care lucrați. Puteți avea mai multe proiecte deschise la un moment dat și fiecare proiect va fi afișat ca rădăcină a unui arbore în vizualizarea arborescentă.


</div>


<div class="mw-translate-fuzzy">

## Degroșarea blocului Motor {#degroșarea_blocului_motor}

Acum, pentru a începe să lucrați la modelul real. Vom începe prin adăugarea unei casete pentru conturul general al blocului motor. Pentru a face aceasta aven nevoie să adăugăm o piesă *part* la model, mergeți la View-\>Workbench-\>Part pentru a selecta [Part Workbench](Part_Workbench.md). Veți observa că după ce selectați atelierul de lucru, veți obține un set diferit de butoane din bara de instrumente în partea de sus. Treceți prin câteva din celelalte ateliere lucru pentru a vă familiariza cu sistemul de ateliere și apoi pentru a reveni la modulul piese (Part).


</div>


<div class="mw-translate-fuzzy">

### Blocul Motor {#blocul_motor}

Pe modulul Piese(Part) veți vedea o grămadă de butoane pentru obiecte primitive geometrice precum casetă, sferă, con, etc. Click pe butonul (<img alt="" src=images/Part_Box.png  style="width:16px;">) pentru a adăuga un cub(palaelipiped ) înj scenă. Fiecare dintre primitivele listate are un set implicit de parametri care se stabilesc atunci când primitivul este adăugat. If you want you can add one of each of the primitives to see what they all look like. Primitives can be removed from the scene by selecting them and pressing the delete key. There are two ways to select objects, you can either left-click on them in the 3D view, or you can left click on them in the tree view. In either method, holding CTRL will let you select multiple items. You can zoom the 3d view with the scroll wheel on your mouse. To pan the view, middle click and drag. To rotate the view you click and hold the middle mouse button and while holding it you *also* push and hold the left mouse button as well, then dragging the mouse will rotate the view. You can also do a single middle click on some part of your 3D object to make the view rotate around that point in 3D space. Also, the numbers 1-6 and the number 0 on the number pad will show you various views of the scene (top, left, axometric, etc). Spend a minute or two getting comfortable with manipulating the 3D view.


</div>


<div class="mw-translate-fuzzy">


:   *Further reading: [ Navigating in the 3D space](Mouse_Model.md)*


</div>


<div class="mw-translate-fuzzy">

Once you have your cube and are comfortable with how the mouse works, we will begin setting up the dimensions of the CAD model. Select the cube by clicking on it in the tree view and then click on the \'Data\' tab of the *Property View* located below the tree view (go to *View-\>Views-\>Property View* if you have closed it). In the data tab you can modify the properties of the object you have selected in the tree view. Depending on what kind of object you select there will be different parameters for you to set in the data tab. For a box we need a 3 vectors, one for its position in 3D space, another for its orientation, and a third to specify the dimensions of the box. For a sphere you would be able to specify the central point, and the radius; cones have a radius, height, and position; and so on. We are building a small 2-cylinder engine block so set the size and position of the box to the following values (make sure you set the XYZ under \'Position\', the ones under \'Axis\' set the axis of rotation and the default values are what we want):


</div>


:   {\| class=wikitable border=1

\|- \| X: 0.0 mm \|\| Length: 140.0 mm \|- \| Y: -40.0 mm \|\| Width: 80.0 mm \|- \| Z: 0.0 mm \|\| Height: 110.0 mm \|- \|}


<div class="mw-translate-fuzzy">

Acum, dacă aveți blocul motorului dvs. dimensionat corect, trebuie să îi dăm un nume mai descriptiv. Select it in the tree view and either right click to rename it or press the *F2 key* on your keyboard. Name this part \'Billet\'.


</div>


<div class="mw-translate-fuzzy">

### Primul cilindru {#primul_cilindru}

Next we will carve out the first cylinder all the way through the engine block. To do this we will add a cylinder to the model with the size we want to bore out and then do a Boolean operation to \"subtract\" the material away from the block. Click the add cylinder button (<img alt="" src=images/Part_Cylinder.png  style="width:16px;">) to create a new cylinder and then select it in the tree view and set its properties to the following:


</div>


:   {\| class=wikitable border=1

\|- \| X: 40.0 mm \|\| Height: 110.0 mm \|- \| Y: 0.0 mm \|\| Radius: 25.0 mm \|- \| Z: 0.0 mm \|\| \|- \|}


<div class="mw-translate-fuzzy">

Odată ce proprietățile sunt setate corect, ar trebui să vedeți capetele circulare ale cilindrului pe fețele de sus și de jos ale blocului motor. Denumiți acest obiect \"Cylinder 1\" selectând-l în vizualizarea arborescentă.


</div>


<div class="mw-translate-fuzzy">

### Al Doilea Cilindru {#al_doilea_cilindru}

Am putea face al doilea cilindru la fel ca în primul rând, dar ar fi mult mai ușor să copiem munca pe care am făcut-o pentru aceasta, deoarece singura diferență dintre cele două este coordonatele lor X. To do this, select *Cylinder 1* in the tree view and then go to *Edit-\>Duplicate Selection*. You will see the new cylinder appear in the tree view (name it *Cylinder 2* right away), but you will not see it in the 3D view as it is in the same place as the first cylinder. Now select *Cylinder 2* in the tree view and then change it\'s X coordinate to 100 mm. Notice that even as you are updating the numbers in the data field you should see the cylinder moving in the 3D view. Once the second cylinder is properly positioned you can see what they look like by selecting the *Billet* in the tree view and then pressing *Spacebar* to hide it (notice that hidden objects are grayed out in the tree view). Hide all three objects one by one and then show them all again.


</div>

### Găurirea Cilindrilor {#găurirea_cilindrilor}

<img alt="" src=images/_Engine_Block_Tutorial_-_Bored_Block.png  style="width:300px;">


<div class="mw-translate-fuzzy">

Acum, că ambii cilindri sunt la locul lor, vrem să îi folosim pentru a găuri blocul la dimensiunile corespunzătoare. To do this we will use *boolean operations* on our 3 primitives. We will start by making a union out of the two cylinders so we can subtract them as a group from the block. Select *Cylinder 1* in the tree view and then *CTRL+LeftClick* to select *Cylinder 2* as well. Now press the Union button (<img alt="" src=images/Part_Fuse.png  style="width:16px;">) to fuse the objects together. You will notice that in the tree view, there is now a new object called *Fusion*. If you click the dropdown arrow next to Fusion you will see the two cylinders but they will be grayed out. Instead of Fusion, lets rename that to *Cylinders* so it is easier to find later. Now we bore out the engine block. Select the *Billet* and *then* select the *Cylinders* and press the Make Cut button (<img alt="" src=images/Part_Cut.png  style="width:16px;">). The two selected objects will again be combined like they were for the union operation and the single resulting object will be named *Cut* (which you should rename to *Bored Block*). Press the *2* key on the number pad and you should now be able to look straight down through the cylinders out the other side of the engine block, then *MiddleClick+LeftClick+Drag* to look at your engine block. To the right you will see what the finished product should look like, notice that I have expanded the tree view on the left to show the individual primitives and have selected *Cylinder 2* for examination in the *Data* tab of the *Property View*.


</div>

### Prinicpalel Avantaje ale Modelării Parametrice {#prinicpalel_avantaje_ale_modelării_parametrice}

Acum, când am găurit cilindrii, vom examina a doua oară avantajele acestui sistem. Suppose at some point in the development, we find out that we want the cylinders to be a bit bigger. Since the union and intersection operations we performed were recorded as groupings in the tree view, we can change the cylinder size and FreeCAD will just re-run the union and intersection process and arrive at the new engine size. Play around with the radius and position of the two cylinders a bit and then return them to the parameters quoted above, before continuing the tutorial.

## Carterul Motorului {#carterul_motorului}

### Billet and Bearing Caps {#billet_and_bearing_caps}


<div class="mw-translate-fuzzy">

Next we will work on a crankcase under the engine block. Add a new box, rename it to *Crankcase Billet*, and give it the following properties:


</div>


:   {\| class=wikitable border=1

\|- \| X: 0.0 mm \|\| Length: 140.0 mm \|- \| Y: -50.0 mm \|\| Width: 100.0 mm \|- \| Z: -85.0 mm \|\| Height: 85.0 mm \|- \|}


<div class="mw-translate-fuzzy">

In order to tell the crankcase apart from the let\'s give one of them a different color. You can change color by right clicking on the object to change in the tree view. You can assign a color yourself or give the object a random color (choose random again if you don\'t like the color). Add another box called *Bearing carve*, give it the following properties, and then cut the *Bearing carve* away from the *Crankcase Billet* (i.e. select the billet first):


</div>

Add another box called **Bearing carve**, give it the following properties, and then cut the **Bearing carve** away from the **Crankcase Billet** (i.e. select the billet first):

:   {\| class=wikitable border=1

\|- \| X: 0.0 mm \|\| Length: 140.0 mm \|- \| Y: -40.0 mm \|\| Width: 80.0 mm \|- \| Z: -85.0 mm \|\| Height: 30.0 mm \|- \|}


<div class="mw-translate-fuzzy">

Rename the resulting *Cut* object to *Carved crankcase*.


</div>


<div class="mw-translate-fuzzy">

### Carving out the journals {#carving_out_the_journals}

Next we will cut out a semi-circular place for the crankshaft to sit and a space in the crankcase for it to spin. We will start with a cylinder, but the orientation of the default cylinder is vertical, whereas we need a horizontal one. This means we need to figure out how to rotate the cylinder to align it properly with our engine. If you look at the guide axis in the bottom right corner of the 3D window you will see we want the crankshaft to lie along the positive x-axis. This means that from its starting location we need to rotate 90 degrees around an axis parallel to the y-axis of the scene. This tells us what we need to enter the parameters for the cylinder. Create a cylinder called *Crankshaft carve* and give it these properties (notice that now we have to specify the orientation parameters, as well as the regular dimensions we did for the cylinder bores):


</div>


:   {\| class=wikitable border=1

\|- \| Axis X: 0.0 mm \|\| Angle: 90.0 degrees \|- \| Axis Y: 1.0 mm \|\| \|- \| Axis Z: 0.0 mm \|\| \|- \| Position X: 0.0 mm \|\| Height: 140.0 mm \|- \| Position Y: 0.0 mm \|\| Radius: 20.0 mm \|- \| Position Z: -55.0 mm \|\| \|- \|}


<div class="mw-translate-fuzzy">

Cut the crankshaft carve object away from the *Carved crankcase* and rename the resulting object *Crankcase with journals*.


</div>

### Finishing out the Crankcase {#finishing_out_the_crankcase}

Lastly we will cut out 2 final boxes so that the piston rods can reach from the crankcase up into the engine block. Make two objects called **Box carve 1** and **Box carve 2** with the following properties; also, you can duplicate **Box carve 1** and just change the X coordinate to get the second carver. Union them into an object called **Box carvers**, and cut this object away from the **Crankcase with journals**, calling the final result **Crankcase**. Remember, you can hide the **Bored block** by selecting it and pushing spacebar so you can see what you are doing.

:   {\| class=wikitable border=1

\|- \| X: 15.0 mm \|\| Length: 50.0 mm \|- \| Y: -25.0 mm \|\| Width: 50.0 mm \|- \| Z: -55.0 mm \|\| Height: 55.0 mm \|- \|}

:   {\| class=wikitable border=1

\|- \| X: 75.0 mm \|\| Length: 50.0 mm \|- \| Y: -25.0 mm \|\| Width: 50.0 mm \|- \| Z: -55.0 mm \|\| Height: 55.0 mm \|- \|}

<img alt="" src=images/_Engine_Block_Tutorial_-_Crankcase.png  style="width:300px;">

On the right you can see what the final result should look like. I have fully expanded the tree view so you can see the hierarchy of the boolean operations used to build the device. Remember that you can still dig down into this tree and change cylinder diameters, change the size or position of the crankshaft, etc, without having to rebuild the whole model from scratch. We could continue to carve out the crankcase further but this will be enough for now. Next we will look at using the 2D drafting mode to design the headbolt pattern and cut down on the weight of the engine block by removing much of the unnecessary steel billet that remains around the outside of the cylinders.

## 2D Drafting the Head Gasket Design {#d_drafting_the_head_gasket_design}

For the head bolts and the shape of the engine block we will be using more boolean operations to \"carve\" away the parts of the block we don\'t want. However, if we stop to think about it, every head bolt is going to look the same, it will cut all the way down into the crankcase, the only thing different will be where on the top of the head it is located. This means we can simply \"draw\" the shape of the head gasket on the top of the engine, and then use that like a pattern to do the carving we want done.

### Entering 2D Drafting Mode {#entering_2d_drafting_mode}

First we need to switch to the 2D Drafting workbench, to do this from part mode you can select *2D Drafting* from the dropdown box at the top that currently says *Part*. If you cannot find the dropdown box (not all workbenches show the dropdown) you can also select a workbench from the {{MenuCommand|View → Workbench}} menu entry. Even though we are doing 2d drawing, we will draw them in the 3D window by telling FreeCAD what plane we want the drawings projected into. After you have selected the 2D Drafting workbench just above the top-right corner of the 3D view and click on the leftmost button which will say one of the following {none, top, front, size, or d(\..., \..., \...)}. Once you click that, the left side of the bar will have a text box for you to enter a plane offset, and 5 buttons: XY, XZ, YZ, View, and None. The first three are the standard top, front, and side views, the *View* entry will use the plane perpendicular to the direction the camera is looking (the camera\'s viewplane), and the last will not project into a plane and let you fully define the XYZ coordinates for every point you draw. We want to set a plane offset of 110 (type it in and press enter) and then click the XY button to project the drawing onto the XY plane, located 110 mm up the Z axis which corresponds to the top of the engine block. Now that we have told FreeCAD what plane to draw in we are ready to start designing the head gasket.

The last thing to do is set up the 3D view. Even though all the drawings we produce will be projected into our defined 2D plane, we can look at the plane we are drawing on from any angle (including the other side of the plane so we draw \"backwards\"). Since we have told it the plane is the one co-planar to the top of the engine block, we should probably have the 3D view looking at that, or at least roughly in that direction. Press the 2 key on the number pad to look at the top view (notice that on the num pad, adjacent keys are opposite views so 1 and 4 are front-rear, 2 and 5 are top-bottom, and 3 and 6 are right-left). Once you are looking at the engine from the top down, you can center it by dragging the middle mouse button to pan the view. Finally, the 2D drafting mode will allow us to snap parts of the drawing to the corners of the engine block, the center of the cylinders, etc, in order to make this work best we should hide the crankcase so the drawings snap only to the part we are working on (press spacebar to show/hide the selected object).

### Laying Out the Head Bolts {#laying_out_the_head_bolts}

Now that the proper plane projection and view is set up we add 2d drawing elements in the same way we added primitives. Click the *Add Circle* button (<img alt="" src=images/Draft_Circle.svg  style="width:16px;">) and move your mouse around in the 3D view. You then need to tell FreeCAD the XY location for the center of the circle, and the radius, for both of these measurements you can either enter them with the mouse (following the instructions in the bottom left status bar), or you can type in the values in the text entry boxes that appear above the tree view. Go ahead and add a couple random circles on the top of the engine, as well as a few not on the engine, i.e. just out in the empty space surrounding your view of the engine. After you have done this, rotate the camera around the top of the engine block and look at the circles you drew, notice how they are \"flat\" in the plane we projected them into and this plane lines up with the top of the engine block; this will be important when we extrude the drawing to shape the engine. Now that you see how to add 2D elements you can delete the test circles you added and we will start entering the actual head layout. Note that if your circle disappears inside the engine block, your drawing projection plane is not properly set to XY mode, offset 110 mm.

Adding drafting elements with the mouse is fast and easy, but it is not very precise. For the actual bolt pattern we use the fact that moving the mouse will update the numbers in the text boxes just above the 3D view so we can see roughly the coordinates of where we want to place things. Once we have these rough coordinates we can type in the real values we want for precise positioning. Reset to the top view of the engine, click the *Add circle* button, and move your mouse around the top left corner of the engine block taking not of a good location for the head bolt. It looks like X=10, Y=30, would be a good place for the circle (note the Z coordinate should be grayed out, if it is not you need to set the plane properly like in the previous section, pressing escape will cancel drawing the circle).

Now that you see how to easily determine the coordinates of drawing elements you can easily design a bolt pattern or other 2 dimensional layout for a part such as fluid channels, circuit-board traces, etc. For our 3 head bolts let\'s on this side of the engine, let\'s use the following coordinates. Note that when you are typing in values to the boxes you can press enter to move on to the next box, and it is also a good idea to move your mouse out of the 3D view before you start typing in the coordinates as too much mouse movement will overwrite the numbers you have already entered in the text entry fields. Also, on my system I had trouble with the typed in circles having their Z coordinates set to 12.5 for some reason, if this is a problem for you, you can set the drawing projection plane to *None* and then manually enter the Z coordinates for the circles to be 110. Finally, when creating the circles, make sure to check the box labeled *Filled* otherwise when we extrude them later they will just create tubes like a toilet paper tube instead of a solid cylinder.

:   {\| class=wikitable border=1

\|- \| X1: 10 \|\| Y1: 25 \|\| Radius: 2.5 mm \|- \| X2: 70 \|\| Y2: 25 \|\| Radius: 2.5 mm \|- \| X3: 130 \|\| Y3: 25 \|\| Radius: 2.5 mm \|}

Name these circles **Bolt 1** through **Bolt 3**.

### The Other Side of the Block {#the_other_side_of_the_block}

Now that the first three head bolts are in place down one side of the engine we need three more mirrored on the other side, there are three ways we could do this:

-   We could just continue adding circles like we did for the first three and just negate the Y coordinates to put the bolts on the other side of the engine.
-   We could select the three we have added, go to {{MenuCommand|Edit → Duplicate Selection}} and then negate the Y coordinates of the three new circles.
-   We could use the mirror functionality in the Part Workbench.

Since you should already know how to do the first and second way, we will choose the third way for this example model. Each of the three methods has its own advantages and disadvantages, but a good operating rule is that simple models (like this one) probably should use the first or second methods, whereas models with lots of duplication and/or duplication of very complicated shapes/objects should probably use the third method.

So even though it is a bit of overkill we will mirror these bolts as a demonstration. Switch back to the part workbench (note that you can always switch to the *Complete* workbench to see all the tools at once if you would rather not switch back and forth (deprecated since v0.17)) by going to {{MenuCommand|View → Workbench}}. Select the three bolt circles in the tree view, and then press the mirror button (<img alt="" src=images/Part_Mirror.svg  style="width:16px;">). Once you press the mirror button you should notice a new display called the *Combo view* pop up on in the pane underneath the Tree view. Many of the tools need additional input before they can run and the Combo view lets you enter these parameters. You can make the Combo view larger by dragging the divider line separating it from the Property view up or down. Select **Bolt 1** from the list on the Combo view and set the *mirror plane* to XZ, then press OK (do the same for bolts 2 and 3).

At this point you should have a basic engine block with the cylinders bored out and the headbolt locations marked.

### Cutting Down the Excess Billet Material from the Block {#cutting_down_the_excess_billet_material_from_the_block}

Now that we have holes marked out for headbolts (we could do the same thing for oil channels, water jackets, etc) we will want to \"trim\" the outside of the block billet down to a more suitable shape. This will make the engine lighter, allow it to cool more easily, mean less steel must be used to cast the block. Like the bolt pattern we will be laying out a 2 dimensional drawing outlining the shape we want on the finished product. We could draw the spline curve directly with the mouse, or use the hybrid approach like we used for the circles where we used the mouse to find approximate coordinates and then typed in the true values we wanted. A more interesting approach is to use the 2D drafting\'s *construction mode* to plot a few guide shapes to help us trace out a nice, symmetric, spline curve by snapping to our constructed guide shapes.

As a guide we will draw two regular polygons for each cylinder, with the polygons concentric with the cylinder. To begin, switch to the top view of the engine block, hide the crankcase, switch back to the 2D drafting workbench, select the reference plane offset to 110 mm and the XY plane mode (or the *None* mode if you prefer), and click the *Construction mode* button in the command bar (the construction mode button looks like a trowel and is located just above the top right corner of the 3D view). Construction mode works just like the normal mode except any 2D drawing objects created while in construction mode get drawn in a different color and are automatically put into a separate group in the Tree view, this allows you to hide you guide drawings and leave behind only the real things like bolt hole markings by hiding the construction group, or to delete all of the guide objects by just deleting the group.

:   *Further reading: [ Construction Mode](Draft_ToggleConstructionMode.md)*

Now that your drawing plane is properly set up and you are in construction mode, click the *Regular Polygon* button (<img alt="" src=images/Draft_Polygon.svg  style="width:16px;">) and move your mouse along the edge of the left cylinder while holding down the CTRL button. You should see that it is snapping a small black dot either to the edge of the cylinder, or to the center of the cylinder, depending on where your mouse is along the circumference. Move so that the black dot snaps to the center of the cylinder and click the left mouse button. This places the center of the polygon at the center of the cylinder, the program prompts us for the number of edges on the polygon and the radius it is inscribed in. Investigating with the mouse a little bit looks like a radius of 30 is good (so type that in) and enter 14 for the number of side, but leave the *Filled* box unchecked this time. If you can\'t get the snap to lock onto the center of the cylinder (I had trouble with mine) you can always enter the coordinates manually (X=40, Y=0, Z=110). Add a second polygon, also centered on the left cylinder but this one should have 22 side and 45 mm radius. Finally add the same two polygons over the right cylinder (centered at X=100, Y=0, Z=110). When you are finished you should have two \"figure-8\'s\" surrounding the cylinders and head bolts. (Note that currently the program does not actually prompt you for the number of edges so you will just have to set the center and radius and then change the number of faces in the Property view).

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline.png  style="width:300px;">

Now that we have our guide polygons in place we are ready to draw in the spline curve defining the outside shape of the engine block. Since this curve will be part of the final object you can turn off construction mode by clicking the same button you pressed to turn it on. Now click the *Add BSpline* button (<img alt="" src=images/Draft_BSpline.svg  style="width:16px;">) and start drawing the BSpline by *CTRL+left clicking* on each place you want to add a control point for the spline curve. You will want your first control point to be on the leftmost point of the inner guide polygon for the left cylinder. Continue adding control points all along the spline curve until you click on the last point *before* the one you started drawing, then click the *Close* button up where you typed in the position and radius for the 2D circles we drew for the headbolts. Clicking this close button finished drawing control points for the spline curve and joins the ends together to form a closed loop. It is very important that you properly close loops like this if you plan to extrude them into solid objects like we will be with this one. For open spline curves you can just click the *Finish* button instead of the Close button when you are finished drawing. To the right you can see what you finished spline curve should look like just before you press the close button (notice I have drawn all but the last line segment and my mouse pointer is just about to click the *Close* button to finish the spline curve). Also notice that I have checked the *Filled* box so the resulting spline curve will form a solid sheet, rather than just an empty ring, this must be done to extrude it into a solid shape that is capped on the ends.

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline_Edit_Mode.png  style="width:300px;">

The control points are not shown in that picture so I have added a second screenshot showing the finished spline in edit mode (click the *Edit mode* button to turn editing on or off for the selected object, make sure to turn it off when you are done editing it or just skip over this step if you are satisfied with your engine block shape). Also, note that there is a discontinuity on the leftmost edge of the spline curve, even though it is closed properly, this is a bug in the program behavior and is currently being fixed, as a result your spline curve may look slightly different if you are running a newer version of the software than is available at this time.

### Extruding the 2D Head Design into our 3D Model to Finish the Design {#extruding_the_2d_head_design_into_our_3d_model_to_finish_the_design}


<div class="mw-translate-fuzzy">

Now we are closing in on the final design of the engine. Return to the Part workbench and click the *Extrude sketch* button (<img alt="" src=images/Part_Extrude.png  style="width:16px;">). In the combo box that pops up, use *CTRL+LeftClick* to select the 6 head bolts and the spline curve for extrusion. The default direction is the positive Z axis, we want the negative Z axis to extrude the head design \"down\" and into the engine block so set the direction to X=0, Y=0 and Z=-1, then type in 110 for the length (the height of the engine block). After you get all the values entered and click OK the circles for the bolts will be extruded downward to for cylinders and the spline will be extruded downward to produce a sort of cylinder with \"rippled\" edges. Select and hide the *Bored block* so you can see the extruded spline, then hide that object so you can see the 6 head bolt cylinders. You see that very sophisticated 3D shapes can be made by starting with a 2D drawing and extruding parts of it downward. We could even extrude different parts of the drawing by different amounts to do things like bore in bolt holes that just go part way through the block, but cut separate water jackets that go all the way through. At this point all your extruded objects are just named \"Extrude001\...\" so you will want to go through and name each of them so you can identify them in the next section (I will name mine *Head bolt bore 1* though *6* and name the spline *Extruded spline*, I suggest using the same names in your model as well). Now that you have your extruded shapes it is just a few boolean operations now to produce the final block design. Go through and show the major components (the *Bored block* and the *Crankcase*), and all your newly created extruded objects.


</div>

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width:300px;">


<div class="mw-translate-fuzzy">

Now that we have 3D objects for the bore holes and the outer shape, we can use a few boolean operations to stitch the whole thing together. Select your 6 extruded head bolts in the tree view and join them into a union (name the resulting object *Head bolt boreholes*). Then select the *Bored block* and the *Head bolt boreholes* in that order and perform a cut (like you did when you bored out the cylinders), name the resulting *Cut* object *Block with headbolts*. Finally, select the *Block with headbolts* and the *Extruded spline* and press the *Make intersection* button (<img alt="" src=images/Part_Common.png  style="width:16px;">), and name the resulting object *Engine block*. Your final object should look like the picture on the right.


</div>

Your final object should look like the picture on the right.




