# Manual:Creating and manipulating geometry/ru
 


{{Manual:TOC/ru}}

В предыдущих главах мы узнали о различных верстаках FreeCAD, и как каждый из них реализует свои собственные инструменты и типы геометрии. То же самое касается работы из кода Python.


<div class="mw-translate-fuzzy">

Мы так же видели, что большинство верстаков FreeCAD зависит от находящегося в фундаменте [верстака Part](Part_Workbench/ru.md). Фактически, некоторые другие верстаки, [Draft](Draft_Workbench/ru.md) или [Arch](Arch_Workbench/ru.md), делают то, что мы делаем в этой главе: используют код Python для создания и манипуляции геометрией Part.


</div>

Поэтому первая вещь, которую надо сделать для работы с геометрией Part, это импортирование модуля Part как эквивалент перехода к верстаку Part в Python:


```python
import Part 
```

Уделите минутку для исследования содержимого модуля Part, напечатав Part. и просмотрев доступные методы. Модуль Part предлагает некоторые общие функции, такие как makeBox, makeCircle, и так далее, которые мгновенно создают объекты для Вас. Попробуйте это, например:


```python
Part.makeBox(3,5,7) 
```

Когда вы после ввода строки выше нажмёте Enter, в окне трёхмерного вида ничего не появится, но в консоли Python будет напечатано нечто вроде этого:


```python
<Solid object at 0x5f43600> 
```

Здесь вступает в силу важная концепция. Мы создали форму Part. Это не объект документа FreeCAD (пока). Объекты и их геометрия в FreeCAD независимы. Считайте объект документа FreeCAD контейнером, который содержит форму. Параметрические объекты так же имеют параметры вроде Length и Width, и **пересчитывают** их форму на лету, когда один из параметров изменяется. Что мы сделали здесь - это вычислили форму вручную.

Теперь мы можем просто сделать \"общий\" объект документа в текущем документе (убедитесь что у Вас открыт хотя бы один новый объект), и дать ему форму куба вроде того, что мы только что сделали:


```python
boxShape = Part.makeBox(3,5,7)
 myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
 myObj.Shape = boxShape
 FreeCAD.ActiveDocument.recompute()
```

Обратите внимание на то, как мы обрабатывали myObj.Shape , мы сделали это в точности как в предыдущей главе мы меняли другие параметры объекта, такие как box.Height = 5 . Фактически, **Shape** это так же параметр, подобно **Height**. Но его тип Part Shape, а не число. В следующей главе мы рассмотрим глубже конструкцию этих параметрических объектов.

Теперь изучим наши формы Part детальнее. В конце главы о [традиционном моделировании с помощью верстака Part](Manual:Traditional_modeling,_the_CSG_way/ru.md) мы показали стол, показывающий как конструируются формы Part, и их различные компоненты (вершины, грани, рёбра и так далее). Точно такие же компоненты существуют и могут быть доступны через Python. Формы Part всегда имеют следующие атрибуты: Vertexes, Edges, Wires, Faces, Shells и Solids. Все они списки, содержащие любое число элементов или пустые:


```python
print(boxShape.Vertexes)
 print(boxShape.Edges)
 print(boxShape.Wires)
 print(boxShape.Faces)
 print(boxShape.Shells)
 print(boxShape.Solids)
```

Например, найдём площадь каждой грани нашей формы куба:


```python
for f in boxShape.Faces:
   print(f.Area)
```

Или, для каждого ребра, начальную и конечную точку:


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```

Как Вы видите, если boxShape имеет атрибут \"Vertexes\", каждый Edge в boxShape так же имеет атрибут \"Vertexes\". Как мы можем ожидать, у boxShape будет 8 вершин, когда ребро имеет 2, которые включены в число этих восьми.

Мы всегда можем проверить, каков тип формы:


```python
print(boxShape.ShapeType)
 print(boxShape.Faces[0].ShapeType)
 print(boxShape.Vertexes[2].ShapeType)
