---
- GuiCommand:
   Name:Mesh FromPartShape
   MenuLocation:Meshes → Create mesh from shape...
   Workbenches:[Mesh](Mesh_Workbench.md)
---

## Description

The **Mesh\_FromPartShape** command creates non-parametric [mesh](mesh.md) objects ([Mesh Features](Mesh_Feature.md)) from [shape](shape.md) objects ([Part Features](Part_Feature.md)).

The inverse operation is [Part ShapeFromMesh](Part_ShapeFromMesh.md) from the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).

## Usage

1.  Optionally select one or more objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_FromPartShape.svg" width=16px> [Mesh FromPartShape](Mesh_FromPartShape.md)** button.
    -   Select the {{MenuCommand|Meshes → <img src="images/Mesh_FromPartShape.svg" width=16px> Create mesh from shape...}} option from the menu.
3.  The {{MenuCommand|Tessellation}} task panel opens.
4.  While the task panel is open you can create a new selection or change an existing selection.
5.  Select the tab for the mesher you wish to use.
6.  Specify the required settings. See [Meshers](#Meshers.md).
7.  Press the **OK** button to close the task panel and finish the command.

## Meshers

These are the available meshers and their settings:

### Standard mesher {#standard_mesher}

-    {{MenuCommand|Surface deviation}}: the maximum [linear deviation](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) of a mesh section from the surface of the object.

-    {{MenuCommand|Angular deviation}}: the maximum [angular deviation](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) from one mesh section to the next. This setting is used when meshing curved surfaces.

-    {{MenuCommand|Relative surface deviation}}: if checked, the maximum linear deviation of a mesh segment will be the specified {{MenuCommand|Surface deviation}} multiplied by the length of the current mesh segment (edge).

-    {{MenuCommand|Apply face colors to mesh}}: if checked, the mesh will get the face colors of the object.

-    {{MenuCommand|Define segments by face colors}}: if checked, mesh segments will be grouped according to the colors of the object\'s faces. These groups will be exported for mesh output formats supporting this feature (the [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file) format for example).

### Mefisto mesher {#mefisto_mesher}

-    {{MenuCommand|Maximum edge length}}: the maximum edge length of the mesh. A smaller value results in a finer mesh. Specifying {{Value|0}}, or unchecking the checkbox, results in a very coarse mesh.

    -   If you press the **Estimate** button the mesher will enter an estimated value for the {{MenuCommand|Maximum edge length}}. This value is not very reliable if multiple objects have been selected.

### Netgen mesher {#netgen_mesher}

-    {{MenuCommand|Fineness}}: select an options for the finesse of the mesh:

    -   
        {{MenuCommand|Very coarse}}
        

    -   
        {{MenuCommand|Coarse}}
        

    -   
        {{MenuCommand|Moderate}}
        

    -   
        {{MenuCommand|Fine}}
        

    -   
        {{MenuCommand|Very fine}}
        

    -   
        {{MenuCommand|User defined}}
        
        : for this option the following settings can be specified:

        -   
            {{MenuCommand|Mesh size grading}}
            
            : a smaller value results in a finer mesh. The value must be in the {{Value|0.1}} - {{Value|1.0}} range.

        -   
            {{MenuCommand|Element per edge}}
            
            : a larger value results in a finer mesh. The value must be in the {{Value|0.2}} - {{Value|10.0}} range.

        -   
            {{MenuCommand|Element per curvature radius}}
            
            : a larger value results in a finer mesh. The value must be in the {{Value|0.2}} - {{Value|10}} range.

-    {{MenuCommand|Optimize surface}}: if checked, the surface shape will be optimized.

-    {{MenuCommand|Second order elements}}: if checked, second order elements will be generated resulting in a finer mesh.

-    {{MenuCommand|Quad dominated}}: if checked, the mesh will preferably use [quadrilateral faces](https://en.wikipedia.org/wiki/Types_of_mesh#Two-dimensional).

### Gmsh mesher {#gmsh_mesher}


<small>(v0.19)</small> 

For Linux users: the external [Gmsh](https://gmsh.info/) module is required.

-    {{MenuCommand|Meshing}}: select a meshing option:

    -   
        {{MenuCommand|Automatic}}
        

    -   
        {{MenuCommand|Adaptive}}
        

    -   
        {{MenuCommand|Delaunay}}
        

    -   
        {{MenuCommand|Frontal}}
        

    -   
        {{MenuCommand|BAMG}}
        

    -   
        {{MenuCommand|Frontal Quad}}
        

    -   
        {{MenuCommand|Parallelograms}}
        

-    {{MenuCommand|Max. element size}}: a smaller value results in a finer mesh. Specify {{Value|0}} to have this size automatically determined.

-    {{MenuCommand|Min. element size}}: a smaller value results in a finer mesh. The value should be smaller than the {{MenuCommand|Max. element size}}. Specify {{Value|0}} to have this size automatically determined.

-    {{MenuCommand|Angle}}: seems to be unsupported at this time.

-    {{MenuCommand|Path}}: press the **...** button and browse to the {{FileName|gmsh.exe}} path.

-   If the meshing process takes too long you can press the **Kill** button to abort it.

-   Press the **Clear** button to remove the information in the text area.

## Notes

-   This command is not restricted to objects created with the [Part workbench](Part_Workbench.md). It can create a mesh from any object that has a shape including objects created with the [PartDesign workbench](PartDesign_Workbench.md).
-   The [Std Export](Std_Export.md) command can export shape objects directly to a mesh format.
-   See also: [Export to STL or OBJ](Export_to_STL_or_OBJ.md) tutorial.

## Preferences

### Standard mesher {#standard_mesher_1}

-   The {{MenuCommand|Surface deviation}} setting is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → LinearDeflection}}.
-   The {{MenuCommand|Angular deviation}} setting is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → AngularDeflection}}.
-   The {{MenuCommand|Relative surface deviation}} setting is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → RelativeLinearDeflection}}.

### Gmsh mesher {#gmsh_mesher_1}

-   The {{MenuCommand|Path}} is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Mod → Mesh → Meshing → gmshExe}}.

## Properties

See: [Mesh Feature](Mesh_Feature.md).

## Scripting

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a mesh object from a shape object use the `meshFromShape` method of the MeshPart module. This method has several signatures. The signature determines the mesher that will be used. The example below uses the Mefisto mesher signature.

 
```python
import FreeCAD, Part, Mesh, MeshPart

cyl = FreeCAD.ActiveDocument.addObject("Part::Cylinder","Cylinder")
FreeCAD.ActiveDocument.recompute()

msh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = MeshPart.meshFromShape(Shape=cyl.Shape, MaxLength=1)
msh.ViewObject.DisplayMode = "Flat Lines"
```




 {{Mesh Tools navi}}  
