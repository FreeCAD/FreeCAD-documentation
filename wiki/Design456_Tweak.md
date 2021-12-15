---
- GuiCommand:
   Name:Design456 Tweak
   MenuLocation:Design456_Tools → 3DTools → Tweak
   Workbenches:[Design456](Design456_Workbench.md)
   Shortcut:None
   SeeAlso:
---

# Design456 Tweak

## Description

The <img alt="" src=images/Design456_Tweak.svg  style="width:24px;"> [Design456 Tweak](Design456_Tweak.md) tool is an experimental command to modify an object\'s shape. This tool, originally conceived for the Draft Workbench, it\'s still unfinished, and became part of the [external workbench](external_workbenches.md) called [Design456](Design456_Workbench.md) to allow initial testing. For reference:

-   [draft pull request discussion](https://github.com/FreeCAD/FreeCAD/pull/3716);
-   [experiment on destructive subelement modifier](https://forum.freecadweb.org/viewtopic.php?f=22&t=48425);
-   [Shape.replaceShape() breaks Shape and confuses Shape.check()](https://forum.freecadweb.org/viewtopic.php?f=10&t=48660)

## Usage

1.  Switch to the <img alt="" src=images/Design456_workbench_icon.svg  style="width:24px;"> _ is necessary, if not previously installed)
2.  Select one or more face, or some edges, or some points from a 3D object, run the command, give a vector to move the selected subshapes. The tool will try to recreate the shape according to the moved subelements.

## Limitations

The tool is actually dose not work well:

-   it can create only planar faces;
-   it frequently breaks the shape if it has to do with an hollow shape, and even if it can fix it automatically, it\'s still not tested totally and might be removed in the future.

## Properties


{{Properties_Title|Base}}

## Scripting





{{Design456 Tools navi

}} 

_

---
[documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > Design456 Tweak
