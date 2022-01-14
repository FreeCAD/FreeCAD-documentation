# Manual:BIM modeling/ro
{{Manual:TOC/ro}}

BIM înseamnă [Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling). Definiția exactă a ceea ce este variază, dar putem spune pur și simplu că în prezent sunt modelate clădiri și alte structuri mari, cum ar fi poduri, tuneluri etc. Modelele BIM se bazează, de obicei, pe modele 3D și includ, de asemenea, o serie de informații suplimentare, cum ar fi informații despre materiale, relații cu alte obiecte sau modele sau instrucțiuni speciale pentru construirea sau întreținerea. Această informație suplimentară permite toate tipurile de analize avansate ale modelului, cum ar fi rezistența structurală, costurile și estimările timpului de construcție sau calculele consumului de energie.


<div class="mw-translate-fuzzy">

Atelierul Arch(Arhitectură) [Arch Workbench](Arch_Workbench/ro.md) a FreeCAD implementează o serie de instrumente și facilități pentru modelarea BIM. Deși are un scop diferit, este făcut să lucreze în strânsă integrare cu restul FreeCAD: Orice realizat cu orice alt atelier de lucru al FreeCAD poate deveni un obiect Arch sau poate fi folosit ca bază pentru un obiect Arch.


</div>

Ca și în Atelierul [PartDesign Workbench](PartDesign_Workbench.md), obeictele produse În Arch Workbench sunt concepute pentru a fi construite în lumea reală. Prin urmare, ele trebuie să fie \'\'\'solide \'\'\'. Instrumentele atelierului Arch au, de obicei, grijă de aceasta în mod automat și oferă, de asemenea, unelte utilitare pentru a vă ajuta să verificați validitatea obiectelor.


<div class="mw-translate-fuzzy">

Atelierul Arch include, de asemenea, toate instrumentele de la atelierul [Draft Workbench](Draft_Workbench.md), și utilizează sistemul său de rețea și de ancorare. Înainte de a începe, este întotdeauna o idee bună să parcurgeți paginile de preferințe din atelierele Draft și Arch și să definiți setările implicite în funcție de preferințele dvs.


</div>

În acest capitol vom vedea cum să modelam această clădire mică:

![](images/Exercise_arch_01.jpg )

și să producă un plan și o vedere de secțiune din acesta:

![](images/Exercise_arch_02.jpg )


<div class="mw-translate-fuzzy">

-   Creați un nou document și comutați la [Arch Workbench](Arch_Workbench/ro.md).
-   Deschideți meniul**Edit -\> Preferences -\> Draft -\> Grid and Snapping** and set the **grid spacing** setați la 1000 mm, așa că avem o rețea/grilă cu nitatea de un metru, care va fi convenabilă pentru dimensiunea clădirii noastre.
-   În **snapping toolbar**, asigurați-vă că butonul <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [grid snap](Draft_ToggleGrid.md) este activat , astfel ca noi să putem utiliza grila cât mai mult posibil.
-   Definiți planul ca fiind **XY** [Working Plane](Draft_SelectPlane.md)
-   Desenați patru linii cu instrumentul <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Draft Line](Draft_Line.md) Puteți introduce coordonatele manual sau pur și simplu alegeți punctele de pe grilă cu mouse-ul:
    -   From point (0,0) to point (0,3)
    -   From point (0,3) to point (4,3)
    -   From point (4,3) to point (4,0)
    -   From point (4,0) to point (0,0)


</div>

![](images/Exercise_arch_03.jpg )

Observați că am tras mereu în aceeași direcție (în sensul acelor de ceasornic). Acest lucru nu este necesar, dar se va asigura că pereții pe care îi vom construi în continuare au toți aceleași direcții stânga și dreapta. S-ar putea să credeți că am putea pur și simplu să trasăm un dreptunghi aici, ceea ce este adevărat. Dar cele patru linii ne vor permite să ilustrăm mai bine cum să adăugăm un obiect în altul.

-   Once your have created the lines check their start and end points and adjust if necessary to get them exactly correct.

![](images/Manual-BIM_Modeling_-_Adjusting_Lines.png )


<div class="mw-translate-fuzzy">

-   Selectați prima linie, apoi apăsați butonul <img alt="" src=images/Arch_Wall.png  style="width:16px;"> [Wall](Arch_Wall.md) .
-   Repetați pentru celelalte linii, până aveți 4 pereți.
-   Selectați cei patru pereți, și definiți: **Height** property to **3.00m** and their **Alignment** property to **left**. Dacă nu ați tras liniile în aceeași ordine ca și cele de mai sus, unii dintre pereți ar putea fi orientați spre stânga și spre dreapta și ar fi trebuit să fie setați la dreapta. Veți obține patru pereți intersectați, în interiorul liniilor de bază:


