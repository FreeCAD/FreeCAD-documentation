---
- GuiCommand:
   Name:Path OpActiveToggle
   MenuLocation:Path → Toggle the Active State of the Operation
   Workbenches:[Path](Path_Workbench.md)
   Shortcut:**P** **X **
---

# Path OpActiveToggle/it

## Descrizione

The **<img src="images/Path_OpActiveToggle.svg" width=24px> [Active](Path_OpActiveToggle.md)** tool in the <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Path Workbench](Path_Workbench.md) is used to toggle the active state of an existing path operation. This tool is not available, indicated as a light gray version of the icon, until you have created one or more path operations. Once your <img alt="" src=images/Path_Job.svg  style="width:24px;"> [Job](Path_Job.md) has at least one path operation the icon will be fully colored indicating it is available for use.

## Usage

1.  Select an operation in the **Operations** group belonging to a Job. A deactivated operation can be recognized by its grayed out label and icon.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Path_OpActiveToggle.svg" width=16px> [Path OpActiveToggle](Path_OpActiveToggle.md)** button.
    -   Select the **Path → <img src="images/Path_OpActiveToggle.svg" width=16px> Toggle the Active State of the Operation** option from the menu.
    -   Use the keyboard shortcut: **P** then **X**.
3.  The result depends on the selected operation:
    -   If you have selected an active operation the command deactivates it:
        -   The operation icon is replaced with the command icon: <img alt="" src=images/Path_OpActiveToggle.svg  style="width:16px;">.
        -   The operation icon and label are grayed out.
        -   The paths generated from the operation disappear from the [3D view](3D_view.md).
        -   When using the <img alt="" src=images/Path_Inspect.svg  style="width:16px;"> [Path Inspect](Path_Inspect.md) command or the <img alt="" src=images/Path_Post.svg  style="width:16px;"> [Path Post](Path_Post.md) command, the operation\'s G-code is not provided.
    -   If you have selected a deactivated operation the command activates it:
        -   The operation icon is replaced with that belonging to the operation.
        -   The operation icon and label are no longer grayed out.
        -   The paths generated from the operation are recomputed and displayed in the [3D view](3D_view.md).
        -   When using the <img alt="" src=images/Path_Inspect.svg  style="width:16px;"> [Path Inspect](Path_Inspect.md) command or the <img alt="" src=images/Path_Post.svg  style="width:16px;"> [Path Post](Path_Post.md) command, the operation\'s G-code is provided.

## Options

Empty

## Properties

Empty

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path OpActiveToggle/it
