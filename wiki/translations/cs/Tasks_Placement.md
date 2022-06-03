# Tasks Placement/cs
## Popis

Command for modifying **Placement**. These options relate only to the position and orientation of the object in space, they do not affect other attributes of the shape. The placement is stored internally as a position, and a rotation (rotation axis and angle transformed into a [quaternion](https   *//en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). While there are several methods to specify a rotation, for instance with a rotation center, this is only used to affect the rotation computation and is not stored for later operations. Similarly, if a rotation axis of (1,1,1) is specified, it may be normalized when stored in the quaternion and appear as (0.58, 0.58, 0.58) when browsing the object later.

## Usage

The function **Placement** can be accessed in several ways   *

-   via [script](Python_scripting_tutorial#Vecteurs_et_Positions.md) Python in the console and its [API](Placement_API.md).

   *   ![Scripting Placement as y/p/r and Matrix](images/PlacePyConv10.png )

-   or, in the window **Combo View → Properties → Data → Placement → **...****,

   *   ![Task\_Placement](images/Tache_Placement_fr_01.png )

-   or by the menu **Edit → Placement\...**.

### Enable Placement in Combo View 

-   Click a shape to select it.
-   Click **Placement** (the title, not the little arrow), and a button with an ellipsis **...** appears   * <img alt="Tache\_Placement" src=images/Tache_Placement_01_fr_00.png  style="width   *256px;">
-   Click on the ellipsis, and the **Placement Dialog** is displayed   *

   *   ![](images/Tache_Placement_en_02.png )

### Options


{{TitleProperty|Translation}}

-    {{TasksTag|X}}<img alt="Translation in X direction (Click to enlarge)" src=images/Tache_Placement_Translation_X_fr.gif  style="width   *150px;"> Moves the coordinate system of the object in the **X** direction in relation to the axis coordinates of origin 0, 0, 0.

-    {{TasksTag|Y}}<img alt="Translation in the Y direction (Click to enlarge)" src=images/Tache_Placement_Translation_Y_fr.gif  style="width   *150px;"> Moves the coordinate system of the object in the **Y** direction in relation to the axis coordinates of origin 0, 0, 0.

-    {{TasksTag|Z}}<img alt="Translation in the Z direction (Click to enlarge)" src=images/Tache_Placement_Translation_Z_fr.gif  style="width   *150px;"> Moves the coordinate system of the object in the **Z** direction in relation to the axis coordinates of origin 0, 0, 0.


{{TitleProperty|Center}}

-    {{TasksTag|X}}   * Move the center of rotation in the direction **X**, from the coordinates of the selected object. (default   * 0,0,0).

-    {{TasksTag|Y}}   * Move the center of rotation in the direction **Y**, from the coordinates of the selected object. (default   * 0,0,0).

-    {{TasksTag|Z}}   * Move the center of rotation in the direction **Z**, from the coordinates of the selected object. (default   * 0,0,0).

-    {{TasksTag|User Defined...}}   * Allows you to change the three axes (**X, Y, Z**) in a single operation <img alt="User Defined" src=images/Part_Revolve_fr_06.png  style="width   *96px;">.


{{TitleProperty|Rotation}}

To adjust our **rotation parameters** we have two methods available.

-   First option. Select \'\'\' Rotation axis with angle \'\'\'<img alt="Tache\_Placement Option rotation axis and angle" src=images/Tache_Placement_fr_05.png  style="width   *256px;"> (Default).
    -   
        {{TasksTag|Axis   * X}}
        
           * The rotation will be on the **X** axis.

    -   
        {{TasksTag|Axis   * Y}}
        
           * The rotation will be on the **Y** axis.

    -   
        {{TasksTag|Axis   * Z}}
        
           * The rotation will be on the **Z** axis. (Default axis).

    -   
        {{TasksTag|Angle   *}}
        
        Angle of rotation in degrees from **-360.00 °** to **360.00 °**. (Default   * **0.00°**).

-   Second option. Select **Euler Angles** <img alt="Tache\_Placement Option Euler angles" src=images/Tache_Placement_fr_04.png  style="width   *256px;">.

This option may be easier to work with, however, even in this mode, there are important things to remember   * Positive rotations are in the **clockwise** direction, looking **out** from the origin along a positive axis. Or to put it differently, the rotations are positive in the **counterclockwise** direction, looking **in** to the origin along a positive axis.

   ** **[Yaw](https   *//en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft))**    * is a horizontal rotation of a body about a vertical axis. (The symbol **ψ** is often used for yaw.)

   ** **[Pitch](https   *//en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft))**    * is defined as an oscillating movement of a vessel fore and aft.

   ** **[Roll](https   *//en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft))**    * is a rotary movement of a body about its longitudinal axis (roll axis).

Yaw, pitch and roll refer to the **attitude** of an object in 3D space. These terms are commonly used in aviation. The angles are the **Tait-Bryan angles**. If you want more information, read [Euler angles](https   *//en.wikipedia.org/wiki/Euler_angles).

![None\|Option Euler angles](images/Tache_Placement_en_03.png )

![None\|Yaw](images/Tache_Placement_Lacet_fr_Mini.gif )

-    {{TasksTag|yaw axis}}**Yaw is the rotation about the Z axis**, that is to say a rotation from left to right. (The Yaw angle is the **Psi ψ**). Value **-360.00 °** to \'\'\'360, 00 ° \'\'\'(Default, **0.00 °**).

![None\|Pitch](images/Tache_Placement_Tangage_fr_Mini.gif )

-    {{TasksTag|pitch axis}}**Pitch is rotation about the Y axis**, that is to say nose-up and nose-down. (The Pitch angle is the **Phi φ**). Value **-360.00 °** to \'\'\'360, 00 ° \'\'\'(Default, **0.00 °**).

![None\|Roll](images/Tache_Placement_Roulis_fr_Mini.gif )

-    {{TasksTag|roll axis}}**Roll is rotation about the X axis**, that is to say wing up and down. (The Roll angle is the **Thêta θ**). Value **-360.00 °** to \'\'\'360, 00 ° \'\'\'(Default, **0.00 °**).

-    {{TasksTag|Apply incremental changes}}to the placement of the object   * Once selected, this option **virtually** sets all parameters to zero, to allow you to enter your values ​​without having to calculate with the original parameters of the form. Once you have confirmed with **OK**, the entered values ​​will be added to the values ​​on the form.

-   The **Reset** returns all values ​​to **0,0,0**.

## Links and Example 

A practical example of using this command is in the tutorial [Aeroplane](Aeroplane.md).

Other explanation on [Placement](Placement.md).




[Category   *Command\_Reference](Category_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Command_Reference](Category_Command_Reference.md) > Tasks Placement/cs
