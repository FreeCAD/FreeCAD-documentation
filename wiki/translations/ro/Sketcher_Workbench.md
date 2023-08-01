# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/ro






## Introducere


<div class="mw-translate-fuzzy">

Atelierul [Sketcher Workbench](Sketcher_Workbench.md) este utilizat pentru a crea forme geometrice 2D cu intenția de a le utiliza în Atelierul [PartDesign Workbench](PartDesign_Workbench.md), [Arch Workbench](Arch_Workbench.md), și alte ateliere. În general, o geometrie 2D este considerată punctul de plecare pentru majoritatea modelelor CAD, deoarece o schiță 2D poate fi \"extrudată\" pentru a crea o formă 3D; mai mult, schițele 2D pot fi folosite pentru a crea alte caracteristici cum ar fi cavități, creste sau extrudări peste formele 3D construite anterior. Împreună cu operațiile booleene pe solide definite în [Part Workbench](Part_Workbench.md), Sketcher-ul formează nucleul de design generativ al formei solide.


</div>


<div class="mw-translate-fuzzy">

Atelierul de lucru Sketcher pune pe primul loc "constrângerile" - permițând definirea formelor 2D după criterii geometrice precise. Un solver matematic de constrângeri calculează nivelul constrângerii și permite explorarea interactivă a gradelor de libertate.


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*A fully constrained sketch*

## Basics of constraint sketching 


<div class="mw-translate-fuzzy">

## Elementele de bază ale constrângerilor schiței 

Pentru a explica cum funcționează Sketcher-ul, poate fi util să îl comparați cu modul tradițional de redactare.


</div>

#### Traditional Drafting 


<div class="mw-translate-fuzzy">

#### Schițarea tradițională 

