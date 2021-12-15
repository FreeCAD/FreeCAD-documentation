# <img alt="TechDraw workbench icon" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/bg

## Introduction

The <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md) is used to produce basic technical drawings from 3D models created with another workbench such as [Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), or [Arch](Arch_Workbench.md), or imported from other applications. Each drawing is a Page, which can contain various Views of drawable objects such as Part::Features, PartDesign::Bodies, App::Part groups, and Document Object groups. The resulting drawings can be used for things like documentation, manufacturing instructions, contracts, permits, etc.

Dimensions, sections, hatched areas, annotations, and [SVG](SVG.md) symbols can be added to the page, which can be further exported to different formats like [DXF](DXF.md), [SVG](SVG.md), and [PDF](PDF.md).

TechDraw was officially included in FreeCAD starting with version 0.17; it is intended to replace the unsupported [Drawing Workbench](Drawing_Workbench.md). Both workbenches are still provided in v0.17, but the Drawing Workbench may be removed in future releases. To keep up with TechDraw plans and developments, visit the [TechDraw Roadmap](TechDraw_Roadmap.md).

If your primary goal is the production of complex 2D drawings and [DXF](DXF.md) files, and you don\'t need 3D modelling, FreeCAD may not be the right choice for you. You may wish to consider a dedicated software program for technical drafting instead, such as [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) or [QCad](https://en.wikipedia.org/wiki/QCad).


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Pages

These are tools for creating Page objects.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Redraw Page](TechDraw_RedrawPage.md): forces an update of the selected page. <small>(v0.19)</small> 

## Views

These are tools for creating View objects.

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Insert View](TechDraw_View.md): adds a 2D projection view of an object.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Insert Active View](TechDraw_ActiveView.md): inserts a view of the active 3D view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Insert Projection Group](TechDraw_ProjectionGroup.md): invokes a dialog to create many views of an object from multiple directions.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Insert Section View](TechDraw_SectionView.md): inserts a cross-section view of an existing view.

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Insert Detail View](TechDraw_DetailView.md): inserts a detail view of a portion of an existing view.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> _ object.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> _ [Section Plane](Arch_SectionPlane.md) object.

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> _ sheet.

## Clips

These are tools to create and manage Clip objects (clipped views).

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Insert Clip Group](TechDraw_ClipGroup.md): inserts a clip group into a page.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Add View to Clip Group](TechDraw_ClipGroupAdd.md): adds an existing view to a clip group.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Remove View from Clip Group](TechDraw_ClipGroupRemove.md): removes a view from a clip group.

## Decorations

These are tools to decorate pages or views:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Hatch Face using Image File](TechDraw_Hatch.md): applies a hatch pattern from a file to a face.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md): applies a hatch pattern to a face using an Autodesk PAT specification.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> _ file into a page.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> _ image into a page.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Turn View Frames On/Off](TechDraw_ToggleFrame.md): turns on/off frames and labels surrounding a view.

## Dimensions

These are tools for creating and working with Dimension objects.

Linear dimensions can be based on two points, on one line, or on two lines.

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Insert Length Dimension](TechDraw_LengthDimension.md): adds a length dimension.

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Insert Horizontal Dimension](TechDraw_HorizontalDimension.md): adds a horizontal length dimension.

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Insert Vertical Dimension](TechDraw_VerticalDimension.md): adds a vertical length dimension.

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Insert Radius Dimension](TechDraw_RadiusDimension.md): adds a radius dimension to a circle or circular arc.

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Insert Diameter Dimension](TechDraw_DiameterDimension.md): adds a diameter dimension to a circle or a circular arc.

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Insert Angle Dimension](TechDraw_AngleDimension.md): adds an angle dimension between two straight edges.

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Insert 3-Point Angle Dimension](TechDraw_3PtAngleDimension.md): adds an angle dimension using three vertices.

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Insert Horizontal Extent Dimension](TechDraw_HorizontalExtentDimension.md): adds a horizontal extent dimension. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Insert Vertical Extent Dimension](TechDraw_VerticalExtentDimension.md): adds a vertical extent dimension. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Link Dimension to 3D Geometry](TechDraw_LinkDimension.md): links an existing dimension to the 3D geometry.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Insert Balloon Annotation](TechDraw_Balloon.md): adds a \"balloon\" annotation to a page. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Insert Landmark Dimension](TechDraw_LandmarkDimension.md): adds a landmark distance dimension. <small>(v0.19)</small> 

