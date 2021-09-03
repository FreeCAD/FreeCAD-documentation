---
- GuiCommand:   Name:Mesh MeshFromShape‏‎   MenuLocation:Meshes → Create Mesh from Shape   Workbenches:[[Mesh Workbench   Mesh]]|SeeAlso:---


</div>

## Description


<div class="mw-translate-fuzzy">

## Introducere

Această comandă creează o plasă dintr-un obiect tip formă.


</div>

The inverse operation is [Part ShapeFromMesh](Part_ShapeFromMesh.md) from the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).

## Utilizare

1.  Selectați obiectul de tip formă.
2.  Alegeți ** Meshes** → **<img src="images/Mesh_Mesh_from_Shape.svg" width=32px> Create Mesh from shape...** din meniul principal.
3.  Un meniu va cere utilizarea mesher-ului/tessellation și valorile corespunzătoare pentru mesher

Doar selectând ** Meshes** → **<img src="images/Mesh_Mesh_from_Shape.svg" width=32px> Create Mesh from shape...** vă va oferi un meniu suplimentar pentru a vă alege forma de transformat în plasă


<div class="mw-translate-fuzzy">

## Limitări


</div>


<div class="mw-translate-fuzzy">

![](images/Mesh_Mesher_Standard.jpg )


</div>


<div class="mw-translate-fuzzy">

Abaterea de suprafață: Dacă acest număr este mai mic, ochiul devine mai fin. Valoarea cea mai mică este de 0,001.


</div>


<div class="mw-translate-fuzzy">

![](images/Mesh_Mesher_Mefisto.jpg )


</div>


<div class="mw-translate-fuzzy">

![](images/Mesh_Mesher_Netgen.jpg )


</div>


<div class="mw-translate-fuzzy">

Puteți alege între plase fiind:

-   Foarte grosieră
-   Grosieră
-   Moderat
-   Fină
-   Foarte fină
-   Definită de utilizator

Pentru ca Mesh fiind \"definit de utilizator\", puteți seta aceste valori:

-   -   Clasificarea dimensiunii ochiului: Dacă acest parametru este mai mic, ochiul devine mai fin. O valoare cuprinsă între 0,1 și 10.
    -   Element per muchie/edge: Dacă acest parametru este mai mare, ochiul devine mai fin. O valoare cuprinsă între 0,1 și 10.
    -   Element pe raza de curbură: Dacă acest parametru este mai mare, ochiul devine mai fin. O valoare cuprinsă între 0,1 și 10.

Pentru fiecare opțiune principală puteți de asemenea să alegeți:

-   Optimizați suprafața: dacă va fi făcută optimizarea formei suprafeței.
-   Elemente de ordine al doilea: Fie elementele de ordinul doi vor fi generate.
-   Quad dominantă: Dacă ochiurile vor fi aranjate ca hexahedral.


</div>


<div class="mw-translate-fuzzy">

**Mefisto Mesher**


</div>


<div class="mw-translate-fuzzy">

**Netgen Mesher**


</div>

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

### Standard mesher {#standard_mesher}

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





{{Mesh Tools navi

}}  
