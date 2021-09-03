---
- GuiCommand:   Name:Part Extrude   MenuLocation:Part → Extrude   Workbenches:[[Part_Workbench   Part]]|SeeAlso:---


</div>

![600px](images/Part_Extrude_demo.png)

## Descriere

**Part Extrude** extinde o formă la o distanță specificată, într-o direcție specificată. Tipul formei de ieșire va varia în funcție de tipul formei de intrare și de opțiunile selectate.


<div class="mw-translate-fuzzy">

În cele mai comune scenarii, lista de mai jos prezintă forma tip de ieșire așteptat de tip de formă de la o intrare/input dată.

-   Extruderea unui vertex (punct), va produce o margine liniară
-   Extruderea unei margine deschisă (de exemplu, linie, arc), va produce o fațetă deschisă (de exemplu, planul)
-   Extrudează o margine închisă (de exemplu, cerc) va produce în cele din urmă o față închisă (de exemplu, cilindru nedeterminat) sau parametrul „solid" este „adevărat", va produce un solid (de exemplu, un cilindru solid închis).
-   Extrude un filament deschis (de exemplu, un proiect de fire), va produce o cochilie deschisă (mai multe fațete îmbinate)
-   Extrudează un filament închis (de exemplu, Draft Wire), va produce în cele din urmă o coajă (mai multe fețe atașat) sau, în cazul în care „solid" este parametrul „true", produce un solid
-   Extrudare fețetei (de exemplu, un plan), va produce un solid (de exemplu, Cuboid)
-   Extrude un [Draft Shape String](Draft_ShapeString.md), va produce un compus solid (șirul este alcătuit din litere, care sunt fiecare un solid)
-   Extruderea unei cochilie de fațete, va produce un Compsolid


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}

