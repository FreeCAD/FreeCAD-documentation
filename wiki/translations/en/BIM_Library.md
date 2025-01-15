---
 GuiCommand:
   Name: BIM Library
   MenuLocation: 3D/BIM , Generic 3D tools , Objects library
   Workbenches: BIM_Workbench
---

# BIM Library/en

## Description

The **BIM Library** tool allows you to place, in the current model, an object from the [Parts Library](Parts_Library_Workbench.md), which must be installed via the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) for this tool to be available.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:600px;"> 
*The '''Library browser''' dialog in the [Task panel](Task_panel.md) on the left*

## Usage

1.  Press the **<img src="images/BIM_Library.svg" width=16px> [Objects library](BIM_Library.md)** button

    :   Result: In the [Combo view](Combo_view.md) → [Task panel](Task_panel.md), a dialog titled **Library browser** is displayed
2.  Click a file from the Library browser
3.  Double-click it or press the **Insert** button
4.  Click a point in the [3D view](3D_view.md) or enter a coordinate manually to place the object

## Options

-   [FCStd](File_Format_FCStd.md), STEP and [brep](File_Format_FCStd#*.brep.md) files are supported. Only STEP and BREP files are placeable. FCStd files will not allow you to choose a placement, as they might be composed of a complex series of objects with significant positions. When choosing an FCStd file, its contents will be inserted at the position that is defined in the file.
-   STEP and BREP objects are inserted as <img alt="" src=images/Arch_Equipment.svg  style="width:24px;"> [Equipment](Arch_Equipment.md) with no separated base shape. Adding a base shape to these objects afterwards will destroy their current shape.
-   On placing an object, you can choose their insertion point between original (the (`0,0,0`) point defined in the file), top, middle, bottom and left, center and right.
-   The Library can work offline, in which case it relies on the Parts Library addon to be installed (and updated by the user), or online, in which case it browses directly from the [Parts Library Git repository](https://github.com/FreeCAD/FreeCAD-library) and allows to download directly from there.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Library/en
