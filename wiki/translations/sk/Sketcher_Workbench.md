# <img alt="ikona pracovného stola Náčrtník" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/sk






## Úvod


<div class="mw-translate-fuzzy">

<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Pracovný stôl Náčrtník](Sketcher_Workbench.md) sa vo FreeCADe používa na tvorbu 2D geometrie, ktorú následne využijete v <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [na pracovnom stole Dizajn dielca](PartDesign_Workbench.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [pracovnom stole Arch](Arch_Workbench.md) a iných pracovných stoloch. Vo všeobecnosti sa za východiskový bod pre väčšinu CAD modelov považuje 2D náčrt, pretože ten dokážeme „vytiahnuť" a vytvoriť tak 3D tvar; navyše je možné 2D náčrty okrem predtým vytvorených 3D tvarov použiť aj na vytvorenie ďalších prvkov, ako sú kapsy, ryhy alebo výlisky. Spolu s booleanovskými operáciami definovanými na <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [pracovnom stole Diel](Part_Workbench.md) tvorí Náčrtník základ [konštruktívnej geometrie telies](constructive_solid_geometry.md) (CSG) - spôsobu tvorby telies. Okrem toho s operáciami <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [pracovného stola Dizajn dielu](PartDesign_Workbench.md) tvorí Náčrtník tiež základ metodológie [úpravy prvkov](feature_editing.md) pri tvorbe telies.


</div>

Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), the Sketcher Workbench, or \"The Sketcher\" for short, forms the basis of the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) method of building solids. Together with <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, it also forms the basis of the [feature editing](Feature_editing.md) methodology of creating solids. But many other workbenches use sketches as well.


<div class="mw-translate-fuzzy">

Pracovný stôl Náčrtník obsahuje \"väzby\", vďaka ktorým dokážete pomocou presných geometrických definícií ako dĺžky, uhla a vzťahov (vodorovnosť, zvislosť, kolmosť atď.) určiť umiestnenie 2d tvarov. Riešiteľ väzieb vypočíta rozsah väzieb 2D geometrie a poskytuje interaktívne prehliadanie stupňov voľnosti náčrtu.


</div>


<div class="mw-translate-fuzzy">

Náčrtník neslúži na tvorbu 2D výkresov. Akonáhle boli náčrty použité na vytvorenie prvku telesa, sú automaticky skryté. Väzby sú viditeľné iba v upravovacom režime náčrtu.


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Plne zaväzbený náčrt*

## Constraints


<div class="mw-translate-fuzzy">

Namiesto rozmerov sú väzby používané na obmedzenie stupňov voľnosti objektu. Napríklad čiara bez väzieb má 4 stupne voľnosti (skrátene SV, angl. DOF): môže byť posúvaná vodorovne alebo zvislo, môže byť natiahnutá a môže byť otočená.


</div>

Použitie vodorovnej alebo zvislej väzby alebo väzby uhla čiary (vzhľadom na inú čiaru alebo jednu z osí) obmedzí jej schopnosť otáčania, takže jej zostanú 3 stupne voľnosti. Zamknutie jedného z jej dvoch bodov vzhľadom na začiatok súradníc odstráni ďalšie 2 stupne voľnosti. A nakoniec použitie väzby rozmeru odstráni posledný stupeň voľnosti. Po týchto úkonoch je čiara považovaná za \"plne zaväzbenú\".


<div class="mw-translate-fuzzy">

Objekty môžu byť takisto zaväzbené medzi sebou. Dve čiary môžete spojiť pomocou jedného z ich bodov vďaka väzbe splynutia bodov. Môže takisto medzi nimi byť nastavený úhol, alebo môžu nastavené ako kolmé. Čiara môže byť dotyčnicou oblúka alebo kruhu apod. Komplexný náčrt s viacerými objektami bude mať viac možných riešení a jeho \"plné zaväzbenie\" znamená, že bolo dosiahnuté práve jedno z týchto možných riešení v závislosti od použitých väzieb.


</div>


<div class="mw-translate-fuzzy">

Existujú dva typy väzieb: geometrické a rozmerové. Sú opísané nižšie v časti [\'Nástroje\'](#Nástroje.md).


</div>

### Edit constraints 

When a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, and if the **Ask for value after creating a dimensional constraint** [preference](Sketcher_Preferences#Display.md) is selected (default), a dialog opens to edit its value.

![](images/Sketcher_Edit_Constraint.png )

You can enter a numerical value or an [expression](Expressions.md), and it is possible to name the constraint to facilitate its use in other expressions. You can also check the **Reference** checkbox to switch the constrain to [reference mode](Sketcher_ToggleDrivingConstraint.md).

To edit the value of an existing dimensional constraint do one of the following:

-   Double-click the constraint value in the [3D view](3D_view.md).
-   Double-click the constraint in the [Sketcher Dialog](Sketcher_Dialog.md).
-   Right-click the constraint in the Sketcher Dialog and select the **Change value** option from the context menu.

### Reposition constraints 

Dimensional constraints can be repositioned in the 3D view by dragging. Hold down the left mouse button over the constraint value and move the mouse. The symbols of geometric constraints are positioned automatically and cannot be moved.

## Profile sketches 

To create a sketch that can be used as a profile for generating solids certain rules must be followed:

-   The sketch must contain only closed contours. Gaps between endpoints, however small, are not allowed.
-   Contours can be nested, to create voids, but should not self-intersect or intersect other contours.
-   Contours cannot share edges with other contours. Duplicate edges must be avoided.
-   T-connections, that is more than two edges sharing a common point, or a point touching an edge, are not allowed.

These rules do not apply to construction geometry (default color blue), which is not shown outside edit mode, or if the sketch is used for a different purpose. Depending on the workbench and the tool that will use the profile sketch, additional restrictions may apply.

## Drawing aids 

The Sketcher Workbench has several drawing aids and other features that can help when creating geometry and applying constraints.

### Continue modes 

There are two continue modes: **Geometry creation \"Continue Mode\"** and **Constraint creation \"Continue Mode\"**. If these are checked (default) in the [preferences](Sketcher_Preferences#Display.md), related tools will restart after finishing. To exit a continuous tool press **Esc** or the right mouse button. This must be repeated if a continuous geometry tool has already received input. You can also exit a continuous tool by starting another geometry or constraint creation tool. Note that pressing **Esc** if no tool is active will exit sketch edit mode. Uncheck the **Esc can leave sketch edit mode** [preference](Sketcher_Preferences#General.md) if you often inadvertently press **Esc** too many times.

### Auto constraints 

In sketches that have **Auto constraints** checked (default) several constraints are applied automatically. The icon of a proposed automatic constraint is shown next to the cursor when it is placed correctly. Left-Clicking will then apply that constraint. This is a per-sketch setting that can be changed in the [Sketcher Dialog](Sketcher_Dialog#Constraints.md) or by changing the **Autoconstraints** [property](Property_editor.md) of the sketch.

The following constraints are applied automatically:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincident](Sketcher_ConstrainCoincident.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangent](Sketcher_ConstrainTangent.md)

-    <small>(v1.0)</small> : <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) (line midpoint)

### Snapping


<small>(v0.21)</small> 

It is possible to [snap](Sketcher_Snap.md) to grid lines and grid intersection, to edges of geometry and midpoints of lines and arcs, and to certain angles. Please note that snapping does not produce constraints in and of itself. For example, only if [Auto constraints](#Auto_constraints.md) is switched on will snapping to an edge produce a [Point on object constraint](Sketcher_ConstrainPointOnObject.md). But just picking a point on the edge would then have the same result.

### On-View-Parameters 


<small>(v1.0)</small> 

Depending on the selected option in the [preferences](Sketcher_Preferences#General.md) only the dimensional On-View-Parameters or both the dimensional and the positional On-View-Parameters can be enabled. Positional parameters allow the input of exact coordinates, for example the center of a circle, or the start point of a line. Dimensional parameters allow the input of exact dimensions, for example the radius of a circle, or the length and angle of a line. On-View-Parameters are not available for all tools.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Determining the center point of a circle with the positional parameters enabled*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Determining the radius of a circle with the dimensional parameters enabled*

If values are entered and confirmed by pressing **Enter** or **Tab**, related constraints are added automatically. If two parameters are displayed at the same time, for example the X and Y coordinate of a point, it is possible to enter one value and pick a point to define the other. Depending on the object additional constraints may be required to fully constrain it. Constraints resulting from On-View-Parameters take precedence over those that may result from [Auto constraints](Sketcher_Dialog#Constraints.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arc created by entering all On-View-Parameters with resulting automatically created constraints*

### Coordinate display 

If the **Show coordinates beside cursor while editing** [preference](Sketcher_Preferences#Display.md) is checked (default), the parameters of the current geometry tool (coordinates, radius, or length and angle) are displayed next to the cursor. This is deactivated while On-View-Parameters are shown.

## Selection methods 

While a sketch is in edit mode the following selection methods can be used:

### 3D view element selection 

As elsewhere in FreeCAD, an element can be selected in the [3D view](3D_view.md) with a single left mouse click. But there is no need to hold down the **Ctrl** key when selecting multiple elements. Holding down that key is possible though and has the advantage that you can miss-click without losing the selection. Edges, points and constraints can be selected in this manner.

### 3D view box selection 

Box selection in the 3D view works without using [Std BoxSelection](Std_BoxSelection.md) or [Std BoxElementSelection](Std_BoxElementSelection.md):

1.  Make sure that no tool is active.
2.  Do one of the following:
    -   Click in an empty area and drag a rectangle from left to right to select elements that lie completely inside the rectangle.
    -   Click in an empty area and drag a rectangle from right to left to also select elements that touch or cross the rectangle.

You can box-select edges and points, constraints cannot be box-selected.

### 3D view connected geometry selection 


<small>(v1.0)</small> 

Double-clicking an edge in the 3D view will select all edges directly and indirectly connected with that edge via endpoints. There is no need for the edges to be connected with [Coincident constraints](Sketcher_ConstrainCoincident.md), endpoints need only have the same coordinates.

### Sketcher Dialog selection 

Edges and points can also be selected from the Elements section of the [Sketcher Dialog](Sketcher_Dialog.md), and constraints from the Constraints section of that dialog.

## Copy, cut and paste 


<small>(v1.0)</small> 

The standard keyboard shortcuts, **Ctrl**+**C**, **Ctrl**+**X** and **Ctrl**+**V**, can be used to copy, cut and paste selected Sketcher geometry including related constraints. But these tools are also available from the **Sketch → Sketcher tools** menu. They can be used within the same sketch but also between different sketches or separate instances of FreeCAD. Since the data is copied to the clipboard in the form of Python code, it can be used in other ways too (e.g. shared on the forum).



## Nástroje


<div class="mw-translate-fuzzy">

Nástroje pracovného stola Náčrtník sa nachádzajú v menu Náčrt, ktoré sa objaví po nahraní pracovného sola Náčrtník.


</div>

Some tools are also available from the [3D view](3D_view.md) context menu while a sketch is in edit mode, or from the context menus of the [Sketcher Dialog](Sketcher_Dialog.md).


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.



### Všeobecné

#### Sketcher toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Nový náčrt](Sketcher_NewSketch.md): Vytvorí nový náčrt na vybranej ploche alebo rovine. Ak nie je pri spustení tohto nástroja vybraná žiadna plocha, užívateľ je vyzvaný zvoliť si z vyskakovacieho okna želanú rovinu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Upraviť náčrt](Sketcher_EditSketch.md): Úprava zvoleného náčrtu. Otvorí sa [dialógové okno Náčrtníka](Sketcher_Dialog.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Namapovať náčrt na plochu](Sketcher_MapSketch.md): Namapuje náčrt na predtým vybranú plochu alebo teleso.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Preorientovať náčrt](Sketcher_ReorientSketch.md): Umožní vám naviazať náčrt na jednu z hlavných rovín.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Skontrolovať náčrt](Sketcher_ValidateSketch.md): Skontroluje toleranciu jednotlivých bodov a upraví ich.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Zlúčiť náčrty](Sketcher_MergeSketches.md): Zlúči dva alebo viac náčrtov.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Zrkadliť náčrt](Sketcher_MirrorSketch.md): Zrkadlí náčrt podľa osy x, y alebo podľa začiatku súradníc.


</div>

#### Sketcher Edit Mode toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Opustiť náčrt](Sketcher_LeaveSketch.md): Ukončí režim úprav náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [Zobraziť náčrt](Sketcher_ViewSketch.md): Nastaví zobrazenie modelu kolmo na rovinu náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Zobraziť rez](Sketcher_ViewSection.md): Vytvorí reznú rovinu a dočasne skryje akýkoľvek materiál nachádzajúci sa pred reznou rovinou.


</div>

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Zastaviť operáciu](Sketcher_StopOperation.md): V režime úprav zastaví aktuálnu operáciu, napr. kreslenie, nastavovanie väzieb apod.


</div>



### Geometria v Náčrtníku 

Tu sú uvedené nástroje pre tvorbu objektov.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Bod](Sketcher_CreatePoint.md): Nakreslí bod.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Lomená čiara (čiara s viacerými bodmi)](Sketcher_CreatePolyline.md): Nakreslí čiaru zloženú z viacerých segmentov. Pri kreslení lomenej čiary a stláčaní klávesy **M** preskakujete medzi jednotlivými štýlmi lomených čiar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Čiara](Sketcher_CreateLine.md): Nakreslí čiarový segment medzi 2 bodmi. Pre potreby niektorých väzieb sa čiary považujú za nekonečne dlhé.


</div>

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Oblúk](Sketcher_CreateArc.md): Nakreslí segment oblúka pomocou stredového bodu, polomeru a začiatočného a koncového uhla.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Oblúk podľa 3 bodov](Sketcher_Create3PointArc.md): Nakreslí segment oblúka pomocou dvoch koncových bodov a ďalšieho bodu na obvode.


