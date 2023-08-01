---
- GuiCommand:
   Name: Drawing View
   Workbenches: [Drawing](Drawing_Workbench.md), Complete
   MenuLocation: Drawing - Insert view in drawing
   Shortcut: none
   SeeAlso: [Drawing Landscape A3](Drawing_Landscape_A3.md)
---

# Drawing View

This tool creates a new view of the selected object in the active drawing sheet.

<img alt="A drawing sheet with three views: front, top and isometric." src=images/Drawing_Views.png  style="width:500px;">

### Usage

Select an object either in the 3D view or the Project tree, then click on the Drawing View tool. By default, a top view scaled at 1:1 (real scale) will be placed at the top left of the page. It may not be visible if it\'s too small or too big for the page.

A **View** object is added to the **Page** object in the Project tree. For subsequent views, a three-digit number will be appended to the name. Click on the arrow in front of the Page object to unfold it and display the views it contains.

If only the object is selected in the Project Tree, the view is added to the first page of the project. If you have multiple pages in your project please select the object and the page it should be added to. Then click on the icon to add the view to the selected page.

### Modify an existing view 

Unfold the Page object in the Project tree, and select the View. Its parameters can be edited in the Property View Data tab.

<img alt="" src=images/Drawing_View_Properties.png‎ ) ![Isometric view with smooth lines visibility off](images/Drawing_View_Iso.png‎  style="width:150px;"> <img alt="Isometric view with smooth lines visibility on" src=images/Drawing_View_Iso_SmoothLines.png‎‎  style="width:150px;">

-   **Label**: changes the view\'s label in the Project tree. You can also click on the View in the tree and right-click → Rename, or press **F2**.
-   **Rotation**: rotates the view. For example, an isometric view will require a 60 degree rotation (see also Direction parameter below)
-   **Scale**: sets the view scale.
-   **X**: sets the view\'s horizontal position on the page in millimeters.
-   **Y**: sets the view\'s vertical position on the page in millimeters. Please note that coordinate (0,0) is located at the top left of the page, so the higher the number, the lower in the page the view will be.
-   **Direction**: changes the view direction. It is set by xyz values that define a vector normal to the page. Top view will be (0,0,1), and isometric will be (1,1,1). Values can be negative.
-   **Show Hidden Lines**: toggles the hidden lines visibility on or off by selecting *True* or *False*.
-   **Show Smooth Lines**: toggles the smooth lines visibility on or off by selecting *True* or *False*. Smooth lines are also called tangency edges. These edges indicate surface changes between tangent surfaces.

### Drawing View Wizard 

To generate a drawing sheet with standard views automatically, use the [Automatic drawing Macro](Macro_Automatic_drawing.md). 

### Other

If you are looking for persective-orthographic toggling in 3D view check [Std PerspectiveCamera](Std_PerspectiveCamera.md) and [Std OrthographicCamera](Std_OrthographicCamera.md)


{{docnav
|[New A3 landscape drawing](Drawing_Landscape_A3.md)
|[Annotation](Drawing_Annotation.md)
|[Drawing Workbench](Drawing_Workbench.md)
|IconL=Drawing_Landscape_A3.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Annotation.png
}}

 {{Drawing Tools navi}}



---
⏵ [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing View
