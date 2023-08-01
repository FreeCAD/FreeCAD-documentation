---
- GuiCommand:Addon
   Name:BIM Library
   MenuLocation:3D Modeling - Library
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench.md)
   Addon:BIM
   SeeAlso:[[Arch Equipment]]
---

# BIM Library/pl

## Description

The BIM Library tool allows you to place, in the current model, an object from the [FreeCAD Parts Library](Parts_Library.md), which must be installed via the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) for this tool to be available.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;"> 
*Above: See the '''Library browser''' dialog in the [[Task panel]] on the left*

## Usage

1.  Press the **<img src="images/BIM_Library.png" width=16px> [[BIM Library]]** button

    :   Result: In the [Combo view](Combo_view.md) → [Task panel](Task_panel.md) a dialog titled **Library browser** will display
2.  Click a file from the Library browser
3.  Double-click it or press the **Insert** button
4.  Click a point in the [3D view](3D_view.md) or enter a coordinate manually to place the object

## Options

-   [FCStd](FCStd.md), [STEP](STEP.md) and [BREP](BREP.md) files are supported. Only STEP and BREP files are placeable. FCStd files will not allow you to choose a placement, as they might be composed of a complex series of objects with significant positions. When choosing an FCStd file, its contents will be inserted at the position that is defined in the file.
-   STEP and BREP objects are inserted as <img alt="Arch Equipment" src=images/Arch_Equipment.svg  style="width:24px;"> [Equipment](Arch_Equipment.md) with no separated base shape. Adding a base shape to these objects afterwards will destroy their current shape.
-   On placing an object, you can choose their insertion point between original (the (`0,0,0`) point defined in the file), top, middle, bottom and left, center and right.
-   The Library can work offline, in which case it relies on the Parts Library addon to be installed (and updated by the user), or online, in which case it browses directly from the [Parts Library Git repository](https://github.com/FreeCAD/FreeCAD-library) and allows to download directly from there.



---
![](images/Button_right.svg) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > BIM Library/pl