Modul tradițional de schițare CAD moștenește de la vechea [drawing board](http://en.wikipedia.org/wiki/Drawing_board). [Vizualizări ortogonale (2D)](http://en.wikipedia.org/wiki/Multiview_orthographic_projection) sunt desenate manual și sunt destinate pentru realizarea desenelor tehnice (cunoscute și sub denumirea de planuri). Obiectele sunt desenate exact la dimensiunea sau dimensiunea dorită. Dacă doriți să desenați o linie orizontală cu lungimea de 100 mm începând cu (0,0), activați instrumentul Linie, faceți clic pe ecran sau introduceți coordonatele (0,0) pentru primul punct, apoi efectuați un al doilea clic sau introduceți coordonatele celui de-al doilea punct la (100,0). Sau vă veți trage linia fără a ține seama de poziția sa și o veți muta ulterior. După ce ați terminat desenarea geometriei, adăugați dimensiuni acestora.


</div>

#### Constraint Sketching 


<div class="mw-translate-fuzzy">

#### Constrângeri în Sketching 

**Sketcherul** se îndepărtează de această logică. Obiectele nu trebuie să fie desenate exact așa cum intenționați, deoarece ele vor fi definite ulterior prin constrângeri. Obiectele pot fi desenate și, atâta timp cât ele nu sunt restricționate, pot fi modificate. Ele sunt în fapt \"plutitoare\" și pot fi mișcate, întinse, rotite, scalate și așa mai departe. Acest lucru oferă o mare flexibilitate în procesul de proiectare.


</div>

#### What are constraints? 


<div class="mw-translate-fuzzy">

#### Ce sunt constrângerile? 

În loc de dimensiuni, constrângerile sunt folosite pentru a limita gradul de libertate al unui obiect. De exemplu, o linie fără constrângeri are 4 [ Degrees of Freedom](#Degrees_of_Freedom.md) (abreviat ca \"DOF\"): poate fi mișcat orizontal sau vertical, poate fi întinsă și poate fi rotită.


</div>

Aplicarea unei constrângeri orizontale sau verticale sau a unei constrângeri de unghi (relativ la o altă linie sau la una dintre axe) va limita capacitatea sa de a se roti, lăsându-l astfel cu 3 grade de libertate. Blocarea unuia dintre punctele sale în raport cu originea va elimina încă 2 grade de libertate. Și aplicarea unei constrângeri de dimensiune va elimina ultimul grad de libertate. Linia este apoi considerată **complet constrânsă**.


<div class="mw-translate-fuzzy">

Obiectele multiple pot fi constrânse între ele. Două linii pot fi unite prin unul dintre punctele lor cu constrângerea punctului coincident. Un unghi poate fi setat între ele sau poate fi setat perpendicular. O linie poate fi tangentă la un arc sau un cerc și așa mai departe. O schiță complexă, cu obiecte multiple, va avea o serie de soluții diferite, ceea ce înseamnă că \"una dintre aceste soluții posibile a fost atinsă pe baza constrângerilor aplicate.


</div>


<div class="mw-translate-fuzzy">

Există două tipuri de constrângeri: geometrice și dimensionale. Acestea sunt detaliate în secțiunea [ \'Instrumentele\'](#_Instrumente.md) de mai jos.


</div>

#### What the Sketcher is not good for 


<div class="mw-translate-fuzzy">

#### La ce nu este bun Sketcher-ul 

Instrumentul Sketcher nu este destinat pentru realizarea planurilor 2D. Odată ce schițele sunt folosite pentru a genera o caracteristică solidă, ele sunt ascunse automat. Constrângerile sunt vizibile numai în modul Editare schiță.


</div>


<div class="mw-translate-fuzzy">

Dacă doriți să creați numai vizualizări 2D pentru tipărire și nu doriți să creați modele 3D, consultați [Draft workbench](Draft_Workbench.md).


</div>

The tool [Draft2Sketch](Draft_Draft2Sketch.md) converts a Draft object to a Sketch object, and vice versa. Many tools that require a 2D element as input work with either type of object as an internal conversion is done automatically.

## Sketching Workflow 


<div class="mw-translate-fuzzy">

## Schițarea fluxului de lucru 

O schiță este întotdeauna bi-dimensională (2D). Pentru a crea un solid, se creează o schiță 2D a unei singure zone închise și apoi fie se aplică o extruziune sau o rotație/revoluție pentru a adăuga cea de-a treia dimensiune, creând un solid 3D din schița 2D.


</div>


<div class="mw-translate-fuzzy">

Dacă schița are segmente care se încrucișă unul pe altul, locurile în care un punct nu se află direct pe un segment sau în locurile în care există discrepanțe între punctele finale ale segmentelor adiacente, Extruderea sau piesa de revoluție nu va crea un solid. Excepția de la această regulă este că nu se aplică în cazul Geometriei de Construcție (albastru).


</div>


<div class="mw-translate-fuzzy">

În interiorul zonei închise putem avea zone mai mici care nu se suprapun. Acestea vor deveni goluri atunci când solidul 3D va fi creat.


</div>

Once a Sketch is fully constrained, the Sketch features will turn green; Construction Geometry will remain blue. It is usually \"finished\" at this point and suitable for use in creating a 3D solid. However, once the Sketch dialog is closed it may be worthwhile going to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and running **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Check geometry](Part_CheckGeometry.md)** to ensure there are no features in the Sketch which may cause later problems.

## Tools


<div class="mw-translate-fuzzy">

## Instrumentele

Instrumentele Sketcher Workbench sunt toate localizate în meniul Sketch care apare atunci când încărcați Sketcher Workbench.


</div>


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.

### General

#### Sketcher toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.png‎‎  style="width:32px;"> [New sketch](Sketcher_NewSketch.md):Creează o nouă schiță pe o fațetă sau pe un plan selectat. Dacă nu este selectată nici o fațetă în timp ce acest instrument este executat, utilizatorul este chemat să selecteze un plan dintr-o fereastră pop-up.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Edit sketch](Sketcher_EditSketch.md): Editează schița selectată.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.png‎  style="width:32px;"> [Map sketch to face](Sketcher_MapSketch.md): Aplică o schiță pe o fațetă a unui solid.


</div>


<div class="mw-translate-fuzzy">

-   [Reorient sketch](Sketcher_ReorientSketch/ro.md): Permite schimbarea poziției schiței


</div>


<div class="mw-translate-fuzzy">

-   [Validate sketch](Sketcher_ValidateSketch/ro.md): Verifică toleranța la direferite puncte și le ajustează.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MergeSketch.png‎  style="width:32px;"> [Merge sketches](Sketcher_MergeSketches.md): Fuzionează două sau mai multe schițe. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MirrorSketch.png‎  style="width:32px;"> [Mirror sketch](Sketcher_MirrorSketch.md): Crează o schiță simetrică după axa x, y sau față de origine. <small>(v0.16)</small> 


</div>

#### Sketcher Edit Mode toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> [Leave sketch](Sketcher_LeaveSketch.md): Părăsește modul de editare al Sketch.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSketch.png‎  style="width:32px;"> [View sketch](Sketcher_ViewSketch.md): Setează modul de vedere perpendicular pe planul schiței.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSection.png  style="width:32px;"> [View section](Sketcher_ViewSection.md): Creează o secțiune plană care ascunde temporar orice lucru în fața planului schiței. <small>(v0.18)</small> 


</div>

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Stop operation](Sketcher_StopOperation.md): When in edit mode, stop the current operation, whether that is drawing, setting constraints, etc.

### Sketcher geometries 

Aceste unelte se folosesc la crearea obiectelor.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> [Point](Sketcher_CreatePoint.md): Desenează un punct.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [Line by 2 point](Sketcher_CreateLine.md): Desenează un segment de linie definit prin 2 puncte. Liniile sunt infinite în ceea ce privește anumite constrângeri.


</div>

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;"> [Create an arc](Sketcher_CompCreateArc.md): Acesta este un meniu de pictograme/iconițe din bara de instrumente Sketcher care deține următoarele comenzi:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> [Arc](Sketcher_CreateArc.md): Desenează un segemnt de cerc definit prin centru, radius, unghiul de stat și cel de capăt.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width:32px;"> [Arc by 3 Point](Sketcher_Create3PointArc.md): Desenează un segment de arc de cerc din două puncte de capăt și un alt punct de pe circumferință.


</div>

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;"> [Create a circle](Sketcher_CompCreateCircle.md): Acesta este un meniu de pictograme din bara de instrumente Sketcher care deține următoarele comenzi:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> [Circle](Sketcher_CreateCircle.md): Desenează un cerc definit prin centru și rază.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateCircle3Point.png  style="width:32px;"> [Circle by 3 Point](Sketcher_Create3PointCircle.md): Desenează un cerc definit prin trei puncte pe circumferință.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:48px;"> [Crearea unei conice](Sketcher_CompCreateConic.md):
    -   <img alt="" src=images/Sketcher_CreateEllipse.png  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Desenează o elipsă definită prin punctul central, un punct pe semiaxa majoră și un punct pe semiaxa minoră. <small>(v0.15)</small> 
    -   <img alt="" src=images/Sketcher_CreateEllipse_3points.png  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Desenează o elipsă definită de către 2 puncte pe axa majoră și punctul pe semiaxa minoră. <small>(v0.15)</small> 
    -   <img alt="" src=images/Sketcher_Elliptical_Arc.png  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md):

Desenează un arc de elipsă definită prin punctul central, punctul principal de rază, punctul de plecare și punctul final.<small>(v0.15)</small> 

-   -   <img alt="" src=images/Sketcher_Hyperbolic_Arc.png  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Desenează un arc de hiperbolă. <small>(v0.17)</small> 
    -   <img alt="" src=images/Sketcher_Parabolic_Arc.png  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Desenează un arc de parabolă. <small>(v0.17)</small> 


</div>

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Draws an ellipse by center point, major radius point and minor radius point.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Draws an ellipse by major diameter (2 points) and minor radius point.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Draws an arc of ellipse by center point, major radius point, starting point and ending point.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Draws an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Draws an arc of parabola.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [Create a B-spline](Sketcher_CompCreateBSpline.md): Acesta este un meniu de pictograme din bara de instrumente Sketcher care deține următoarele comenzi:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [Create B-spline](Sketcher_CreateBSpline.md):Trasează o curbă B-spline definită prin punctele sale de control.<small>(v0.17)</small> 
    -   <img alt="" src=images/Sketcher_Create_Periodic_BSpline.svg  style="width:32px;"> [Create periodic B-spline](Sketcher_CreatePeriodicBSpline.md): Desenează o curbă B-spline periodică (închisă) definită prin punctele sale de control. <small>(v0.17)</small> 


</div>

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Draws a B-spline curve by its control points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Draws a periodic (closed) B-spline curve by its control points.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Draws a B-spline curve by its knots. <small>(v0.21)</small> 

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Draws a periodic (closed) B-spline curve by its knots. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.png  style="width:32px;"> [Polyline (multiple-point line)](Sketcher_CreatePolyline.md): Creează o linie formată din mai multe segmente de linie. Apăsând tasta M în timp ce desenați o polilinie comută între diferite moduri de polilinie.


</div>

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Create rectangle](Sketcher_CompCreateRectangles.md): This is an icon menu in the Sketcher toolbar that holds the following commands: <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle.md): Desenează un dreptunghi definit prin 2 puncte diagonal opuse.


</div>

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md): Draws a rectangle from a central point and an edge point. <small>(v0.20)</small> 

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rounded rectangle](Sketcher_CreateOblong.md): Draws a rounded rectangle from 2 opposite points. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width:48px;"> [Create regular polygon](Sketcher_CompCreateRegularPolygon.md): Acesta este un meniu de pictograme din bara de instrumente Sketcher care deține următoarele comenzi:


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateTriangle.png  style="width:32px;"> [Triangle](Sketcher_CreateTriangle.md): Desenează un triunghi echilateral inscris într-un cerc .<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> [Square](Sketcher_CreateSquare.md): Desenează un pătrat înscris într-un cerc. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon.md): Desenează un pentagon regulat înscris într-un cerc. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon.md): Desenează un hexagon regulat înscris într-un cerc. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon.md): Desenează un heptagon regulat înscris într-un cerc. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Octagon](Sketcher_CreateOctagon.md): Desenează un octogon regulat înscris într-un cerc. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.png  style="width:32px;"> [Create Regular Polygon](Sketcher_CreateRegularPolygon.md) : Desenează un poligon regulat prin selectarea numărului de laturi și a două puncte: centrul, respectiv unul dintre unghiuri.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.png  style="width:32px;"> [Slot](Sketcher_CreateSlot.md): Desenează un oval (locaș de pană) prin selectare centrului unui semicerc, a razei și un punct de capăt al celuilalt semicerc.


