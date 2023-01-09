---
- GuiCommand:
   Name:Part EditAttachment
   MenuLocation:Part → Attachment...
   Workbenches:[Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[Placement](Placement.md), [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md), [Part Part2DObject](Part_Part2DObject.md)
---

# Part EditAttachment/pl

## Opis

**Part EditAttachment** is a utility to attach an object to another one. The attached object is linked to the other object, which means that if the latter\'s placement is changed afterwards, the attached object will update to its new position.

## Użycie

1.  Select the object to be attached.
2.  Go to the **Part → Attachment\...** menu.

    :   **Note**: when working in [PartDesign](PartDesign_Workbench.md) and creating sketches, datum geometry or primitives, steps 1 and 2 are unnecessary: the Attachment dialogue is brought up automatically.
3.  Under **Attachment** parameters, *Not attached* can be read. The first button below is labeled **Selecting…** to indicate it is expecting a selection in the 3D view.
4.  Select a topology element on the object to attach to: vertex, edge or face/plane. Datum geometry from [Part containers](Std_Part.md) are also selectable.
5.  The first button\'s label now adopts the type of topology selected. In the white field to its right, the referenced object and its element is added. For example, if a face on a primitive cube is selected, the field will show Box:Face6.
6.  Select an [Attachment mode](#Attachment_mode.md) in the list. The available modes are filtered by the selected references. *Attached with mode * will be displayed under the **Attachment** header.

    :   For live information on the attachment modes, hover the mouse on top of one of the modes in the list for a tooltip to appear.
7.  Optionally, add up to 3 more references by pressing the **Reference2**, **Reference3**, and **Reference4** buttons and repeating step 4.
8.  Optionally set an [Attachment Offset](#Attachment_Offset.md).
9.  Press **OK**.

## Opcje

<img alt="" src=images/Part_Offset_Tasks.png  style="width:250px;">

### Tryb dołączenia 

#### Nieaktywny

Default, no reference selected.

#### Normalna do krawędzi 

Object is made perpendicular to edge. Optional vertex reference defines location.

:; Reference combinations:

:   Edge
:   Edge, Vertex
:   Vertex, Edge

See [Align O-X-Y type attachment modes](O-X-Y_type_attachment_modes.md) for more details on the following modes:

#### Align O-Z-X 

Matches object\'s origin with first referenced vertex, then aligns its normal and horizontal plane axis toward vertex/along line.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Align O-Z-Y 

Matches object\'s origin with first referenced vertex and aligns its normal and vertical plane axis toward vertex/along line.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Align O-X-Y 

Matches object\'s origin with first referenced vertex and aligns its horizontal and vertical plane axes toward vertex/along line.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Align O-X-Z 

Matches object\'s origin with first referenced vertex and aligns its horizontal plane axis and normal toward vertex/along line.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Align O-Y-Z 

Matches object\'s origin with first referenced vertex and aligns its vertical plane axis and normal toward vertex/along line.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Align O-Y-X 

Matches object\'s origin with first referenced vertex and aligns its vertical and horizontal plane axes toward vertex/along line.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Vertex, Vertex, Edge
:   Vertex, Edge, Vertex
:   Vertex, Edge, Edge
:   Vertex, Vertex
:   Vertex, Edge

#### Translate origin 

Object\'s origin is aligned to matched vertex. Orientation is controlled by [Placement](Placement.md) property.

:; Reference combinations:

:   Vertex.

#### Object\'s XY 

Plane is aligned to XY local plane of linked object.

:; Reference combinations:

:   Any, Conic.

#### Object\'s XZ 

Plane is aligned to XZ local plane of linked object.

:; Reference combinations:

:   Any, Conic.

#### Object\'s YZ 

Plane is aligned to YZ local plane of linked object.

:; Reference combinations:

:   Any, Conic

#### Plane face 

Plane is aligned to coincide to planar face.

:; Reference combinations:

:   Plane

#### Tangent to surface 

Plane is made tangent to surface at vertex.

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

Aligns to plane to osculating circle of an edge. Optional Vertex link defines where.

:; Reference combinations:

:   Curve
:   Circle
:   Curve, Vertex
:   Circle, Vertex
:   Vertex, Curve
:   Vertex, Circle

#### Revolution Section 

Plane is perpendicular to edge, and Y axis is matched with axis of osculating circle. Optional Vertex link defines where.

:; Reference combinations:

:   Curve
:   Circle
:   Curve, Vertex
:   Circle, Vertex
:   Vertex, Curve
:   Vertex, Circle

#### Plane by 3 points 

Aligns XY plane to pass through three vertices.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Line, Vertex
:   Vertex, Line
:   Line, Line

#### Normal to 3 points 

Aligns plane to pass through first two vertices, and perpendicular to plane that passes through 3 vertices.

:; Reference combinations:

:   Vertex, Vertex, Vertex
:   Line, Vertex
:   Vertex, Line
:   Line, Line

#### Folding

Specialty mode for folding polyhedra. Select 4 edge in order: glueable edge, fold line, other fold line, other glueable edge. Plane will be aligned to folding the first edge. In the picture below, it is not required that both leafs to fold together be the same.

:; Reference combinations

:   Line, Line, Line, Line
:   ![ 250px](images/Attacher_mode_Folding.png )

#### Bezwładność 2-3 

Object will be attached to a plane passing through second and third principal axes of inertia (passes through center of mass).

:; Reference combinations:

:   Any
:   Any, Any
:   Any, Any, Any
:   Any, Any, Any, Any

### Attachment Offset 

Attachment Offset is used to apply a linear or rotary offset from the referenced object. That means the offsets are relative to the *local* coordinate system, not to the global. It becomes active when an attachment mode other than *Deactivated* has been selected.

-   **X**: sets an offset distance in the X axis of the reference object.

-   **Y**: sets an offset distance in the Y axis of the reference object.

-   **Z**: sets an offset distance in the Z axis of the reference object. This coordinate is to be used for the frequent use case that you want to offset a sketch perpendicular to the plane.

-   **Yaw**: rotates the attached object along the reference object\'s Z axis.

-   **Pitch**: rotates the attached object along the reference object\'s Y axis.

-   **Roll**: rotates the attached object along the reference object\'s X axis.

-   **Flip sides**: if checked, the attached object is reversed from its XY plane.

## Ograniczenia

-   [Part](Std_Part.md) and [Body](PartDesign_Body.md) containers are not supported. While it\'s possible to use Attachment to align them, the attachment won\'t be parametrically linked.
-   If selecting two lines results in a traceback with \"points are collinear. Can\'t make a plane\", try selecting three points instead [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594).





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/pl
