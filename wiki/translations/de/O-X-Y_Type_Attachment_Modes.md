# O-X-Y Type Attachment Modes/de
Hier werden detailliertere Informationen zur Anwendung der Befestigungsverfahren der Art **Ausrichten O-X-Y** unter [Part Befestigen](Part_EditAttachment/de.md).

Diese Verfahren sind:

-   Ausrichten O-Z-X
-   Ausrichten O-Z-Y
-   Ausrichten O-X-Y
-   Ausrichten O-X-Z
-   Ausrichten O-Y-Z
-   Ausrichten O-Y-X


<div lang="en" dir="ltr" class="mw-content-ltr">

These modes are used to attach to a specified vertex, with an orientation determined by reference to other vertices or edges.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


**Reference1**

must be a vertex. The origin is mapped to this selected point.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Note: If an edge is selected for **Reference1**, O-X-Y type modes are not offered.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


**Reference2**

and **Reference3** must be either vertices or edges. They provide direction information. For a vertex, the direction is from the origin to the selected vertex. For an edge, it is the direction of the edge. **Reference3** is optional.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Take mode O-X-Z as an example:

-   The **O** represents the origin, corresponding to **Reference1**.
-   The **X** indicates that the X-axis of the attached object is to be aligned with the direction of **Reference2**.
-   The **Z** indicates that the Z-axis of the attached object is to be aligned with the component of the direction of **Reference3** at right angles to the X-axis.
-   The **Y**-axis completes the orthogonal right-hand axis triad.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

For other modes, the axes are mapped in a corresponding fashion.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If **Reference3** is not provided, FreeCAD makes default choices for it.


</div>


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > O-X-Y Type Attachment Modes/de
