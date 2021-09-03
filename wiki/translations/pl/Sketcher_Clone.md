---
- GuiCommand:
   Name:Sketcher Clone
   MenuLocation:Sketch → Sketcher tools → Clone
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Version:0.16
   SeeAlso:[Sketcher Copy](Sketcher_Copy.md), [Sketcher Move](Sketcher_Move.md)
---

## Description

Clones the selected sketch elements from one point to another, using the last selected point as reference. If any constraints are part of the source elements, then the new constraints are linked to the source constraints; if the constraints in the source are changed, the constraints in the clone are also changed. To avoid this linking see **<img src=images/Sketcher_Copy.svg style="width:16px"> [Sketcher Copy](Sketcher_Copy.md)**.

Note that a clone of a clone becomes a Sketcher Copy. If you wish to create linked constraints, clone the original source elements again.

## Usage

1.  Select the sketch elements to clone.
2.  Click on **<img src=images/Sketcher_Clone.svg style="width:16px"> <img src=images/Sketcher_Clone.svg style="width:Sketcher Clone](Sketcher_Clone.md)** or choose {{MenuCommand|Sketch → Sketcher tools  → [16px"> Clone}} from the top menu.
3.  Place clone in the [3D view](3D_view.md).

No extra constraints for clone-behaviour are added.





{{Sketcher Tools navi

}}  
