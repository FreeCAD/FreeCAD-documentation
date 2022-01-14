# Sandbox:HowTo
Back to [FreeCADDocu:Sandbox](FreeCADDocu:Sandbox#HowTo_test.md)

**FreeCAD Wiki HowTo Page**

## Overview

This is an experimental page for discussion. Please change and add as seen fit.

### Foldable HowTo Template 

Here is an empty template to quickly add a HowTo to this page. You need to be logged in to use it. Go to edit mode and copy&paste it.

     <div class="mw-collapsible mw-collapsed toccolours">
     * HowTo make a HowTo Enty
     <div class="mw-collapsible-content">
     Just copy me to the correct section and change the headline and this section. Do not change the "div" fields in brackets.

    [top](#top.md)
     </div>
     </div>

The *Top* link below gets you quickly to the top of the page. It looks in wiki markup like this: [top](#top.md). For easier navigation in long pages its recommended to include this under your section. Make sure there is an empty line before it.

[top](#top.md)

## HowTo

### General Design Use Cases 


<div class="mw-collapsible mw-collapsed toccolours">

-   **HowTo center a hole to a face**


<div class="mw-collapsible-content">

Use External geometry to map the edges.

-   Add a circle roughtly inthe middle
-   First select 2 diagonal corner points
-   Last selected point is the symmetry point. Here its our cirle.
-   Select the symmetry constraint.

Note that the 3 point symmetry enforces that all poinst must lie on a straight line. If that can not be achived the constraint will fail. [top](#top.md)


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

-   **HowTo make holes through multiple bodies**


<div class="mw-collapsible-content">

Normally the Hole function only works within a single body, no matter what values are given for Dimension.

To make hole though muliple bodies you need to assing the hole function to each body seperately. The most important point is to make sure the holes stay aligned and are linked to each other. That means when the master part is moved all other holes move as well.

This can be done by making references of the sketches used for the holes in the master part. Just use the function \"ShapeBinder\" from the [PartDesign Workbench](PartDesign_Workbench.md). There is an example on the Reference page.

[top](#top.md)


</div>


</div>

[top](#top.md)

### General GUI Use Cases 


<div class="mw-collapsible mw-collapsed toccolours">

-   \'\'\'How to slice the 3D view \'\'\'


<div class="mw-collapsible-content">

Please add if you know. I did not yetfind out ;)

[top](#top.md)


</div>


</div>

[top](#top.md)

### Workbench Use Cases 

#### TechDraw Use Cases 


<div class="mw-collapsible mw-collapsed toccolours">

-   **HowTo Dimension the distance between two hole edges**


<div class="mw-collapsible-content">

The idea is to see directly how much material is left between two holes (obviously it can be calculated when the center distance and the radii are given, but that is not the point).

In FC 0.18 this does not work. The View are projected from the acutal 3D view, but only the corners and center points of the 3D geomtry is selectable for the dimensioning tools in 2D. If thats wrong or has changed please correct.

[top](#top.md)


</div>


</div>

[top](#top.md)

[<img src="images/Property.png" style="width:16px"> Sandbox](Category_Sandbox.md)

---
[documentation index](../README.md) > Sandbox:HowTo
