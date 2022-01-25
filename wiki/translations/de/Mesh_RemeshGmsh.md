---
- GuiCommand:/de
   Name:Mesh RemeshGmsh
   Name/de:Netz WiedervernetzenGmsh
   MenuLocation:Netze → Verfeinerung...
   Workbenches:[Netz](Mesh_Workbench/de.md)
   Version:0.19
   SeeAlso:[Netz AusTeilForm](Mesh_FromPartShape/de.md)
---

# Mesh RemeshGmsh/de

## Beschreibung

Der **Netz WiedervernetzenGmsh** Befehl wiedervernetzt ein Netzobjekt unter Verwendung des [Gmsh](https://gmsh.info/) Vernetzers. Das neue Netz kann feiner oder gröber sein.

## Anwendung

1.  Select a single mesh object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_RemeshGmsh.svg" width=16px> [Mesh RemeshGmsh](Mesh_RemeshGmsh.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_RemeshGmsh.svg" width=16px> Refinement...** option from the menu.
3.  The **Remesh by gmsh** task panel opens.
4.  Specify the required settings. See the [Gmsh mesher settings](Mesh_FromPartShape#Gmsh_mesher.md) of the [Mesh FromPartShape](Mesh_FromPartShape.md) command.
5.  Press the **Apply** button to remesh the mesh object.
6.  Optionally change one or more settings and again press the **Apply** button until the new mesh is to your liking.
7.  Press the **Close** button to close the task panel and finish the command.

## Hinweise

-   In some cases this command will produce a mesh with flipped normals. The [Mesh FlipNormals](Mesh_FlipNormals.md) command can be used to correct this.

## Eigenschaften

See: [Mesh Feature](Mesh_Feature.md).


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemeshGmsh/de