## Annotations

The annotation tools are for \"marking up\" a drawing with additional information.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Insert Annotation](TechDraw_Annotation.md): adds a plain text block as annotation.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Add Leaderline to View](TechDraw_LeaderLine.md): adds a leaderline to a view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Insert Rich Text Annotation](TechDraw_RichTextAnnotation.md): adds an rich text block as annotation to a leaderline or a view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Add Cosmetic Vertex](TechDraw_CosmeticVertex.md): adds a Vertex which is not part of the source geometry. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Add Midpoint Vertices](TechDraw_Midpoints.md): adds Cosmetic Vertices at midpoints of selected edges. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Add Quadrant Vertices](TechDraw_Quadrants.md): adds Cosmetic Vertices at quarter points of selected (circular) edges. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Add Centerline to Faces](TechDraw_FaceCenterLine.md): adds a centerline to selected face(s). <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Add Centerline between 2 Lines](TechDraw_2LineCenterLine.md): adds a centerline between 2 lines. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Add Centerline between 2 Points](TechDraw_2PointCenterLine.md): adds a centerline between 2 points. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Add Cosmetic Line Through 2 points](TechDraw_2PointCosmeticLine.md): adds a cosmetic line connecting 2 vertices. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md): removes cosmetic objects from a page. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Change Appearance of Lines](TechDraw_DecorateLine.md): changes the appearance of selected line(s). <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Show/Hide Invisible Edges](TechDraw_ShowAll.md): shows/hides invisible lines/edges in a view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Add Welding Information to Leader](TechDraw_WeldSymbol.md): adds welding specifications to an existing leaderline. <small>(v0.19)</small> 

## Extensions

These are tools to improve your TechDraw drawings.


**Some of these tools have yet to be released.**

### Attributes and modifications 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:32px;"> [Aspect](TechDraw_ExtensionSelectLineAttributes.md): select style, width and colour of lines. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:32px;"> [Stretch](TechDraw_ExtensionExtendLine.md): extend a line at both ends. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width:32px;"> [Shorten](TechDraw_ExtensionShortenLine.md): shorten a line at both ends. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width:32px;"> [Lock/Unlock](TechDraw_ExtensionLockUnlockView.md): Lock/Unlock a view. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width:32px;"> [Align Section](TechDraw_ExtensionPositionSectionView.md): align a section view orthogonal to its source view. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:32px;"> [Align Horizontal](TechDraw_ExtensionPosHorizChainDimension.md): align a horizontal dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width:32px;"> [Align Vertical](TechDraw_ExtensionPosVertChainDimension.md): align a vertical dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width:32px;"> [Align Oblique](TechDraw_ExtensionPosObliqueChainDimension.md): align an oblique dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:32px;"> [Horizontal Spacing](TechDraw_ExtensionCascadeHorizDimension.md): cascade horizontal dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width:32px;"> [Vertical Spacing](TechDraw_ExtensionCascadeVertDimension.md): cascade vertical dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width:32px;"> [Oblique Spacing](TechDraw_ExtensionCascadeObliqueDimension.md): cascade oblique dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width:32px;"> [Change Aspect](TechDraw_ExtensionChangeLineAttributes.md): change style, width and colour of lines. <small>(v0.20)</small> 

### Centerlines and threading 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Arc-Circle Centerlines](TechDraw_ExtensionCircleCenterLines.md): adds centerlines to circles and arcs. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width:32px;"> [Circular Series Centerlines](TechDraw_ExtensionHoleCircle.md): draw the centerlines of a hole/bolt circle. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:32px;"> [Intersection Point](TechDraw_ExtensionVertexAtIntersection.md): create the vertexes at intersection of lines. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:32px;"> [Circunference](TechDraw_ExtensionDrawCosmCircle.md): draw a cosmetic circumference using center and radius vertex. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawArc.svg  style="width:32px;"> [Arch](TechDraw_ExtensionDrawArc.md): draw an arc rotating counterclockwise. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width:32px;"> [Perpendicular](TechDraw_ExtensionLinePerpendicular.md): draw a line perpendicular to another line through a vertex. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:32px;"> [Parallel](TechDraw_ExtensionLineParallel.md): draw a line parallel to another line through a vertex. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Thread section Hole](TechDraw_ExtensionThreadHoleSide.md): adds a symbolic thread to the side view of a hole. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [Thread section Shaft](TechDraw_ExtensionThreadBoltSide.md): adds a symbolic thread to the side view of a bolt. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Thread Hole](TechDraw_ExtensionThreadHoleBottom.md): adds symbolic threads to the bottom view of holes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Thread Shaft](TechDraw_ExtensionThreadBoltBottom.md): adds symbolic threads to the bottom view of bolts. <small>(v0.20)</small> 

