---
- GuiCommand:/ro
   Name/ro:Part Attachment
   Empty:1
   Workbenches:[Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md)
   MenuLocation:Part → Attachment...
   SeeAlso:[[Placement]]
   Version:0.17
---

# Part EditAttachment/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

**Attachment** este un utilitar pentru asocierea unui obiect cu altul. Obiectul asociat este legat de celălalt obiect, ceea ce înseamnă că dacă poziționarea acestuia este modificată ulterior, obiectul asociat se actualizează în noua sa poziție.


</div>

## Cum se foloseste 

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

## Opţiuni


<div class="mw-translate-fuzzy">

![ right](images/Part_Offset_Tasks.png )


</div>

### Atașament

#### Dezactivat

Default, no reference selected .

#### Muchie Normal 

Object is made perpendicular to edge. Optional vertex reference defines location .

:; Reference combinations:

:   Edge
:   Edge, Vertex
:   Vertex, Edge

See [Align O-X-Y type attachment modes](O-X-Y_type_attachment_modes.md) for more details on the following modes:


<div class="mw-translate-fuzzy">

#### Align O-N-X 


</div>

Matches object\'s origin with first referenced vertex, then aligns its normal and horizontal plane axis toward vertex/along line .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-N-Y 


</div>

Matches object\'s origin with first referenced vertex and aligns its normal and vertical plane axis toward vertex/along line .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Align O-X-Y 

Matches object\'s origin with first referenced vertex and aligns its horizontal and vertical plane axes toward vertex/along line .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-X-N 


</div>

Matches object\'s origin with first referenced vertex and aligns its horizontal plane axis and normal toward vertex/along line .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge


<div class="mw-translate-fuzzy">

#### Align O-Y-N 


</div>

Matches object\'s origin with first referenced vertex and aligns its vertical plane axis and normal toward vertex/along line .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Align O-Y-X 

Matches object\'s origin with first referenced vertex and aligns its vertical and horizontal plane axes toward vertex/along line .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Translatarea originii 

Object\'s origin is aligned to matched vertex. Orientation is controlled by [Placement](Placement.md) property.

:; Reference combinations:

:   Vertex.

#### Object\'s XY 

Plane is aligned to XY local plane of linked object .

:; Reference combinations:

:   Any, Conic.

#### Object\'s XZ 

Plane is aligned to XZ local plane of linked object .

:; Reference combinations:

:   Any, Conic.

#### Object\'s YZ 

Plane is aligned to YZ local plane of linked object .

:; Reference combinations:

:   Any, Conic

#### Plane face 

Plane is aligned to coincide to planar face .

:; Reference combinations:

:   Plane

#### Tangent to surface 

Plane is made tangent to surface at vertex .

:; Reference combinations:

:   Face, Vertex
:   Vertex, Face

#### Frenet NB 

Plane is set to normal-binormal (NB) axes of [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) at the point of the edge\'s curve that is closest to the vertex (or defined by MapPathParameter property, if vertex is not linked). The object\'s origin is translated to the vertex if the vertex is first, or kept at the curve if edge is first. This mode is similar to *Normal to edge*, except that X axis is well-defined.

:;Reference combinations:

:   Curve
:   Curve, Vertex
:   Vertex, Curve
:   <img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">

#### Frenet TN 

Plane is set to tangent-normal (TN) axes of [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) at the point of the edge\'s curve that is closest to the vertex (or defined by MapPathParameter property, if vertex is not linked). The origin of sketch is translated to the vertex if the vertex is first, or kept at the curve if edge is first. Effectively, if the curve is planar, the sketching plane is the plane of the curve.

:;Reference combinations:

:   Curve
:   Curve, Vertex
:   Vertex, Curve
:   <img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">

#### Frenet TB 

Plane is set tangent-binormal (TB) axes of [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) at the point of the edge\'s curve that is closest to the vertex (or defined by MapPathParameter property, if vertex is not linked). The origin of sketch is translated to the vertex if the vertex is first, or kept at the curve if edge is first.

:;Reference combinations:

:   Curve
:   Curve, Vertex
:   Vertex, Curve
:   <img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">

#### Concentric

Aligns to plane to osculating circle of an edge. Optional Vertex link defines where .

:; Reference combinations:

:   Curve
:   Circle
:   Curve, Vertex
:   Circle, Vertex
:   Vertex, Curve
:   Vertex, Circle

#### Revolution Section 

Plane is perpendicular to edge, and Y axis is matched with axis of osculating circle. Optional Vertex link defines where .

:; Reference combinations:

:   Curve
:   Circle
:   Curve, Vertex
:   Circle, Vertex
:   Vertex, Curve
:   Vertex, Circle

#### Plane by 3 points 

Aligns XY plane to pass through three vertices .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Line, Vertex
:   Vertex, Line
:   Line, Line

#### Normal to 3 points 

Aligns plane to pass through first two vertices, and perpendicular to plane that passes through 3 vertices .

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Line, Vertex
:   Vertex, Line
:   Line, Line

#### Folding


<div class="mw-translate-fuzzy">

Specialty mode for folding polyhedra. Select 4 edge in order: foldable edge, fold line, other fold line, other foldable edge. Plane will be aligned to folding the first edge. In the picture below, it is not required that both leafs to fold together be the same .


</div>

:; Reference combinations

:   Line, Line, Line, Line
:   ![ 250px](images/Attacher_mode_Folding.png )

#### Inertia 2-3 

Object will be attached to a plane passing through second and third principal axes of inertia (passes through center of mass) .

:; Reference combinations:

:   Any
:   Any, Any
:   Any, Any, Any
:   Any, Any, Any, Any

### Attachment Offset 

Attachment Offset is used to apply a linear or rotary offset from the referenced object. It becomes active when an attachment mode other than *Deactivated* has been selected .

-   **X**: sets an offset distance in the X axis of the reference object .

-   **Y**: sets an offset distance in the Y axis of the reference object .

-   **Z**: sets an offset distance in the Z axis of the reference object .

-   **Yaw**: rotates the attached object along the reference object\'s Z axis .

-   **Pitch**: rotates the attached object along the reference object\'s Y axis .

-   **Roll**: rotates the attached object along the reference object\'s X axis .

-   **Flip sides**: if checked, the attached object is reversed from its XY plane .

## Limite

-   Containerele [Part](Std_Part.md) și [Body](PartDesign_Body.md) nu sunt suportate. În timp ce este posibil să se utilizeze Atașament pentru a le alinia, atașamentul nu va fi legat parametric.





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/ro
