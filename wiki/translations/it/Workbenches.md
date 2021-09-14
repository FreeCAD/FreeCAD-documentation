# Workbenches/it






FreeCAD, come molte applicazioni moderne di progettazione come [Revit](wikipedia:Revit.md) o [CATIA](wikipedia:CATIA.md), è basato sul concetto di [Workbench](wikipedia:Workbench.md). Un banco da lavoro può essere considerato come un insieme di strumenti appositamente raggruppati per un certo compito. In un tradizionale laboratorio di mobili, si avrebbe un tavolo da lavoro per la persona che lavora con il legno, un altro per quello che lavora con i pezzi di metallo, e forse un terzo per quello che monta tutti i pezzi insieme.

In FreeCAD, viene applicato lo stesso concetto. Gli strumenti sono raggruppati per ambienti in base alle funzioni correlate.

Quando si passa da un ambiente di lavoro ad un altro, cambiano anche gli strumenti disponibili visualizzati sull\'interfaccia. Le barre degli strumenti, le barre dei comandi e eventualmente altre parti dell\'interfaccia si adattano al nuovo ambiente, ma il contenuto della scena visualizzata non cambia. Si può, ad esempio, iniziare a disegnare forme 2D utilizzando l\'ambiente **Draft** e poi continuare a lavorare su di esse con l\'ambiente **Parte**.


<div class="mw-translate-fuzzy">

Notare che a volte un Ambiente viene indicato come un *Modulo*. Gli Ambienti e i Moduli sono però entità diverse. Un modulo è una estensione di FreeCAD, mentre un ambiente di lavoro è una speciale configurazione dell\'interfaccia grafica che raggruppa alcune barre degli strumenti e dei menu specifici. Di solito, ogni modulo contiene anche il proprio ambiente di lavoro, e viceversa, ogni ambiente dipende da un modulo, per questo motivo succede di fare un uso incrociato del nome.


</div>

## Ambienti incorporati 


<div class="mw-translate-fuzzy">

Attualmente in tutte le installazioni di FreeCAD sono disponibili i seguenti ambienti:


</div>

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar as the Part Shape builder Face from edges.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Deprecati


<div class="mw-translate-fuzzy">

I seguenti ambienti di lavoro sono ancora inclusi nell\'installazione di base per motivi di compatibilità, ma non dovrebbero più essere utilizzati.

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> [Completo](Complete_Workbench/it.md) contiene tutti i comandi e le funzionalità di tutti i moduli e banchi di lavoro che soddisfano determinati criteri di qualità. {{Obsolete/it|0.17}}
-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> [Drawing](Drawing_Workbench/it.md) è stato usato per visualizzare il lavoro in 3D su un foglio 2D ma ora è stato deprecato, è ancora necessario leggere i vecchi file di FreeCAD che contengono un oggetto Drawing originariamente creato con questo ambiente. Vedere [TechDraw](TechDraw_Workbench/it.md), che è un sostituto più avanzato. {{Obsolete/it|0.17}}


</div>

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> The [Complete Workbench](Complete_Workbench.md) holds all commands and features from all workbenches that met certain quality criteria. {{Obsolete|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings but has now been deprecated. It is still needed to read old FreeCAD files that contain objects created with this workbench. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement. {{Obsolete|0.17}}

## Ambienti aggiuntivi 

Gli ambienti di lavoro per FreeCAD sono facilmente programmabili in [Python](Python/it.md), quindi ci sono molte persone che stanno sviluppando degli ambienti aggiuntivi al di fuori dell\'area principale di sviluppo di FreeCAD.

La pagina [Ambienti complementari](external_workbenches/it.md) elenca tutti quelli che sono noti a questa comunità. La maggior parte è facilmente installabile da FreeCAD, usando [Addon manager](Addon_Manager/it.md), che si trova nel menu **Strumenti → <img src="images/_AddonManager.svg" width=24px> Addon manager**.

Sono in fase di sviluppo ulteriori nuovi ambienti, mantenetevi aggiornati.







[Category:Workbenches](Category:Workbenches.md)
