---
 GuiCommand:
   Name: Assembly CreateJointBelt
   MenuLocation: Assembly , Create Gear/Belt Joint , Create Belt Joint
   Workbenches: Assembly_Workbench
   Shortcut: 
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointBelt/pt-br


</div>



## Descrição


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:24px;"> [Assembly CreateJointBelt](Assembly_CreateJointBelt.md) tool creates a belt joint that couples the rotation of two parts of two different revolute joints. In connection with the already existing joints this joint can be used to simulate belt drives, timing gears, etc.


</div>



## Utilização


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Optionally select two geometric entities of two different parts that have previously been used to define two Revolute joints.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointBelt.svg" width=16px> [Create Belt Joint](Assembly_CreateJointBelt.md)** button.
    -   Select the **Assembly →  Create Gear/Belt Joint →  <img src="images/Assembly_CreateJointBelt.svg" width=16px> Create Belt Joint** option from the menu.
3.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
4.  For further steps see [Assembly CreateJointFixed](Assembly_CreateJointFixed#Usage.md).


</div>



## Notas


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Radius1 and Radius2 refer to the pitch circle of timing gears or the outer diameter of pulleys. They store their values in the **Distance** and **Distance2** properties and they define the ratio between both rotations.
-   Use the same value for both radii to connect both ends of a flexible shaft (if the rotations don\'t match, either reverse one [Revolute joint](Assembly_CreateJointRevolute.md) or use the [Gear joint](Assembly_CreateJointGears.md) instead of this one).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Properties


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

See also: [Property editor](Property_editor.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

A **Belt** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. See [Assembly CreateJointFixed](Assembly_CreateJointFixed#Properties.md) for additional properties.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointBelt/pt-br
