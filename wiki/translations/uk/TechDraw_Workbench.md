# <img alt="TechDraw workbench icon" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/uk

## Introduction

The <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md) is used to produce basic technical drawings from 3D models created with another workbench such as [Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), or [BIM](BIM_Workbench.md), or imported from other applications. Each drawing is a Page, which can contain various Views of drawable objects such as Part::Features, PartDesign::Bodies, App::Part groups, and Document Object groups. The resulting drawings can be used for things like documentation, manufacturing instructions, contracts, permits, etc.

Dimensions, sections, hatched areas, annotations, and [SVG](SVG.md) symbols can be added to the page, which can be further exported to different formats like [DXF](DXF.md), [SVG](SVG.md), and [PDF](PDF.md).

If your primary goal is the production of complex 2D drawings and [DXF](DXF.md) files, and you don\'t need 3D modelling, FreeCAD may not be the right choice for you. You may wish to consider a dedicated software program for technical drafting instead, such as [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) or [QCad](https://en.wikipedia.org/wiki/QCad).




<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Snapping


<small>(v1.0)</small> 

: The TechDraw Workbench has a snapping feature. It can be used to automatically align views, section views and dimensions when positioning them by dragging with the mouse. With **Snap View Alignment** enabled (default) in the [preferences](TechDraw_Preferences#Snapping.md), views will snap to alignment with other views when close enough (**View Snapping Factor** setting). Dimensions are also snapped to other parallel dimensions and the dimension text can be snapped to the middle of the dimension line. Snapping can be temporarily disabled by holding down the **Alt** key.

## Tools

### Pages

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Insert Default Page](TechDraw_PageDefault.md): adds a new page using the default [template](TechDraw_Templates.md).

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Insert Page using Template](TechDraw_PageTemplate.md): adds a new page using a selected [template](TechDraw_Templates.md).

-   <img alt="" src=images/TechDraw_FillTemplateFields.svg  style="width:32px;"> [Update template fields](TechDraw_FillTemplateFields.md): <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Redraw Page](TechDraw_RedrawPage.md): forces an update of the selected page.

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width:32px;"> [Print All Pages](TechDraw_PrintAll.md): prints all pages in a document. <small>(v0.21)</small> 

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Export Page as SVG](TechDraw_ExportPageSVG.md): saves the current page as [SVG](SVG.md) file.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Export Page as DXF](TechDraw_ExportPageDXF.md): saves the current page as [DXF](DXF.md) file.

### Views

#### TechDraw views 

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Insert View](TechDraw_View.md): adds a representation of one or more objects. <small>(v1.0)</small> : It can create a single view, a [Projection Group](TechDraw_ProjectionGroup.md), a [Spreadsheet View](TechDraw_SpreadsheetView.md), an [Arch View](TechDraw_ArchView.md), a [Symbol](TechDraw_Symbol.md) or an [Image View](TechDraw_Image.md).

-   <img alt="" src=images/TechDraw_BrokenView.svg  style="width:32px;"> [Insert Broken View](TechDraw_BrokenView.md): adds a broken view of one or more objects. <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Insert Section View](TechDraw_SectionView.md): inserts a cross-section view of an existing view.

-   <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Insert Complex Section View](TechDraw_ComplexSection.md): inserts a cross-section view of an existing view based on a profile. <small>(v0.21)</small> 

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Insert Detail View](TechDraw_DetailView.md): inserts a detail view of a portion of an existing view.

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Insert Projection Group](TechDraw_ProjectionGroup.md): invokes a dialog to create multiple views of an object from different directions. <small>(v1.0)</small> : The [Insert View](TechDraw_View.md) tool can be used instead.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Insert Clip Group](TechDraw_ClipGroup.md): inserts a clip group.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [Insert SVG Symbol](TechDraw_Symbol.md): inserts a symbol from a [SVG](SVG.md) file into a page. <small>(v1.0)</small> : The [Insert View](TechDraw_View.md) tool can be used instead.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Insert Bitmap Image](TechDraw_Image.md): inserts a PNG or JPG [bitmap](bitmap.md) image into a page. <small>(v1.0)</small> : The [Insert View](TechDraw_View.md) tool can be used instead.

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width:32px;"> [Share View](TechDraw_ShareView.md): shares a view between multiple pages.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Turn View Frames On/Off](TechDraw_ToggleFrame.md): turns on/off frames and labels surrounding a view.

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:32px;"> [Project Shape](TechDraw_ProjectShape.md): creates projections of shapes in the [3D view](3D_view.md).

