# <img alt="L\'icona di TechDraw" src=images/Workbench_TechDraw.svg  style="width   *64px;"> TechDraw Workbench/it

## Introduzione

L\'ambiente <img alt="" src=images/Workbench_TechDraw.svg  style="width   *24px;"> [TechDraw](TechDraw_Workbench/it.md) serve per produrre disegni tecnici di base derivati dai modelli 3D creati con un altro ambiente di lavoro come [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md), o [Arch](Arch_Workbench/it.md), o importati da altre applicazioni. Ogni disegno è una pagina, che può contenere varie viste di oggetti disegnabili come Part   *   *Features, PartDesign   *   *Bodies, App   *   *Part groups, e gruppi Document Object. I disegni risultanti possono essere utilizzati per la documentazione, le istruzioni di costruzione, i contratti, i permessi, ecc.

Alla pagina possono essere aggiunte dimensioni, sezioni, aree tratteggiate, annotazioni e simboli [SVG](SVG/it.md), e la pagina può essere ulteriormente esportata in diversi formati come [DXF](DXF/it.md), [SVG](SVG/it.md), e [PDF](PDF/it.md).

TechDraw è stato incluso ufficialmente in FreeCAD a partire dalla versione 0.17; è destinato a sostituire l\'ambiente [Drawing](Drawing_Workbench/it.md) non più supportato. In v0.17 sono ancora forniti entrambi gli ambienti, ma nelle versioni future Drawing potrebbe essere rimosso. Per essere aggiornati sui piani e gli sviluppi di TechDraw, visitare la [Roadmap di TechDraw](TechDraw_Roadmap.md).


<div class="mw-translate-fuzzy">

FreeCAD è principalmente un\'applicazione di modellazione 3D, e quindi non ha molti strumenti di disegno 2D, che sono per lo più inclusi in [Draft](Draft_Workbench/it.md) e [Sketcher](Sketcher_Workbench/it.md). Se l\'obiettivo primario è la produzione di disegni 2D complessi, e di file [ DXF](DXF.md), e non si ha bisogno di modelli 3D, si può prendere in considerazione un programma software dedicato al disegno tecnico, come [LibreCAD](https   *//en.wikipedia.org/wiki/LibreCAD), [QCad](https   *//en.wikipedia.org/wiki/QCad), TurboCad e altri.


</div>


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width   *600px;">

## Pagine

Questi sono gli strumenti per crere gli oggetti Pagine.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width   *32px;"> [Nuovo disegno standard](TechDraw_PageDefault/it.md)   * aggiunge una nuova pagina utilizzando il [modello](TechDraw_Templates/it.md) predefinito.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width   *32px;"> [Nuovo disegno da modello](TechDraw_PageTemplate/it.md)   * aggiunge una nuova pagina utilizzando un [modello](TechDraw_Templates/it.md) selezionato.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width   *32px;"> [Ridisegna la pagina](TechDraw_RedrawPage/it.md)   * forza un aggiornamento della pagina selezionata. {{Version/it|0.19}}


</div>

## Viste

Questi sono gli strumenti per crere gli oggetti Viste.

-   <img alt="" src=images/TechDraw_View.svg  style="width   *32px;"> [Vista di oggetto](TechDraw_View/it.md)   * aggiunge una vista in proiezione 2D di un oggetto.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width   *32px;"> [Vista attiva](TechDraw_ActiveView/it.md)   * inserisce una vista della vista 3D attiva. {{Version/it|0.19}}


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width   *32px;"> [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)   * richiama una finestra di dialogo per creare molte viste di un oggetto da più direzioni.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width   *32px;"> [Vista di sezione](TechDraw_SectionView/it.md)   * aggiunge una vista in sezione trasversale di una vista esistente.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width   *32px;"> [Dettaglio](TechDraw_DetailView/it.md)   * aggiunge una vista di dettaglio di una porzione di una vista esistente.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width   *32px;"> [Vista di Draft](TechDraw_DraftView/it.md)   * aggiunge una vista di [Draft](Draft_Workbench/it.md) di un oggetto.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width   *32px;"> [Vista di Arch](TechDraw_ArchView/it.md)   * aggiunge una vista di un oggetto [Piano di sezione](Arch_SectionPlane/it.md) di [Arch](Arch_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width   *32px;"> [Vista di foglio di calcolo](TechDraw_SpreadsheetView/it.md)   * inserisce in un disegno una vista di un [foglio di calcolo](Spreadsheet_Workbench/it.md) selezionato.


