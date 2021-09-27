# FEM Element Types/it
{{TOCright}}

## Introduzione

Questa descrizione è basata sul formato MED come descritto in \[<https://hammi.extra.cea.fr/static/MED/web_med/logiciels/med-2.3.1/doc/html/modele_de_donnees.html#3>. modele de donnes\].

## Elemento Segmento 

<img alt="" src=images/FEM_mesh_elements_1_segment.svg  style="width:600px;">

  Edge   Node 1   Node 2   Middle node
  ------ -------- -------- -------------
  E1     N1       N2       N3

  : Edges of Seg2 and Seg3

## Elemento Triangolo 

<img alt="" src=images/FEM_mesh_elements_2_triangle.svg  style="width:600px;">

  Edge   Node 1   Node 2   Middle node
  ------ -------- -------- -------------
  E1     N1       N2       N4
  E2     N2       N3       N5
  E3     N3       N1       N6

  : Edges of Tria3 and Tria6

  Face   Edge 1   Edge 2   Edge 3
  ------ -------- -------- --------
  F1     E1       E2       E3

  : Face by Edges of Tria3 and Tria6

  Face   Node 1   Node 2   Node 3   Node 1
  ------ -------- -------- -------- --------
  F1     N1       N2       N3       N1

  : Face by Nodes of Tria3

  Face   Node 1   Node 2   Node 3   Node 4   Node 5   Node 6   Node 1
  ------ -------- -------- -------- -------- -------- -------- --------
  F1     N1       N4       N2       N5       N3       N6       N1

  : Face by Nodes of Tria6

## Elemento Quadrangolo 

<img alt="" src=images/FEM_mesh_elements_3_quadrangle.svg  style="width:600px;">

  Edge   Node 1   Node 2   Middle node
  ------ -------- -------- -------------
  E1     N1       N2       N5
  E2     N2       N3       N6
  E3     N3       N4       N7
  E4     N4       N1       N8

  : Edges of Quad4 and Quad8

  Face   Edge 1   Edge 2   Edge 3   Edge 4
  ------ -------- -------- -------- --------
  F1     E1       E2       E3       E4

  : Face by Edges of Quad4 and Quad8

  Face   Node 1   Node 2   Node 3   Node 4   Node 1
  ------ -------- -------- -------- -------- --------
  F1     N1       N2       N3       N4       N1

  : Face by Nodes of Quad4

  Face   Node 1   Node 2   Node 3   Node 4   Node 5   Node 6   Node 7   Node 8   Node 1
  ------ -------- -------- -------- -------- -------- -------- -------- -------- --------
  F1     N1       N5       N2       N6       N3       N7       N4       N8       N1

  : Face by Nodes of Quad8

## Elemento Tetraedro 

<img alt="" src=images/FEM_mesh_elements_4_tetrahedron.svg  style="width:600px;">

  Edge   Node 1   Node 2   Middle node
  ------ -------- -------- -------------
  E1     N1       N2       N5
  E2     N2       N3       N6
  E3     N3       N1       N7
  E4     N1       N4       N8
  E5     N2       N4       N9
  E6     N3       N4       N10

  : Edges of Tetra4 and Tetra10

  Face   Edge 1   Edge 2   Edge 3
  ------ -------- -------- --------
  F1     E1       E2       E3
  F2     E4       -E5      -E1
  F3     E5       -E6      -E2
  F4     E6       -E4      -E3

  : Faces by Edges of Tetra4 and Tetra10

  Face   Node 1   Node 2   Node 3   Node 1
  ------ -------- -------- -------- --------
  F1     N1       N2       N3       N1
  F2     N1       N4       N2       N1
  F3     N2       N4       N3       N2
  F4     N3       N4       N1       N3

  : Faces by Nodes of Tetra4

  Face   Node 1   Node 2   Node 3   Node 4   Node 5   Node 6   Node 1
  ------ -------- -------- -------- -------- -------- -------- --------
  F1     N1       N5       N2       N6       N3       N7       N1
  F2     N1       N8       N4       N9       N2       N5       N1
  F3     N2       N9       N4       N10      N3       N6       N2
  F4     N3       N10      N4       N8       N1       N7       N3

  : Faces by Nodes of Tetra10

## Elemento Esaedro 

<img alt="" src=images/FEM_mesh_elements_5_hexahedron.svg  style="width:600px;">

  Edge   Node 1   Node 2   Middle node
  ------ -------- -------- -------------
  E1     N1       N2       N9
  E2     N2       N3       N10
  E3     N3       N4       N11
  E4     N4       N1       N12
  E5     N5       N6       N13
  E6     N6       N7       N14
  E7     N7       N8       N15
  E8     N8       N5       N16
  E9     N1       N5       N17
  E10    N2       N6       N18
  E11    N3       N7       N19
  E12    N4       N8       N20

  : Edges of Hexa8 and Hexa20

  Face   Edge 1   Edge 2   Edge 3   Edge 4
  ------ -------- -------- -------- --------
  F1     E1       E2       E3       E4
  F2     -E8      -E7      -E6      -E5
  F3     E9       E5       -E10     -E1
  F4     E10      E6       -E11     -E2
  F5     E11      E7       -E12     -E3
  F6     E12      E8       -E9      -E4

  : Faces by Edges of Hexa8 and Hexa20

  Face   Node 1   Node 2   Node 3   Node 4   Node 1
  ------ -------- -------- -------- -------- --------
  F1     N1       N2       N3       N4       N1
  F2     N5       N8       N7       N6       N5
  F3     N1       N5       N6       N2       N1
  F4     N2       N6       N7       N3       N2
  F5     N3       N7       N8       N4       N3
  F6     N4       N8       N5       N1       N4

  : Faces by Nodes of Hexa8

  Face   Node 1   Node 2   Node 3   Node 4   Node 5   Node 6   Node 7   Node 8   Node1
  ------ -------- -------- -------- -------- -------- -------- -------- -------- -------
  F1     N1       N9       N2       N10      N3       N11      N4       N12      N1
  F2     N5       N16      N8       N15      N7       N14      N6       N13      N5
  F3     N1       N17      N5       N13      N6       N18      N2       N9       N1
  F4     N2       N18      N6       N14      N7       N19      N3       N10      N2
  F5     N3       N19      N7       N15      N8       N20      N4       N11      N3
  F6     N4       N20      N8       N16      N5       N17      N1       N12      N4

  : Faces by Nodes of Hexa20

## Elemento Pentaedro (prisma) 

<img alt="" src=images/FEM_mesh_elements_6_pentahedron.svg  style="width:600px;">

  Edge   Node 1   Node 2   Middle node
  ------ -------- -------- -------------
  E1     N1       N2       N7
  E2     N2       N3       N8
  E3     N3       N1       N9
  E4     N4       N5       N10
  E5     N5       N6       N11
  E6     N6       N4       N12
  E7     N1       N4       N13
  E8     N2       N5       N14
  E9     N3       N6       N15

  : Edges of Penta6 and Penta15

  Face   Edge 1   Edge 2   Edge 3   Edge 4
  ------ -------- -------- -------- --------
  F1     E1       E2       E3       \_
  F2     -E6      -E5      -E4      \_
  F3     E7       E4       -E8      -E1
  F4     E8       E5       -E9      -E2
  F5     E9       E6       -E7      -E3

  : Faces by Edges of Penta6 and Penta15

  Face   Node 1   Node 2   Node 3   Node 4   Node 1
  ------ -------- -------- -------- -------- --------
  F1     N1       N2       N3       \_       N1
  F2     N4       N6       N5       \_       N4
  F3     N1       N4       N5       N2       N1
  F4     N2       N5       N6       N3       N2
  F5     N3       N6       N4       N1       N3

  : Faces by Nodes of Penta6

  Face   Node 1   Node 2   Node 3   Node 4   Node 5   Node 6   Node 7   Node 8   Node 1
  ------ -------- -------- -------- -------- -------- -------- -------- -------- --------
  F1     N1       N7       N2       N8       N3       N9       \_       \_       N1
  F2     N4       N12      N6       N11      N5       N10      \_       \_       N4
  F3     N1       N13      N4       N10      N5       N14      N2       N7       N1
  F4     N2       N14      N5       N11      N6       N15      N3       N8       N2
  F5     N3       N15      N6       N12      N4       N13      N1       N9       N3

  : Faces by Nodes of Penta15

## Elemento Piramide 

<img alt="" src=images/FEM_mesh_elements_7_pyramid.svg  style="width:600px;">

  Edge   Node 1   Node 2   Middle node
  ------ -------- -------- -------------
  E1     N1       N2       N6
  E2     N2       N3       N7
  E3     N3       N4       N8
  E4     N4       N1       N9
  E5     N1       N5       N10
  E6     N2       N5       N11
  E7     N3       N5       N12
  E8     N4       N5       N13

  : Edges of Pyra5 and Pyra13

  Face   Edge 1   Edge 2   Edge 3   Edge 4
  ------ -------- -------- -------- --------
  F1     E1       E2       E3       E4
  F2     E5       -E6      -E1      \_
  F3     E6       -E7      -E2      \_
  F4     E7       -E8      -E3      \_
  F5     E8       E5       -E4      \_

  : Faces by Edges of Pyra5 and Pyra13

  Face   Node 1   Node 2   Node 3   Node4   Node1
  ------ -------- -------- -------- ------- -------
  F1     N1       N2       N3       N4      N1
  F2     N1       N5       N2       \_      N1
  F3     N2       N5       N3       \_      N2
  F4     N3       N5       N4       \_      N3
  F5     N4       N5       N1       \_      N4

  : Faces by Nodes of Pyra5

  Face   Node 1   Node 2   Node 3   Node4   Node 5   Node 6   Node 7   Node8   Node1
  ------ -------- -------- -------- ------- -------- -------- -------- ------- -------
  F1     N1       N6       N2       N7      N3       N8       N4       N9      N1
  F2     N1       N10      N5       N11     N2       N6       \_       \_      N1
  F3     N2       N11      N5       N12     N13      N7       \_       \_      N2
  F4     N3       N12      N5       N13     N4       N8       \_       \_      N3
  F5     N4       N13      N5       N10     N1       N9       \_       \_      N4

  : Faces by Nodes of Pyra13


{{FEM Tools navi

}}  

_ _

---
[documentation index](../README.md) > [Developer](Category_Developer.md) > FEM Element Types/it
