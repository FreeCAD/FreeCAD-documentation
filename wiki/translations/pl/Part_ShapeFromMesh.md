---
- GuiCommand:
   Name: Part ShapeFromMesh‏‎
   Name/pl: Część: Utwórz kształt z siatki
   MenuLocation: Part -> Utwórz kształt z siatki ...
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_MakeSolid/pl, Part_RefineShape/pl, Part_PointsFromMesh/pl
---

# Part ShapeFromMesh/pl



## Wprowadzenie

Polecenie **<img src="images/Part_ShapeFromMesh.svg" width=16px> '''Utwórz kształt z siatki'''** tworzy kształt z [obiektu siatkowego](Mesh/pl.md). Obiekty siatkowe mają ograniczone możliwości edycji w FreeCAD, konwersja ich do [kształtu](Shape/pl.md) pozwoli na ich użycie z wieloma innymi narzędziami logicznymi i modyfikującymi.

Operacja odwrotna to **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Siatka z kształtu](Mesh_FromPartShape/pl.md)** ze środowiska pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatki](Mesh_Workbench/pl.md).



## Użycie

1.  Wybierz obiekt siatki w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Przejdź do menu **Część → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Utwórz kształt z siatki ...**
3.  Pojawi się wyskakujące okienko z pytaniem o tolerancję szycia kształtu, domyślną wartością jest {{Value|0.1}}.
4.  [Kształt](Shape/pl.md) z obiektu siatki jest tworzony jako oddzielny nowy obiekt.

Analiza i naprawa siatki, jeśli to konieczne, powinna być wykonana ręcznie przed uruchomieniem narzędzia **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> '''Utwórz kształt z siatki ...'''**. Odpowiednie narzędzia do tego zadania dostępne są w środowisku pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md).

Po utworzeniu [Kształtu](Shape/pl.md) przydatne może być użycie narzędzia **[<img src=images/Part_MakeSolid.svg style="width:16px"> [Przekształć na bryłę](Part_MakeSolid/pl.md)** *(niezbędne dla operacji [logicznych](Part_Boolean.md))* oraz **[<img src=images/Part_RefineShape.svg style="width:16px"> [Udoskonal kształt](Part_RefineShape/pl.md)**.



## Odnośniki internetowe 

-   [Edytuj pliki STL w FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) wideo autorstwa AllVisuals4U.



## Tworzenie skryptów 

Tworzenie [kształtu](Shape/pl.md) z [siatki](Mesh/pl.md) może być wykonane za pomocą metody `makeShapeFromMesh` z [kształtu topologicznego](Part_TopoShape/pl.md). Musisz określić siatkę źródłową i tolerancję, a następnie przypisać wynik do nowego obiektu [Cechy](Part_Feature/pl.md).

Należy zauważyć, że siatka musi zostać ponownie obliczona przed konwersją do Kształtu, w przeciwnym razie nie będzie informacji o topologii, a konwersja nie powiedzie się.


```python
import FreeCAD as App
import Part

doc = App.newDocument()
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

solid = doc.addObject("Part::Feature", "Shape")
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid.Shape = shape
solid.Placement.Base = App.Vector(15, 0, 0)
solid.purgeTouched()
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/pl
