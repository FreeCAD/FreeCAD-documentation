---
 GuiCommand:
   Name: CAM SimulatorGL
   MenuLocation: CAM , New CAM Simulator
   Workbenches: CAM_Workbench
   Shortcut: **P** **N**
   Version: 1.0
   SeeAlso: CAM_Simulator
---

# CAM SimulatorGL/de


</div>



## Beschreibung


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/CAM_SimulatorGL.svg  style="width:24px;"> [SimulatorGL](CAM_SimulatorGL.md) tool is a new alternative to [CAM Simulator](CAM_Simulator.md). It\'s based on low-level OpenGL functions. To eliminate interference with the 3D view of FreeCAD, it works in a separate window with a separate OpenGL context. It\'s meant to be faster and more precise than the old simulator.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/CAM_new_simulator.PNG  style="width:600px;">


</div>



## Anwendung


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/CAM_SimulatorGL.svg" width=16px> [CAM SimulatorGL](CAM_SimulatorGL.md)** button.
    -   Select the **CAM → <img src="images/CAM_Simulator.svg" width=16px> New CAM Simulator** option from the menu.
    -   Use the keyboard shortcut: **P** then **N**.
2.  De-select any **Operations** that are not to be simulated
3.  Tune the **Accuracy** setting.
4.  Select the **Job** for simulation from the drop menu.
5.  Press the <img alt="" src=images/CAM_BPlay.svg  style="width:24px;"> (Activate / resume simulation) button
    -   A separate window with the simulator will open.
    -   Use the left-side buttons: Play, Single-Step and Fast Forward and the slider to control the animation.
    -   Use the right-side buttons to: Show/hide overlay of base model, Orbit the model, Display the path and Enable/disable Ambient Occlusion.
    -   Control the 3D view with the current FreeCAD mouse controls.


</div>



## Eigenschaften


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Accuracy**: The accuracy of the simulation expressed as a percentage indicating the simulations deviation from the Job. For interactive simulation, reducing accuracy to 0.3 works much faster.

-    **Job**: The Job used as the basis of the simulation

-    **Operation List**: The list of Operations selected for inclusion in the simulation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM SimulatorGL/de
