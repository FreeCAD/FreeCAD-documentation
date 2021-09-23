---
- GuiCommand:
   Name:Part Tube
   MenuLocation:Part → Primitives → Create tube
   Workbenches:[Part](Part_Workbench.md)
   Version:0.19
   SeeAlso:[Part CreatePrimitives](Part_CreatePrimitives.md)
---

# Part Tube/pt-br

## Description

The Tube command inserts a tube into the active document. The tube is geometrically treated as a cut of a smaller cylinder into a larger one. By default, the command will insert a 10 mm high tube with an outer radius of 5 mm and an inner radius of 2 mm. These parameters can be modified after the object has been added.

![Screenshot of a Tube](images/Part_Tube-screenshot.png )

## Usage

To create a tube either:

-   press the **<img src="images/Part_Tube.svg" width=16px> '''Tube'''** button in the toolbar
-   use the menu **Part → Primitives → Create tube**

To edit the tube

-   either
    -   select it in the tree and double-click on it
    -   edit the parameters in the appearing dialog
-   or use the the [ property editor](Property_editor.md) to edit the parameters

## Properties

-   Via the [ Property Editor](Property_editor.md):
    -   **Height:** Sets the height (default is 10 mm).
    -   **Inner Radius:** Set the inner radius (default is 2 mm).
    -   **Outer Radius:** Set the outer radius (default is 5 mm).
    -   **Placement:** Specifies the orientation and position of the Box in the 3D space. See [ Placement](Placement.md). The reference point is the left front lower corner of the box.
    -   **Label:** The Label is the name given to the operation. This name can be changed at your convenience.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Tube/pt-br
