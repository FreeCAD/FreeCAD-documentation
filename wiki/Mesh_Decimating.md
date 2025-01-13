---
 GuiCommand:
   Name: Mesh Decimating
   MenuLocation: Meshes , Decimation...
   Workbenches: Mesh_Workbench
   Version: 0.19
---

# Mesh Decimating

## Description

The **Mesh Decimating** command reduces the number of faces in mesh objects.

## Usage

1.  Select one or more mesh objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Decimating.svg" width=16px> [Decimation...](Mesh_Decimating.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_Decimating.svg" width=16px> Decimation...** option from the menu.
3.  The **Decimating** task panel opens.
4.  Specify the **Reduction**:
    -   If only one mesh object has been selected and you choose the **Absolute number** option:
        -   Move the slider or enter a number to specify an absolute number of faces.
    -   In other cases:
        -   Move the slider or enter a number to specify a percentage of faces.
        -   Specify the **Tolerance**. The tolerance parameter in the mesh simplification process acts like a quality control setting. Imagine you\'re trying to simplify a detailed sculpture into a rougher shape without losing too much of its important features. By setting a higher tolerance, you allow for bigger changes and more simplification, resulting in a rougher shape. A lower tolerance means the simplification process will be more careful and only make small adjustments, keeping the shape closer to the original. If the tolerance is set to zero, the process will simplify the shape as much as possible within its rules, aiming for a balance between reducing complexity and keeping the original form recognizable.
5.  Press the **OK** button to finish the command.




 {{Mesh Tools navi}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Decimating
