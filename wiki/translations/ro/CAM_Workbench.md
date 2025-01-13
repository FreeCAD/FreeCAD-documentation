# CAM Workbench/ro
<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="CAM workbench icon" src=images/Workbench_CAM.svg  style="width:128px;">


</div>






## Introducere


<div class="mw-translate-fuzzy">

Atelierul traiectorii este folosit pentru producerea unor instrucţiuni [CNC machines](https://en.wikipedia.org/wiki/CNC_router) pornind de la un model FreeCAD 3D. Acestea produc obeicte reale 3D pe mașini CNC ca frezele, strungurile, mașinile de tăiat cu laser, sau similare.În mod tipic instrucțiile sunt un dialect [G-Code](https://en.wikipedia.org/wiki/G-Code) .


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Algoritmul pentru crearea acestor instrucțiuni în FreeCAD, în limbajul G-cod, este următorul:

-   Un model 3D este obiectul de bază, creat în mod obișnuit folosind una sau mai multe tabele de lucru [Part Design](PartDesign_Workbench/ro.md), [Part](Part_Workbench/ro.md) sau [Draft](Draft_Workbench/ro.md).
-   O [Job](CAM_Job/ro.md) este creată în Path Workbench. Aceasta conține toate informațiile necesare pentru a genera codul G necesar pentru a procesa lucrarea pe o moară CNC: există material stoc, moara are un anumit [set de instrumente](CAM_ToolBitLibraryOpen.md) și urmează anumite comenzi care controlează viteza și mișcările (de obicei, Codul G).
-   Instrumentele sunt selectate după cum este cerut de Operațiunile de Lucru.
-   Căile de frezare sunt create folosind, de ex. [Contour](CAM_Profile/ro.md) și [Pocket](CAM_Pocket_3D/ro.md) Operații. Aceste Obiecte de cale folosesc dialectul intern al FreeCAD G, independent de mașina CNC.
-   Exportați lucrarea cu un cod g, care se potrivește cu mașina dvs.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## General concepts 


</div>


<div class="mw-translate-fuzzy">

## Concepte generale 

Path Workbench generează G-Code care definește căile necesare pentru a mula Proiectul reprezentat de modelul 3D pe miezul țintă [https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format the Path Job Operations FreeCAD G-Code dialect](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format_the_Path_Job_Operations_FreeCAD_G-Code_dialect.md), care ulterior se traduce în dialectul corespunzător pentru controlerul CNC țintă prin selectarea postprocesorului adecvat.   Codul G este generat de directivele și operațiile conținute într-o traiectorie. Fluxul de lucru al joburilor le afișează în ordinea în care vor fi executate. Lista este populată prin adăugarea operațiunilor de deplasare, a traiectoriile suplimentare(Dressup), a comenzilor parțiale ale traiectorilor și a modificărilor de parcurs - din meniul Path sau prin butoanele GUI.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The G-code is generated from directives and Operations contained in a CAM Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding CAM Operations, Path Dressups, Supplemental Commands, and Path Modifications from the CAM Menu, or GUI buttons.


</div>


<div class="mw-translate-fuzzy">

Path Workbench oferă un Manager de instrumente (Library, Tool-Table) și G-Code Inspection și instrumente de simulare. Acesta leagă postprocesorul și permite importarea și exportul șabloanelor de lucrări.


</div>


<div class="mw-translate-fuzzy">

Path Workbench include dependențe externe:

1.  Unitățile de măsură ale modelului FreeCAD 3D sunt definite în **Edit → Preference → General → Units tab's Units settings**.. Configurația Postprocesorului definește unitățile finale de cod G.
2.  Fișierul Macro al traiectorie, and Geometric toleranțe, sunt definite în **Edit → Preferences → Path → Job Preferences** .
3.  Culorile sunt definite in the **Edit → Preferences → Path → Path colors** tab.
4.  Parametrii Punților de susținere (Holding tag) sunt definite în **Edit → Preferences → Path → Dressups** tab.
5.  Calitatea modelului 3D de bază acceptă cerințele Path WB, passes Check Geometry.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Limitations


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Some current limitations of which you should be aware are:

-   Most of the CAM Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/CAM_3DPocket.svg" width=24px> [3D Pocket](CAM_Pocket_3D.md)** and **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)** (which is still an [experimental feature](CAM_experimental.md) as of November 2020).
-   Most of CAM workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19_pre.
-   Most operations in CAM workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/CAM_Engrave.svg" width=24px> [Engrave](CAM_Engrave.md)** and **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)** operations.
-   The operations within the CAM workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.


</div>



## Unități de măsură 


<div class="mw-translate-fuzzy">

Unitatea de măsură în Traiectorie poate crea confuzii. Există mai multe puncte de înțeles:

1.  În FreeCAD unitățile de măsură pentru lungime și timp sunt \'mm\' and \'s\' respectively. Viteza este în \'mm/s\'. Aceasta este stocată intern în FreeCAD indiferent de orice altceva
2.  Schema default de Unități de măsură utilizează unitățile implicite. Dacă utilizați schema implicită și introduceți o rată de alimentare fără a specifică unitățile de măsură, aceasta va fi introdusă ca \'mm/s\'
3.  Majoritatea mașinilor CNC se așteaptă ca rata de alimentare să fie sub formă de fie \'mm/min\' or \'in/min\'. Cele mai multe postprocesoare vor converti automat unitatea atunci când generează gcode.


</div>


<div class="mw-translate-fuzzy">

Scheme:

1.  Schimbarea schemei din preferințe modifică șirul de unități implicit pentru câmpurile de introducere. Dacă sunteți un utilizator Path și preferați să proiectați în metrice, este foarte recomandat să utilizați schema \"Metric Small Parts & CNC\". Dacă proiectați în unități din SUA, fie Decimalul Imperial și Clădirea SUA vor funcționa
2.  Schimbarea schemei de unități preferate nu va avea niciun efect asupra ieșirii, dar va ajuta la evitarea erorilor de intrare


</div>


<div class="mw-translate-fuzzy">

Ieşire:

1.  Generarea unității corecte în ieșire este responsabilitatea postprocesorului și se face numai la momentul respectiv
2.  Unitatea de ieșire a mașinii nu are nicio legătură cu schema unității selectată
3.  Postprocesoarele produc fie ieșire metrică (G21), ieșire Imperial (G20), fie configurabile.
4.  Implicit post-procesor configurabil la metric (G21)
5.  Dacă doriți ca postprocesorul dvs. configurabil să emită gcode imperiale (G20), Setați argumentul corect în configurația de ieșire a jobului (de ex. \--Inches pentru linuxcnc). Acest lucru poate fi stocat într-un șablon de lucru și setat ca șablon implicit pentru al face automat pentru toate lucrările viitoare


</div>


<div class="mw-translate-fuzzy">

Căi de inspecție:

1.  Dacă utilizați instrumentul Path Inspect pentru a vedea codul g, îl veți vedea în \'mm/s\' deoarece nu este post-procesat


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Heights and depths 


</div>


<div class="mw-translate-fuzzy">

## Comenzi pentru Traiectorie 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Commands


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Some commands are experimental and not available by default. To enable them see [CAM experimental](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Project Commands 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Job.png  style="width:32px;"> [Job](CAM_Job/ro.md): Creează un nou CNC job


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_PostProcess.png  style="width:32px;"> [Post Process](CAM_Post/ro.md): Exportă un proiect ca G-code


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Sanity.png  style="width:32px;"> [CAM Errors](CAM_Sanity/ro.md): Verifică lucrarea selectată pentru valori lipsă


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-ExportTemplate.png  style="width:32px;"> [Export Template](CAM_ExportTemplate/ro.md): Exportă job-ul curent ca șablon


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Tool Commands 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Inspect.png  style="width:32px;"> [G-Code Inspector](CAM_Inspect/ro.md): Arată G-code pentru verificare


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Simulator.png  style="width:32px;"> [Simulator](CAM_Simulator/ro.md): Arată operațiunile de frezare ca și cum ar fi fost deja făcute pe mașina-unealtă


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_SimulatorGL.svg  style="width:32px;"> [CAM SimulatorGL](CAM_SimulatorGL.md): Enables the new, improved CAM simulator. <small>(v1.0)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-CompleteLoop.png  style="width:32px;"> [Complete Loop](CAM_SelectLoop/ro.md): Completează o buclă de la două muchii selceționate


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](CAM_OpActiveToggle.md): Activates or de-activates a path operation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](CAM_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](CAM_ToolBitDock.md): Toggles the ToolBit Dock.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Basic Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profile](CAM_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Pocket.png  style="width:32px;"> [Pocket](CAM_Pocket_Shape/ro.md): Creează o operație de realizare a unor adâncituri dreptunghiulare pornind de la una sau mai multe buzunare -pocket(s)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Drilling.png  style="width:32px;"> [Drilling](CAM_Drilling/ro.md): Realizează un ciclu de găurire


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Face.png  style="width:32px;"> [Mill Face](CAM_MillFace/ro.md): Creează o traiectorie de suprafață


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Helix.png  style="width:32px;"> [Helix](CAM_Helix/ro.md): Creează o traiectorie elicoidală


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Adaptive.svg  style="width:32px;"> [Adaptive](CAM_Adaptive.md): Creates an adaptive clearing and profiling operation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Slot.svg  style="width:32px;"> [Slot](CAM_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](CAM_experimental.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Engrave.png  style="width:32px;"> [Engrave](CAM_Engrave/ro.md): Creează o gravură


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Deburr.svg  style="width:32px;"> [Deburr](CAM_Deburr.md): Creates a deburr path.


</div>


<div class="mw-translate-fuzzy">

### Traiectorie suplimentară 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### 3D Operations 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DPocket.png  style="width:32px;"> [3D Pocket](CAM_Pocket_3D/ro.md): Creează o traiectorie pentru o adâncitură 3D- 3D pocket


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DSurface.png  style="width:32px;"> [3D Surface](CAM_Surface/ro.md): Creează o traiectorie de uzinare pentru o suprafață 3D


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Waterline.svg  style="width:32px;"> [Waterline](CAM_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Path Dressup 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupAxisMap.svg  style="width:32px;"> [Axis Map](CAM_DressupAxisMap.md): Remaps one axis to another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:32px;"> [Boundary](CAM_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_DressupDogbone.png  style="width:32px;"> [Dogbone Dressup](CAM_DressupDogbone/ro.md): Adaugă modificări de traiectorie pentru colțurile interne (dogbone)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_DressupDragKnife.png  style="width:32px;"> [Dragknife Dressup](CAM_DressupDragKnife/ro.md): Adaugă o traiectorie suplimentară pentru un dragknife la traiectoria selectată


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_DressupLeadInOut.png  style="width:32px;"> [Lead In Dressup](CAM_DressupLeadInOut/ro.md):Adaugă un punct de intrare și / sau un punct de ieșire la o traiectorie selectată


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_DressupRampEntry.png  style="width:32px;"> [Ramp Entry Dressup](CAM_DressupRampEntry/ro.md): Adaugă o traiectorie suplimentară de intrare intrare în șpan


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_DressupTag.png  style="width:32px;"> [Tag Dressup](CAM_DressupTag/ro.md): Adaugă punți de susținere (holding tag) la traiectoria selectată


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](CAM_DressupZCorrect.md): Corrects the Z depth using Probe Map.


</div>




<div class="mw-translate-fuzzy">

### Comenzi Speciale 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Fixture.png  style="width:32px;"> [Fixture](CAM_Fixture/ro.md): Schimbă poziția punctului de fixare


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Comment.png  style="width:32px;"> [Comment](CAM_Comment/ro.md): Inserează un comentariu în G-codul traiectoriei


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Stop.png  style="width:32px;"> [Stop](CAM_Stop/ro.md): Introduce o oprire completă a mașinii


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Custom.png  style="width:32px;"> [Custom](CAM_Custom/ro.md): Inserează G-cod personalizat


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Probe.svg  style="width:32px;"> [Probe](CAM_Probe.md): Creates a Probing Grid from a job stock.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Shape.svg  style="width:32px;"> [From Shape](CAM_Shape/ro.md): Creează un obiect traiectorie dintr-un obiect Piesă selectat


</div>




<div class="mw-translate-fuzzy">

### Modificarea Traiectoriei 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Copy.png  style="width:32px;"> [Copy](CAM_Copy/ro.md): Creează o Copie parametrică a obiectului traiectorie selectat


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Array.png  style="width:32px;"> [Array](CAM_Array/ro.md): Creează o matrice de multiplicare a traiectoriei selectate


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_SimpleCopy.png  style="width:32px;"> [Simple Copy](CAM_SimpleCopy/ro.md): Creează o copie neparametrică a unui obiect traiectorie selectat


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Specialty Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ThreadMilling.svg  style="width:32px;"> [Thread Milling](CAM_ThreadMilling.md): Creates a CAM Thread Milling operation from features of a base object. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Miscellaneous


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area.png  style="width:32px;"> [Feature area](CAM_Area/ro.md): Creează o zonă de caracteristici din obiectele selectate


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area-Workplane.png  style="width:32px;"> [Feature area workplane](CAM_Area_Workplane/ro.md): Creează un plan de lucru pentru zona de caracteristici


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## ToolBit architecture 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Tools](CAM_Tools.md)
-   [CAM ToolShape](CAM_ToolShape.md)
-   [CAM ToolBit](CAM_ToolBit.md)
-   [CAM ToolBit Library](CAM_ToolBit_Library.md)
-   [CAM ToolController](CAM_ToolController.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Other


</div>


<div class="mw-translate-fuzzy">

Path Workbench partajează mai multe concepte cu alte pachete software CAM, dar are propriile particularități. Dacă ceva pare rău, ar putea fi un loc bun pentru a începe.


</div>




<div class="mw-translate-fuzzy">

### Preferințe


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Preferences\...](CAM_Preferences/ro.md): Preferințe disponibile în Atelierul Traiectorie.


</div>



## Script


<div class="mw-translate-fuzzy">

A se vedea pagina [CAM scripting](Path_scripting/ro.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Tutorials


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Walkthrough for the Impatient](CAM_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with CAM.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Videos


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): A playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [CAM Workbench](CAM_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): A playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ): A playlist with a series of 8 videos in English by CAD CAM Lessons.
-   Also see the [Computer-Aided Manufacturing (CAM) section](Video_tutorials#Computer-Aided_Manufacturing_(CAM).md) of the [Video tutorials](Video_tutorials.md) wiki page.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Roadmap


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Development Roadmap](CAM_Development_Roadmap.md): Read this if you are a developer and want to contribute to CAM.


</div>


<div class="mw-translate-fuzzy">


{{Userdocnavi/ro}}


</div>


{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > CAM Workbench/ro