</div>

![](images/Exercise_arch_04.jpg )


<div class="mw-translate-fuzzy">

Acum trebuie să ne alăturăm acestor pereți împreună, astfel încât să se intersecteze în mod corespunzător. Acest lucru nu este necesar atunci când pereții dvs. sunt desenați într-un mod în care se conectează deja cu ușurință, aici avem nevoie, deoarece se intersectează. În Arh, acest lucru se face prin alegerea unuia dintre pereți drept \"host\" și adăugarea celorlalte ca \"additions\". Toate obiectele Arch pot avea orice număr de adăugiri (obiectelor ale căror geometrie va fi adăugate la geometria gazdei) și subtracțiile (obiecte a căror geometrie va fi scăzută). Adăugările și scăderea unui obiect pot fi gestionate oricând prin dublu clic pe obiectul din arborescență.

-   Selectați cei patru pereți cu tasta **Ctrl** apăsată, ultimul fiind zidul pe care l-ați ales sădevină \'host\'
-   Apăsați butonul <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Add](Arch_Add.md). Cei patru pereții sunt acum transformați într-unul singur:


</div>

![](images/Exercise_arch_05.jpg )

The individual walls are however still accessible, by expanding the wall in the tree view.


<div class="mw-translate-fuzzy">

-   Let\'s now place a door. In FreeCAD, doors are considered a special case of windows, so this is done using the [Window](Arch_Window.md) tool.
-   Start by selecting the wall. This is not necessary, but a good habit to take. If an object is selected when starting the window tool, you will force the window to be inserted in that object, even if you snap to another object.
-   Set the [Working Plane](Draft_SelectPlane.md) to **auto** so we are not restricted to the ground plane
-   Press the <img alt="" src=images/Arch_Window.png  style="width:16px;"> [Window](Arch_Window.md) button.
-   In the window creation panel, select the **Simple door** preset, and set its **Width** to 0.9m and its **Height** to 2.1m
-   Make sure the <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Near snap](Draft_Snap_Near.md) location is turned on, so we can snap on faces
-   Place your window roughly on the middle of the front face of the wall:


</div>

![](images/Exercise_arch_06.jpg )

-   După ce faceți clic, fereastra noastră este pe fațeta corectă, dar nu exact unde vrem:

![](images/Exercise_arch_07.jpg )

-   Acum putem defini locația exactă prin extinderea obiectelor tip perete și tip fereatră din arborescența vederilor și modificarea proprietății **Placement** acestora pentru of the base sketch of our door. Set its position to **x = 2m, y = 0, z = 0**. Our window is now exactly where we want it:

![](images/Exercise_arch_08.jpg )

-   Repeat the operation to place a window: Select the wall, press the window tool, select the **Open 2-pane** preset, and place a 1m x 1m window in the same face as the door. Set the placement of the underlying sketch to position **x = 0.6m, y = 0, z = 1.1m**, so the upper line of the window is aligned to the top of the door.

![](images/Exercise_arch_09.jpg )

Windows are always built on sketches. It is easy to create custom windows by first creating a sketch on a face, then turning it into a window by selecting it, then pressing the window button. Then, the window creation parameters, that is, which wires of the sketch must be extruded and how much, can be defined by double-clicking the window in the tree view. Now, let\'s create a slab:


<div class="mw-translate-fuzzy">

-   Set the [Working Plane](Draft_SelectPlane.md) to **XY** plane
-   Create a <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> [rectangle](Draft_Rectangle.md) with a **length** of 5m, a height of **4m**, and place it at position x:-0.5m, y:-0.5m, z:0.
-   Select the rectangle
-   Click the <img alt="" src=images/Arch_Structure.png  style="width:16px;"> [structure](Arch_Structure.md) tool to create a slab from the rectangle
-   Set the **height** property of the slab to 0.2m and its **normal** direction to (0,0,-1) because we want it to extrude downwards. We could also simply have moved it 0.2m down, but it is always good practice to keep extruded objects at the same place as their base profile.
-   Set the **Role** property of the slab to **slab**. This is not necessary in FreeCAD, but is important for IFC export, as it will ensure that the object is exported with the correct IFC type.


</div>

![](images/Exercise_arch_10.jpg )


<div class="mw-translate-fuzzy">

-   Let\'s now use one of the structural presets to make a metallic beam. Click the <img alt="" src=images/Arch_Structure.png  style="width:16px;"> [structure](Arch_Structure.md) button, select a **HEB 180** preset, and set its height to **4m**. Place it anywhere:


</div>

![](images/Exercise_arch_11.jpg )

