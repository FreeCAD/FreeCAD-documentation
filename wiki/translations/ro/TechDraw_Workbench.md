# TechDraw Workbench/ro






<img alt="TechDraw workbench icon" src=images/Workbench_TechDraw.svg  style="width:128px;">

## Introducere

Tehnologia [ TechDraw Workbench](TechDraw_Workbench.md) este utilizată pentru a produce desene tehnice de bază de la modele 3D create cu un alt atelier de lucru, cum ar fi [Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), sau [Arch](Arch_Workbench.md),sau importate din alte aplicații. Fiecare desen este o pagină care poate conține diferite Vizualizări ale obiectelor trasabile cum ar fi Part::Features, PartDesign::Bodies, App::Part groups, și Document Object groups. Desenele rezultate pot fi folosite pentru lucruri precum documentație, instrucțiunile de fabricație, contracte, permise etc.

La pagină pot fi adăugate simboluri, secțiuni, suprafețe hașurate, adnotări și simboluri [SVG](SVG.md), care pot fi exportate în continuare în diferite formate ca [DXF](DXF.md), [SVG](SVG.md) și [PDF](PDF.md).

TechDraw a fost oficial inclus în FreeCAD începând cu versiunea 0.17; acesta este destinat să înlocuiască [Drawing Workbench](Drawing_Workbench.md). Ambele benzi de lucru sunt încă furnizate în v0.17, dar Workbench-ul de desen poate fi eliminat în versiunile viitoare. Pentru a ține pasul cu planurile și evoluțiile TechDraw, vizitați [TechDraw Roadmap](TechDraw_Roadmap.md)..

FreeCAD este în primul rând o aplicație de modelare 3D și, prin urmare, nu are multe instrumente de desenare 2D, care sunt incluse în cea mai mare parte în [ Draft](Draft_Workbench.md) și [Sketcher Workbench](Sketcher_Workbench.md). Dacă obiectivul dvs. principal constă în realizarea de desene complexe 2D și [DXF](DXF.md) și nu aveți nevoie de modelare 3D, vă recomandăm să luați în considerare un program software dedicat pentru redactarea tehnică, cum ar fi \[https: //en.wikipedia .org / wiki / LibreCAD LibreCAD\], [QCad](https://en.wikipedia.org/wiki/QCad), TurboCad și altele.


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Pagini

Acestea sunt instrumente pentru crearea obiectelor de pagină.

-   <img alt="" src=images/TechDraw_New_Default.png  style="width:32px;"> [New Default](TechDraw_New_Default.md): adaugă o nouă pagină utilizând [template](TechDraw_Templates.md) implicit.

-   <img alt="" src=images/TechDraw_New_Pick.png  style="width:32px;"> [New Pick](TechDraw_New_Pick.md): Adaugă o nouă pagină utilizând o selecție [template](TechDraw_Templates.md).

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Redraw Page](TechDraw_RedrawPage.md): forces an update of the selected page. <small>(v0.19)</small> 

## Vederi

Acestea sunt instrumente pentru crearea de Vizualizare obiecte.

-   <img alt="" src=images/techdraw-view.png  style="width:32px;"> [New View](TechDraw_View/ro.md): adaugă o vedere de proiecție 2D a unui obiect.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Insert Active View](TechDraw_ActiveView.md): inserts a view of the active 3D view. <small>(v0.19)</small> 

-   <img alt="" src=images/techdraw-projgroup.png  style="width:32px;"> [New Projection Group](TechDraw_NewProjGroup.md): învocă un dialog pentru crearea vederilor multiple din mai multe direcții.

-   <img alt="" src=images/techdraw-viewsection.png  style="width:32px;"> [New Section](TechDraw_NewSection.md): adaugă o vedere în secțiune transversală într-o vizualizarea existentă deja.

-   <img alt="" src=images/techdraw-viewdetail.png  style="width:32px;"> [New Detail](TechDraw_NewDetail.md): adaugă un detaliu vizualizarea unei porțiuni dintr-o vizualizare existentă.

-   <img alt="" src=images/techdraw-draft-view.png  style="width:32px;"> [New Draft](TechDraw_NewDraft.md): adaugă o vizualizare la un Obiect din Atelierul [Draft Workbench](Draft_Workbench.md) .

-   <img alt="" src=images/techdraw-arch-view.png  style="width:32px;"> [New Arch](TechDraw_NewArch.md): adaugă o vizualizare la un obiect din Atelierul Arhitectură adaugă o vizualizare a [Arch Workbench](Arch_Workbench.md) [SectionPlane](Arch_SectionPlane.md) .

-   <img alt="" src=images/techdraw-spreadsheet.svg  style="width:32px;"> [Spreadsheet](TechDraw_Spreadsheet.md): inserează o vizualizare a unei foi de calcul [Spreadsheet Workbench](Spreadsheet_Workbench.md) sheet.

## Măști

Acestea sunt instrumente pentru a crea și a gestiona vederile mascate Clip objects

-   <img alt="" src=images/techdraw-clip.svg  style="width:32px;"> [Clip](TechDraw_Clip.md): inserează un grup de vederi mascate în secțiune într-o pagină.

