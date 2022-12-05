# FEM Mesh CalculiX/fr
{{TOCright}}

## Types d\'éléments MEF dans CalculiX 

Pour plus d\'informations détaillées de FreeCAD FEM éléments voir [FEM Maillage](FEM_Mesh/fr.md) et [FEM Types d\'éléments](FEM_Element_Types/fr.md). Pour les questions spécifiques à CalculiX, vous pouvez essayer [Discourse group](https://calculix.discourse.group) ou [Discord channel](https://discord.gg/yyuQQg5).

### Élément Segment 

   
  Nœuds FreeCAD seg2                      Nœuds FreeCAD seg3
  <img alt="" src=images/Seg2.png  style="width:250px;">   <img alt="" src=images/Seg3--fc.png  style="width:250px;">
  Nœuds CalculiX seg2 (B31)               Nœuds CalculiX seg3 (B32)
  <img alt="" src=images/Seg2.png  style="width:250px;">   <img alt="" src=images/Seg3--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nœuds               
  N1, N2                                  N1, N3, N2
   

  : **Élément de segment de FreeCAD à CalculiX \-- affectation des nœuds**

### Élément Triangle 

   
  Nœuds FreeCAD tria3                                 Nœuds FreeCAD tria6
  <img alt="" src=images/Tria3--fc.png  style="width:250px;">     <img alt="" src=images/Tria6--fc.png  style="width:250px;">
  Nœuds CalculiX tria3 (S3)                           Nœuds CalculiX tria6 (S6)
  <img alt="" src=images/Tria3--ccx.png  style="width:250px;">   <img alt="" src=images/Tria6--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nœuds                           
  N1, N2, N3                                          N1, N2, N3, N4, N5, N6
   

  : **Élément de triangle de FreeCAD à CalculiX \-- affectation des nœuds**

### Élément Quadrilatère 

   
  Nœuds FreeCAD quad4                                 Nœuds FreeCAD quad8
  <img alt="" src=images/Quad4--fc.png  style="width:250px;">     <img alt="" src=images/Quad8--fc.png  style="width:250px;">
  Nœuds CalculiX quad4 (S4)                           Nœuds CalculiX quad8 (S8)
  <img alt="" src=images/Quad4--ccx.png  style="width:250px;">   <img alt="" src=images/Quad8--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nœuds                           
  N1, N2, N3, N4                                      N1, N2, N3, N4, N5, N6, N7, N8
   

  : **Élément de quadrilatère de FreeCAD à CalculiX \-- affectation des nœuds**

### Élément Tétraèdre 

L\'ordre de nœud suivant n\'est pas implémenté ! TODO: vérifier l\'ordre des noeuds (n\'oubliez pas getccxVolumesByFace()).

   
  Nœuds FreeCAD tetra4                                  Nœuds FreeCAD tetra10
  <img alt="" src=images/Tetra4--fc.png  style="width:250px;">     <img alt="" src=images/Tetra10--fc.png  style="width:250px;">
  Nœuds CalculiX tetra4 (C3D4)                          Nœuds CalculiX tetra10 (C3D10)
  <img alt="" src=images/Tetra4--ccx.png  style="width:250px;">   <img alt="" src=images/Tetra10--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nœuds                             
  N2, N3, N4, N1                                        N2, N3, N4, N1, N6, N10, N9, N5, N7, N8
   

  : **Élément de tétraèdre de FreeCAD à CalculiX \-- affectation des nœuds**

### Élément Hexaèdre 

   
  Nœuds FreeCAD hexa8                                 Nœuds FreeCAD hexa20
  <img alt="" src=images/Hexa8--fc.png  style="width:250px;">     <img alt="" src=images/Hexa20--fc.png  style="width:250px;">
  Nœuds CalculiX hexa8 (C3D8)                         Nœuds CalculiX hexa20 (C3D20)
  <img alt="" src=images/Hexa8--ccx.png  style="width:250px;">   <img alt="" src=images/Hexa20--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nœuds                           
  N6, N7, N8, N5, N2, N3, N4, N1                      N6, N7, N8, N5, N2, N3, N4, N1, N14, N15, N16, N13, N10, N11, N12, N9, N18, N19, N20, N17
   

  : **Élément de hexaèdre de FreeCAD à CalculiX \-- affectation des nœuds**

### Élément Pentaèdre 

   
  Nœuds FreeCAD penta6                                  Nœuds FreeCAD penta15
  <img alt="" src=images/penta6--fc.png  style="width:250px;">     <img alt="" src=images/Penta15--fc.png  style="width:250px;">
  Nœuds CalculiX penta6 (C3D6)                          Nœuds CalculiX penta15 (C3D15)
  <img alt="" src=images/Penta6--ccx.png  style="width:250px;">   <img alt="" src=images/Penta15--ccx.png  style="width:250px;">
  FreeCAD → CalculiX, Nœuds                             
  N5, N6, N4, N2, N3, N1                                N5, N6, N4, N2, N3, N1, N11, N12, N10, N8, N9, N7, N14, N15, N13
   

  : **Élément de pentaèdre de FreeCAD à CalculiX \-- affectation des nœuds**

## En relation 

-   La page [FEM Calculix](FEM_CalculiX/fr.md)
-   [Préférences de CalculiX](FEM_Preferences/fr#CalculiX.md) dans le menu des préférences de l\'atelier FEM.


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [FEM](Category_FEM.md) > FEM Mesh CalculiX/fr
