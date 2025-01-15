---
 GuiCommand:
   Name: Arch RemoveShape
   Name/ru: Arch RemoveShape
   MenuLocation: Архитектура , Утилиты , Удалить форму из Архитектуры
   Workbenches: Arch_Workbench/ru
   SeeAlso: Arch MeshToShape/ru
---

# Arch RemoveShape/ru


</div>



## Описание

The **Arch RemoveShape** tool attempts at removing the inner cubic shape of an [Arch Wall](Arch_Wall.md) or [Arch Structure](Arch_Structure.md), and adjusting its properties, making it totally parametric. This tool will only work if the underlying shape is cubic (exactly 6 faces, all corners have only right angles).



## Применение

1.  Select an [Arch Wall](Arch_Wall.md) or [Arch Structure](Arch_Structure.md).
2.  Select the **Utils → <img src="images/Arch_RemoveShape.svg" width=16px> Remove Shape from Arch** option from the menu.



## Программирование


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
removeShape(objs, mark=True)
```

-   Takes a list of Arch objects (`objs`) built on a cubic shape, and removes the inner shape, keeping the length, width and height as properties of the Arch object.
    -   
        `objs`
        
        is a single object, [Arch Wall](Arch_Wall.md) or [Arch Structure](Arch_Structure.md), or a list of them.
-   If `mark` is `True`, objects that cannot be processed by this function will become red.


```python
import FreeCAD, Draft, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(Box)
FreeCAD.ActiveDocument.recompute()

Arch.removeShape(Structure)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch RemoveShape/ru
