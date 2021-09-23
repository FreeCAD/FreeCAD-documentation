---
- GuiCommand:
   Name:Assembly3 ConstraintCoincidence
   Icon:Plane_Coincidence.svg
   Icon:Assembly ConstraintCoincidence.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintCoincidence

## Description

This tool links two or more objects of an assembly and matches their orientations. The selected elements of each object or more precisely their implicit coordinate systems (ICSs) are used to position one object in relation to another.

Assuming the first object is already locked in place by the <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Lock constraint](Assembly3_ConstraintLock.md) then the following objects are moved to positions where the x-y-planes of all ICSs are coplanar and the z-axes are collinear.

An option for this link is to set a distance between the x-y-planes and making them parallel.

The angle between their x-axes (and y-axes as well) are not defined. Related to the first object the following objects can still spin around the z-axis. This is leaving 1 degree of freedom (DOF) for each link unconstrained.

This link can be used as a hinge in kinematics.

The rotation can be stopped by switching Lock Angle to true in the properties panel and the angle can be set to a specific value. With controlled value the link can be used as an actuator in a kinematic system.

## Usage

1.  Place two or more objects into an assembly.
2.  Select one planar face element of each object.
3.  Press the **<img src="images/Assembly_ConstraintCoincidence.svg" width=16px> [Plane Coincidence](Assembly3_ConstraintCoincidence.md)** button.

---
[documentation index](../README.md) > Assembly3 ConstraintCoincidence
