# Workbenches/it
FreeCAD, come molte applicazioni moderne di progettazione come [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit) o [CATIA](https://en.wikipedia.org/wiki/CATIA), è basato sul concetto di [Ambiente di Lavoro](https://en.wikipedia.org/wiki/Workbench). Un ambiente di lavoro può essere considerato come un insieme di strumenti appositamente raggruppati per un certo compito. In un tradizionale laboratorio di mobili, avresti un tavolo da lavoro per la persona che lavora con il legno, un altro per quello che lavora con i pezzi di metallo, e forse un terzo per quello che monta tutti i pezzi insieme.

In FreeCAD, viene applicato lo stesso concetto. Gli strumenti sono raggruppati per ambienti di lavoro in base ai compiti correlati.

Quando si passa da un ambiente di lavoro ad un altro, cambiano anche gli strumenti disponibili visualizzati sull\'interfaccia. Le barre degli strumenti, le barre dei comandi e eventualmente altre parti dell\'interfaccia si adattano al nuovo ambiente, ma il contenuto della scena visualizzata non cambia. Si può, ad esempio, iniziare a disegnare forme 2D utilizzando l\'ambiente **Draft** e poi continuare a lavorare su di esse con l\'ambiente **Part**.

Notare che a volte un Ambiente viene indicato come un *Modulo*. Gli Ambienti e i Moduli sono però entità diverse. Un Modulo è un\'estensione di FreeCAD, mentre un Ambiente di lavoro è un tipo speciale di modulo con una GUI configurata (barre degli strumenti e menu).



## Ambienti incorporati 



### Attuale

I seguenti ambienti di lavoro sono inclusi in ogni installazione di FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Menu di Base](Std_Base/it.md). Questo non è realmente un ambiente di lavoro, ma piuttosto una categoria di comandi e strumenti \"standard\" che possono essere utilizzati in tutti gli ambienti di lavoro.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Ambiente Architettura](Arch_Workbench/it.md) per lavorare con elementi architettonici.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Ambiente Draft](Draft_Workbench/it.md) contiene strumenti 2D e operazioni CAD 2D e 3D di base.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Ambiente FEM](FEM_Workbench/it.md) fornisce un flusso di lavoro di analisi agli elementi finiti (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [Ambiente Inspection](Inspection_Workbench/it.md) è realizzato per fornirti strumenti specifici per l\'esame delle forme. È ancora nelle prime fasi di sviluppo.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Ambiente Mesh](Mesh_Workbench/it.md) per lavorare con maglie triangolari.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [Ambiente OpenSCAD](OpenSCAD_Workbench/it.md) per l\'interoperabilità con OpenSCAD e la riparazione della cronologia del modello della [geometria solida costruttiva](Constructive_solid_geometry/it.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Ambiente Part](Part_Workbench/it.md) per lavorare con primitive geometriche ed operazioni booleane.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Ambiente Part Design](PartDesign_Workbench/it.md) per la costruzione di forme di parti da schizzi.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [Ambiente Path](Path_Workbench/it.md) viene utilizzato per produrre istruzioni G-Code.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [Ambiente Punti](Points_Workbench/it.md) per lavorare con nuvole di punti.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [Ambiente Ingegneria inversa](Reverse_Engineering_Workbench/it.md) ha lo scopo di fornire strumenti specifici per convertire forme/solidi/mesh in forme parametriche compatibili con FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [ Ambiente Robot](Robot_Workbench/it.md) per lo studio dei movimenti dei robot. Attualmente non mantenuto.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Ambiente Sketcher](Sketcher_Workbench/it.md) per lavorare con schizzi a geometria vincolata.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Ambiente Foglio di calcolo](Spreadsheet_Workbench/it.md) per la creazione e la manipolazione di dati in un foglio di calcolo.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> [Ambiente Start](Start_Workbench/it.md) consente di passare rapidamente agli ambienti di lavoro più comuni.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Ambiente Superficie](Surface_Workbench/it.md) fornisce strumenti per creare e modificare le superfici. È simile al [Part Builder](Part_Builder/it.md) con l\'opzione faccia dai bordi.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [Ambiente TechDraw](TechDraw_Workbench/it.md) per la produzione di disegni tecnici da modelli 3D. È il successore dell\'[Ambiente Disegno Tecnico](Drawing_Workbench/it.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [Ambiente di Test](Testing/it.md) serve per il debug di FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> [Ambiente Web](Web_Workbench/it.md) fornisce una finestra del browser invece della [vista 3D](3D_view/it.md) all\'interno di FreeCAD.



### Obsoleto

I seguenti ambienti di lavoro non sono più inclusi dopo la versione 0.20:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> [Drawing](Drawing_Workbench/it.md) è stato utilizzato per la produzione di disegni tecnici. L\'[Ambiente TechDraw](TechDraw_Workbench/it.md) è il suo sostituto più avanzato. {{Obsolete/it|0.17}}

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> L\'[Ambiente Immagine](Image_Workbench/it.md) è stato utilizzato per lavorare con immagini bitmap. La sua funzionalità è stata integrata nel menù [Base](Std_Base/it.md). Vedere [<File:Importa>](Std_Import/it.md) e [Strumenti: Carica Immagine](Std_ViewLoadImage/it.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> [Ambiente Raytracing](Raytracing_Workbench/it.md) è stato utilizzato per il ray-tracing (rendering). Al suo posto dovrebbe essere usato l\'ambiente esterno [Render Workbench](https://github.com/FreeCAD/FreeCAD-render).



## Ambienti aggiuntivi 

Gli ambienti di lavoro per FreeCAD sono facilmente programmabili in [Python](Python/it.md), quindi ci sono molte persone che stanno sviluppando degli ambienti aggiuntivi al di fuori dell\'area principale di sviluppo di FreeCAD.

La pagina [Ambienti complementari](External_workbenches/it.md) elenca tutti quelli che sono noti a questa comunità. La maggior parte è facilmente installabile da FreeCAD, usando [Addon manager](Std_AddonMgr/it.md), che si trova nel menu **Strumenti → <img src="images/Std_AddonMgr.svg" width=24px> Addon manager**.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/it
