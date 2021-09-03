


{{TOCright}}


<div class="mw-translate-fuzzy">

## 概述

我们将在本文中向您解释如何直接用FreeCAD的Python解释器来控制[零件模块](Part_Workbench.md)，或者从任意外部脚本来实现这一点。关于拓扑数据脚本的基本描述位于[零件模块的概念介绍](Part_Workbench#Scripting.md)。如果您需要了解关于FreeCAD中python脚本工作原理的更多信息，请一定阅读[脚本一节与](Scripting.md)[FreeCAD脚本基础页面](FreeCAD_Scripting_Basics.md)。


</div>

Here we will explain to you how to control the [Part](Part_Workbench.md) module directly from the FreeCAD Python interpreter, or from any external script. Be sure to browse the [Scripting](Scripting.md) section and the [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) pages if you need more information about how Python scripting works in FreeCAD. If you are new to Python, it is a good idea to first read the [Introduction to Python](Introduction_to_Python.md).

### See also 

-   [Part scripting](Part_scripting.md)
-   [OpenCASCADE](OpenCASCADE.md)


<div class="mw-translate-fuzzy">

### 类图

这是零件模块中最关键类的 [统一建模语言（Unified Modeling Language (UML)）](http://en.wikipedia.org/wiki/Unified_Modeling_Language)概述： ![零件模块中的Python类](images/Part_Classes.jpg )


</div>

This is a [Unified Modeling Language (UML)](http://en.wikipedia.org/wiki/Unified_Modeling_Language) overview of the most important classes of the Part module: ![Python classes of the Part module](images/Part_Classes.jpg ) {{Top}}


<div class="mw-translate-fuzzy">

### 几何图形

这些几何图形对象是一切拓扑对象的基石：

-   **Geom** 几何图形对象的基类
-   **Line** 3D空间中的直线段，由起始点与终点定义而成
-   **Circle** 由中心点、起始点与终点定义的圆形或部分圆环段（circle segment）
-   **\...\...** 以及后续更多的几何图形


</div>

The geometric objects are the building blocks of all topological objects:

-   **Geom** Base class of the geometric objects.
-   **Line** A straight line in 3D, defined by starting point and end point.
-   **Circle** Circle or circle segment defined by a center point and start and end point.
-   Etc.


{{Top}}


<div class="mw-translate-fuzzy">

### 拓扑

FreeCAD中有下列可用的拓扑数据类型：

-   **复合（Compound）对象** 一组任意类型的拓扑对象。
-   **组合实体（Compsolid）** 一个复合实体是一组由其面连接起来的实体。它会将连线（WIRE）与壳（SHELL）扩展为实体。
-   **实体（Solid）** 由壳界定的部分空间。实体是3D对象。
-   **壳（Shell）** 一组由其边连接起来的面。一个壳可以是开放或闭合的。
-   **面（Face）** 在2D空间中，它是部分平面；而在3D空间中，它是部分表面。面的几何图形由轮廓来约束（调整）。面是2D对象。
-   **连线（Wire）** 一组由其顶点连接起来的边。连线可以是开放或闭合的轮廓，这取决于其中的边是否互连。
-   **边（Edge）** 一种对应于约束曲线的拓扑元素。一条边通常受其顶点限制。边是一种1D对象。
-   **顶点（Vertex）** 一种对应于点的拓扑元素。顶点是零维对象。
-   **几何形状（Shape）** 一种涵盖上述所有对象的通称。


</div>

The following topological data types are available:

-   **Compound** A group of any type of topological objects.
-   **Compsolid** A composite solid is a set of solids connected by their faces. It expands the notions of WIRE and SHELL to solids.
-   **Solid** A part of space limited by shells. It is three dimensional.
-   **Shell** A set of faces connected by their edges. A shell can be open or closed.
-   **Face** In 2D it is part of a plane; in 3D it is part of a surface. Its geometry is constrained (trimmed) by contours. It is two dimensional.
-   **Wire** A set of edges connected by their vertices. It can be an open or closed contour depending on whether the edges are linked or not.
-   **Edge** A topological element corresponding to a restrained curve. An edge is generally limited by vertices. It has one dimension.
-   **Vertex** A topological element corresponding to a point. It has zero dimension.
-   **Shape** A generic term covering all of the above.


{{Top}}


<div class="mw-translate-fuzzy">

### 简易示例 ：创建简单拓扑结构 


</div>

![连线](images/Wire.png )


<div class="mw-translate-fuzzy">

现在，我们将通过构造简单的几何图形来创建对应的拓扑。就用我们在图中看到的零件为例，它由4个顶点，2个半圆以及2条线段构成。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建几何图形

首先，我们必须创建此连线中的不同几何图形部分。 而且，还要小心处理几何图形中位于**相同**位置的不同顶点。否则，我们随后可能无法将这些几何图形连接为一个拓扑结构。


</div>

First we create the distinct geometric parts of this wire. Making sure that parts that have to be connected later share the same vertices.


<div class="mw-translate-fuzzy">

因此，我们先来创建其中的点：


</div>


```python
import Part
from FreeCAD import Base
V1 = Base.Vector(0, 10, 0)
V2 = Base.Vector(30, 10, 0)
V3 = Base.Vector(30, -10, 0)
V4 = Base.Vector(0, -10, 0)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 弧


</div>

![半圆](images/Circel.png )


<div class="mw-translate-fuzzy">

为了创建圆周上的弧，我们要做一个辅助点，并通过圆周上的3个点来创建对应的弧：


</div>


```python
VC1 = Base.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = Base.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 线段


</div>

![线段](images/Line.png )


<div class="mw-translate-fuzzy">

众所周知，两点定一线段：


</div>


```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 合而为一

最后一步就是将上述基本几何元素放在一起，并烘焙出一个拓扑形状：


</div>

The last step is to put the geometric base elements together and bake a topological shape:


```python
S1 = Part.Shape([C1, L1, C2, L2])
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 制作一个外框

现在令连线在同一方向上挤压成型，构造一个实际的3D图形：


</div>

Now extrude the wire in a direction and make an actual 3D shape:


```python
W = Part.Wire(S1.Edges)
P = W.extrude(Base.Vector(0, 0, 10))
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 将结果呈现出来


</div>


```python
Part.show(P)
```


{{Top}}


<div class="mw-translate-fuzzy">

## 创建基本的几何形状

您可以利用零件模块中的\"make\...()\"方法来轻松地创建一个基础的拓扑对象。


</div>

You can easily create basic topological objects with the `make...()` methods from the Part module:


```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```


<div class="mw-translate-fuzzy">

其他可用的make\...()方法：

-   **makeBox(l,w,h)**: 在点p（？）处创建一个维数为(l,w,h)且指向方向d（？）的立方体
-   **makeCircle(radius)**: 以指定的半径创建一个圆形
-   **makeCone(radius1,radius2,height)**: 以指定的两个半径与高度创建一个圆锥体（圆台）
-   **makeCylinder(radius,height)**: 以指定的半径与高度创建一个圆柱体
-   **makeLine((x1,y1,z1),(x2,y2,z2))**: 根据两点创建一条线段
-   **makePlane(length,width)**: 利用指定的长度与宽度创建一个平面
-   **makePolygon(list)**: 根据指定的点集创建一个多边形
-   **makeSphere(radius)**: 利用指定的半径创建一个球体
-   **makeTorus(radius1,radius2)**: 利用指定的两个半径创建一个圆环体

请参考[Part API页来查阅零件模块中的完整可用方法列表](Part_API.md)。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 导入所需的模块

首先，我们需要导入零件（Part）模块，继而通过python使用其中提供的内容。 另外，我们也将从FreeCAD模块中导入基础（Base）模块：


</div>

First we need to import the Part module so we can use its contents in Python. We\'ll also import the Base module from inside the FreeCAD module:


```python
import Part
from FreeCAD import Base
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个向量

在构建几何图形的过程中， [向量](http://en.wikipedia.org/wiki/Euclidean_vector) 是提供最关键信息的对象类型之一。向量属性中通常都有3个数字（但并非总是如此）：即直角坐标系中的3种坐标分量：x、y、z。您可以按下列方式来创建一个向量：


</div>

[Vectors](http://en.wikipedia.org/wiki/Euclidean_vector) are one of the most important pieces of information when building shapes. They usually contain three numbers (but not necessarily always): the X, Y and Z cartesian coordinates. You create a vector like this:


```python
myVector = Base.Vector(3, 2, 0)
```


<div class="mw-translate-fuzzy">

我们刚刚在x=3, y=2, z=0坐标处创建了一个向量。在零件模块中，到处都能看到向量的身影。构建零件形状的过程中，也会用到另一种名为顶点的点表示法，它是一种向量的简易容器。您可像下面那样来访问一个点的向量：


</div>


```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一条边

一条边不过是具有两个顶点的线段：


</div>

An edge is nothing but a line with two vertices:


```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

请注意，您也可以通过输入两个向量来创建一条边：


```python
vec1 = Base.Vector(0, 0, 0)
vec2 = Base.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

您能通过下列方式来查看一条边的长度与中点：


```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 将图形显示在屏幕上

到目前为止，我们已经创建了一个边对象，但是它却并没有出现在屏幕上。 这是因为：只有在您告诉FreeCAD要呈现什么内容之后，它才会显示出对应的3D场景。为此，我们要通过下列简单函数来实现这一点：


</div>

So far we created an edge object, but it doesn\'t appear anywhere on the screen. This is because the FreeCAD 3D scene only displays what you tell it to display. To do that, we use this simple method:


```python
Part.show(edge)
```


<div class="mw-translate-fuzzy">

此show函数在我们当前的FreeCAD文档中创建了一个对象，并为之赋予此前创建的\"edge\"几何形状。每当需要在屏幕上显示您所创建的对象们时，使用此函数即可。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个连线

一条连线（wire）由多条边构成。创建连线需要指定一个边列表，或者甚至是一个连线列表：


</div>

A wire is a multi-edge line and can be created from a list of edges or even a list of wires:


```python
edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
wire1 = Part.Wire([edge1, edge2]) 
edge3 = Part.makeLine((10, 10, 0), (0, 10, 0))
edge4 = Part.makeLine((0, 10, 0), (0, 0, 0))
wire2 = Part.Wire([edge3, edge4])
wire3 = Part.Wire([wire1, wire2])
wire3.Edges
> [<Edge object at 016695F8>, <Edge object at 0197AED8>, <Edge object at 01828B20>, <Edge object at 0190A788>]
Part.show(wire3)
```


<div class="mw-translate-fuzzy">

Part.show(wire3)命令将显示构成我们所创连线的4条边。而其他有用的信息可通过下列方式方便地检索：


</div>


```python
wire3.Length
> 40.0
wire3.CenterOfMass
> Vector (5, 5, 0)
wire3.isClosed()
> True
wire2.isClosed()
> False
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个面

只有根据闭合连线创建的面才是有效的。在本示例中，wire3是一个闭合的连线，而wire2却不是一个闭合的连线（参见此前的代码）


</div>

Only faces created from closed wires will be valid. In this example, wire3 is a closed wire but wire2 is not (see above):


```python
face = Part.Face(wire3)
face.Area
> 99.99999999999999
face.CenterOfMass
> Vector (5, 5, 0)
face.Length
> 40.0
face.isValid()
> True
sface = Part.Face(wire2)
sface.isValid()
> False
```


<div class="mw-translate-fuzzy">

只有面才具有自己的面积，而连线与边却没有。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个圆形

我们可以按下列方式简单地创建一个圆形：


</div>

A circle can be created like this:


```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
```

如果您想以特定的位置与方向来创建它，则可：


```python
ccircle = Part.makeCircle(10, Base.Vector(10, 0, 0), Base.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
```


<div class="mw-translate-fuzzy">

所创的圆形ccircle将位于x轴上距原点10个单位处，并沿轴方向面向外侧。请注意：makeCircle仅接收Base.Vector()作为其位置以及方向参数，而非元组（tuples）。您也可以通过指定起始角度与结束角度来创建部分圆：


</div>


```python
from math import pi
arc1 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 180, 360)
```


<div class="mw-translate-fuzzy">

arc1与arc2拼接起来即是一个圆。角度参数使用的是角度制；如果您采用的是弧度制，可简单的通过下列公式进行转换：角度 = 弧度 \* 180/PI，或借助python的数学模块（当然啦，要在导入数学模块后才能使用）：


</div>


```python
import math
degrees = math.degrees(radians)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 沿多个点创建一条弧

可惜的是，FreeCAD并没有提供makeArc函数，但是我们有Part.Arc函数可通过3个点来创建一条弧。它经过起始点、中点以及两者间的一个中间点来创建一个弧对象。另外，必须调用弧对象的.toShape()函数来得到一个边对象，与Arc用法相同的是Part.LineSegment而非Part.makeLine。


</div>

Unfortunately there is no `makeArc()` function, but we have the `Part.Arc()` function to create an arc through three points. It creates an arc object joining the start point to the end point through the middle point. The arc object\'s `toShape()` function must be called to get an edge object, the same as when using `Part.LineSegment` instead of `Part.makeLine`.


```python
arc = Part.Arc(Base.Vector(0, 0, 0), Base.Vector(0, 5, 0), Base.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```


<div class="mw-translate-fuzzy">

Arc函数仅接受Base.Vector()作为绘弧所用的点，而非元组（tuples）。arc\_edge就是我们要借助Part.show(arc\_edge)语句所显示的边。您也通过截取部分圆来获得一条弧：


</div>


```python
from math import pi
circle = Part.Circle(Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```

弧都是像线条那样的有效边，因此也可将其用作连线。 {{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个多边形

多边形是利用多条直边连接而成的简易连线。 makePolygon函数将获取一个点列表，并通过其中的多个点来创建一条连线：


</div>

A polygon is simply a wire with multiple straight edges. The `makePolygon()` function takes a list of points and creates a wire through those points:


```python
lshape_wire = Part.makePolygon([Base.Vector(0, 5, 0), Base.Vector(0, 0, 0), Base.Vector(5, 0, 0)])
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一条贝塞尔曲线

贝塞尔曲线常用于模拟平滑的曲线，绘制贝塞尔曲线要借助一系列极点（poles）以及权值。下列函数根据一组FreeCAD.Vector点来创建一条Part.BezierCurve。(请注意：当"获取"或"设置"单个极点或权值时，起始索引为1而非0。)


</div>

Bézier curves are used to model smooth curves using a series of poles (points) and optional weights. The function below makes a `Part.BezierCurve()` from a series of `FreeCAD.Vector()` points. Note: when \"getting\" and \"setting\" a single pole or weight, indices start at 1, not 0.


```python
def makeBCurveEdge(Points):
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个平面

平面就是一个简单的矩形平面。**makePlane(length,width,\[start\_pnt,dir\_normal\])**方法可用于创建一个平面。默认值为 start\_pnt = Vector(0,0,0)与dir\_normal = Vector(0,0,1)。通过dir\_normal = Vector(0,0,1)将创建一个面向z轴正方向的平面，而dir\_normal = Vector(1,0,0)将创建一个面向x轴正方向的平面：


</div>

A Plane is a flat rectangular surface. The method used to create one is `makePlane(length, width, [start_pnt, dir_normal])`. By default start\_pnt = Vector(0, 0, 0) and dir\_normal = Vector(0, 0, 1). Using dir\_normal = Vector(0, 0, 1) will create the plane facing in the positive Z axis direction, while dir\_normal = Vector(1, 0, 0) will create the plane facing in the positive X axis direction:


```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, Base.Vector(3, 0, 0), Base.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```


<div class="mw-translate-fuzzy">

其中的包围盒BoundBox是一个包围目标平面的长方体，它有一条自(3,0,0)始至(5,0,2)终的对角线。可以看出，BoundBox的厚度在y轴上为0，这是因为被包围的对象是一个平面。


</div>


<div class="mw-translate-fuzzy">

请注意，makePlane仅接收Base.Vector()作为其start\_pnt与dir\_normal参数，而非元组（tuples）。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个椭圆

有多种方法可以创建椭圆：


</div>

There are several ways to create an ellipse:


```python
Part.Ellipse()
```


<div class="mw-translate-fuzzy">

创建一个长半轴为2、短半轴为1，且中点位于(0,0,0)处的椭圆。


</div>


```python
Part.Ellipse(Ellipse)
```

创建一个指定椭圆的副本。


```python
Part.Ellipse(S1, S2, Center)
```


<div class="mw-translate-fuzzy">

创建一个以点Center为中心的椭圆，所在平面由Center、S1与S2定义，长轴由Center与S1定义，长半轴为Center与S1间的距离，而短半轴则是S2与长轴间的距离。


</div>


```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```


<div class="mw-translate-fuzzy">

以长半轴MajorRadius与短半轴MinorRadius创建一个椭圆，其所在平面由Center与法线(0,0,1)定义。


</div>


```python
eli = Part.Ellipse(Base.Vector(10, 0, 0), Base.Vector(0, 5, 0), Base.Vector(0, 0, 0))
Part.show(eli.toShape())
```


<div class="mw-translate-fuzzy">

在上面的代码中，我们分别传入了S1、S2与中心位置。与Arc函数类似，Ellipse函数创建了一个椭圆对象而非边，所以我们需要用toShape()将其转换为一条边，以便显示。


</div>


<div class="mw-translate-fuzzy">

请注意：Arc仅接收Base.Vector()作为其输入点，而非元组。


</div>


```python
eli = Part.Ellipse(Base.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```


<div class="mw-translate-fuzzy">

针对上述Ellipse函数的构造函数，我们为之传入了中心位置，MajorRadius与MinorRadius。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个环面

利用**makeTorus(radius1,radius2,\[pnt,dir,angle1,angle2,angle\])**来创建环面。 其默认值为：pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=360与angle=360。 可以将环面想象为：一个小圆沿着一个大圆扫过的图形。Radius1为大圆的半径，radius2为小圆的半径，pnt为环面的中心，而dir则为法线方向。angle1与angle2都是针对小圆的以弧度制（？）表示的角度；最后一个参数angle描述的是截取的部分环面：


</div>

Using `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = 0, angle2 = 360 and angle = 360. Consider a torus as small circle sweeping along a big circle. Radius1 is the radius of the big circle, radius2 is the radius of the small circle, pnt is the center of the torus and dir is the normal direction. angle1 and angle2 are angles in degrees for the small circle; the last angle parameter is to make a section of the torus:


```python
torus = Part.makeTorus(10, 2)
```


<div class="mw-translate-fuzzy">

以上代码将场景一个直径为20（半径为10）且厚度为4（小圆半径为2）的环面。


</div>


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
```

以上代码将场景一个环面的切片。


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 360, 180)
```


<div class="mw-translate-fuzzy">

上述代码将创建半个环面；只有最后一个参数发生了改变。 即除了最后的angle，其余角度皆为默认值。将angle指定为180，将创建大环0至180度范围内的环面，也就是半个环面。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个立方体或长方体

通过**makeBox(length,width,height,\[pnt,dir\])**可创建一个立方体或长方体。其可选项默认值为pnt=Vector(0,0,0)与dir=Vector(0,0,1)。


</div>

Using `makeBox(length, width, height, [pnt, dir])`. By default pnt = Vector(0, 0, 0) and dir = Vector(0, 0, 1).


```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个球体

利用**makeSphere(radius,\[pnt, dir, angle1,angle2,angle3\])**函数可创建一个球体。其可选项默认值为pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=-90, angle2=90与angle3=360。 angle1与angle2分别为球体在垂直方向上（截取）的最大值与最小值，angle3为球体水平方向的截取部分。


</div>

Using `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 and angle3 = 360. Angle1 and angle2 are the vertical minimum and maximum of the sphere, angle3 is the sphere diameter.


```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), -90, 90, 180)
```


{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个圆柱体

通过**makeCylinder(radius,height,\[pnt,dir,angle\])**可创建一个圆柱体。可选项的默认值为pnt=Vector(0,0,0)，dir=Vector(0,0,1)以及 angle=360。


</div>

Using `makeCylinder(radius, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360. 
```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}


<div class="mw-translate-fuzzy">

#### 创建一个圆锥体

利用**makeCone(radius1,radius2,height,\[pnt,dir,angle\])**函数可创建一个圆锥体。其可选项默认值为 pnt=Vector(0,0,0), dir=Vector(0,0,1)与angle=360。


</div>

Using `makeCone(radius1, radius2, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360. 
```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}


<div class="mw-translate-fuzzy">

## 修改几何形状

FreeCAD提供了若干方法来修改几何形状。其中一些是简单的变换操作，如移动或旋转几何形状，而其他的更为复杂，如令两个形状进行并集与差集操作。


</div>

There are several ways to modify shapes. Some are simple transformation operations such as moving or rotating shapes, others are more complex, such as unioning and subtracting one shape from another. {{Top}}


<div class="mw-translate-fuzzy">

### 变换操作


</div>


<div class="mw-translate-fuzzy">

#### 平移一个几何形状

平移也就是将一个几何图形在不同的位置之间进行移动。 任意形状（边、面、立方体等等......）都可以通过下列同一种方式进行平移：


</div>

Translating is the act of moving a shape from one place to another. Any shape (edge, face, cube, etc\...) can be translated the same way: 
```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(Base.Vector(2, 0, 0))
```


<div class="mw-translate-fuzzy">

上述代码将几何形状\"myShape\"在x轴方向上移动2个单位。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

#### 旋转一个几何形状

为了旋转一个几何形状，您需要指定旋转中心、旋转轴以及旋转角度：


</div>

To rotate a shape, you need to specify the rotation center, the axis, and the rotation angle: 
```python
myShape.rotate(Base.Vector(0, 0, 0),Base.Vector(0, 0, 1), 180)
``` 上述代码将目标形状沿Z轴旋转180度。 {{Top}}


<div class="mw-translate-fuzzy">

#### 利用矩阵进行通用变换

矩阵是存储3D空间中各种变换的一种简便方式。您可以在单个矩阵中设置平移、旋转以及缩放的相关数值来对目标对象进行变换。例如：


</div>

A matrix is a very convenient way to store transformations in the 3D world. In a single matrix, you can set translation, rotation and scaling values to be applied to an object. For example: 
```python
myMat = Base.Matrix()
myMat.move(Base.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
```


<div class="mw-translate-fuzzy">

请注意：FreeCAD中的矩阵采用的是弧度制。另外，基本所有的矩阵操作都会借助一个向量，也可以直接取三个对应的数值，因此以下两行代码是等价的：


</div>


```python
myMat.move(2, 0, 0)
myMat.move(Base.Vector(2, 0, 0))
```


<div class="mw-translate-fuzzy">

一旦设置好矩阵中的值，我们就可以将其应用至待变换的几何形状。FreeCAD为此提供了两种方法：transformShape()与transformGeometry()。两者的不同之处在于：在使用前者时，您要确保执行的变换不会对目标形状造成形变（参见下文"缩放一个几何形状"）。我们可以像下面那样来执行变换：


</div>


```python
myShape.transformShape(myMat)
```

或者 
```python
myShape.transformGeometry(myMat)
```{{Top}}


<div class="mw-translate-fuzzy">

#### 对几何形状进行缩放

对一个几何形状进行缩放是一种更为危险的操作，因为这并不像平移或旋转那样，（以不同的x、y与z值）进行非等比缩放会修改原始形状的结构。例如，以相对于纵向值较大的水平值对圆形进行缩放，将使之成为一个椭圆形，以数学角度观之区别甚大。对于缩放操作而言，我们不能使用transformShape，而一定要采用transformGeometry()：


</div>

Scaling a shape is a more dangerous operation because, unlike translation or rotation, scaling non-uniformly (with different values for X, Y and Z) can modify the structure of the shape. For example, scaling a circle with a higher value horizontally than vertically will transform it into an ellipse, which behaves mathematically very differently. For scaling, we cannot use the `transformShape()`, we must use `transformGeometry()`: 
```python
myMat = Base.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```{{Top}}


<div class="mw-translate-fuzzy">

### 布尔运算


</div>


<div class="mw-translate-fuzzy">

#### 差集

从一个图形中去掉另一个图形在OCC/FreeCAD的术语中被称之为"切割（cut）"，可以这样来实现：


</div>

Subtracting a shape from another one is called \"cut\" in FreeCAD and is done like this: 
```python
cylinder = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
sphere = Part.makeSphere(5, Base.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```{{Top}}


<div class="mw-translate-fuzzy">

#### 交集

类似地，两个图形之间的交集被称之为"共有（common）"，可以这样来实现：


</div>

The same way, the intersection between two shapes is called \"common\" and is done this way: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```{{Top}}


<div class="mw-translate-fuzzy">

#### 并集

并集操作被称为"融合（fuse）"，可以实现如下：


</div>

Union is called \"fuse\" and works the same way: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```{{Top}}


<div class="mw-translate-fuzzy">

#### 截面

截面（section）是实体与平面的交集。它将返回一个交集曲线，一个由多条边复合而成的复合曲线。（？）


</div>

A \"section\" is the intersection between a solid shape and a plane shape. It will return an intersection curve, a compound curve composed of edges. 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
section = cylinder1.section(cylinder2)
section.Wires
> []
section.Edges
> [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
 <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
 <Edge object at 0D8F4BB0>]
```{{Top}}


<div class="mw-translate-fuzzy">

#### 挤型

挤型（extrusion）是将一个平面几何形状以特定的方向"推进"从而构建对应实体的动作。试想，将一个圆形"推挤"为一个管子：


</div>

Extrusion is the act of \"pushing\" a flat shape in a certain direction, resulting in a solid body. Think of a circle becoming a tube by \"pushing it out\": 
```python
circle = Part.makeCircle(10)
tube = circle.extrude(Base.Vector(0, 0, 2))
```


<div class="mw-translate-fuzzy">

如果采用的是空心圆形，将得到一个空心管。如果使用的是具有填充面的圆盘，则将得到一个实心圆柱体：


</div>


```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(Base.Vector(0, 0, 2))
```


{{Top}}


<div class="mw-translate-fuzzy">

## 考察形状

您可以方便地考察拓扑数据结构：


</div>

You can easily explore the topological data structure: 
```python
import Part
b = Part.makeBox(100, 100, 100)
b.Wires
w = b.Wires[0]
w
w.Wires
w.Vertexes
Part.show(w)
w.Edges
e = w.Edges[0]
e.Vertexes
v = e.Vertexes[0]
v.Point
```


<div class="mw-translate-fuzzy">

通过在python解释器中输入以上代码，您将得到一个易于理解的零件对象结构。其中使用makeBox()命令创建了一个实体形状。此实体就像所有其他零件实体一样，含有许多面。而面里总是包含多条连线，也就是构成面的边界的一系列边。每个面都有至少一条闭合连线（如果面内有个洞，则可能存在更多的闭合连线）。在连线中，我们可以看到每个独立的边，在每条边内，又可看到其顶点。显而易见，直边仅有两个顶点。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### 边的分析

对于以一条任意曲线作为边的情况而言，想必大多用户都希望对它进行离散化处理。在FreeCAD中是通过边的长度来对其进行参数化的。这就意味您可以通过其长度来构造一条边/曲线：


</div>

In case of an edge, which is an arbitrary curve, it\'s most likely you want to do a discretization. In FreeCAD the edges are parametrized by their lengths. That means you can walk an edge/curve by its length: 
```python
import Part
box = Part.makeBox(100, 100, 100)
anEdge = box.Edges[0]
print(anEdge.Length)
```


<div class="mw-translate-fuzzy">

您现在可以将长度作为位置，借此来访问对应边的大量属性。这意味着，如果边长为100mm，则起始位置为0，而终点位置为100。


</div>


```python
anEdge.tangentAt(0.0)          # tangent direction at the beginning
anEdge.valueAt(0.0)            # Point at the beginning
anEdge.valueAt(100.0)          # Point at the end of the edge
anEdge.derivative1At(50.0)     # first derivative of the curve in the middle
anEdge.derivative2At(50.0)     # second derivative of the curve in the middle
anEdge.derivative3At(50.0)     # third derivative of the curve in the middle
anEdge.centerOfCurvatureAt(50) # center of the curvature for that position
anEdge.curvatureAt(50.0)       # the curvature
anEdge.normalAt(50)            # normal vector at that position (if defined)
```


{{Top}}


<div class="mw-translate-fuzzy">

### 使用选中的对象

在此，我们来看看如何使用在视图中选择的对象。我们先来创建一个立方体，并令它在视图中显示出来。


</div>

Here we see now how we can use a selection the user did in the viewer. First of all we create a box and show it in the viewer. 
```python
import Part
Part.show(Part.makeBox(100, 100, 100))
Gui.SendMsgToActiveView("ViewFit")
```


<div class="mw-translate-fuzzy">

现在来选中其中的一些面和边。利用下列脚本，您可以遍历所有被选中的对象及其子元素：


</div>


```python
for o in Gui.Selection.getSelectionEx():
    print(o.ObjectName)
    for s in o.SubElementNames:
        print("name: ", s)
        for s in o.SubObjects:
            print("object: ", s)
```

利用以下脚本来统计选中对象的边长总和： 
```python
length = 0.0
for o in Gui.Selection.getSelectionEx():
    for s in o.SubObjects:
        length += s.Length

print("Length of the selected edges: ", length)
```{{Top}}


<div class="mw-translate-fuzzy">

## 完整的示例：OCC瓶子

我们可以在[OpenCasCade技术教程](http://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html#sec1)找到一个典型示例，其内容是如何构建一个瓶子。这对于FreeCAD而言也是个不错的练手机会。事实上，如果您同时随以下示例以及上述OCC页面进行对比学习，便会洞悉OCC结构是如何有效地实现于FreeCAD中的。以下完整脚本亦包含在FreeCAD安装内容中（在Mod/Part文件夹里），可通过在python解释器中输入下列代码来进行调用：


</div>

A typical example found on the [OpenCasCade Technology website](https://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html) is how to build a bottle. This is a good exercise for FreeCAD too. In fact, if you follow our example below and the OCC page simultaneously, you will see how well OCC structures are implemented in FreeCAD. The script is included in the FreeCAD installation (inside the {{FileName|Mod/Part}} folder) and can be called from the Python interpreter by typing: 
```python
import Part
import MakeBottle
bottle = MakeBottle.makeBottle()
Part.show(bottle)
```{{Top}}


<div class="mw-translate-fuzzy">

### 瓶子示例完整脚本

以下为MakeBottle的完整脚本代码：


</div>

For the purpose of this tutorial we will consider a reduced version of the script. In this version the bottle will not be hollowed out, and the neck of the bottle will not be threaded. 
```python
import Part, math
from FreeCAD import Base

def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])

    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])

    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)

    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    myBody = myBody.fuse(myNeck)

    return myBody

el = makeBottleTut()
Part.show(el)
```{{Top}}


<div class="mw-translate-fuzzy">

### 详细说明


</div>


```python
import Part, math
from FreeCAD import Base
```


<div class="mw-translate-fuzzy">

在此示例中，我们不仅需要Part模块，还要用到FreeCAD.Base模块，后者包括了如向量与矩阵这样的FreeCAD基本结构。


</div>


```python
def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)
```


<div class="mw-translate-fuzzy">

我们在此定义了makeBottle函数。调用此函数时可不输入任何参数，就像我们在上面所做的那样，在这种情况下，函数采用的是默认的宽、高以及厚度值。接下来，我们定义了一组点用于构建瓶子的基本轮廓。


</div>


```python
    ...
    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)
```


<div class="mw-translate-fuzzy">

以上代码分别：利用三个点构建了一条弧，依次利用两个点构建了两条线段。


</div>


```python
    ...
    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
```


<div class="mw-translate-fuzzy">

还记得几何图元与拓扑形状的区别吗？在此，我们利用此前创建的结构几何对象来构建拓扑形状。首先构建三条边（边可以是直边或曲边），随即利用它们创建一条连线。


</div>


```python
    ...
    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])
