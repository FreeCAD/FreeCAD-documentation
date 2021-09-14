# Mesh to Part/ru




{{TOCright}}

## Преобразование объектов Part в полигональную сетку 


<div class="mw-translate-fuzzy">

Конвертация высокоуровневых объектов, таких как формы [Part(Деталей)](Part_Workbench/ru.md), в простые объекты, такие как [полигональные сетки](Mesh_Workbench/ru.md), это довольно прямолинейная операция, когда все грани Part разбиваются на треугольники. Результат этой триангуляции затем используется для построения сетки:


</div>


```python
import Mesh

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape
faces = []

triangles = shp.tessellate(1) # the number represents the precision of the tessellation
for tri in triangles[1]:
    face = []
    for i in tri:
        face.append(triangles[0][i])
    faces.append(face)

m = Mesh.Mesh(faces)
Mesh.show(m)
```

Альтернативный пример:


```python
import Mesh
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Part object must be preselected
shp = obj.Shape

mesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh.Mesh = MeshPart.meshFromShape(
        Shape=shp,
        LinearDeflection=0.01,
        AngularDeflection=0.025,
        Relative=False)
```

## Преобразование полигональных сеток в объекты Part 

Преобразование полигональных сеток в Part - самая обычная операция. Очень часто вы получаете трёхмерные данные в полигональном виде. Сетки довольно практичны для представления геометрии свободной формы и больших визуальных сцен, поскольку они очень легковесны. Но в FreeCAD мы в основном предпочитаем высокоуровневые объекты, твердотельные, которые несут гораздо больше информации, и позволяют кривые поверхности.

Преобразование сетки в высокоуровневый объект (обрабатываемый в FreeCAD [верстаком Деталь](Part_Workbench/ru.md)) это не простая задача. Сетки могут содержать тысячи треугольников (например, когда они сгенерированы 3D сканером), и телом, состоящим из того же числа граней, будет чрезвычайно сложно управлять. Поэтому обычно хочется оптимизировать объект при преобразовании.

В настоящее время FreeCAD предлагает два метода для преобразования полигональных сеток в объект Part. Первый метод прост, это прямое преобразование, без какой либо оптимизации:


```python
import Mesh
import Part

mesh = Mesh.createTorus()
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
solid = Part.makeSolid(shape)
Part.show(solid)
```

Второй метод позволяет учитывать какие грани сетки компланарны, когда угол между ними принимает определенное значение, уменьшая количество граней в конечном результате:


```python
import Mesh
import Part
import MeshPart

obj = FreeCADGui.Selection.getSelection()[0] # a Mesh object must be preselected
mesh = obj.Mesh
segments = mesh.getPlanarSegments(0.00001) # use rather strict tolerance here
faces = []

for i in segments:
    if len(i) > 0:
        # a segment can have inner holes
        wires = MeshPart.wireFromSegment(mesh, i)
        # we assume that the exterior boundary is that one with the biggest bounding box
        if len(wires) > 0:
            ext = None
            max_length=0
            for i in wires:
                if i.BoundBox.DiagonalLength > max_length:
                    max_length = i.BoundBox.DiagonalLength
                    ext = i

            wires.remove(ext)
            # all interior wires mark a hole and must reverse their orientation, otherwise Part.Face fails
            for i in wires:
                i.reverse()

            # make sure that the exterior wires comes as first in the list
            wires.insert(0, ext)
            faces.append(Part.Face(wires))

solid = Part.Solid(Part.Shell(faces))
Part.show(solid)
```


{{Powerdocnavi

}} {{Mesh Tools navi}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
