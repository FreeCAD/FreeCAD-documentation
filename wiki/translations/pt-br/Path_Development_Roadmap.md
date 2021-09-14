# Path Development Roadmap/pt-br

 





{{TOCright}}

## Purpose

This page will discuss the strategic objectives for the [Path Workbench](Path_Workbench.md). This shouldn\'t be a list of features to implement but broader objectives that will steer the overall direction of Path development.

## Core Objectives 

These things make Path a reliable, performant, and flexible tool. Work in this area is never-ending and always high priority. New Developers should consider helping here before developing new features.

-   Broad test coverage
-   DRY and well documented code base
-   Bug fixes
-   Support for many CNC machines (postprocessors)

## Workflow

Obviously, the goal is a workflow that is efficient and resists human errors. However, the specific workflow can vary depending on the type of machine the user is working with and the type of geometry they are working on.

### Job Types 

Path is optimized for 2.5D milling. It needs the concept of job \'types\' to handle other kinds of workflows like Lathe, 4th Axis, and pure 2D machines. Additional job types would help narrow the choices a user must make and eliminate the visual noise and confusion that comes from options that don\'t apply to the desired task.

### 2D workflow 

2D workflows like laser/waterjet/plasma have some unique requirements.

-   Nesting of parts into cut sheets
-   marking for part ID, fold lines, stitching, etc.
-   Efficient import from DXF

Additional 2D strategies

-   Engrave - Engrave by following a set of 2D edges. We support this partly now but the workflow is rough and keeping the 2D elements oriented with the shape is nearly impossible.
-   V-Carve - Engrave by following the centerline between edges while controlling Z depth
-   Hatch Fill - Fill an arbitrary boundary with a hatching pattern

### Lathe Workflow 

Lathe setup is different from milling. The user is generally viewing the coordinate system with Z axis pointing right and X axis pointing toward the user. Toolpaths are viewed as 2D relative to one side of the work or relative to the end for facing operations.

Lathe operations

-   Center Drill
-   Contour Roughing - Remove material to approximate
-   Contour Finishing - Contour finishing pass
-   Facing
-   Boring
-   Threading External
-   Threading Internal

### 4/5 axis workflow 

continuous 4th axis operations may rotate the 4th while engaging the cutter. These kinds of operations will need to visualize the toolpath relative to the part. Other operations use the 4th to rotate the part to an orientation and then perform a pure 2.5D operation on the work. This is more like multiple setups and visualization might need to be take into account each discrete step.

### 2.5D (milling) workflow 

This is Path\'s strongest area. But there\'s room to improve.

Additional strategies

-   Threading
-   Boring - Straightline Boring Canned operation (G85/G89)
-   Slitting Saw - Slot cutting with saw tool on the side of the work

### 3D surface milling 

Additional strategies

-   Constant scallop
-   Pencil

### Multi-Job Context 

Some parts require multiple setups to complete. Each setup is represented by a separate job but no structure links them together other than the top-level document. This is insufficient because the document may contain multiple parts that have completely independent manufacturing steps/jobs/setups.

Commercial CNC users usually produce a document called a [\'setup sheet\'](https://www.cnccookbook.com/art-setup-sheet/) which describes to the CNC operator how to set up the machine in order to manufacture the part. This \'setup sheet\' is not at all related to the Path setupsheet concept. It is a human-readable document meant to communicate assumptions and notes required to correctly execute the gcode. The setup sheet usually contains the following information:

-   tools required
-   lowest z level
-   Part name/number/version
-   customer
-   rough stock or starting condition
-   operations
-   estimated run time
-   critical dimensions and inspection criteria
-   notes about previous runs
-   gcode program name
-   Fixtures and workholding information

## Low Level Libraries 

Path makes use of several libraries to generate toolpaths based on part geometry. These include libarea/patharea/clipper, [Open CASCADE Technology](https://dev.opencascade.org/doc/overview/html/), and [OpenCamLib](https://github.com/aewallin/opencamlib). Other libraries are available and more will likely be written in the future. We should include these whenever possible and when a native (OCCT) solution is unavailable.

[Openvoronoi](https://github.com/aewallin/openvoronoi) is one library that is available and license compatible. At present, it does not build for python3 and isn\'t packaged for distribution with FreeCAD. Making openvoronoi available would allow v-carving operation and possibly some other interesting toolpaths.

[Deepnest](https://github.com/Jack000/Deepnest) or an equivalent nesting/bin packing library would allow us to efficiently arrange parts in a cut-sheet to minimize stock usage.

## Path Modifications 

Some of the operations/strategies offer features and tools that are useful but not available for other op/strategies. We should work to make things more consistent.

Pocket/3D Pocket has a boundary extension tool. This should be available to all operations where it makes sense. For example adaptive, surface, waterline,

## Representation of remaining material 

Path should have a more robust state for the remaining material. This would be useful for visualization, collision avoidance, and REST milling.

## Post Processing & Advanced Gcode 

-   Post to git

Gcode for the hobbyist is transient. It\'s used once and then likely not retained. If the user needs it again, they simply re-post the original file. For commercial users under certain certification standards, the gcode is a long-term asset and often may require version control protection. Integrating version control directly into the post-processing workflow might be an interesting feature.

-   modular output for older machines with limited memory.

Many old machines have an extremely limited capacity for gcode. While physically able to produce more complex paths, the very large output from surfacing and adaptive toolpaths make them unusable. It would be useful to post-process the output with an eye on the size of the resulting file. As a file reaches a maximum size, the post-processor could insert a spindle retraction and stop gracefully, then the next file could continue. Output files would be numbered to indicate sequence.

-   Support for Macros, subprograms, variables.

## Path Analysis 

-   Tip up Prediction / avoidance

When 2D cutting (laser/waterjet/plasma) of material supported on a grating, small parts cut out of the main stock can \'tip up\' creating a crash hazard for the cutting tool during subsequent moves. Being able to predict these events or avoid them by ordering paths would be desirable. ([Further reading](https://shopfloorlasers.com/nesting-software/263-heads-up))

-   Visualization of remaining material after each operation could be improved

## List of shortcomings 

The following list is not individual bugs but shows how Path is inconsistent in its application of concepts.

-   Inconsistent use of cut direction. We should be talking about climb/conventional everywhere and not using language like CW/CCW.
-   Inconsistent use of stepover. I wish we had used the terminology of DOC/WOC (depth of cut / width of cut) from the beginning but we didn\'t. We use \'stepdown\' and \'stepover\' but inconsistently apply it. Sometimes it is an absolute value and other times a percent of cutter diameter.
-   Inconsistent implementation of the ObjectOp class hierarchy. Some of the ops can\'t be toggled off.
-   Finishing Passes. I think we should add an additional ObjectOp.Feature for FeatureFinishPass. This would give a new tab where a user could configure the final finishing pass with a different tool controller, direction, etc.
-   Inconsistent control of performance vs. accuracy. Many operations have poorly named or inconsistent controls for tolerance. At a minimum these could be grouped into a consistently named property group.
-   Inconsistent use of stock shapes and extensions.
-   No high level path optimization / automatic grouping of disjunct cutting areas.





{{Path_Tools_navi

}} 