#### Views from other workbenches 

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Insert Active View](TechDraw_ActiveView.md): inserts a view of the active 3D view.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Insert Draft Workbench Object](TechDraw_DraftView.md): inserts a view of a [Draft Workbench](Draft_Workbench.md) object.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Insert BIM Workbench Object](TechDraw_ArchView.md): inserts a view of a [BIM Workbench](BIM_Workbench.md) [Arch Section Plane](Arch_SectionPlane.md) object. <small>(v1.0)</small> : The [Insert View](TechDraw_View.md) tool can be used instead.

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Insert Spreadsheet View](TechDraw_SpreadsheetView.md): inserts a view of a [Spreadsheet Workbench](Spreadsheet_Workbench.md) sheet. <small>(v1.0)</small> : The [Insert View](TechDraw_View.md) tool can be used instead.

### Stacking

These are tools for changing the stacking order which controls the apparent depth of views on a page.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Adjust Stacking Order:

  - <img alt="" src=images/TechDraw_StackTop.svg  style="width:32px;"> [Move view to top of stack](TechDraw_StackTop.md): moves views to the top of the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackBottom.svg  style="width:32px;"> [Move view to bottom of stack](TechDraw_StackBottom.md): moves views to the bottom of the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackUp.svg  style="width:32px;"> [Move view up one level](TechDraw_StackUp.md): moves views up one level in the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackDown.svg  style="width:32px;"> [Move view down one level](TechDraw_StackDown.md): moves views down one level in the stacking order. <small>(v0.21)</small> 

### Dimensions

-   <img alt="" src=images/TechDraw_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensions:

  - <img alt="" src=images/TechDraw_Dimension.svg  style="width:32px;"> [Insert Dimension](TechDraw_Dimension.md): adds a contextual dimension. <small>(v1.0)</small> 

  - <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Insert Length Dimension](TechDraw_LengthDimension.md): adds a length dimension.

  - <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Insert Horizontal Dimension](TechDraw_HorizontalDimension.md): adds a horizontal length dimension.

  - <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Insert Vertical Dimension](TechDraw_VerticalDimension.md): adds a vertical length dimension.

  - <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Insert Radius Dimension](TechDraw_RadiusDimension.md): adds a radius dimension to a circle or circular arc.

  - <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Insert Diameter Dimension](TechDraw_DiameterDimension.md): adds a diameter dimension to a circle or a circular arc.

  - <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Insert Angle Dimension](TechDraw_AngleDimension.md): adds an angle dimension between two straight edges.

  - <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Insert 3-Point Angle Dimension](TechDraw_3PtAngleDimension.md): adds an angle dimension using three vertices.

  - <img alt="" src=images/TechDraw_AreaDimension.svg  style="width:32px;"> [Insert Area Annotation](TechDraw_AreaDimension.md): adds an area dimension to a face. <small>(v1.0)</small> 

  - <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Create Arc Length Dimension](TechDraw_ExtensionCreateLengthArc.md): creates an arc length dimension.

  - <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Insert Horizontal Extent Dimension](TechDraw_HorizontalExtentDimension.md): adds a horizontal extent dimension.

  - <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Insert Vertical Extent Dimension](TechDraw_VerticalExtentDimension.md): adds a vertical extent dimension.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Create Horizontal Chain Dimensions](TechDraw_ExtensionCreateHorizChainDimension.md): creates a sequence of aligned horizontal dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Create Vertical Chain Dimensions](TechDraw_ExtensionCreateVertChainDimension.md): creates a sequence of aligned vertical dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Create Oblique Chain Dimensions](TechDraw_ExtensionCreateObliqueChainDimension.md): creates a sequence of aligned oblique dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Create Horizontal Coordinate Dimensions](TechDraw_ExtensionCreateHorizCoordDimension.md): creates multiple evenly spaced horizontal dimensions starting from the same baseline.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Create Vertical Coordinate Dimensions](TechDraw_ExtensionCreateVertCoordDimension.md): creates multiple evenly spaced vertical dimensions starting from the same baseline.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Create Oblique Coordinate Dimensions](TechDraw_ExtensionCreateObliqueCoordDimension.md): creates multiple evenly spaced oblique dimensions starting from the same baseline.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Create Horizontal Chamfer Dimension](TechDraw_ExtensionCreateHorizChamferDimension.md): creates a horizontal size and angle dimension for a chamfer.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Create Vertical Chamfer Dimension](TechDraw_ExtensionCreateVertChamferDimension.md): creates a vertical size and angle dimension for a chamfer.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Insert Balloon Annotation](TechDraw_Balloon.md): adds a \"balloon\" annotation to a page.