</div>

-   <img alt="" src=images/Sketcher_CompCreateFillets.png  style="width:48px;"> [Create fillet](Sketcher_CompCreateFillets.md): This is an icon menu in the Sketcher toolbar that holds the following commands:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> [Fillet](Sketcher_CreateFillet.md): Face o racordare între două linii îmbinate într-un punct. Selectați ambele linii sau faceți clic pe punctul de intersecție, apoi activați instrumentul.


</div>

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their (virtual) intersection.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Trimming](Sketcher_Trimming.md): Ajustează o linie, un cerc sau un arc în raport cu amplasarea unui punct dat(poziția mouse-ului).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Extend](Sketcher_Extend.md): Extinde o linie sau un arc de cerc până la o limită definită printr-un arc de cerc, elipsă, arc de elipsă sau un punct în spațiu. <small>(v0.17)</small> 


</div>

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Split](Sketcher_Split.md): Splits an edge into two while keeping most of the constraints. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [External Geometry](Sketcher_External.md): Creează o margine legată de geometria exterioară.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [CarbonCopy](Sketcher_CarbonCopy.md): Copiază forma geometrică din altă schiță.<small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction Mode](Sketcher_ToggleConstruction.md): Comută elementele geometrice ale schiței de la / la modul de Construcție. Forma geometrică este afișată în albastru și nu este luată în considerare în afara modului de editare a schiței.


</div>



### Constrângeri Sketcher 

Constrângerile sunt folosite pentru a defini lungimile, a stabili reguli între elementele de schiță și pentru a bloca schița de-a lungul axelor verticale și orizontale. Unele constrângeri necesită utilizarea [Helper constraints](Sketcher_helper_constraint.md).