</div>

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Creates an arc of ellipse.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Creates an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Creates an arc of parabola.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle/ellipse:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Kruh](Sketcher_CreateCircle.md): Nakreslí kruh pomocou stredového bodu a polomeru.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Kruh podľa 3 bodov](Sketcher_Create3PointCircle.md): Nakreslí kruh pomocou troch bodov na jeho obvode.


</div>

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Creates an ellipse by its center, an endpoint of one of its axes, and a point along the ellipse. <small>(v1.0)</small> : Or by both endpoints of one of its axes and a point along the ellipse.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Creates an ellipse by the endpoints of one of its axes and a point along the ellipse. <small>(v1.0)</small> : This is the same tool as [Ellipse by center](Sketcher_CreateEllipseByCenter.md) but with a different initial mode.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Obdĺžnik](Sketcher_CreateRectangle.md): Nakreslí obdĺžnik pomocou 2 protiľahlých bodov.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Vycentrovaný obdĺžnik](Sketcher_CreateRectangle_Center.md): Nakreslí obĺdžnik pomocou stredového bodu a rohového bodu. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Zaoblený obĺdžnik](Sketcher_CreateOblong.md): Nakreslí zaoblený obĺdžnik z dvoch protiľahlých bodov. <small>(v0.20)</small> 