-   Adjust its **placement** by setting its **Angle** to 90° in the (1,0,0) axis, and its **position** to x:90mm, y:3.5m, z:3.09m. This will position the beam exactly on one of the side walls:

![](images/Exercise_arch_12.jpg )


<div class="mw-translate-fuzzy">

-   We need now to duplicate this beam a couple of times. We could do that one by one using the <img alt="" src=images/Draft_Clone.png  style="width:16px;"> [clone](Draft_Clone.md) tool, but there is a better way, to do all the copies at once using an array:
-   Select the beam
-   Press the <img alt="" src=images/Draft_Array.png  style="width:16px;"> [Array](Draft_Array.md) button
-   Set the **Number X** property of the array to 6, leave the Y and Z numbers to 1
-   Expand the **interval X** property, and press the small <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **expression** icon at the right side of the X field. This will open an [expressions editor](Expressions.md):


</div>

![](images/Exercise_arch_13.jpg )

-   Write **(4m-180mm)/5** in the expression field, and press **OK**. This will set the x value to 0.764 (4m is the total length of our front wall, 180mm is the width of the beam, which is why it is called HEB180, and we want a fifth of that space as interval between each beam):

![](images/Exercise_arch_14.jpg )


<div class="mw-translate-fuzzy">

-   We can now easily build a simple slab on top of them, by drawing a rectangle directly on the top plane of the beams. Select a top face of one of the beams
-   Press the <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> [working plane](Draft_SelectPlane.md) button. The working plane is now set to that face.
-   Create a <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> [rectangle](Draft_Rectangle.md), snapping to two opposite points of the border beams:


</div>

![](images/Exercise_arch_15.jpg )


<div class="mw-translate-fuzzy">

-   Select the rectangle
-   Click the <img alt="" src=images/Arch_Structure.png  style="width:16px;"> [structure](Arch_Structure.md) button and create a slab with a height of **0.2m**.


</div>

That\'s it, our model is now complete. We should now organize it so it exports correctly to IFC. The IFC format requires that all objects of a building are inside a building object, and optionally, inside a story. It also requires that all buildings are placed on a site, but the IFC exporter of FreeCAD will add a default site automatically if needed, so we don\'t need to add one here.


<div class="mw-translate-fuzzy">

-   Select the two slabs, the wall, and the array of beams
-   Press the <img alt="" src=images/Arch_Floor.png  style="width:16px;"> [Floor](Arch_Floor.md) button
-   Select the floor we just created
-   Press the <img alt="" src=images/Arch_Building.png  style="width:16px;"> [Building](Arch_Building.md) button


</div>

Our model is now ready to export:

![](images/Exercise_arch_16.jpg )

The [IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) is one of the most precious assets in a free BIM world, because it allows the exchange of data between any application and actor of the construction world, in an open manner (the format is open, free and maintained by an independent consortium). Exporting your BIM models as IFC ensures that anyone can see and analyze them, no matter the application used.

