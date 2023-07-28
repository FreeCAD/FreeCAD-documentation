---
- GuiCommand:/ru
   Name/ru:Улучшить форму
   Name:Part_RefineShape
   MenuLocation:Деталь → Создать копию → Refine Shape
   Workbenches:[Part](Part_Workbench/ru.md)
   SeeAlso:[Создать простую копию](Part_SimpleCopy/ru.md), [Создать преобразованную копию](Part_TransformedCopy/ru.md), [Создать копию элемента формы](Part_ElementCopy/ru.md), [Элемент закрепления фигуры](OpenSCAD_RefineShapeFeature/ru.md)
---

# Part RefineShape/ru



## Определение


**<img src="images/Part_RefineShape.svg" width=16px> [Улучшить форму](Part_RefineShape/ru.md)
**

создает непараметрическую копию формы у которой все грани полностью отчищены от лишних ребер на их поверхности.

After certain boolean operations, like [Part Fuse](Part_Fuse.md), some lines from the previous shapes may remain visible. This tool produces a copy of that boolean result, and cleans up those seams.

**Alternatively**, to produce other non-parametric copies use **<img src="images/Part_SimpleCopy.svg" width=16px> [Simple Copy](Part_SimpleCopy.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Transformed Copy](Part_TransformedCopy.md)**, and **<img src="images/Part_ElementCopy.svg" width=16px> [Element Copy](Part_ElementCopy.md)**

![](images/PartRefineShape_it.png ) 
*Original boolean result with 11 faces (left), and refined shape copy with 7 faces (right).*



## Применение

1.  Select an object that you wish to clean and copy.
2.  Go to the menu **Part → Create a copy → <img src="images/Part_RefineShape.svg" width=16px> Refine shape**.
3.  A cleaned, independent copy of the original object is created; the original object is hidden.

As of <small>(v0.19)</small>  the result defaults to a parametric (linked) copy.

This behavior can be changed in the <img alt="" src=images/Std_DlgParameter.svg  style="width:24px;"> [Parameter editor](Std_DlgParameter.md):

1.  Go to the subgroup: `BaseApp/Preferences/Mod/Part`
2.  Change `ParametricRefine` of type `Boolean` to `False` to get the old behavior (independent copy).

See other parameters in [Fine-tuning](Fine-tuning.md).



## Примечания


<div class="mw-translate-fuzzy">

-   Эту функцию можно использовать в качестве завершающего шага для очистки форма, в процессе моделирования [конструктивной сплошной геометрии](constructive_solid_geometry/ru.md).
-   Эта функция может помочь очистить модель от нежелательных швов перед применением функций для создания кромок например таких, как [Фаска](Part_Fillet/ru.md).
-   Такая \"очистка\" формы может улучшить качество печати на 3D-принтере, т.к. перед экспортом в формат сетки у твердого тела будут отсутствовать нежелательные швы.
-   Эта функция также может быть использована после преобразования сетки в форму ([Shape From Mesh](Part_ShapeFromMesh/ru.md)) для удаления ребер которые лежат в одной плоскости на плоских гранях.


</div>



## Ограничения

-   The refinement algorithm only works on shells. Therefore it iterates over the shells of the input shape and then for each shell it creates a new shell with joined faces wherever possible. This means that if your input shape is only a face, wire, edge or vertex then the algorithm does nothing.
-   Unlike the <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [OpenSCAD RefineShapeFeature](OpenSCAD_RefineShapeFeature.md) command, <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part RefineShape](Part_RefineShape.md) won\'t update when the preceding shapes are changed.



## Программирование

Команда Python для улучшения формы выглядит следующим образом:


```python
shape.removeSplitter()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/ru