</div>

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Trojuholník](Sketcher_CreateTriangle.md): Nakreslí pravidelný trojuholník vpísaný do kružnice v konštrukčnej geometrii.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Štvorec](Sketcher_CreateSquare.md): Nakreslí pravidelný štvorec vpísaný do kružnice v konštrukčnej geometrii.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Päťuholník](Sketcher_CreatePentagon.md): Nakreslí pravidelný päťuholník vpísaný do kružnice v konštrukčnej geometrii.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Šesťuholník](Sketcher_CreateHexagon.md): Nakreslí pravidelný šesťuholník vpísaný do kružnice v konštrukčnej geometrii.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Sedemuholník](Sketcher_CreateHeptagon.md): Nakreslí pravidelný sedemuholník vpísaný do kružnice v konštrukčnej geometrii.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Osemuholník](Sketcher_CreateOctagon.md): Nakreslí pravidelný osemuholník vpísaný do kružnice v konštrukčnej geometrii.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Vytvoriť pravidelný mnohouholník](Sketcher_CreateRegularPolygon.md): Nakreslí pravidelný mnohouholník pomocou voľby počtu strán a výberom dvoch bodov: stredu a jedného rohu.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Drážka](Sketcher_CreateSlot.md): Nakreslí ovál pomocou stredu jedného polkruhu a koncového bodu druhého polkruhu.


