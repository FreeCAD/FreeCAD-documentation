# <img alt="" src=images/preferences-techdraw.svg  style="width:64px;">  TechDraw Roadmap/ru

The [TechDraw Workbench](TechDraw_Workbench.md) was introduced officially as part of FreeCAD in version 0.17.

Here is a rough roadmap of areas to be addressed in the future (in no particular order).

### Current Activity 

-   TBD

### Upcoming

-   TBD

### Recent Changes 

-   TBD

## Futures

### Navigation Models 

TechDraw does not support the various navigation model used in the rest of FreeCAD (CAD, Blender, etc).

### HLR vs Face Occlusion 

TechDraw PartViews use the OCC Hidden Line Removal algorithms to project the Shape. HLR is computation intensive, and some (many? most?) views do not require hidden lines to be displayed. A new method of generating views is required. This may require getting the image directly from the 3D display.

### Draft/Arch coexistence 

There are inconsistencies between the way the Draft/Arch and TechDraw modules represent shapes. This limits the suitability of TechDraw for Draft/Arch users. One notable short-coming is that TechDraw is unable to apply Dimensions to the Svg images it receives from Draft/Arch.

### Templates

Making a template with editable text fields requires significant expertise with [SVG](SVG.md) and an SVG editor like Inkscape. Making the template creation process simpler will be a priority in the v0.18 development cycle.

### Bug Fixes/Feature Requests 

See the bug tracker for up to date information.


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Roadmap/ru
