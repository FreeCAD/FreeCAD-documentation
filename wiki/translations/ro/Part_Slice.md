---
- GuiCommand:
   Name:Part Slice
   MenuLocation:Part → Split → Slice to compound
   Workbenches:[Part](Part_Workbench.md)
   Version:0.17
   SeeAlso:[Part Boolean Fragments](Part_BooleanFragments.md), [Part XOR](Part_XOR.md), [Part Join features](Part_CompJoinFeatures.md), [Part Boolean](Part_Boolean.md)
---

# Part Slice/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Este un instrument pentru a împărți forme prin intersecția cu alte forme. De exemplu, pentru o cutie și un plan, este creat un compus de două solide.


</div>

![600px](images/Part_Slice_Demo.png)


<div class="mw-translate-fuzzy">

(on the picture above, the pieces were moved apart manually afterwards, to reveal the slicing)


</div>

There are two commands to slice a shape: <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part Slice apart](Part_SliceApart.md) and <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part Slice to compound](Part_Slice.md). They both create a \'Slice\' parametric feature, that puts the sliced pieces into a compound. However, <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part Slice Apart](Part_SliceApart.md) explodes the resulting compound into separate objects. \"Slice to compound\" is fully-parametric, and causes no trouble as the number of pieces changes. \"Slice apart\" will not update the number of objects as the number of pieces changes.


<div class="mw-translate-fuzzy">

The output shape occupies the same space as the original. But it is split where it intersects with other shapes. The split pieces are put into a compound (or compsolid), so the object appears to remain in one piece. You need to explode the compound to get the individual pieces. If you want to access the individual pieces in a parametric way you can use [Part CompoundFilter](Part_CompoundFilter.md) for the purpose. For quick non parametric access use [Draft Downgrade](Draft_Downgrade.md).


</div>


<div class="mw-translate-fuzzy">

The tool has three modes: \"Standard\", \"Split\", and \"CompSolid\".


</div>

\"Standard\" and \"Split\" differ by the action of the tool on wires, shells and compsolids: if \"Split\", those are separated; if \"Standard\", they are kept together (get extra segments).

Compounding structure in \"Standard\" and \"Split\" modes follows the compounding structure of shape being sliced.

In \"CompSolid\" mode, the output is a compsolid (or a compound of compsolids, if the resulting solids form more than one island of connectedness). Compsolid is a set of solids connected by faces; they are related to solids like wires are related to edges, and shells are related to faces; the name is probably a shortened phrase \"composite solid\".


<div class="mw-translate-fuzzy">

The overall action of the tool is very similar to [Boolean Fragments](Part_BooleanFragments.md), except only the pieces from the first shape are in the result.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cu se folosește 

1.  Select the object to be sliced, first, and then some objects to slice with.
    The order of selection is important. Compounds with self-intersections are not allowed (self-intersections sometimes can be accounted for by passing the compound through [BooleanFragments](Part_BooleanFragments.md))
2.  Invoke the Part Slice command.


</div>

1.  Noteː The Objects to slice with must completely separate the object to be sliced. Thus a cube cannot be sliced by a wire, but by a plane derived from an extruded wire for instance.


<div class="mw-translate-fuzzy">

A Slice parametric object is created. Original objects are hidden, and the result of intersection is shown in 3D view.


</div>

### Tree structure of Slice 

The Slice command creates a sliced object. In the following example a cube is sliced by a face.

The slice is created and each piece of it is united in a Compound.

![](images/Part_SliceTree.png )

## Properties


<div class="mw-translate-fuzzy">

## Proprietăți


{{TitleProperty|Slice}}

-    **Base**: Object to be sliced.

-    **Tools**: List of objects to slice with. (as of FreeCAD v0.17.8053, this property is not displayed in property editor, and can only be accessed via Python).

-    **Mode**: \"Standard\", \"Split\", or \"CompSolid\". \"Split\" is default. Standard and Split differ by the action of the tool on aggregation type shapes: if Split, those are separated; otherwise they are kept together (get extra segments).

-    **Tolerance**: \"fuzziness\" value. This is an extra tolerance to apply when searching for intersections, in addition to tolerances stored in the input shapes.


</div>

̈Noteː Properties are accessible on the slices inner object, not on the result level.




