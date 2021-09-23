# Sketch/ko


## Introduction


{{TOCright}}

In FreeCAD the word \"[Sketch](Sketch.md)\" is normally used to refer to a [Sketcher SketchObject](Sketcher_SketchObject.md) (`Sketcher::SketchObject` class) that is defined by the [Sketcher Workbench](Sketcher_Workbench.md). This is a 2D drawing that uses mathematical constraints to describe 2D geometry precisely.

See [Sketcher SketchObject](Sketcher_SketchObject.md) for more information about this type of object.

## Usage

There are two common ways to create a Sketch: using the [Sketcher Workbench](Sketcher_Workbench.md) directly, or through the [PartDesign Workbench](PartDesign_Workbench.md).

### Sketcher Workbench 

1.  Switch to the <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher Workbench](Sketcher_Workbench.md).
2.  Press **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher NewSketch](Sketcher_NewSketch.md)**.

### PartDesign Workbench 

1.  Switch to the <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md).
2.  Press **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.
3.  Press **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)**.

After you finish editing the sketch, close it to go out of edit mode. Double click on it to enter edit mode again.

## Notes

A Sketch is very commonly used in conjunction with the <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> <img src=images/PartDesign_Pad.svg style="width:PartDesign Workbench](PartDesign_Workbench.md) to create solids by extrusion, using the **[16px"> [PartDesign Pad](PartDesign_Pad.md)** operation.

Nevertheless, a Sketch can always be created by itself for any other purpose; it does not have to be tied to a <img src=images/Arch_Window.svg style="width:PartDesign Body](PartDesign_Body.md). For example, the **[16px"> <img src=images/Arch_Wall.svg style="width:Arch Window](Arch_Window.md)** tool of the <img alt="" src=images/Workbench_Arch.svg  style="width:16px;"> [Arch Workbench](Arch_Workbench.md) uses Sketches to define the shapes of windows and doors; in the same way, they can be used to define the shape of **[16px"> [Arch Walls](Arch_Wall.md)**.


{{Sketcher Tools navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
