# Tolerancing/pl
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

![GD&T 3D annotations](images/Tolerancing_Annotated_Design_Model.png ) [Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing) (GD&T) means the specification of permissible limits/deviation of dimensions. Here we\'re talking strictly about geometric tolerances: a real-world error of shape, size, location, orientation in relation to the designed ideal.

There\'s also a distinction between the terms \"limits and fits\" and \"geometric tolerances and surface conditions\". 

## Standards

There are 2 ANSI/ISO standards:

-   ISO 1101 / ASME Y14.5 Stating and interpreting Geometric Dimensions and Tolerances (Definitions and symbols) [1](http://www.sharifcadcam.ir/uploaded/2e22f9ef-dfc5-47bc-a126-cc51e9686c4f.pdf)
-   ISO 16792 / ASME Y14.41 Model-based definitions (CAD data) 3D model presentation and geometric dimensioning and tolerancing [2](http://gost-snip.su/download/asme_y14_412003_digital_product_definition_data_practices)

ISO 16792 is a part of \"Geometrical Product Specification\" (GPS), which defines dimensional and geometrical tolerancing, surface properties and the related verification principles, measuring equipment and calibration requirements, including the uncertainty of dimensional and geometrical measurement.

-   [GPS Table of contents](https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/gps_toc_.pdf)

There\'s also ISO 10303 (informally \"STEP\"), which defines the file format for exchanging product and manufacturing information, which is sourced from model-based definitions.

## Approaches

There are two approaches to specifying Product and Manufacturing Information (PMI).

-   The legacy approach (Traditional) of producing 2D drawings with GD&T symbols. In some industries, this approach is also referred to as Technical Product Documentation (TPD). How this is achieved with FreeCAD is described in [TechDraw Geometric dimensioning and tolerancing](TechDraw_Geometric_dimensioning_and_tolerancing.md).
-   The modern 3D approach Model-Based Definition (MBD) which embeds GD&T data into the model and produces drawings with GD&T symbols

  Traditional                                           MBD
   
  3D models with 2D drawings containing GD&T/PMI        3D model with embedded GD&T/PMI
  Human-readable                                        Human- and machine-readable
  Relies on human interpretation                        Relies on an automated process
  Labour-intensive                                      Automated
  Multiple files                                        Single data model
  Manual synchronization between CMM/CAM/CAI software   Single source of truth

## Existing software 

-   [Adding geometric tolerance with feature control frame in AutoCAD](https://www.youtube.com/watch?v=C4c_kJtwtxc)
-   [Working with Drawing Symbols in Fusion 360](https://www.youtube.com/watch?v=sVxuIgLgsKk)
-   [Tech Tip Tuesday: Using the GD&T Quick Creation Menu in GOM Inspect](https://www.youtube.com/watch?v=Os1PVdb4UU8)
-   [CATIA V5 - FUNCTIONAL TOLERANCING & ANNOTATION](https://www.youtube.com/watch?v=WQUjodi7Izs)
-   [SmartProfile GD&T Analysis Software](https://www.youtube.com/watch?v=0z7IoDiVYMY)

## Implementation so far 

-   [TechDraw symbols SVG files](https://github.com/FreeCAD/FreeCAD/commits/master/src/Mod/TechDraw/Symbols/gd-and-t)
-   [GDT workbench](https://github.com/juanvanyo/FreeCAD-GDT)
-   [TechDraw balloon macro](https://github.com/reox/FreeCAD_macros/blob/b6731feb10573e2d21781ce161c8ec7e894d1b73/TDCustomFormat.FCMacro)
-   [A branch that introduced a new type of DocumentObject: DrawViewGDTReference](https://github.com/lidiriel/FreeCAD/commits/gdt-reference2)

## Forum threads 

-   [Enhancing TechDraw with geometric tolerances and surface finishings](https://forum.freecadweb.org/viewtopic.php?f=35&t=41726) - Developer discussion (2019)

-   [Geometrical tolerances](https://forum.freecadweb.org/viewtopic.php?t=15497) - User feature request (2016)
-   [GD&T Workbench for FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=10&t=22072) - A workbench for FreeCAD 0.16 (2016)
-   [TechDraw balloons](https://www.forum.freecadweb.org/viewtopic.php?f=9&t=35392) - A general-purpose TechDraw Macro which can be used to place GD&T symbols on a TechDraw page (2019)
-   [ISO 1101: 2017 Geometric Tolerancing Standard](https://forum.freecadweb.org/viewtopic.php?f=35&t=35887) - A link to the ISO 1101:2017 PDF file (2019)
-   [Geometric Dimensioning & Tolerancing](https://forum.freecadweb.org/viewtopic.php?t=42426) - Developer proposing contributions (2019)

## Tutorials and learning materials on GD&T 

-   [Brief introduction (Video)](https://www.youtube.com/watch?v=P5GT9ZSRYl0)
-   [How Precise Is That Part? Know Your GD&T](https://hackaday.com/2018/10/04/how-precise-is-that-part-know-your-gdt/)
-   [GD&T for beginners \| step by step approach to do GD&T for mechanical drawing (Video)](https://www.youtube.com/watch?v=-3tN7KvDUjQ)
-   [Straight To The Point Engineering (Video tutorials)](https://www.youtube.com/c/StraightToThePointEngineering/videos?view=0&sort=da&flow=grid)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [TechDraw](Category_TechDraw.md) > Tolerancing/pl
