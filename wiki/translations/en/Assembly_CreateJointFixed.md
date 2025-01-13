---
 GuiCommand:
   Name: Assembly CreateJointFixed
   MenuLocation: Assembly , Create a Fixed Joint
   Workbenches: Assembly_Workbench
   Shortcut: **F**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointFixed/en

## Description

The <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:24px;"> [Assembly CreateJointFixed](Assembly_CreateJointFixed.md) tool creates a joint locking two assembly parts together, preventing any movement or rotation.

## Usage

1.  Optionally select two geometric entities of two different parts. Other selections will be rejected.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointFixed.svg" width=16px> [Create a Fixed Joint](Assembly_CreateJointFixed.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateJointFixed.svg" width=16px> Create a Fixed Joint** option from the menu.
    -   Use the keyboard shortcut: **F**.
3.  Pre-selected parts are moved to meet at their selected entities.
4.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
5.  Optionally change the joint type in the dropdown list:
    -   Select **Fixed**.
        1.  If the selection list is empty: select two geometric entities.
        2.  The parts are moved to meet at their selected entities.
        3.  Optionally enter an *Offset* value.
        4.  Optionally enter a *Rotation* value.
        5.  Optionally press **<img src="images/Button_sort.svg" width=16px>** to change the direction of the joint.
    -   Select **Revolute**.
        1.  If the selection list is empty: select two geometric entities.
        2.  The parts are moved to meet at their selected entities.
        3.  Optionally enter an *Offset* value.
        4.  Optionally press **<img src="images/Button_sort.svg" width=16px>** to change the direction of the joint.
        5.  Optionally check the **Min angle** option and enter a value.
        6.  Optionally check the **Max angle** option and enter a value.
    -   Select **Cylindrical**.
        1.  If the selection list is empty: select two geometric entities.
        2.  Optionally press **<img src="images/Button_sort.svg" width=16px>** to change the direction of the joint.
        3.  Optionally check the **Min length** option and enter a value.
        4.  Optionally check the **Max length** option and enter a value.
        5.  Optionally check the **Min angle** option and enter a value.
        6.  Optionally check the **Max angle** option and enter a value.
    -   Select **Slider**.
        1.  If the selection list is empty: select two geometric entities.
        2.  Optionally enter a *Rotation* value.
        3.  Optionally press **<img src="images/Button_sort.svg" width=16px>** to change the direction of the joint.
        4.  Optionally check the **Min length** option and enter a value.
        5.  Optionally check the **Max length** option and enter a value.
    -   Select **Ball**.
        1.  If the selection list is empty: select two geometric entities.
    -   Select **Distance**.
        1.  If the selection list is empty: select two geometric entities.
        2.  Optionally enter a *Distance* value.
        3.  Optionally press **<img src="images/Button_sort.svg" width=16px>** to change the direction of the joint.
    -   Select **Parallel**.
        1.  If the selection list is empty: select two geometric entities.
        2.  Optionally press **<img src="images/Button_sort.svg" width=16px>** to change the direction of the joint.
    -   Select **Perpendicular**.
        1.  If the selection list is empty: select two geometric entities.
    -   Select **Angle**.
        1.  If the selection list is empty: select two geometric entities.
        2.  Optionally enter an *Angle* value.
    -   Select **RackPinion**.
        1.  If the selection list is empty: select two geometric entities of two different parts that have previously been used to define a Slider joint and a Revolute joint. (Slider direction and rotation axis must be perpendicular)
        2.  Optionally enter a *Pitch radius* value.
    -   Select **Screw**.
        1.  If the selection list is empty: select two geometric entities of two different parts that have previously been used to define a Slider joint and a Revolute joint. (Slider direction and rotation axis must be parallel)
        2.  Optionally enter a *Pitch radius* value.
    -   Select **Gears**.
        1.  If the selection list is empty: select two geometric entities of two different parts that have previously been used to define two different Revolute joints.
        2.  Optionally enter a *Radius 1* value.
        3.  Optionally enter a *Radius 2* value.
        4.  Optionally check/uncheck the **Reverse rotation** option. (unchecking selects the **Belt** option) - not working for 1.0 RC so far
    -   Select **Belt**.
        1.  If the selection list is empty: select two geometric entities of two different parts that have previously been used to define two different Revolute joints.
        2.  Optionally enter a *Radius 1* value.
        3.  Optionally enter a *Radius 2* value.
        4.  Optionally check/uncheck the **Reverse rotation** option. (checking selects the **Gears** option) - not working for 1.0 RC so far
