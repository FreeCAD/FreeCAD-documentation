# TechDraw Workbench/es
<div class="mw-translate-fuzzy">





</div>

<img alt="El icono del Ambiente de trabajo Dibujo Técnico" src=images/Workbench_TechDraw.svg  style="width:128px;">



## Introducción


<div class="mw-translate-fuzzy">

El <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Ambiente de trabajos Croquizador](TechDraw_Workbench/es.md) se utiliza para producir dibujos técnicos básicos a partir de modelos 3D creados con otro Ambiente de trabajos como [Part](Part_Workbench/es.md), [PartDesign](PartDesign_Workbench/es.md), o [Arch](Arch_Workbench/es.md), o importados de otras aplicaciones. Cada dibujo es una Página, que puede contener varias Vistas de objetos dibujables como Part::Características, PartDesign::Cuerpos, App::Grupos de piezas, y Grupos de objetos de documentos. Los dibujos resultantes pueden ser utilizados para cosas como documentación, instrucciones de fabricación, contratos, permisos, etc.


</div>

Dimensiones, secciones, áreas sombreadas, anotaciones y [SVG](SVG/es.md) símbolos se pueden añadir a la página, que se pueden exportar a diferentes formatos como [DXF](DXF/es.md), [SVG](SVG/es.md) y [PDF](PDF/es.md).


<div class="mw-translate-fuzzy">

FreeCAD es principalmente una aplicación de modelado en 3D, y por lo tanto no tiene muchas herramientas de dibujo en 2D, las cuales están incluidas en su mayoría en el [Draft](Draft_Workbench/es.md) y [Ambiente des trabajo Croquizador](Sketcher_Workbench/es.md). Si su objetivo principal es la producción de complejos dibujos 2D y archivos [DXF](DXF/es.md), y no necesita modelado 3D, puede considerar un programa de software dedicado al dibujo técnico como [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), TurboCad, y otros.


</div>




<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Snapping


<small>(v1.0)</small> 

: The TechDraw Workbench has a snapping feature. It can be used to automatically align views, section views and dimensions when positioning them by dragging with the mouse. With **Snap View Alignment** enabled (default) in the [preferences](TechDraw_Preferences#Snapping.md), views will snap to alignment with other views when close enough (**View Snapping Factor** setting). Dimensions are also snapped to other parallel dimensions and the dimension text can be snapped to the middle of the dimension line. Snapping can be temporarily disabled by holding down the **Alt** key.

## Tools




<div class="mw-translate-fuzzy">

## Páginas


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Insertar página predeterminada](TechDraw_PageDefault/es.md): Agrega una nueva página usando el predeterminado [Plantilla](TechDraw_Templates/es.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Insertar la página usando la plantilla](TechDraw_PageTemplate/es.md): Agrega una nueva página usando un seleccionado [Plantilla](TechDraw_Templates/es.md).


</div>

-   <img alt="" src=images/TechDraw_FillTemplateFields.svg  style="width:32px;"> [Update template fields](TechDraw_FillTemplateFields.md): <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Redibujar página](TechDraw_RedrawPage/es.md): fuerza una actualización de la página seleccionada. <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width:32px;"> [Print All Pages](TechDraw_PrintAll.md): prints all pages in a document. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Exportar página como SVG](TechDraw_ExportPageSVG/es.md): guarda la página actual como archivo [SVG](SVG/es.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Exportar página como DXF](TechDraw_ExportPageDXF/es.md): guarda la página actual como archivo [DXF](DXF/es.md).


</div>




<div class="mw-translate-fuzzy">

## Vistas


</div>

#### TechDraw views 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Insertar Vista](TechDraw_View/es.md): Agrega una vista de proyección 2D de un objeto.


</div>

-   <img alt="" src=images/TechDraw_BrokenView.svg  style="width:32px;"> [Insert Broken View](TechDraw_BrokenView.md): adds a broken view of one or more objects. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Insertar vista de sección](TechDraw_SectionView/es.md): inserta una vista de sección transversal de una vista existente.


</div>