-   <img alt="" src=images/techdraw-clipplus.svg  style="width:32px;"> [ClipPlus](TechDraw_ClipPlus.md): Adaugă o vedere existentă la un grup mască.

-   <img alt="" src=images/techdraw-clipminus.svg  style="width:32px;"> [ClipMinus](TechDraw_ClipMinus.md): Extrage o vedere dintr-un grup mascat.

## Cotare

Acestea sunt instrumente pentru a crea și lucra cu obiicte tip Cotă.

Cotele liniare pot fi bazate pe două puncte, o linie sau două linii.

-   <img alt="" src=images/Techdraw_Dimension_Length.png  style="width:32px;">

<img alt="Dimension_Length.png" src=images/Dimension_Length.png  style="width:32px;"> [New Length](TechDraw_Dimension_Length.md): adaugă o cotă tip lungime.

-   <img alt="" src=images/Techdraw_Dimension_Horizontal.png  style="width:32px;"> [New Horizontal](TechDraw_Dimension_Horizontal.md): adaugă o cotă orizontală tip lungime.

-   <img alt="" src=images/Techdraw_Dimension_Vertical.png  style="width:32px;"> [New Vertical](TechDraw_Dimension_Vertical.md): adaugă o cotă tip lungime verticală

-   <img alt="" src=images/Techdraw_Dimension_Radius.png  style="width:32px;"> [New Radius](TechDraw_Dimension_Radius.md): adaugă o cotă pentru raza unui cerc sau a unui arc de cerc.

-   <img alt="" src=images/Techdraw_Dimension_Diameter.png  style="width:32px;"> [New Diameter](TechDraw_Dimension_Diameter.md): adaugă o cotă pentru diametrul unui cerc sau a unui arc de cerc.

-   <img alt="" src=images/Techdraw_Dimension_Angle.png  style="width:32px;"> [New Angle](TechDraw_Dimension_Angle.md): adaugă o cotă pentru un unghi sau pentru două margini drepte.

-   <img alt="" src=images/TechDraw_Dimension_Angle3Pt.png  style="width:32px;"> [New Angle3Pt](TechDraw_Dimension_Angle3Pt.md): adaugă o cotă tip dimensiune unghiulară utilizând trei vârfuri.

-   <img alt="" src=images/TechDraw_Dimension_Horizontal_Extent.svg  style="width:32px;"> [New Horizontal Extent](TechDraw_Dimension_Horizontal_Extent.md): adds a horizontal extent dimension. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Dimension_Vertical_Extent.svg  style="width:32px;"> [New Vertical Extent](TechDraw_Dimension_Vertical_Extent.md): adds a vertical extent dimension. <small>(v0.19)</small> 

-   <img alt="" src=images/Dimension_Link.png  style="width:32px;"> [New Links](TechDraw_Dimension_Link.md): leagă o cotă existetnă de o formă geometrică 3 D

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [New Balloon](TechDraw_Balloon.md): adds a \"balloon\" annotation to a page. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Dimension_Landmark.svg  style="width:32px;"> [New Landmark Dimension](TechDraw_Dimension_Landmark.md): adds a landmark distance dimension. <small>(v0.19)</small> 

## Import/Export

These are tools for exporting pages to other applications.

-   \* <img alt="" src=images/techdraw-saveSVG.svg  style="width:32px;"> [Save SVG](TechDraw_SaveSVG.md): Salvează o pagină ca fișier [SVG](SVG.md) .
-   <img alt="" src=images/techdraw-saveDXF.svg  style="width:32px;"> [Save DXF](TechDraw_SaveDXF.md): Salvează o pagină ca fișier [DXF](DXF.md).

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Export Page as DXF](TechDraw_ExportPageDXF.md): saves the current page as [DXF](DXF.md) file.

## Decorațiune

Acestea sunt instrumente pentru modificarea aspectului paginilor și al vizualizărilor.

-   <img alt="" src=images/techdraw-hatch.png  style="width:32px;"> [Hatch Area](TechDraw_Hatch.md): aplică un model de hașurare dintr-un fișier, unei fațete

-   <img alt="" src=images/techdraw-geomhatch.png  style="width:32px;"> [Geometric Hatch](TechDraw_GeomHatch.md): aplică un model de trasură la o față folosind o specificație Autodesk PAT.

-   <img alt="" src=images/techdraw-symbol.png  style="width:32px;"> [New Symbol](TechDraw_Symbol.md): inserază un simbol cartezian [SVG](SVG.md) în pagină.

-   <img alt="" src=images/Techdraw-image.png  style="width:32px;"> [New Image](TechDraw_Image.md): Inserează o imagine PNG or JPG [bitmap](bitmap.md) în pagină.

-   <img alt="" src=images/techdraw-toggleframe.png  style="width:32px;"> [Toggle Frames](TechDraw_Toggle.md): Comuntă on/off cadrele și etichete care înconjoară o pagină.

## Annotation

The annotation tools are for \"marking up\" a drawing with additional information.

