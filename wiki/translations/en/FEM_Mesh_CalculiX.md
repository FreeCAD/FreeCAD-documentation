# FEM Mesh CalculiX/en
{{TOCright}}

## FEM element types in CalculiX 

For detailed information on FreeCAD FEM elements see [FEM Mesh](FEM_Mesh.md) and [FEM Element Types](FEM_Element_Types.md). For CalculiX specific questions you may try the [Discourse group](https://calculix.discourse.group) or the [Discord channel](https://discord.gg/yyuQQg5).

### Segment element 

  --------------------------------------- -------------------------------------------------
  seg2 FreeCAD nodes                      seg3 FreeCAD nodes
  <img alt="" src=images/Seg2.png  style="width:250px;">   <img alt="" src=images/Seg3--fc.png  style="width:250px;">
  seg2 (B31) CalculiX nodes               seg3 (B32) CalculiX nodes
  <img alt="" src=images/Seg2.png  style="width:250px;">   <img alt="" src=images/Seg3--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nodes               
  N1, N2                                  N1, N3, N2
  --------------------------------------- -------------------------------------------------

  : **Segment element from FreeCAD to CalculiX \-- node assignment**

### Triangle element 

  --------------------------------------------------- ---------------------------------------------------
  tria3 FreeCAD nodes                                 tria6 FreeCAD nodes
  <img alt="" src=images/Tria3--fc.png  style="width:250px;">     <img alt="" src=images/Tria6--fc.png  style="width:250px;">
  tria3 (S3) CalculiX nodes                           tria6 (S6) CalculiX nodes
  <img alt="" src=images/Tria3--ccx.png  style="width:250px;">   <img alt="" src=images/Tria6--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nodes                           
  N1, N2, N3                                          N1, N2, N3, N4, N5, N6
  --------------------------------------------------- ---------------------------------------------------

  : **Triangle element from FreeCAD to CalculiX \-- node assignment**

### Quadratic element 

  --------------------------------------------------- ---------------------------------------------------
  quad4 FreeCAD nodes                                 quad8 FreeCAD nodes
  <img alt="" src=images/Quad4--fc.png  style="width:250px;">     <img alt="" src=images/Quad8--fc.png  style="width:250px;">
  quad4 (S4) CalculiX nodes                           quad8 (S8) CalculiX nodes
  <img alt="" src=images/Quad4--ccx.png  style="width:250px;">   <img alt="" src=images/Quad8--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nodes                           
  N1, N2, N3, N4                                      N1, N2, N3, N4, N5, N6, N7, N8
  --------------------------------------------------- ---------------------------------------------------

  : **Quadratic element from FreeCAD to CalculiX \-- node assignment**

### Tetrahedron element 

The following node order is not implemented ! TODO: verify node order (do not forget getccxVolumesByFace()).

  ----------------------------------------------------- -------------------------------------------------------
  tetra4 FreeCAD nodes                                  tetra10 FreeCAD nodes
  <img alt="" src=images/Tetra4--fc.png  style="width:250px;">     <img alt="" src=images/Tetra10--fc.png  style="width:250px;">
  tetra4 (C3D4) CalculiX nodes                          tetra10 (C3D10) CalculiX nodes
  <img alt="" src=images/Tetra4--ccx.png  style="width:250px;">   <img alt="" src=images/Tetra10--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nodes                             
  N2, N3, N4, N1                                        N2, N3, N4, N1, N6, N10, N9, N5, N7, N8
  ----------------------------------------------------- -------------------------------------------------------

  : **Tetrahedron element from FreeCAD to CalculiX \-- node assignment**

### Hexahedron element 

  --------------------------------------------------- --------------------------------------------------------------------------------------------
  hexa8 FreeCAD nodes                                 hexa20 FreeCAD nodes
  <img alt="" src=images/Hexa8--fc.png  style="width:250px;">     <img alt="" src=images/Hexa20--fc.png  style="width:250px;">
  hexa8 (C3D8) CalculiX nodes                         hexa20 (C3D20) CalculiX nodes
  <img alt="" src=images/Hexa8--ccx.png  style="width:250px;">   <img alt="" src=images/Hexa20--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nodes                           
  N6, N7, N8, N5, N2, N3, N4, N1                      N6, N7, N8, N5, N2, N3, N4, N1 , N14, N15, N16, N13, N10, N11, N12, N9, N18, N19, N20, N17
  --------------------------------------------------- --------------------------------------------------------------------------------------------

  : **Hexahedron element from FreeCAD to CalculiX \-- node assignment**

### Pentahedron element 

  ----------------------------------------------------- ------------------------------------------------------------------
  penta6 FreeCAD nodes                                  penta15 FreeCAD nodes
  <img alt="" src=images/penta6--fc.png  style="width:250px;">     <img alt="" src=images/Penta15--fc.png  style="width:250px;">
  penta6 (C3D6) CalculiX nodes                          penta15 (C3D15) CalculiX nodes
  <img alt="" src=images/Penta6--ccx.png  style="width:250px;">   <img alt="" src=images/Penta15--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nodes                             
  N5, N6, N4, N2, N3, N1                                N5, N6, N4, N2, N3, N1, N11, N12, N10, N8, N9, N7, N14, N15, N13
  ----------------------------------------------------- ------------------------------------------------------------------

  : **Pentahedron element from FreeCAD to CalculiX \-- node assignment**

## Related

-   [FEM CalculiX](FEM_CalculiX.md) page
-   [CalculiX preferences](FEM_Preferences#CalculiX.md) dialog menu in the FEM Workbench preferences menu


{{FEM Tools navi

}}  

[Category:Developer](Category:Developer.md) [Category:Poweruser\_Documentation](Category:Poweruser_Documentation.md)

---
[documentation index](../README.md) > [Developer](Category:Developer.md) > FEM Mesh CalculiX/en
