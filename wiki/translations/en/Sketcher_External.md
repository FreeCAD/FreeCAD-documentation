---
 GuiCommand:
   Name: Sketcher External
   MenuLocation: Sketch , Sketcher geometries , Create external geometry
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **X**
   SeeAlso: Sketcher_ToggleConstruction
---

# Sketcher External/en

## Description

Use the **<img src="images/Sketcher_External.svg" width=16px> [Create external geometry](Sketcher_External.md)** tool when you need to apply a constraint between sketch geometry and something outside of the sketch. It works by inserting a linked construction geometry into the sketch. The default colour of externally linked edges is magenta. As with standard non-linked construction geometry (blue), the externally linked geometry is only visible when the sketch is in edit mode and is not directly used in the subsequent result from use of the sketch in another tool. Both types of construction geometry may be used as a reference for constraints within the sketch.

A note of caution, using this tool to link to generated (solid) geometry can lead to unexpected results due to [Topological Naming Problem](Topological_naming_problem.md). Also see [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).

<FILE:Sketcher_ExternalEsempio1.png>

## Usage

-   Create a new sketch, or open an existing sketch.
-   Press the **[<img src=images/Sketcher_External.svg style="width:16px"> [Create external geometry](Sketcher_External.md)** button.
-   Select an edge or a vertex that you want to link to in the sketch.
-   Press **Esc**, or select another tool to stop importing geometry into the sketch.

### Selection rules 

-   Only edges and vertices from objects from same coordinate system are allowed.

That is, the sketch and the object must be in same Body (when in Part Design workbench), or in same Part (when in Part workbench), or both outside of any Parts and Bodies.

For example, If the open sketch is in Body, you can use another sketch from Body as external geometry, but you can\'t use a sketch from Body001, or an edge from a Part Cube in the root of the project. Use Shapebinder feature to bring in a copy of the object into the coordinate system of open sketch. Then you will be able to use edges/vertices of Shapebinder object.

-   No circular dependencies are allowed.

That means, you can\'t link to Pocket made with this sketch. You can\'t link to any object that depends on the sketch.

Sketch doesn\'t have to be on any face in order to use this tool. Links directly between sketches are possible, and encouraged, as they are more reliable.

### Appearance When Successfully Linked 

A (default magenta) coloured line will be overlaid when an edge is successfully linked (the vertices will be red), and will be visible in your sketch only while your sketch is in edit mode.

### Similarity to Construction Lines 

External geometry (default colour magenta) lines are similar (default colour blue) [Contruction lines](Sketcher_ToggleConstruction.md) except in that the external geometry magenta lines are parametrically linked back to an element of the solid to which the sketch is mapped. Construction geometry are lines that are internal to the sketch, are only visible when the sketch is in edit mode and will be used for constraint references only, and not directly for later solid operations, like Pad or Pocket.

### Use Of External Geometry in a PartDesign Workbench Work Flow 

In the PartDesign workbench work flow, the External Geometry tool is used to assist in the positioning of an aspect of the solid you are constructing, relative to the previous stage in its construction. PartDesign workbench is intended to produce one single solid, therefore these sketches with external geometry are used to create a new feature of that one single solid.

The external geometry can, for example, be used as a reference for a constraint being used to position a hole in an object at a specific location relative to an edge or vertex.

### Use Of External Geometry in a Part Workbench Work Flow 

You can use any Part geometry that is in coordinate system of the sketch. It is advised to link to the earliest feature possible, as it forms a more stable link.

## Example

This, below, is a sketch mapped to the top face of a solid created from a Pad of a previous sketch. The magenta lines are External Geometry linked to two edges of this pre-existing Pad.

In this case they are used as a reference for tangency constraints with the circumferences of one circle. They are also used as the reference for a horizontal and a vertical constraint to locate the centre of the second circle relative to the end and top of the Pad.

<FILE:Sketcher_ExternalEsempio2.png>

This is the same sketch in edit mode, with the Pad upon which it is mapped hidden.

<FILE:Sketcher_ExternalEsempio4.png>

When the sketch edit mode is closed, external Geometry lines are not visible.

<FILE:Sketcher_ExternalEsempio3.png>





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/en
