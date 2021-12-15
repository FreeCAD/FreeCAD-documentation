# <img alt="TechDraw workbench icon" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/ro

## Introducere

Tehnologia [ TechDraw Workbench](TechDraw_Workbench.md) este utilizată pentru a produce desene tehnice de bază de la modele 3D create cu un alt atelier de lucru, cum ar fi [Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), sau [Arch](Arch_Workbench.md),sau importate din alte aplicații. Fiecare desen este o pagină care poate conține diferite Vizualizări ale obiectelor trasabile cum ar fi Part::Features, PartDesign::Bodies, App::Part groups, și Document Object groups. Desenele rezultate pot fi folosite pentru lucruri precum documentație, instrucțiunile de fabricație, contracte, permise etc.

La pagină pot fi adăugate simboluri, secțiuni, suprafețe hașurate, adnotări și simboluri [SVG](SVG.md), care pot fi exportate în continuare în diferite formate ca [DXF](DXF.md), [SVG](SVG.md) și [PDF](PDF.md).

TechDraw a fost oficial inclus în FreeCAD începând cu versiunea 0.17; acesta este destinat să înlocuiască [Drawing Workbench](Drawing_Workbench.md). Ambele benzi de lucru sunt încă furnizate în v0.17, dar Workbench-ul de desen poate fi eliminat în versiunile viitoare. Pentru a ține pasul cu planurile și evoluțiile TechDraw, vizitați [TechDraw Roadmap](TechDraw_Roadmap.md)..


<div class="mw-translate-fuzzy">

FreeCAD este în primul rând o aplicație de modelare 3D și, prin urmare, nu are multe instrumente de desenare 2D, care sunt incluse în cea mai mare parte în [ Draft](Draft_Workbench.md) și [Sketcher Workbench](Sketcher_Workbench.md). Dacă obiectivul dvs. principal constă în realizarea de desene complexe 2D și [DXF](DXF.md) și nu aveți nevoie de modelare 3D, vă recomandăm să luați în considerare un program software dedicat pentru redactarea tehnică, cum ar fi \[https: //en.wikipedia .org / wiki / LibreCAD LibreCAD\], [QCad](https://en.wikipedia.org/wiki/QCad), TurboCad și altele.


</div>


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Pagini

Acestea sunt instrumente pentru crearea obiectelor de pagină.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> _ implicit.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Redraw Page](TechDraw_RedrawPage.md): forces an update of the selected page. <small>(v0.19)</small> 

## Vederi

Acestea sunt instrumente pentru crearea de Vizualizare obiecte.

-   <img alt="" src=images/techdraw-view.png  style="width:32px;"> [New View](TechDraw_View/ro.md): adaugă o vedere de proiecție 2D a unui obiect.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Insert Active View](TechDraw_ActiveView.md): inserts a view of the active 3D view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Insert Projection Group](TechDraw_ProjectionGroup.md): învocă un dialog pentru crearea vederilor multiple din mai multe direcții.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Insert Section View](TechDraw_SectionView.md): adaugă o vedere în secțiune transversală într-o vizualizarea existentă deja.

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Insert Detail View](TechDraw_DetailView.md): adaugă un detaliu vizualizarea unei porțiuni dintr-o vizualizare existentă.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> _ [SectionPlane](Arch_SectionPlane.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> _ sheet.

## Măști

Acestea sunt instrumente pentru a crea și a gestiona vederile mascate Clip objects

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Insert Clip Group](TechDraw_ClipGroup.md): inserează un grup de vederi mascate în secțiune într-o pagină.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [ClipPlus](TechDraw_ClipGroupAdd/ro.md): Adaugă o vedere existentă la un grup mască.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [ClipMinus](ClipGroupRemove/ro.md): Extrage o vedere dintr-un grup mascat.

## Decorațiune

Acestea sunt instrumente pentru modificarea aspectului paginilor și al vizualizărilor.

-   <img alt="" src=images/techdraw-hatch.png  style="width:32px;"> [Hatch Area](TechDraw_Hatch.md): aplică un model de hașurare dintr-un fișier, unei fațete

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md): aplică un model de trasură la o față folosind o specificație Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> _ în pagină.

-   <img alt="" src=images/Techdraw-image.png  style="width:32px;"> _ în pagină.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Turn View Frames On/Off](TechDraw_ToggleFrame.md): Comuntă on/off cadrele și etichete care înconjoară o pagină.

## Cotare

Acestea sunt instrumente pentru a crea și lucra cu obiicte tip Cotă.

Cotele liniare pot fi bazate pe două puncte, o linie sau două linii.


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

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Insert Horizontal Extent Dimension](TechDraw_HorizontalExtentDimension.md): adds a horizontal extent dimension. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Insert Vertical Extent Dimension](TechDraw_VerticalExtentDimension.md): adds a vertical extent dimension. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [New Links](TechDraw_LinkDimension.md): leagă o cotă existetnă de o formă geometrică 3 D


</div>

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Insert Balloon Annotation](TechDraw_Balloon.md): adds a \"balloon\" annotation to a page. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Insert Landmark Dimension](TechDraw_LandmarkDimension.md): adds a landmark distance dimension. <small>(v0.19)</small> 

## Annotations

The annotation tools are for \"marking up\" a drawing with additional information.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Insert Annotation](TechDraw_Annotation.md): adaugă un bloc de text care servește ca adnotare

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


<div class="mw-translate-fuzzy">

## Import/Export


</div>

These are tools for exporting pages to other applications.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> _ file.

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


<div class="mw-translate-fuzzy">

## Limitări

-   -   TechDraw drawings and its API are not interchangeable with the [Drawing Workbench](Drawing_Workbench.md) and its API. It is possible to convert Drawing Pages to TechDraw Pages using a Python script (`moveViews.py`).

-   Este posibil să aveți atât TechDraw cât și Pagini de desen în același document FreeCAD, deoarece fiecare pagină este complet independentă una față de cealaltă.

-   Există diferențe minore în specificarea textelor editabile în șabloanele [SVG](SVG.md) în comparație cu modulul Desenare. În TechDraw, scalarea documentului SVG afectează poziția câmpurilor de text editabile. Vedeți discuția pe forum [Scala TechDraw șabloane](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271) pentru mai multe detalii.

-   Nu tăiați, copiați și lipiți obiecte TechDraw în vizualizarea arborescentă, deoarece în general aceasta nu funcționează bine.


</div>

## Tutoriale


<div class="mw-translate-fuzzy">

-   [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md): introducere în crearea de desene cu TechDraw Workbench.
-   [ Crearea unui nou șablon](TechDraw_TemplateHowTo.md): instrucțiuni pentru crearea unui nou șablon de pagină în Inkscape pentru utilizarea cu TechDraw Workbench.


</div>

Video tutorials by sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/ro
