---
 GuiCommand:
   Name/ru: Улучшить форму
   Name: Part_RefineShape
   MenuLocation: Деталь , Создать копию , Refine Shape
   Workbenches: Part_Workbench/ru
   SeeAlso: Part_SimpleCopy/ru, Part_TransformedCopy/ru, Part_ElementCopy/ru, OpenSCAD_RefineShapeFeature/ru
---

# Part RefineShape/ru


</div>



## Определение


<div class="mw-translate-fuzzy">


**<img src="images/Part_RefineShape.svg" width=16px> [Улучшить форму](Part_RefineShape/ru.md)
**

создает непараметрическую копию формы у которой все грани полностью отчищены от лишних ребер на их поверхности.


</div>

![](images/PartRefineShape_it.png ) 
*Original with 11 faces (left), and refined copy with 7 faces (right).*



## Применение

1.  Select one or more objects.
2.  Select the **Part → Create a copy → <img src="images/Part_RefineShape.svg" width=16px> Refine shape** option from the menu.
3.  For each object a cleaned, parametric copy is created
4.  The original objects are hidden.



## Примечания


<div class="mw-translate-fuzzy">

-   Эту функцию можно использовать в качестве завершающего шага для очистки форма, в процессе моделирования [конструктивной сплошной геометрии](constructive_solid_geometry/ru.md).
-   Эта функция может помочь очистить модель от нежелательных швов перед применением функций для создания кромок например таких, как [Фаска](Part_Fillet/ru.md).
-   Такая \"очистка\" формы может улучшить качество печати на 3D-принтере, т.к. перед экспортом в формат сетки у твердого тела будут отсутствовать нежелательные швы.
-   Эта функция также может быть использована после преобразования сетки в форму ([Shape From Mesh](Part_ShapeFromMesh/ru.md)) для удаления ребер которые лежат в одной плоскости на плоских гранях.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A Part RefineShape object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional property:

### Data


{{TitleProperty|Refine}}

-    **Source|Link**: specifies the linked source shape.



## Программирование

Команда Python для улучшения формы выглядит следующим образом:


```python
shape.removeSplitter()
```


<div class="mw-translate-fuzzy">





</div>


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/ru