</div>

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): Creates an arc slot. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Creates a B-spline curve by control points. <small>(v1.0)</small> : Or by knot points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Creates a periodic (closed) B-spline curve by control points. <small>(v1.0)</small> : This is the same tool as [B-spline by control points](Sketcher_CreateBSpline.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Creates a B-spline curve by knot points. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Creates a periodic (closed) B-spline curve by knot points. Idem.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Konštrukčný režim](Sketcher_ToggleConstruction.md): Prepne geometriu náčrtu z/do konštrukčného režimu. Konštrukčná geometria je sfarbená na modro a mimo režim úprav náčrtu je neviditeľná.


</div>



### Väzby v Náčrtníku 


<div class="mw-translate-fuzzy">

Väzby sa používajú na definovanie dĺžok, nastavenie pravidiel medzi súčasťami náčrtu a na ukotvenie náčrtu vzhľadom na vodorovnú a zvislú os. Niektoré väzby vyžadujú [Pomocné väzby](Sketcher_helper_constraint.md).


</div>

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): Is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Vodorovná vzdialenosť](Sketcher_ConstrainDistanceX.md): Nastaví vodorovnú vzdialenosť medzi dvomi bodmi alebo koncovými bodmi čiary. Ak je vybraný len jeden objekt, je vzdialenosť nastavená voči začiatku súradníc.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Zvislá vzdialenosť](Sketcher_ConstrainDistanceY.md): Nastaví zvislú vzdialenosť medzi dvomi bodmi alebo koncovými bodmi čiary. Ak je vybraný len jeden objekt, je vzdialenosť nastavená voči začiatku súradníc.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Vzdialenosť](Sketcher_ConstrainDistance.md): Definuje vzdialenosť vybranej čiary zaväzbením jej dĺžky, alebo definuje vzdialenosť medzi dvomi bodmi zaväzbením ich vzájomnej vzdialenosti.


</div>

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Fixes the radius of arcs and B-spline weight circles, and the diameter of circles.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Polomer](Sketcher_ConstrainRadius.md): Zaväzbí polomer vybraného oblúka alebo kruhu určením jeho konkrétnej hodnoty.
-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Priemer](Sketcher_ConstrainDiameter.md): Zaväzbí priemer vybraného oblúka alebo kruhu určením jeho konkrétnej hodnoty.
-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [ Automatické zaväzbenie polomeru/priemeru](Sketcher_ConstrainRadiam.md): Automaticky definuje polomer/priemer vybraného oblúka alebo kruhu (váhu riadiaceho bodu B-spline krivky, priemer kompletného kruhu, polomer oblúka) <small>(v0.20)</small> 
-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Uhol](Sketcher_ConstrainAngle.md): Definuje interný uhol medzi dvomi vybranými čiarami.


</div>

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Fixes the diameter of circles and arcs.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Fixes the angle between two edges, the angle of a line with the horizontal axis of the sketch, or the aperture angle of a circular arc.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Zámok](Sketcher_ConstrainLock.md): Zaväzbí vybraný objekt nastavením jeho zvislej a vodorovnej vzdialenosti od začiatku súradníc, čím v podstate uzamkne umiestnenie objektu. Tieto väzobné vzdialenosti je možné následne upraviť.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): Creates a coincident constraint between points, fixes points on edges or axes, or creates a concentric constraint. It combines the [Coincident](Sketcher_ConstrainCoincident.md) and [Point on object](Sketcher_ConstrainPointOnObject.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Splynutie](Sketcher_ConstrainCoincident.md): Pripojí bod na jeden alebo viacero iných bodov.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Bod na objekt](Sketcher_ConstrainPointOnObject.md): Pripojí bod na iný objekt typu čiara, oblúk alebo os.


