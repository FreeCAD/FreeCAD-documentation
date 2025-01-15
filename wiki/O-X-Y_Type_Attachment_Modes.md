# O-X-Y Type Attachment Modes
Here we provide more detailed information on the use of **Align O-X-Y** type modes in the [Part Attachment editor](Part_EditAttachment.md).

These modes are:

-   Align O-Z-X
-   Align O-Z-Y
-   Align O-X-Y
-   Align O-X-Z
-   Align O-Y-Z
-   Align O-Y-X

These modes are used to attach to a specified vertex, with an orientation determined by reference to other vertices or edges.


**Reference1**

must be a vertex. The origin is mapped to this selected point.

Note: If an edge is selected for **Reference1**, O-X-Y type modes are not offered.


**Reference2**

and **Reference3** must be either vertices or edges. They provide direction information. For a vertex, the direction is from the origin to the selected vertex. For an edge, it is the direction of the edge. **Reference3** is optional.

Take mode O-X-Z as an example:

-   The **O** represents the origin, corresponding to **Reference1**.
-   The **X** indicates that the X-axis of the attached object is to be aligned with the direction of **Reference2**.
-   The **Z** indicates that the Z-axis of the attached object is to be aligned with the component of the direction of **Reference3** at right angles to the X-axis.
-   The **Y**-axis completes the orthogonal right-hand axis triad.

For other modes, the axes are mapped in a corresponding fashion.

If **Reference3** is not provided, FreeCAD makes default choices for it.

 {{Part_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > O-X-Y Type Attachment Modes
