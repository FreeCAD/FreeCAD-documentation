---
 GuiCommand:
   Name/ru: Создать прямоугольник
   Name: Sketcher_CreateRectangle
   MenuLocation: Sketch , Геометрия эскиза , Создать прямоугольник
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **R**
   SeeAlso: Sketcher_CreateOblong/ru, Sketcher_CreatePolyline/ru
---

# Sketcher CreateRectangle/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент рисует прямоугольник, по двум противоположным точкам. При запуске инструмента указатель мыши меняется на белый крест с красным прямоугольником. Координаты указателя отображаются рядом с ним синим цветом в режиме реального времени.


</div>

To define a rectangle via a center point and an edge point, use the [Centered rectangle](Sketcher_CreateRectangle_Center.md) tool.

![](images/SketcherCreateRectangleExample.png‎ )



## Применение


<div class="mw-translate-fuzzy">

-   После нажатия кнопки **<img src="images/Sketcher_CreateRectangle.svg" width=24px> Прямоугольник** щелкните один раз, чтобы установить первый угол, затем переместите мышь и щелкните второй раз, чтобы установить противоположный угол.
-   Нажатие **Esc** или правой кнопки мыши закрывает функцию.


</div>

## Notes

-   When launched the rectangle tools add a **Rectangle parameters** section at the top of the Sketcher [Task panel](Task_panel.md) (<small>(v0.22)</small> ). It contains:

1.  A **Mode** spinbox to chose one of the modes to draw the rectangle:
    -   Corner, length & width
    -   Center, length & width
    -   3 corners
    -   Center and two corners
2.  A **Rounded corners** checkbox to apply round corners to the rectangle.
3.  A **Frame** checkbox to add a contour with a constant offset to the (rounded) rectangle.

-   All three buttons in this selection now launch the same tool but with different preset combinations of mode and options that can still be altered after the first click.
-   If **Rounded corners** is enabled, the offset is inward, and the offset value is larger than the corner radius, the offset contour will be created without fillets.
-   The modes **3 corners**, and **Center and two corners** create parallelograms rather than rectangles.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/ru
