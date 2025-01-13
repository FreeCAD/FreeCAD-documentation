---
 GuiCommand:
   Name/ru: Указать горизонтальный габаритный размер
   Name: TechDraw_HorizontalExtentDimension
   MenuLocation: TechDraw , Размеры , Указать горизонтальный габаритный размер
   Workbenches: TechDraw_Workbench/ru
   Version: 0.19
   SeeAlso: TechDraw_LengthDimension/ru, TechDraw_VerticalExtentDimension/ru
---

# TechDraw HorizontalExtentDimension/ru



## Описание

The **TechDraw HorizontalExtentDimension** tool adds a linear dimension to a View. The dimension extends from the left most point on the selected objects to the right most point.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Horizontal and vertical extent dimensions of a B-spline*

## Usage

1.  Select a View or a collection of Edges in a View.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning tools** [preference](TechDraw_Preferences#Dimensions.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> Insert Horizontal Extent Dimension** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Insert Horizontal Extent Dimension](TechDraw_HorizontalExtentDimension.md)** button.

    -   Select the **TechDraw → Dimensions → <img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> Insert Horizontal Extent Dimension** option from the menu.
3.  A dimension is added to the View.
4.  The dimension may be dragged to the desired position.
5.  If needed, add tolerances as described on [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

### Change properties 

To change the properties of a dimension object either double-click it in the drawing or in the [Tree view](Tree_view.md). This will open the [Dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).



## Ограничения

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md).

## Notes

See [TechDraw LengthDimension](TechDraw_LengthDimension#Notes.md).



## Свойства

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md). Exceptions noted below.



### Данные


{{Properties_Title|Base}}

-    **Measure Type|Enumeration**: Not yet implemented for extent dimensions.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Horizontal Extent Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
selection = ['Edge1', 'Edge2']                      # or [] for all

TechDraw.makeExtentDim(view1, selection, 0)         # view1 is a DrawViewPart; 0 for horizontal
App.ActiveDocument.DimExtent.Y = -60                # offset dimension line from dimensioned edges in Y direction
App.ActiveDocument.DimExtent.X = 10                 # offset dimension text along dimension line in X direction
App.ActiveDocument.DimExtent.FormatSpec = '%.0f'    # Dimension format

TechDraw.makeExtentDim(view1, selection, 1)         # view1 is a DrawViewPart; 1 for vertical
App.ActiveDocument.DimExtent001.X = -130            # offset dimension line from dimensioned edges in X direction
App.ActiveDocument.DimExtent001.Y = 10              # offset dimension text along dimension line in Y direction
App.ActiveDocument.DimExtent001.FormatSpec = '%.0f'

# Note the dimension names are 'DimExtent', 'DimExtent001' etc in the order created.
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/ru