</div>

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Horizontal/vertical constraints:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer.md): Constrains lines or pairs of points to be horizontal or vertical, whichever is closest to the current alignment. It combines the [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Vodorovná väzba](Sketcher_ConstrainHorizontal.md): Zaväzbí vybrané čiary alebo elementy lomených čiar do presne vodorovnej polohy. Pred aplikovaním tejto väzby môžete vybrať jeden alebo viac objektov.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Zvislá väzba](Sketcher_ConstrainVertical.md): Zaväzbí vybrané čiary alebo elementy lomených čiar do presne zvislej polohy. Pred aplikovaním tejto väzby môžete vybrať jeden alebo viac objektov.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Rovnobežná väzba](Sketcher_ConstrainParallel.md): Zaväzbí dve alebo viac číar tak, aby boli rovnobežné.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Kolmá väzba](Sketcher_ConstrainPerpendicular.md): Zaväzbí dve čiary tak, aby boli na seba kolmé, alebo zaväzbí čiaru kolmo na koncový bod oblúka.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Väzba dotyčnice](Sketcher_ConstrainTangent.md): Medzi dvomi vybranými objektami vytvorí väzbu dotyčnice, alebo kolineárnu väzbu medzi dvomi čiarovými segmentami. Čiarový segment nemusí nutne ležať priamo na oblúku alebo kruhu, aby mohol s týmto oblúkom alebo kruhom vytvárať väzbu dotyčnice.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Väzba zhodnosti](Sketcher_ConstrainEqual.md): Zaväzbí dva vybrané objekty tak, aby boli zhodné. Ak ju použijete na kruhy alebo oblúky, ich polomery sa budú zhodovať.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Väzba symetrie](Sketcher_ConstrainSymmetric.md): Zaväzbí dva body symetricky k čiare, alebo zaväzbí prvé dva vybrané body symetricky k tretiemu vybranému bodu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Blokovacia väzba](Sketcher_ConstrainBlock.md): Zablokuje hranu a znemožní jej posun, to znamená, že neumožní jej vrcholom zmeniť umiestnenie. Hodí sa napríklad na ukotvenie pozície B-Spline kriviek. Viď [príspevok na fóre o blokovacej väzbe](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Snellov zákon](Sketcher_ConstrainSnellsLaw.md): Zaväzbí dve čiary tak, aby dodržiavali zákon lomu a simulovali prechod svetla cez optické rozhranie.


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Toggle constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Prepnúť riadiacu/referenčnú väzbu](Sketcher_ToggleDrivingConstraint.md): Prepne lištu nástrojov alebo zvolenú väzbu do/z referenčného stavu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Aktivovať/dekativovať väzbu](Sketcher_ToggleActiveConstraint.md): Zapne alebo vypne už umiestnenú väzbu. <small>(v0.19)</small> 


</div>



### Nástroje Náčrtníka 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet/chamfer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Zaoblenie](Sketcher_CreateFillet.md): Medzi dvomi čiarami spojenými bodom vytvorí zaoblenie. Vyberte obe čiary alebo rohový bod a potom aktivujte nástroj.


</div>

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chamfer](Sketcher_CreateChamfer.md): creates a chamfer between two non-parallel edges. This is the same tool as [Fillet](Sketcher_CreateFillet.md) but with a different initial mode. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Orezanie](Sketcher_Trimming.md): Oreže čiaru, kruh alebo oblúk podľa zvoleného bodu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Rozdelenie](Sketcher_Split.md): Rozdelí čiaru alebo oblúk na dve časti, premení kruh na oblúk pri zachovaní väčšiny väzieb. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Predĺženie](Sketcher_Extend.md): Predĺži čiaru alebo oblúk až po hraničnú čiaru, oblúk, elipsu, oblúk elipsy alebo bod v priestore.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Vonkajšia geometria](Sketcher_External.md): Vytvorí hranu spojenú s vonjakšou geometriou.


</div>

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Presná kópia](Sketcher_CarbonCopy.md): Skopíruje geometriu iného náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Vybrať začiatok súradníc](Sketcher_SelectOrigin.md): Vyberie začiatok súradníc náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Vybrať vodorovnú os](Sketcher_SelectHorizontalAxis.md): Vyberie vodorovnú os náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Vybrať zvislú os](Sketcher_SelectVerticalAxis.md): Vyberie zvislú os náčrtu.


