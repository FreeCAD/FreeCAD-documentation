---
 GuiCommand:
   Name: FEM ConstraintPlaneRotation
   MenuLocation: Model , Geometrical analysis features , Plane multi-point constraint
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintTransform
---

# FEM ConstraintPlaneRotation/de



## Beschreibung

Creates a FEM multi-point constraint (MPC) for keeping the nodes on a planar surface on the same plane.



## Anwendung

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> [Plane multi-point constraint](FEM_ConstraintPlaneRotation.md)** button.
    -   Select the **Model → Geometrical analysis features → <img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> Plane multi-point constraint** option from the menu.
2.  In the [3D view](3D_view.md) select the object the multi-point constraint should be applied to, which can be a face.

## Limitations

1.  Plane multi-point constraint can only be applied to a single planar face.
2.  When a plane multi-point constraint is applied to the same face as a displacement/fixed boundary condition, the displacement/fixed boundary condition takes precedence.



## Hinweise

1.  The constraint uses the \*MPC card in CalculiX. The card is explained in detail at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation/de