1.  Select the shape(s) in the 3D view or in the Model tree
2.  Click on the **<img src="images/Part_Extrude.png" width=16px> '''Extrude'''** icon in the toolbar, or go to the Part → Extrude menu
3.  Set the direction and length and optionally other parameters (see the following [Parameters](#Parameters.md) section for more details).
4.  Click OK.


</div>


<div class="mw-translate-fuzzy">

Alternatively, the selection can be done after launching the tool, by selecting one or more shape from the list in the Tasks panel.


</div>

The Model tree will list as many Extrude objects as there were selected shapes. Each input shape is placed underneath its Extrude object.

## Parametri

Forma Extrude este definită de următorii parametri, care pot fi editați după crearea ei în fila/tab-ul Date.

-   **Base**: the input shape (the shape upon which the Part Extrude was applied)

-   **Dir**: the direction to extend the shape. If **Dir Mode** is \'Custom\', you can edit **Dir**. Otherwise, **Dir** is read-only, and computed from the linked shape.

-   **Dir Link**: parametric link to a edge (line) that sets the direction of extrusion. As of v0.17, this property is not supported by property editor.


<div class="mw-translate-fuzzy">

-   **Dir Mode**: sets how **Dir** is controlled. \'Custom\' meand **Dir** is editable. \'Edge\' means Dir is obtained from an edge (line) linked by **Dir Link**. \'Normal\' means Dir is perpendicular to plane of the input shape.


</div>

-   **Length Fwd**: The distance to extrude by. If both **Length Fwd** and **Length Rev** are zero, the length of **Dir** vector is used.

-   **Length Rev**: Additional length to extrude against **Dir**.

-   **Solid**: if True, extruding a closed edge or a closed wire will yield a solid. If False, a shell will result.

-   **Reversed**: reverses the extrusion to go against **Dir**.

-   **Symmetric**: if True, extrusion is centered at the input shape, and total length is **Length Fwd**. **Length Rev** is ignored.


<div class="mw-translate-fuzzy">

-   **Taper Angle** and **Taper Angle Rev**: applies an angle to the extrusion, so that sides of the extrusion are drafted by the specified angle. Positive angle means the cross-section expands. **Taper Angle Rev** sets the taper for the reversed part of the extrusion (the part from **Length Rev**). As of v0.17, tapered extrusion is only supported for wires with no holes.


</div>

-   **Face Maker Class**: sets C++ class name of face making code, which is used when making solids from wires. This property is here mainly for maintaining backward compatibility. Do not touch, unless you know what you are doing.

-   **Placement**: the standard [placement](Placement.md) parameters


<div class="mw-translate-fuzzy">

-   **Label**: label to be shown in the Model tree (not available on Extrude creation)


</div>

## Task dialog {#task_dialog}

![](images/Part_Extrude_dialog.png )


<div class="mw-translate-fuzzy">

-   OK: creates the extrusion, and closes the dialog.


</div>


<div class="mw-translate-fuzzy">

-   Close: closes dialog, without doing anything.


</div>


<div class="mw-translate-fuzzy">

-   Apply: creates the extrusion, but does not close the dialog. You can then select another shape in the list on the bottom, and create more extrusions. Clicking Apply may times creates many extrusions.


</div>

-   \'Direction\' radio buttons: set the way extrusion direction is computed.


<div class="mw-translate-fuzzy">

-   \'Select\' button: click it, and then pick an edge in 3D view. That edge will appear in text field next to the button, in format \"ObjectName:EdgeN\". You can also type the link manually. Values X,Y,Z will be filled according to the edge direction.


</div>


<div class="mw-translate-fuzzy">

-   X, Y, Z buttons: click X button to set extrusion direction to +X axis. Click it again to set -X axis.


</div>


<div class="mw-translate-fuzzy">

-   X,Y,Z input fields: set or display the direction vector of extrusion. If both lengths are zero, the length of this vector sets the length of extrusion, and values are always in mm, regardless of unit preferences.


</div>

-   Length fields: set length of extrusion. These input fields have unit support.

-   Symmetric: spreads out the extrusion into both directions, so that the profile remains in the middle.

-   Taper Outward Angle: positive angle means profile is expanded at other end of extrusion.

-   Create Solid checkbox: if checked, extruding a closed wire or edge will yield a solid. It is checked by default, if a closed wire was preselected before invoking Part Extrude.

-   Shape list: here you select, what shapes to extrude. If multiple objects are selected, multiple Extrude objects are created.


<div class="mw-translate-fuzzy">

## Contra intuitive/Gotchas {#contra_intuitivegotchas}

Dialogul Extrude Parts nu are încă o previzualizare. \"Aplicați\" creează un obiect de extrudare de fiecare dată când faceți clic pe el, ceea ce poate fi util ca previzualizare. Cu toate acestea, acestea vor rămâne și un altul va fi creat când faceți clic pe OK.[Undo](Std_Undo.md) can be useful to clean them up before clicking OK.


</div>


<div class="mw-translate-fuzzy">

Since v0.17, a sketch created from within PartDesign cannot be used for Part Extrude, if it is within a Body (\"Links go out of allowed scope\" error). In order to Part-Extrude a sketch, you should *create the sketch from Sketcher workbench*. Or you can just drag a PartDesign one out of a Body.


</div>


<div class="mw-translate-fuzzy">

Extrusion with taper angle does not support holes. It also may give bogus results if the number of segments in the profile changes as a result of taper.


</div>


<div class="mw-translate-fuzzy">

## Comparison with [PartDesign Pad](PartDesign_Pad.md) {#comparison_with_partdesign_pad}


</div>

PartDesign Pad este, de asemenea, o funcți(e)onalitate de extrudare, dar există diferențe importante.

Part Extrude always creates a standalone shape. PartDesign Pad fuses the extrusion result to the rest of the Body.


<div class="mw-translate-fuzzy">

Part Extrude doesn\'t care where it is in model tree. PartDesign Pad can only live inside a [PartDesign Body](PartDesign_Body.md).


</div>

Part Extrude poate extruda orice obiect care are Part Geometry (forma OCC), cu excepția solidelor și compsolids. Și nu poate extruda fațetele individuale ale altor obiecte. PartDesign Pad va accepta doar o schiță ca profil (și o mică selecție de alte tipuri de obiecte) sau o fațetă a unui solid.





  
