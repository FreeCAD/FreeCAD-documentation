---
- GuiCommand:
   Name:PartDesign Fillet
   MenuLocation:PartDesign → Apply a dress-up feature → Fillet
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   SeeAlso:[PartDesign Chamfer](PartDesign_Chamfer.md), [Part Fillet](Part_Fillet.md)
---

# PartDesign Fillet/pl

## Description

This tool creates fillets (rounds) on the selected edges of an object. A new separate Fillet entry (followed by a sequential number if there are already existing fillets in the document) is created in the project tree.

## Usage

-   Select a single or multiple edges or a face on an object, then start the tool either by clicking its icon or going into the menu. In case you selected a face or a 3D object (<small>(v0.20)</small> ) all its edges are respected for filleting.
-   In the appearing [Task panel](Task_panel.md) set the fillet radius either by entering the value, or by clicking on the up/down arrows.
-   If you want to add more edges or faces click the **Add** button and select edges and/or the faces.
-   After clicking the **Add** button you can add all edges of the object by right-clicking and selecting **Add all edges** from the context menu. <small>(v0.20)</small> 
-   If you want to remove edges or faces
    -   either select the edge/face in the list of the dialog and press the **DEL** key. *Note*: Since there must be at least one edge for the feature, the last remaining edge or face in the list cannot be removed.
    -   or click the **Remove** button. All edges and faces being previously selected are highlighted in purple. Select the edge or the face to be removed.
-   Click **OK** to validate.
-   For a chain of edges tangential to one another, one single edge can be selected; the fillet will propagate along the chain.
-   To edit the fillet after the function has been validated, either double-click on the Fillet label in the Project tree, or right-click on it and select **Edit Fillet**.

## Notes

-   PartDesign Fillet should not be confused with [Part Fillet](Part_Fillet.md). Unless you know what you are doing, [Part Fillet](Part_Fillet.md) should not be used on a PartDesign Body. See [Part and PartDesign](Part_and_PartDesign.md).

## Known Issues 

Fillets, chamfers, and other features that operate on solid bodies depend on the underlying OpenCASCADE Technology (OCCT) kernel that FreeCAD uses. The OCCT kernel occasionally has difficulty handling coincident sharp edges, where two faces meet. If this is the case FreeCAD may crash without an explanation.

If run from the terminal, FreeCAD may output a log like this one after the crash:


{{code|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

This output references functions located in `libTKBRep.so`, `libTKFillet.so`, etc., which are OCCT libraries. If this type of crashes occurs, the problem may need to be reported and solved in OCCT rather than in FreeCAD.

See the forum threads for more information:

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part design fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)

The user is also responsible for the integrity of his or her own model. Depending on the model, it may be impossible to perform a fillet or chamfer if the body is not big enough to support that operation. For example, it wouldn\'t be possible to create a 10 mm fillet if an edge is separated only 5 mm from the next surface. In that case, the maximum radius for a fillet would be 5 mm; trying to use a larger value may result in a shape that doesn\'t compute, or even a crash. If using the exact limit of 5 mm doesn\'t work, it may be possible to use a very close approximation, like 4.9999 mm, to produce the same visible result.

### Topological naming 

Edge numbers are not completely stable, therefore it is advisable that you finish the main design work of your solid body before applying features like fillets and chamfers, otherwise edges could change name and filleted edges would likely become invalid.

Read more in [topological naming problem](topological_naming_problem.md).

## Scripting

The tool **[16px|text-top=Fillet|link=PartDesign_Fillet](File:PartDesign_Fillet.svg.md) [Fillet](PartDesign_Fillet.md)** can be used in a macro, and, from the Python console using the following function:


```python
Box = Box.makeFillet(3,[Box.Edges[0]]) # 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
```

-   3 = radius
-   Box.Edges\[2\] = Edge with its number

Example:


```python
import PartDesign
from FreeCAD import Base

Box = Part.makeBox(10,10,10)
Box = Box.makeFillet(3,[Box.Edges[0]]) # pour 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
Part.show(Box)
```





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/pl
