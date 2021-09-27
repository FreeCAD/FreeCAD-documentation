---
- GuiCommand:
   Name:Part CrossSections
   MenuLocation:Part → Cross-sections...
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Section](Part_Section.md)
---

# Part CrossSections/en

## Description

The **Cross-sections** utility creates one or more cross-sections through the selected shape.

## Usage

1.  Select a shape.
2.  Press the **_ '''Cross-sections'''** button.
3.  Define the guiding plane.
4.  Define the position (height of the cross-section).
5.  Optionally, check **Sections** to create more than one cross-section:
    -   Checking *On both sides* will distribute the cross-sections on each side of the guiding plane location.
    -   Set the count.
6.  Press **OK**.

## Limitations

-   The resulting object is not parametric, that is it is not linked to the original shape.
-   A single object is created, even with more than one cross-section.

## Example

![Select an object](images/SectionCross1.png )

![Dialog window](images/SectionCross2.png )

![Result](images/SectionCross3.png )

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part CrossSections/en
