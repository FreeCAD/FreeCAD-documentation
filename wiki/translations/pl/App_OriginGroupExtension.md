# App OriginGroupExtension/pl
## Wprowadzenie

Obiekt **Rozszerzenie odniesienia położenia grupy** lub formalnie `App::OriginGroupExtension`, to klasa dostarczająca elementy możliwe do zaznaczenia, reprezentujące trzy standardowe osie *(X, Y, Z)* i trzy standardowe płaszczyzny *(XY, XZ i YZ)* dla obiektów, które mają na celu rozmieszczanie różnych typów geometrii w przestrzeni.

<img alt="" src=images/Std_Part.svg  style="width:16px;"> [Std: Część](Std_Part/pl.md) [(App: Część)](App_Part/pl.md) obiektów i <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Projekt Części: Zawartość](PartDesign_Body/pl.md) są domyślnie tworzone z obiektami Odniesienia położenia. W razie potrzeby obiekty Odniesienia położenia można dodać do <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width:16px;"> [Złożenia](Assembly3_CreateAssembly/pl.md) obiektów w środowisku <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Złożenie 3](Assembly3_Workbench/pl.md).

<img alt="Tree view" src=images/App_OriginGroupExtension_example.png  style="width:200px;"> <img alt="3D view" src=images/App_OriginGroupExtension-02.png  style="width:400px;"> 
*Po lewej: [widok drzewa](Tree_view/pl.md) pokazujący trzy obiekty korzystające z obiektów Odniesienia położenia. Po prawej: Reprezentacja elementów Odniesienia położenia w [widoku 3D](3D_view/pl.md).*

Osie i płaszczyzny są obiektami typu `App::Line` i `App::Plane` odpowiednio. Każdy z tych elementów można ukryć i ponownie wyświetlić indywidualnie za pomocą klawisza **Spacja**. Może to być przydatne przy wyborze właściwej odniesienia do tworzenia innych obiektów, np. [Szkiców](Sketch/pl.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagram uproszczonych relacji między głównymi obiektami w programie. Dwa z nich posiadają obiekt Odniesienia położenia ''(Origin)'', aby kontrolować położenie obiektów zgrupowanych pod nimi.*


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App OriginGroupExtension/pl
