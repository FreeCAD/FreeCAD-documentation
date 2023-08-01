---
- GuiCommand:
   Name:Mesh SplitComponents
   MenuLocation:Meshes → Split by components
   Workbenches:[Mesh](Mesh_Workbench.md)
   Version:0.19
   SeeAlso:[Mesh Merge](Mesh_Merge.md)
---

# Mesh SplitComponents/de



## Beschreibung

The **Mesh SplitComponents** command splits a mesh object into its components. A mesh component is a complete group of connected faces. For each component a new non-parametric mesh object, a [Mesh Feature](Mesh_Feature.md), is created. If the original mesh object contains only one component, and this is usually the case, a single new mesh object, effectively a copy, is created. This command is the counterpart of the [Mesh Merge](Mesh_Merge.md) command.



## Anwendung

1.  Select a single mesh object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_SplitComponents.svg" width=16px> [Mesh SplitComponents](Mesh_SplitComponents.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_SplitComponents.svg" width=16px> Split by components** option from the menu.



## Eigenschaften

Siehe: [Mesh Formelement](Mesh_Feature/de.md).





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SplitComponents/de
