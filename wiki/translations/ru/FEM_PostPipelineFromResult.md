---
- GuiCommand:
   Name: FEM PostPipelineFromResult
   Name/ru: FEM PostPipelineFromResult
   MenuLocation:  Results - Post pipeline from result
   Workbenches: [FEM](FEM_Workbench/ru.md)
   Version: 0.17
   Shortcut: 
   SeeAlso: [FEM tutorial](FEM_tutorial/ru.md)
---

# FEM PostPipelineFromResult/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Конвейер - это результирующий объект, создающий новое графическое представление результатов анализа МКЭ на анализируемой детали. Он добавляет цветовую шкалу и дополнительные параметры отображения.


</div>

## Применение

1.  Select a result object.
2.  Click the **<img src="images/FEM_PostPipelineFromResult.svg" width=16px> '''Post pipeline from result'''** button, or select the **Results → <img src="images/FEM_PostPipelineFromResult.svg" width=16px> Post pipeline from result** option from the menu.
3.  A new object called \"Pipeline\" is added to your analysis.
4.  Double-click the new Pipeline object in the [Tree view](Tree_view.md) and select a display mode and the result field. For example for the mode {{Value|Surface}} and the field {{Value|Von Mises stress}} the pipeline will look like this:

<img alt="" src=images/Pipeline.PNG  style="width:500px;">

If you see no model in the graphical area, go to and enable **Edit → Preferences → Display → 3D View → Rendering → Backlight color**.

If you use a [SI](https://en.wikipedia.org/wiki/International_System_of_Units)-derived FreeCAD [unit system](Preferences_Editor#Units.md), the values in the output scale are based on SI units as well. This means the displacement is in meter, the stress is in Pascal and the temperature is in Kelvin.

## Properties

### Dialog box 

This pipeline dialog box has the following settings:

-   **Mode**: How to draw the results. The possible modes are
    -   **Outline**: The outline of the result mesh. In fact is displays no results but only the borders of the mesh.
    -   **Nodes**: The result mesh nodes.
    -   **Surface**: This is the default and displays the surface of the result mesh.
    -   **Surface with Edges**: Like **Surface** but with the mesh outline edges and the surface mesh node connection lines.
-   **Field**: Which result property to draw.
-   **Vector**: Is only active if the **Field** is a vector. You can select whether to display the vector *Magnitude* or its X, Y, Z components.

### Scale

If you double-click on the scale, you get this settings dialog box:

![](images/SIMTUT_05.PNG )

and you can modify these properties:

-   **Gradient**: You can select reversed order of the default color gradient, *Red-White-Blue*, *Black-White* or *White-Black*.
-   **Style**: The default option *Flow* uses the full color gradient range. The option *Zero* uses only the color gradient range starting form the color that would display the mean value to the maximum.
-   **Visibility**: The option *Out grayed* will color all mesh nodes whose values are outside the set minimum/maximum range in gray. The option *Out transparent* will make these mesh nodes transparent.
-   **Parameter range**: Minimum and maximum values are filled-in automatically. You can modify them, however make sure you know what you are doing. You can also change the number of displayed decimal places and the number of labels distributed over the parameter range.

### Property Editor 

In the [property editor](Property_editor.md) you can set in the *View* tab the settings from the dialog box. In the *Data* tab you can additionally set this:

-    **Mode**: How the filters used in the pipeline will be treated. These modes are possible:

    -   **Serial**: In this mode every filter takes the previous filter as input. The order is hereby the order of creation. The first created filter takes the pipeline as input. Its **Input** property is therefore empty.
    -   **Parallel**: In this mode all filters take the pipeline as input.
    -   **Custom**: <small>(v0.20)</small>  This is the default and keeps the input of the filters as they are. Therefore it allows to have e.g. two filters that take the pipeline as input, and a third filter that takes one of the two filters as input.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/ru
