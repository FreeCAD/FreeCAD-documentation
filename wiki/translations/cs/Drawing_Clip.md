# Drawing Clip/cs
---
- GuiCommand:   Name: Drawing Clip   Name/cs: Drawing Clip   Workbenches: [[Drawing Workbench/cs   Drawing]], Complete|MenuLocation: Drawing - Clip   Shortcut: none---

## Popis

This command allows you to place a clipping rectangle on a [Drawing page](Drawing_Landscape_A3.md). [Drawing View](Drawing_View.md) objects can then be added to that clipping rectangle, and their display will be truncated by the borders of the rectangle.

## Usage

1.  Create a [Drawing page](Drawing_Landscape_A3.md)
2.  [Refresh](Std_Refresh.md) the view if a Drawing view wasn\'t opened
3.  Press the **<img src="images/Drawing_Clip.png" width=16px> [[Drawing Clip]]** button
4.  Adjust the desired properties, such as size and position.
5.  Drag and Drop [Drawing View](Drawing_View.md) objects on the Clip object in the Tree View

## Options

-   A property allows you to show or hide the clipping rectangle itself.

## Limitations

-   Clipping objects are not displayed properly by the internal Qt-based Svg viewer, but the [Open Browser](Drawing_Openbrowser.md) command shows them correctly.


{{docnav|[Annotation](Drawing_Annotation.md)|[Open Browser](Drawing_Openbrowser.md)|[Drawing Workbench](Drawing_Workbench.md)|IconL=Drawing_Annotation.png|IconC=Workbench_Drawing.svg|IconR=Drawing_Openbrowser.png}}


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Clip/cs
