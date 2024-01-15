---
 GuiCommand:
   Name: Part Sweep
   Name/ro: Part Sweep
   MenuLocation: Part , Sweep...
|
   Workbenches: Part_Workbench/ro
   SeeAlso: Part Loft/ro
---

# Part Sweep/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Baleiere **Sweep Part** este folosit pentru a crea o fațetă, o cochilie sau o formă solidă plecând de la unul sau mai multe profile (secțiuni transversale) proiectate de-a lungul unei traiectorii.


</div>


<div class="mw-translate-fuzzy">

Instrumentul Baleiere (Part Sweep) este similar cu [Part Loft](Part_Loft/ro.md) având suplimentar o traiectorie neliniară pentru a defini proiecția dintre profile.


</div>

<img alt="" src=images/Part_Sweep_simple.png  style="width:400px;"> 
*A solid sweep generated from a single profile (A) distributed along a spine (B)*

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Apăsați butonul **<img src="images/Part_Sweep.png" width=16px> '''Sweep'''**. Acesta deschide parametrii Sweep în Tasks panel.
2.  In the *Available Profiles* left column (previously *Vertex/Edge/Wire/Face* in v0.16), click on the element to be used as sweep profile, then click on the right arrow to place it in the *Selected profiles* right column (previously *Sweep* in v0.16). Repeat if more than one profile is desired. Use the up and down arrows to reorder the selected profiles.
3.  Click on the **Sweep Path** button, then choose either mode of selection:
    -   *Single segment selection*: select one or more contiguous edges in the 3D view (press **CTRL** for multiple selection) and click **Done**. The sweep will only be generated along the selected edges.
    -   *Complete path selection*: switch to the Model tab, select the 2D object to be used as path in the tree, switch back to the Tasks pane and click **Done**. The sweep will be generated along all the contiguous edges found in the 2D object.
4.  Definiți opțiunile [Solid](#Solid.md) și [Frenet](#Frenet.md).
5.  Click OK.


</div>

### Accepted geometry 


<div class="mw-translate-fuzzy">

### Geometrie Acceptată 

-   **Profiles**: pot fi un punct (vertex), linie (Edge), fir/polilinie sau fațetă. Muchiile/liniile și firele pot fi deschise sau închise. There are various [profile limitations and complications](Part_Sweep#Profile_limitations_and_complications.md), vedeți mai jos, dar profilurile pot proveni de la primitivele Atelierului Part Workbench, de la funcționalitățile Atelierului Draft Workbench și de la Sketches.


</div>


<div class="mw-translate-fuzzy">

-   **Path**: poate fi o linie (Edge) sau o seri de linii conectate (polilinii), fire sau diverse priiteve geometrice din Atelierul Part, Funcționalitățile Atelierului Draft sau Sketch. The path is often selected directly from the main model window, however it can also be selected from the Tree View (Model Tab of Combo View). The path can either be an entire appropriate shape or an appropriate sub-component of a more advance shape (for example, an edge of a Part Cube could be selected as the path). The path may be either open or closed and will thus create either an open or closed Sweep. A closed path such as a Part Circle will result in a closed Sweep. De exemplu, un Sweep de un cerc mai mic în jurul unei căi de cerc mai mare va crea un tor.


</div>

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Options

#### Solid


<div class="mw-translate-fuzzy">

## Proprietăți

### Solid 

Dacă \"Solid\" este setat ca fiind \"true\", FreeCAD crează un solid, furnizând profilele ca fiind forme geometrice închise; Dacă este setat ca fiind \"false\", FreeCAD creează o fațetă sau (dacă sunt mai multe fațete) o cochilie pentru profile deschise sau închise.


</div>

#### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">


<div class="mw-translate-fuzzy">

### Frenet 

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;"> Proprietatea \"Frenet\" controlează cum orientarea proficului

se schimbă de-a lungul traiectoriei de baleiere. If "Frenet" is "false", the orientation of the profile is kept consistent from point to point. The resulting shape has the minimum possible twisting. Unintuitively, when a profile is swept along a helix, this results in the orientation of the profile slowly creep (rotate) as it follows the helix. Setting "Frenet" to true prevents such a creep.


</div>


<div class="mw-translate-fuzzy">

If \"Frenet\" is \"true\" the orientation of the profile is computed basing on local curvature and tangency vectors of the path. This keeps the orientation of the profile consistent when sweeping along a helix (because curvature vector of a straight helix is always pointing to its axis). However, when path is not a helix, the resulting shape can have strange looking twists sometimes. For more information, see [Frenet Serret formulas](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).


</div>

#### Transition


<div class="mw-translate-fuzzy">

### Tranziție

\"Transition\" sets the transition style of the Sweep at a joint in the path, if the path does not define the corner transition (for example where the path is a wire). The property is not exposed in the Tasks pane and can be found in properties after the Sweep has been created.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A Part Sweep object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Sweep}}

-    **Sections|LinkList**: lists the sections used.

-    **Spine|LinkSub**: spine (path) to sweep along.

-    **Solid|Bool**: true or false (default). True creates a Solid.

-    **Frenet|Bool**: true or false (default). True uses Frenet algorithm.

-    **Transition|Enumeration**: transition mode. Options are *Transformed*, *Right corner* or *Round corner*.

## Limitations

### Vertex or point 

A vertex or point may only be used as the first and/or last profile.
For example:

-   You cannot Sweep from a circle to a point, to an ellipse.
-   You can however Sweep from a point to a circle to an ellipse to another point.

### Profiles

In one Sweep, all profiles (lines wires etc.) must be either open or closed.
For example:

-   FreeCAD cannot Sweep between a Part Circle and a Part Line.

### Sketches

-   The profile may be created with a sketch. However only valid sketches will be available for selection in the task panel.
-   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire).

### Draft Workbench objects 

A profile can be a [Draft Workbench](Draft_Workbench.md) object.
The following objects can be valid profiles:

-   Point
-   Line, Wire
-   B-spline, Bézier Curve
-   Circle, Ellipse
-   Rectangle, Polygon

### Part Workbench objects 

A profile can be a Part object created with the [Part Primitives](Part_Primitives.md) command.
The following objects can be valid profiles:

-   Point (Vertex)
-   Line (Edge)
-   Helix, Spiral
-   Circle, Ellipse
-   Regular Polygon
-   Plane (Face)

## Links


<div class="mw-translate-fuzzy">

## Legături

-   De aceea Sweep este adesea utilizat pentru a crea filete pentru șururbur, puteți vedea la [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md).


</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/ro
