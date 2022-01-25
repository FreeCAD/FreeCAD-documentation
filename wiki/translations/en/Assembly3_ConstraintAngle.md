---
- GuiCommand:
   Name:Assembly3 ConstraintAngle
   Icon:Assembly_ConstraintAngle.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintAngle/en

## Description

This tool builds a link between two objects of an assembly and matches their orientation. The selected elements of each object or more precisely their implicit coordinate systems (ICS) are used to position one object to another.

The angle between two elements i.e. the angle between their z-axes is fixed.

The offset of their origins in x-, y- and z-direction and the angles between the x-, and y-axes are not defined. Related to the first object the following object can still move along the x-, y- and z-axis and spin around both z-axes. This is leaving 5 degrees of freedom (DOFs) for each link unconstrained.

The constraint accepts straight edges and planar faces.

## Usage

1.  Place two or more objects into an assembly.
2.  Select one straight edge element or one planar face element of each object.
3.  Press the **<img src="images/Assembly_ConstraintAngle.svg" width=16px> [Angle](Assembly3_ConstraintAngle.md)** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintAngle/en
