# Task panel
## Introduction

The [Task panel](Task_panel.md) appears in a stand-alone [dockable](Combo_view#Dock_Task_panel_on_top_of_Combo_view.md) panel called **Tasks**. It is a customizable space that is able to contain any type of graphical widgets like input fields, checkboxes, spinboxes, buttons, labels, images, and other elements, depending on the currently active tool.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:250px;">



*Task panel showing various tools when the [PartDesign Workbench](PartDesign_Workbench.md) is active, and a [sketch](Sketch.md) is selected.*

## Working with the Task panel 

A Task panel normally opens when a tool that requires user input is activated. If the tool doesn\'t need user input, it will produce its result or terminate, but won\'t display a Task panel. The user input may be anything such as text, 3D point coordinates, elements from a list, faces from a shape, or options to modify the way the tool operates.

There are many tools that require the selection of shapes or objects. In such cases the Task panel will wait for the user to select the appropriate objects from the [Tree view](Tree_view.md) or the [3D view](3D_view.md). When a Task panel is open, it is possible to switch to the [Tree view](Tree_view.md) to choose an object. Once this is done, it is possible to switch back to the Task panel to proceed with the tool. The Task panel is usually closed by clicking an **OK** or a **Close** button, or pressing the **Esc** key to abort the tool.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel_ArchComponent.png  style="width:250px;">



*Task panel that opens when editing an [Arch Component](Arch_Component.md). The panel waits for the user to select objects that can be added or subtracted from the component.*

## Notes

-   Users migrating from other CAD solutions that use the **ESC** key as part of their workflow may get different results in FreeCAD. When **ESC** is pressed in FreeCAD the Task panel that has the focus will close. To disable this functionality, please see [Fine tuning](Fine-tuning#Escape_key.md) and [Sketcher Preferences](Sketcher_Preferences#General.md).

 {{Interface_navi}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Task panel
