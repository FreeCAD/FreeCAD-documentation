---
 GuiCommand:
   Name: Arch_Building
   Name/ru: Здание
   Workbenches: Arch_Workbench/ru
   MenuLocation: Arch , Здание
   Shortcut: **B** **U**
   SeeAlso: Arch_BuildingPart/ru, Arch_Site/ru
---

# Arch Building/ru

## Описание

Arch Building - это особый тип объекта группы FreeCAD, который особенно подходит для представления целого здания. Они в основном используются для организации вашей модели с помощью объектов [ floor](Arch_Floor.md).

## Применение

1.  Optionally, select one or more objects to be included in your new building.
2.  Press the **<img src="images/Arch_Building.svg" width=16px> [Arch Building](Arch_Building.md)** button, or press the **B** then **U** keys.

## Опции

-   Starting from FreeCAD version 0.18, the Building object is actually a [BuildingPart](Arch_BuildingPart.md) with its **IFC Type** property set to \"Building\". You can convert any BuildingPart to a Building simply by changing its IFC Type.
-   After creating a building, you can add more objects to it by drag and dropping them in the Tree View or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.
-   You can remove objects from a building by drag and dropping them out of it the Tree View or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

## Свойства

-    **Building Type**: The type of this building, to choose from a list

## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Building tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

-   Creates a `Building` object from `objectslist`, which is a list of objects, or `baseobj`, which is a `Shape`.

Пример:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Building/ru
