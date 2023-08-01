# Release notes 0.12
This is a summary of the most interesting changes occured in FreeCAD since latest version. See [here](http://www.freecadweb.org/tracker/changelog_page.php) for the complete list of changes.

Older versions: [0.11](Release_notes_0.11.md)

### Welcome!

-   When you open FreeCAD for the first time, you are now welcomed by a brand new start center, which gathers the most common actions you would want to perform, such as open a particular workbench, load one of the recent files you worked on, read the latest news from the FreeCAD development, or watch one of the many new videos tutorials the heroic FreeCAD community has been making recently.

![](images/FreeCAD_start_center.jpg )

### Sketcher & PartDesign 

<img alt="" src=images/Rim_bling.png  style="width:800px;">

-   The [Sketcher](Sketcher_Workbench.md) has received a huge amount of work since the previous version, and is now based on a new solver designed from scratch for the task. The sketcher is now able to perform almost all 2D drawing operations of the [Draft Workbench](Draft_Workbench.md), and place a wide array of constraints on the sketch elements.

-   In addition, the [PartDesign Workbench](PartDesign_Workbench.md) has also evolved a lot and offers several common (and totally parametric) tools to work on top of sketches, such as extrusion, lofting or revolution.

### Architecture

-   A new [Architecture module](Arch_Workbench.md) is now part of FreeCAD. It is still in early development, but already features a couple of handy helper objects, such as walls and structural elements (columns and beams). Those can be built on top of existing 2D geometry, such as lines, wires and sketches, by specifying a width and a height, or, in case of structural elements, on top of 2D profiles. They can also be based on solids, or even include other solid shapes, as additions or even as subtractions, allowing virtually any possible geometry.

![](images/Arch_screenshot.jpg )

-   The Arch module also features an [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) importer, a [DAE (collada)](http://en.wikipedia.org/wiki/Collada) importer and exporter, and a special [OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file) exporter more suited to architecture models than the standard one.

-   Included in the Arch module is also a growing collection of tools to make the process of working with Mesh objects from other applications such as [Blender](http://www.blender.org) easier. Mesh objects, if well modeled, can easily and automatically be turned into clean shapes, and then into parametric Arch objects.

### 2D Drafting 

![](images/Draft_taskview.jpg )

-   Reclaim your work space! The Draft module now features a new UI mode that uses the FreeCAD Task system, which gathers all user interaction in one place, redeeming the precious space eaten by the Draft toolbar. To enable this, go to the Draft preferences and enable Taskbar mode.

-   The Draft Trim/Extend tool is now able to extrude single faces of existing objects.

-   Several new snap modes have been added, now allowing to snap perpendicularly and parallel to existing lines, and to locations that are aligned with other line segments.

-   The Draft module also features a new tool that produces, inside the same document, a projected 2D view of any 3D shape.

-   Draft objects can now be drawn directly on top of existing faces. If you didn\'t specify a working plane, it will be adapted temporarily to the underlying face.

-   The Draft module is now able to import Bézier curves from SVG files.


{{languages | {{es|Release_notes_0.12/es}} {{fr|Release_notes_0.12/fr}} {{it|Release_notes_0.12/it}}  {{pl|Release_notes_0.12/pl}} {{ru|Release_notes_0.12/ru}} }}



---
![](images/Button_right.svg) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.12
