---
- GuiCommand:
   Name:Part CrossSections
   MenuLocation:Part → Cross-sections...
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Section](Part_Section.md)
---


</div>

## Descriere

Utilitarul **Cross-sections** crează una sau mai multe secțiuni transversale prin forma selectată.

## Cum se folosește 

1.  Select a shape.
2.  Press the **<img src=images/Part_SectionCross.png style="width:24px"> '''Cross-sections'''** button.
3.  Define the guiding plane.
4.  Define the position (height of the cross-section).
5.  Optionally, check **Sections** to create more than one cross-section:
    -   Checking *On both sides* will distribute the cross-sections on each side of the guiding plane location.
    -   Set the count.
6.  Press **OK**.

## Limite

-   The resulting object is not parametric, that is it is not linked to the original shape.
-   A single object is created, even with more than one cross-section.

## Exemplu

![Select an object](images/SectionCross1.png )

![Dialog window](images/SectionCross2.png )

![Result](images/SectionCross3.png )





  