-   <img alt="" src=images/techdraw-annotation.png  style="width:32px;"> [New Annotation](TechDraw_NewAnnotation.md): adaugă un bloc de text care servește ca adnotare

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Add Leaderline to View](TechDraw_LeaderLine.md): adds a leaderline to a view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Insert Rich Text Annotation](TechDraw_RichTextAnnotation.md): adds an rich text block as annotation to a leaderline or a view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Add Cosmetic Vertex](TechDraw_CosmeticVertex.md): adds a Vertex which is not part of the source geometry. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Add Midpoint Vertices](TechDraw_Midpoints.md): adds Cosmetic Vertices at midpoints of selected edges. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Add Quadrant Vertices](TechDraw_Quadrants.md): adds Cosmetic Vertices at quarter points of selected (circular) edges. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Add Centerline to Faces](TechDraw_FaceCenterLine.md): adds a centerline to selected face(s). <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Add Centerline between 2 Lines](TechDraw_2LineCenterLine.md): adds a centerline between 2 lines. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Add Centerline between 2 Points](TechDraw_2PointCenterLine.md): adds a centerline between 2 points. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Add a cosmetic line](TechDraw_2PointCosmeticLine.md): adds a cosmetic line connecting 2 vertices. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md): removes cosmetic objects from a page. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Change Appearance of Lines](TechDraw_DecorateLine.md): changes the appearance of selected line(s). <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Show/Hide Invisible Edges](TechDraw_ShowAll.md): shows/hides invisible lines/edges in a view. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Add Welding Information to Leader](TechDraw_WeldSymbol.md): adds welding specifications to an existing leaderline. <small>(v0.19)</small> 

## Extension Package 

The Extension Package includes many useful tools to improve your TechDraw drawings.


**Some of these tools have yet to be released.**

-   <img alt="" src=images/TechDraw_Extension_CircleCenterLines.svg  style="width:32px;"> [CircleCenterLines](TechDraw_Extension_CircleCenterLines.md): adds center lines to circles and arcs. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_Extension_ThreadHoleSide.svg  style="width:32px;"> [ThreadHoleSide](TechDraw_Extension_ThreadHoleSide.md): adds a symbolic thread to the side view of a hole. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_Extension_ThreadHoleBottom.svg  style="width:32px;"> [ThreadHoleBottom](TechDraw_Extension_ThreadHoleBottom.md): adds symbolic threads to the bottom view of holes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_Extension_ThreadBoltSide.svg  style="width:32px;"> [ThreadBoltSide](TechDraw_Extension_ThreadBoltSide.md): adds a symbolic thread to the side view of a bolt. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_Extension_ThreadBoltBottom.svg  style="width:32px;"> [ThreadBoltBottom](TechDraw_Extension_ThreadBoltBottom.md): adds symbolic threads to the bottom view of bolts. <small>(v0.20)</small> 

## Caracteristici suplimentare 

-   [Hatching](TechDraw_Hatching.md): explică diverse tehnici de hașurare.
-   [Line Groups](TechDraw_LineGroup.md): Grosimi implicite pot fi asignate diferitor tipuri de linie.
-   [Templates](TechDraw_Templates.md): șabloanele implicite definite pentru paginile de desen.

## Setările de elecție 

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Preferences](TechDraw_Preferences.md): preferințele pentru valorile implicite ale paginii desenului, cum ar fi unghiul de proiectare, culori, dimensiunile textului și stilurile de linie.

## Script-Programare 

Instrumentele TechDraw pot fi utilizate în [macros](macros.md) și din consola [Python](Python.md) utilizând două API-uri.

-   [TechDraw API](TechDraw_API.md)
-   [TechDrawGui API](TechDrawGui_API.md)

## Limitări

-   -   TechDraw drawings and its API are not interchangeable with the [Drawing Workbench](Drawing_Workbench.md) and its API. It is possible to convert Drawing Pages to TechDraw Pages using a Python script (`moveViews.py`).

-   Este posibil să aveți atât TechDraw cât și Pagini de desen în același document FreeCAD, deoarece fiecare pagină este complet independentă una față de cealaltă.

-   Există diferențe minore în specificarea textelor editabile în șabloanele [SVG](SVG.md) în comparație cu modulul Desenare. În TechDraw, scalarea documentului SVG afectează poziția câmpurilor de text editabile. Vedeți discuția pe forum [Scala TechDraw șabloane](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271) pentru mai multe detalii.

-   Nu tăiați, copiați și lipiți obiecte TechDraw în vizualizarea arborescentă, deoarece în general aceasta nu funcționează bine.

## Tutoriale

-   [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md): introducere în crearea de desene cu TechDraw Workbench.
-   [ Crearea unui nou șablon](TechDraw_TemplateHowTo.md): instrucțiuni pentru crearea unui nou șablon de pagină în Inkscape pentru utilizarea cu TechDraw Workbench.

Video tutorials by sliptonic

-   TechDraw Workbench [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   TechDraw Workbench [Part 4 (Section and Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Customizing Templates)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)

!!FUZZY!!{{docnav|Surface_Workbench|Test Framework Workbench}}


{{TechDraw Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)