### Dimensions 

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:32px;"> [Diameter Symbol](TechDraw_ExtensionInsertDiameter.md): insert diameter sign as praefix character. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width:32px;"> [Tubular Symbol](TechDraw_ExtensionInsertSquare.md): insert square sign as praefix character. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Horizontal Series](TechDraw_ExtensionCreateHorizChainDimension.md): create a horizontal dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Vertical Series](TechDraw_ExtensionCreateVertChainDimension.md): create a vertical dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Oblique Series](TechDraw_ExtensionCreateObliqueChainDimension.md): create an oblique dimension chain. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Parallel Horizontal](TechDraw_ExtensionCreateHorizCoordDimension.md): create cascaded horizontal dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Parallel Vertical](TechDraw_ExtensionCreateVertCoordDimension.md): create cascaded vertical dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Parallel Oblique](TechDraw_ExtensionCreateObliqueCoordDimension.md): create cascaded oblique dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Horizontal Chamfer](TechDraw_ExtensionCreateHorizChamferDimension.md): create a horizontal chamfer dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Vertical Chamfer](TechDraw_ExtensionCreateVertChamferDimension.md): create a vertical chamfer dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Arc Length](TechDraw_ExtensionCreateLengthArc.md): create an arc length dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:32px;"> [Increase Accuracy](TechDraw_ExtensionIncreaseDecimal.md): increase decimal places . <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width:32px;"> [Decrease Accuracy](TechDraw_ExtensionDecreaseDecimal.md): decrease decimal places . <small>(v0.20)</small> 

## Export

These are tools for exporting pages to other applications.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> _ file.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> _ file.

## Additional features 

-   [Line Groups](TechDraw_LineGroup.md): to control the appearance of various types of lines.
-   [Templates](TechDraw_Templates.md): the default templates defined for the drawing pages.
-   [Hatching](TechDraw_Hatching.md): explanation of the different hatching techniques.
-   [Geometric dimensioning and tolerancing](TechDraw_Geometric_dimensioning_and_tolerancing.md): explanation on how to achieve geometric dimensioning and tolerancing.

## Preferences

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Preferences](TechDraw_Preferences.md): preferences for the default values of the drawing page such as projection angle, colors, text sizes, and line styles.

## Scripting

The TechDraw tools can be used in [macros](macros.md) and from the [Python](Python.md) console by using two APIs.

-   [TechDraw API](TechDraw_API.md)
-   [TechDrawGui API](TechDrawGui_API.md)

## Limitations

-   TechDraw drawings and its API are not interchangeable with the [Drawing Workbench](Drawing_Workbench.md) and its API. It is possible to convert Drawing Pages to TechDraw Pages using a Python script (`moveViews.py`).
-   It is possible to have both TechDraw and Drawing Pages in the same FreeCAD document, as each page is completely independent from each other.
-   There are minor differences in specifying editable texts in [SVG](SVG.md) templates compared to the Drawing module. In TechDraw the scaling of the SVG document affects the position of the editable text fields. See the forum discussion [TechDraw templates scale](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271) for more details.
-   Do not cut, copy and paste TechDraw objects in the tree view as this generally does not work out well.

## Tutorials

-   [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md): introduction to creating drawings with the TechDraw Workbench.
-   [Creating a new template](TechDraw_TemplateHowTo.md): instructions to create a new page template in Inkscape for using with the TechDraw Workbench.
-   [Measurement Of Angles On Holes](Measurement_Of_Angles_On_Holes.md): instructions for adding centerlines and subsequent angle representations on holes.
-   [Miscellaneous](TechDraw_HowTo_Page.md): instructions for different settings like center marks, etc.
-   [TechDraw Pitch Circle Tutorial](TechDraw_Pitch_Circle_Tutorial.md): instructions for adding a pitch circle.

Video tutorials by sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/bg
