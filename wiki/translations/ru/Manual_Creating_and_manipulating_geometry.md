# Manual:Creating and manipulating geometry/ru
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

В предыдущих главах мы узнали о различных верстаках FreeCAD, и как каждый из них реализует свои собственные инструменты и типы геометрии. То же самое касается работы из кода Python.


</div>


<div class="mw-translate-fuzzy">

Мы так же видели, что большинство верстаков FreeCAD зависит от находящегося в фундаменте [верстака Part](Part_Workbench/ru.md). Фактически, некоторые другие верстаки, [Draft](Draft_Workbench/ru.md) или [Arch](Arch_Workbench/ru.md), делают то, что мы делаем в этой главе: используют код Python для создания и манипуляции геометрией Part.


</div>


<div class="mw-translate-fuzzy">

Поэтому первая вещь, которую надо сделать для работы с геометрией Part, это импортирование модуля Part как эквивалент перехода к верстаку Part в Python:


</div>


```python
import Part 
```

Take a moment to explore the Part module by typing **Part.** in the Python console and browsing through the available methods and attributes in the autocomplete window. This is a great way to familiarize yourself with the functionality the module offers. You\'ll find a variety of convenient functions, such as makeBox and makeCircle, which allow you to quickly create geometric shapes and objects with just a single command. Many of these functions also offer optional parameters, giving you precise control over dimensions and placement.


<div class="mw-translate-fuzzy">

Уделите минутку для исследования содержимого модуля Part, напечатав Part. и просмотрев доступные методы. Модуль Part предлагает некоторые общие функции, такие как makeBox, makeCircle, и так далее, которые мгновенно создают объекты для Вас. Попробуйте это, например:


</div>


```python
Part.makeBox(3,5,7) 
```


<div class="mw-translate-fuzzy">

Когда вы после ввода строки выше нажмёте Enter, в окне трёхмерного вида ничего не появится, но в консоли Python будет напечатано нечто вроде этого:


</div>


```python
<Solid object at 0x5f43600> 
```


<div class="mw-translate-fuzzy">

Здесь вступает в силу важная концепция. Мы создали форму Part. Это не объект документа FreeCAD (пока). Объекты и их геометрия в FreeCAD независимы. Считайте объект документа FreeCAD контейнером, который содержит форму. Параметрические объекты так же имеют параметры вроде Length и Width, и **пересчитывают** их форму на лету, когда один из параметров изменяется. Что мы сделали здесь - это вычислили форму вручную.


</div>


<div class="mw-translate-fuzzy">

Теперь мы можем просто сделать \"общий\" объект документа в текущем документе (убедитесь что у Вас открыт хотя бы один новый объект), и дать ему форму куба вроде того, что мы только что сделали:


</div>

In this case, we manually created a shape using the **Part.makeBox()** function. This shape is a non-parametric object, meaning it won't update automatically based on any properties---it is static unless we manipulate it programmatically. To make this shape part of the active FreeCAD document, it would need to be assigned to a document object (like a **Part::Feature**), which would link it to the graphical interface and make it visible and manageable within the FreeCAD environment.


<div class="mw-translate-fuzzy">

Обратите внимание на то, как мы обрабатывали myObj.Shape , мы сделали это в точности как в предыдущей главе мы меняли другие параметры объекта, такие как box.Height = 5 . Фактически, **Shape** это так же параметр, подобно **Height**. Но его тип Part Shape, а не число. В следующей главе мы рассмотрим глубже конструкцию этих параметрических объектов.


</div>

We can now easily create a \"generic\" document object in the current document (make sure you have at least one new document open), and give it a box shape like the one we just made:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Here is a breakdown of the previous commands:

-   **boxShape = Part.makeBox(3,5,7)**: Creates a 3D box with dimensions 3x5x7 (length, width, and height) and stores it as a Part Shape in the variable boxShape. This shape exists only in memory and is not yet part of the FreeCAD document.

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::Feature\", \"MyNewBox\")**: Adds a new Part::Feature object named \"MyNewBox\" to the active FreeCAD document and assigns it to the variable myObj. The new object will appear in the FreeCAD document tree.

-   **myObj.Shape = boxShape**: Links the boxShape geometry to the Shape property of myObj, integrating the geometry into the FreeCAD document.

-   **FreeCAD.ActiveDocument.recompute()**: Updates the document to reflect the changes, ensuring that the new object and its geometry appear in the graphical interface.

Note how we handled **myObj.Shape**. It was done in the same way as in the previous chapter, where we changed other properties of an object, such as **box.Height = 5**. In fact, **Shape** is also a property, just like **Height**. However, instead of taking a number, **Shape** requires a Part Shape. In the next chapter, we will take a closer look at how these parametric objects are constructed.


<div class="mw-translate-fuzzy">

Например, найдём площадь каждой грани нашей формы куба:


</div>

