---
- GuiCommand   */pl
   Name   *Part Loft
   Name/pl   *Part   * Wyciągnij po profilach
   MenuLocation   *Część → Wyciągnięcie po profilach...
   Workbenches   *[Środowisko pracy Część](Part_Workbench/pl.md)
   Version   *0.13
   SeeAlso   *[Wyciągnięcie po ścieżce](Part_Sweep/pl.md)
---

# Part Loft/pl

## Overview

The **Part Loft** tool is used to create a face, shell or a solid shape from two or more profiles. The profiles can be a point (vertex), line (Edge), wire or face. Edges and wires may be either open or closed. There are various [Limitations and complications](Part_Loft#Limitations_and_complications.md), see below, however the profiles may come from [Part Workbench primitives](Part_Workbench.md), [Draft Workbench objects](Draft_Workbench.md) and [Sketches](Sketcher_Workbench.md).

The Loft has three parameters, \"Ruled surface\",\"Create solid\" and \"Closed\" each with a value of either \"true\" or \"false\".

If \"Create solid\" is \"true\" FreeCAD creates a solid if the profiles are of closed geometry, if \"false\" FreeCAD creates a face or (if more than one face) a shell for either open or closed profiles.

If \"Ruled surface\" is \"true\" FreeCAD creates a face, faces or a solid from ruled surfaces. [Ruled surface page on Wikipedia.](http   *//en.wikipedia.org/wiki/Ruled_surface)

If \"Closed\" is \"true\" FreeCAD attempts to loft the last profile to the first profile to create a closed figure.

For more info on how the profiles are joined together, refer [Part Loft Technical Details](Part_Loft_Technical_Details.md) page.

![centre\|Part Loft. From three profiles which are two Part Circles and one Part Ellipse. Parameters are Solid \"True\" and Ruled \"True\"](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Limitations and complications 

-   A vertex or point
    -   vertex or point may only be used as the first and/or last profile in the list of profiles.
        -   For example
            -   you cannot loft from a circle to a point, to an ellipse.
            -   However you could Loft from a point to a circle to an ellipse to another point.
-   Open or closed geometry profiles can not be mixed in one single Loft
    -   In one Loft, all profiles (lines wires etc.) must be either open or closed.
        -   For example
            -   FreeCAD can not Loft between one Part Circle and one default Part Line.
-   Draft Workbench features
    -   Draft Workbench features can be directly used as a profile in FreeCAD 0.14 or later.
        -   For example the following Draft features can be used as profiles in a Part Loft
            -   Draft Polygon.
            -   Draft Point, Line, wire,
            -   Draft B-spline, Bezier Curve
            -   Draft Circle, Ellipse, Rectangle
-   PartDesign Sketches
    -   The profile may be created with a sketch. However only a valid sketch will be shown in the list to be available for selection.
    -   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire)
-   Part Workbench
    -   the profile can be a valid Part geometric primitive which can be created with the [Part Primitives](Part_Primitives.md) tool
        -   For example the following Part geometric primitives can be a valid profile
            -   Point (Vertex), Line (Edge)
            -   Helix, Spiral
            -   Circle, Ellipse
            -   Regular Polygon
            -   Plane (Face)

-   Closed Lofts
    -   The results of closed lofts may be unexpected - the loft may develop twists or kinks. Lofting is very sensitive to the Placement of the profiles and the complexity of the curves required to connect the corresponding Vertices in all the profiles.

## An example Loft 

The Loft tool is in the Part Workbench, menu Part -\> Loft\... or via the icon in the tool bar.

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )

In the \"Tasks\" will be two lists   * \"Available\" and \"Selected\".

![](images/Part_Loft_Liste3.png )

### Selection of the sections 

In the \"Available\" the available items are displayed. Two sections must be selected one after the first in this list.

![](images/Part_Loft_Liste_Auswahl_3b.png )

Thereafter, with the blue arrow that item is added to the list of \"Selected\".

![](images/Part_Loft_Liste_Auswahl_3c.png )

The selected items must be of the same type.

Tip   * the active/selected items in the list are displayed in the 3D area as active/selected.

### Command complete 

If both sections are selected, the command can be completed with \"OK\".

![](images/Part_Loft_Liste_Auswahl_3d.png )

### Result

From closed lines we get surfaces which might be taken as a superficial look for solids.

![](images/Part_Loft_geschlossen.png )

If indeed a solid needs to be created, used the button \"Create Solid\" or after creating the Loft switch to its *properties* tab *data* and set the switch \"Solid\" to true.

The procedure is the same as described above with open polylines.

### Changing the selection of sections 

If you want to change the selection of the sections after creation of the loft, you can select the field Sections in the Data tab and click the occuring ellipsis button. The list of all selectable sections occurs, the current selection is highlighted. You can remove or add additional sections.

The sequence of sections depends on the sequence of clicks in the list. If you want to make substantial changes it is recommended to first deselect all and then start selection in the right order.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/pl