-   <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Insert Complex Section View](TechDraw_ComplexSection.md): inserts a cross-section view of an existing view based on a profile. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Insertar la vista detallada](TechDraw_DetailView/es.md): Agrega una vista detallada de una parte de una vista existente.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Insertar el Grupo de Proyección](TechDraw_ProjectionGroup/es.md): Invoca un diálogo para crear vistas de uno o más objetos dibujables desde múltiples direcciones.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Inserta un grupo de clip](TechDraw_ClipGroup/es.md): Inserta un grupo de clip en una página.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [Insertar símbolo SVG](TechDraw_Symbol/es.md): inserta un símbolo de un archivo [SVG](SVG/es.md) en una página.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Insertar Bitmap imagen](TechDraw_Image/es.md): inserta una imagen PNG o JPG [bitmap](bitmap/es.md) en una página.


</div>

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width:32px;"> [Share View](TechDraw_ShareView.md): shares a view between multiple pages.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Turn View Frames On/Off](TechDraw_ToggleFrame/es.md): activa y desactiva ver marcos y etiquetas que rodean una vista.


</div>

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:32px;"> [Project Shape](TechDraw_ProjectShape.md): creates projections of shapes in the [3D view](3D_view.md).

#### Views from other workbenches 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Insertar la vista activa](TechDraw_ActiveView/es.md): inserta una vista de la vista 3D activa. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Insertar el borrador del objeto de l\'ambiente de trabajo](TechDraw_DraftView/es.md) Inserta una vista de un objeto [Draft ambiente de trabajo](Draft_Workbench/es.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Insertar Ambiente de trabajo architectura Objeto](TechDraw_ArchView/es.md): Agrega una vista de un [Architectura Ambiente de trabajo](Arch_Workbench/es.md) [Plano de la sección](Arch_SectionPlane/es.md) objeto.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Insertar Spreadsheet Vista](TechDraw_SpreadsheetView/es.md): Inserta una vista de una [Spreadsheet Ambiente de trabajo](Spreadsheet_Workbench/es.md) sheet.


</div>

### Stacking

These are tools for changing the stacking order which controls the apparent depth of views on a page.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Adjust Stacking Order:

  - <img alt="" src=images/TechDraw_StackTop.svg  style="width:32px;"> [Move view to top of stack](TechDraw_StackTop.md): moves views to the top of the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackBottom.svg  style="width:32px;"> [Move view to bottom of stack](TechDraw_StackBottom.md): moves views to the bottom of the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackUp.svg  style="width:32px;"> [Move view up one level](TechDraw_StackUp.md): moves views up one level in the stacking order. <small>(v0.21)</small> 

  - <img alt="" src=images/TechDraw_StackDown.svg  style="width:32px;"> [Move view down one level](TechDraw_StackDown.md): moves views down one level in the stacking order. <small>(v0.21)</small> 




<div class="mw-translate-fuzzy">

## Dimensiones


</div>

-   <img alt="" src=images/TechDraw_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensions:

  - <img alt="" src=images/TechDraw_Dimension.svg  style="width:32px;"> [Insert Dimension](TechDraw_Dimension.md): adds a contextual dimension. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Nueva longitud](TechDraw_LengthDimension/es.md): Agrega una dimensión de longitud.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Nuevo Horizontal](TechDraw_HorizontalDimension/es.md): Agrega una dimensión de distancia horizontal.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Nueva vertical](TechDraw_VerticalDimension/es.md): Agrega una dimensión de distancia vertical.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Nuevo radio](TechDraw_RadiusDimension/es.md): Agrega una dimensión de radio a un círculo o arco circular.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Nuevo Diámetro](TechDraw_DiameterDimension/es.md): Agrega una dimensión de Diámetro a un círculo o un arco circular.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Nuevo Ángulo](TechDraw_AngleDimension/es.md): Agrega una dimensión de Ángulo entre dos bordes rectos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Nuevo ángulo3Pt](TechDraw_3PtAngleDimension/es.md):

Agrega una dimensión de ángulo usando tres vértices.


</div>

  - <img alt="" src=images/TechDraw_AreaDimension.svg  style="width:32px;"> [Insert Area Annotation](TechDraw_AreaDimension.md): adds an area dimension to a face. <small>(v1.0)</small> 

  - <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Create Arc Length Dimension](TechDraw_ExtensionCreateLengthArc.md): creates an arc length dimension.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Nueva extensión horizontal](TechDraw_HorizontalExtentDimension/es.md): agrega una dimensión de extensión horizontal. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Nueva extensión vertical](TechDraw_VerticalExtentDimension/es.md): agrega una dimensión de extensión vertical. <small>(v0.19)</small> 


