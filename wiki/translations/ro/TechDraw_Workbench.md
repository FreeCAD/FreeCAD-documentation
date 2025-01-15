# <img alt="TechDraw workbench icon" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/ro



## Introducere


<div class="mw-translate-fuzzy">

Tehnologia [ TechDraw Workbench](TechDraw_Workbench.md) este utilizată pentru a produce desene tehnice de bază de la modele 3D create cu un alt atelier de lucru, cum ar fi [Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), sau [Arch](Arch_Workbench.md),sau importate din alte aplicații. Fiecare desen este o pagină care poate conține diferite Vizualizări ale obiectelor trasabile cum ar fi Part::Features, PartDesign::Bodies, App::Part groups, și Document Object groups. Desenele rezultate pot fi folosite pentru lucruri precum documentație, instrucțiunile de fabricație, contracte, permise etc.


</div>

La pagină pot fi adăugate simboluri, secțiuni, suprafețe hașurate, adnotări și simboluri [SVG](SVG.md), care pot fi exportate în continuare în diferite formate ca [DXF](DXF.md), [SVG](SVG.md) și [PDF](PDF.md).


<div class="mw-translate-fuzzy">

FreeCAD este în primul rând o aplicație de modelare 3D și, prin urmare, nu are multe instrumente de desenare 2D, care sunt incluse în cea mai mare parte în [ Draft](Draft_Workbench.md) și [Sketcher Workbench](Sketcher_Workbench.md). Dacă obiectivul dvs. principal constă în realizarea de desene complexe 2D și [DXF](DXF.md) și nu aveți nevoie de modelare 3D, vă recomandăm să luați în considerare un program software dedicat pentru redactarea tehnică, cum ar fi \[https: //en.wikipedia .org / wiki / LibreCAD LibreCAD\], [QCad](https://en.wikipedia.org/wiki/QCad), TurboCad și altele.


</div>




<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Snapping


<small>(v1.0)</small> 

: The TechDraw Workbench has a snapping feature. It can be used to automatically align views, section views and dimensions when positioning them by dragging with the mouse. With **Snap View Alignment** enabled (default) in the [preferences](TechDraw_Preferences#Snapping.md), views will snap to alignment with other views when close enough (**View Snapping Factor** setting). Dimensions are also snapped to other parallel dimensions and the dimension text can be snapped to the middle of the dimension line. Snapping can be temporarily disabled by holding down the **Alt** key.

## Tools




<div class="mw-translate-fuzzy">

## Pagini


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Insert Default Page](TechDraw_PageDefault.md): adaugă o nouă pagină utilizând [template](TechDraw_Templates.md) implicit.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Insert Page using Template](TechDraw_PageTemplate.md): Adaugă o nouă pagină utilizând o selecție [template](TechDraw_Templates.md).


</div>

-   <img alt="" src=images/TechDraw_FillTemplateFields.svg  style="width:32px;"> [Update template fields](TechDraw_FillTemplateFields.md): <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Redraw Page](TechDraw_RedrawPage.md): forces an update of the selected page.

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width:32px;"> [Print All Pages](TechDraw_PrintAll.md): prints all pages in a document. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Export Page as SVG](TechDraw_ExportPageSVG.md): Salvează o pagină ca fișier [SVG](SVG.md).


</div>

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Export Page as DXF](TechDraw_ExportPageDXF.md): saves the current page as [DXF](DXF.md) file.




<div class="mw-translate-fuzzy">

## Vederi


</div>

#### TechDraw views 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [New View](TechDraw_View/ro.md): adaugă o vedere de proiecție 2D a unui obiect.


</div>

-   <img alt="" src=images/TechDraw_BrokenView.svg  style="width:32px;"> [Insert Broken View](TechDraw_BrokenView.md): adds a broken view of one or more objects. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Insert Section View](TechDraw_SectionView.md): adaugă o vedere în secțiune transversală într-o vizualizarea existentă deja.


</div>

-   <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Insert Complex Section View](TechDraw_ComplexSection.md): inserts a cross-section view of an existing view based on a profile. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Insert Detail View](TechDraw_DetailView.md): adaugă un detaliu vizualizarea unei porțiuni dintr-o vizualizare existentă.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Insert Projection Group](TechDraw_ProjectionGroup.md): învocă un dialog pentru crearea vederilor multiple din mai multe direcții.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Insert Clip Group](TechDraw_ClipGroup.md): inserează un grup de vederi mascate în secțiune într-o pagină.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [New Symbol](TechDraw_Symbol.md): inserază un simbol cartezian [SVG](SVG.md) în pagină.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [New Image](TechDraw_Image.md): Inserează o imagine PNG or JPG [bitmap](bitmap.md) în pagină.


</div>

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width:32px;"> [Share View](TechDraw_ShareView.md): shares a view between multiple pages.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Turn View Frames On/Off](TechDraw_ToggleFrame.md): Comuntă on/off cadrele și etichete care înconjoară o pagină.


</div>

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:32px;"> [Project Shape](TechDraw_ProjectShape.md): creates projections of shapes in the [3D view](3D_view.md).