#### Geometric constraints 


<div class="mw-translate-fuzzy">

#### Constrângeri geometrice 

Aceste constrângeri nu sunt asociate cu date numerice.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> [Coincident](Sketcher_ConstrainCoincident.md): Creează o constrângere de coincidență cu unul sau mai multe puncte.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnObject.png  style="width:32px;"> [Point On Object](Sketcher_ConstrainPointOnObject.md): Face să coincidă un punct cu altul cu alt obiect ca de ex: linie, arc, sau axă.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical.md): Constrâne liniile selectate sau elementele poliliniei la o orientare verticală. Se poate aplică la mai mult de un obiect.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Horizontal.png  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md):

Constrânge liniile selectate sau elementele de polilinie la o orientare orizontală reală. Pot fi selectate mai multe obiecte înainte de aplicarea acestei constrângeri.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel.md): Constrânge două sau mai multe linii a fi paralele înte ele.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Perpendicular.png  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md): Constrânge două linii a fi perpendiculare una pe ceallată, sau consrînge o linie a fi perpendiculară pe un capăt de arc de cerc.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Tangent](Sketcher_ConstrainTangent.md): Creează o constrângere de tangență în două entități selectate ates, sau o constrânere de coliniaritaea între două segmente de linie. Un segment de linie nu trebuie să stea direct pe un arc sau un cerc pentru a fi constrâns tangent la acel arc sau cerc.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Equal Length](Sketcher_ConstrainEqual.md): Constrânge două entități selectate a fi egale una cu celălaltă. Dacă sunt utilizate pe cercuri sau arce de cerc, raza lor va fi egală.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md):Constrânge două puncte a fi simetrice față de o linie sau constrânge primele două puncte selectate a fi simetrice în raport cu un al treilea punct selectat.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainBlock.png  style="width:32px;"> [Constrain Block](Sketcher_ConstrainBlock.md):

Practic permite blocarea unui element geometric în loc cu o singură constrângere. Ar trebui să fie deosebit de util să lucrați cu acest la curbele B-Splines. A se vedea [Block Constraint forum topic](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572). <small>(v0.17)</small> 


</div>

#### Dimensional constraints 


<div class="mw-translate-fuzzy">

#### Constrângeri dimensionale 

Acestea sunt constrângeri asociate datelor numerice, pentru care puteți utiliza expresiile [expressions](Expressions.md). Datele pot fi preluate dintr-un [spreadsheet](Spreadsheet_Workbench.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.png‎  style="width:32px;"> [Lock](Sketcher_ConstrainLock.md): Restricționează elementul selectat prin stabilirea distanțelor orizontale și orizontale față de origine, blocând astfel locația acelui element. Aceste distanțe de constrângere pot fi editate mai târziu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_HorizontalDistance.png‎  style="width:32px;"> [Horizontal Distance](Sketcher_ConstrainDistanceX.md):

Fixează distanța orizontală dintre două puncte sau puncte finale. Dacă este selectat un singur element, distanța este setată față de origine.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Vertical Distance](Sketcher_ConstrainDistanceY.md):

Fixează distanța verticală între 2 puncte sau puncte de capăt ale liniei. Dacă este selectat un singur element, distanța este setată față de origine.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Distance](Sketcher_ConstrainDistance.md):

Definește distanța unei linii selectate prin limitarea lungimii acesteia sau definește distanța dintre două puncte prin limitarea distanței dintre ele.


</div>

-   <img alt="" src=images/Sketcher_CompConstrainRadDia.png  style="width:48px;"> [Constrain radius or diameter](Sketcher_CompConstrainRadDia.md): This is an icon menu in the Sketcher constraints toolbar that holds the following commands:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Radius](Sketcher_ConstrainRadius.md):

Definește raza unui arc de cerc sau cerc selectat prin limitarea razei.

-   <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Internal Angle](Sketcher_ConstrainAngle.md):

Definește unghiul interior dintre două linii selectate.


</div>

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Defines the diameter of an arc or circle.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Defines the radius of an arc, the diameter of a circle or the weight of a B-spline pole. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Defines the internal angle between two selected lines.

