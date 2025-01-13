# Manual:BIM modeling/ro
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

BIM înseamnă [Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling). Definiția exactă a ceea ce este variază, dar putem spune pur și simplu că în prezent sunt modelate clădiri și alte structuri mari, cum ar fi poduri, tuneluri etc. Modelele BIM se bazează, de obicei, pe modele 3D și includ, de asemenea, o serie de informații suplimentare, cum ar fi informații despre materiale, relații cu alte obiecte sau modele sau instrucțiuni speciale pentru construirea sau întreținerea. Această informație suplimentară permite toate tipurile de analize avansate ale modelului, cum ar fi rezistența structurală, costurile și estimările timpului de construcție sau calculele consumului de energie.


</div>


<div class="mw-translate-fuzzy">

Atelierul Arch(Arhitectură) [Arch Workbench](Arch_Workbench/ro.md) a FreeCAD implementează o serie de instrumente și facilități pentru modelarea BIM. Deși are un scop diferit, este făcut să lucreze în strânsă integrare cu restul FreeCAD: Orice realizat cu orice alt atelier de lucru al FreeCAD poate deveni un obiect Arch sau poate fi folosit ca bază pentru un obiect Arch.


</div>


<div class="mw-translate-fuzzy">

Ca și în Atelierul [PartDesign Workbench](PartDesign_Workbench.md), obeictele produse În Arch Workbench sunt concepute pentru a fi construite în lumea reală. Prin urmare, ele trebuie să fie **solide**. Instrumentele atelierului Arch au, de obicei, grijă de aceasta în mod automat și oferă, de asemenea, unelte utilitare pentru a vă ajuta să verificați validitatea obiectelor.


</div>

În acest capitol vom vedea cum să modelam această clădire mică:

![](images/FreeCAD_BIMHouse.png )


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


<div class="mw-translate-fuzzy">

Observați că am tras mereu în aceeași direcție (în sensul acelor de ceasornic). Acest lucru nu este necesar, dar se va asigura că pereții pe care îi vom construi în continuare au toți aceleași direcții stânga și dreapta. S-ar putea să credeți că am putea pur și simplu să trasăm un dreptunghi aici, ceea ce este adevărat. Dar cele patru linii ne vor permite să ilustrăm mai bine cum să adăugăm un obiect în altul.


</div>

-   Once you have created the lines check their start and end points and adjust if necessary to get them exactly correct.

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

![](images/FreeCAD_BIMDoor.png )


<div class="mw-translate-fuzzy">

-   După ce faceți clic, fereastra noastră este pe fațeta corectă, dar nu exact unde vrem:


</div>

![](images/FreeCAD_BIMDoorPos.png )


<div class="mw-translate-fuzzy">

-   Repeat the operation to place a window: Select the wall, press the window tool, select the **Open 2-pane** preset, and place a 1m x 1m window in the same face as the door. Set the placement of the underlying sketch to position **x = 0.6m, y = 0, z = 1.1m**, so the upper line of the window is aligned to the top of the door.


</div>

![](images/FreeCAD_BIMWindow.png )


<div class="mw-translate-fuzzy">

Windows are always built on sketches. It is easy to create custom windows by first creating a sketch on a face, then turning it into a window by selecting it, then pressing the window button. Then, the window creation parameters, that is, which wires of the sketch must be extruded and how much, can be defined by double-clicking the window in the tree view. Now, let\'s create a slab:


</div>


<div class="mw-translate-fuzzy">

-   Set the [Working Plane](Draft_SelectPlane.md) to **XY** plane
-   Create a <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> [rectangle](Draft_Rectangle.md) with a **length** of 5m, a height of **4m**, and place it at position x:-0.5m, y:-0.5m, z:0.
-   Select the rectangle
-   Click the <img alt="" src=images/Arch_Structure.png  style="width:16px;"> [structure](Arch_Structure.md) tool to create a slab from the rectangle
-   Set the **height** property of the slab to 0.2m and its **normal** direction to (0,0,-1) because we want it to extrude downwards. We could also simply have moved it 0.2m down, but it is always good practice to keep extruded objects at the same place as their base profile.
-   Set the **Role** property of the slab to **slab**. This is not necessary in FreeCAD, but is important for IFC export, as it will ensure that the object is exported with the correct IFC type.


</div>

![](images/FreeCAD_BIMSlab.png )


<div class="mw-translate-fuzzy">

-   We can now easily build a simple slab on top of them, by drawing a rectangle directly on the top plane of the beams. Select a top face of one of the beams
-   Press the <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> [working plane](Draft_SelectPlane.md) button. The working plane is now set to that face.
-   Create a <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> [rectangle](Draft_Rectangle.md), snapping to two opposite points of the border beams:


</div>

![](images/FreeCAD_BIMHouseg.png )


<div class="mw-translate-fuzzy">

That\'s it, our model is now complete. We should now organize it so it exports correctly to IFC. The IFC format requires that all objects of a building are inside a building object, and optionally, inside a story. It also requires that all buildings are placed on a site, but the IFC exporter of FreeCAD will add a default site automatically if needed, so we don\'t need to add one here.


</div>


<div class="mw-translate-fuzzy">

-   Select the two slabs, the wall, and the array of beams
-   Press the <img alt="" src=images/Arch_Floor.png  style="width:16px;"> [Floor](Arch_Floor.md) button
-   Select the floor we just created
-   Press the <img alt="" src=images/Arch_Building.png  style="width:16px;"> [Building](Arch_Building.md) button


</div>

Our model is now ready to export:

![](images/FreeCAD_BIMExport.png )

The [IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) is one of the most precious assets in a free BIM world, because it allows the exchange of data between any application and actor of the construction world, in an open manner (the format is open, free and maintained by an independent consortium). Exporting your BIM models as IFC ensures that anyone can see and analyze them, no matter the application used.

-   Select the top object you want to export, that is, the Building object.
-   Select menu **File -\> Export -\> Industry Foundation Classes** and save your file.
-   The resulting IFC file can now be opened in a wide range of applications and viewers (the image below shows the file opened in the free [IfcPlusPlus](http://www.ifcquery.com/) viewer). Checking the exported file in such a viewer application before distributing it to other people is important to check that all the data contained in the file is correct. FreeCAD itself can also be used to re-open the resulting IFC file.

![](images/FreeCAD_BIMIFC.png )


<div class="mw-translate-fuzzy">

We will now place some dimensions. Unlike the [previous chapter](Manual_Generating_2D_drawings.md), where we drew all the dimensions directly on the Drawing sheet, we will use another method here, and place [Draft dimensions](Draft_Dimension.md) directly in the 3D model. These dimensions will then be placed on the Drawing sheet automatically. We will first make two groups for our dimensions, one for the dimensions that will appear in the plan view, and another for those that appear on the elevation.


</div>

![](images/FreeCAD_BIMHouseDrawing.png )

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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Manual:BIM modeling/ro