-   <img alt="" src=images/TechDraw_AxoLengthDimension.svg  style="width:32px;"> [Insert Axonometric Length Dimension](TechDraw_AxoLengthDimension.md): adds an axonometric length dimension. <small>(v0.21)</small> 

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Insert Landmark Dimension - EXPERIMENTAL](TechDraw_LandmarkDimension.md): adds a landmark distance dimension.

-   <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:32px;"> [Dimension Repair](TechDraw_DimensionRepair.md): can adjust the 2D or 3D geometry references of a dimension. <small>(v0.21)</small> 

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Link Dimension to 3D Geometry](TechDraw_LinkDimension.md): links an existing dimension to the 3D geometry (deprecated).

### Hatching

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Hatch Face using Image File](TechDraw_Hatch.md): applies a hatch pattern from a file to a face.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md): applies a hatch pattern to a face using an Autodesk PAT specification.

### Annotations

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Insert Annotation](TechDraw_Annotation.md): adds a plain text block as annotation.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Add Leaderline to View](TechDraw_LeaderLine.md): adds a leaderline to a view.

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Insert Rich Text Annotation](TechDraw_RichTextAnnotation.md): adds an rich text block as annotation to a leaderline or a view.

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Cosmetic Vertices:

  - <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Add Cosmetic Vertex](TechDraw_CosmeticVertex.md): adds a Vertex which is not part of the source geometry.

  - <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Add Midpoint Vertices](TechDraw_Midpoints.md): adds Cosmetic Vertices at midpoints of selected edges.

  - <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Add Quadrant Vertices](TechDraw_Quadrants.md): adds Cosmetic Vertices at quarter points of selected (circular) edges.

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Centerlines:

  - <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Add Centerline to Faces](TechDraw_FaceCenterLine.md): adds a centerline to selected face(s).

  - <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Add Centerline between 2 Lines](TechDraw_2LineCenterLine.md): adds a centerline between 2 lines.

  - <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Add Centerline between 2 Points](TechDraw_2PointCenterLine.md): adds a centerline between 2 points.

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Add Cosmetic Line Through 2 points](TechDraw_2PointCosmeticLine.md): adds a cosmetic line connecting 2 vertices.

-   <img alt="" src=images/TechDraw_CosmeticCircle.svg  style="width:32px;"> [Add Cosmetic Circle](TechDraw_CosmeticCircle.md): adds a cosmetic circle. <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Change Appearance of Lines](TechDraw_DecorateLine.md): changes the appearance of selected line(s).

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Show/Hide Invisible Edges](TechDraw_ShowAll.md): shows/hides invisible lines/edges in a view.

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Add Welding Information to Leader](TechDraw_WeldSymbol.md): adds welding specifications to an existing leaderline.

-   <img alt="" src=images/TechDraw_SurfaceFinishSymbols.svg  style="width:32px;"> [Add Surface Finish Symbol](TechDraw_SurfaceFinishSymbols.md): adds a surface finish symbol to a page. <small>(v0.21)</small> 

-   <img alt="" src=images/TechDraw_HoleShaftFit.svg  style="width:32px;"> [Add Hole/Shaft Fit](TechDraw_HoleShaftFit.md): adds hole or shaft tolerances using ISO 286 to a dimension. <small>(v0.21)</small> 

### Extensions

#### Attributes and modifications 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:32px;"> [Select Line Attributes, Cascade Spacing and Delta Distance](TechDraw_ExtensionSelectLineAttributes.md): selects the attributes (style, width and color) for new cosmetic lines and centerlines, and specifies the cascade spacing and delta distance.

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width:32px;"> [Change Line Attributes](TechDraw_ExtensionChangeLineAttributes.md): changes the attributes (style, width and color) of cosmetic lines and centerlines.

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Change Length of Cosmetic Lines or Centerlines:

  - <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:32px;"> [Extend Line](TechDraw_ExtensionExtendLine.md): extends a cosmetic line or centerline at both ends.

  - <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width:32px;"> [Shorten Line](TechDraw_ExtensionShortenLine.md): shortens a cosmetic line or centerline at both ends.

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width:32px;"> [Lock/Unlock View](TechDraw_ExtensionLockUnlockView.md): locks or unlocks the position of a view.

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width:32px;"> [Position Section View](TechDraw_ExtensionPositionSectionView.md): orthogonally aligns a section view with its source view.

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Align Dimensions:

  - <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:32px;"> [Position Horizontal Chain Dimensions](TechDraw_ExtensionPosHorizChainDimension.md): aligns horizontal dimensions to create a chain dimension.

  - <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width:32px;"> [Position Vertical Chain Dimensions](TechDraw_ExtensionPosVertChainDimension.md): aligns vertical dimensions to create a chain dimension.

  - <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width:32px;"> [Position Oblique Chain Dimensions](TechDraw_ExtensionPosObliqueChainDimension.md): aligns oblique dimensions to create a chain dimension.

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Evenly Space Dimensions:

  - <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:32px;"> [Cascade Horizontal Dimensions](TechDraw_ExtensionCascadeHorizDimension.md): evenly spaces horizontal dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width:32px;"> [Cascade Vertical Dimensions](TechDraw_ExtensionCascadeVertDimension.md): evenly spaces vertical dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width:32px;"> [Cascade Oblique Dimensions](TechDraw_ExtensionCascadeObliqueDimension.md): evenly spaces oblique dimensions.

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width:32px;"> [Calculate the area of selected faces](TechDraw_ExtensionAreaAnnotation.md): calculates the area of selected faces and inserts an area annotation.

-   <img alt="" src=images/TechDraw_ExtensionArcLengthAnnotation.svg  style="width:32px;"> [Calculate the arc length of selected edges](TechDraw_ExtensionArcLengthAnnotation.md): calculates the arc length of selected edges and inserts an arc length annotation. <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width:32px;"> [Customize format label](TechDraw_ExtensionCustomizeFormat.md): customizes the formatting of a balloon text or dimension text. GD&T symbols and other special character can be added.

#### Centerlines and threading 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Centerlines:

  - <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Add Circle Centerlines](TechDraw_ExtensionCircleCenterLines.md): adds centerlines to circles and arcs.

  - <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width:32px;"> [Add Bolt Circle Centerlines](TechDraw_ExtensionHoleCircle.md): adds centerlines to a circular pattern of circles.

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Cosmetic Threads:

  - <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Add Cosmetic Thread Hole Side View](TechDraw_ExtensionThreadHoleSide.md): adds a cosmetic thread to the side view of a hole.

  - <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Add Cosmetic Thread Hole Bottom View](TechDraw_ExtensionThreadHoleBottom.md): adds a cosmetic thread to the top or bottom view of holes.

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [Add Cosmetic Thread Bolt Side View](TechDraw_ExtensionThreadBoltSide.md): adds a cosmetic thread to the side view of a bolt/screw/rod.

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Add Cosmetic Thread Bolt Bottom View](TechDraw_ExtensionThreadBoltBottom.md): adds a cosmetic thread to the top or bottom view of bolts/screws/rods.

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Vertexes:

  - <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:32px;"> [Add Cosmetic Intersection Vertex(es)](TechDraw_ExtensionVertexAtIntersection.md): adds cosmetic vertex(es) at the intersection(s) of selected edges.

  - <img alt="" src=images/TechDraw_CommandAddOffsetVertex.svg  style="width:32px;"> [Add an offset vertex](TechDraw_CommandAddOffsetVertex.md): adds a cosmetic vertex at a specified offset from a selected vertex. <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Cosmetic Circles or Arcs:

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:32px;"> [Add Cosmetic Circle](TechDraw_ExtensionDrawCosmCircle.md): adds a cosmetic circle based on two vertexes.

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width:32px;"> [Add Cosmetic Arc](TechDraw_ExtensionDrawCosmArc.md): adds a cosmetic counter clockwise arc based on three vertexes.

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width:32px;"> [Add Cosmetic Circle 3 Points](TechDraw_ExtensionDrawCosmCircle3Points.md): adds a cosmetic circle based on three vertexes.

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Cosmetic Parallel or Perpendicular Lines:

  - <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:32px;"> [Add Cosmetic Parallel Line](TechDraw_ExtensionLineParallel.md): adds a cosmetic line parallel to another line through a vertex.

  - <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width:32px;"> [Add Cosmetic Perpendicular Line](TechDraw_ExtensionLinePerpendicular.md): adds a cosmetic line perpendicular to another line through a vertex.

