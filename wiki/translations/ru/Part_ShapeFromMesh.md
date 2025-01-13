---
 GuiCommand:
   Name/ru: Создать фигуру из полигональной сетки
   Name: Part_ShapeFromMesh‏‎
   MenuLocation: Part , Создание фигуры из полигональной сетки...
   Workbenches: Part_Workbench/ru
   SeeAlso: Part_MakeSolid/ru, Part_RefineShape/ru, Part_PointsFromMesh/ru
---

# Part ShapeFromMesh/ru


</div>



## Введение


<div class="mw-translate-fuzzy">

## Введение 

Эта команда создаёт форму из [сетки](Glossary/ru#Mesh.md). Возможности объектов типа сетка внутри FreeCAD ограничены, преобразование их в формы позволяет использовать с ними гораздо больше инструментов (см. так же [примечания](#Примечание.md)).


</div>

The inverse operation is [Mesh FromPartShape](Mesh_FromPartShape.md) from the <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh Workbench](Mesh_Workbench.md).



## Применение


<div class="mw-translate-fuzzy">

## Использование

1.  Выберите полигонально-сеточный объект.
2.  Выберите в верхнем меню ** Деталь** → **<img src="images/Part_ShapeFromMesh.png" width=32px> Создание формы из сетки...**.
3.  Всплывающее меню запросит допуск сшивания формы (значение по умолчанию: 0,1)
4.  Инструмент создаёт из сетки отдельный новый объект - форму.


</div>

## Properties

See also: [Property editor](Property_editor.md).

The Part ShapeFromMesh command creates [Part Feature](Part_Feature.md) objects with no additional properties.



## Программирование

Creating a [Shape](Shape.md) from a [Mesh](Mesh.md) can be done by using the `makeShapeFromMesh` method from a [Part TopoShape](Part_TopoShape.md); you need to specify the source mesh and tolerance, and assign the result to a new [Part Feature](Part_Feature.md) object.

Notice that the mesh must be recalculated before it is converted to a Shape, otherwise there won\'t be topology information, and the conversion won\'t be successful.


```python
import FreeCAD as App
import Part

doc = App.ActiveDocument
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid = doc.addObject("Part::Feature", "Solid")
solid.Shape = Part.Solid(shape.removeSplitter())
solid.Placement.Base = App.Vector(15, 0, 0)
doc.recompute()
```



## Ссылки

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) video by AllVisuals4U.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/ru