</div>

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width   *32px;"> [Move View](TechDraw_MoveView.md)   * Moves a view and its dependents to a different page. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width   *32px;"> [Share View](TechDraw_ShareView.md)   * Share a view between multiple pages. <small>(v0.20)</small> 

## Clip

Questi sono strumenti per creare e gestire gli oggetti Clip (ritagli di viste).


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width   *32px;"> [Gruppo di clip](TechDraw_ClipGroup/it.md)   * inserisce un gruppo di clip in una pagina.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width   *32px;"> [Aggiungi una vista al gruppo clip](TechDraw_ClipGroupAdd/it.md)   * aggiunge una vista esistente a un gruppo di clip.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width   *32px;"> [Rimuovi la vista dal gruppo clip](TechDraw_ClipGroupRemove/it.md)   * rimuove una vista da un gruppo di clip.


</div>

## Aspetto

Si tratta di strumenti per modificare l\'aspetto delle pagine e della vista.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width   *32px;"> [Tratteggio da modello](TechDraw_Hatch/it.md)   * applica a una faccia un modello di tratteggio preso da un file.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *32px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md)   * tratteggia una faccia usando uno specifico Autodesk PAT.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width   *32px;"> [Simbolo SVG](TechDraw_Symbol/it.md)   * inserisce un simbolo [SVG](SVG/it.md) in una pagina.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Image.svg  style="width   *32px;"> [Immagine bitmap](TechDraw_Image/it.md)   * inserisce un\'immagine [bitmap](bitmap/it.md) PNG o JPG in una pagina.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width   *32px;"> [Attiva o disattiva la cornice](TechDraw_ToggleFrame/it.md)   * mostra o nasconde le cornici e le etichette che circondano una vista.


</div>

## Dimensioni

Questi sono strumenti per creare e lavorare con gli oggetti Dimension.

Le dimensioni lineari possono essere basate su due punti, su una linea o su due linee.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width   *32px;"> [Lunghezza](TechDraw_LengthDimension/it.md)   * aggiunge una dimensione di lunghezza.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width   *32px;"> [Quota orizzontale](TechDraw_HorizontalDimension/it.md)   * aggiunge una dimensione orizzontale di lunghezza.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width   *32px;"> [Quota verticale](TechDraw_VerticalDimension/it.md)   * aggiunge una dimensione verticale.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width   *32px;"> [Raggio](TechDraw_RadiusDimension/it.md)   * aggiunge una dimensione raggio a un cerchio o arco.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width   *32px;"> [Diametro](TechDraw_DiameterDimension/it.md)   * aggiunge una dimensione di diametro a un cerchio o un arco.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width   *32px;"> [Angolo](TechDraw_AngleDimension/it.md)   * aggiunge una misura di angolo tra due bordi diritti.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width   *32px;"> [Angolo da 3 punti](TechDraw_3PtAngleDimension/it.md)   * aggiunge una quota angolare usando tre vertici.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width   *32px;"> [Estensione orizzontale](TechDraw_HorizontalExtentDimension/it.md)   * aggiunge una dimensione di estensione orizzontale. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width   *32px;"> [Estensione verticale](TechDraw_VerticalExtentDimension/it.md)   * aggiunge una dimensione di estensione verticale. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width   *32px;"> [Link alla geometria 3D](TechDraw_LinkDimension/it.md)   * collega una dimensione esistente alla geometria 3D.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width   *32px;"> [Pallinatura](TechDraw_Balloon/it.md)   * aggiunge un\'annotazione \"Pallino\" a una pagina. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width   *32px;"> [Quota da punti di riferimento](TechDraw_LandmarkDimension/it.md)   * aggiunge una dimensione basata su punti di riferimento. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

## Annotazioni


</div>

