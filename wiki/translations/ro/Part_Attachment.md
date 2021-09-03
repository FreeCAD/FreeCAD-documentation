---
- GuiCommand:/ro
   Name/ro:Part Attachment
   Empty:1
   Workbenches:[Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md)
   MenuLocation:Part → Attachment...
   SeeAlso:[[Placement]]
   Version:0.17
---


</div>


<div class="mw-translate-fuzzy">

## Descriere


</div>

**Attachment** este un utilitar pentru asocierea unui obiect cu altul. Obiectul asociat este legat de celălalt obiect, ceea ce înseamnă că dacă poziționarea acestuia este modificată ulterior, obiectul asociat se actualizează în noua sa poziție.


<div class="mw-translate-fuzzy">

## Cum se foloseste {#cum_se_foloseste}


</div>


<div class="mw-translate-fuzzy">

1.  Selectați obiectul de atașat.
2.  Mergeți la meniul **Part → Attachment\...**.

    :   **Notă**: Atunci când se lucrează în [PartDesign](PartDesign_Workbench.md) pentru a crea schițe, geometrie de referință sau primitive, etapele 1 și 2 nu sunt necesare: caseta de dialog Atașamentul este activat automat.
3.  Mai jos, în parametrii **Attachment**, *Not attached* poate fi citit. Primul buton de jos este etichetat **Selecting…** pentru a indica că se așteaptă o selecție în vizualizarea 3D .
4.  Selectați un element topologic pe obiectul care urmează să fie asociat: un vârf, o margine, o fațetă sau un plan. De asemenea, pot fi selectate geometrii de referință ale unei piese [Part containers](Std_Part.md) .
5.  Eticheta primului buton adoptă acum tipul de topologie selectat. În câmpul alb spre dreapta, se adaugă obiectul de referință și elementul său de referință. De exemplu, dacă o fațetă este selectată pe o primitivă tip cub, câmpul arată Box:Face6.
6.  Selectați un [Attachment mode](#Attachment_mode.md) din listă. Modurile disponibile sunt filtrate prin referințele selectate. Sub titlul *Attached with mode * este afișat sub antetul/headerul **Attachment**.

    :   Pentru informații în timp real despre modul de asociere, plasați cursorul mouse-ului peste unul dintre modurile în listă pentru a afișa un indiciu.
7.  Opțional, adăugați până la 3 referințe apăsând butoanele **Reference2**, **Reference3**, și **Reference4** și repetând pasul 4.
8.  Optional deefiniți un [Attachment Offset](#Attachment_Offset.md).
9.  Apăsați **OK**.


</div>


<div class="mw-translate-fuzzy">

## Opţiuni


</div>


<div class="mw-translate-fuzzy">

![ right](images/Part_Offset_Tasks.png )


</div>


<div class="mw-translate-fuzzy">

### Atașament


</div>


<div class="mw-translate-fuzzy">

#### Dezactivat


</div>


<div class="mw-translate-fuzzy">

Default, no reference selected .


</div>


<div class="mw-translate-fuzzy">

#### Muchie Normal {#muchie_normal}


</div>


<div class="mw-translate-fuzzy">

Object is made perpendicular to edge. Optional vertex reference defines location .


</div>

:; Reference combinations:

:   Edge
:   Edge, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-N-X {#align_o_n_x}


</div>


<div class="mw-translate-fuzzy">

Matches object\'s origin with first referenced vertex, then aligns its normal and horizontal plane axis toward vertex/along line .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-N-Y {#align_o_n_y}


</div>


<div class="mw-translate-fuzzy">

Matches object\'s origin with first referenced vertex and aligns its normal and vertical plane axis toward vertex/along line .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-X-Y {#align_o_x_y}


</div>


<div class="mw-translate-fuzzy">

Matches object\'s origin with first referenced vertex and aligns its horizontal and vertical plane axes toward vertex/along line .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-X-N {#align_o_x_n}


</div>


<div class="mw-translate-fuzzy">

Matches object\'s origin with first referenced vertex and aligns its horizontal plane axis and normal toward vertex/along line .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-Y-N {#align_o_y_n}


</div>


<div class="mw-translate-fuzzy">

Matches object\'s origin with first referenced vertex and aligns its vertical plane axis and normal toward vertex/along line .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-Y-X {#align_o_y_x}


</div>


<div class="mw-translate-fuzzy">

Matches object\'s origin with first referenced vertex and aligns its vertical and horizontal plane axes toward vertex/along line .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Translatarea originii {#translatarea_originii}


</div>


<div class="mw-translate-fuzzy">

Object\'s origin is aligned to matched vertex. Orientation is controlled by [Placement](Placement.md) property.


</div>

:; Reference combinations:

:   Vertex.


<div class="mw-translate-fuzzy">

#### Object\'s XY {#objects_xy}


</div>


<div class="mw-translate-fuzzy">

Plane is aligned to XY local plane of linked object .


</div>

:; Reference combinations:

:   Any, Conic.


<div class="mw-translate-fuzzy">

#### Object\'s XZ {#objects_xz}


</div>


<div class="mw-translate-fuzzy">

Plane is aligned to XZ local plane of linked object .


</div>

:; Reference combinations:

:   Any, Conic.


<div class="mw-translate-fuzzy">

#### Object\'s YZ {#objects_yz}


</div>


<div class="mw-translate-fuzzy">

Plane is aligned to YZ local plane of linked object .


</div>

:; Reference combinations:

:   Any, Conic


<div class="mw-translate-fuzzy">

#### Plane face {#plane_face}


</div>


<div class="mw-translate-fuzzy">

Plane is aligned to coincide to planar face .


</div>

:; Reference combinations:

:   Plane


<div class="mw-translate-fuzzy">

#### Tangent to surface {#tangent_to_surface}


</div>


<div class="mw-translate-fuzzy">

Plane is made tangent to surface at vertex .


</div>

:; Reference combinations:

:   Face, Vertex
:   Vertex, Face


<div class="mw-translate-fuzzy">

#### Frenet NB {#frenet_nb}


</div>

Plane is set to normal-binormal (NB) axes of [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) at the point of the edge\'s curve that is closest to the vertex (or defined by MapPathParameter property, if vertex is not linked). The object\'s origin is translated to the vertex if the vertex is first, or kept at the curve if edge is first. This mode is similar to *Normal to edge*, except that X axis is well-defined.

:;Reference combinations:

:   Curve
:   Curve, Vertex
:   Vertex, Curve
:   <img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">


<div class="mw-translate-fuzzy">

#### Frenet TN {#frenet_tn}


</div>

Plane is set to tangent-normal (TN) axes of [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) at the point of the edge\'s curve that is closest to the vertex (or defined by MapPathParameter property, if vertex is not linked). The origin of sketch is translated to the vertex if the vertex is first, or kept at the curve if edge is first. Effectively, if the curve is planar, the sketching plane is the plane of the curve.

:;Reference combinations:

:   Curve
:   Curve, Vertex
:   Vertex, Curve
:   <img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">


<div class="mw-translate-fuzzy">

#### Frenet TB {#frenet_tb}


</div>

Plane is set tangent-binormal (TB) axes of [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) at the point of the edge\'s curve that is closest to the vertex (or defined by MapPathParameter property, if vertex is not linked). The origin of sketch is translated to the vertex if the vertex is first, or kept at the curve if edge is first.

:;Reference combinations:

:   Curve
:   Curve, Vertex
:   Vertex, Curve
:   <img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">


<div class="mw-translate-fuzzy">

#### Concentric


</div>


<div class="mw-translate-fuzzy">

Aligns to plane to osculating circle of an edge. Optional Vertex link defines where .


</div>

:; Reference combinations:

:   Curve
:   Circle
:   Curve, Vertex
:   Circle, Vertex
:   Vertex, Curve
:   Vertex, Circle


<div class="mw-translate-fuzzy">

#### Revolution Section {#revolution_section}


</div>


<div class="mw-translate-fuzzy">

Plane is perpendicular to edge, and Y axis is matched with axis of osculating circle. Optional Vertex link defines where .


</div>

:; Reference combinations:

:   Curve
:   Circle
:   Curve, Vertex
:   Circle, Vertex
:   Vertex, Curve
:   Vertex, Circle


<div class="mw-translate-fuzzy">

#### Plane by 3 points {#plane_by_3_points}


</div>


<div class="mw-translate-fuzzy">

Aligns XY plane to pass through three vertices .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Line, Vertex
:   Vertex, Line
:   Line, Line


<div class="mw-translate-fuzzy">

#### Normal to 3 points {#normal_to_3_points}


</div>


<div class="mw-translate-fuzzy">

Aligns plane to pass through first two vertices, and perpendicular to plane that passes through 3 vertices .


</div>

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Line, Vertex
:   Vertex, Line
:   Line, Line


<div class="mw-translate-fuzzy">

#### Folding


</div>


<div class="mw-translate-fuzzy">

Specialty mode for folding polyhedra. Select 4 edge in order: foldable edge, fold line, other fold line, other foldable edge. Plane will be aligned to folding the first edge. In the picture below, it is not required that both leafs to fold together be the same .


</div>

:; Reference combinations

:   Line, Line, Line, Line
:   ![ 250px](images/Attacher_mode_Folding.png )


<div class="mw-translate-fuzzy">

#### Inertia 2-3 {#inertia_2_3}


</div>


<div class="mw-translate-fuzzy">

Object will be attached to a plane passing through second and third principal axes of inertia (passes through center of mass) .


</div>

:; Reference combinations:

:   Any
:   Any, Any
:   Any, Any, Any
:   Any, Any, Any, Any


<div class="mw-translate-fuzzy">

### Attachment Offset {#attachment_offset}


</div>


<div class="mw-translate-fuzzy">

Attachment Offset is used to apply a linear or rotary offset from the referenced object. It becomes active when an attachment mode other than *Deactivated* has been selected .


</div>


<div class="mw-translate-fuzzy">

-   **X**: sets an offset distance in the X axis of the reference object .


</div>


<div class="mw-translate-fuzzy">

-   **Y**: sets an offset distance in the Y axis of the reference object .


</div>


<div class="mw-translate-fuzzy">

-   **Z**: sets an offset distance in the Z axis of the reference object .


</div>


<div class="mw-translate-fuzzy">

-   **Yaw**: rotates the attached object along the reference object\'s Z axis .


</div>


<div class="mw-translate-fuzzy">

-   **Pitch**: rotates the attached object along the reference object\'s Y axis .


</div>


<div class="mw-translate-fuzzy">

-   **Roll**: rotates the attached object along the reference object\'s X axis .


</div>


<div class="mw-translate-fuzzy">

-   **Flip sides**: if checked, the attached object is reversed from its XY plane .


</div>


<div class="mw-translate-fuzzy">

## Limite


</div>


<div class="mw-translate-fuzzy">

-   Containerele [Part](Std_Part.md) și [Body](PartDesign_Body.md) nu sunt suportate. În timp ce este posibil să se utilizeze Atașament pentru a le alinia, atașamentul nu va fi legat parametric.


</div>





{{Part_Tools_navi

}} 
