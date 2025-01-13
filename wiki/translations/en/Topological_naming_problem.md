# Topological naming problem/en
## Introduction




The [topological naming problem](topological_naming_problem.md) in FreeCAD refers to the issue of a shape changing its internal name after a modelling operation (pad, cut, union, chamfer, fillet, etc.) is performed. This will result in other parametric features that depend on that shape to break or be incorrectly computed. This issue affects all objects in FreeCAD but is especially notable when building solids with the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), and when dimensioning those solids with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

-   In <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md), if a feature is supported on a face (or edge or vertex), the feature may break if the underlying solid changes size or orientation, as the original face (or edge or vertex) may be internally renamed.
-   In <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench.md), if a dimension is measuring the length of a projected edge, the dimension may break if the 3D model is changed, as the vertices may be renamed thus changing the measured edge.

The topological naming issue is a complex problem in CAD modelling that stems from the way the internal FreeCAD routines handle updates of the geometrical shapes created with the [OCCT kernel](OpenCASCADE.md). This problem is not unique to FreeCAD. It is generally present in CAD software, but most other CAD software has heuristics to reduce the impact of the problem on users.

Starting with FreeCAD 0.19 there are ongoing development efforts to improve the core handling of shapes by adding heuristics that reduce the impact of these issues. The [naming algorithm](#Topological_naming_algorithm.md) is designed to reduce manual effort, sometimes by automatically fixing up problems, and other times presenting a likely solution, and otherwise at least clearly showing what caused the problem. The first stable release of FreeCAD to feature this new naming algorithm is 1.0. Over time, this algorithm will be applied to more parts of FreeCAD, and more automatic and assisted repair will be added in later versions.

The topological naming problem most often affects and confuses new users of FreeCAD. In PartDesign, the user is advised to follow the best practices discussed in the [feature editing](feature_editing.md) page. Use of supporting datum objects like [planes](PartDesign_Plane.md) and [local coordinate systems](PartDesign_CoordinateSystem.md) is strongly recommended to produce models that aren\'t easily subject to such topological errors. In TechDraw, the user is advised to add dimensions only when the 3D model is complete and won\'t be modified further.

## Example

1\. In the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), create a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md), then use <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign NewSketch](PartDesign_NewSketch.md) and select the XY plane to draw the base sketch; then perform a <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md) to create a first solid.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Select the top face of the previous solid, and then use <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign NewSketch](PartDesign_NewSketch.md) to draw another sketch; then perform a second pad.

+++
| <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;"> |
+++

3\. Select the top face of the previous extrusion, and once again create a sketch, and a pad.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Now, double click the second sketch, and modify it so that its length is along the X direction; doing this will recreate the second pad. The third sketch and pad will stay in the same place.

+++
| <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;"> |
+++

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. Now, double click the second sketch again, and adjust its points so that a portion of it is outside the limits defined by the first pad. By doing this, the second pad will recompute correctly, however, when looking at the [tree view](tree_view.md), an error will be indicated in the third pad.

+++
| <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;"> |
+++

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. By making visible the third sketch and pad, it is clear that the computation of the new solid did not proceed correctly. The third sketch, instead of being supported by the top face of the second pad, appears in a strange place, with its normal oriented towards the X direction. This results in an invalid pad, as this pad would be disconnected from the rest of the <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md), which is not allowed.

The problem appears to be that when the second sketch was modified, the top face of the second pad was renamed from `Face13` to `Face14`. The third sketch is attached to `Face13` as it originally was, but since this face is now on the side (not at the top), the sketch follows its orientation and now is incorrectly positioned.

+++
| <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;"> |
+++

7\. To fix the issue, the third sketch should be mapped to the top face again. Select the sketch, click on the ellipsis (three dots) next to the **Map Mode** property, and choose the top face of the second pad again. Then the sketch moves to the top of the existing solid, and the third pad is generated without issues.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

+++
| <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;"> |
+++

Remapping a sketch in this way can be done every time there is a topological naming error, however, this may be tedious if the model is complicated and there are many such sketches that need to be adjusted.

## Solution

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

The [dependency graph](Std_DependencyGraph.md) is a tool that is helpful to observe the relationships between the different bodies in the document. Using the original modelling workflow reveals the direct relationship that exists between the sketches and the pads. Like a chain, it is easy to see that this direct dependence will be subject to topological naming problems if any of the links in the sequence changes.

As explained on the [feature editing](Feature_editing.md) page, a solution to this problem is to support sketches not on faces, but on the main planes of the [PartDesign Body\'s](PartDesign_Body.md) Origin, or on datum planes attached to those main planes. Using datum planes to support a single sketch, as is described below, is actually not necessary as the sketch itself can be directly attached to a main plane and has the same offset options as a datum plane. But using datum planes can make sense when positioning multiple sketches.

1\. Select the origin of the [PartDesign Body](PartDesign_Body.md) and make sure that it is visible. Then select the XY plane, and click on [PartDesign Plane](PartDesign_Plane.md). In the attachment offset dialog, give it an offset in the Z direction so that the datum plane is coplanar with the top face of the first pad.

2\. Repeat the process but this time add a larger offset so that the second datum plane is coplanar with the top face of the second pad.




+++
| <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;"> |
+++

3\. Select the second sketch, click on the ellipsis next to the **Map Mode** property, and then select the first datum plane. The datum plane is already offset from the body\'s XY plane, so no further Z offset is required for the sketch.

4\. Repeat the process with the third sketch, and select the second datum plane as support. Again, no further Z offset is necessary.

5\. The dependency graph now shows that the sketches and pads are supported by the datum planes. This model is more stable as each sketch can be modified essentially independently from each other.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Double click the second sketch and modify the shape. The second pad should update immediately without causing topological problems with the third sketch and the third pad.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. In fact, every sketch can be modified without interfering with each other\'s pads. As long as the pads have sufficient extrusion length, so that they touch and form a contiguous solid, the entire body will be valid.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">

## Tradeoffs

Adding datum objects is more work for the user but ultimately produces more stable models that are less subject to the topological naming problem.

Naturally, datum objects can be created before any sketches are drawn, and pads are produced. This may be helpful to visualize the approximate shape and dimensions of the final body.

Datum planes can also be based on other datum planes. This creates a chain of dependencies that could also result in topological problems; however, since datum planes are very simple objects, the risks of having these issues is less than if the face of a solid object is used as support.

Datum objects, [points](PartDesign_Point.md), [lines](PartDesign_Line.md), [planes](PartDesign_Plane.md), and [coordinate systems](PartDesign_CoordinateSystem.md), may also be useful as reference geometry, that is, as visual aids to show the important features in the model, even if no sketch is directly attached to them.

## Topological naming algorithm 

Realthunder\'s topological naming algorithm, described in forum thread [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278), which was selected to reduce the impact of this problem, has been widely described as \"fixing the topological naming problem.\" This has unintentionally misled many users into thinking that it will no longer be helpful to use techniques like datums, explicit sketch placement, and [Feature editing](Feature_editing#Advice_for_creating_stable_models.md) to make models more stable. The algorithm is not intended to fix every failure introduced by topological naming ambiguity. Rather, it has three purposes.

1.  The first and most important purpose is, whenever possible, to **identify** broken references from topological changes and display an error to the user. Instead of having to work through a series of operations to find the first operation that diverges from the design intent, the operation that changes the names will normally be flagged with an error, making it much easier to manually fix model problems introduced by changes to operations or parameters.
2.  Sometimes, FreeCAD will be able to identify a **likely** fix for a broken reference, so that when the user is manually fixing up the flagged broken reference, a candidate will be presented for them to accept or change. A common example of this is dress-up operations like fillets and chamfers, where user might have to to edit the operation and either accept the proposed replacement feature selection or change it to correct it.
3.  In some cases, FreeCAD will be able to **automatically** resolve the broken reference, because enough information about the reference is stored to have high confidence that the replacement is correct. For example, when sketching directly on a face, the algorithm will frequently (but not always) correctly repair the reference to the face when the underlying geometry is changed parametrically. (When changing the structure, such as by adding or deleting operations in the middle of a Part Design Body, this kind of automatic repair will be less likely.) However, FreeCAD will do this only with high confidence in the correctness of the repair, because an incorrect automatic repair may re-introduce the problem of having to hunt for where a problem was introduced in order to repair a model after a modification. *First, do no harm.*

In FreeCAD 1.0, the implementation of this algorithm in the official FreeCAD release reached feature parity with Realthunder\'s \"Linkstage 3\" fork, where he originally developed the algorithm, as of the time the integration work started. There are new FreeCAD features that could use the algorithm but do not yet, and there will always be more opportunities to add candidate fixes and automatic repair. The initial work has provided a *framework* to use for these additional improvements over time, both in core FreeCAD and in Addons.

## Links

-   [PartDesign Fillet - Topological naming](PartDesign_Fillet#Topological_naming.md)
-   [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278): a possible solution, by realthunder.
-   [Topological Naming Project](Topological_Naming_Project.md): idea to solve the problem, by ickby.
-   [Topological data scripting](Topological_data_scripting.md)
-   [Feature editing](Feature_editing.md): contains alternate advice for stable modelling techniques.
-   [Clarifying and expanding \"Topological Naming Problem\" documentation](https://forum.freecad.org/viewtopic.php?p=770360): Clarifying expectations for Realthunder\'s topological naming algorithm selected for FreeCAD 1.0.

## Videos

-   [Why do my FreeCAD models break? - \"Topological Naming Problem\"](https://youtu.be/6p2vqEEmWq4): A Video explanation of the underlying issues of [Topological naming problem](Topological_naming_problem.md)
-   [FreeCAD Is Fundamentally Broken! - Now what\... Help Me Decide\...](https://www.youtube.com/watch?v=QSsVFu929jo): A Maker Tales Video


 {{TechDraw Tools navi}} {{PartDesign Tools navi}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [TechDraw](Category_TechDraw.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Topological naming problem/en
