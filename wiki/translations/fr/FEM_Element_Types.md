 {{TOCright}}

## Introduction

Cette description est basée sur le format MED décrit dans \[<https://hammi.extra.cea.fr/static/MED/web_med/logiciels/med-2.3.1/doc/html/modele_de_donnees.html#3>. modèle de données\].

## Les segments {#les_segments}

<img alt="" src=images/FEM_mesh_elements_1_segment.svg  style="width:600px;">

  Arête   Sommet 1   Sommet 2   Milieu
  ------- ---------- ---------- --------
  E1      N1         N2         N3

  : **Arêtes de Seg2 et Seg3**

## Les triangles {#les_triangles}

<img alt="" src=images/FEM_mesh_elements_2_triangle.svg  style="width:600px;">

  Arête   Sommet 1   Sommet 2   Milieu
  ------- ---------- ---------- --------
  E1      N1         N2         N4
  E2      N2         N3         N5
  E3      N3         N1         N6

  : **Sommets du Tria3 et Tria6**

  Face   Arête 1   Arête 2   Arête 3
  ------ --------- --------- ---------
  F1     E1        E2        E3

  : **Face par arêtes du Tria3 et Tria6**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 1
  ------ --------- --------- --------- ---------
  F1     N1        N2        N3        N1

  : **Face par noeuds du Tria3**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 5   Noeud 6   Noeud 1
  ------ --------- --------- --------- --------- --------- --------- ---------
  F1     N1        N4        N2        N5        N3        N6        N1

  : **Face par Noeud du Tria6**

## Les quadrangles {#les_quadrangles}

<img alt="" src=images/FEM_mesh_elements_3_quadrangle.svg  style="width:600px;">

  Arête   Noeud 1   Noeud 2   Milieu
  ------- --------- --------- --------
  E1      N1        N2        N5
  E2      N2        N3        N6
  E3      N3        N4        N7
  E4      N4        N1        N8

  : **Arêtes du Quad4 et Quad8**

  Face   Arête 1   Arête 2   Arête 3   Arête 4
  ------ --------- --------- --------- ---------
  F1     E1        E2        E3        E4

  : **Face par arêtes du Quad4 et Quad8**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 1
  ------ --------- --------- --------- --------- ---------
  F1     N1        N2        N3        N4        N1

  : **Face par noeuds du Quad4**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 5   Noeud 6   Noeud 7   Noeud 8   Noeud 1
  ------ --------- --------- --------- --------- --------- --------- --------- --------- ---------
  F1     N1        N5        N2        N6        N3        N7        N4        N8        N1

  : **Face par noeuds du Quad8**

## Les tétraèdres {#les_tétraèdres}

<img alt="" src=images/FEM_mesh_elements_4_tetrahedron.svg  style="width:600px;">

  Arête   Noeud 1   Noeud 2   Milieu
  ------- --------- --------- --------
  E1      N1        N2        N5
  E2      N2        N3        N6
  E3      N3        N1        N7
  E4      N1        N4        N8
  E5      N2        N4        N9
  E6      N3        N4        N10

  : **Arêtes du Tetra4 et Tetra10**

  Face   Arête 1   Arête 2   Arête 3
  ------ --------- --------- ---------
  F1     E1        E2        E3
  F2     E4        -E5       -E1
  F3     E5        -E6       -E2
  F4     E6        -E4       -E3

  : **Faces par arêtes du Tetra4 et Tetra10**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 1
  ------ --------- --------- --------- ---------
  F1     N1        N2        N3        N1
  F2     N1        N4        N2        N1
  F3     N2        N4        N3        N2
  F4     N3        N4        N1        N3

  : **Faces par noeuds du Tetra4**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 5   Noeud 6   Noeud 1
  ------ --------- --------- --------- --------- --------- --------- ---------
  F1     N1        N5        N2        N6        N3        N7        N1
  F2     N1        N8        N4        N9        N2        N5        N1
  F3     N2        N9        N4        N10       N3        N6        N2
  F4     N3        N10       N4        N8        N1        N7        N3

  : **Faces par noeuds du Tetra10**

## Les hexaèdres {#les_hexaèdres}

<img alt="" src=images/FEM_mesh_elements_5_hexahedron.svg  style="width:600px;">

  Arête   Noeud 1   Noeud 2   Milieu
  ------- --------- --------- --------
  E1      N1        N2        N9
  E2      N2        N3        N10
  E3      N3        N4        N11
  E4      N4        N1        N12
  E5      N5        N6        N13
  E6      N6        N7        N14
  E7      N7        N8        N15
  E8      N8        N5        N16
  E9      N1        N5        N17
  E10     N2        N6        N18
  E11     N3        N7        N19
  E12     N4        N8        N20

  : **Arêtes d\'Hexa8 et Hexa20**

  Face   Arête 1   Arête 2   Arête 3   Arête 4
  ------ --------- --------- --------- ---------
  F1     E1        E2        E3        E4
  F2     -E8       -E7       -E6       -E5
  F3     E9        E5        -E10      -E1
  F4     E10       E6        -E11      -E2
  F5     E11       E7        -E12      -E3
  F6     E12       E8        -E9       -E4

  : **Faces par arête d\'Hexa8 et Hexa20**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 1
  ------ --------- --------- --------- --------- ---------
  F1     N1        N2        N3        N4        N1
  F2     N5        N8        N7        N6        N5
  F3     N1        N5        N6        N2        N1
  F4     N2        N6        N7        N3        N2
  F5     N3        N7        N8        N4        N3
  F6     N4        N8        N5        N1        N4

  : **Faces par noeuds d\'Hexa8**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 5   Noeud 6   Noeud 7   Noeud 8   Noeud 1
  ------ --------- --------- --------- --------- --------- --------- --------- --------- ---------
  F1     N1        N9        N2        N10       N3        N11       N4        N12       N1
  F2     N5        N16       N8        N15       N7        N14       N6        N13       N5
  F3     N1        N17       N5        N13       N6        N18       N2        N9        N1
  F4     N2        N18       N6        N14       N7        N19       N3        N10       N2
  F5     N3        N19       N7        N15       N8        N20       N4        N11       N3
  F6     N4        N20       N8        N16       N5        N17       N1        N12       N4

  : **Faces par noeud d\'Hexa20**

## Les pentaèdres (prismes) {#les_pentaèdres_prismes}

<img alt="" src=images/FEM_mesh_elements_6_pentahedron.svg  style="width:600px;">

  Arête   Noeud 1   Noeud 2   Milieu
  ------- --------- --------- --------
  E1      N1        N2        N7
  E2      N2        N3        N8
  E3      N3        N1        N9
  E4      N4        N5        N10
  E5      N5        N6        N11
  E6      N6        N4        N12
  E7      N1        N4        N13
  E8      N2        N5        N14
  E9      N3        N6        N15

  : **Arêtes du Penta6 et Penta15**

  Face   Arête 1   Arête 2   Arête 3   Arête 4
  ------ --------- --------- --------- ---------
  F1     E1        E2        E3        \_
  F2     -E6       -E5       -E4       \_
  F3     E7        E4        -E8       -E1
  F4     E8        E5        -E9       -E2
  F5     E9        E6        -E7       -E3

  : **Faces par arêtes du Penta6 et Penta15**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 1
  ------ --------- --------- --------- --------- ---------
  F1     N1        N2        N3        \_        N1
  F2     N4        N6        N5        \_        N4
  F3     N1        N4        N5        N2        N1
  F4     N2        N5        N6        N3        N2
  F5     N3        N6        N4        N1        N3

  : **Faces par noeuds du of Penta6**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 5   Noeud 6   Noeud 7   Noeud 8   Noeud 1
  ------ --------- --------- --------- --------- --------- --------- --------- --------- ---------
  F1     N1        N7        N2        N8        N3        N9        \_        \_        N1
  F2     N4        N12       N6        N11       N5        N10       \_        \_        N4
  F3     N1        N13       N4        N10       N5        N14       N2        N7        N1
  F4     N2        N14       N5        N11       N6        N15       N3        N8        N2
  F5     N3        N15       N6        N12       N4        N13       N1        N9        N3

  : **Faces par noeuds du Penta15**

## Les pyramides {#les_pyramides}

<img alt="" src=images/FEM_mesh_elements_7_pyramid.svg  style="width:600px;">

  Arête   Noeud 1   Noeud 2   Milieu
  ------- --------- --------- --------
  E1      N1        N2        N6
  E2      N2        N3        N7
  E3      N3        N4        N8
  E4      N4        N1        N9
  E5      N1        N5        N10
  E6      N2        N5        N11
  E7      N3        N5        N12
  E8      N4        N5        N13

  : **Arêtes de Pyra5 et Pyra13**

  Face   Arête 1   Arête 2   Arête 3   Arête 4
  ------ --------- --------- --------- ---------
  F1     E1        E2        E3        E4
  F2     E5        -E6       -E1       \_
  F3     E6        -E7       -E2       \_
  F4     E7        -E8       -E3       \_
  F5     E8        E5        -E4       \_

  : **Faces par arêtes de Pyra5 et Pyra13**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 1
  ------ --------- --------- --------- --------- ---------
  F1     N1        N2        N3        N4        N1
  F2     N1        N5        N2        \_        N1
  F3     N2        N5        N3        \_        N2
  F4     N3        N5        N4        \_        N3
  F5     N4        N5        N1        \_        N4

  : **Faces par noeuds de Pyra5**

  Face   Noeud 1   Noeud 2   Noeud 3   Noeud 4   Noeud 5   Noeud 6   Noeud 7   Noeud 8   Noeud 1
  ------ --------- --------- --------- --------- --------- --------- --------- --------- ---------
  F1     N1        N6        N2        N7        N3        N8        N4        N9        N1
  F2     N1        N10       N5        N11       N2        N6        \_        \_        N1
  F3     N2        N11       N5        N12       N13       N7        \_        \_        N2
  F4     N3        N12       N5        N13       N4        N8        \_        \_        N3
  F5     N4        N13       N5        N10       N1        N9        \_        \_        N4

  : **Faces par noeuds de Pyra13**


{{FEM Tools navi

}}  

[Category:Developer{{\#translation:}}](Category:Developer.md) [Category:Poweruser\_Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)