In FreeCAD, IFC import and export is done by interfacing with another piece of software, called [IfcOpenShell](http://ifcopenshell.org/). To be able to export to IFC from FreeCAD, the [IfcOpenShell-python](http://ifcopenshell.org/python.html) package must be installed on your system. Be sure to select one which uses the same python version as FreeCAD. The python version that FreeCAD uses is informed when opening the **View -\> Panels -\> Python console** panel in FreeCAD. When that is done, we can now export our model:

-   Select the top object you want to export, that is, the Building object.
-   Select menu **File -\> Export -\> Industry Foundation Classes** and save your file.
-   The resulting IFC file can now be opened in a wide range of applications and viewers (the image below shows the file opened in the free [IfcPlusPlus](http://www.ifcquery.com/) viewer). Checking the exported file in such a viewer application before distributing it to other people is important to check that all the data contained in the file is correct. FreeCAD itself can also be used to re-open the resulting IFC file.

![](images/Exercise_arch_17.jpg )

We will now place some dimensions. Unlike the [previous chapter](Manual_Generating_2D_drawings.md), where we drew all the dimensions directly on the Drawing sheet, we will use another method here, and place [Draft dimensions](Draft_Dimension.md) directly in the 3D model. These dimensions will then be placed on the Drawing sheet automatically. We will first make two groups for our dimensions, one for the dimensions that will appear in the plan view, and another for those that appear on the elevation.


<div class="mw-translate-fuzzy">

-   Right-click the \"house\" document in the tree view, and create two new groups: **Plan dimensions** and **Elevation dimensions**.
-   Set the [Working Plane](Draft_SelectPlane.md) to **XY** plane
-   Make sure the <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [restrict](Draft_Snap_WorkingPlane.md) snap location is turned on, so everything you draw stays on the working plane.
-   Draw a couple of <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [dimensions](Draft_Dimension.md), for example as on the image below. Pressing **Shift** and **Ctrl** while snapping the dimension points will give you additional options.


</div>

![](images/Exercise_arch_18.jpg )

-   Select all your dimensions, and drag them to the **Plan dimensions** group in the tree view
-   Set the [Working Plane](Draft_SelectPlane.md) to **XZ** plane, that is, the frontal vertical plane.
-   Repeat the operation, draw a couple of dimensions, and place them in the **Elevation dimensions** group.

![](images/Exercise_arch_19.jpg )


<div class="mw-translate-fuzzy">

We will now prepare a set of views from our model, to be placed on a Drawing page. We can do that with the tools from the Drawing Workbench, as we have seen in the previous chapter, but the Arch Workbench also offers an all-in-one advanced tool to produce plan, section and elevation views, called [Section Plane](Arch_SectionPlane.md). We will now add two of these section planes, to create a plan view and an elevation view.

-   Select the building object in the tree view
-   Press the <img alt="" src=images/Arch_SectionPlane.png  style="width:16px;"> [Section Plane](Arch_SectionPlane.md) button.
-   Set its **Display Height** property to 5m, its **Display Length** to 6m, so we encompass our house (this is not needed, but will look better, as it will show naturally what it is used for), and its **Placement** position at x:2m, y:1.5m, z:1.5m.
-   Check the list of objects considered by the Section Plane by double-clicking it in the tree view. Section Planes only render specified objects from the model, not all of them. The objects considered by the Section Plane can be changed here.


</div>

![](images/Exercise_arch_20.jpg )

-   Repeat the operation to create another section plane, give it the same display length and height, and give it the following **Placement**: position: x:2m, y:-2m, z:1.5m, angle: 90°, axis: x:1, y:0, z:0. Make sure this new section plane also considers the building object.

![](images/Exercise_arch_21.jpg )


<div class="mw-translate-fuzzy">

-   Now we have everything we need, and we can create our Drawing page. Start by switching to the [Drawing Workbench](Drawing_Workbench.md), and create a new default <img alt="" src=images/Drawing_Landscape_A3.png  style="width:16px;"> [A3 page](Drawing_Landscape_A3.md) (or select another template if you wish).
-   Select the first section plane, used for the plan view
-   Press the <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Draft View](Drawing_DraftView.md) button. This tool offers a couple of additional features over the standard [Drawing View](Drawing_View.md) tool, and supports the Section Planes from the Arch Workbench.
-   Give the new view the following properties:
    -   X: 50
    -   Y: 140
    -   Scale: 0.03
    -   Line width: 0.15
    -   Show Cut True
    -   Show Fill: True
-   Select the other section plane, and create a new Draft View, with the following properties:
    -   X: 250
    -   Y: 150
    -   Scale: 0.03
    -   Rendering: Solid


</div>

![](images/Exercise_arch_22.jpg )

We will now create two more Draft Views, one for each group of dimensions.

-   Select the Plan dimensions group
-   Press the <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Draft View](Drawing_DraftView.md) button.
-   Give the new view the following properties:
    -   X: 50
    -   Y: 140
    -   Scale: 0.03
    -   Line width: 0.15
    -   Font size: 10mm
-   Repeat the operation for the other group, with the following settings:
    -   X: 250
    -   Y: 150
    -   Scale: 0.03
    -   Line width: 0.15
    -   Font size: 10mm
    -   Direction: 0,-1,0
    -   Rotation: 90°

Our page is now ready, and we can export it to SVG or DXF formats, or print it. The SVG format allows you to open the file using illustration applications such as [Inkscape](http://www.inkscape.org), with which you can quickly enhance technical drawings and turn them into much nicer presentation drawings. It offers many more possibilities than the DXF format.


<div class="mw-translate-fuzzy">

**Downloads**


</div>

-   The file produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd>
-   The IFC file exported from the above file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.ifc>
-   The SVG file exported from the above file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.svg>


<div class="mw-translate-fuzzy">

**De citit în plus**


</div>


<div class="mw-translate-fuzzy">

-   [Atelierul Arch](Arch_Workbench/ro.md)
-   [The Draft working plane](Draft_SelectPlane.md)
-   [The Draft snapping settings](Draft_Snap.md)
-   [The expressions system](Expressions.md)
-   [The IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes)
-   [IfcOpenShell](http://ifcopenshell.org)
-   [IfcPlusPlus](http://www.ifcquery.com)
-   [Inkscape](http://www.inkscape.org)


</div>





{{Tutorials navi

}} 

[<img src="images/Property.png" style="width:16px"> BIM](Category_BIM.md)

---
[documentation index](../README.md) > [BIM](Category_BIM.md) > Manual:BIM modeling/ro
