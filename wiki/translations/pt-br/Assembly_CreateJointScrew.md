---
 GuiCommand:
   Name: Assembly CreateJointScrew
   MenuLocation: Assembly , Create Screw Joint
   Workbenches: Assembly_Workbench
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointScrew/pt-br


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:24px;"> [Assembly CreateJointScrew](Assembly_CreateJointScrew.md) tool creates a screw joint (helical joint) that couples the translation of a part of a slider joint and the rotation of a part of a revolute joint. In connection with the already existing joints this joint can be used to simulate a lead screw gear.


</div>



## Utilização


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Optionally select two geometric entities of two different shapes that have previously been used to define a Slider joint and a Revolute joint.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointScrew.svg" width=16px> [Create Screw Joint](Assembly_CreateJointScrew.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateJointScrew.svg" width=16px> Create Screw Joint** option from the menu.
    -   Use the keyboard shortcut: **W**.
3.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
4.  For further steps see [Assembly CreateJointFixed](Assembly_CreateJointFixed#Usage.md).


</div>



## Notas


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Pitch radius refers to the pitch of a (lead) screw. It is stored in **Distance** and defines the translation per one turn of the screw.


</div>



## Propriedades


<div lang="en" dir="ltr" class="mw-content-ltr">

See also: [Property editor](Property_editor.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

A **Screw** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. See [Assembly CreateJointFixed](Assembly_CreateJointFixed#Properties.md) for additional properties.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointScrew/pt-br
