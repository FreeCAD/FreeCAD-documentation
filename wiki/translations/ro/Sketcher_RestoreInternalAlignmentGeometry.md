---
 GuiCommand:
   Name: Sketcher RestoreInternalAlignmentGeometry
   Name/ro: Sketcher RestoreInternalAlignmentGeometry
   MenuLocation: Sketch , Sketcher tools , Show/hide internal geometry
   Workbenches: Sketcher_Workbench/ro
   Shortcut: **Ctrl**+**Shift**+**E**
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/ro


</div>




<div class="mw-translate-fuzzy">

#### Descriere

Comanda șterge elemente neutilizate în geometria internă sau recreează elementele lipsă.


</div>

The <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:24px;"> [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md) tool deletes the internal geometry of elements, or recreates missing internal geometry. The tool does not delete internal geometry that has associated constraints.




<div class="mw-translate-fuzzy">

#### Utilizare

-   Selectați un element al unei schițe care acceptă alinierea internă (în prezent, doar Elipsa / Arc).
-   Apelați comanda făcând clic pe un buton de pe bara de instrumente, selectând elementul de meniu sau utilizând comanda rapidă de la tastatură.

Dacă există sloturi de aliniere libere pentru elementul selectat, se creează o nouă geometrie a construcției și se aliniază cu sloturile disponibile. Dacă toate locațiile de aliniere sunt ocupate, geometria internă neutilizată este ștearsă (elementul este tratat ca nefolosit dacă nu este forțat să facă altceva).


</div>

1.  Select one or more sketch elements that support internal geometry ([ellipse](Sketcher_CreateEllipseByCenter.md), [arc of ellipse](Sketcher_CreateArcOfEllipse.md), [arc of hyperbola](Sketcher_CreateArcOfHyperbola.md), [arc of parabola](Sketcher_CreateArcOfParabola.md) or [B-spline](Sketcher_CreateBSpline.md)).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_RestoreInternalAlignmentGeometry.svg" width=16px> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** button.
    -   Select the **Sketch → Sketcher visual → <img src="images/Sketcher_RestoreInternalAlignmentGeometry.svg" width=16px> Show/hide internal geometry** option from the menu.
    -   Use the keyboard shortcut: **Z** then **I**.
3.  Internal geometry is deleted for selected elements with a complete set of internal geometry, else missing internal geometry is recreated.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/ro