```


<div class="mw-translate-fuzzy">

到目前为止，我们仅构建了半个瓶子的轮廓。构建整个瓶子其实再次重复同样的流程即可，我们这里取巧对此前的半个轮廓进行镜像操作，再将它们粘合起来。首先创建一个矩阵。矩阵是将变换作用于3D空间物体的常用手段，这是因为借助它就能仅在一个结构中囊括3D物体的所有基本变换（移动、旋转、缩放）。 创建矩阵后，将其设置为对应的镜像变换，再创建一个此前连线的副本，并为之应用变换矩阵。现在就有了两条连线，由于连线实际是一系列边，因此我们可借助这两条连线来创建第三条连线。


</div>


```python
    ...
    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
```


<div class="mw-translate-fuzzy">

现在，我们就得到了一条闭合连线，借助它即可构造出面。一旦有了面，我们就可以对它进行挤型。挤型过程中我们就创建了一个实体。接下来，我们在对瓶体稍加倒圆角，这样做是因为我们都有匠人精神，不是嘛？


</div>


```python
    ...
    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
```


<div class="mw-translate-fuzzy">

此刻，瓶体大功告成，但是革命尚未成功，同志还需努力，我们还需创建一个瓶颈。因此我们利用一个圆柱体创建了新实体。


</div>


```python
    ...
    myBody = myBody.fuse(myNeck)
