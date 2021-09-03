


{{TOCright}}

## Введение

Чтобы получить доступ к модулю `Mesh`, вы должны сначала импортировать его:


```python
import Mesh
```

## Создание

Чтобы создать пустой объект сетки, просто используйте стандартный конструктор:


```python
mesh = Mesh.Mesh()
```

Вы также можете создать объект из файла:


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

Или создайте его из множества треугольников, задав их вершины:


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

Ядро Mesh заботится о создании топологического правильной структуры данных, сортируя совпадающие точки и края.

[наверх](#top.md)

## Моделирование

Для создания правильной геометрии вы можете использовать один из методов `create*()`. Например, тор можно создать следующим образом:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```

Первые два параметра определяют радиусы тороида, а третий параметр - фактор подвыборки, как много треугольников будет создано. Чем выше это значение, тем сглаженней тело.

Модуль `Mesh` также предоставляет три булевых метода: `union()`, `intersection()` и `difference()`:


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

Вот пример, который создает трубку, используя метод `difference()`:


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

[наверх](#top.md)

## Примечания

Широко применяемый, хотя и трудный в использовании, источник скриптов обработки полигональных сеток - это тестовые скрипты в модуле `Mesh`. В этих тестах модуля буквально все методы вызываются и все свойства/атрибуты перебираются. Так что если вы достаточно смелы, взгляните на [Unit Test module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).

Смотрите так же: [Mesh API](Mesh_API/ru.md).

[наверх](#top.md)


{{Powerdocnavi

}} {{Mesh Tools navi}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