</div>

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): Rotates or optionally creates rotated copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Creates equidistant edges around selected edges. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symetria](Sketcher_Symmetry.md): Skopíruje element náčrtu symetricky ku zvolenej čiare.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Odstrániť zarovnanie k osám](Sketcher_RemoveAxesAlignment.md): Odstráni zarovnanie k osám a zároveň sa pokúsi zachovať vzťah väzieb výberu. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Zmazať všetku geometriu](Sketcher_DeleteAllGeometry.md): Zmaže všetku geometriu v náčrte.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Zmazať všetky väzby](Sketcher_DeleteAllConstraints.md): Zmaže všetky väzby z náčrtu.


</div>

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).



### Nástroje B-spline kriviek Náčrtníka 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Konvertovať geometriu na B-spline krivku](Sketcher_BSplineApproximate.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Zvýšiť stupeň B-spline krivky](Sketcher_BSplineIncreaseDegree.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Znížiť stupeň B-spline krivky](Sketcher_BSplineDecreaseDegree.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Zvýšiť násobnosť uzla](Sketcher_BSplineIncreaseKnotMultiplicity.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Znížiť násobnosť uzla](Sketcher_BSplineDecreaseKnotMultiplicity.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into a B-spline or increases the multiplicity of an existing knot.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Creates a B-spline by joining two existing B-splines or other edges. <small>(v0.21)</small> 

### Sketcher visual 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Select solver DOFs](Sketcher_SelectElementsWithDoFs.md): Zelenou farbou označí geometrické elementy, pri ktorých riešiteľ stále ukazuje nezaväzbené stupne voľnosti.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Vybrať väzby](Sketcher_SelectConstraints.md): Vyberie väzby elementu náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Vybrať elementy spojené s väzbami](Sketcher_SelectElementsAssociatedWithConstraints.md): Vyberie elementy náčrtu spojené s väzbami.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Vybrať nadbytočné väzby](Sketcher_SelectRedundantConstraints.md): Vyberie nadbytočné väzby náčrtu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Vybrať konfliktné väzby](Sketcher_SelectConflictingConstraints.md): Vyberie konfliktné väzby náčrtu.


</div>

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): Shows or hides the circular helpers (underlying virtual circles) for arcs in all sketches. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Zobraziť/skryť stupeň B-spline krivky](Sketcher_BSplineDegree.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Zobraziť/skryť kontrolný polygón B-spline krivky](Sketcher_BSplinePolygon.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Zobraziť/skryť hrebeň zakrivenia B-spline krivky](Sketcher_BSplineComb.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Zobraziť/skryť násobnosť uzla B-spline krivky](Sketcher_BSplineKnotMultiplicity.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Zobraziť/skryť váhu kontrolných bodov B-spline krivky](Sketcher_BSplinePoleWeight.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Zobraziť/skryť vnútornú geometriu](Sketcher_RestoreInternalAlignmentGeometry.md): Znovu vytvorí chýbajúcu/zmaže nepotrebnú vnútornú geometriu vybraného kruhu, oblúka elipsy/hyperboly/paraboly alebo B-spline krivky.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Prepnúť virtuálny priestor](Sketcher_SwitchVirtualSpace.md): Umožní vám skryť všetky väzby náčrtu a potom ich znovu zobraziť.


</div>

### Obsolete tools 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Klon](Sketcher_Clone.md): Vytvorí klon elementu náčrtu s prepojením na originál.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Uzavrieť tvar](Sketcher_CloseShape.md): Vytvorí uzavretý tvar aplikovaním väzieb splynutia na koncové body.


</div>

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their corner point. Not available in <small>(v1.0)</small> .


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Spojiť hrany](Sketcher_ConnectLines.md): Spojí elementy náčrtu aplikovaním väzieb splynutia na koncové body.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Kópia](Sketcher_Copy.md): Vytvorí kópiu elementu náčrtu bez prepojenia na originál.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Presun](Sketcher_Move.md): Presunie vybranú geometriu podľa posledného vybraného bodu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Obdĺžnikové pole](Sketcher_RectangularArray.md): Vytvorí pole z vybraných elementov náčrtu.


</div>



## Predvoľby


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Predvoľby](Sketcher_Preferences.md): Predvoľby pracovného stola \"Náčrtník\".


</div>




<div class="mw-translate-fuzzy">

