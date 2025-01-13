# Sketcher MapSketch/ro
---
 GuiCommand:   Name: Sketcher MapSketch   Create a sketch on a face, PartDesign Workbench---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Acest instrument pune o schiță existentă pe fața unei forme. PartDesign features created from this sketch will be fused with the underlying solid for additive features (Pad, Revolution) or be subtracted from the underlying solid in case of subtractive features (Pocket, Groove).


</div>


<div class="mw-translate-fuzzy">

Rețineți că acest instrument nu este utilizat pentru a crea schițe noi. It only maps, or remaps an existing sketch to the face of a solid or a PartDesign feature. Typical use cases are:

-   The sketch was created on a standard plane (XY, XZ, YZ) and you want to map it to the face of a solid in order to build a feature upon it.
-   The sketch was mapped on a specific face of a solid but you need to map it to a different face.
-   Repairing a broken model.


</div>

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">

## Usage


<div class="mw-translate-fuzzy">

## Cum se utilizează 

-   Select the face of a PartDesign feature or a solid.
-   Click on the **![](images/)_[Map_sketch_to_face](Sketcher_MapSketch.md)** icon in the toolbar (or go to the PartDesign or Sketch menu depending on which workbench is active)
-   In the **Select sketch** dialog window that opens, select from the list the sketch to map to the face and click OK.
-   The sketch is automatically opened in edit mode.


</div>


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/ro