6.  The Parts are moved to meet at their selected entities.
7.  Press **OK** to finish the tool.

## Notes

-   A fixed joint can be used as an actuator to control the motion of a kinematic simulation. Mouse wheel action in the Task panel immediately rearranges the connected parts.
    -   Offset translates along its local Z axis, negative offsets are accepted.
    -   Rotation revolves around its local Z axis, angles \> 360° and even negative angles are accepted.

## Properties

See also: [Property editor](Property_editor.md).

A **Fixed** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Joint}}

-    **Activated|Bool**: This indicates if the joint is active.

-    **Distance|Float**: This stores the **Distance** of the Distance joint. It is also used by the RackPinion and Screw joints to store the **Pitch radius**, and by the Gear, and Belt joints to store **Radius1**.

-    **Distance2|Float**: This is the second distance of the joint. It is used only by the Gear and Belt joints to store **Radius2**.

-    **Joint Type|Ennumeration**: The type of the joint. ({{Value|Fixed}}, {{Value|Revolute}}, {{Value|Cylindrical}}, {{Value|Slider}}, {{Value|Ball}}, {{Value|Distance}}, {{Value|Parallel}}, {{Value|Perpendicular}}, {{Value|Angle}}, {{Value|RackPinion}}, {{Value|Screw}}, {{Value|Gears}}, {{Value|Belt}})

Removed properties (v.1.0.0-RC-38728) These were the properties that could be used to animate:

-    **Offset|Vector**: This is the offset vector of the joint.

-    **Rotation|Float**: This is the rotation of the joint.


{{TitleProperty|Joint Connector 1}}

-    **Detach1|Bool**: This prevents placement1 from recomputing, enabling custom positioning of the placement.

-    **Offset1|Placement**: This is the attachment offset of the first connector of the joint. (added with v.1.0.0-RC-38728)

-    **Placement1|Placement**: This is the local coordinate system within reference1\'s object that will be used for the joint.

-    **Reference1|XlinkSubHidden**: The first reference of the joint.

Removed properties:

-    **Element1|String**: The selected element of the first object.

-    **Object1|String**: The first object of the joint.

-    **Part1|Link**: The first Part of the joint.

-    **Vertex1|String**: The selected Vertex of the first object.


{{TitleProperty|Joint Connector 2}}

-    **Detach2|Bool**: This prevents placement2 from recomputing, enabling custom positioning of the placement.

-    **Offset2|Placement**: This is the attachment offset of the second connector of the joint. (added with v.1.0.0-RC-38728)

-    **Placement2|Placement**: This is the local coordinate system within reference2\'s object that will be used for the joint.

-    **Reference2|XlinkSubHidden**: The second reference of the joint.

Removed properties:

-    **Element2|String**: The selected element of the second object.

-    **Object2|String**: The second object of the joint.

-    **Part2|Link**: The second Part of the joint.

-    **Vertex2|String**: The selected Vertex of the second object.


{{TitleProperty|Limits}}

-    **Angle Max|Float**: This is the maximum limit for the angle between both coordinate systems (between their X axes).

-    **Angle Min|Float**: This is the minimum limit for the angle between both coordinate systems (between their X axes).

-    **Enable Angle Max|Bool**: Enable the maximum angle limit of the joint.

-    **Enable Angle Min|Bool**: Enable the minimum angle limit of the joint.

-    **Enable Length Max|Bool**: Enable the maximum length limit of the joint.

-    **Enable Length Min|Bool**: Enable the minimum length limit of the joint.

-    **Length Max|Float**: This is the maximum limit for the distance between both coordinate systems (along their Z axis).

-    **Length Min|Float**: This is the minimum limit for the distance between both coordinate systems (along their Z axis).

Removed property:

-    **Enable Limits|Bool**: Is this joint using limits?





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointFixed/en
