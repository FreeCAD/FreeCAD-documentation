---
- GuiCommand:
   Name: Sketcher RestoreInternalAlignmentGeometry
   Name/ro: Sketcher RestoreInternalAlignmentGeometry
   MenuLocation: Sketch -> Sketcher tools -> Show/hide internal geometry
   Workbenches: Sketcher_Workbench/ro
   Shortcut: **Ctrl**+**Shift**+**E**
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/ro




<div class="mw-translate-fuzzy">

#### Descriere

Comanda șterge elemente neutilizate în geometria internă sau recreează elementele lipsă.


</div>

The command deletes unused elements aligned to internal geometry, or recreates the missing ones.




<div class="mw-translate-fuzzy">

#### Utilizare

-   Selectați un element al unei schițe care acceptă alinierea internă (în prezent, doar Elipsa / Arc).
-   Apelați comanda făcând clic pe un buton de pe bara de instrumente, selectând elementul de meniu sau utilizând comanda rapidă de la tastatură.

Dacă există sloturi de aliniere libere pentru elementul selectat, se creează o nouă geometrie a construcției și se aliniază cu sloturile disponibile. Dacă toate locațiile de aliniere sunt ocupate, geometria internă neutilizată este ștearsă (elementul este tratat ca nefolosit dacă nu este forțat să facă altceva).


</div>

-   Select a sketch element that supports internal alignment ([Ellipse](Sketcher_CreateEllipseByCenter.md), [Arc of ellipse](Sketcher_CreateArcOfEllipse.md), [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md), [Arc of parabola](Sketcher_CreateArcOfParabola.md) or [B-spline](Sketcher_CreateBSpline.md)).
-   Invoke the command by clicking **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** or choose **Sketch → Sketcher tools → [<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> Show/hide internal geometry** or using the keyboard shortcut.

If there are free alignment places for the selected element, new construction geometry is created and aligned to the available places. If all alignment places are occupied, the unused internal geometry is deleted (the element is treated as unused if it is not constrained to anything else).




<div class="mw-translate-fuzzy">

#### Exemplu

Creați o nouă elipsă. Noi elipse sunt întotdeauna complet ambalate. Veți vedea o elipsă și o grămadă de geometrie a construcției: diametru major, diametru minor, focare.


</div>

1.  Create a new ellipse. New ellipses are always fully-packed. You\'ll see an ellipse and a bunch of construction geometry: major diameter, minor diameter, foci.
2.  Select minor diameter line and hit **Del**. The diameter is gone, but the ellipse remains. How do we get the diameter back?
3.  Select the ellipse and invoke the **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** command. The diameter is restored.
4.  Now, constrain the major diameter of the ellipse to some length. Select the ellipse and invoke the **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** command.

**Result:** Minor diameter and foci are deleted, but the major diameter is kept, because it participates in other constraints. Ellipse\'s center remains too, because it is inherent, like center of a circle.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/ro