#### Special constraints 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_SnellsLaw.png  style="width:32px;"> [Snell\'s Law](Sketcher_ConstrainSnellsLaw.md): Constrânge două linii pentru a se supune unei legi de refracție pentru a simula lumina care traversează o interfață. <small>(v0.15)</small> 


</div>

#### Constraint tools 

The following tools can be used the change the effect of constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstraint.png  style="width:32px;"> [Toggle reference/driving constraint](Sketcher_ToggleDrivingConstraint.md): Comută bara de instrumente sau constrângerile selectate de la/din modul de referință. <small>(v0.16)</small> 


</div>

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md): Enable or disable an already placed constraint.



### Instrumente Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Select solver DOFs](Sketcher_SelectElementsWithDoFs.md): Evidențiază în verde geometria cu grade de libertate (DOF), adică nu este complet constrânsă. <small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.png‎  style="width:32px;"> [Select Constraints](Sketcher_SelectConstraints.md): Selectează constrângerile elementului Sketcher <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.png‎  style="width:32px;"> [Select Elements Associated with constraints](Sketcher_SelectElementsAssociatedWithConstraints.md): Selectați elementele sketcher asociate cu constrângerile <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.png‎  style="width:32px;"> [Select Redundant Constraints](Sketcher_SelectRedundantConstraints.md): Selectează constrângeri redundante a sketch <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.png‎  style="width:32px;"> [Select Conflicting Constraints](Sketcher_SelectConflictingConstraints.md): Selectează constrângerile conflictuale ale unei sketch <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_Ellipse_All.png‎  style="width:32px;"> [Show/Hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md): Reface pierderea / ștergerea geometriei interne inutile a unei elipse selectate, arcului de elipsă / hyperbola / parabola sau B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.png‎  style="width:32px;"> [Select Origin](Sketcher_SelectOrigin.md): Selectează originea unei sketch <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.png‎  style="width:32px;"> [Select Horizontal Axis](Sketcher_SelectHorizontalAxis.md): Selectează axa orizontală a sketch <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.png‎  style="width:32px;"> [Select Vertical Axis](Sketcher_SelectVerticalAxis.md): Selectează axa verticală a sketch <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.png‎  style="width:32px;"> [Symmetry](Sketcher_Symmetry.md): Copiază elementul simetric față de o linie selectatăe <small>(v0.16)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.png‎  style="width:32px;"> [Clone](Sketcher_Clone.md): Clonează un element sketcher <small>(v0.16)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.png‎  style="width:32px;"> [Copy](Sketcher_Copy.md): Copiază un element sketcher <small>(v0.16)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Move](Sketcher_Move.md): Mută elementul geometric ales luând ca referință ultimul punct selectat.<small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.png‎  style="width:32px;"> [Rectangular Array](Sketcher_RectangularArray.md): Creează o matrice de multiplicare a elementelor sketcher selectate <small>(v0.16)</small> 


</div>

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md): Remove axes alignment while trying to preserve the constraint relationship of the selection. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_SelectionTypeInvalid.svg  style="width:32px;"> [Delete All Geometry](Sketcher_DeleteAllGeometry.md): Șterger toate elementele geometrice din sketch. <small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_SelectionTypeInvalid.svg  style="width:32px;"> [Delete All Constraints](Sketcher_DeleteAllConstraints.md): Șterge toate constrângerile din sketch. <small>(v0.18)</small> 


</div>



### Instrumentele pentru Sketcher B-spline 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Show/Hide B-spline degree](Sketcher_BSplineDegree.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Show/Hide B-spline control polygon](Sketcher_BSplinePolygon.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Show/Hide B-spline curvature comb](Sketcher_BSplineComb.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Show/Hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)


</div>

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md): Shows or hides the display of the weights for the control points of a B-spline.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Convert Geometry to B-spline](Sketcher_BSplineApproximate.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Increase degree](Sketcher_BSplineIncreaseDegree.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md): Decreases the degree (order) of a B-spline.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into an existing B-spline. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Joins two curves at selected end points. <small>(v0.21)</small> 



