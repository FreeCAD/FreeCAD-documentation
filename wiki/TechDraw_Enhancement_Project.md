# TechDraw Enhancement Project
This page is describes a potential 2018 Google Summer of Code project regarding updates to the FreeCAD Technical Drawing workbench (TechDraw).

## Outline

FreeCAD is first and foremost a 3D modeling tool. There are times, however, when we must produce 2D drawings for documentation, contracts, permits, etc. The Technical Drawing workbench (TechDraw) is used to produce basic technical drawings based on the 3D model. TechDraw is a recent addition to FreeCAD and requires many enhancements to bring it up to the level of sophistication seen in other workbenches.

## Details

1.  The FreeCAD user community is very diverse. As such, they use a diverse collection of technical drawing standards. Currently the individual parameters that make up a drawing style must be selected individually. A system of managing groups of drawing parameters by standard is required.
2.  Drawing tools to be added include the ability to add leaders and callouts drawings. This is a prerequisite to many enhancements, particularly in the drawing annotation area, such as feature control frames.
3.  There is a need for Dimensions that do not rely on specific vertex/edges, but on extrema of the figure - for example, overall width/height. A related request is for an \"arbitrary\" measurement that can be added when an actual value can not be calculated automatically.
4.  A \"Broken View\" is required to depict very large objects.
5.  Conversion to Part Workbench 2D geometry. The Part Workbench was recently enhanced with a full suite of 2D geometry tools. These were not available when TechDraw was first coded. For future ease of maintenance, a single suite of 2D tools would be preferred.

## Expected Outcome 

1.  A more robust and capable TechDraw workbench

## Future Possibilities 

This work will provide an introduction to the FreeCAD code base and the use of supporting software such as OpenCascade and Qt.

## Project Properties 

### Skills

-   Programming language mainly C++, unit tests in python
-   Understand of FreeCAD API is obviously beneficial.
-   Familiarity with any or all of the following will be helpful
    -   Qt Graphics View Framework
    -   Scalable Vector Graphics (SVG) standard
    -   Regular expressions
-   Experience in using CAD software is beneficial
-   Exposure to technical drawing standards

### Difficulty

Medium

### Additional Information



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Enhancement Project