## Osvedčené postupy 


</div>


<div class="mw-translate-fuzzy">

Každý CAD používateľ si priebežne vytvára vlastný pracovný postup, ale existujú určité osvedčené postupy, ktoré je dobré zachovávať.


</div>


<div class="mw-translate-fuzzy">

-   Séria jednoduchých náčrtov sa spravuje ľahšie, ako jeden komplexný náčrt. Napríklad prvý náčrt môžete vytvoriť pre základný 3D prvok (napríklad pomocou vytiahnutia alebo obtočenia), zatiaľ čo druhý môžete použiť na vytvorenie dier alebo výrezov (kapies). Niektoré detaily môžete vynechať a vytvoriť ich neskôr ako 3D prvky. Môžete v náčrte takisto vynechať zaoblenia, ak ich obsahuje príliš veľa, pričom ich neskôr pridáte ako 3D prvky.
-   Vždy vytvárajte uzavretý profil, inak z vášho náčrtu nebudete môcť vytvoriť teleso, ale iba súbor otvorených plôch. Ak nechcete, aby boli niektoré objekty zahrnuté do tvorby telesa, zmeňte ich pomocou nástroja Konštrukčný režim na konštrukčné elementy.
-   Aby ste nemuseli všetky väzby vytvárať manuálne, môžete na niektoré elementy použiť ich automatické vytváranie.
-   Vo všeobecnosti platí, že najprv by ste mali aplikovať geometrické väzby, potom väzby rozmerov a na koniec celý náčrt uzamknúť. Ale zapamätajte si: pravidlá sú často na to, aby sa porušovali. Ak máte problém manipulovať s náčrtom, môže byť vhodné niektoré objekty zaväzbiť, než celý náčrt dokončíte.
-   Ak sa dá, vycentrujte náčrt k začiatku súradníc (0,0) pomocou väzby Zámok. Ak náčrt nie je symetrický, zaväzbite jeden z jeho bodov k začiatku súradníc, alebo si pre väzby vzdialeností zvoľte okrúhle čísla. Vo verzii 0.12 nie sú externé väzby (umožňujúce zaväzbiť náčrt k existujúcej 3D geometrii, ako napríklad hranám či iným náčrtom) ešte implementované. To znamená, že naviazanie geometrie náčrtu k predchádzajúcemu náčrtu musíte vykonať manuálne nastavením vzdialeností od predchádzajúceho náčrtu. Väzba zámku (25,75) od začiatku súradníc sa určite pamätá lepšie, než (23.47,73.02).
-   Ak máte možnosť výberu medzi väzbou dĺžky a väzbami vodorovnej/zvislej vzdialenosti, použite radšej tie druhé. Väzby vodorodnej a zvislej vzdialenosti sä výpočetne jednoduchšie.
-   Vo všeobecnosti sú najlepšie väzby tieto: vodorovná a zvislá vzdialenosť, vodorovná a zvislá dĺžka, dotyčnica bod-na-bod. Ak je to možné, obmedzte použitie týchto väzieb: všeobecná väzba dĺžky; dotyčnica hrana-na-hranu; väzba bodu na čiaru; väzba symetrie.
-   Ak máte pochybnosti o platnosti náčrtu po jeho ukončení (prvky sú vysvietené nazeleno), zavrite dialógové okno Náčrtníka, prepnite sa na <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [pracovný stôl Dielec](Part_Workbench.md) a spustite príkaz **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Skontrolovať geomegriu](Part_CheckGeometry.md)**.


</div>



## Návody


<div class="mw-translate-fuzzy">

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php) od autora chrisb. Toto je 70-stranový PDF dokument, ktorý slúži ako detailný návod na použitie Náčrtníka. Vysvetľuje základy použitia Náčrtníka a poskytuje veľa detailov o tvorbe geometrických tvarov a všetkých druhov väzieb.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) pre začiatočníkov
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimálne požiadavky na náčrt a úplné určenie náčrtu.


</div>



## Skriptovanie

Stránka [Skriptovanie v Náčrtníku](Sketcher_scripting.md) obsahuje príklady vytvárania väzieb pomocou skriptov v jazyku Python.

## Examples

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/sk
