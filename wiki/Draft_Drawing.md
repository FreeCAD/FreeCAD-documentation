---
 GuiCommand:
   Name: Draft Drawing
   Workbenches: Drawing_Workbench, Draft_Workbench, Arch_Workbench
   SeeAlso: TechDraw_DraftView
---

# Draft Drawing

## Description

The <img alt="" src=images/Draft_Drawing.svg  style="width:24px;"> **Draft Drawing** command inserts views of selected objects into a [drawing](Drawing_Workbench.md) page.

This command is similar to the [Drawing View](Drawing_View.md) command but is optimized for [Draft](Draft_Workbench.md) objects. Contrary to that command, it can handle specific objects such as [Draft Dimensions](Draft_Dimension.md) and [Draft Texts](Draft_Text.md), and it can render faces.

This command is now obsolete. Use the [TechDraw Workbench](TechDraw_Workbench.md) and the [TechDraw DraftView](TechDraw_DraftView.md) command instead.

 <img alt="" src=images/Draft_drawing_example.jpg  style="width:640px;">  
*On the left the selected Draft objects. On the right the created drawing views.*

## Usage

1.  To use this command in FreeCAD version 0.19 and later you need to add a button to a custom toolbar. See [Interface Customization](Interface_Customization.md).
2.  Select one or more objects. A separate view will be created for each object.
3.  Optionally add a [Drawing](Drawing_Workbench.md) page to the selection. If you do not, the view is inserted into the first page in the document. If there are no pages in the document a new page is created first.
4.  Press the **<img src="images/Draft_Drawing.svg" width=16px> [Draft Drawing](Draft_Drawing.md)** button.
5.  There is a bug in the FreeCAD version 0.19 version of the command. The initial value of the **Direction** property is {{Value|[0, 0, 0]}} which is not allowed. For objects on a plane parallel to the XY plane of the global coordinate system it should be changed to {{Value|[0, 0, 1]}}. After changing this property the page and the view may need to be [recomputed](Std_Refresh.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Drawing
