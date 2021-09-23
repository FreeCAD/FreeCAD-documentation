# Task panel/pt-br
 {{TOCright}}

## Introdução

The [task panel](Task_panel.md) appears in the **Tasks** tab of the [combo view](combo_view.md), one of the important panels of the [interface](interface.md). It is a customizable space that is able to contain any type of graphical widget like collapsible sub-windows, tables, input fields, checkboxes, spinboxes, selector boxes, text boxes, buttons, labels, images, and other elements, depending on the currently active [workbench](Workbenches.md), and the currently active tool.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="550px;">


*The task panel showing various commands when the [PartDesign Workbench](PartDesign_Workbench.md) is active, and a [sketch](Sketch.md) is selected.*

## Working with the task panel 

A task panel normally opens when a tool that requires user input is activated, either by pressing a toolbar button or double clicking on an object. If the tool doesn\'t need user input, it will produce its result or terminate, but won\'t display a task panel.

The user input may be anything such as text, 3D point coordinates, elements from a list, faces from a shape, or options to modify the way the tool operates.

![](images/FreeCAD_Combo_view_Task_panel_Sketcher.png )


*Task panel that opens when a [Sketch](Sketch.md) is being edited. Various types of information are presented like solver messages, grid options, constraints, and geometrical elements.*

There are many commands that require selection of shapes or objects present in the document; for such cases the task panel will wait for the user to select the appropriate objects from the [tree view](tree_view.md) or the [3D view](3D_view.md). When a task panel is open, it is possible to switch to the **Model** tab to display the [tree view](Tree_view.md) to choose an object; once this is done, it is possible to switch back to the **Tasks** tab to proceed with the command. The task panel is usually closed by clicking an **OK** or a **Close** button, or pressing the **Esc** key on the keyboard to abort the command.

![](images/FreeCAD_Combo_view_Task_panel_ArchComponent.png )


*Task panel that opens when editing an [Arch Component](Arch_Component.md). The panel waits for the user to select objects that can be added or subtracted from the component.*

**Note:** Please notice that switching from the **Tasks** tab to the **Model** tab does not terminate the active command; the task will still be running in the background. The user is responsible for properly terminating or aborting the active command before starting a different task; leaving a task running may produce errors when trying to launch other tools.

## Notes

-   Users migrating from other CAD solutions that use the **ESC** key as part of their workflow may get different results in FreeCAD. When **ESC** is pressed in FC if the task panel is in focus will auto-exit the task panel. To disable this functionality, please see [Escape Key](Fine-tuning#Escape_Key.md).

## Scripting


**Please reformulate and update this section**

See [forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=44170&p=376759#p376759) Call that a Task Dialog widget can use to close the Task View. It can be closed with \"this-\>close()\", but that only closes the lower part of the view, not that view itself.

Using python: 
```python
Gui.Control.closeDialog()
```

Using c++: 
```python
Gui::Control().closeDialog();
```


{{Interface navi

}} 