-   **Vertexes**: Points in 3D space that define the corners or endpoints of geometry.
-   **Edges**: Straight or curved lines connecting two vertexes.
-   **Wires**: Closed or open loops formed by one or more connected edges.
-   **Faces**: Surfaces enclosed by one or more wires.
-   **Shells**: Groups of connected faces, forming a continuous surface.
-   **Solids**: 3D volumes enclosed by one or more shells.

All of these attributes are represented as lists in Python. Each list can contain any number of elements or be empty, depending on the shape being explored. For example, a box will have eight **Vertexes**, twelve **Edges**, six **Faces**, one **Shell**, and one **Solid**, while a line will only have two **Vertexes** and one **Edge**, with all other attributes being empty. These components are fundamental building blocks of Part geometry and can be accessed and manipulated programmatically. Understanding how they interact provides powerful control over the creation and modification of 3D models. We can access those lists as follows:


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```


<div class="mw-translate-fuzzy">

Или, для каждого ребра, начальную и конечную точку:


</div>


```python
for f in boxShape.Faces:
   print(f.Area)
```

Or, for each edge, its start point and end point:


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```


<div class="mw-translate-fuzzy">

Как Вы видите, если boxShape имеет атрибут \"Vertexes\", каждый Edge в boxShape так же имеет атрибут \"Vertexes\". Как мы можем ожидать, у boxShape будет 8 вершин, когда ребро имеет 2, которые включены в число этих восьми.


</div>

Мы всегда можем проверить, каков тип формы:


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Here is a short explanation of the above commands:

-   **print(boxShape.ShapeType)**: Displays the type of the top-level shape represented by **boxShape**. In this case, since **boxShape** was created as a box using **Part.makeBox**, the output will be \"Solid\", indicating that the shape is a 3D solid object.

-   **print(boxShape.Faces\[0\].ShapeType)**: Accesses the first face in the **Faces** list of **boxShape** (index 0) and prints its shape type. For a box, each face is a flat surface, so the output will be \"Face\".

-   **print(boxShape.Vertexes\[2\].ShapeType)**: Accesses the third vertex in the **Vertexes** list of **boxShape** (index 2) and prints its shape type. Since this is a specific point in 3D space, the output will be \"Vertex\".


<div class="mw-translate-fuzzy">

Так что возобновим тему Part Shape: всё начинается с вершин (Vertice). С одной или двумя вершинами (окружность имеет только одну вершину) формируется ребро (Edge). С несколькими рёбрами формируется ломаная (Wire). С одной или несколькими замкнутыми ломаными формируется грань (Face) (дополнительные ломаные образуют в грани \"отверстия\"). Несколько граней создают оболочку (Shell). Когда оболочка замкнута (водонепроницаемо), из неё можно создать тело (Solid). И в конце можно соединить несколько форм (Shape) различных видов, это называется соединение (Compound).


</div>

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


<div class="mw-translate-fuzzy">

Заметили, что нам не надо создавать Vertices? Мы можем сразу создать Part.LineSegments из FreeCAD Vectors, потому, что у нес ещё не созданы рёбра (Edge). Part.LineSegments (как и Part.Circle, Part.Arc, Part.Ellipse или Part.BSpline) создают не ребро (Edge), а базовую геометрию, на которой будут созданы рёбра. Рёбра всегда делаются из такой базовой геометрии, сохраняемой в её атрибуте Curve. Так что если у Вас есть Edge, команда:


</div>


```python
print(Edge.Curve) 
```


<div class="mw-translate-fuzzy">

покажет Вам, какого типа этот Edge, базируется ли он на линии, дуге или ещё чем\... Но вернёмся к нашему примеру, и свяжем сегменты дуги. Для этого нам нужна третья точка, поэтому мы можем использовать подходящий Part.Arc, у которого 3 точки:


</div>

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


<div class="mw-translate-fuzzy">

Иначе, базовая геометрия так же имеет функцию toShape(), которая делает то же самое:


</div>


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```


<div class="mw-translate-fuzzy">

Когда у нас есть последовательность рёбер, мы можем сформировать ломаную (Wire), придав ей список рёбер (Edge):


</div>


```python
W = Part.Wire([E1,E4,E2,E3]) 
```


<div class="mw-translate-fuzzy">

И мы можем проверить, правильно ли понята наша ломаная (Wire), и корректно ли она замкнута:


</div>


```python
print( W.isClosed() ) 
```


<div class="mw-translate-fuzzy">

Здесь будет напечатано \"True\" или \"False\". Чтобы создать грань (Face), нам нужны замкнутые ломаные (Wire), так что всегда полезно проверить это, прежде чем создать грань. Мы можем создать Face, передав ей единственную полилинию (Wire), или список полилиний, если нам нужны отверстия:


</div>


```python
F = Part.Face(W) 
```

Затем мы выдавим его:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```


<div class="mw-translate-fuzzy">

Зметьте, что P уже твёрдое тело (Solid):


</div>


```python
print(P.ShapeType) 
```

This is because when we extrude a single face, we always get a solid. This wouldn\'t be the case, for example, if we had extruded the wire instead:


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
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



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/ru
