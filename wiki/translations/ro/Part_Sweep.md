---
- GuiCommand   */ro
   Name   *Part Sweep
   Name/ro   *Part Sweep
   MenuLocation   *Part → Sweep...
|
   Workbenches   *[Part](Part_Workbench/ro.md)
   SeeAlso   *[Part Loft](Part_Loft/ro.md)
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

![](images/Part_Sweep_simple.png ) *Un balaiaj solid generat pronind de la un profil (A) proiectat de-a lungul unei traiectorii(B).*

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Apăsați butonul **<img src="images/Part_Sweep.png" width=16px> '''Sweep'''**. Acesta deschide parametrii Sweep în Tasks panel.
2.  In the *Available Profiles* left column (previously *Vertex/Edge/Wire/Face* in v0.16), click on the element to be used as sweep profile, then click on the right arrow to place it in the *Selected profiles* right column (previously *Sweep* in v0.16). Repeat if more than one profile is desired. Use the up and down arrows to reorder the selected profiles.
3.  Click on the **Sweep Path** button, then choose either mode of selection   *
    -   *Single segment selection*   * select one or more contiguous edges in the 3D view (press **CTRL** for multiple selection) and click **Done**. The sweep will only be generated along the selected edges.
    -   *Complete path selection*   * switch to the Model tab, select the 2D object to be used as path in the tree, switch back to the Tasks pane and click **Done**. The sweep will be generated along all the contiguous edges found in the 2D object.
4.  Definiți opțiunile [Solid](#Solid.md) și [Frenet](#Frenet.md).
5.  Click OK.


</div>

### Accepted geometry 


<div class="mw-translate-fuzzy">

### Geometrie Acceptată 

-   **Profiles**   * pot fi un punct (vertex), linie (Edge), fir/polilinie sau fațetă. Muchiile/liniile și firele pot fi deschise sau închise. There are various [profile limitations and complications](Part_Sweep#Profile_limitations_and_complications.md), vedeți mai jos, dar profilurile pot proveni de la primitivele Atelierului Part Workbench, de la funcționalitățile Atelierului Draft Workbench și de la Sketches.


</div>


<div class="mw-translate-fuzzy">

-   **Path**   * poate fi o linie (Edge) sau o seri de linii conectate (polilinii), fire sau diverse priiteve geometrice din Atelierul Part, Funcționalitățile Atelierului Draft sau Sketch. The path is often selected directly from the main model window, however it can also be selected from the Tree View (Model Tab of Combo View). The path can either be an entire appropriate shape or an appropriate sub-component of a more advance shape (for example, an edge of a Part Cube could be selected as the path). The path may be either open or closed and will thus create either an open or closed Sweep. A closed path such as a Part Circle will result in a closed Sweep. De exemplu, un Sweep de un cerc mai mic în jurul unei căi de cerc mai mare va crea un tor.


</div>

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Properties

### Solid


<div class="mw-translate-fuzzy">

## Proprietăți

### Solid 

Dacă \"Solid\" este setat ca fiind \"true\", FreeCAD crează un solid, furnizând profilele ca fiind forme geometrice închise; Dacă este setat ca fiind \"false\", FreeCAD creează o fațetă sau (dacă sunt mai multe fațete) o cochilie pentru profile deschise sau închise.


</div>

### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width   *500px;">


<div class="mw-translate-fuzzy">

### Frenet 

<img alt="" src=images/Sweep-frenet-comp.png  style="width   *500px;"> Proprietatea \"Frenet\" controlează cum orientarea proficului

se schimbă de-a lungul traiectoriei de baleiere. If "Frenet" is "false", the orientation of the profile is kept consistent from point to point. The resulting shape has the minimum possible twisting. Unintuitively, when a profile is swept along a helix, this results in the orientation of the profile slowly creep (rotate) as it follows the helix. Setting "Frenet" to true prevents such a creep.


</div>

If \"Frenet\" is \"true\" the orientation of the profile is computed basing on local curvature and tangency vectors of the path. This keeps the orientation of the profile consistent when sweeping along a helix (because curvature vector of a straight helix is always pointing to its axis). However, when path is not a helix, the resulting shape can have strange looking twists sometimes. For more information, see [Frenet Serret formulas](http   *//en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).

### Transition


<div class="mw-translate-fuzzy">

### Tranziție

\"Transition\" sets the transition style of the Sweep at a joint in the path, if the path does not define the corner transition (for example where the path is a wire). The property is not exposed in the Tasks pane and can be found in properties after the Sweep has been created.


</div>

## Profile limitations and complications 


<div class="mw-translate-fuzzy">

## Limitări și complicații asupra Profilelor 

-   A vertex or point
    -   vertex or point may only be used as the first and/or last profile in the list of profiles.
        -   For example
            -   you can not Sweep from a circle to a point, to a ellipse.
            -   However you could Sweep from a point to a circle to an ellipse to another point.
-   Open or closed geometry profiles can not be mixed in one single Sweep
    -   In one Sweep, all profiles (lines wires etc.) must be either open or closed.
        -   For example
            -   FreeCAD can not Sweep between one Part Circle and one default Part Line.
-   Draft Workbench features
    -   Draft Workbench features can be directly used as a profile in FreeCAD 0.14 or later.
        -   For example the following Draft features can be used as profiles in a Part Sweep
            -   Draft Polygon.
            -   Draft Point, Line, wire,
            -   Draft B-spline, Bezier Curve
            -   Draft Circle, Ellipse, Rectangle
-   PartDesign Sketches
    -   The profile may be created with a sketch. However only a valid sketch will be shown in the list to be available for selection.
    -   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire)
-   Part Workbench
    -   the profile can be a valid Part geometric primitive which can be created with the [Part CreatePrimitives tool](Part_CreatePrimitives.md)
        -   For example the following Part geometric primitives can be a valid profile
            -   Point (Vertex), Line (Edge)
            -   Helix, Spiral
            -   Circle, Ellipse
            -   Regular Polygon
            -   Plane (Face)


</div>

## Links


<div class="mw-translate-fuzzy">

## Legături

-   De aceea Sweep este adesea utilizat pentru a crea filete pentru șururbur, puteți vedea la [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md).


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/ro
