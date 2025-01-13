---
 GuiCommand:
   Name: Part ShapeFromMesh‏‎
   Name/pl: Część: Utwórz kształt z siatki
   MenuLocation: Part , Utwórz kształt z siatki ...
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_MakeSolid/pl, Part_RefineShape/pl, Part_PointsFromMesh/pl
---

# Part ShapeFromMesh/pl



## Wprowadzenie

Polecenie **<img src="images/Part_ShapeFromMesh.svg" width=16px> '''Utwórz kształt z siatki'''** tworzy kształty z [obiektów siatki](Mesh/pl.md). Obiekty siatki mają ograniczone możliwości edycji w programie FreeCAD, konwersja do [kształtu](Shape/pl.md) pozwoli na ich użycie z wieloma innymi narzędziami logicznymi i modyfikującymi.

Operacja odwrotna to [Siatka z kształtu](Mesh_FromPartShape/pl.md) ze środowiska pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md).



## Użycie

1.  Analiza i naprawa obiektu siatki, jeśli to konieczne, powinna być wykonana przed uruchomieniem tego polecenia. Odpowiednie narzędzia do tego zadania dostępne są w środowisku pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Siatka](Mesh_Workbench/pl.md).
2.  Wybierz jeden lub więcej obiektów siatki.
3.  Wybierz opcję **Część → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Utwórz kształt z siatki ...** z menu.
4.  Otworzy się okno dialogowe **Kształt z siatki**.
5.  Opcjonalnie zaznacz pole wyboru **Zszyj kształt** i określ tolerancję:
    -   Opcja ta zazwyczaj nie jest potrzebna. Jest ona przeznaczona dla obiektów siatkowych, które nie są wodoszczelne i mają małe odstępy między krawędziami.
    -   Jeśli opcja jest zaznaczona, tworzone jest złożenie powłok zamiast złożenia ścian.
    -   Operacja szycia może być wymagająca obliczeniowo.
6.  Naciśnij przycisk **OK**.
7.  Dla każdego wybranego obiektu siatki zostanie utworzony [kształt](Shape/pl.md) jako oddzielny nowy obiekt.
8.  Opcjonalnie użyj funkcji <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Udoskonal kształt](Part_RefineShape/pl.md) na tych obiektach.
9.  Opcjonalnie przekształć ten obiekt w bryłę za pomocą polecenia <img alt="" src=images/Part_MakeSolid.svg  style="width:16px;"> [Przekształć na bryłę](Part_MakeSolid/pl.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Tworzone są obiekty [Część: Cecha](Part_Feature/pl.md) bez dodatkowych właściwości.



## Tworzenie skryptów 

Tworzenie [kształtu](Shape/pl.md) z [siatki](Mesh/pl.md) może być wykonane za pomocą metody `makeShapeFromMesh` z [kształtu topologicznego](Part_TopoShape/pl.md). Musisz określić siatkę źródłową i tolerancję, a następnie przypisać wynik do nowego obiektu [Cechy](Part_Feature/pl.md).

Należy zauważyć, że siatka musi zostać ponownie obliczona przed konwersją do Kształtu, w przeciwnym razie nie będzie informacji o topologii, a konwersja nie powiedzie się.


```python
import FreeCAD as App
import Part

doc = App.ActiveDocument
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid = doc.addObject("Part::Feature", "Solid")
solid.Shape = Part.Solid(shape.removeSplitter())
solid.Placement.Base = App.Vector(15, 0, 0)
doc.recompute()
```



## Odnośniki internetowe 

-   [Edytuj pliki STL w FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) wideo autorstwa AllVisuals4U.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/pl
