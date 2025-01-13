---
 GuiCommand:
   Name: Assembly CreateSimulation
   MenuLocation: Assembly , Create Simulation
   Workbenches: Assembly_Workbench
   Shortcut: **S**
   Version: 1.1
   SeeAlso: 
---

# Assembly CreateSimulation

## Description

The <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:24px;"> [Assembly CreateSimulation](Assembly_CreateSimulation.md) tool creates a simulation of the current assembly.

## Usage

1.  Make sure that an assembly is active.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateSimulation.svg" width=16px> [Create Simulation](Assembly_CreateSimulation.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateSimulation.svg" width=16px> Create Simulation** option from the menu.
    -   Use the keyboard shortcut: **S**.
3.  If no Simulations object pre-exists: A Simulations container is added to the active assembly.
4.  A Simulation object is added to the Simulations container.
5.  The **Create Simulation** [Task panel](Task_panel.md) opens.
6.  Press the green plus button to open a dialog window.
    -   Select one joint from the list.
    -   If necessary select a Motion Type.
    -   Optionally edit the Formula.
    -   Press the **OK** button to close the dialog.
7.  Optionally adjust the Simulation settings.
8.  Press the **Generate** button.
9.  An **Animation Player** section is added to the Task panel.
    -   Use the player widgets to animate the assembly.
10. Press the **OK** button to finish the tool and close the Task panel.

## Notes

-   The unnamed dialog helps to define an actuator:
    1.  Select the desired joint from the **Joints** list.
    2.  If there is more than one transformation available with the selected joint, select one from the **Motion Type** list.
    3.  Edit the Formula that describes the relation between the time running and the driven angle/distance.
    4.  Optionally press the Help button to see examples of **Formula** descriptions.
-   In the Formula **time** seems to represent 1 rad per second, and with 360° = 6,283 rad for a full rotation we can do either:
    -   Enter {{Value|6.283 * time}} in the Formula field and set a duration (End value - Start value) of one second under Simulation settings in the Task panel.
    -   Enter {{Value|1 * time}} in the Formula field and set a duration (End value - Start value) of 6.283 seconds under Simulation settings in the Task panel.

## Properties

See also: [Property editor](Property_editor.md).

### Simulations

A **Simulations** container is an {{Incode|Assembly::SimulationGroup}} object which is derived from an [App DocumentObjectGroup](App_DocumentObjectGroup.md) object and inherits all its properties. It has no additional properties.

### Simulation

A **Simulation** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

#### Data


{{Properties_Title|Base}}

-    **Group|LinkList**: The Motion objects of the object.

-    **_ Group Touched|Bool|hidden**:


{{Properties_Title|Simulation}}

-    **a Time Start|Time**: Default is {{value|0.0 s}}. Simulation start time.

-    **b Time End|Time**: Default is {{value|4.0 s}}. Simulation end time.

-    **c Time Step Output|Time**: Default is {{value|0.01 s}}. Simulation time step for output.

-    **f Global Error Tolerance|Float**: Default is {{value|1e-06}}. Integration global error tolerance.

-    **j Frames Per Second|Integer**: Default is {{value|30}}. Frames Per Second.

### View


{{Properties_Title|Space}}

-    **Decimals|Integer**: Default is {{value|9}}. The number of decimals to use for calculated texts.

### Motion

A **Motion** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

#### Data 


{{Properties_Title|Motion}}

-    **Formula|String**: The formula of the motion. For example {{Value|1.0*time}}.

-    **Joint|XLinkSubHidden**: The joint that is moved by the motion.

-    **Motion Type|Enumeration**: The type of the motion. The options are: {{Value|Angular}} and {{Value|Linear}}.




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateSimulation
