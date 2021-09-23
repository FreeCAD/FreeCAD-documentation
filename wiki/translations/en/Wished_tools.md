# Wished tools/en
 I begin this page as an attempt to gather end-user wishes on specific tools they would like to find in FreeCAD. Several cad users already chatted with me about cad tools, about what they use most, what they would like to see in FreeCAD, what they couldn\'t live without, etc\... Although FreeCAD is not meant to specifically become a replacement for any other famous CAD software (especially the one that begins with Auto and ends with CAD), I think this can become a good reference to know about end-users expectations, and maybe to prioritize things over others in development.

If you are a CAD user and would like to add stuff here, feel free to edit, we would be glad to have your opinion here.

## 2D drawing 

-   ~~**Line**: Draws a line~~ - see [Draft Line](Draft_Line.md).
-   **Construction Line**: Draws a line at any angle infinitely - should be easy if possible in coin. To be investigated
-   ~~**Polyline**: Line with as many points as you like until command is ended~~ - see [Draft\_Wire](Draft_Wire.md).
-   **Polygon**: dependant on no. of sides
-   ~~**Rectangle**~~ - see [Draft Rectangle](Draft_Rectangle.md).
-   ~~**Arc**~~ - see [Draft Arc](Draft_Arc.md).
-   ~~**Circle**~~ - see [Draft Circle](Draft_Circle.md).
-   **Hatch**: Be able to fill an area with technical-style pattern (oblique lines, etc\...) - Under investigation
-   **Make and insert Blocks**: That is in FreeCAD two things: ~~be able to group elements in one object (compound?)~~ - see [Draft Upgrade](Draft_Upgrade.md) - and be able to instantiate those objects (several documents objects share same shape?)
-   **Text** - see [Draft Text](Draft_Text.md). To be extended to more complex stuff\...
-   **Display Order**: That is showing coplanar objects in desired order. Not sure this is possible, though\... Maybe, in a 3D world, we should rethink the way we draw 2D objects, and consider those \"overlapping\" objects differently (= draw them differently). To be discussed\...
-   ~~**Erase**~~ - see [Std Delete](Std_Delete.md).
-   ~~**Copy**~~ - see [Draft Move](Draft_Move.md).
-   ~~**Copy with base point**~~ - see [Draft Move](Draft_Move.md).
-   **Multiple copy**: Copy an object several times from same base point
-   **Paste**
-   **Paste as Block**
-   ~~**Offset**~~ - see [Draft Offset](Draft_Offset.md).
-   ~~**Move**~~ - see [Draft Move](Draft_Move.md).
-   ~~**Rotate**~~ - see [Draft Rotate](Draft_Rotate.md)
-   **Array**: interesting, could be merged with copy tool\...
-   **Stretch**
-   ~~**Trim**~~ - see [Draft Trimex](Draft_Trimex.md), but could be extended
-   ~~**Extend**~~ - see [Draft Trimex](Draft_Trimex.md), but could be extended
-   **Chamfer**
-   ~~**Fillet (with angle input)**~~ - implemented in Fold module
-   ~~**Explode**: Explodes blocks/lines~~ - see [Draft Downgrade](Draft_Downgrade.md).
-   ~~**Dimension**~~ - see [Draft Dimension](Draft_Dimension.md)
-   **Angle Dimension** - planned in Draft module
-   **Arc Length** - planned in Draft module
-   **Diameter** - see [Draft Dimension](Draft_Dimension.md)
-   ~~**Radius**~~ - see [Draft Dimension](Draft_Dimension.md)
-   **Continue Dimension**: continues a running dimension - planned in Draft module
-   ~~**Views: Top, Bottom, Right, Left**~~ - see [Std View Menu](Std_View_Menu.md).
-   ~~**View: Isometric views**~~ - see [Std OrthographicCamera](Std_OrthographicCamera.md).
-   ~~**Model Space and Paper space**~~ - see the [Drawing Workbench](Drawing_Workbench.md) - Model space = Where the model is drawn, Paper space = tabs with different setups that can be plotted. (tab can be drawn in and has viewports made by closed polylines or shapes that view into the model space.) you need to be able to click in and out of model space so you can set up the paper with boders and title boxes. The view needs to be scaled as needed ie. 1:50 or 1:100 - planned in Drawing module
-   **Drawing units**: All drawing units should be mm - this is a quite special topic, there are many things to be considered. To be discussed further.
-   **Thread** - PartDesign workbench. Feature Hole: correct functionality of bore depth according to ISO 6410--1 standard
-   **Thread** - normative correct simplified presentation of cross section in Techdraw according to ISO 6410--1 standard
-   ~~**Fillet** - PartDesign workbench: elimination of rounding problems~~

## Mesh modeling 

-   **Primitives**: Cubes, spheres etc. - present but no toolbar button
-   **Convert Part objects into meshes** - present but no toolbar button
-   **Flip mesh normals** - present but no toolbar button
-   **Close holes in meshes** - present but no toolbar button
-   **Remove faces of meshes** - present but no toolbar button
-   **Boolean operations**: Union, subtract and intersect meshes - present but no toolbar button

## Part modeling 

-   ~~**Primitives**~~
-   **Mesh conversion** to Part shapes
-   ~~**Boolean operations**~~
-   ~~**Extrude flat shapes**~~
-   ~~**Fillet edges of shapes**~~

## Parametric modeling 

-   **Custom properties for all objects**: so scripts and exporting to other software can carry additional information
-   ~~**Python objects**~~: 100% python-scripted objects - see [Scripted objects](Scripted_objects.md).

## Architecture modeling 

-   Wall
-   Window
-   Door
-   Beam
-   Slab
-   Roof
-   Assemblies

[Category:Hubs](Category:Hubs.md) [Category:Roadmap](Category:Roadmap.md) [Category:Developer](Category:Developer.md)
