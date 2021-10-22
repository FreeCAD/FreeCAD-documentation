# Part TopoShape/pl
{{TOCright}}

## Wprowadzenie

_ zazwyczaj mają Kształt topologiczny.

Kształty topologiczne, jak również ich metody, i są ostatecznie definiowane przez kernel *(OCCT)* w technologii _.

Innym typem klasy jest [siatka](Mesh/pl.md). Klasa ta nie jest zbyt parametryczna, ponieważ nie można jej łatwo przedefiniować, chyba że poprzez określenie poszczególnych wierzchołków i trójkątnych powierzchni.

![](images/Shape_and_mesh.svg )



*Po lewej: _, zdefiniowana przez wierzchołki i powierzchnie trójkątne.*

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami programu. Klasa `Part::TopoShape* jest osadzona w obiekcie {{incode|Part::Feature` i stamtąd jest propagowana do wszystkich obiektów, które są od niej pochodne.}}

## Użycie

Część: Kształt topologiczny jest obiektem, który jest przypisany do niektórych [App: Obiektów dokumentu](App_DocumentObject/pl.md).

W szczególności podstawowym obiektem, który obsługuje tego typu atrybuty jest [Część: Cecha](Part_Feature/pl.md) *(klasa `Part::Feature`)*. Wszystkie obiekty wywodzące się z tej klasy będą miały dostęp do Kształtu topologicznego.

Niektóre z najważniejszych obiektów Kształtu topologicznego środowiska Część są następujące:

-   Dowolna bryła pierwotna utworzona za pomocą środowiska pracy [Część](Part_Workbench/pl.md).
-   Każda [Zawartość](PartDesign_Body/pl.md) i [Cecha środowiska Projekt Części](PartDesign_Feature/pl.md) utworzona za pomocą środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md).
-   Każdy obiekt wywodzący się z [Część: Part2DObject](Part_Part2DObject/pl.md), jak większość obiektów utworzonych za pomocą środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md).
-   Każdy [szkic](Sketch/pl.md), czyli obiekt środowiska Szkicownik [SketchObject](Sketcher_SketchObject/pl.md), utworzony za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).
-   Dowolny obiekt utworzony przez import plików w formacie STEP, BREP i podobnych formatach bryłowych.

## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Wszystkie obiekty pochodzące z `Part::Feature` będą miały [Kształt topologiczny środowiska Część](Part_TopoShape.md), który jest normalnie dostępny z atrybutu `Kształt`. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Box", "Box")
print(obj.Shape)
```

Kształt topologiczny posiada wiele atrybutów *(zmiennych)* i metod, które zawierają informacje o nim i które pozwalają na wykonywanie na nim operacji. Te zmienne i metody mogą być testowane w [konsoli Python](Python_console/pl.md). 
```python
print(obj.Shape.Area)
print(obj.Shape.BoundBox)
print(obj.Shape.CenterOfMass)
print(obj.Shape.ShapeType)

obj.Shape.check()
obj.Shape.copy()
obj.Shape.exportStep("my_file.step")
obj.Shape.exportStl("my_file.stl")
```

Pełna lista atrybutów i metod znajduje się w <img src=images/Std_PythonHelp.svg style="width:dokumentacji źródłowej](Source_documentation/pl.md) oraz w dokumentacji **[16px"> [Std: Pomoc do środowiska Python](Std_PythonHelp/pl.md)**.

Możesz uzyskać szybkie podsumowanie wszystkich metod, używając wbudowanej w środowisko Python funkcji `help()`. 
```python
help(obj.Shape)
```


 {{Document objects navi}}

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part TopoShape/pl
