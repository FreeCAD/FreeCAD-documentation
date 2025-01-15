---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintTie
   MenuLocation: Model , Mechanical boundary conditions and loads , Tie constraint
   Workbenches: FEM_Workbench
   Version: 0.19
   SeeAlso: FEM_ConstraintPressure
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ConstraintTie/en

## Description

Defines a tie constraint that connects the two selected surfaces in such a way that (as opposed to how contact works) they can\'t separate or slide on each other throughout the analysis. Thus, the surfaces remain permanently bonded all the time.


<small>(v1.0)</small> 

: Can be also used to define cyclic symmetry.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintTie.svg" width=16px> [Tie constraint](FEM_ConstraintTie.md)** button.
    -   Select the **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintTie.svg" width=16px> Tie constraint** option from the menu.

2.  Press the **Add** button in the task panel and then click on the face you want to add to tie constraint definition. Exactly two faces have to be added, one after the other. The first selected face will be the slave face while the second one will be the master face.

3.  Optionally define Tolerance - tie constraint will be applied only to slave surface nodes separated from the master surface by a distance not larger than the one specified here.

4.  
    <small>(v1.0)</small> : Optionally check the *Enable Adjust* box to allow the slave surface nodes to be automatically moved to lie on the master surface if they are involved in the constraint (i.e. meet the tolerance criterion).

## Cyclic symmetry 


<small>(v1.0)</small> 

: Tie constraint can also be used to define cyclic symmetry. This allows the models exhibiting rotational periodic symmetry (repetitive circular patterns around a symmetry axis) to be analyzed using just a single representative sector. It can be particularly useful for rotors, shafts, turbines, fans, flywheels and similar parts, often in combination with [centrifugal load](FEM_ConstraintCentrif.md) (loading must also exhibit this form of symmetry). Cyclic symmetry can be defined by selecting the two faces of the cut for tie constraint and setting the following properties:

-    **Cyclic Symmetry**: setting to *true* activates cyclic symmetry

-    **Sectors**: total number of sectors, equal to 360° divided by the angle of the representative sector (e.g. 8 for 45° sector or 6 for 60° sector)

-    **Connected Sectors**: number of sectors displayed in results, set it to the same number as **Sectors** if you want to visualize the whole 360° part

-    **Symmetry Axis**\- axis of cyclic symmetry - global Z axis by default, can be moved by applying the Placement transformation to the Z versor (similar to what can be done with [Part Lines](Part_Line.md) - to understand how to move the symmetry axis, it might in fact be helpful to change the Placement of Part Line which is usually needed for centrifugal load anyway).

One important limitation of this feature in FEM is that boundary conditions can\'t be applied to the nodes of the slave surface of cyclic symmetry (slave surface in tie constraint definition) since that would cause an overconstraint. So in some cases, it might be necessary to remove the nodes lying on the edge between the face with the boundary condition and the slave surface of cyclic symmetry from the boundary condition definition. Unfortunately, FreeCAD doesn\'t operate on node sets and individual nodes can\'t be deselected so one would have to use workarounds like adding a narrow [face partition](FEM_Geometry_Preparation_and_Meshing#Geometry_partitioning.md) as a transition between the slave surface and the surface with the boundary condition.

## Notes

-   This feature uses the [\*TIE card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node251.html).

-    <small>(v1.0)</small> : Cyclic symmetry also uses the [\*CYCLIC SYMMETRY MODEL card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node183.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTie/en
