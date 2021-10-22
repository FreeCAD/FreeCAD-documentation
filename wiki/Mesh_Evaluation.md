---
- GuiCommand:
   Name:Mesh Evaluation
   MenuLocation:Meshes → Analyze → Evaluate and repair mesh...
   Workbenches:[Mesh](Mesh_Workbench.md)
---

# Mesh Evaluation

## Description

The **Mesh Evaluation** command evaluates and repairs a mesh object.

 ![](images/Mesh_Evaluation_dialog.png )  
*The Evaluate & Repair Mesh dialog box with the Folds on surface option enabled*

## Usage

1.  Optionally select a single mesh object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Evaluation.svg" width=16px> [Mesh Evaluation](Mesh_Evaluation.md)** button.
    -   Select the **Meshes → Analyze → <img src="images/Mesh_Evaluation.svg" width=16px> Evaluate and repair mesh...** option from the menu.
3.  The **Evaluate & Repair Mesh** dialog box opens.
4.  Optionally press the **Settings...** button to change the following settings:
    -   
        **Check for non-manifold points**
        

    -   
        **Enable check for folds on surface**
        

    -   
        **Only consider zero area faces as degenerated**
        
5.  If you have not yet selected a mesh object: select one from the dropdown list at the top of the dialog box.
6.  The dialog contains 7 or 8 (if the **Folds on surface** option is enabled) test options.
7.  Do not use the checkboxes, they will be checked automatically if errors are found.
8.  Press any of the **Analyze** buttons to start a test.
9.  Or use the **Analyze** button from the **All above tests together** option to run all 7 or 8 tests together.
10. Errors will be indicated in the dialog box, and also, with yellow and red markers, in the [3D view](3D_view.md).
11. Optionally press one or more **Repair** buttons to repair the errors that were found.
12. Optionally press the **Reset** button to reset all test results. This will reset the dialog and remove the colored markers from the 3D view. If you want to repeat the same test or run all tests together there is no need to do this.
13. Optionally select a different mesh object from the dropdown list to continue testing and repairing.
14. Press the **Close** button to close the dialog box and finish the command.
15. The **Refresh** button does not work properly at this time.

## Notes

-   Repairing a mesh can mean that problematic elements are deleted from the mesh resulting in holes. Holes can be closed with the [Mesh FillupHoles](Mesh_FillupHoles.md), [Mesh FillInteractiveHole](Mesh_FillInteractiveHole.md) and [Mesh AddFacet](Mesh_AddFacet.md) commands.
-   See [this forum post](https://forum.freecadweb.org/viewtopic.php?f=3&p=533252#p533252) for an explanation of the mesh data structure. This information may help to understand why a mesh has problems.

## Preferences

-   The **Check for non-manifold points** setting is stored: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Evaluation → CheckNonManifoldPoints**.
-   The **Enable check for folds on surface** setting is stored: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Evaluation → EnableFoldsCheck**.
-   The **Only consider zero area faces as degenerated** setting is stored: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Evaluation → StrictlyDegenerated**.




 {{Mesh Tools navi}}

---
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Evaluation