#### Dimensions 

Several of the Extensions dimension tools are listed under [Dimensions](#Dimensions.md) above.

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Insert Prefix:

  - <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:32px;"> [Insert \'⌀\' Prefix](TechDraw_ExtensionInsertDiameter.md): inserts a \'⌀\' symbol at the beginning of the dimension text.

  - <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width:32px;"> [Insert \'□\' Prefix](TechDraw_ExtensionInsertSquare.md): inserts a \'□\' symbol at the beginning of the dimension text.

  - <img alt="" src=images/TechDraw_ExtensionInsertRepetition.svg  style="width:32px;"> [Insert \'n×\' Prefix](TechDraw_ExtensionInsertRepetition.md): inserts a repeated feature count at the beginning of the dimension text. <small>(v1.0)</small> 

  - <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width:32px;"> [Remove Prefix](TechDraw_ExtensionRemovePrefixChar.md): removes all symbols at the beginning of the dimension text.

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Change Decimal Places:

  - <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:32px;"> [Increase Decimal Places](TechDraw_ExtensionIncreaseDecimal.md): increases the number of decimal places of the dimension text.

  - <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width:32px;"> [Decrease Decimal Places](TechDraw_ExtensionDecreaseDecimal.md): decreases the number of decimal places of the dimension text.

### Miscellaneous

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md): removes cosmetic objects from a page.

### Obsolete tools 

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Add View to Clip Group](TechDraw_ClipGroupAdd.md): adds an existing view to a clip group. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Remove View from Clip Group](TechDraw_ClipGroupRemove.md): removes a view from a clip group. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width:32px;"> [Move View](TechDraw_MoveView.md): moves a view and its dependents to a different page. Not available in <small>(v1.0)</small> .

## Additional features 

-   [Line Groups](TechDraw_LineGroup.md): to control the appearance of various types of lines.
-   [Templates](TechDraw_Templates.md): the default templates defined for the drawing pages.
-   [Hatching](TechDraw_Hatching.md): explanation of the different hatching techniques.
-   [Geometric dimensioning and tolerancing](TechDraw_Geometric_dimensioning_and_tolerancing.md): explanation on how to achieve geometric dimensioning and tolerancing.

## Preferences

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Preferences](TechDraw_Preferences.md): preferences for the default values of the drawing page such as projection angle, colors, text sizes, and line styles.

## Scripting

The TechDraw tools can be used in [macros](Macros.md) and from the [Python](Python.md) console. For more information see:

-   [Autogenerated API documentation](https://freecad.github.io/SourceDoc/)
-   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)
-   [Editable Text Fields](TechDraw_PageDefault#Editable_text_fields.md)

## Limitations

-   Do not cut, copy and paste TechDraw objects in the [Tree view](Tree_view.md) as this generally does not work out well.
-   Do not drag TechDraw objects in the [Tree view](Tree_view.md) with the mouse.

## Tutorials

-   [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md): introduction to creating drawings with the TechDraw Workbench.
-   [Creating a new template](TechDraw_TemplateHowTo.md): instructions to create a new page template in Inkscape for using with the TechDraw Workbench.
-   [TechDraw TemplateGenerator](TechDraw_TemplateGenerator.md): instructions to create a macro for generating a basic template.

:   A \"few\" added lines of code result in a tool like the [Macro TemplateHelper](Macro_TemplateHelper.md).

-   [Measurement Of Angles On Holes](Measurement_Of_Angles_On_Holes.md): instructions for adding centerlines and subsequent angle representations on holes.
-   [Miscellaneous](TechDraw_HowTo_Page.md): instructions for different settings like center marks, etc.
-   [TechDraw Pitch Circle Tutorial](TechDraw_Pitch_Circle_Tutorial.md): instructions for adding a pitch circle.

Video tutorials by sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)

## Development

Do you want to know about the future of the TechDraw Workbench? Visit [the TechDraw Roadmap Page](TechDraw_Roadmap.md) to learn more.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [TechDraw](Category_TechDraw.md) > TechDraw Workbench/uk
