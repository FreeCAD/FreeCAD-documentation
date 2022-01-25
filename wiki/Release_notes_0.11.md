# Release notes 0.11
This is a summary of the most important changes and new features available in the 0.11 release of FreeCAD. The complete list can be found [here](http://www.freecadweb.org/tracker/changelog_page.php).

<img alt="" src=images/FreeCAD011.png  style="width:800px;">

A screenshot of the 0.11 version

### General

-   The [FreeCAD translation project](http://crowdin.net/project/freecad) has received huge help from many people around the world and FreeCAD now ships with no less than 15 languages: English, German, French, Italian, Swedish, Spanish, Portuguese, Russian, Ukrainian, Norwegian, Afrikaans, Finnish, Simplified Chinese, Croatian and Dutch. And many more languages are being worked on for the next releases.

![](images/release011-translation.jpg )

-   Several improvements have been brought all over FreeCAD, for example the hierarchy tree now allows complex object stacks, keeping all your geometry history clean and easily accessible and modifiable. New Python API improvements also allow objects to interact better with the tree, defining their own behaviour, icons, etc.

![](images/release011-dependency.jpg )

-   The copy/paste mechanism has also been much improved, now allowing easy copy/pasting of objects between documents.
-   The [Part Workbench](Part_Workbench.md) features new tools such as mirroring and edge fillets and chamfers.

### Sketch and part design 

-   The constraint solver of the [Sketcher Workbench](Sketcher_Workbench.md) has been totally rewritten and the Sketcher, even if still not complete, features already a good array of tools such as lines, rectangles, and constraints such as point coincidence, parallelism, fixed length or horizontal or vertical constraints.

-   In addition to the Sketcher, a new PartDesign workbench now allow you to quickly build solids on top of Sketches. As a rule now in FreeCAD, everything is parametric, you can go back anytime to change your sketch, and all geometry that depends on it will be adapted automatically

![](images/release011-sketcher.jpg )

![](images/Movie.png ) Examples: [Sketcher demo](http://www.youtube.com/watch?v=hvXupH5bA0E) • [PartDesign demo](http://www.youtube.com/watch?v=7ih9Jp3OAwA)

### Robot simulation 

-   The [Robot Workbench](Robot_Workbench.md) has been extended with many GUI tools and is now fairly functional and allows you to easily simulate industrial robot movements

![](images/release011-robot.jpg )

### 2D drafting 

-   Snapping has been greatly optimized and now works pretty fast, even on complex objects
-   The \"Trim/Extend\" tool can now be called \"Trim/Extend/Extrude\", since it allows you to quickly extrude single faces, offering a convenient shortcut to the standard Part Extrude tool
-   The Draft-to-Drawing sheet workflow has also been enhanced, all the Draft workbench objects can now be placed on a Drawing page, and they all offer the same level of comfort as standard Part objects, offering the ability to change their position, rotation and scale on the fly. They also offer some extra features, such as hatch pattern fillings

![](images/release011-draft-drawing.jpg )

-   The Draft workbench also offers new tools such as regular polygons and bSplines
-   There is also a new Edit tool, allowing to edit the geometry of most of the Draft objects

![](images/release011-draft.jpg )

-   Dimensions can now have their text edited and moved, and wires can have an end arrow, allowing to use them as leaders
-   Several commands such as move, rotate or dimensioning now allow you to do several copies without exiting the tool
-   The Draft workbench also gained a Python [API](Draft_API.md).
-   The DXF importer now support block attributes

![](images/Movie.png ) Examples: [Draft module demo](http://www.youtube.com/watch?v=Q7cG-LQK8Ps)

### Images

-   The image workbench now features an ImagePlane object, allowing you to display an image file inside the 3D scene, that can be used for example to construct geometry on top of scanned blueprints

### Documentation

-   The [FreeCAD manual](Online_Help_Toc.md) now has several well advanced translations. Check the main page!


{{languages | {{de|Release_notes_0.11/de}} {{es|Release_notes_0.11/es}} {{fr|Release_notes_0.11/fr}} {{it|Release_notes_0.11/it}} {{pl|Release_notes_0.11/pl}} {{ru|Release_notes_0.11/ru}} }}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.11