### Sketcher în spațiul virtual 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.png‎  style="width:32px;"> [Switch Virtual Space](Sketcher_SwitchVirtualSpace.md): Vă permite să comutați între a "ascunde" constrângerile și a le face iarăși vizibile. <small>(v0.17)</small>  See <https://forum.freecadweb.org/viewtopic.php?f=9&t=26614>


</div>

### Obsolete tools 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.png‎  style="width:32px;"> [Close Shape](Sketcher_CloseShape.md): Creează o formă închisă prin aplicarea unor constrângeri de coincidență a punctelor de capăt<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.png‎  style="width:32px;"> [Connect Edges](Sketcher_ConnectLines.md): Conectați elementele Sketcher aplicând constrângeri de coincidentență la punctele de capăt <small>(v0.15)</small> 


</div>




<div class="mw-translate-fuzzy">

### Preferințe


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Preferences\...](Sketcher_Preferences.md): Preferințe disponibile în Sketcher Tools.


</div>

## Best Practices 


<div class="mw-translate-fuzzy">

## Cele mai bune practici 

Fiecare utilizator CAD își dezvoltă în timp propriul mod de a lucra, dar există câteva principii generale utile care trebuie urmate.


</div>


<div class="mw-translate-fuzzy">

-   O serie de schițe simple sunt mai ușor de gestionat decât una complexă. De exemplu, o primă schiță poate fi creată pentru funcționalitate 3D de bază (fie un pad, fie o rotire), în timp ce a doua poate conține găuri sau decupări (buzunare). Unele detalii pot fi lăsate, pentru a fi realizate ulterior ca elemente 3D. Puteți alege să evitați filamentele din schiță dacă există prea multe și adăugați-le ca o funcționalitate 3D.
-   Creați întotdeauna un profil închis, sau schița dvs. nu va produce un solid, ci mai degrabă un set de fețe deschise. Dacă nu doriți ca unele obiecte să fie incluse în creația solidă, transformați-le în elementele de construcție cu instrumentul Mod de construcție.
-   Utilizați caracteristica de constrângeri automate pentru a limita numărul de constrângeri pe care trebuie să le adăugați manual.
-   Ca regulă generală, aplicați mai întâi constrângeri geometrice, apoi constrângeri dimensionale și blocați ultima schiță. Dar amintiți-vă: regulile sunt făcute pentru a fi încălcate. Dacă întâmpinați dificultăți în manipularea schiței dvs., poate fi util să restrângeți mai întâi câteva obiecte înainte de a vă completa profilul.
-   Dacă este posibil, centrați schița la origine (0,0) cu constrângerea de blocare. Dacă schița dvs. nu este simetrică, localizați unul dintre punctele sale la origine sau alegeți numere rotunde frumoase pentru distanțele de blocare. În v0.12, constrângerile externe (constrângerea schiței față de geometria 3D existentă ca marginile sau alte schite) nu sunt implementate. Aceasta înseamnă că pentru a localiza geometria schițelor care urmează în prima schiță, va trebui să setați manual distanțele față de prima schiță. O constrângere de blocare a (25,75) de origine este mai ușor de reținut decât (23,47,73.02).
-   Dacă aveți posibilitatea de a alege între constrângerile de lungime și constrângerile orizontale sau verticale, preferați ultima. Constrângerile orizontale și verticale sunt mai puțin costisitoare ca timp computațional.
-   În general, cele mai bune constrângeri de utilizat sunt: ​​Constrângerile orizontale și verticale; Restricții de lungime orizontală și verticală; Point-to-Point Tangency. Dacă este posibil, limitați utilizarea acestora: restricția generală a lungimii; Tangența de la muchie la muchie; Fix Point pe o linie Constrângere; Constrângerea simetrice.


</div>




<div class="mw-translate-fuzzy">

## Tutoriale


</div>

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a 70-page long PDF document that serves as a detailed manual for the sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) for beginners
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimum requirement for a sketch and Complete determination of a sketch

## Scripting

The [Sketcher scripting](Sketcher_scripting.md) page contains examples on how to create constraints from Python scripts.

## Examples

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/ro
