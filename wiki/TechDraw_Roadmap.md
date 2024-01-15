# <img alt="" src=images/preferences-techdraw.svg  style="width:64px;">  TechDraw Roadmap

Here is a rough roadmap of areas to be addressed in the [TechDraw Workbench](TechDraw_Workbench.md) in 2023.

### Current Activity 

-   refactoring code into more maintainable pieces

### Primary Focus for 2023 

There are 2 main areas to be addressed in 2023:

-   conversion between drawing geometry and model geometry
    -   these conversions are scattered throughout the code
    -   the most visible impact is the difficulty in specifying cosmetic geometry
    -   cosmetic vertex/edge/centerline now rotates with the parent view.

-   the \"lesser topological naming problem\"
    -   primarily making dimensions survive the renaming of reference geometry
        -   Phase1 (reference geometry has a new name, but still exists) implemented by [PR #8989](https://github.com/FreeCAD/FreeCAD/pull/8989)
        -   First attempt at Phase2 (handling situation where reference geometry has legitimately changed) stalled. Rethinking.
    -   also affects face hatching
    -   also affects edge appearance attributes

### Work Completed in 2023 

-   remove redundant edges from HLR result PR #9280
-   dimension reference name change handling PR #8989
-   RichTextAnnotation fix text size & position in svg export PR #10019
-   improve SVG hatch drawing speed PR #9995 and PR #9885
-   add large ANSI format templates PR #9825
-   fix precision errors in 3d window direction/orientation PR #9577
-   add shaft/hole fit annotation PR #8455
-   add ANSI Y14.5 compatible font PR #8198
-   Replacement for Qt XMLPatterns [PR #9104](https://github.com/FreeCAD/FreeCAD/pull/9104) (Thanks Werner!)
-   zoom improvements PR #10547, #10456
-   hatch speed improvements PR #9995, #9985

### Other Items for 2023 

These items would be nice to address in 2023:

-   drawing overlay
    -   allow graphics to be added to a drawing page as on a transparent overlay in traditional drafting. This will build on the [SymbolsAndTraces](https://github.com/WandererFan/FreeCAD/tree/SymbolsAndTraces) research project and \@Evgeniy\'s schematic workbench.

### Work Completed in 2022 

These items were implemented in 2022:

-   Navigation modes
-   New face detection algorithm
-   PrintAll function
-   Bitmap hatching fix
-   Extension line gaps
-   Section dialog live/deferred update option (implemented as part of complex section)
-   Convert all templates to \"plain svg\" (implemented for latin script templates)
-   View stacking order
-   Use separate thread for hidden line removal, face finding, section and detail cuts
-   replace ActiveView Svg creation with simple screen capture
-   complex section views
-   easier dimensions from 3d geometry
-   simple dimension reference repair dialog

### 2022 Plan Items Not Completed 

These items are still on the infamous TODO list. They will be worked on as and if time allows.

-   Projection group dialog upgrade including live/deferred update option
-   Ability to specify file preferences as relative paths [6707](https://github.com/FreeCAD/FreeCAD/issues/6707)
-   ability to specify units by dimension or page instead of system wide.
-   weld symbol upgrades including ISO/AWS symbology and help text [6313](https://github.com/FreeCAD/FreeCAD/issues/6313)
-   ordinate dimensions [6587](https://github.com/FreeCAD/FreeCAD/issues/6587)
-   broken view [5694](https://github.com/FreeCAD/FreeCAD/issues/5694)
-   improved handling of Draft/Arch objects
-   include sketcher points in drawings
-   Feature Control Frames (GD&T)
-   Threaded hole representation


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Roadmap
