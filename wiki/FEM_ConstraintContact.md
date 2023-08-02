---
- GuiCommand:
   Name: FEM ConstraintContact
   MenuLocation: Model -> Mechanical Constraints -> Constraint contact
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintFixed
---

# FEM ConstraintContact

## Description

Creates a FEM constraint for contact between 2 surfaces.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintContact.svg" width=16px> [FEM ConstraintContact](FEM_ConstraintContact.md)** button.
    -   Select the **Model → Mechanical Constraints → <img src="images/FEM_ConstraintContact.svg" width=16px> Constraint contact** option from the menu.
2.  Select the master face.
3.  Select the slave face.
4.  Enter a contact stiffness.
5.  Enter a friction coefficient.

## Limitations

-   The contact constraint can only be applied to two faces.
-   Development for multiple contact at once: <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=130#p303275>
-   Because multiple meshes are currently not supported, contact must be applied to faces that are separated by (at least) a small distance. If the faces were touching (no gap between them), the result of a boolean union or boolean fragments operation (necessary to avoid having multiple meshes which is not allowed at the moment) would be a continuous mesh and thus no need to use contact anymore. See [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=62307).

## Notes

### Tips for modeling 

-   from <https://forum.freecadweb.org/viewtopic.php?f=18&p=340874#p340494>
-   Better use linear elements otherwise calculations are very time consuming
-   master/slave assignment:
    -   The larger of the two surfaces should act as the master surface.
    -   If the surfaces are of comparable size, the surface on the stiffer body should act as the master surface.
    -   If the surfaces are of comparable size and stiffness, the surface with the coarser mesh should act as the master surface.

### CalculiX

-   The contact stiffness should be 10 times the young\'s modulus of the material for hard contact. The higher the value for contact stiffness, the harder the contact between surfaces.
-   The slave face is the face which penetrates into the master face, and therefore experiences more deformation.
-   The \*CONTACT PAIR card is used for modeling contact in CalculiX. The constraint uses Face-to-Face penalty contact and the contact formulation is explained in detail at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node112.html>
-   Overview for different contact types: <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=90#p188736>
-   Further interesting informations:
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=23102#p180709> and following posts !!!
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=20276>
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=21331>
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699> (initial contact topic)

-   A very detailed CalculiX contact example. ([link](http://dip28p.web.fc2.com/calculix/netgen2calculix/index.html))

-   A very cool example found in the FreeCAD German subforum. ([link](https://forum.freecadweb.org/viewtopic.php?f=13&t=39663&start=10#p337254))




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintContact
