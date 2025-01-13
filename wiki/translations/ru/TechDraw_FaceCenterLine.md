---
 GuiCommand:
   Name/ru: Добавить осевую линию к граням
   Name: TechDraw_FaceCenterLine
   MenuLocation: TechDraw , Добавить Линии , Add Centerline to Face
   Workbenches: TechDraw_Workbench/ru
   Version: 0.19
   SeeAlso: TechDraw_CosmeticVertex/ru, TechDraw_2LineCenterLine/ru, TechDraw_2PointCenterLine/ru, TechDraw_CosmeticEraser/ru
---

# TechDraw FaceCenterLine/ru


</div>



## Описание

The **TechDraw FaceCenterLine** tool adds a centerline to selected faces.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Centerline added to a face*

## Usage create 

1.  Select one or more faces in a View.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Add Centerline to Faces](TechDraw_FaceCenterLine.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_FaceCenterLine.svg" width=16px> Add Centerline to Faces** option from the menu.
3.  A task panel opens. See [Options](#Options.md) for more information.
4.  Press the **OK** button to confirm.
5.  A centerline is added at the midpoint of the bounding box of the selected face(s).

## Usage edit 

Any of the centerline tools (<img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:16px;"> TechDraw FaceCenterLine, <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:16px;"> [TechDraw 2LineCenterLine](TechDraw_2LineCenterLine.md) and <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:16px;"> [TechDraw 2PointCenterLine](TechDraw_2PointCenterLine.md)) can be used to edit any centerline.

1.  Select a centerline.
2.  Invoke a centerline tool.
3.  A task panel opens. See [Options](#Options.md) for more information.
4.  Press the **OK** button to confirm.




<div class="mw-translate-fuzzy">

## Свойства


</div>

-   **Orientation**:
    -   **Vertical**: Forces the centerline vertical. Ignored for 2PointCenterLines.
    -   **Horizontal**: Forces the centerline horizontal. Ignored for 2PointCenterLines.
    -   **Aligned**: Not available for FaceCenterLines. Forces the centerline to follow the general direction of the selected edges for 2LineCenterLines. Ignored for 2PointCenterLines.
-   **Shift Horizontal**: Moves the centerline left or right of its normal position.
-   **Shift Vertical**: Moves the centerline up or down from its normal position.
-   **Rotate**: Rotates the centerline around its midpoint (degrees. + counterclockwise, - clockwise).
-   **Extend By**: Makes the centerline longer by this amount.
-   **Color**: The color of the centerline.
-   **Weight**: The width of the centerline.
-   **Style**: The linestyle of the centerline. The options are:
    -   <img alt="" src=images/Continuous-line.svg  style="width:20px;"> 
**Continuous**
    -   <img alt="" src=images/Dash-line.svg  style="width:20px;"> 
**Dash**
    -   <img alt="" src=images/Dot-line.svg  style="width:20px;"> 
**Dot**
    -   <img alt="" src=images/DashDot-line.svg  style="width:20px;"> 
**DashDot**
    -   <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> 
**DashDotDot**



## Примечания

-   To delete a centerline select it and press **Delete**. <small>(v1.0)</small> 
-   FaceCenterLines will eventually replace two View properties:
    -   
        **HorizCenterLine**
        
        : Show a horizontal centerline through view.

    -   
        **VertCenterLine**
        
        : Show a vertical centerline through view.

## Properties

Centerlines have no properties of their own, as they are not document objects.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/ru