```


<div class="mw-translate-fuzzy">

融合（fuse）操作，在其他应用程序中有时也称并集，这是一种强大的工具。它负责小心地粘合需要粘合的部分，并去掉需要去掉的部分。


</div>


```python
    ...
    return myBody
```

随后，我们将Part零件实体作为函数的处理结果返回。 
```python
el = makeBottleTut()
Part.show(el)
``` 最后，我们调用此函数来创建实际零件，并将其显示粗来。 {{Top}}


<div class="mw-translate-fuzzy">

## 盒体穿孔

此实例为构建一个穿孔的盒子。


</div>

Here is a complete example of building a pierced box.


<div class="mw-translate-fuzzy">

构建的过程中，每次只构造一个面；当立方体创建完成后，再通过从中切割一个穿过它的圆柱体来实现穿孔。


</div>


```python
import Part, math
from FreeCAD import Base

size = 10
poly = Part.makePolygon([(0, 0, 0), (size, 0, 0), (size, 0, size), (0, 0, size), (0, 0, 0)])

face1 = Part.Face(poly)
face2 = Part.Face(poly)
face3 = Part.Face(poly)
face4 = Part.Face(poly)
face5 = Part.Face(poly)
face6 = Part.Face(poly)
     
myMat = Base.Matrix()

