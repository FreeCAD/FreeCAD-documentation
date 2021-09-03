 {{TutorialInfo
|Topic= Import text and geometry from Inkscape
|Level= Beginner
|Time= 30 minutes
|Author=r-frank
|FCVersion=0.16.6704
|Files=
}}

## Introduction

This tutorial is supposed to show how to import text or geometry created with inkscape via svg-format into FreeCAD.
Inkscape 0.91 and FreeCAD 0.16.6704 on Windows are used for these operations.

## General tips for importing from inkscape 

-   the svg-import in FreeCAD cannot handle a svg file with a resolution of more than 45 dpi, so check the settings in inkscape
-   when importing path objects which show up in the 3D view in FreeCAD not very smooth it may be a matter of the FreeCAD-settings for the shape view.
    -   in FreeCAD choose ** Edit** → ** Preferences** → ** Part Design** → ** Shape View**
    -   as for \"Tesselation\", the \"Maximum deviation depending on the model bounding box\" the default value is \"0,5 %\"
    -   setting this to a lower value will increase smoothness of the model in the 3D view (and use more PC performance)
    -   don\'t use values lower than \"0,01 %\", this will most likely crash FreeCAD
    -   in that case deleting \"system.cfg\" and \"user.cfg\" in your FreeCAD-user-directory will solve this problem

## Importing text from inkscape 

-   In inkscape, after inserting text (and perhaps applying effects like bending or something else to it) make sure to
    -   select your text and choose ** Path** → ** Object to path**
    -   ungroup your objects
    -   save as \"Plain SVG (\*.svg)\" file format
-   open the file in FreeCAD, choosing the option \"SVG as geometry (importSVG)\"
-   a path object for each letter/number/sign will be created in the tree view
-   use [Draft](Draft_Workbench.md) [upgrade tool](Draft_Upgrade.md) on each path object to create faces
-   use pad or [Part](Part_Workbench.md) [extrude tool](Part_Extrude.md) on the faces to get solids
-   you can fuse your objects or use compound on them depending on your intended further work

## Importing geometry from inkscape 

Since inkscape and FreeCAD seem to have different approaches on how to apply dimensions on svg-object, the recommended workflow seems to be:

-   ungroup all objects in inkscape
-   select all objects in inkscape
-   apply a stroke style with a width of 0 mm (yes, that is zero millimeter) to all objects
-   save as \"Inkscape SVG (\*.svg)\" or \"Plain SVG (\*.svg)\" file format
-   open the file in FreeCAD, choosing the option \"SVG as geometry (importSVG)\"
-   the dimensions of the objects in inkscape and in FreeCAD should now be identical

## Credits

Thanks to users \"freecad-heini-1\" and \"herbk\" for testing and providing valuable feedback.




