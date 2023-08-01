---
- TutorialInfo:/ro
   Topic: Drafting
   Level: Beginner
   Time: 20 minutes
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16 or above
   Files:
---

# Draft tutorial/ro




<div class="mw-translate-fuzzy">




</div>




<div class="mw-translate-fuzzy">

### Introducere

Acest îndrumător este menit să deprindă utilizatorul cu elementele de bază ale unui flux de operaţii bazat pe [Panoul Ciornă (Draft)](Draft_Workbench/ro.md), printre care se numără crearea de profile, folosirea planurilor active, crearea dimensiunilor de cotare, textelor şi notelor. Acest îndrumător foloseşte notarea **(X, Y, Z)** pentru desemnarea coordonatelor necesare pentru definirea diferitelor puncte într-un obiect.


</div>

This tutorial was originally written by Drei, and it was rewritten and illustrated by vocx.

This tutorial is meant to introduce the reader to the basic workflow of the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md).

The reader will practice:

-   creation of lines, arcs, and polygons
-   the use of working planes
-   the creation of dimensions, text, and shapestrings
-   the creation of a technical drawing

This tutorial uses the notation {{Value|(x, y, z)}} to denote the coordinates required to define points in an object. The default unit is millimeters {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Final drawing including various Draft objects.*




<div class="mw-translate-fuzzy">

### Cerinţe

-   FreeCAD versiunea 0.16 sau anterioară
-   Cititorul cunoaşte cum se folosesc *tab*-urile **Date** şi **Vedere** pentru a schimba proprietăţile unui element atunci când doreşte acest lucru.


</div>

1\. Open FreeCAD, create a new empty document with **File → [<img src=images/Std_New.svg style="width:16px"> [New](Std_New.md)**.

:   1.1. Switch to the [Draft Workbench](Draft_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **View → Workbench → [<img src=images/Workbench_Draft.svg style="width:16px"> Draft**.
:   1.2. Make sure you understand how to use the [property editor](property_editor.md), particularly the **Data** and **View** tabs to change the properties. When changing properties, you may have to do a **<img src="images/Std_Refresh.svg" width=16px> [Std Refresh](Std_Refresh.md)** action to see the result in the [3D view](3D_view.md).
:   1.3. Since the Draft objects are planar shapes, they are better viewed from the top. Use **[<img src=images/Std_ViewTop.svg style="width:16px"> [View top](Std_ViewTop.md)** to set the [3D view](3D_view.md).
:   1.4. Although it is not used in this tutorial, the Draft grid is helpful to position geometrical elements. Use **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [SelectPlane](Draft_SelectPlane.md)** to set both the working plane and the grid, and then show and hide the grid with **[<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Toggle grid](Draft_ToggleGrid.md)**.




<div class="mw-translate-fuzzy">

### Cum se procedează 

Este obligatoriu să vă asigurați că bara de instrumente **Ciornă Ancorare** (Draft Snap toolbar) va fi disponibilă pentru utilizare pe parcursul operaţiilor din acest îndrumător.


</div>


<div class="mw-translate-fuzzy">

1.  Porniţi **FreeCAD**.
2.  Dacă nu ați deschis un nou document FreeCAD (cea mai mare parte a ferestrei FreeCAD se prezintă ca fiind gri), din meniul derulant, faceți clic pe Fișier, apoi pe Nou sau faceți clic pe instrumentul **Creați un document nou** ![ 32px](images/_Document-new.svg ).
3.  Activați panoul **Ciornă** (Draft );
4.  Selectați meniul **Editare**;
5.  Faceți clic pe **Preferințe**;
6.  Mergeți la **Ciornă** (Draft ) și selectați tab-ul **Grilă și ancorare** (Grid and snapping);
7.  Verificați dacă bara de instrumente **Arată bara Ciornă Ancorare** (Show Draft Snap toolbar) este activă.


</div>


<div class="mw-translate-fuzzy">

Rețineți că puteți modifica vizibilitatea **Grilei** din acest meniu, în cazul în care doriți să o dezactivați.


</div>




<div class="mw-translate-fuzzy">

#### Folosirea planelor 

Planele sunt folosite pentru a delimita efectul uneltelor din **Ciornă** la un anumit plan, evitând astfel problemele cu localizarea punctelor și curbelor în piesele complexe. Planele pot să se refere la axele sistemului de coordonate **(XY, YZ, \...)** sau pot să folosească o suprafață plană din document ca referință.


</div>

Most Draft objects are planar shapes so they are naturally based on a **working plane**. A working plane can be one of the main XY, XZ, and YZ global coordinate planes, or it can be a plane that is parallel to them with a positive or negative offset, or it can be a plane defined by the face of a solid object.


<div class="mw-translate-fuzzy">

1.  Selectați <img alt="" src=images/Draft_SelectPlane.png  style="width:32px;"> [ Alegeţi planul de lucru](Draft_SelectPlane.md). Acesta poate fi localizat în **Bara de unelte Panou Ciornă** sau în **Meniul Ciornă** din secţiunea **Unelte pentru crearea de ciorne**.
2.  Selectați planul **XY**.


</div>

Before pressing the button, you can also change the value of the offset in millimeters, as well as the grid spacing, the main lines and snapping radius.




<div class="mw-translate-fuzzy">

##### Linii și Arce 

1.  Selectați ![](images/Draft_Arc.png ) [Arc](Draft_Arc.md).
2.  Setați **centrul** la **(0, 0, 0)**.
3.  Setați **raza** la 30 mm.
4.  **Unghiul de pornire** este de 60,0°.
5.  **Deschiderea** este de 60,0°.


</div>


<div class="mw-translate-fuzzy">

Repetați procedeul pentru trasarea unui al doilea arc cu o rază de 25 mm. Celelalte proprietăți rămân neschimbate.


</div>


<div class="mw-translate-fuzzy">

1.  Selectaţi ![](images/Draft_Line.png ) [Linie](Draft_Line/ro.md).
2.  Îndreptaţi-vă către **capătul** oricărui arc. Când cursorul Dvs. <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> se va apropia de punctul de terminare, la apropierea de el, punctul va deveni alb.
3.  Selectaţi capătul celuilalt arc şi uniţi.
4.  Repetaţi operaţia în cealaltă parte a arcelor.


</div>

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Closed profile created by two arcs and two lines.*

## Fusing or compounding 


<div class="mw-translate-fuzzy">

Acum avem mai multe curbe care descriu un profil, însă acesta nu este recunoscut ca o entitate de sine stătătoare. Se poate continua lucrul cu elementele nemodificate, totuşi în acest caz vom prefera să le unim într-un singur obiect.


</div>


<div class="mw-translate-fuzzy">

1.  Selectaţi un arc şi o linie în timp ce apăsaţi tasta **CTRL**
2.  Daţi clic pe ![](images/Draft_Upgrade.png ) [Actualizare](Draft_Upgrade/ro.md)


</div>

6b. If you wish to maintain the parametric nature of the objects you can create a compound instead.

:   6b.1. Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).
:   6b.2. With these objects selected, click on **[<img src=images/Part_Compound.svg style="width:16px"> [Part Compound](Part_Compound.md)**.




<div class="mw-translate-fuzzy">

##### Plane, dreptunghiuri şi cercuri 

1.  Daţi clic pe ![](images/Draft_Rectangle.png ) [Dreptunghi](Draft_Rectangle/ro.md)
2.  Setaţi coordonatele primului punct la **(-100, -60, 0)**
3.  Setaţi coordonatele celui de-al doilea punct la **(140, 90, 0)**


</div>

7\. We will draw a rectangular frame. (Switch back to the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [ Draft Workbench](Draft_Workbench.md).)

:   7.1. Press **[<img src=images/Draft_Rectangle.svg style="width:16px"> [Rectangle](Draft_Rectangle.md)**.
:   7.2. Enter the values of the first point {{Value|(-100, -60, 0)}}, and press **Enter**.
:   7.3. Make sure the **Relative** option is unchecked, as we will use absolute units. You may press **R** in the keyboard to quickly toggle this option on and off.
:   7.4. Enter the values for the second point {{Value|(140, 90, 0)}}, and press **Enter**.


<div class="mw-translate-fuzzy">

Rezultatul este un **Plan**. Aspectul lui pot fi modificat prin clic dreapta: dacă doriţi înlăturarea **suprafeţei de umplere**, schimbaţi **Stil de desenare** în **Cadru cu linii** (Wireframe).


</div>


<div class="mw-translate-fuzzy">

1.  Selectaţi ![](images/Draft_Circle.png )
2.  Setaţi coordonatele centrului la **(0, 0, 0)**
3.  Setaţi raza ca 15 mm


</div>


<div class="mw-translate-fuzzy">

##### Polygons

1.  Selectaţi ![](images/Draft_Polygon.png ) [Poligon](Draft_Polygon/ro.md)
2.  Punctul central este localizat la **(0, 0, 0)**.
3.  Setaţi raza la 50 mm.
4.  Selectaţi ca număr de laturi 6.


</div>

Again, you may change the **Make Face** and **Display Mode** properties in the [property editor](property_editor.md) if you want.

The rectangle, the circle, the polygon, and most other objects created with the [Draft Workbench](Draft_Workbench.md) share many data and view properties because they are derived from the same base class, [Part Part2DObject](Part_Part2DObject.md).

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Rectangle, circle and polygon added.*




<div class="mw-translate-fuzzy">

##### Matrici (tablouri) 

Matricile sunt folosite pentru a replica un obiect de mai multe ori pe o direcție, după o axă de rotație sau de-a lungul unei căi.

1.  Selectaţi **Cablul** creat anterior
2.  Daţi clic pe <img alt="" src=images/Draft_Array.png  style="width:32px;"> [Matrici](Draft_Array/ro.md)
3.  În tab-ul **Date** al objectului, schimbaţi tipul matricii din **orto** în **polar**
4.  Schimbaţi **Numărul polar** din 1 în 3


</div>

Arrays are used to replicate an object several times in an orthogonal direction (X, Y, Z), around a revolution axis, or along a path.

10\. We will create a polar array.

:   10.1. Select the {{Value|Wire}} object that was previously created with the **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Upgrade](Draft_Upgrade.md)** tool, or the {{Value|Compound}} created with the **[<img src=images/Part_Compound.svg style="width:16px"> [Part Compound](Part_Compound.md)** tool.
:   10.2. Press **[<img src=images/Draft_PolarArray.svg style="width:16px"> [PolarArray](Draft_PolarArray.md)**.
:   10.3. Adjust the polar angle to {{Value|360°}}.
:   10.4. Set the number of elements to {{Value|4}}.
:   10.5. Enter the values for the center of rotation {{Value|(0, 0, 0)}}, and press **Enter**.

The array object shows copies of the object around the origin.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width:" height="400px;"> 
*Polar array of the small profile centered around the origin.*




<div class="mw-translate-fuzzy">

#### Adăugaţi dimensiunile de cotare 

Dimensiunile de cotare necesită o utilizare constantă a **ancorării constrângerilor** pentru a selecta corect punctele pe care doriți să le folosiţi la dimensionare. Pentru a schimba selectarea punctelor posibile, se va utiliza bara de instrumente **Ancorare**.


</div>

Linear dimensions work best when using the appropriate [Draft Snap](Draft_Snap.md) methods to select points and edges to measure. However, they can also be created by specifying absolute coordinates.


<div class="mw-translate-fuzzy">

1.  Selectați ![](images/Draft_Dimension.png ) [Dimension](Draft_Dimension.md)
2.  Selectați primul punct. Acesta poate să fie un element existent, fie specificat de coordonate. Pentru acest tutorial, primul punct va fi întotdeauna la **(0, 0, 0)**
3.  Selectați al doilea punct. Abordați punctul de mijloc al liniei de sus a poligonului. Un punct alb trebuie să apară lângă această pictogramă <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;">
4.  Mutați cursorul în locația dorită a dimensiunii și dați clic pe ea.
5.  Schimbați dimensiunea fontului în **View** tab la 6 mm


</div>


<div class="mw-translate-fuzzy">

Repetați procesul pentru arcuri de cerc și cercuri.


</div>

13\. Repeat the process for the circle located in the center. The first point of the measurement will still be the origin. To select the second point make sure **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Toggle snap](Draft_Snap_Lock.md)** is active, and only **[<img src=images/Draft_Snap_Angle.svg style="width:16px"> [Angle](Draft_Snap_Angle.md)** as well. As you move the pointer to the top of the circle, the <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> [Angle](Draft_Snap_Angle.md) icon should appear; click to select this point. Then move the cursor to the right, and click to fix the dimension.

Remember to adjust the **Font Size**, and other properties to see the dimension correctly.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width:" height="400px;"> 
*Dimensions that measure the vertical distance from the origin to the top of the circle, arcs, and polygon.*




<div class="mw-translate-fuzzy">

#### Adnotări şi text 

Între cele două, există doar o diferență de nuanţă : textul oferă un profil ce poate fi utilizat pentru a efectua modelări 3D.


</div>


<div class="mw-translate-fuzzy">

##### Annotations

1.  Selectaţi ![](images/Draft_Text.png ) [Text](Draft_Text/ro.md)
2.  Selectaţi punctul de referinţă în **Vedere 3D**. In acest caz, este punctul de mijloc al arcului de sus.
3.  Introduceţi textul şi apăsaţi tasta **Enter**. Repetaţi pentru fiecare linie de text pe care doriţi s-o introduceţi.
4.  Ca să terminaţi, apăsaţi tasta **Enter** de două ori.


</div>


<div class="mw-translate-fuzzy">

##### Text

1.  Selectaţi <img alt="" src=images/Draft_ShapeString.png  style="width:32px;"> [ShapeString](Draft_ShapeString/ro.md)
2.  Selectaţi punctul de referinţă în **Vederea 3D View**. Acesta poate fi un punct existent sau dat de poziţia curentă a cursorului.
3.  Introduceţi textul şi apăsaţi tasta **Enter**.
4.  Setaţi mărimea literelor.
5.  Păstraţi **urma** (tracking) de 0 mm
6.  Selectaţi **calea de acces** către fişierul tipului de font pe care doriţi să-l folosiţi (dacă lăsaţi gol, se va folosi **fontul implicit**)


</div>

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:" height="400px;"> 
*Text and ShapeString objects added.*

To extrude letters and engrave them on to solids, see the [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md).




<div class="mw-translate-fuzzy">

#### Crearea planşelor 

Pentru a realiza planşe, este necesară crearea unei pagini **Desenare** cu elementele pe care doriţi să le folosiţi. Vă rugăm să citiţi [Îndrumător pentru Desenare](Drawing_tutorial/ro.md) pentru o descriere detaliată.


</div>

As it is now, the objects that we have created can be saved, exported to other formats like [SVG](SVG.md) or [DXF](DXF.md), or printed.

If you wish, you may create a technical drawing to display these objects together with additional information like a frame.

Before doing anything, hide the Draft grid by pressing **[<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Toggle  grid](Draft_ToggleGrid.md)**.

16\. Switch to the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

:   16.1. Create a standard page by pressing **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw PageDefault](TechDraw_PageDefault.md)**.
:   16.2. In the [tree view](tree_view.md) select all objects created, except for the Page, and then press **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [TechDraw ActiveView](TechDraw_ActiveView.md)**. Press **OK** with the default options; it may take a few seconds to create the view in the page.
:   16.3. Selecting the Page object in the [tree view](tree_view.md) will automatically display the Page in the main window. With the Page selected, go to the [property editor](Property_editor.md), and change **Scale** to {{Value|0.75}}.
:   16.4. Expand the Page object in the [tree view](tree_view.md) to select the ActiveView object. With this view selected, go to the [property editor](Property_editor.md), and change **Scale Type** to {{Value|Page}}.
:   16.5. Recompute the model by using **[<img src=images/Std_Refresh.svg style="width:16px"> [Refresh](Std_Refresh.md)** or pressing **F5**.
:   16.6. Hide the frames of the objects by pressing **[<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [TechDraw ToggleFrame](TechDraw_ToggleFrame.md)**.

Learn more about the [TechDraw Workbench](TechDraw_Workbench.md) by reading the [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:" height="400px;"> 
*TechDraw page with a projection of the shapes created with the Draft Workbench.*

TechDraw works best with objects that have a [Part TopoShape](Part_TopoShape.md). Since some objects from Draft, like [Draft Texts](Draft_Text.md) and [Draft Dimensions](Draft_Dimension.md), don\'t have such \"[shapes](Shape.md)\", some operations of TechDraw don\'t work with these elements.

Tools like **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [TechDraw ActiveView](TechDraw_ActiveView.md)**, **[<img src=images/TechDraw_DraftView.svg style="width:16px"> [TechDraw DraftView](TechDraw_DraftView.md)**, and **[<img src=images/TechDraw_ArchView.svg style="width:16px"> [TechDraw ArchView](TechDraw_ArchView.md)** work by receiving an internal SVG image that is generated by internal Draft functions; therefore, TechDraw doesn\'t have much control about how these views are displayed. More integration of Draft and TechDraw is a work in progress.




<div class="mw-translate-fuzzy">

Aici se termină şirul de operaţii elementare ce pot fi realizate cu [panoul Ciornă (Draft)](Draft_Workbench/ro.md).


</div>

The [Draft Workbench](Draft_Workbench.md) in many ways is similar to the [Sketcher Workbench](Sketcher_Workbench.md), as both are intended to produce 2D shapes. The main difference is in the way each workbench handles coordinate systems, and how the objects are positioned. In Draft, objects are freely positioned in the global coordinates system, usually snapping their points to a grid, or to other objects. In Sketcher, a \"[sketch object](Sketch.md)\" defines a local coordinate system which serves as the reference for all geometrical elements within that sketch. Moreover, the sketch relies on \"constraints\" to define the final position of its points.

-   The [Draft Workbench](Draft_Workbench.md) is intended for 2D drawings which are suitable to be drawn on a grid. The [Arch Workbench](Arch_Workbench.md) mostly builds on top of the tools defined in the [Draft Workbench](Draft_Workbench.md).

-   The [Sketcher Workbench](Sketcher_Workbench.md) is intended for 2D drawings that require precise relationships between its points. It does not rely on a grid, but on rules of positioning (constraints) to determine where the points and edges will be placed. The [Sketcher Workbench](Sketcher_Workbench.md) is mostly used together with the [PartDesign Workbench](PartDesign_Workbench.md) for the creation of solid [bodies](Body.md).

-   It is possible to transform a Draft object into a [Sketch](Sketch.md), and the other way around, using the **[<img src=images/Draft_Draft2Sketch.svg style="width:16px"> [Draft Draft2Sketch](Draft_Draft2Sketch.md)** tool.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft tutorial/ro
