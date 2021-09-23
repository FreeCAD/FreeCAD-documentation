---
- GuiCommand:
   Name:Mesh EvaluateFacet
   MenuLocation:Meshes → Analyze → Face info
   Workbenches:[Mesh](Mesh_Workbench.md)
---

# Mesh EvaluateFacet/en

## Description

The **Mesh EvaluateFacet** command shows information about faces of mesh objects.

Mesh: Ellipsoid Facet 3631: Points: <1817, 1818, 1866>, Neighbours: <3534, 3632, 3630>
Triangle: <[1.964574, 0.047063, 0.748046], [1.937166, 0.062461, 0.992797], [1.964574, -0.047063, 0.748046]>


*Example of the information displayed in the Report view*

## Usage

1.  It is advisable to enable the [Report view](Report_view.md). The command will display detailed information there.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_EvaluateFacet.svg" width=16px> [Mesh EvaluateFacet](Mesh_EvaluateFacet.md)** button.
    -   Select the **Meshes → Analyze → <img src="images/Mesh_EvaluateFacet.svg" width=16px> Face info** option from the menu.
3.  The cursor changes to a pipette icon.
4.  Select a face of a mesh object.
5.  Its index will be displayed in the [3D view](3D_view.md).
6.  Additional information is shown in the Report view:
    -   The internal name of the mesh object.
    -   The index of the selected face.
    -   The indices of the three face points.
    -   The indices of the faces that share an edge with the selected face.
    -   The coordinates of the face points.
7.  Optionally select more faces.
8.  Select the **Leave info mode** option from the 3D view context menu to finish the command.





{{Mesh Tools navi

}}

---
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh EvaluateFacet/en
