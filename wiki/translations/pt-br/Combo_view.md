# Combo view/pt-br
{{TOCright}}

## Introdução

The [Combo view](combo_view.md) is one of the main panels in the FreeCAD [interface](interface.md). It is located on the left side of the screen by default. It is **composed of two sections**, the:

-   [Upper section](#Upper_section.md) which contains two tabs: the **Model** tab and **Tasks** tab
-   [Lower section](#Lower_section.md) shows the [Property editor](property_editor.md). It contains two tabs: the **View** and **Data** properties. The [Property editor](property_editor.md) is only shown when the **Model** tab is **active**, that is, when the [tree view](tree_view.md) is visible.


**Note:**

originally the upper part ([tree view](tree_view.md)) was separate from the lower part ([property editor](property_editor.md)) but then they were combined, and thus the \"combo\" view was created.

## Upper section 

The **Model** tab shows the [tree view](tree_view.md), which is a representation of the document\'s content, including 2D and 3D geometry with their parametric history, but also supporting objects that contain data saved in the document.

The **Tasks** tab shows the [task panel](task_panel.md), which will show different actions depending on the active workbench, and the active tool.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="600px;">


*The combo view has two tabs: the Model tab that controls displaying the [tree view](tree_view.md) and the [property editor](property_editor.md), and the Tasks tab that controls showing the [task panel](task_panel.md).*

## Lower section 

The lower part of the combo view shows the [property editor](property_editor.md), which displays two tabs for **View** and **Data** properties. The property editor is only shown when the **Model** tab is active, that is, when the [tree view](tree_view.md) is visible.

-   The **View** tab shows visualization properties of the objects, which only affect their appearance in the [3D view](3D_view.md).

-   The **Data** tab shows the parametric properties of the objects, which determine how the geometrical shapes are really defined.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Tree_Data_properties.png  style="width:" height="600px;">


*The lower part of the combo view is the property editor, which shows View and Data properties.*

## Disabling Combo view 

To use these views by themselves use the [parameter editor](Std_DlgParameter.md). Create the following subgroups if they don\'t exist

-    `BaseApp/Preferences/DockWindows/TreeView`
    

-    `BaseApp/Preferences/DockWindows/PropertyView`
    

then add the parameter `Enabled` of type `Boolean`, and set it to `True`.

Then activate the view using the menu, **View → Panels → Tree view** or **→ Property view**.


{{Std Base navi

}} {{Interface navi}}

---
[documentation index](../README.md) > Combo view/pt-br
