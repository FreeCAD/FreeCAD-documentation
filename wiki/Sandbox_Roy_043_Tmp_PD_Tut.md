# Sandbox:Roy 043 Tmp PD Tut
### Applying constraints 

The rectangle already has 8 constraints that have been applied automatically   * 4 <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *24px;"> [coincident constraints](Sketcher_ConstrainCoincident.md), 2 <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width   *24px;"> [horizontal constraints](Sketcher_ConstrainHorizontal.md) and 2 <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width   *24px;"> [vertical constraints](Sketcher_ConstrainVertical.md). To fully constrain the rectangle apply the following additional constraints   *

<img alt="Fig   * 1" src=images/Pd_tut_rect_h_dim_end.png  style="width   *300px;">

A horizontal distance constraint   *

1.  Select the upper line of the rectangle by clicking it with the left mouse button.
2.  Press the <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width   *24px;"> button to apply a [horizontal distance constraint](Sketcher_ConstrainDistanceX.md).
3.  A dimension will appear between end points of the line. The current horizontal distance between the points is indicated.
4.  Additionally a dialog will appear   *
    ![dimension dialog](images/Pd_tut_rect03.png )
5.  Assign **Length = 53mm**.
6.  To be able to reference the dimension later a name is required as well   * assign **Name = length**.
7.  Press the **OK** button.
8.  The result should resemble **Fig   * 1**.





<img alt="Fig   * 2" src=images/Pd_tut_rect04.png  style="width   *300px;">

A symmetrical constraint   *

1.  Select the top left corner and top right corner of the rectangle, and then select the origin of the sketch. The selection order of the points is important.
2.  Press the <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *32px;"> button to apply a [symmetrical constraint](Sketcher_ConstrainSymmetric.md).
3.  Because the upper line is horizontal this constraint also fixes the position of upper line of the rectangle relative to the origin of the sketch.
4.  The result should resemble **Fig   * 2**. The light green color of the upper line indicates that it is already fully constrained.





<img alt="Fig   * 3" src=images/Pd_tut_rect_v3.png  style="width   *300px;">

A vertical distance constraint   *

1.  Select left line of the rectangle.
2.  Press the <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width   *24px;"> button to apply a [vertical distance constraint](Sketcher_ConstrainDistanceY.md).
3.  Assign **Length = 26 mm** and **Name = width**.
4.  Press the **OK** button.
5.  The result should resemble **Fig   * 3**. The bright green color indicates that the whole sketch is fully constrained.





[Category   *Sandbox](Category_Sandbox.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Sandbox:Roy 043 Tmp PD Tut