#### Views from other workbenches 

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Insert Active View](TechDraw_ActiveView.md): inserts a view of the active 3D view.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Insert Draft Workbench Object](TechDraw_DraftView.md): adaugă o vizualizare la un Obiect din Atelierul [Draft Workbench](Draft_Workbench.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Insert Arch Workbench Object](TechDraw_ArchView.md): adaugă o vizualizare la un obiect din Atelierul Arhitectură adaugă o vizualizare a [Arch Workbench](Arch_Workbench.md) [SectionPlane](Arch_SectionPlane.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Insert Spreadsheet View](TechDraw_SpreadsheetView.md): inserează o vizualizare a unei foi de calcul [Spreadsheet Workbench](Spreadsheet_Workbench.md) sheet.


</div>

### Stacking

These are tools for changing the stacking order which controls the apparent depth of views on a page.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Adjust Stacking Order:

  - <img alt="" src=images/TechDraw_StackTop.svg  style="width:32px;"> [Move view to top of stack](TechDraw_StackTop.md): moves views to the top of the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackBottom.svg  style="width:32px;"> [Move view to bottom of stack](TechDraw_StackBottom.md): moves views to the bottom of the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackUp.svg  style="width:32px;"> [Move view up one level](TechDraw_StackUp.md): moves views up one level in the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackDown.svg  style="width:32px;"> [Move view down one level](TechDraw_StackDown.md): moves views down one level in the stacking order. <small>(v0.21)</small> 




<div class="mw-translate-fuzzy">

## Cotare


</div>

-   <img alt="" src=images/TechDraw_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensions:

  - <img alt="" src=images/TechDraw_Dimension.svg  style="width:32px;"> [Insert Dimension](TechDraw_Dimension.md): adds a contextual dimension. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Insert Length Dimension](TechDraw_LengthDimension.md): adaugă o cotă tip lungime.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Insert Horizontal Dimension](TechDraw_HorizontalDimension.md): adaugă o cotă orizontală tip lungime.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [New Vertical](TechDraw_VerticalDimension.md): adaugă o cotă tip lungime verticală


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Insert Radius Dimension](TechDraw_RadiusDimension.md): adaugă o cotă pentru raza unui cerc sau a unui arc de cerc.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [New Diameter](TechDraw_DiameterDimension.md): adaugă o cotă pentru diametrul unui cerc sau a unui arc de cerc.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Insert Angle Dimension](TechDraw_AngleDimension.md): adaugă o cotă pentru un unghi sau pentru două margini drepte.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Insert 3-Point Angle Dimension](TechDraw_3PtAngleDimension.md): adaugă o cotă tip dimensiune unghiulară utilizând trei vârfuri.


</div>

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


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [New Links](TechDraw_LinkDimension.md): leagă o cotă existetnă de o formă geometrică 3 D


</div>

### Hatching


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Hatch Area](TechDraw_Hatch.md): aplică un model de hașurare dintr-un fișier, unei fațete


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md): aplică un model de trasură la o față folosind o specificație Autodesk PAT.


</div>

### Annotations


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Insert Annotation](TechDraw_Annotation.md): adaugă un bloc de text care servește ca adnotare


</div>

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


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [ClipPlus](TechDraw_ClipGroupAdd/ro.md): Adaugă o vedere existentă la un grup mască.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [ClipMinus](ClipGroupRemove/ro.md): Extrage o vedere dintr-un grup mascat.


</div>

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width:32px;"> [Move View](TechDraw_MoveView.md): moves a view and its dependents to a different page. Not available in <small>(v1.0)</small> .



## Caracteristici suplimentare 


<div class="mw-translate-fuzzy">

-   [Hatching](TechDraw_Hatching.md): explică diverse tehnici de hașurare.
-   [Line Groups](TechDraw_LineGroup.md): Grosimi implicite pot fi asignate diferitor tipuri de linie.
-   [Templates](TechDraw_Templates.md): șabloanele implicite definite pentru paginile de desen.


</div>

## Preferences


<div class="mw-translate-fuzzy">

## Setările de elecție 

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Preferences](TechDraw_Preferences.md): preferințele pentru valorile implicite ale paginii desenului, cum ar fi unghiul de proiectare, culori, dimensiunile textului și stilurile de linie.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programare 

Instrumentele TechDraw pot fi utilizate în [macros](macros.md) și din consola [Python](Python.md) utilizând două API-uri.

-   [TechDraw API](TechDraw_API.md)
-   [TechDrawGui API](TechDrawGui_API.md)


</div>

## Limitations

-   Do not cut, copy and paste TechDraw objects in the [Tree view](Tree_view.md) as this generally does not work out well.
-   Do not drag TechDraw objects in the [Tree view](Tree_view.md) with the mouse.



## Tutoriale


<div class="mw-translate-fuzzy">

-   [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md): introducere în crearea de desene cu TechDraw Workbench.
-   [ Crearea unui nou șablon](TechDraw_TemplateHowTo.md): instrucțiuni pentru crearea unui nou șablon de pagină în Inkscape pentru utilizarea cu TechDraw Workbench.


</div>

Video tutorials by sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)

## Development

Do you want to know about the future of the TechDraw Workbench? Visit [the TechDraw Roadmap Page](TechDraw_Roadmap.md) to learn more.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [TechDraw](Category_TechDraw.md) > TechDraw Workbench/ro
