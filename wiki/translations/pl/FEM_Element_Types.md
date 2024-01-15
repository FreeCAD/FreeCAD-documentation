# FEM Element Types/pl
## Wprowadzenie

Ten opis jest oparty na formacie MED opisanym na stronie \[<https://hammi.extra.cea.fr/static/MED/web_med/logiciels/med-2.3.1/doc/html/modele_de_donnees.html#3>. model danych *(w języku francuskim)*\].



## Element 1D 

<img alt="" src=images/FEM_mesh_elements_1_segment.svg  style="width:600px;">

  Krawędź   Węzeł 1   Węzeł 2   Węzeł środkowy
     
  E1        N1        N2        N3

  : Krawędzie elementów Seg2 i Seg3



## Element trójkątny 

<img alt="" src=images/FEM_mesh_elements_2_triangle.svg  style="width:600px;">

  Krawędź   Węzeł 1   Węzeł 2   Węzeł środkowy
     
  E1        N1        N2        N4
  E2        N2        N3        N5
  E3        N3        N1        N6

  : Krawędzie elementów Tria3 i Tria6

  Ściana   Krawędź 1   Krawędź 2   Krawędź 3
     
  F1       E1          E2          E3

  : Ściana z krawędzi elementów Tria3 i Tria6

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 1
      
  F1       N1        N2        N3        N1

  : Ściana z węzłów elementu Tria3

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 5   Węzeł 6   Węzeł 1
         
  F1       N1        N4        N2        N5        N3        N6        N1

  : Ściana z węzłów elementu Tria6



## Element czworokątny 

<img alt="" src=images/FEM_mesh_elements_3_quadrangle.svg  style="width:600px;">

  Krawędź   Węzeł 1   Węzeł 2   Węzeł środkowy
     
  E1        N1        N2        N5
  E2        N2        N3        N6
  E3        N3        N4        N7
  E4        N4        N1        N8

  : Krawędzie elementów Quad4 i Quad8

  Ściana   Krawędź 1   Krawędź 2   Krawędź 3   Krawędź 4
      
  F1       E1          E2          E3          E4

  : Ściana z krawędzi elementów Quad4 i Quad8

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 1
       
  F1       N1        N2        N3        N4        N1

  : Ściana z węzłów elementu Quad4

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 5   Węzeł 6   Węzeł 7   Węzeł 8   Węzeł 1
           
  F1       N1        N5        N2        N6        N3        N7        N4        N8        N1

  : Ściana z węzłów elementu Quad8



## Element czworościenny 

<img alt="" src=images/FEM_mesh_elements_4_tetrahedron.svg  style="width:600px;">

  Krawędź   Węzeł 1   Węzeł 2   Węzeł środkowy
     
  E1        N1        N2        N5
  E2        N2        N3        N6
  E3        N3        N1        N7
  E4        N1        N4        N8
  E5        N2        N4        N9
  E6        N3        N4        N10

  : Krawędzie elementów Tetra4 i Tetra10

  Ściana   Krawędź 1   Krawędź 2   Krawędź 3
     
  F1       E1          E2          E3
  F2       E4          -E5         -E1
  F3       E5          -E6         -E2
  F4       E6          -E4         -E3

  : Ściana z krawędzi elementów Tetra4 i Tetra10

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 1
      
  F1       N1        N2        N3        N1
  F2       N1        N4        N2        N1
  F3       N2        N4        N3        N2
  F4       N3        N4        N1        N3

  : Ściany z węzłów elementu Tetra4

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 5   Węzeł 6   Węzeł 1
         
  F1       N1        N5        N2        N6        N3        N7        N1
  F2       N1        N8        N4        N9        N2        N5        N1
  F3       N2        N9        N4        N10       N3        N6        N2
  F4       N3        N10       N4        N8        N1        N7        N3

  : Ściany z węzłów elementu Tetra10



## Element prostopadłościenny 

<img alt="" src=images/FEM_mesh_elements_5_hexahedron.svg  style="width:600px;">

  Krawędź   Węzeł 1   Węzeł 2   Węzeł środkowy
     
  E1        N1        N2        N9
  E2        N2        N3        N10
  E3        N3        N4        N11
  E4        N4        N1        N12
  E5        N5        N6        N13
  E6        N6        N7        N14
  E7        N7        N8        N15
  E8        N8        N5        N16
  E9        N1        N5        N17
  E10       N2        N6        N18
  E11       N3        N7        N19
  E12       N4        N8        N20

  : Krawędzie elementów Hexa8 i Hexa20

  Ściana   Krawędź 1   Krawędź 2   Krawędź 3   Krawędź 4
      
  F1       E1          E2          E3          E4
  F2       -E8         -E7         -E6         -E5
  F3       E9          E5          -E10        -E1
  F4       E10         E6          -E11        -E2
  F5       E11         E7          -E12        -E3
  F6       E12         E8          -E9         -E4

  : Ściany z krawędzi elementów Hexa8 i Hexa20

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 1
       
  F1       N1        N2        N3        N4        N1
  F2       N5        N8        N7        N6        N5
  F3       N1        N5        N6        N2        N1
  F4       N2        N6        N7        N3        N2
  F5       N3        N7        N8        N4        N3
  F6       N4        N8        N5        N1        N4

  : Ściany z węzłów elementu Hexa8

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 5   Węzeł 6   Węzeł 7   Węzeł 8   Węzeł 1
           
  F1       N1        N9        N2        N10       N3        N11       N4        N12       N1
  F2       N5        N16       N8        N15       N7        N14       N6        N13       N5
  F3       N1        N17       N5        N13       N6        N18       N2        N9        N1
  F4       N2        N18       N6        N14       N7        N19       N3        N10       N2
  F5       N3        N19       N7        N15       N8        N20       N4        N11       N3
  F6       N4        N20       N8        N16       N5        N17       N1        N12       N4

  : Ściany z węzłów elementu Hexa20



## Element pięciościenny 

<img alt="" src=images/FEM_mesh_elements_6_pentahedron.svg  style="width:600px;">

  Krawędź   Węzeł 1   Węzeł 2   Węzeł środkowy
     
  E1        N1        N2        N7
  E2        N2        N3        N8
  E3        N3        N1        N9
  E4        N4        N5        N10
  E5        N5        N6        N11
  E6        N6        N4        N12
  E7        N1        N4        N13
  E8        N2        N5        N14
  E9        N3        N6        N15

  : Krawędzie elementów Penta6 i Penta15

  Ściana   Krawędź 1   Krawędź 2   Krawędź 3   Krawędź 4
      
  F1       E1          E2          E3          \_
  F2       -E6         -E5         -E4         \_
  F3       E7          E4          -E8         -E1
  F4       E8          E5          -E9         -E2
  F5       E9          E6          -E7         -E3

  : Ściany z krawędzi elementów Penta6 i Penta15

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 1
       
  F1       N1        N2        N3        \_        N1
  F2       N4        N6        N5        \_        N4
  F3       N1        N4        N5        N2        N1
  F4       N2        N5        N6        N3        N2
  F5       N3        N6        N4        N1        N3

  : Ściany z krawędzi elementu Penta6

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 5   Węzeł 6   Węzeł 7   Węzeł 8   Węzeł 1
           
  F1       N1        N7        N2        N8        N3        N9        \_        \_        N1
  F2       N4        N12       N6        N11       N5        N10       \_        \_        N4
  F3       N1        N13       N4        N10       N5        N14       N2        N7        N1
  F4       N2        N14       N5        N11       N6        N15       N3        N8        N2
  F5       N3        N15       N6        N12       N4        N13       N1        N9        N3

  : Ściany z węzłów elementu Penta15



## Element piramidalny 

<img alt="" src=images/FEM_mesh_elements_7_pyramid.svg  style="width:600px;">

  Krawędź   Węzeł 1   Węzeł 2   Węzeł środkowy
     
  E1        N1        N2        N6
  E2        N2        N3        N7
  E3        N3        N4        N8
  E4        N4        N1        N9
  E5        N1        N5        N10
  E6        N2        N5        N11
  E7        N3        N5        N12
  E8        N4        N5        N13

  : Krawędzi elementów Pyra5 i Pyra13

  Ściana   Krawędź 1   Krawędź 2   Krawędź 3   Krawędź 4
      
  F1       E1          E2          E3          E4
  F2       E5          -E6         -E1         \_
  F3       E6          -E7         -E2         \_
  F4       E7          -E8         -E3         \_
  F5       E8          E5          -E4         \_

  : Ściany z krawędzi elementów Pyra5 i Pyra13

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 1
       
  F1       N1        N2        N3        N4        N1
  F2       N1        N5        N2        \_        N1
  F3       N2        N5        N3        \_        N2
  F4       N3        N5        N4        \_        N3
  F5       N4        N5        N1        \_        N4

  : Ściany z węzłów elementu Pyra5

  Ściana   Węzeł 1   Węzeł 2   Węzeł 3   Węzeł 4   Węzeł 5   Węzeł 6   Węzeł 7   Węzeł 8   Węzeł 1
           
  F1       N1        N6        N2        N7        N3        N8        N4        N9        N1
  F2       N1        N10       N5        N11       N2        N6        \_        \_        N1
  F3       N2        N11       N5        N12       N13       N7        \_        \_        N2
  F4       N3        N12       N5        N13       N4        N8        \_        \_        N3
  F5       N4        N13       N5        N10       N1        N9        \_        \_        N4

  : Ściany z węzłów elementu Pyra13


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [FEM](Category_FEM.md) > FEM Element Types/pl