</div>

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Create Horizontal Chain Dimensions](TechDraw_ExtensionCreateHorizChainDimension.md): creates a sequence of aligned horizontal dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Create Vertical Chain Dimensions](TechDraw_ExtensionCreateVertChainDimension.md): creates a sequence of aligned vertical dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Create Oblique Chain Dimensions](TechDraw_ExtensionCreateObliqueChainDimension.md): creates a sequence of aligned oblique dimensions.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Create Horizontal Coordinate Dimensions](TechDraw_ExtensionCreateHorizCoordDimension.md): creates multiple evenly spaced horizontal dimensions starting from the same baseline.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Create Vertical Coordinate Dimensions](TechDraw_ExtensionCreateVertCoordDimension.md): creates multiple evenly spaced vertical dimensions starting from the same baseline.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Create Oblique Coordinate Dimensions](TechDraw_ExtensionCreateObliqueCoordDimension.md): creates multiple evenly spaced oblique dimensions starting from the same baseline.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Create Horizontal Chamfer Dimension](TechDraw_ExtensionCreateHorizChamferDimension.md): creates a horizontal size and angle dimension for a chamfer.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Create Vertical Chamfer Dimension](TechDraw_ExtensionCreateVertChamferDimension.md): creates a vertical size and angle dimension for a chamfer.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Globo nuevo](TechDraw_Balloon/es.md): agrega una anotación de \"globo\" a una página. <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/TechDraw_AxoLengthDimension.svg  style="width:32px;"> [Insert Axonometric Length Dimension](TechDraw_AxoLengthDimension.md): adds an axonometric length dimension. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Nueva dimensión del hito](TechDraw_LandmarkDimension/es.md): agrega una dimensión de distancia de referencia. <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:32px;"> [Dimension Repair](TechDraw_DimensionRepair.md): can adjust the 2D or 3D geometry references of a dimension. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Nuevos enlaces](TechDraw_LinkDimension/es.md): Vincula 1 o más dimensiones a la geometría 3D.


</div>

### Hatching


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Achurado plano utilizar un archivo de imagen](TechDraw_Hatch/es.md): Aplica un achurado patrón desde un archivo a uno plano.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Geometric Hatch](TechDraw_GeometricHatch/es.md): aplica una sombrea uno plano usando una especificación PAT de Autodesk.


</div>




<div class="mw-translate-fuzzy">

## Anotación


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Insertar Anotación](TechDraw_Annotation/es.md): Agrega un bloque de texto simple como anotación.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:24px;"> [Añadir Leaderline a la vista](TechDraw_LeaderLine/es.md): añade una línea de anotación a una vista. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:24px;"> [Insertar Anotación de Texto Enriquecido](TechDraw_RichTextAnnotation/es.md): añade un bloque de texto enriquecido como anotación a una línea de liderazgo o a una vista. {{Version/es|0.19}}


</div>

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Cosmetic Vertices:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:24px;"> [Agrega Vértice Cosmético](TechDraw_CosmeticVertex/es.md): agrega un Vértice que no es parte de la geometría de la fuente. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:24px;"> [Agregar Punto Medio Vértices](TechDraw_Midpoints/es.md): agrega vértices cosméticos en los puntos medios de los bordes seleccionados. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:24px;"> [Agregar Vértices de Cuadrante](TechDraw_Quadrants/es.md): agrega Vértices Cosméticos en los cuartos de punto de los bordes seleccionados (circulares). {{Version/es|0.19}}


</div>

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Add Centerlines:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:24px;"> [Añadir línea central a las caras](TechDraw_FaceCenterLine/es.md): añade una línea central a las caras seleccionadas. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:24px;"> [Añadir línea central entre 2 líneas](TechDraw_2LineCenterLine/es.md): añade una línea central entre 2 líneas. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:24px;"> [Añadir línea central entre 2 puntos](TechDraw_2PointCenterLine/es.md): añade una línea central entre 2 puntos. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:24px;"> [Añadir una línea cosmética](TechDraw_2PointCosmeticLine/es.md): añade una línea cosmética que conecta 2 vértices. {{Version/es|0.19}}


</div>