myMat.rotateZ(math.pi / 2)
face2.transformShape(myMat)
face2.translate(Base.Vector(size, 0, 0))

myMat.rotateZ(math.pi / 2)
face3.transformShape(myMat)
face3.translate(Base.Vector(size, size, 0))

myMat.rotateZ(math.pi / 2)
face4.transformShape(myMat)
face4.translate(Base.Vector(0, size, 0))

myMat = Base.Matrix()

myMat.rotateX(-math.pi / 2)
face5.transformShape(myMat)

face6.transformShape(myMat)               
face6.translate(Base.Vector(0, 0, size))

myShell = Part.makeShell([face1, face2, face3, face4, face5, face6])   
mySolid = Part.makeSolid(myShell)

myCyl = Part.makeCylinder(2, 20)
myCyl.translate(Base.Vector(size / 2, size / 2, 0))

cut_part = mySolid.cut(myCyl)

Part.show(cut_part)
```


{{Top}}


<div class="mw-translate-fuzzy">

## 加载与保存

在零件模块中有若干种保存工作进度的方式。您可以保存自己的FreeCAD文件，也可以将零件对象直接保存为常见的CAD格式，例如BREP，IGS，STEP与STL。


</div>

There are several ways to save your work. You can of course save your FreeCAD document, but you can also save [Part](Part_Workbench.md) objects directly to common CAD formats, such as BREP, IGS, STEP and STL.


<div class="mw-translate-fuzzy">

将一个几何形状保存至文件中是很方便的。FreeCAD针对所有图形提供了exportBrep()、exportIges()、exportStl()与exportStep()方法。因此，可以这样来保存它：


</div>


```python
import Part
s = Part.makeBox(10, 10, 10)
s.exportStep("test.stp")
```


<div class="mw-translate-fuzzy">

以上做法会将我们创建的立方体保存至一个STEP文件。而为了加载BREP、IGES或STEP文件，我们可以：


</div>


```python
import Part
s = Part.Shape()
s.read("test.stp")
```


<div class="mw-translate-fuzzy">

为了将一个**.stp**文件转换为一个**.igs**文件可以：


</div>


```python
 import Part
 s = Part.Shape()
 s.read("file.stp")       # incoming file igs, stp, stl, brep
 s.exportIges("file.igs") # outbound file igs
```


{{Top}}


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
