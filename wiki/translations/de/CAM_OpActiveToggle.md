---
 GuiCommand:
   Name: CAM OpActiveToggle
   MenuLocation: CAM , Toggle the Active State of the Operation
   Workbenches: CAM_Workbench
   Shortcut: **P** **X **
---

# CAM OpActiveToggle/de



## Beschreibung

The <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:24px;"> [Active](CAM_OpActiveToggle.md) tool in the <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [CAM Workbench](CAM_Workbench.md) is used to toggle the active state of an existing path operation.

This tool can only be used if your <img alt="" src=images/CAM_Job.svg  style="width:24px;"> [Job](CAM_Job.md) has at least one path operation.



## Anwendung

1.  Select an operation in the **Operations** group belonging to a Job. A deactivated operation can be recognized by its grayed out label and icon.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/CAM_OpActiveToggle.svg" width=16px> [CAM OpActiveToggle](CAM_OpActiveToggle.md)** button.
    -   Select the **CAM → <img src="images/CAM_OpActiveToggle.svg" width=16px> Toggle the Active State of the Operation** option from the menu.
    -   Use the keyboard shortcut: **P** then **X**.
3.  The result depends on the selected operation:
    -   If you have selected an active operation the command deactivates it:
        -   The operation icon is replaced with the command icon: <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:16px;">.
        -   The operation icon and label are grayed out.
        -   The paths generated from the operation disappear from the [3D view](3D_view.md).
        -   When using the <img alt="" src=images/CAM_Inspect.svg  style="width:16px;"> [CAM Inspect](CAM_Inspect.md) command or the <img alt="" src=images/CAM_Post.svg  style="width:16px;"> [CAM Post](CAM_Post.md) command, the operation\'s G-code is not provided.
    -   If you have selected a deactivated operation the command activates it:
        -   The operation icon is replaced with that belonging to the operation.
        -   The operation icon and label are no longer grayed out.
        -   The paths generated from the operation are recomputed and displayed in the [3D view](3D_view.md).
        -   When using the <img alt="" src=images/CAM_Inspect.svg  style="width:16px;"> [CAM Inspect](CAM_Inspect.md) command or the <img alt="" src=images/CAM_Post.svg  style="width:16px;"> [CAM Post](CAM_Post.md) command, the operation\'s G-code is provided.



## Optionen

Empty



## Eigenschaften

Empty



## Skripten


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM OpActiveToggle/de
