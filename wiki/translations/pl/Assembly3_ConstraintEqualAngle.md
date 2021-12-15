---
- GuiCommand:
   Name:Assembly3 ConstraintEqualAngle
   Icon:Assembly_ConstraintEqualAngle.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintEqualAngle/pl

## Description

This tool builds a link between two objects of an assembly and fixes one angle between them in relation to another angle\'s value. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

It can handle 3D line elements and planar face elements as well as 2D line elements within a work plane.

The line directions as well as the face normals are represented by each ICS\'s z-axis and so it actually fixes the angle between both elements\' z-axes (on basis of another angle between two z-axes).

## Usage

1.  Place two objects into an assembly
2.  Select one line element or one planar face element of each object
3.  Select two more line or one planar face elements to extract the value of the angle between them
4.  Press the **<img src="images/Assembly_ConstraintEqualAngle.svg" width=16px> [Equal angle](Assembly3_ConstraintEqualAngle.md)** button.

:   In addition the \"Flip element\" function of the elements properties panel may be needed if ICSs are not orientated as expected.

---
[documentation index](../README.md) > Assembly3 ConstraintEqualAngle/pl
