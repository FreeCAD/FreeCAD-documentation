---
- GuiCommand:/de
   Name:FEM MeshClear
   Name/de:FEM NetzLöschen
   MenuLocation:Kontextmenü des Mesh-Objekts oder der Baumansicht → FEM-Netz löschen
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM MeshClear/de

## Beschreibung

Enables the user to reiniitialize the mesh from the FreeCAD FEM mesh object. The mesh still exists but does not have any vertices, edges, faces or elements. The meshing information, Netgen/Gmsh parameters, mesh regions, mesh groups and mesh boundary layer remain in the Model Tree, which means the mesh can be reproduced later. The main use of this function is to lighten the FreeCAD file, either to improve performance when using FreeCAD, to save disk space or enable easy transfer of files without losing meshing data.

## Anwendung

1.  Eins der <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:16px;"> [Netgen-](FEM_MeshNetgenFromShape.md) oder <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:16px;"> [Gmsh-FEM](FEM_MeshGmshFromShape.md)-Mesh-Objekte mit der rechten Maustaste in der [Baumansicht](Tree_view/de.md) anklicken.
2.  Den Menüeintrag **<img src="images/FEM_MeshClear.svg" width=16px> FEM-Netz löschen** des Kontextmenüs auswählen.

## Hinweise

Die Objekte in der Baumansicht bleiben erhalten, da sie die Vernetzungsdaten repräsentieren, aber das eigentliche Netz wird aus der FreeCAD-Datei entfernt.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshClear/de
