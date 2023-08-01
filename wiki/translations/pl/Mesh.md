# Mesh/pl
{{TOCright}}

## Wprowadzenie

W FreeCAD słowo \"[Siatka](Mesh/pl.md)\" jest zwykle używane w odniesieniu do [obiektu siatki](Mesh_MeshObject/pl.md) *(klasa `Mesh::MeshObject`)*, typu obiektu, który definiuje dane 3D, ale nie jest \"[kształtem](Shape/pl.md)\" bryły.

Siatki to bardzo proste obiekty, zawierające jedynie wierzchołki *(punkty)*, krawędzie i trójkątne ściany. Ogólnie rzecz biorąc, są one łatwe do tworzenia, modyfikowania, dzielenia i rozciągania, i mogą być przekazywane z jednej aplikacji do drugiej bez utraty szczegółów. Ponadto, ponieważ siatki zawierają bardzo proste dane, aplikacje 3D, takie jak oprogramowanie do animacji i gry wideo, mogą zarządzać bardzo dużymi ich ilościami *(milionami trójkątów)* bez zużywania dużych zasobów obliczeniowych.

Jednak w dziedzinie inżynierii siatki mają jedno duże ograniczenie: są zbudowane tylko z powierzchni i nie mają informacji o \"masie\", więc nie zachowują się jak \"bryły\". Oznacza to, że operacje oparte na bryłach, takie jak [Operacje logiczne na bryłach](Part_Boolean/pl.md), są trudne do wykonania na siatkach. Ponadto, ponieważ są one zdefiniowane przez pojedyncze punkty, trudno je opisać w sposób parametryczny.

Zobacz stronę [Siatka: Obiekt siatki](Mesh_MeshObject/pl.md), aby uzyskać więcej informacji o tym typie obiektu, oraz [Siatka wielokąta](https://en.wikipedia.org/wiki/Polygon_mesh) dla ogólnych informacji w systemach komputerowych.

![](images/Shape_and_mesh.svg )



*Po lewej: [Kształt](Shape/pl.md) parametryczny zdefiniowany przez właściwości. <br>Po prawej: [Siatka](Mesh/pl.md), zdefiniowana przez wierzchołki i powierzchnie trójkątne.*

## Użycie

Siatki są zwykle tworzone przez wewnętrzne funkcje środowiska pracy [Siatka](Mesh_Workbench/pl.md), lub przez import plików w formacie siatki, jak np STL i OBJ.

Zasadniczo, każdy obiekt wywodzący się z [Siatka: Cecha](Mesh_Feature/pl.md) *(klasa `Mesh::Feature`)* ma za zadanie trzymać i manipulować Siatką.

Ponieważ FreeCAD jest przede wszystkim zaprojektowany jako modeler bryłowy, jest lepiej przystosowany do radzenia sobie z [kształtami](Shape/pl.md) brył. Może importować i wyświetlać siatki w oknie [widoku 3D](3D_view/pl.md), a środowisko pracy [Siatka](Mesh_Workbench/pl.md) oferuje kilka poleceń do bezpośredniego manipulowania nimi. Jednak w wielu przypadkach siatka musi być najpierw przekonwertowana na [Kształt](Shape/pl.md) *(zobacz stronę [Część: Kształt z siatki](Part_ShapeFromMesh/pl.md))*, lub geometria musi być odtworzona przy użyciu technik modelowania bryłowego w środowisku pracy [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md).

## Siatki elementu skończonego 

W FreeCAD słowo \"[siatka](Mesh/pl.md)\" może również odnosić się do konkretnego obiektu, który będzie wykorzystywany w analizie metodą elementów skończonych *(MES)*.

Gdy obiekt z bryłą [Kształt](Shape/pl.md) jest używany w środowisku pracy [FEM Workbench](FEM_Workbench/pl.md), zostanie on rozłożony do siatki trójkątów. W tym przypadku obiekt wynikowy jest obiektem [MES: Siatka](FEM_Mesh/pl.md) *(klasa `Fem::FemMeshObject`)* i nie jest pochodną [Siatka: Cecha](Mesh_Feature/pl.md) *(klasa `Mesh::Feature`)*.

Więcej informacji można znaleźć na stronach [środowisko pracy MES](FEM_Workbench/pl.md) i [siatka MES](FEM_Mesh/pl.md).

## Informacje dodatkowe 

-   [Geometria poligonalna *(siatkowa)*](https://forum.freecadweb.org/viewtopic.php?f=8&t=47493)


{{Mesh Tools navi

}} {{FEM Tools navi}} {{Document objects navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Category_Mesh.md) > [FEM](Category_FEM.md) > Mesh/pl
