# O-X-Y type attachment modes
Here we provide more detailed information on the use of **Align O-X-Y** type modes in the [Part_EditAttachment](Part_EditAttachment.md) attachment editor. These modes are

-   Align O-X-Y
-   Align O-X-Z
-   Align O-Y-X
-   Align O-Y-Z
-   Align O-Z-X
-   Align O-Z-Y

These modes are used to attach to a specified vertex, with an orientation determined by reference to other vertices or edges.


**Reference1**

must be a Vertex. The origin is mapped to this selected point. (Note   * If an edge *is* selected for **Reference1**, O-X-Y type modes are not offered.)


**Reference2**

and **Reference3** must be either Vertices or Edges. They provide direction information. For a Vertex, the direction is from the origin to the selected vertex. For an Edge it is the direction of the edge. **Reference3** is optional.

Take mode O-X-Z as an example.

-   The \'O\' represents the origin, corresponding to the **Reference1**.
-   The \'X\' indicates that the X-axis of the attached object is to be aligned with the direction of **Reference2**
-   The \'Z\' indicates that the Z-axis of the attached object is to be aligned with the component of the direction of **Reference3** at right angles to the X-axis.
-   The \'Y\'-axis completes the orthogonal right-hand axis triad.

For other modes, the axes are mapped in the corresponding fashion.

If **Reference3** is not provided, FreeCAD makes default choices for it. For modes O-X-Y, O-X-Z, O-Y-X and O-Y-Z **Reference3** is taken to align with the global Z-axis. For modes O-Z-X and O-Z-Y **Reference3** is taken to be the global Y-axis.



---
![](images/Right_arrow.png) [documentation index](../README.md) > O-X-Y type attachment modes
