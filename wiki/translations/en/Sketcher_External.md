---
 GuiCommand:
   Name: Sketcher External
   MenuLocation: Sketch , Sketcher tools , Create external geometry
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **X**
   SeeAlso: Sketcher_ToggleConstruction
---

# Sketcher External/en

## Description


{{VersionMinus|1.0}}

: The <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Sketcher External](Sketcher_External.md) tool projects edges and/or vertices belonging to objects outside the sketch onto the sketch plane. The projected geometry is called \"external geometry\". It stays parametrically linked to its source objects. External geometry edges are marked with a dedicated [color](Sketcher_Preferences#Appearance.md) (default magenta) and (<small>(v1.0)</small> ) linetype. Similar to construction geometry, external geometry is not visible outside the sketch, it is intended to help define constraints and other geometry inside the sketch itself.


<small>(v1.1)</small> 

: See <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projection](Sketcher_Projection.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*The two magenta lines are external geometry linked to edges of a pre-existing [Pad](PartDesign_Pad.md). They are used to constrain the circles.*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_External.svg" width=16px> [Create external geometry](Sketcher_External.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_External.svg" width=16px> Create external geometry** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_External.svg" width=16px> Create external geometry** option from the context menu.
    -   Use the keyboard shortcut: **G** then **X**.
2.  The cursor changes to a cross with the tool icon.
3.  Select an external edge or a vertex. See [Notes](#Notes.md).
4.  External geometry is created.
5.  This tool always runs in continue mode: optionally keep selecting external edges and/or a vertices.
6.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   Only edges and vertices from objects within the same coordinate system can be selected. The sketch and the object must be in same [Body](PartDesign_Body.md), or the same [Part](Std_Part.md), or both in the global coordinate system. Use a [Binder](PartDesign_SubShapeBinder.md) to bring a copy of the object into the current coordinate system if required.
-   Circular dependencies are not allowed. You cannot link to an object that depends on the sketch itself.
-   Links to elements from other sketches are possible, and encouraged, as they are more reliable than links to generated (solid) geometry. The latter can suffer from the [Topological Naming Problem](Topological_naming_problem.md). See [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/en
