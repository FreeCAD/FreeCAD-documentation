---
- TutorialInfo:/ro
   Topic:Modeling
   Level:Intermediate
   Time:
   Author:[Yorik](User_Yorik.md)
   FCVersion:0.14
   Files:
---

# Arch tutorial/ro




<div class="mw-translate-fuzzy">




</div>

![](images/Arch_tutorial_00.jpg )



## Introducere


<div class="mw-translate-fuzzy">

Acest tutorial are scopul de a vă oferi elementele de bază pentru a lucra cu [Arch Workbench](Arch_Workbench.md). Voi incerca sa o fac destul de simplu, astfel încât sa nu aveți nevoie de experiență anterioară cu FreeCAD, dar sa aveți o experiență cu 3D sau cu aplicații tip [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) . În orice caz, ar trebui să fiți pregătit să vă căutați informații suplimentare despre modul în care funcționează FreeCAD pe [FreeCAD documentation wiki](Main_Page.md). Pagina de pornire [ Getting started](Getting_started.md) trebuie citită, dacă nu aveți experiență anterioară cu FreeCAD. De asemenea, verificați secțiunea noastră [ tutorials](tutorials.md) și pe [youtube](http://www.youtube.com/results?search_query=freecad) veți găsi, de asemenea, mult mai multe tutoriale gratuite.


</div>


<div class="mw-translate-fuzzy">

Scopul Atelierului [Arch Workbench](Arch_Workbench.md) este să ofere o completă [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) workflow inside FreeCAD. Deoarece este încă în curs de dezvoltare, nu vă așteptați să găsiți aici aceleași instrumente și nivel de completare ca alternativele comerciale adulte cum ar fi [Revit](http://en.wikipedia.org/wiki/Revit) sau \[http: /en.wikipedia.org/wiki/Archicad ArchiCAD\], dar, pe de altă parte, FreeCAD fiind folosit într-un domeniu mult mai mare decât aceste aplicații, [Arch Workbench](Arch_Workbench.md) beneficiază foarte mult de celelalte discipline pe care FreeCAD le satisface și oferă câteva caracteristici rar întâlnite în aplicațiile tradiționale BIM.


</div>


<div class="mw-translate-fuzzy">

Iată, de exemplu, câteva caracteristici interesante ale programului [Arch Workbench](Arch_Workbench.md) al FreeCAD pe care le veți găsi cu greu în alte aplicații BIM:


</div>

-   Obiectele arhitecturale sunt întotdeauna solide. Din fundamentul mecanic puternic al FreeCAD, am învățat importanța de a lucra întotdeauna cu obiecte solide. Acest lucru asigură un flux de lucru mult mai lipsit de erori și operații booleene foarte fiabile. Deoarece tăierea prin obiecte 3D cu un plan 2D, pentru extragerea secțiunilor, este și o operație booleană, puteți vedea imediat importanța acestui punct.

-   Obiectele arhitecturale pot avea întotdeauna orice formă. Fără restricții. Pereții nu trebuie să fie verticali, dalele nu trebuie să arate ca plăci. Orice obiect solid poate deveni întotdeauna orice obiect arhitectural. Lucruri foarte complexe, de obicei greu de definit în alte aplicații BIM, cum ar fi o pardoseală curbată și un zid (da, arhitectul Zaha Hadid, despre care vorbim), nu prezintă nici o problemă specială în FreeCAD.


<div class="mw-translate-fuzzy">

-   Întreaga putere a FreeCAD vă este la îndemână. Aveți posibilitatea să proiectați obiecte arhitecturale cu orice alt instrument al FreeCAD, cum ar fi [PartDesign Workbench](PartDesign_Workbench.md), și atunci când acestea sunt gata, convertiți-le în obiecte arhitecturale. Ele vor păstra în continuare istoria lor de modelare completă și vor continua să fie complet editabile. De asemenea, [Arch Workbench](Arch_Workbench.md) moștenește o mare parte din funcți(ile)onalitatea [Draft Workbench](Draft_Workbench.md), cum ar fi [snapping](Draft_Snap.md) și [working planes](Draft_SelectPlane.md).


</div>


<div class="mw-translate-fuzzy">

-   [Arch Workbench](Arch_Workbench.md) este foarte prietenos cu [ mesh](Mesh_Workbench.md). Puteți proiecta cu ușurință un model arhitectural într-o aplicație bazată pe plasă, cum ar fi [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) sau [SketchUp](http://en.wikipedia.org/wiki/Sketchup) și să îl importați în FreeCAD. Dacă ați avut grijă de calitatea modelului dvs., iar obiectele sale sunt forme multiple, transformarea lor în obiecte arhitecturale necesită doar apăsarea unui buton.


</div>


<div class="mw-translate-fuzzy">

În timp ce scriu acest lucru, lucrarea [Arch Workbench](Arch_Workbench.md), ca și restul programului FreeCAD, suferă unele limitări. Cele mai multe sunt lucrate, totuși, și vor dispărea în viitor.


</div>


<div class="mw-translate-fuzzy">

-   FreeCAD is no 2D application. It is made for 3D. There is a reasonable set of tools for drawing and editing 2D objects with the [Draft Workbench](Draft_Workbench.md) and [Sketcher Workbench](Sketcher_Workbench.md), but it is not made for handling very large (and sometimes badly drawn) 2D CAD files. You can usually successfully import 2D files, but don\'t expect very high performance if you want to keep working on them in 2D. You have been warned.


</div>


<div class="mw-translate-fuzzy">

-   No materials support. FreeCAD will have a complete [Material](Material.md) system, able to define very complex materials, with all the goodies you can expect (custom properties, material families, rendering and visual aspect properties, etc), and the [Arch Workbench](Arch_Workbench.md) will of course use it when it is ready.


</div>

-   Very preliminary [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) support. You can already [import IFC files](Arch_IFC.md), quite reliably, provided [IfcOpenShell](http://ifcopenshell.org) is installed on your system, but exporting is still not officially supported. This is worked on both by the FreeCAD and IfcOpenShell developers, and in the future we can expect full-powered IFC support.

-   Most Arch tools are still in development. That means that automatic \"wizard\" tools that create complex geometry automatically, such as [Arch Roof](Arch_Roof.md) or [Arch Stairs](Arch_Stairs.md) can only produce certain types of objects, and other tools that have presets, such as [Arch Structure](Arch_Structure.md) or [Arch Window](Arch_Window.md) only have a couple of basic presets. This will of course grow over time.

-   [Units](Units.md) are being implemented in FreeCAD, which will allow you to work with any unit you wish (even imperial units, you guys from the USA can be eternally grateful for this to Jürgen, FreeCAD\'s godfather and dictator). But at the moment the implementation is not complete, and the Arch workbench still doesn\'t support them. You must consider it \"unit-less\".


<div class="mw-translate-fuzzy">


{{Note|FreeCAD version 0.14 required|This tutorial was written using [FreeCAD version 0.14](Release_notes_0.14.md). You will need at least this version number in order to follow it. Earlier versions might not contain all the needed tools, or they could lack options presented here.}}


</div>

## Typical workflows 


<div class="mw-translate-fuzzy">

Atelierul [Arch Workbenchse](Arch_Workbench.md) face în principal pentru două tipuri de fluxuri de lucru:


</div>

-   Construiți-vă modelul cu o aplicație mai rapidă, bazată pe plasă, cum ar fi [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) sau [SketchUp](http://en.wikipedia.org/wiki/Sketchup),și le importați în FreeCAD pentru a extrage planurile și secțiunile. FreeCAD fiind conceput pentru modelare de precizie, la un nivel mult mai ridicat decât ceea ce avem nevoie de obicei în modelarea arhitecturală, construirea modelelor dvs. direct în FreeCAD poate fi greoaie și lentă. Din acest motiv, un astfel de flux de lucru are mari avantaje. Am descris-o pe blogul meu [this article](http://yorik.uncreated.net/guestblog.php?2012=180). Dacă aveți grijă să modelați corect și precis (plase curate, solide, necombinate), acest flux de lucru vă oferă același nivel de performanță și precizie ca celălalte.


<div class="mw-translate-fuzzy">

-   Construiți-vă modelul direct în FreeCAD. Așa voi prezenta în acest tutorial. Vom folosi în principal trei Ateliere de lucru: [Arch](Arch_Workbench.md), bineăînțeles, dar și [Draft](Draft_Workbench.md), ale căror unelte sunt incluse în Aatelierul Arch, astfel încât nu este necesar să se schimbe Atelierele lucru și [Sketcher](Sketcher_Workbench.md).

În mod convenabil, puteți face cum fac eu de obicei, ceea ce înseamnă crearea unei bare de instrumente personalizate în atelierul lucru Arch, with Tools → Customize, adăugați instrumentele de la Sketcher pe care îl utilizați frecvent. Acesta este Atelierul meu \"personalizat\" Arch:


</div>

![](images/Arch_tutorial_01.jpg )

În acest tutorial, vom modela casa în 3D, pe baza desenelor 2D pe care le vom descărca de pe net și vom extrage din acestea documente 2D, cum ar fi planurile, elevațiile și secțiunile.



## Pregătirea

În loc să creați un proiect de la zero, să luăm un model de exemplu, acesta ne va economisi timp. Am ales această minunată casă a celebrului arhitect [Vilanova Artigas](http://en.wikipedia.org/wiki/Jo%C3%A3o_Batista_Vilanova_Artigas) (see a series of [pictures](http://www.leonardofinotti.com/projects/architects-second-house/image/40409-130405-010d) by Leonardo Finotti), pentru că este aproape de locul în care trăiesc, este simplu, este un exemplu minunat al uimitoarei arhitecturi moderniste din São Paulo, și desenele în format DWG sunt disponibile la [easily available](http://www.bibliocad.com/library/second-house-vilanova-artigas_72926#).

Vom folosi desene 2D DWG obținute de la link-ul de mai sus (trebuie să vă înregistrați pe site-ul de mai sus pentru a descărca, dar este gratuit, sau prinde/înhață direct o versiune DXF [here](http://yorik.uncreated.net/scripts/artigas.dxf)) ca bază de construre a modelului. So the first thing you\'ll want to do is to download the file, unzip it, and open the DWG file inside with a dwg application such as [DraftSight](http://www.3ds.com/products-services/draftsight/overview/). Alternatively, you can convert it to DXF with a free utility such as the [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter). If you have the ODA converter installed (and its path set in the Arch preferences settings), FreeCAD is also [able to import DWG files directly](Draft_DXF.md). Dar, din moment ce aceste fișiere pot fi uneori de proastă calitate și foarte grele, este de obicei mai bine să le deschideți mai întâi cu o aplicație CAD 2D și să faceți o curățare a lor.

Here, I removed all the detail drawings, all the titleblocks and page layouts, did a \"clean\" (\"purge\" in AutoCAD slang) to remove all unused entities, reorganized the sections at a logical location in relation to the plan view, and moved everything to the (0,0) point. After that, our file can be opened quite efficiently in FreeCAD. Check the different options available in Edit → Preferences → Draft → Import/Export, they can affect how (and how quickly) DXF/DWG files are imported.

This is how the file looks after being opened in FreeCAD. I also changed the thickness of the walls (the contents of the \"muros\" group), and flipped a couple of doors that were imported with wrong X scale, with the [Draft Scale](Draft_Scale.md) tool:

![](images/Arch_tutorial_02.jpg )

The [DXF importer](Draft_DXF.md) (which also takes care of DWG files, since when importing DWG files, they are simply converted to DXF first), groups the imported objects by layer. There is no layer in FreeCAD, but there are [groups](Std_Group.md). [Groups](Std_Group.md) offer a similar way to organize the objects of your files, but don\'t have specific properties, like AutoCAD layers, that apply to their contents. But they can be placed inside other groups, which is very handy. The first thing we might want to do here, is to create a new [group](Std_Group.md) in the [tree view](Document_structure.md), right-click on the document icon, add a group, right click on it to rename it as \"base 2D plans\", and drag and drop all the other objects into it.



## Construirea pereților 


<div class="mw-translate-fuzzy">

Ca și multe obiecte [Arch](Arch_Workbench.md), [walls](Arch_Wall.md) pot fi construite peste o mare varietate de obiecte: [lines](Draft_Line.md), [wires](Draft_Wire.md) (polylines), [sketches](Sketcher_Workbench.md), fațetă sau solid (sau pe nimic, caz în care sunt definite prin înălțime, lățime și lungime). The resulting geometry of the wall depends on that base geometry, and the properties you fill in, such as width and height. As you might guess, a wall based on a line will use that line as its alignment line, while a wall based on a face will use that face as its base footprint, and a wall based on a solid will simply adopt the shape of that solid. This allows about any shape imaginable to become a wall.


</div>


<div class="mw-translate-fuzzy">

There are different possible strategies to build walls in FreeCAD. One might want to build a complete \"floor plan\" with the [sketcher](Sketcher_Workbench.md), and build one, big, wall object from it. This technique works, but you can only give one thickness for all the walls of the project. Or, you can build each piece of wall from separate line segments. Or, this is what we will do here, a mix of both: We will build a couple of [wires](Draft_Wire.md) on top of the imported plan, one for each type of wall:


</div>

![](images/Arch_tutorial_03.jpg )

As you see, I\'ve drawn in red the lines that will become concrete walls (a [pictures search](http://www.google.com/search?tbm=isch&q=casa+artigas+brooklin) of the house can help you to see the different wall types), the green ones are the exterior brick walls, and the blue ones will become the inner walls. I passed the lines through the doors, because doors will be inserted in the walls later, and will create their openings automatically. Walls can also be aligned left, right or centrally on their baseline, so it doesn\'t matter which side you draw the baseline. I also took care on avoiding intersections as much as I could, because our model will be cleaner that way. But we\'ll take care of intersections later.

When this is done, place all those lines in a new [group](Std_Group.md) if you want, select each line one by one, and press the [Arch Wall](Arch_Wall.md) tool to build a wall from each of them. You can also select several lines at once. After doing that, and correcting widths (exterior walls are 25cm wide, inner walls are 15cm wide) and some alignments, we have our walls ready:

![](images/Arch_tutorial_04.jpg )

We could also have built our walls from scratch. If you press the [Arch Wall](Arch_Wall.md) button with no object selected, you will be able to click two points on the screen to draw a wall. But under the hood, the wall tool will actually draw a line and build a wall on it. In this case, I found it more didactic to show you how things work.

Did you notice that I took great care not to cross the walls? This will save us some headache later, for example if we export our work to other applications, that might not like it. I have only one intersection, where I was too lazy to draw two small line segments, and drew one big wire crossing another. This must be fixed. Fortunately, all Arch objects have a great feature: you can add one to another. Doing that will unite their geometries, but they are still editable independently after. To add one of our crossing walls to the other, just select one, CTRL + select the other, and press the [Arch Add](Arch_Add.md) tool:

![](images/Arch_tutorial_05.jpg )

On the left are the two intersecting walls, on the right the result after adding one to the other.


<div class="mw-translate-fuzzy">


{{Note|An important note about parametric objects|Something is important to consider already. As you can see, in FreeCAD, everything is parametric: Our new "united" wall is made from two walls, each based on a baseline. When you expand them in the [tree view](Document_structure.md), you can see all that chain of dependencies. As you can imagine, this little game can quickly become very complex. Furthermore, if you already know how to work with the [sketcher](Sketcher_Workbench.md), you might have wanted to draw the baselines with constrained sketches. This whole complexity has a cost: it raises exponentially the number of calculations that FreeCAD has to perform to keep your model geometry up to date. So, think about it, don't add unnecessary complexity when you don't need it. Keep a good balance between simple and complex objects, and keep these for the cases where you really need them.}}


</div>

For example, I could have drawn all my baselines above without caring about what crosses what, and fix things with the [Arch Add](Arch_Add.md) tool later. But I would have raised much the complexity of my model, for no gain at all. Better make them correct right from the start, and keeping them as very simple pieces of geometry.

Now that our walls are okay, we need to raise their height, until they intersect the roof. Then, since the wall object still cannot be cut automatically by roofs (this will happen some day, though), we will build a \"dummy\" object, that follows the shape of the roof, to be subtracted from our walls.

First, by looking at our 2D drawings, we can see that the highest point of the roof is 5.6m above the ground. So let\'s give all our walls a height of 6m, so we make sure they will be cut by our dummy roof volume. Why 6m and not 5.6m? You may ask. Well, if you already worked with boolean operations (additions, subtractions, intersections), you must already know that these operations usually don\'t like much \"face-on-face\" situations. They prefer clearly, frankly intersecting objects. So by doing this, we keep on the safe side.

To raise the height of our walls, simply select all of them (don\'t forget the one we added to the other) in the tree view, and change the value of their \"height\" property.

Before making our roof and cutting the walls, let\'s make the remaining objects that will need to be cut: The walls of the above studio, and the columns. The walls of the studio are made the same way as we did, on the superior floor plan, but they will be raised up to level 2.6m. So we will give them the needed height so their top is at 6m too, that is, 3.4m. Once this is done, let\'s move our walls up by 2.6m: Select them both, put yourself in frontal view (View → Standard Views → Front), press the [Draft Move](Draft_Move.md) button, select a first point, then enter 0, 2.6, 0 as coordinates, and press enter. Your objects now have jumped 2.6m high:

![](images/Arch_tutorial_06.jpg )


<div class="mw-translate-fuzzy">


{{Note|About coordinates|The [Draft](Draft_Workbench.md) objects, and most [Arch](Arch_Workbench.md) objects too, obey to a Draft system called [working planes](Draft_SelectPlane.md). This system defines a 2D plane where next operations will take place. If you don't specify any, that working plane adapts itself to the current view. This is why we switched to frontal view, and you see that we indicated a movement in X of 0 and in Y of 2.6. We could also have forced the working plane to stay on the ground, by using the [[Draft SelectPlane]] tool. Then, we would have entered a movement of X of 0, Y of 0 and Z of 2.6. }}


</div>

Now let\'s move our walls horizontally, to their correct location. Since we have points to snap to, this is easier: Select both walls, press the [Draft Move](Draft_Move.md) tool, and move them from one point to the other:

![](images/Arch_tutorial_07.jpg )

Finally, I changed the color of some walls to a brick-like color (so it\'s easier to differentiate), and made a small correction: Some walls don\'t go up to the roof, but stop at a height of 2.60m. I corrected the height of those walls.



## Ridicarea structurii 

Acum, deoarece va trebui să ne tăiem zidurile cu un volum de substracție, am putea vedea și dacă nu există alte obiecte care vor trebui să fie tăiate în acest fel. Există câteva coloane. Aceasta este o bună ocazie de a introduce un al doilea obiect arch(itectural): [Arch Structure](Arch_Structure.md). Obiectele structurale se comportă mai mult sau mai puțin ca pereții, dar nu sunt făcute să urmeze o linie de referință. Mai degrabă, preferă să lucreze dintr-un profil, care este extrudat (de-a lungul unei linii de profil sau nu). Orice obiect plat poate fi un profil pentru o structură, cu o singură cerință: trebuie să formeze o formă închisă.

For our columns, we will use another strategy than with the walls. Instead of \"drawing\" on top of the 2D plans, we will directly use objects from it: the circles that represent the columns in the plan view. In theory, we could just select one of them, and press the [Arch Structure](Arch_Structure.md) button. However, if we do that, we produce an \"empty\" structural object. This is because you can never be too sure at how well objects were drawn in the DWG file, and often they are not closed shapes. So, before turning them into actual columns, let\'s turn them into faces, by using the [Draft Upgrade](Draft_Upgrade.md) tool twice on them. The first time to convert them into closed wires (polylines), the second time to convert those wires into faces. That second step is not mandatory, but, if you have a face, you are 100% sure that it is closed (otherwise a face cannot be made).

After we have converted all our columns to faces, we can use the [Arch Structure](Arch_Structure.md) tool on them, and adjust the height (some have 6m, other only 2.25m height):

![](images/Arch_tutorial_08.jpg )

On the image above, you can see two columns that are still as they were in the DWG file, two that were upgraded to faces, and two that were turned into structural objects, and their height set to 6m and 2.25m.

Note that those different Arch objects (walls, structures, and all the others we\'ll discover) all share a lot of things between them (for example all can be added one to another, like we already saw with walls, and any of them can be converted to another). So it\'s more a matter of taste, we could have made our columns with the wall tool too, and converted them if needed. In fact, some of our walls are concrete walls, we might want to convert them to structures later.



## Subtracția

Acum este timpul să construim volumul de scădere. Cea mai ușoară cale va fi să-i desenezi profilul în partea superioară a vederii de secțiune.Apoi, îl vom roti și îl vom pune în poziția sa corectă. Vezi de ce am plasat secțiunile și elevațiile de genul ăsta înainte de a începe? Va fi foarte util pentru a desena lucruri acolo, apoi pentru a o muta în poziția corectă pe model.

Let\'s draw a volume, bigger than the roof, that will be subtracted from our walls. To do that, I drew two lines on top of the base of the roof, then extended them a bit further with the [Draft Trimex](Draft_Trimex.md) tool. Then, I drew a [wire](Draft_Wire.md), snapping on these lines, and going well above our 6 meters. I also drew a blue line on the ground level (0.00), that will be our rotation axis.

<img alt="" src=images/Arch_tutorial_09.jpg  style="width:1024px;">

Now is the tricky part: We will use the [Draft Rotate](Draft_Rotate.md) tool to rotate our profile 90 degrees up, in the right position to be extruded. To do that, we must first change the [working plane](Draft_SelectPlane.md) to the YZ plane. Once this is done, the rotation will happen in that plane. But if we do like we did a bit earlier, and set our view to side view, it will be hard to see and select our profile, and to know where is the basepoint around which it must rotate, right? Then we must set the working plane manually: Press the [Draft SelectPlane](Draft_SelectPlane.md) button (it is in the \"tasks\" tab of the tree view), and set it to YZ (which is the \"side\" plane). Once you set the working plane manually, like that, it won\'t change depending on your view. You can now rotate your view until you have a good view of all the things you must select. To switch the working plane back to \"automatic\" mode later, press the [Draft SelectPlane](Draft_SelectPlane.md) button again and set it to \"None\".

Now the rotation will be easy to do: Select the profile, press the [Draft Rotate](Draft_Rotate.md) button, click on a point of the blue line, enter 0 as start angle, and 90 as rotation:

<img alt="" src=images/Arch_tutorial_10.jpg  style="width:1024px;">

Now all we need to do it to move the profile a bit closer to the model (set the working plane to XY if needed), and extrude it. This can be done either with the [Part Extrude](Part_Extrude.md) tool, or [Draft Trimex](Draft_Trimex.md), which also has the special hidden power to extrude faces. Make sure your extrusion is larger than all the walls it will be subtracted from, to avoid face-on-face situations:

<img alt="" src=images/Arch_tutorial_11.jpg  style="width:1024px;">

Now, here comes into action the contrary of the [Arch Add](Arch_Add.md) tool: [Arch Remove](Arch_Remove.md). As you might have guessed, it also makes an object a child of another, but its shape is subtracted from the host object, instead of being united. So now things are simple: Select the volume to subtract (I renamed it as \"Roof volume to subtract\" in the tree view so it is easy to spot), CTRL + select a wall, and press the [Arch Remove](Arch_Remove.md) button. You\'ll see that, after the subtraction happened, the volume to subtract disappeared from both the 3D view and the tree view. That is because it has been marked as child of the wall, and \"swallowed\" by that wall. Select the wall, expand it in the tree view, there is our volume.

Now, select the volume in the tree vieew, CTRL + select the next wall, press [Arch Remove](Arch_Remove.md). Repeat for the next walls until you have everything properly cut:

<img alt="" src=images/Arch_tutorial_12.jpg  style="width:1024px;">

Remember that for both [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md), the order you select the objects is important. The host is always the last one, like in \"Remove X from Y\" or \"Add X to Y\"


{{Note|A note about additions and subtractions|Arch objects that support such additions and subtractions (all of them except the "visual" helper objects such as the axes) keep track of such objects by having two properties, respectively "Additions" and "Subtractions", that contain a list of links to other objects to be subtracted or added. A same object can be in the lists of several other objects, as it is the case of our subtraction volume here. Each of the fathers will want to swallow it in the tree view, though, so it will usually "live" in the last one. But you can always edit those lists for any object, by double-clicking it in the tree view, which in FreeCAD enters edit mode. Pressing the escape key exits edit mode.}}



## Realizarea acoperișului 

Acum, tot ce trebuie să facem pentru a finaliza structura, este de a face acoperișul și plăcile de gresie interioare mai mici.Din nou, cea mai ușoară cale este de a atrage profilurile pe partea superioară a secțiunii, cu instrumentul [Draft Wire](Draft_Wire.md). Aici am desenat 3 profile unul peste celălalt (le-am mutat separat în imaginea de mai jos pentru a se vedea mai bine). Cel verde va fi folosit pentru marginea laterală a dalei/plăcii de acoperiș, apoi cea albastră pentru părțile laterale și cele roșii pentru partea centrală care se află deasupra blocului de baie:

<img alt="" src=images/Arch_tutorial_13.jpg  style="width:1024px;">

Then, we must repeat the rotation operation above, to rotate the objects in a vertical position, then move them at their correct places, and copy some of them that will need to be extruded twice, with the [Draft Move](Draft_Move.md) tool, with the ALT key pressed, which creates copies instead of moving the current object. I also added two more profiles for the side walls of the bathroom opening.

<img alt="" src=images/Arch_tutorial_14.jpg  style="width:1024px;">

When everything is in place, it\'s just a matter of using the [Draft Trimex](Draft_Trimex.md) tool to extrude, then convert them to [Arch Structure](Arch_Structure.md) objects.

<img alt="" src=images/Arch_tutorial_15.jpg  style="width:1024px;">

After that, we can see some problems arising: two of the columns on the right are too short (they should go up to the roof), and there is a gap between the slab and the walls of the studio on the far right (the 2.60 level symbol on the section view was obviously wrong). Thanks to the parametric objects, all this is very easy to solve: For the columns, just change their height to 6m, fish your roof subtraction volume from the tree view, and subtract it to the columns. For the walls, it\'s even easier: move them a bit down. Since the subtraction volume remains at the same place, the wall geometry will adapt automatically.

Now one last thing must be fixed, there is a small slab in the bathroom, that intersects some walls. Let\'s fix that by creating a new subtraction volume, and subtract it from those walls. Another feature of the [Draft Trimex](Draft_Trimex.md) tool, that we use to extrude stuff, is that it can also extrude one single face of an existing object. This creates a new, separate object, so there is no risk to \"harm\" the other object. So we can select the base face of the small slab (look at it from beneath the model, you\'ll see it), then press the [Draft Trimex](Draft_Trimex.md) button, and extrude it up to well above the roofs. Then, subtract it from the two inner bathroom walls with the [Arch Remove](Arch_Remove.md) tool:

<img alt="" src=images/Arch_tutorial_16.jpg  style="width:1024px;">



## Podele, scări și coșul 

Acum, structura noastră este completă, avem doar câteva obiecte mai mici de făcut.



### Coșul/Șemineul

Să începem cu hornul. Acum știți deja cum funcționează, nu? Desenați două fire/polilinii închise [wires](Draft_Wire.md), mișcați - le la înălțimea corectă cu instrumentul [Draft Move](Draft_Move.md), extgrudați-le cu instrumentul [Draft Trimex](Draft_Trimex.md), transformați pe cea mai mare într-o [structure](Arch_Structure.md), și extrageți-o pe cea mai mică. Observați cum tubul de coș de fum nu a fost desenat într-o vizualizare plană, dar am găsit poziția prin tragerea de linii albastre din secțiunile de vizualizare.

<img alt="" src=images/Arch_tutorial_17.jpg  style="width:1024px;">



### Podeaua

Podelele nu sunt bine reprezentate în desenele de bază. Când vă uitați la secțiuni, nu puteți ști unde și cât de groase sunt dalele podelei. Așadar, presupunem că zidurile stau în partea superioară a blocurilor de fundație, la nivelul 0,00, și că există plăci de podea, așezate și pe acele blocuri de 15 cm grosime. Deci, plăcile de podea nu funcționează sub pereți, ci în jurul lor. Am putea face asta creând o placă dreptunghiulară mare, apoi scăzând zidurile, dar amintim că operațiile de scădere ne costă. Mai bine o faceți în bucăți mai mici, va fi \"mai ieftină\" în ceea ce privește calculul și, de asemenea, dacă o facem inteligent, cameră pe cameră, acestea vor fi, de asemenea, utile pentru a calcula suprafețele de podea mai târziu:

<img alt="" src=images/Arch_tutorial_18.jpg  style="width:1024px;">

Odată ce firele/poliliniile au fost desenate, doar le transformați în [structures](Arch_Structure.md), și le dați o înălțime de 0.15:

<img alt="" src=images/Arch_tutorial_19.jpg  style="width:1024px;">



### Scările

Acum sunt scările. Faceți cunoștință cu următoarele instrumente Arc, [Arch Stairs](Arch_Stairs.md). Acest instrument este încă într-un stadiu incipient de dezvoltare, la momentul în care scriu, deci nu vă așteptați prea mult. Dar este deja destul de util să faci scări simple și drepte. Un concept este important de știut, instrumentul de scări este gândit să construiască scări de la un pod plat până la un perete. Cu alte cuvinte, când privim dinspre partea de sus, obiectul scărilor ocupă exact spațiul pe care îl ocupă în vederea planului, astfel încât ultima contratreaptă nu este desenată (dar, desigur, este luat în considerare la calcularea înălțimilor).

In this case, I preferred to build the stairs on the section view, because we\'ll need many measurements that are easier to get from that view. Here, I drew a couple of red guidelines, then two blue lines that will be the base of our two pieces of stairs, and two green closed wires, that will form the missing parts. Now select the first blue line, press the [Arch Stairs](Arch_Stairs.md) tool, set the number of steps to 5, the height to 0.875, the width to 1.30, the structure type to \"massive\" and the structure thickness to 0.12. Repeat for the other piece.

Then, extrude both green wires by 1.30, and rotate and move them to the right position:

<img alt="" src=images/Arch_tutorial_20.jpg  style="width:1024px;">

On the elevation view, draw (then rotate) the border:

<img alt="" src=images/Arch_tutorial_21.jpg  style="width:1024px;">

Then move everything into place:

<img alt="" src=images/Arch_tutorial_22.jpg  style="width:1024px;">

Don\'t forget also to cut the column that crosses the stairs, because in BIM it\'s always bad to have intersecting objects. We are building like in the real world, remember, where solid objects cannot intersect. Here, I didn\'t want to subtract the column directly from the stairs (otherwise the column object would be swallowed by the stairs object in the tree view, and I didn\'t like that), so I took the face on which the column was built, and extruded it again. This new extrusion was then subtracted from the stairs.

Right! All the hard work is now done, let\'s go on with the very hard work!



## Uși și Ferestre 

[Arch Windows](Arch_Window.md) sunt obiecte destul de complexe. Ele sunt folosite pentru a face tot felul de obiecte \"introduse\", cum ar fi ferestrele sau ușile. Da, în FreeCAD, ușile sunt doar o fereastră specială. Și în viața reală este la fel, dacă te gândești mai bine, nu? Instrumentul [Arch Window](Arch_Window.md) poate fi în continuare un pic greu de folosit astăzi, însă considerați acest lucru drept un compromis, deoarece a fost construit pentru o putere de calcul maximă. Aproape orice fel de fereastră pe care imaginația ta o poate produce se poate face cu ea. Dar, deoarece instrumentul va câștiga mai multe presetări, această situație va deveni cu siguranță mai bună în viitor.


<div class="mw-translate-fuzzy">

The [Arch Window](Arch_Window.md) object works like this: It is based on a 2D layout, any 2D object, but preferably a [sketch](Sketcher_Workbench.md), that contains closed wires (polylines). These wires define the different parts of the window: outer frames, inner frames, glass panels, solid panels, etc. The window objects then has a property that stores what to do with each of these wires: extrude it, place it at a certain offset, etc. Finally, a window can be inserted into a host object such as a wall or structure, and it will automatically create a hole in it. That hole will be calculated by extruding the biggest wire found in the 2D layout.


</div>

There are two ways to create such objects in FreeCAD: By using a preset, or drawing the window layout from scratch. We\'ll look at both methods here. But remember that the preset method does nothing else than creating the layout object and defining the necessary extrusions for you.



### Utilizarea setărilor prealabile 

Când apăsați instrumentul [Arch Window](Arch_Window.md) fără selectarea obiectului, sunteți invitat să alegeți un aspect 2D sau să utilizați una dintre presetări. Să folosim presetarea \"ușă simplă\" pentru a plasa ușa principală de intrare a modelului nostru. Dați-i o lățime de 1m, o înălțime de 2,45m, o dimensiune W1 de 0,15m și lăsați ceilalți parametri la 0,05m. Apoi faceți clic pe colțul din stânga jos al peretelui și noua ușă este creată:

<img alt="" src=images/Arch_tutorial_23.jpg  style="width:1024px;">

You will notice that your new door won\'t appear in the tree view. That is because, by snapping to a wall, we indicated that wall as its host object. Consequently, it has been \"swallowed\" by the wall. But a right click on it → Go to selection will find it in the tree.

In this case, as our window is not inserted in any wall (the opening was there already), we might as well detach our window from its host wall. This is done by double-clicking the host wall in the tree view to enter its edit mode. There, you will see the window in its \"Subtractions\" group. Simply select the window there, press the \"remove element\" button, then \"OK\". Our window has now been removed from its host wall, and lies at the bottom of the tree view.

We have a second door, exactly the same as this one, a bit on the left. Instead of creating a new door from scratch, we have two ways to make a copy of the previous one: By using the [Draft Move](Draft_Move.md) tool, with the ALT key pressed, which, as you already know, copies an object instead of moving it. Or, even better, we can use the [Draft Clone](Draft_Clone.md) tool. The clone tool produces a \"clone\" of a selected object, that you can move around, but that retains the shape of the original object. If the original object changes, the clone changes too.

So all we need to do now is select the door, press the [Draft Clone](Draft_Clone.md) tool, then move the clone to its correct position with the [Draft Move](Draft_Move.md) tool.



### Organizarea modelului dvs 

<img alt="" src=images/Arch_tutorial_24.jpg  style="width:400px;">

Acum ar fi un moment bun pentru a face un pic de curățenie de casă. Din moment ce avem deja două ferestre, este un moment bun să facem o curățare în arborescența vizualizărilor: Creați un nou grup [Std_Group ](Std_Group.md), redenumiți-l \"windows\" și plasați cele 2 ferestre în el. De asemenea, vă recomandăm să separați alte elemente în acest fel, cum ar fi pereții și structurile. Deoarece puteți crea și grupuri [groups](Std_Group.md) în interiorul grupurilor, le puteți organiza mai departe, de exemplu prin plasarea tuturor elementelor care formează acoperișul într-un grup separat, astfel încât este ușor să activați și să dezactivați (să faceți un grup vizibil sau invizibil și să faceți același lucru cu toate obiectele din interior).


<div class="mw-translate-fuzzy">

Arhitectura [Arch Workbench](Arch_Workbench.md) are câteva instrumente suplimentare pentru a vă organiza modelul: [Arch Site](Arch_Site.md), [Arch Building](Arch_Building.md) și [Floor Arch](Arch_Floor.md). Aceste 3 obiecte se bazează pe grupul standard FreeCAD, deci se comportă exact ca grupuri, dar au și câteva proprietăți suplimentare. De exemplu, [floors](Arch_Floor.md) au capacitatea de a defini/seta și de a controla înălțimea pereților și structurii conținute și, atunci când sunt mutate, tot conținutul lor este mutat.


</div>

But here, since we have only one building with only one (and a half) floor, there is no real need to use such objects, so let\'s stick with simple groups.




Now, let\'s get back to work. Turn off the roof group, so we can see better inside, and switch the Display Mode of the floor objects to Wireframe (or use the [Draft ToggleDisplayMode](Draft_ToggleDisplayMode.md) tool) so we can still snap to them, but we can see the plan view underneath. But you can also turn off the floors completely, then place your doors at level 0, then raise them of 15cm with the [Draft Move](Draft_Move.md) tool.

Let\'s place the interior doors. Use the \"Simple Door\" preset again, make doors of 1.00m and 0.70m wide x 2.10m high, with W1 size of 0.1m. Make sure you snap to the correct wall when you place them, so they automatically create a hole in that wall. If it is hard to place them correctly, you can place them at an easier location, at the corner of the wall, for example, then move them. The \"hole\" will move together.

Dacă din greșeală ați găzduit o fereastră în peretele greșit, este ușor să remediați: Scoateți fereastra din grupul de \"scădere\" a peretelui gazdă în modul de editare, după cum am văzut mai sus, apoi adăugați-l la grupul de \"Subtracție\" în peretele corect, prin aceeași metodă sau, pur și simplu, utilizând instrumentul [Arch Remove](Arch_Remove.md).

A little work later, all our doors are there:

<img alt="" src=images/Arch_tutorial_25.jpg  style="width:1024px;">

After a closer look at the elevation view, I now detected another error: The top of the brick walls is not as 2.60m, but 17.5cm lower, that is, 2.425m. Fortunately, windows based on presets have a facility: You can alter their general dimensions (width and height) from their properties. So let\'s change their height to 2.425 - 0.15, that is, 2.275. The second window, as it is a clone of the first one, will adapt too. This is basically where the true magic of parametric design appears.

Now we can look at the really interesting stuff: How to design your own custom windows.



### Crearea de ferestre personalizate 


<div class="mw-translate-fuzzy">

Așa cum am explicat mai sus, obiectele [Arch Window](Arch_Window.md) sunt create din elemente 2D, realizate din elemente închise (fire/polilinii, cercuri, dreptunghiuri, orice). Deoarece obiectele [Draft](Draft_Workbench.md) nu pot conține mai mult de unul dintre aceste elemente, instrumentul preferat de a desena layout-uri de ferestre este [Sketcher](Sketcher_Workbench.md). Din nefericire, cu sketcher-ul, nu este posibilă fixarea unor obiecte externe, cum ar fi Atelierul de lucru Draft, care ar fi util aici, deoarece înălțimile noastre sunt deja desenate. Din fericire, există o unealtă pentru a converti obeictele Draftt într-o schiță: Instrumentul [Draft To Sketch](Draft_Draft2Sketch.md).


</div>

So, let\'s start by building our first window layout. I drew it on the elevation, using several [rectangles](Draft_Rectangle.md): One for the outer line, and 4 for the inner lines. I stopped before the door, because, remember, our door already has a frame there:

<img alt="" src=images/Arch_tutorial_26.jpg  style="width:1024px;">

Then, select all the rectangles, and press the [Draft To Sketch](Draft_Draft2Sketch.md) button (and delete the rectangles, because this tool doesn\'t delete the original objects, in case something goes wrong). Then, with the new sketch selected, press the [Arch Window](Arch_Window.md) tool:

<img alt="" src=images/Arch_tutorial_27.jpg  style="width:1024px;">

The tool will detect that the layout has one outer wire and several inner wires, and automatically proposes you a default configuration: One frame, made by subtracting the inner wires from the outer one, extruded by 1m. Let\'s change that, by entering the window\'s edit mode, by double-clicking on it in the tree view:

You will see a \"Default\" component, that has been created automatically by the Window tool, that uses the 5 wires (always subtracting the other ones from the biggest one), and has an extrusion value of 1. Let\'s change its extrusion value to 0.1, to match what we used in the doors.

Then, let\'s add 4 new glass panels, each using a single wire, and give them an extrusion of 0.01, and an offset of 0.05, so they are placed at the middle of the frame. This will be how your window looks like when you are finished:

<img alt="" src=images/Arch_tutorial_28.jpg  style="width:1024px;">

I suppose now you must have understood the power of this system: Any combination of frames and panels of any shape is possible. If you can draw it in 2D, it can exist as a full valid 3D object.

Now, let\'s draw the other pieces, then we\'ll move everything into place together. But first. we\'ll need to do some corrections to the base 2D drawing, because some lines are clearly missing, where the windows meet the stairs. We can fix that by offsetting the stairs line by 2.5cm with the [Draft Offset](Draft_Offset.md) tool (with ALT pressed of course, to copy our lines instead of moving them). Now we can draw our layout, with [wires](Draft_Wire.md), then convert them to a sketch, then making a window of it.

After doing that a couple of times (I made it in 4 separate pieces, but it\'s up to you to decide), we have our facade complete:

<img alt="" src=images/Arch_tutorial_29.jpg  style="width:1024px;">

Now, as before, it\'s just a matter of rotating the pieces, and moving them to their correct position:

<img alt="" src=images/Arch_tutorial_30.jpg  style="width:1024px;">

Last missing piece, there is a segment of wall that didn\'t appear on the plan view, that we need to add. We have several options for that, I chose to draw a line on the ground plane, then move it up to the correct height, then create a wall from it. Then, we also need to fish up our roof subtraction volume (it must have stayed in the last column), then subtract it. Now this side of the building is ready:

<img alt="" src=images/Arch_tutorial_31.jpg  style="width:1024px;">

Ready? Not quite. Look at the image above, we did our doors with a 5cm frame, remember (it was the default from the preset). But the other windows have 2.5cm frames. This needs to be fixed.



### Editarea ferestrelor 

Am văzut deja cum să construim și să actualizăm componentele ferestrei, prin modul de editare al ferestrei, dar putem de asemenea să editați schița care stă la baza. Ferestrele prestabilite nu diferă de ferestrele personalizate, instrumentul [Arch Window](Arch_Window.md) a creat doar schița de bază. Selectați obiectul de ușă (originalul, nu copia, amintiți-vă, am făcut o clonă) și l-ați extins în vizualizarea arborescentă. Există schița noastră. Faceți dublu clic pe acesta pentru a intra în modul de editare.


<div class="mw-translate-fuzzy">

the [Sketcher Workbench](Sketcher_Workbench.md) is an extremely powerful tool. It doesn\'t have some of the [Draft](Draft_Workbench.md) conveniences, such as snapping or working planes, but it has many other advantages. In FreeCAD you will frequently use one or another depending on the need. The most important feature of the sketcher is constraints. Constraints allow you to automatically fix the position of some elements relative to others. For example, you can force a segment to always be vertical, or to always be at a certain distance to another.


</div>

When we edit our door sketch, we can see that it is made on a fully constrained sketch:

<img alt="" src=images/Arch_tutorial_32.jpg  style="width:1024px;">

Now all we need to do is edit the 5cm distances between the outer line and the inner line, by double-clicking them, and changing their value to 2.5cm (Remember, the units are still not fully functional at the time I\'m writing this). After clicking the \"OK\" button, our door (and its clone) have been updated.



## Lucrul fără sprijin 2D 

Pana acum munca noastra a fost relativ usoara, pentru ca am avut desenele 2D subiacente care ne-au pus bazele lucrarii. Dar acum trebuie să facem fațada opusă și atriul de sticlă și lucrurile devin din ce în ce mai complicate: desenul fațadei opuse are multe lucruri greșite, nu reprezintă deloc atriul și pur și simplu nu avem desen pentru interiorul pereții din atrium. Așadar, va trebui să inventăm câteva lucruri noi înșine. Asigurați-vă că ați aruncat o privire la [imagini de referință](http://www.pedrokok.com.br/2010/02/residencia-artigas-sao-paulo-sp/img_8265-533px/) pentru a afla cum se fac lucrurile. Sau faceți așa cum doriți!

One thing we can already do: duplicate the complicated stairs window with the [Draft Move](Draft_Move.md) tool, because it is equal on both sides:

<img alt="" src=images/Arch_tutorial_33.jpg  style="width:1024px;">

Note that here, I preferred to duplicate with the [Draft Move](Draft_Move.md) tool instead of using a [clone](Draft_Clone.md), because the clone currently doesn\'t support different colors inside objects. The difference is that the clone is a copy of the final shape of the original object, while if you copy an object, you create a new object and give it all the same properties as the original one (therefore, also its base sketch and its window components definition, which are both stored as properties).

Now we must attack the parts that are not drawn anywhere. Let\'s start with the glass wall between the sitting room and the atrium. It\'ll be easier to draw it on the elevation view, because we\'ll get the correct height of the roof. Once you are in plan view, you can rotate the view from the menu View → Standard Views → Rotate left or right, until you get a comfortable view to work, like this:

<img alt="" src=images/Arch_tutorial_34.jpg  style="width:1024px;">

Note how on the image above, I made a line from the model to the left section, to get the exact width of the window. Then, I reproduced that width on the elevation view and divided it into 4 pieces. Then I built one main window piece, plus 4 additional windows for the sliding doors. The sketcher sometimes has difficulties with overlapping wires, that\'s why I preferred to keep them separated like this:

<img alt="" src=images/Arch_tutorial_35.jpg  style="width:1024px;">

After the necessary rotations, everything clicks perfectly into place:

<img alt="" src=images/Arch_tutorial_36.jpg  style="width:1024px;">

We still need some corner piece there. A little useful trick with the [Draft SelectPlane](Draft_SelectPlane.md) tool, if you have a face selected when you press the button, the working plane matches this face (at least its position, and if the face is rectangular, it also tries to match its axes). This is useful to draw 2D objects directly on the model, such as here, we can draw a rectangle to be extruded directly at its correct position:

<img alt="" src=images/Arch_tutorial_37.jpg  style="width:1024px;">

Then let\'s do the two remaining pieces. One is easy, it is a copy of what\'s on the other side, so we can simply use the 2D drawing:

<img alt="" src=images/Arch_tutorial_38.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

The other one is a bit tricky, by looking at the pictures, we see that it has many vertical divisions, like the stairs windows. By chance (or very good design from Vilanova Artigas), the width of our window, of 4.50m, is exactly the same as the stairs window, so we can use the exact same division: 15 pieces of 30cm. Here I used the [Draft Array](Draft_Array.md) tool to copy over the two lines 15 times,and drew rectangles on top of them:


</div>

<img alt="" src=images/Arch_tutorial_39.jpg  style="width:1024px;">

Once this is done, we can create our window with the same method we already know. Another small useful trick, in case you haven\'t found it yourself already: When editing a window, if you change the name of a component, it actually creates a duplicate of it. So to create the 15 inner glass panels, instead of clicking 15 times the \"add\" button and fill 15 times the data, you can just keep editing one, and change its name and wire, it will create a copy each time.

After the window is rotated and moved into place, the atrium is complete:

<img alt="" src=images/Arch_tutorial_40.jpg  style="width:1024px;">



## Editări și rezolvări 

Acum, când ne uităm la elevația noastră din spate și o comparăm cu planul, vedem că există unele diferențe care trebuie rezolvate. Și anume, ferestrele dormitorului sunt mai mici decât am crezut prima dată și va trebui să adăugăm niște pereți. Pentru a face acest lucru în mod corespunzător, unele etaje trebuie să fie tăiate:

<img alt="" src=images/Arch_tutorial_41.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

We have of course several ways to do that, making a subtraction volume would be an easy way, but it would add unnecessary complexity to the model. Better to edit the base wire of each floors. This is where the [Draft Edit](Draft_Edit.md) mode comes into action. By expanding these floors in the tree view, then making their base wire visible, we can then double-click them to enter edit mode. There, we can move their points, or add or remove points. With this,editing our floor plates becomes easy.


</div>

<img alt="" src=images/Arch_tutorial_42.jpg  style="width:1024px;">

After some more sweat (the person who made those drawings obviously became pretty lazy when did this last elevation, much is drawn wrong), we finally have our complete house:

<img alt="" src=images/Arch_tutorial_43.jpg  style="width:1024px;">

Note the chimney tube, which is made from a circle I used to make a hole in the chimney block, that I extruded, then converted into a tube with the [Part Offset](Part_Offset.md) tool.


{{Note|Problems in objects|Sometimes an object you made can have problems. For example, the object it was based onto has been deleted, and the object can therefore not recalculate its shape. These are usually shown to you by a little red sign on their icon, and/or a warning in the output window. There is no generic recipe to fix these problems, because they can have many origins. But, the easiest way to solve them is often to delete them, and, if you didn't delete their base objects, recreate them.}}



## Rezultat

Acum, după toată munca grea prin care am trecut pentru a construi acest model, vine recompensa: Ce putem face cu ea? Practic, acesta este marele avantaj al colaborării cu BIM, toate modelele noastre arhitecturale tradiționale, cum ar fi desene 2d (planuri, secțiuni etc.), randări și calcule (facturi de cantități etc.) pot fi extrase din model. Și, chiar mai bine, regenerată de fiecare dată când modelul se schimbă. Vă voi arăta aici cum să obțineți aceste documente diferite.



### Pregătiri

Înainte de a începe să exportați diverse chestii, este interesant de luat în considerarea un lucru: după cum ați văzut, modelul nostru devine din ce în ce mai complex, cu o mulțime de relații între obiecte. Acest lucru poate face operațiuni ulterioare de calcul subsecvente, cum ar fi tăierea prin model, dificile. O modalitate rapidă de a \"simplifica\" în mod drastic modelul dvs., este să eliminați toate aceste complexități, exportându-le pe formatul [STEP](http://en.wikipedia.org/wiki/ISO_10303-21). Acest format vă va păstra toată geometria, dar va renunța la toate relațiile și construcțiile parametrice, păstrând doar forma finală. Când reimportați acel fișier STEP în FreeCAD, veți obține un model care nu mai are nicio relație și o dimensiune mult mai mică a fișierului. Gândiți-vă la acesta ca la un fișier \"de ieșire\", pe care îl puteți regenera oricând din fișierul \"master\":

<img alt="" src=images/Arch_tutorial_44.jpg  style="width:1024px;">



### Exportul fișierelor IFC și alte aplicații 

<img alt="" src=images/Arch_tutorial_45.jpg  style="width:400px;">

Unul dintre lucrurile fundamentale de care aveți nevoie atunci când lucrați cu BIM este de a putea să importați și să exportați [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) files. Aceasta este încă o lucrare în desfășurare în FreeCAD. Formatul [ IFC](Arch_IFC.md) este deja acceptat și importul fișierelor IFC în FreeCAD este deja destul de fiabil. Exportul este încă experimental și are în prezent numeroase limitări. Cu toate acestea, lucrurile se îmbunătățesc continuu și ar trebui să obținem exportul adecvat al IFC foarte curând.

[IFC export](Arch_IFC.md) requires very little setup, once the necessary software libraries are installed. You only need to recreate the building structure, which is needed in all IFC files, by adding an [Arch Building](Arch_Building.md) to your file, then an [Arch Floor](Arch_Floor.md), then moving all the groups of objects that compose your model in it. Make sure you leave your construction geometry (all the 2D stuff we\'ve been drawing) out of it to avoid making your IFC file unnecessarily heavy.

Another thing to set, is to check the \"Role\" property of structural elements. Since IFC has no \"generic\" structural element, like FreeCAD, we need to assign them roles (column, beam, etc\...) so the exporter knows what element to create in the IFC file.

In this case, we need our whole architectural system, so the IFC exporter can know if an object must be exported as a wall or a column, so we are using our \"master\" model, not our \"output\" model.

Once this is done, simply select your building object, and choose the \"Industry Foundation Classes\" format. Exporting to non-BIM applications, such as [Sketchup](http://www.sketchup.com/) is also easy, you have several export formats at your disposal, such as [Collada](Arch_DAE.md), STEP, IGES ou OBJ.






### Randarea


<div class="mw-translate-fuzzy">

FreeCAD include, de asemenea, un modul de randare, [Raytracing Workbench](Raytracing_Workbench.md). Acest suport de lucru acceptă în prezent două motoare de randare, [PovRay](http://www.povray.org/) și [LuxRender](http://www.luxrender.net). Deoarece FreeCAD nu este proiectat pentru randarea imaginilor, caracteristicile pe care le oferă Atelierul de lucru Raytracing sunt oarecum limitate. Cea mai bună cale de acțiune atunci când doriți să faceți redarea corectă este să exportați modelul într-un format bazat pe plasă, cum ar fi OBJ sau STL, și să-l deschideți într-o aplicație mai potrivită pentru randare, cum ar fi \[http: // www. blender.org blender\]. Imaginea de mai jos a fost redată cu motorul ciclurilor blenderului:


</div>

<img alt="" src=images/Arch_tutorial_47.jpg  style="width:1024px;">

But, for a quick rendering, the Raytracing workbench can already do a good job, with the advantage of being very easy to setup, thanks to its templates system. This is a rendering of our model fully made within FreeCAD, with the Luxrender engine, using the \"indoor\" template.

<img alt="" src=images/Arch_tutorial_48.jpg  style="width:1024px;">

The Raytracing workbench still offers you very limited control over materials, but lighting and environments are defined in templates, so they can be fully customized.



### Desene 2D 

Desigur, cea mai importantă utilizare a BIM este să producă automat desene 2D. Acest lucru se face în FreeCAD cu instrumentul [Arch SectionPlane](Arch_SectionPlane.md). Acest instrument vă permite să plasați un obiect plan de secțiune în vizualizarea 3D, pe care îl puteți orienta pentru a produce planuri, secțiuni și elevații. Planurile de secțiune trebuie să știe ce obiecte trebuie să ia în considerare, așa că odată ce le-ați creat, trebuie să adăugați obiecte cu ajutorul instrumentului [Arch Add](Arch_Add.md). Puteți adăuga obiecte individuale sau, mai convenabil, un grup, un podea sau o clădire întreagă. Acest lucru vă permite să modificați cu ușurință domeniul de aplicare a unui anumit plan de secțiune mai târziu, adăugând sau eliminând obiecte în / din grupul respectiv. Orice modificare a acestor obiecte se reflectă în vizualizările produse de planul secțiunii.

The section plane automatically produces cut views of the objects it intersects. In other words, to produce views instead of sections, you just need to place the section plane outside of your objects.

<img alt="" src=images/Arch_tutorial_49.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

The section planes can produce two different outputs: [shape](Part_Workbench.md) objects, that live in the same document as your 3D model, or [drawing views](Drawing_Workbench.md), that are made to use on a drawing sheet produced by the [Drawing workbench](Drawing_Workbench.md). Each of these behave differently, and has its own advantages.


</div>

**Vederea formelor**


<div class="mw-translate-fuzzy">

Această ieșire este produsă utilizând instrumentul [Draft Shape2DView](Draft_Shape2DView.md) cu un plan de secțiune selectat. Efectuați o vizualizare 2D a modelului direct în spațiul 3D, ca în imaginea de mai sus. Principalul avantaj aici este că puteți lucra la ele folosind instrumentele [ Draft](Draft_Workbench.md) (sau orice alt instrument standard al FreeCAD), astfel încât să puteți adăuga texte, dimensiuni, simboluri etc:


</div>

<img alt="" src=images/Arch_tutorial_50.jpg  style="width:1024px;">

On the image above, two [Shape2D views](Draft_Shape2DView.md) have been produced for each section, one showing everything, the other showing only the cut lines. This allows us to give it a different line weight, and turn hatching on. Then, dimensions, texts and symbols have been added, and a couple of DXF blocks have been imported to represent the furniture. These views are then easy to export to DXF or DWG, and open in your favorite 2D CAD application, such as [LibreCAD](http://www.librecad.org) or [DraftSight](http://www.3ds.com/products-services/draftsight/overview/), where you can work further on them:

<img alt="" src=images/Arch_tutorial_51.jpg  style="width:1024px;">

Note that some features are still not supported by the [DXF/DWG exporter](Draft_DXF.md) so the result in your 2D application might differ a bit. For example, in the image above, I had to redo the hatching, and correct the position of some dimension texts. If you place your objects in different groups in FreeCAD, these become layers in your 2D CAD application.

**ArchViews**

The other kind of output that can be produced from [section planes](Arch_SectionPlane.md) are [TechDraw ArchViews](TechDraw_ArchView.md). This method has one big limitation compared to the previous one: you have limited possibilities to edit the results, and at the moment, things like dimensioning or hatching are still not natively supported.

On the other hand, the final output being easier to manipulate, and the graphical possibilities of the SVG format being huge, in the future, undoubtedly this will be the preferred method. At the moment, though, you\'ll get better results using the previous one.

<img alt="" src=images/Arch_tutorial_52.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

On the image above, the geometry is the direct output of the section plane, but some other Draft objects have been added, such as dimensions and hatched polygons, and another view object with same scale and offset values has been produced from them with the [Draft Drawing](Draft_Drawing.md) tool. In the future, such operations will be done directly on the Drawing page, leaving your model totally clean.


</div>



### Extragerea cantităților 


<div class="mw-translate-fuzzy">

Aceasta este o altă sarcină foarte importantă care trebuie efectuată pe modelele BIM. În FreeCAD, lucrurile arată bine încă de la început, deoarece kernelul OpenCasCade al FreeCAD are deja grijă de calculul lungimilor, zonelor și volumelor pentru toate formele pe care le produce. Deoarece toate obiectele [Arch](Arch_Workbench/ro.md) sunt solide, aveți întotdeauna garanția că veți putea obține un volum din ele.


</div>

**Using spreadsheets**

To populate a spreadsheet with values extracted from the model the Arch_Schedule tool can be used.

![](images/Arch_schedule_example03.jpg )

**The survey mode**

O altă modalitate de a vă cerceta modelul și de a extrage valorile este să utilizați modul [Arch Survey](Arch_Survey.md). În acest mod, puteți face clic pe puncte, muchii, fețe sau faceți dublu clic pentru a selecta obiecte întregi și veți obține valorile altitudinii, lungimii, zonei sau volumului, afișate pe model, imprimate pe fereastra de ieșire FreeCAD și copiate în clipboard, astfel încât să puteți alege și lipi cu ușurință valorile într-o altă aplicație deschisă

<img alt="" src=images/Arch_tutorial_54.jpg  style="width:1024px;">



## Concluzii


<div class="mw-translate-fuzzy">

Sper că acest lucru vă oferă o imagine de ansamblu asupra instrumentelor disponibile, asigurați-vă că vă referiți la documentația pentru Atelierul [Arch Workbench](Arch_Workbench.md) sau Atelierul [Draft Workbench](Draft_Workbench.md) pentru informații suplimentare (există mai multe instrumente pe care nu le-am menționat aici), și, în general, cu restul [FreeCAD documentation](Main_Page.md). Vizitați și [forum](http://forum.freecadweb.org), multe probleme pot fi de obicei rezolvate acolo în cel mai scurt timp, și urmați-mă pe [blog](http://yorik.uncreated.net/guestblog.php?tag=freecad) pentru noutăți despre dezvoltarea Atelierului Arch .


</div>


<div class="mw-translate-fuzzy">

Fișierul creat pe durata acestui tutorial poate fi găsit la [here](http://yorik.uncreated.net/archive/freecad/casa_artigas.fcstd)


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch tutorial/ro
