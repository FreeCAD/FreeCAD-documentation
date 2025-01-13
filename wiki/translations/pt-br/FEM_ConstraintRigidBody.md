---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintRigidBody
   MenuLocation: Model , Mechanical boundary conditions and loads , Rigid body constraint
   Workbenches: FEM_Workbench
   Version: 1.0
   SeeAlso: FEM_ConstraintDisplacement
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ConstraintRigidBody/pt-br


</div>



## Descrição


<div lang="en" dir="ltr" class="mw-content-ltr">

Defines the CalculiX\'s rigid body constraint that constrains the motion of the nodes of a selected geometrical entity to the motion of a reference node whose location is defined by the user. In practice, this can be used to apply a boundary condition or load that will be propagated to the selected object. Since the reference node has rotational degrees of freedom, it\'s possible to apply a moment load or a rotational boundary condition to any face this way. The location of the reference node can be selected, if it\'s offset from a geometrical entity, a remote load (a force acting on a lever) can be applied.


</div>



## Utilização


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintRigidBody.svg" width=16px> [Rigid body constraint](FEM_ConstraintRigidBody.md)** button.
    -   Select the **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintRigidBody.svg" width=16px> Rigid body constraint** option from the menu.
2.  Press the **Add** button.
3.  In the [3D view](3D_view.md) select the geometrical element(s) (vertices, edges or faces but not a mix of them) to which the constraint should be applied. To remove objects from the selection, press the **Remove** button and click on them.
4.  Specify the coordinates of the reference node. After closing the task panel, a spherical symbol will show this location.
5.  Choose modes for the 3 translational and 3 rotational degrees of freedom (DOFs):
    -   *Free* - default, no boundary condition or load on that DOF
    -   *Constraint* - displacement/rotation boundary condition with a specified value (default: 0 = fixed) on that DOF - for rotation, one needs to set an axis (X, Y or Z) and specify the *Angle*
    -   *Load* - force/moment load with a specified value on that DOF


</div>



## Limitações


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Currently, the moment units can be somewhat confusing. To apply 1 N\*m, one needs to set 1 J in the input field (those units are equivalent).
-   The feature can be applied only to vertices, edges and faces for now, support for solids (to make whole volumes/parts rigid) should follow in the future.
-   The selected object is made rigid. To apply loads in a more flexible way, one would need to use CalculiX\'s distributing coupling constraints which are currently unsupported.


</div>



## Notas


<div lang="en" dir="ltr" class="mw-content-ltr">

-   This constraint is the standard way of applying torque to arbitrary parts. The other options are the [Local coordinate system](FEM_ConstraintTransform.md) (only for cylindrical faces) or a pair of forces but the rigid body constraint should be sufficient in pretty much all the cases.
-   No other constraints/boundary conditions should be applied to the nodes involved in a rigid body constraint.
-   When applying this constraint to a vertex or an edge, one should set a proper rotational DOF (in the case of an edge, the one that will prevent the rotation about it) to zero.
-   This feature uses the [\*RIGID BODY card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node236.html).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintRigidBody/pt-br
