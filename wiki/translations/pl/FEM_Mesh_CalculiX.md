# FEM Mesh CalculiX/pl
## Typy elementów MES w CalculiX 

Szczegółowy informacje na temat elementów skończonych we FreeCAD można znaleźć na stronach [MES: Siatka](FEM_Mesh/pl.md) i [MES: Rodzaje elementów](FEM_Element_Types/pl.md). Pytania związane ściśle z solverem CalculiX można zadawać na grupach [Discourse](https://calculix.discourse.group) i [Discord](https://discord.gg/yyuQQg5).



## Element 1D 

+++
| seg2 FreeCAD węzły                    | seg3 FreeCAD węzły                              |
+++
| <img alt="" src=images/Seg2.png  style="width:250px;"> | <img alt="" src=images/Seg3--fc.png  style="width:250px;">   |
+++
| seg2 (B31) CalculiX węzły             | seg3 (B32) CalculiX węzły                       |
+++
| <img alt="" src=images/Seg2.png  style="width:250px;"> | <img alt="" src=images/Seg3--ccx.png  style="width:250px;"> |
+++
| FreeCAD → CalculiX, węzły             |                                                 |
+++
| N1, N2                                | N1, N3, N2                                      |
+++

: **Element 1D z FreeCAD do CalculiX \-- przypisanie węzłów**



## Element trójkątny 

+++
| tria3 FreeCAD węzły                               | tria6 FreeCAD węzły                               |
+++
| <img alt="" src=images/Tria3--fc.png  style="width:250px;">   | <img alt="" src=images/Tria6--fc.png  style="width:250px;">   |
+++
| tria3 (S3) CalculiX węzły                         | tria6 (S6) CalculiX węzły                         |
+++
| <img alt="" src=images/Tria3--ccx.png  style="width:250px;"> | <img alt="" src=images/Tria6--ccx.png  style="width:250px;"> |
+++
| FreeCAD → CalculiX, węzły                         |                                                   |
+++
| N1, N2, N3                                        | N1, N2, N3, N4, N5, N6                            |
+++

: **Element trójkątny z FreeCAD do CalculiX \-- przypisanie węzłów**



### Element czworokątny 

+++
| quad4 FreeCAD węzły                               | quad8 FreeCAD węzły                               |
+++
| <img alt="" src=images/Quad4--fc.png  style="width:250px;">   | <img alt="" src=images/Quad8--fc.png  style="width:250px;">   |
+++
| quad4 (S4) CalculiX węzły                         | quad8 (S8) CalculiX węzły                         |
+++
| <img alt="" src=images/Quad4--ccx.png  style="width:250px;"> | <img alt="" src=images/Quad8--ccx.png  style="width:250px;"> |
+++
| FreeCAD → CalculiX, węzły                         |                                                   |
+++
| N1, N2, N3, N4                                    | N1, N2, N3, N4, N5, N6, N7, N8                    |
+++

: **Element czworokątny z FreeCAD do CalculiX \-- przypisanie węzłów**



## Element czworościenny 

Następująca kolejność węzłów nie jest zaimplementowanaǃ Do zrobieniaː zweryfikować kolejność węzłów *(nie zapomnieć getccxVolumesByFace())*.

+++
| tetra4 FreeCAD węzły                                | tetra10 FreeCAD węzły                                 |
+++
| <img alt="" src=images/Tetra4--fc.png  style="width:250px;">   | <img alt="" src=images/Tetra10--fc.png  style="width:250px;">   |
+++
| tetra4 (C3D4) CalculiX węzły                        | tetra10 (C3D10) CalculiX węzły                        |
+++
| <img alt="" src=images/Tetra4--ccx.png  style="width:250px;"> | <img alt="" src=images/Tetra10--ccx.png  style="width:250px;"> |
+++
| FreeCAD → CalculiX, węzły                           |                                                       |
+++
| N2, N3, N4, N1                                      | N2, N3, N4, N1, N6, N10, N9, N5, N7, N8               |
+++

: **Element czworościenny z FreeCAD do CalculiX \-- przypisanie węzłów**



## Element prostopadłościenny 

+++
| hexa8 FreeCAD węzły                               | hexa20 FreeCAD węzły                                                                      |
+++
| <img alt="" src=images/Hexa8--fc.png  style="width:250px;">   | <img alt="" src=images/Hexa20--fc.png  style="width:250px;">                                         |
+++
| hexa8 (C3D8) CalculiX węzły                       | hexa20 (C3D20) CalculiX węzły                                                             |
+++
| <img alt="" src=images/Hexa8--ccx.png  style="width:250px;"> | <img alt="" src=images/Hexa20--ccx.png  style="width:250px;">                                       |
+++
| FreeCAD → CalculiX, węzły                         |                                                                                           |
+++
| N6, N7, N8, N5, N2, N3, N4, N1                    | N6, N7, N8, N5, N2, N3, N4, N1, N14, N15, N16, N13, N10, N11, N12, N9, N18, N19, N20, N17 |
+++

: **Element prostopadłościenny z FreeCAD do CalculiX \-- przypisanie węzłów**



### Element pięciościenny 

+++
| penta6 FreeCAD węzły                                | penta15 FreeCAD węzły                                            |
+++
| <img alt="" src=images/penta6--fc.png  style="width:250px;">   | <img alt="" src=images/Penta15--fc.png  style="width:250px;">              |
+++
| penta6 (C3D6) CalculiX węzły                        | penta15 (C3D15) CalculiX węzły                                   |
+++
| <img alt="" src=images/Penta6--ccx.png  style="width:250px;"> | <img alt="" src=images/Penta15--ccx.png  style="width:250px;">            |
+++
| FreeCAD → CalculiX, węzły                           |                                                                  |
+++
| N5, N6, N4, N2, N3, N1                              | N5, N6, N4, N2, N3, N1, N11, N12, N10, N8, N9, N7, N14, N15, N13 |
+++

: **Element pięciościenny z FreeCAD do CalculiX \-- przypisanie węzłów**



## Powiązane

-   Strona [MESː CalculiX](FEM_CalculiX/pl.md)
-   Okno dialogowe [preferencji CalculiX](FEM_Preferences/pl#CalculiX.md) w menu preferencji środowiska pracy MES


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [FEM](Category_FEM.md) > FEM Mesh CalculiX/pl
