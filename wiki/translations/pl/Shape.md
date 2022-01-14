# Shape/pl
## Wprowadzenie

W programie FreeCAD słowo **[kształt](Shape/pl.md)** jest zwykle używane w odniesieniu do [kształtu topologicznego](Part_TopoShape/pl.md) *(klasa `Part::TopoShape`)*, typu obiektu, który nadaje elementowi jego trójwymiarową reprezentację geometryczną i parametryczną *(sześcian, ostrosłup, sfera, walec, zespolenie itd.)*.

Zasadniczo wszystkie obiekty, które są wyświetlane w oknie [widoku 3D](3D_view/pl.md) posiadają [Kształt topologiczny](Part_TopoShape/pl.md), z wyjątkiem **[Siatek](Mesh/pl.md)**, które posiadają [Obiekt siatkowy](Mesh_MeshObject/pl.md) *(klasa `Mesh::MeshObject`)*.

Zobacz stronę [Część: Kształt topologiczny](Part_TopoShape/pl.md) aby uzyskać więcej informacji na temat tego typu obiektu.

![](images/Shape_and_mesh.svg )



*Po lewej: [Kształt](Shape/pl.md) parametryczny zdefiniowany przez właściwości. <br>Po prawej: [Siatka](Mesh/pl.md), zdefiniowana przez wierzchołki i powierzchnie trójkątne.*

## Użycie

Kształty są zwykle tworzone przez wewnętrzne funkcje środowiska pracy [Część](Part_Workbench/pl.md), i są ostatecznie definiowane przez kernel *(OCCT)* w technologii [OpenCASCADE](OpenCASCADE/pl.md).

Raz utworzony Kształt może być używany i modyfikowany przez wszystkie [środowiska pracy](Workbenches/pl.md) poprzez [obiekty tworzone skryptami](Scripted_objects/pl.md) wokół tego Kształtu.

Zasadniczo, każdy obiekt wywodzący się z [Część: Cecha](Part_Feature/pl.md) *(klasa `Part::Feature`)* ma za zadanie trzymać i manipulować Kształtem.

## Uwagi

W nieformalnym użyciu, \"Kształt\" może być dowolną figurą geometryczną, która jest widoczna w oknie [widoku 3D](3D_view/pl.md), a zatem jego pojęcie może być mylone z pojęciem \"[Zawartości](Body/pl.md)\" lub \"[Części](Part/pl.md)\".

Jednakże, gdy wymagana jest większa precyzja, należy dokonać rozróżnienia.

-   \"[Zawartość](Body/pl.md)\" to obiekt wywodzący się z obiektu [Część: Cecha](Part_Feature/pl.md) *(klasy `Part::Feature`)*, utworzony za pomocą środowiska pracy [Projekt Części](PartDesign_Workbench.md).
-   \"Kształt\" jest obiektem wewnętrznym, osadzonym w \"[Zawartości](Body/pl.md)\".
-   [Część](Part/pl.md)\" jest używana do grupowania kilku \"[zawartości](Body/pl.md)\" w celu utworzenia [złożenia](Assembly/pl.md). \"Część\" posiada kolekcję \"Kształtów\", ale nie posiada własnego \"Kształtu\".


 {{Document objects navi}} 

[<img src="images/Property.png" style="width:16px"> Glossary](Category_Glossary.md)

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Shape/pl