```

Так что возобновим тему Part Shape: всё начинается с вершин (Vertice). С одной или двумя вершинами (окружность имеет только одну вершину) формируется ребро (Edge). С несколькими рёбрами формируется ломаная (Wire). С одной или несколькими замкнутыми ломаными формируется грань (Face) (дополнительные ломаные образуют в грани \"отверстия\"). Несколько граней создают оболочку (Shell). Когда оболочка замкнута (водонепроницаемо), из неё можно создать тело (Solid). И в конце можно соединить несколько форм (Shape) различных видов, это называется соединение (Compound).

Теперь мы попробуем создать сложные формы с нуля, конструируя все их компоненты один за другим. Например, попробуем создать объём вроде этого:

![](images/Exercise_python_03.jpg )

Начнём с создания плоской формы вроде этой:

![](images/Wire.png )

Сначала создадим четыре базовые точки:


```python
V1 = FreeCAD.Vector(0,10,0)
 V2 = FreeCAD.Vector(30,10,0)
 V3 = FreeCAD.Vector(30,-10,0)
 V4 = FreeCAD.Vector(0,-10,0)
```

Затем создадим два линейных сегмента

![](images/Line.png )


```python
L1 = Part.LineSegment(V1,V2)
L2 = Part.LineSegment(V4,V3)
```

Заметили, что нам не надо создавать Vertices? Мы можем сразу создать Part.LineSegments из FreeCAD Vectors, потому, что у нес ещё не созданы рёбра (Edge). Part.LineSegments (как и Part.Circle, Part.Arc, Part.Ellipse или Part.BSpline) создают не ребро (Edge), а базовую геометрию, на которой будут созданы рёбра. Рёбра всегда делаются из такой базовой геометрии, сохраняемой в её атрибуте Curve. Так что если у Вас есть Edge, команда:


```python
print(Edge.Curve) 
```

покажет Вам, какого типа этот Edge, базируется ли он на линии, дуге или ещё чем\... Но вернёмся к нашему примеру, и свяжем сегменты дуги. Для этого нам нужна третья точка, поэтому мы можем использовать подходящий Part.Arc, у которого 3 точки:

![](images/Circel.png )


```python
VC1 = FreeCAD.Vector(-10,0,0)
 C1 = Part.Arc(V1,VC1,V4)
 VC2 = FreeCAD.Vector(40,0,0)
 C2 = Part.Arc(V2,VC2,V3)
```

Теперь у нас 2 линии (L1 и L2) и 2 дуги (C1 и C2). Их надо превратить в ребро (Edge):


```python
E1 = Part.Edge(L1)
 E2 = Part.Edge(L2)
 E3 = Part.Edge(C1)
 E4 = Part.Edge(C2)
```

Иначе, базовая геометрия так же имеет функцию toShape(), которая делает то же самое:


```python
E1 = L1.toShape()
 E2 = L2.toShape()
 ...
```

Когда у нас есть последовательность рёбер, мы можем сформировать ломаную (Wire), придав ей список рёбер (Edge):


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

И мы можем проверить, правильно ли понята наша ломаная (Wire), и корректно ли она замкнута:


```python
print( W.isClosed() ) 
```

Здесь будет напечатано \"True\" или \"False\". Чтобы создать грань (Face), нам нужны замкнутые ломаные (Wire), так что всегда полезно проверить это, прежде чем создать грань. Мы можем создать Face, передав ей единственную полилинию (Wire), или список полилиний, если нам нужны отверстия:


```python
F = Part.Face(W) 
```

Затем мы выдавим его:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Зметьте, что P уже твёрдое тело (Solid):


```python
print(P.ShapeType) 
```

This is because when we extrude a single Face, we always get a Solid. This wouldn\'t be the case, for example, if we had extruded the Wire instead:


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
 print(s.ShapeType)
```

Это, разумеется, даст нам полую оболочку, без верхней и нижней плоскости.

Теперь, когда у нас есть окончательная форма, мы с нетерпением желаем увидеть её на экране! Так что создадим общий объект, и назначим наше новое тело (Solid) к нему:


```python
myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","My_Strange_Solid")
 myObj2.Shape = P
 FreeCAD.ActiveDocument.recompute()
```

Альтернативно модуль Part предлагает ярлык, делающий эту операцию быстрее (но Вы не сможете выбрать имя объекта):


```python
Part.show(P) 
```

Всё это, и многое другое, вместе с примерами детально описано на странице [Part Scripting](Topological_data_scripting/ru.md).

**Читать далее**:

-   [Верстак Part](Part_Workbench/ru.md)
-   [Написание скриптов обработки топологии](Topological_data_scripting/ru.md)





{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
