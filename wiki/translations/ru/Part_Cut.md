---
- GuiCommand:
   Name: Part Cut
   Name/ru: Обрезать
   MenuLocation: Деталь - Булевы операции - Обрезать
   Workbenches: [Part](Part_Workbench/ru.md)
   SeeAlso: [Объединение](Part_Union/ru.md), [Пересечение](Part_Common/ru.md), [Part Boolean](Part_Boolean/ru.md)
---

# Part Cut/ru



## Описание

Cuts (subtracts) selected Part objects, the last one being subtracted from the first one. This operation is fully parametric and the components can be modified and the result recomputed.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

[480px\|left\|Cut](IMAGE:Part_Cut_01.png.md)



## Применение

1.  Select two shapes
2.  Invoke the Part Cut command several ways:
    -   Press the **![](images/) '''Cut'''** button in the Part toolbar
    -   Use the **Part → Boolean → Cut** entry from the Part menu

## Supported inputs 

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. For example objects made with the Part, PartDesign or Sketcher workbenches. For meshes there are dedicated Boolean tools in [Mesh Workbench](Mesh_Workbench.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/ru
