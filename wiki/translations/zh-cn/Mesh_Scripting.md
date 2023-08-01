# Mesh Scripting/zh-cn
{{TOCright}}


<div class="mw-translate-fuzzy">

### 简介

首先，导入网格模块是必不可少的:


</div>

To get access to the `Mesh` module you have to import it first:


```python
import Mesh
```


<div class="mw-translate-fuzzy">

### 创建与加载

如果要创建一个空的网格对象，仅需轻松地调用以下标准构造函数：


</div>

To create an empty mesh object just use the standard constructor:


```python
mesh = Mesh.Mesh()
```


<div class="mw-translate-fuzzy">

您也可以利用文件中的数据来创建一个网格对象：


</div>


```python
mesh = Mesh.Mesh("D:/temp/Something.stl")
```

或者利用一组三角形（即利用构成三角形的顶点）来创建网格：


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


<div class="mw-translate-fuzzy">

网格内核会通过对重合点与边进行排序来小心地创建一个正确的拓扑数据结构。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

### 建模

您可以利用Python脚本BuildRegularGeoms.py来创建规则的几何图形。


</div>

To create regular geometries you can use one of the `create*()` methods. A torus, for instance, can be created as follows:


```python
m = Mesh.createTorus(8.0, 2.0, 50)
Mesh.show(m)
```


<div class="mw-translate-fuzzy">

前两个参数定义了圆环的半径，而第三个参数则是针对创建多少个三角形而设置的子采样因子。第三个参数的值越大，则物体表面就越平滑且细节愈丰富细腻。网格类提供了一组以建模为目的的布尔函数，其中有对两个网格对象进行并、交、差的操作。


</div>

The `Mesh` module also provides three Boolean methods: `union()`, `intersection()` and `difference()`:


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


<div class="mw-translate-fuzzy">

最后，这里给出一个计算球体与立方体相交的示例，显示的是在球体上两者的交集。


</div>


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


<div class="mw-translate-fuzzy">

### 七零八碎的小东东

这里还有一个与网格有关的脚本扩展源：即网格模块的单元测试脚本（尽管挺难使的）。 在此单元测试中，将调用所有的方法并调整所有的属性，以确保它们的正确性。 所以，如果您有充足的冒险精神，就可以去看一看[单元测试模块](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py)。


</div>

An extensive, though hard to use, source of mesh related scripting are the unit test scripts of the `Mesh` module. In these unit tests literally all methods are called and all properties/attributes are tweaked. So if you are bold enough, take a look at the [Unit Test module](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Mesh/App/MeshTestsApp.py).


<div class="mw-translate-fuzzy">

参见[Mesh API](Mesh_API.md)


</div>


{{Top}}


 {{Mesh Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Mesh](Mesh_Workbench.md) > Mesh Scripting/zh-cn
