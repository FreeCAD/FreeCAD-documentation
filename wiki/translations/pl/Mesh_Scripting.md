# Mesh Scripting/pl




{{TOCright}}

## Wprowadzenie

Aby uzyskać dostęp do modułu `Mesh` musisz go najpierw zaimportować:


```python
import Mesh
```

## Tworzenie

Aby utworzyć pusty obiekt siatki wystarczy użyć standardowego konstruktora:


```python
mesh = Mesh.Mesh()
```

Możesz również utworzyć obiekt na podstawie pliku:


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

Lub stwórz go z zestawu trójkątów opisanych przez ich punkty narożne:


```python
triangles = [
# triangle 1
[-0.5000, -0.5000, 0.0000], [0.5000, 0.5000, 0.0000], [-0.5000, 0.5000, 0.0000],
#triangle 2
[-0.5000, -0.5000, 0.0000], [0.5000, -0.5000, 0.0000], [0.5000, 0.5000, 0.0000],
]
meshObject = Mesh.Mesh(triangles)
Mesh.show(meshObject)
```

Jądro Mesh zapewnia utworzenie topologicznie poprawnej struktury danych, poprzez sortowanie zbieżnych punktów i krawędzi. {{Top}}

## Modelowanie

Do tworzenia regularnych geometrii można użyć jednej z metod `create*()`. Torus, na przykład, może być utworzony w następujący sposób:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```

Pierwsze dwa parametry określają promienie torusa, a trzeci parametr jest współczynnikiem podpróbkowania dla liczby utworzonych trójkątów. Im wyższa jest ta wartość, tym gładsza jest siatka.

Moduł `Mesh` dostarcza również trzy logiczne metody do modelowania: `union()`, `intersection()` i `difference()`:


```python
m1, m2              # are the input mesh objects
m3 = Mesh.Mesh(m1)  # create a copy of m1
m3.unite(m2)        # union of m1 and m2, the result is stored in m3
m4 = Mesh.Mesh(m1)
m4.intersect(m2)    # intersection of m1 and m2
m5 = Mesh.Mesh(m1)
m5.difference(m2)   # the difference of m1 and m2
m6 = Mesh.Mesh(m2)
m6.difference(m1)   # the difference of m2 and m1, usually the result is different to m5
```

Oto przykład, który tworzy rurę za pomocą metody `difference()`:


```python
import FreeCAD, Mesh
cylA = Mesh.createCylinder(2.0, 10.0, True, 1.0, 36)
cylB = Mesh.createCylinder(1.0, 12.0, True, 1.0, 36)
cylB.Placement.Base = (FreeCAD.Vector(-1, 0, 0)) # move cylB to avoid co-planar faces
pipe = cylA
pipe = pipe.difference(cylB)
pipe.flipNormals() # somehow required
doc = FreeCAD.ActiveDocument
obj = d.addObject("Mesh::Feature", "Pipe")
obj.Mesh = pipe
doc.recompute()
```


{{Top}}

## Uwagi

Rozległym *(choć trudnym w użyciu)* źródłem skryptów związanych z siatkami są skrypty do testów jednostkowych Środowiska pracy `Mesh`. Podczas tych testów jednostkowych wywoływane są dosłownie wszystkie metody i wszystkie właściwości/atrybuty są udoskonalane. Więc jeśli jesteś wystarczająco odważny, spójrz na [Moduł testowy jednostek](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

Zobacz również: [API dla Mesh](Mesh_API.md) {{Top}} {{Powerdocnavi}} {{Mesh Tools navi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
