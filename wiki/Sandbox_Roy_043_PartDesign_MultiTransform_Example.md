# Sandbox:Roy 043 PartDesign MultiTransform Example
## Example

You can use this tool to create a fully parametric part that is symmetrical about two axes from a sketch.

This could be a 150x100x10mm large mounting plate for a motor with symmetric holes.

<img alt="" src=images/PartDesign_MultiTransform_Example2.png  style="width   *400px;">

1.  Create a <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [Body](PartDesign_Body.md) and add a <img alt="" src=images/PartDesign_NewSketch.svg  style="width   *16px;"> [sketch](PartDesign_NewSketch.md) on one of its base planes.
2.  In the sketch create geometry for one quadrant of the part (i.e. the upper right quadrant).
    -   Note that the constraints must also only cover a quarter of the part, e.g. instead of the full dimension of {{Value|150mm}} enter {{Value|150/2mm}} or {{Value|75mm}}.
    -   Make sure the sketch is closed by adding lines along the vertical and horizontal axes.
3.  Extrude the part with <img alt="" src=images/PartDesign_Pad.svg  style="width   *16px;"> [PartDesign Pad](PartDesign_Pad.md).
4.  Select <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> 
**PartDesign MultiTransform**
5.  The task dialog opens.
6.  The last feature of the Body is already selected. Since we want to mirror that feature we can ignore the **Add feature** or **Remove feature** buttons.
7.  Right-click in the **Transformations** field and select **Add mirrored transform** from the context menu.
8.  For the **Plane** select **Vertical sketch axis**.
9.  If the **Update view** checkbox is checked, you should now see the part mirrored about one axis.
10. Again select **Add mirrored transform** from the context menu of the **Transformations** field.
11. Now for the **Plane** select **Horizontal sketch axis**.
12. To remove the edges along the axes of symmetry in the final result, in the [Property editor](Property_editor.md) set the **Refine** property of the new feature to {{Value|true}}.

To verify that the part is fully parametric open the initial sketch with the quarter part and change one dimension, say a hole position. After closing the sketch the three other holes will have changed accordingly. This works with all other dimensions as well. A sketch modelling the full part with a single extrusion and no mirroring would be a lot more complex and all later changes would be more complicated.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Sandbox:Roy 043 PartDesign MultiTransform Example