Gli strumenti di annotazione servono per \"commentare\" un disegno con informazioni aggiuntive.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width   *32px;"> [Annotazione](TechDraw_Annotation/it.md)   * aggiunge un blocco di testo normale da utilizzare come annotazione.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width   *24px;"> [Linea guida](TechDraw_LeaderLine/it.md)   * aggiunge una linea di annotazione a una vista. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width   *24px;"> [Blocco di testo](TechDraw_RichTextAnnotation/it.md)   * aggiunge un blocco di annotazione rich text a una [Linea guida](TechDraw_LeaderLine/it.md) o una vista. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width   *24px;"> [Vertice cosmetico](TechDraw_CosmeticVertex/it.md)   * Lo strumento Vertice cosmetico aggiunge un vertice che non fa parte della geometria originale. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width   *24px;"> [Punti mediani](TechDraw_Midpoints/it.md)   * Lo strumento Punti mediani aggiunge dei Vertici cosmetici nei punti medi di uno o più bordi. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width   *24px;"> [Quadrante](TechDraw_Quadrants/it.md)   * Lo strumento Quadrante aggiunge dei Vertici cosmetici nei punti quarti di uno o più bordi circolari. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width   *24px;"> [Linea a centro faccia](TechDraw_FaceCenterLine/it.md)   * Lo strumento Linea a centro faccia aggiunge una linea centrale alle facce selezionate. {{Version/it|0.19}}


