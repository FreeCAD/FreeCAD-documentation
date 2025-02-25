---
 GuiCommand:
   Name: Arch Equipment
   Name/ru: Оборудование
   MenuLocation: Arch , Оборудование
   Workbenches: Arch_Workbench/ru
   Shortcut: **E** **Q**
   SeeAlso: Arch_3Views/ru
---

# Arch Equipment/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Инструмент \"Оборудование\" предлагает вам простой и удобный способ добавления в интерьер ваших проектов неструктурных, автономных элементов, таких как: предметы мебели, бытовая техника, сантехническое оборудование или электроприборы. Оборудование основано на [деталях верстака Part](Part_Workbench/ru.md), что позволяет извлечь выгоду из солидных возможностей геометрии BRep и создавать красивые виды при визуализации в виде плана и сечения.


</div>

<img alt="" src=images/Arch_equipment_example.jpg  style="width:600px;"> 
*Furniture objects enclosed in an [Arch Equipment](Arch_Equipment.md) object. The flat projections can be obtained by the [Draft Shape2DView](Draft_Shape2DView.md) tool*

Начиная с версии 0.17, объекты оборудования также имеют свойство **HiRes (высокая детализация)**, к которому может быть присоединен [Mesh](Mesh_Workbench/ru.md) объект. Объекты оборудования затем могут быть созданы для отображения этой высокоспециализированной модели в 3D-представлении вместо их формы, что позволяет использовать любые объекты с высокой детализацией, такие как реалистичные предметы мебели, обычно встречающиеся на веб-сайтах.

<img alt="" src=images/Arch_equipment_mesh.jpg  style="width:600px;"> 
*Furniture objects enclosed in an [Arch Equipment](Arch_Equipment.md) object, with a high resolution mesh attached*

При использовании экспортера Arch OBJ все объекты оборудования, находящиеся в режиме отображения сетки, будут экспортироваться как mesh сетка, а не как форма.



## Применение

1.  Select a [Part](Part_Workbench.md) shape, and optionally a [Mesh](Mesh_Workbench.md) object.
2.  Press the **<img src="images/Arch_Equipment.svg" width=16px> [Equipment](Arch_Equipment.md)** button, or press **E** then **Q** keys.



## Опции

-   Оборудование обладает такими же общими свойствами и моделью поведения, как и все остальные [компоненты верстака Arch](Arch_Component/ru.md)



## Свойства

-    **Model**: A description of the model of this equipment.

-    **Url**: An URL of the product page where more information about this equipment can be found.

-    **Mesh**: A [Mesh](Mesh_Workbench.md) representation to use for this equipment. When set, the **Mesh** display mode becomes available.



## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Equipment tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Equipment = makeEquipment(baseobj=None, placement=None, name="Equipment")
```

-   Creates an `Equipment` object from the given `baseobj`, which can be a `Part` or a `Mesh`.
-   If a `placement` is given, it is used.
-   It returns `None` if the operation fails.

Пример: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 500
Box.Width = 2000
Box.Height = 600

Equip = Arch.makeEquipment(Box)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Equipment/ru