<div class="mw-translate-fuzzy">

## Exemple: making puzzle 

1.  Switch to [Sketcher Workbench](Sketcher_Workbench.md), create an new sketch. Draw a rectangle that will outline the overall shape of the puzzle. Close the sketch.
    ![320px](images/slice_example_step1.png)
2.  Switch to [Part workbench](Part_Workbench.md). Select the sketch, and pick Part-\>Create face from sketch (in menu).
    ![320px](images/slice_example_step2.png)
3.  Switch to Sketcher workbench, and create another sketch on the same plane. Using polyline tool, draw the lines that will split the puzzle into pieces.
    ![320px](images/slice_example_step3.png)
4.  Switch to Part workbench. Select the splitter sketch, and apply [Part Boolean Fragments](Part_BooleanFragments.md). This will insert vertices where lines of splitter sketch intersect. Having them is essential for the next step to work.
    ![320px](images/slice_example_step4.png)
5.  Select the rectangular face, and the BooleanFragments of splitter sketch, and apply Part Split.
    ![320px](images/slice_example_step5.png)
6.  Switch to Draft workbench, and apply Draft Downgrade to the result. You should get all the pieces as \"Face00X\" in document tree, that can be moved independently. Done!
    ![320px](images/slice_example_step6.png)


</div>

### Creating a Puzzle 

1.  Switch to <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md)
    -   Create a new sketch.
    -   Draw a rectangle that will outline the overall shape of the puzzle.
    -   Close the sketch.
        ![320px](images/slice_example_step1.png)
2.  Switch to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part workbench](Part_Workbench.md).
    -   Select the sketch, and pick **Part → <img src="images/Part_MakeFace.svg" width=24px> [Make face from wires](Part_MakeFace.md)**.
        ![320px](images/slice_example_step2.png)
3.  Switch back to <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md)
    -   Create another sketch on the same plane.
    -   Using polyline tool, draw the lines that will split the puzzle into pieces.
        ![320px](images/slice_example_step3.png)
4.  Switch back to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).
    -   Select the splitter sketch, and apply <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Part Boolean Fragments](Part_BooleanFragments.md). This will insert vertices where lines of splitter sketch intersect. Having them is essential for the next step to work.
        ![320px](images/slice_example_step4.png)
5.  Select the rectangular face, and the BooleanFragments of splitter sketch, and apply <img alt="" src=images/Part_Slice.svg  style="width:24px;"> Part Slice.
    ![320px](images/slice_example_step5.png)
6.  Use <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> [Part ExplodeCompound](Part_ExplodeCompound.md) on the sliced face, to break apart the compound made by Part Slice into individual pieces.

**Note:** Steps 5 and 6 can be done in single click using <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part SliceApart](Part_SliceApart.md)

## Notes


<div class="mw-translate-fuzzy">

## Versiune

Acest instrument a fost introdus în FreeCAD v0.17.8053. FreeCAD și necesită compilarea cu OCC 6.9.0 sau mai recent; altfel instrumentul este inutilizabil.


</div>



## Scrip-Programare 


<div class="mw-translate-fuzzy">

Instrumentul poate fi utilizat în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>


```pythonBOPTools.SplitFeatures.makeSlice(name)```

-   Creates an empty Slice feature. The \'Base\' and \'Tools\' properties must be assigned explicitly, afterwards.
-   Returns the newly created object.

Slice poate fi, de asemenea, aplicat la forme simple, fără a fi nevoie să aibă un obiect de document, prin: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` This can be useful for making custom Python scripted features. Acest lucru poate fi util pentru crearea de funcții(onalități) script-Programare personalizate Python.

Example: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}


<div class="mw-translate-fuzzy">

Instrumentul propriu-zis este implementat în Python, vezi /Mod/Part/BOPTools/SplitFeatures.py unde este instalat FreeCAD.


</div>

## Tutorials

-   [FreeCad 0.18 Part WB using Slice and Slice Apart](https://www.youtube.com/watch?v=tzHkQaHgrfQ) (English language), author: Ha Gei

-   [FreeCAD Slice und Slice Apart und andere Tricks](https://www.youtube.com/watch?v=JJAL5JmqqKQ) (German language), author: Ha Gei



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Slice/ro
