# Mesh MeshObject/pl
## Opis

**Siatka: Obiekt siatki**, lub formalnie `Mesh::MeshObject`, jest klasą, która definiuje strukturę danych siatki w oprogramowaniu. Jest to podobne do obiektu [Część: Kształt topologiczny](Part_TopoShape/pl.md), ale dla [siatek](Mesh/pl.md).

Siatki są zwykle tworzone za pomocą środowiska pracy [Projekt Siatki](Mesh_Workbench/pl.md) lub importowane z plików STL, OBJ i podobnych formatów siatek.

Proszę zauważyć, że środowisko pracy **<img src="images/Workbench_FEM.svg" width=16px> [MES](FEM_Workbench/pl.md)** również wykorzystuje siatki, ale w tym przypadku używa innej struktury danych, zwanej [MES: Siatka](FEM_Mesh/pl.md) *(klasa `Fem::FemMesh`)*. Ta informacja nie dotyczy siatek MES.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony schemat zależności pomiędzy podstawowymi obiektami programu. Klasa `Mesh::MeshObject* jest osadzona w obiekcie {{incode|Mesh::Feature` i stamtąd jest propagowana do wszystkich obiektów, które są od niej pochodne.}}

## Użycie

Siatka: MeshObject jest obiektem, który jest przypisany do niektórych [App: Obiektów dokumentu](App_DocumentObject/pl.md).

W szczególności podstawowym obiektem obsługującym tego typu atrybuty jest [cecha siatki](Mesh_Feature/pl.md) *(klasa `Mesh::Feature`)*. Wszystkie obiekty wywodzące się z tej klasy będą miały dostęp do obiektu typu Siatka: MeshObject.

Najbardziej godne uwagi obiekty, które będą posiadały MeshObject to:

-   Każda siatka elementu pierwotnego utworzona za pomocą środowiska pracy [Projekt Siatki](Mesh_Workbench/pl.md)
-   Każdy obiekt utworzony przez import plików w formacie STL, OBJ i podobnych siatek.

## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty tworzone skryptami](Scripted_objects/pl.md). Pełną listę atrybutów i metod można znaleźć w [dokumentacji źródeł](Source_documentation/pl.md) oraz w opisie narzędzia [Pomoc dla środowiska Python](Std_PythonHelp/pl.md).

Wszystkie obiekty pochodzące z `Mesh::Feature` będą miały [Obiekt siatki](Mesh_MeshObject/pl.md) środowiska Projekt Siatki, który jest normalnie dostępny z atrybutu `Kształt`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Cube", "Cube")
App.ActiveDocument.recompute()
print(obj.Mesh)
```

MeshObject posiada wiele atrybutów *(zmiennych)* i metod, które zawierają informacje o nim i które pozwalają na wykonywanie na nim operacji. Te zmienne i metody mogą być testowane w [konsoli Python](Python_console/pl.md).


```python
print(obj.Mesh.Area)
print(obj.Mesh.BoundBox)
print(obj.Mesh.CountPoints)
print(obj.Mesh.Volume)

obj.Mesh.copy()
obj.Mesh.countComponents()
obj.Mesh.getEigenSystem()
obj.Mesh.write("my_file.stl")
```


{{Mesh Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh MeshObject/pl