-   <img alt="" src=images/TechDraw_CosmeticCircle.svg  style="width:32px;"> [Add Cosmetic Circle](TechDraw_CosmeticCircle.md): adds a cosmetic circle. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:24px;"> [Cambiar la apariencia de las líneas](TechDraw_DecorateLine/es.md): cambia la apariencia de la(s) línea(s) seleccionada(s). {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:24px;"> [Mostrar/Ocultar Bordes Invisibles](TechDraw_ShowAll/es.md): muestra/oculta las líneas/bordes invisibles en una vista. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:24px;"> [Añadir información de soldadura a la línea de mando](TechDraw_WeldSymbol/es.md): añade especificaciones de soldadura a una línea de mando existente. {{Version/es|0.19}}


</div>

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


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:24px;"> [Eliminar objeto cosmético](TechDraw_CosmeticEraser/es.md): elimina los objetos cosméticos de una página.{{Version/es|0.19}}


</div>

### Obsolete tools 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Agrega vista al grupo de clips](TechDraw_ClipGroupAdd.md): Agrega una vista existente a un grupo de clip.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Eliminar la vista del grupo de clips](TechDraw_ClipGroupRemove/es.md): Elimina una vista de un grupo de clip.


</div>

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width:32px;"> [Move View](TechDraw_MoveView.md): moves a view and its dependents to a different page. Not available in <small>(v1.0)</small> .



## Características adicionales 


<div class="mw-translate-fuzzy">

-   [Grupos de líneas](TechDraw_LineGroup/es.md): para controlar la aparición de varios tipos de líneas.
-   [Plantillas](TechDraw_Templates/es.md): las plantillas por defecto definidas para las páginas de dibujo.
-   [Achurado](TechDraw_Hatching/es.md): explicación de las diferentes técnicas de achurado.
-   [Dimensionamiento y tolerancia geométricos](TechDraw_Geometric_dimensioning_and_tolerancing/es.md): explicación sobre cómo lograr el dimensionamiento y tolerancia geométricos.


</div>

## Preferences


<div class="mw-translate-fuzzy">

## Preferencias

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Preferencias](TechDraw_Preferences/es.md): preferencias para los valores por defecto de la página de dibujo como el ángulo de proyección, los colores, los tamaños de texto y los estilos de línea.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Guión

Las herramientas de TechDraw pueden ser utilizadas en [macros](macros/es.md) y desde la consola [Python](Python/es.md) utilizando dos APIs.

-   [TechDraw API](TechDraw_API/es.md)
-   [TechDrawGui API](TechDrawGui_API/es.md)


</div>

## Limitations

-   Do not cut, copy and paste TechDraw objects in the [Tree view](Tree_view.md) as this generally does not work out well.
-   Do not drag TechDraw objects in the [Tree view](Tree_view.md) with the mouse.



## Tutoriales


<div class="mw-translate-fuzzy">

-   [Tutorial básico de DibujoTécnico](Basic_TechDraw_Tutorial/es.md): Introducción a la creación de dibujos con el ambiente de trabajo DibujoTécnico.
-   [Creando una nueva plantilla](TechDraw_TemplateHowTo/es.md): instrucciones para crear una nueva plantilla de página en Inkscape para usarla con el ambiente de trabajo DibujoTécnico.
-   [Medición de los ángulos en los agujeros](Measurement_Of_Angles_On_Holes/es.md): instrucciones para añadir líneas centrales y posteriores representaciones de ángulos en los agujeros.
-   [Misceláneos](TechDraw_HowTo_Page/es.md): Instrucciones para diferentes configuraciones como marcas centrales, etc.
-   [Crear un círculo de cabeceo](TechDraw_Pitch_Circle_Tutorial/es.md): instrucciones para añadir un círculo de cabeceo


</div>

Tutoriales de vídeo de sliptonic

-   Ambiente de trabajo TechDraw [Parte 1 (Básico)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Parte 2 (Dimensiones)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Parte 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   Ambiente de trabajo de TechDraw [Parte 4 (Sección y detalle)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Parte 5 (Plantillas de personalización)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)

## Development

Do you want to know about the future of the TechDraw Workbench? Visit [the TechDraw Roadmap Page](TechDraw_Roadmap.md) to learn more.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [TechDraw](Category_TechDraw.md) > TechDraw Workbench/es