</div>

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width   *24px;"> [Linea centrale a 2 linee](TechDraw_2LineCenterLine/it.md)   * Lo strumento Linea a centro linee aggiunge una linea centrale tra 2 bordi. {{Version/it|0.19}}

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width   *24px;"> [Linea centrale a 2 punti](TechDraw_2PointCenterLine/it.md)   * Lo strumento Linea a centro punti aggiunge una linea centrale tra 2 punti. {{Version/it|0.19}}


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width   *24px;"> [Linea tra due punti](TechDraw_2PointCosmeticLine/it.md)   * aggiunge una linea cosmetica che collega 2 vertici. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width   *24px;"> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)   * Lo strumento Rimuovi oggetto cosmetico rimuove gli oggetti cosmetici da una pagina. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width   *24px;"> [Aspetto delle linee](TechDraw_DecorateLine/it.md)   * Lo strumento DecorateLine modifica l\'aspetto dei bordi. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width   *24px;"> [Mostra/nascondi i bordi invisibili](TechDraw_ShowAll/it.md)   * Lo strumento mostra o nasconde i bordi impostati invisibili in una vista. {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width   *24px;"> [Informazioni di saldatura](TechDraw_WeldSymbol/it.md)   * Lo strumento Informazioni di saldatura aggiunge le specifiche di saldatura a una linea guida esistente. {{Version/it|0.19}}


</div>

## Extensions

These are tools to improve your TechDraw drawings.

### Attributes and modifications 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width   *32px;"> [Select Line Attributes, Cascade Spacing and Delta Distance](TechDraw_ExtensionSelectLineAttributes.md)   * selects the attributes (style, width and color) for new cosmetic lines and centerlines, and specifies the cascade spacing and delta distance. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width   *32px;"> [Change Line Attributes](TechDraw_ExtensionChangeLineAttributes.md)   * changes the attributes (style, width and color) of cosmetic lines and centerlines. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width   *32px;"> [Extend Line](TechDraw_ExtensionExtendLine.md)   * extends a cosmetic line or centerline at both ends. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width   *32px;"> [Shorten Line](TechDraw_ExtensionShortenLine.md)   * shortens a cosmetic line or centerline at both ends. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width   *32px;"> [Lock/Unlock View](TechDraw_ExtensionLockUnlockView.md)   * locks or unlocks the position of a view. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width   *32px;"> [Position Section View](TechDraw_ExtensionPositionSectionView.md)   * orthogonally aligns a section view with its source view. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width   *32px;"> [Position Horizontal Chain Dimensions](TechDraw_ExtensionPosHorizChainDimension.md)   * aligns horizontal dimensions to create a chain dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width   *32px;"> [Position Vertical Chain Dimensions](TechDraw_ExtensionPosVertChainDimension.md)   * aligns vertical dimensions to create a chain dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width   *32px;"> [Position Oblique Chain Dimensions](TechDraw_ExtensionPosObliqueChainDimension.md)   * aligns oblique dimensions to create a chain dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width   *32px;"> [Cascade Horizontal Dimensions](TechDraw_ExtensionCascadeHorizDimension.md)   * evenly spaces horizontal dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width   *32px;"> [Cascade Vertical Dimensions](TechDraw_ExtensionCascadeVertDimension.md)   * evenly spaces vertical dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width   *32px;"> [Cascade Oblique Dimensions](TechDraw_ExtensionCascadeObliqueDimension.md)   * evenly spaces oblique dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width   *32px;"> [Calculate the area of selected faces](TechDraw_ExtensionAreaAnnotation.md)   * calculates the area of selected faces and inserts an area annotation. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width   *32px;"> [Customize format label](TechDraw_ExtensionCustomizeFormat.md)   * customizes the formatting of a balloon text or dimension text. GD&T symbols and other special character can be added. <small>(v0.20)</small> 

### Centerlines and threading 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width   *32px;"> [Add Circle Centerlines](TechDraw_ExtensionCircleCenterLines.md)   * adds centerlines to circles and arcs. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width   *32px;"> [Add Bolt Circle Centerlines](TechDraw_ExtensionHoleCircle.md)   * adds centerlines to a circular pattern of circles. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width   *32px;"> [Add Cosmetic Thread Hole Side View](TechDraw_ExtensionThreadHoleSide.md)   * adds a cosmetic thread to the side view of a hole. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width   *32px;"> [Add Cosmetic Thread Hole Bottom View](TechDraw_ExtensionThreadHoleBottom.md)   * adds a cosmetic thread to the top or bottom view of holes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width   *32px;"> [Add Cosmetic Thread Bolt Side View](TechDraw_ExtensionThreadBoltSide.md)   * adds a cosmetic thread to the side view of a bolt/screw/rod. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width   *32px;"> [Add Cosmetic Thread Bolt Bottom View](TechDraw_ExtensionThreadBoltBottom.md)   * adds a cosmetic thread to the top or bottom view of bolts/screws/rods. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width   *32px;"> [Add Cosmetic Intersection Vertex(es)](TechDraw_ExtensionVertexAtIntersection.md)   * adds cosmetic vertex(es) at the intersection(s) of selected edges. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width   *32px;"> [Add Cosmetic Circle](TechDraw_ExtensionDrawCosmCircle.md)   * adds a cosmetic circle based on two vertexes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width   *32px;"> [Add Cosmetic Arc](TechDraw_ExtensionDrawCosmArc.md)   * adds a cosmetic counter clockwise arc based on three vertexes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width   *32px;"> [Add Cosmetic Circle 3 Points](TechDraw_ExtensionDrawCosmCircle3Points.md)   * adds a cosmetic circle based on three vertexes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width   *32px;"> [Add Cosmetic Parallel Line](TechDraw_ExtensionLineParallel.md)   * adds a cosmetic line parallel to another line through a vertex. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width   *32px;"> [Add Cosmetic Perpendicular Line](TechDraw_ExtensionLinePerpendicular.md)   * adds a cosmetic line perpendicular to another line through a vertex. <small>(v0.20)</small> 

### Dimensions

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width   *32px;"> [Create Horizontal Chain Dimensions](TechDraw_ExtensionCreateHorizChainDimension.md)   * creates a sequence of aligned horizontal dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width   *32px;"> [Create Vertical Chain Dimensions](TechDraw_ExtensionCreateVertChainDimension.md)   * creates a sequence of aligned vertical dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width   *32px;"> [Create Oblique Chain Dimensions](TechDraw_ExtensionCreateObliqueChainDimension.md)   * creates a sequence of aligned oblique dimensions. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width   *32px;"> [Create Horizontal Coordinate Dimensions](TechDraw_ExtensionCreateHorizCoordDimension.md)   * creates multiple evenly spaced horizontal dimensions starting from the same baseline. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width   *32px;"> [Create Vertical Coordinate Dimensions](TechDraw_ExtensionCreateVertCoordDimension.md)   * creates multiple evenly spaced vertical dimensions starting from the same baseline. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width   *32px;"> [Create Oblique Coordinate Dimensions](TechDraw_ExtensionCreateObliqueCoordDimension.md)   * creates multiple evenly spaced oblique dimensions starting from the same baseline. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width   *32px;"> [Create Horizontal Chamfer Dimension](TechDraw_ExtensionCreateHorizChamferDimension.md)   * creates a horizontal size and angle dimension for a chamfer. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width   *32px;"> [Create Vertical Chamfer Dimension](TechDraw_ExtensionCreateVertChamferDimension.md)   * creates a vertical size and angle dimension for a chamfer. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width   *32px;"> [Create Arc Length Dimension](TechDraw_ExtensionCreateLengthArc.md)   * creates an arc length dimension. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width   *32px;"> [Insert \'⌀\' Prefix](TechDraw_ExtensionInsertDiameter.md)   * inserts a \'⌀\' symbol at the beginning of the dimension text. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width   *32px;"> [Insert \'〼\' Prefix](TechDraw_ExtensionInsertSquare.md)   * inserts a \'〼\' symbol at the beginning of the dimension text. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width   *32px;"> [Remove Prefix](TechDraw_ExtensionRemovePrefixChar.md)   * removes all symbols at the beginning of the dimension text. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width   *32px;"> [Increase Decimal Places](TechDraw_ExtensionIncreaseDecimal.md)   * increases the number of decimal places of the dimension text. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width   *32px;"> [Decrease Decimal Places](TechDraw_ExtensionDecreaseDecimal.md)   * decreases the number of decimal places of the dimension text. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

## Importazione e Esportazione 


</div>

Questi sono gli strumenti per esportare le pagine in altre applicazioni.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width   *32px;"> [Esporta pagina in SVG](TechDraw_ExportPageSVG/it.md)   * salva una pagina come file [SVG](SVG/it.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width   *32px;"> [Export Page as DXF](TechDraw_ExportPageDXF/it.md)   * salva la pagina corrente come file [DXF](DXF.md).


</div>

## Ulteriori funzioni 


<div class="mw-translate-fuzzy">

-   [Gruppi di linee](TechDraw_LineGroup/it.md)   * si possono assegnare valori di default a vari tipi di linee.
-   [Modelli di squadrature](TechDraw_Templates/it.md)   * i modelli predefiniti per le pagine di disegno di TechDraw.
-   [Tipi di tratteggio](TechDraw_Hatching/it.md)   * spiegazione delle diverse tecniche di tratteggio.
-   [Dimensionamento e tolleranza geometrica](TechDraw_Geometric_dimensioning_and_tolerancing/it.md)   * spiegazione su come realizzare la quotatura geometrica e la tolleranza.


</div>

## Preferences


<div class="mw-translate-fuzzy">

## Preferenze

-   <img alt="" src=images/Preferences-techdraw.svg  style="width   *32px;"> [Preferenze di TechDraw](TechDraw_Preferences/it.md)   * le preferenze per i valori predefiniti della pagina di disegno come l\'angolo di proiezione, i colori, le dimensioni del testo e gli stili di linea.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script

Gli strumenti TechDraw possono essere utilizzati nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando due API.

-   [API TechDraw](TechDraw_API/it.md)
-   [API TechDrawGui](TechDrawGui_API/it.md)


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Limitazioni

-   I disegni di TechDraw e le relative API non sono intercambiabili con i disegni di [Drawing](Drawing_Workbench/it.md) e le relative API. È possibile convertire le pagine di Drawing in pagine TechDraw utilizzando uno script Python (`moveViews.py`).
-   Nello stesso documento di FreeCAD è possibile avere sia pagine di TechDraw che pagine di Drawing, poiché ciascuna pagina è completamente indipendente l\'una dall\'altra.
-   Ci sono alcune piccole differenze nello specificare i testi modificabili nei modelli [SVG](SVG/it.md) rispetto al modulo Drawing. In TechDraw il ridimensionamento del documento SVG influisce sulla posizione dei campi di testo modificabili. Per maggiori dettagli vedere la discussione sul forum [TechDraw templates scale](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271).
-   Non tagliare, copiare e incollare oggetti TechDraw nella vista ad albero, in quanto generalmente non funziona bene.


</div>

## Tutorial


<div class="mw-translate-fuzzy">

-   [Tutorial base di TechDraw](Basic_TechDraw_Tutorial/it.md)   * introduzione alla creazione di disegni con TechDraw.
-   [Come creare dei modelli TechDraw personalizzati](TechDraw_TemplateHowTo/it.md)   * istruzioni per creare un nuovo modello di pagina in Inkscape per l\'utilizzo con TechDraw.
-   [Misura degli angoli sui fori](Measurement_Of_Angles_On_Holes/it.md)   * istruzioni per l\'aggiunta di linee centrali e successive rappresentazioni angolari sui fori.
-   [Informazioni pratiche su TechDraw](TechDraw_HowTo_Page/it.md)   * istruzioni per diverse impostazioni come i segni di centratura, ecc.
-   [Asse circolare](TechDraw_Pitch_Circle_Tutorial.md)   * istruzioni per aggiungere un asse circolare.


</div>

Video tutorial di sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https   *//www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https   *//www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https   *//www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https   *//www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https   *//www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/it
