---
- GuiCommand   *
   Name   *Assembly3 ConstraintLock
   Icon   *Assembly_ConstraintLock.svg
   Workbenches   *[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintLock/pl

## Description

This tool links an object to the global coordinate system (GCS) of the assembly using the implicit coordinate system (ICS) of a selected element.

   *   \- If a vertex is selected the coordinates of its ICS are fixed relative to the GCS.

       *   The object can still rotate around the vertex.
   *   \- If a (straight) edge is selected the coordinates of its ICS and the direction of its z-axis are fixed relative to the GCS.

       *   The object can still rotate around the edge.
   *   \- If a face is selected the coordinates and the orientation of its ICS are fixed relative to the GCS.

       *   The object is completely fixed to the GCS.

This can be used to define the fixed set in a static assembly as well as in a kinematic system.

## Usage

1.  Place an object into an assembly.
2.  Select one element of the object.
3.  Press the **<img src="images/Assembly_ConstraintLock.svg" width=16px> [Locked](Assembly3_ConstraintLock.md)** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintLock/pl
