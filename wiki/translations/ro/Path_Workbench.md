# <img alt="Path workbench icon" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/ro


{{TOCright}}



## Introducere


<div class="mw-translate-fuzzy">

Atelierul traiectorii este folosit pentru producerea unor instrucţiuni [CNC machines](https://en.wikipedia.org/wiki/CNC_router) pornind de la un model FreeCAD 3D. Acestea produc obeicte reale 3D pe mașini CNC ca frezele, strungurile, mașinile de tăiat cu laser, sau similare.În mod tipic instrucțiile sunt un dialect [G-Code](https://en.wikipedia.org/wiki/G-Code) .


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Algoritmul pentru crearea acestor instrucțiuni în FreeCAD, în limbajul G-cod, este următorul:

-   Un model 3D este obiectul de bază, creat în mod obișnuit folosind una sau mai multe tabele de lucru [Part Design](PartDesign_Workbench/ro.md), [Part](Part_Workbench/ro.md) sau [Draft](Draft_Workbench/ro.md).
-   O [Job](Path_Job/ro.md) este creată în Path Workbench. Aceasta conține toate informațiile necesare pentru a genera codul G necesar pentru a procesa lucrarea pe o moară CNC: există material stoc, moara are un anumit [set de instrumente](Path_ToolLibraryEdit/ro.md) și urmează anumite comenzi care controlează viteza și mișcările (de obicei, Codul G).
-   Instrumentele sunt selectate după cum este cerut de Operațiunile de Lucru.
-   Căile de frezare sunt create folosind, de ex. [Contour](Path_Profile/ro.md) și [Pocket](Path_Pocket_3D/ro.md) Operații. Aceste Obiecte de cale folosesc dialectul intern al FreeCAD G, independent de mașina CNC.
-   Exportați lucrarea cu un cod g, care se potrivește cu mașina dvs.


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## Concepte generale 

Path Workbench generează G-Code care definește căile necesare pentru a mula Proiectul reprezentat de modelul 3D pe miezul țintă [https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format the Path Job Operations FreeCAD G-Code dialect](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format_the_Path_Job_Operations_FreeCAD_G-Code_dialect.md), care ulterior se traduce în dialectul corespunzător pentru controlerul CNC țintă prin selectarea postprocesorului adecvat.   Codul G este generat de directivele și operațiile conținute într-o traiectorie. Fluxul de lucru al joburilor le afișează în ordinea în care vor fi executate. Lista este populată prin adăugarea operațiunilor de deplasare, a traiectoriile suplimentare(Dressup), a comenzilor parțiale ale traiectorilor și a modificărilor de parcurs - din meniul Path sau prin butoanele GUI.


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


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

## Limitations

Some current limitations of which you should be aware are:

-   Most of the Path Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/Path_3DPocket.svg" width=24px> [3D Pocket](Path_Pocket_3D.md)** and **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** (which is still an [experimental feature](Path_experimental.md) as of November 2020).
-   Most of Path workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19_pre.
-   Most operations in Path workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/Path_Engrave.svg" width=24px> [Engrave](Path_Engrave.md)** and **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** operations.
-   The operations within the Path workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.



## Unități de măsură 

Unitatea de măsură în Traiectorie poate crea confuzii. Există mai multe puncte de înțeles:

1.  În FreeCAD unitățile de măsură pentru lungime și timp sunt \'mm\' and \'s\' respectively. Viteza este în \'mm/s\'. Aceasta este stocată intern în FreeCAD indiferent de orice altceva
2.  Schema default de Unități de măsură utilizează unitățile implicite. Dacă utilizați schema implicită și introduceți o rată de alimentare fără a specifică unitățile de măsură, aceasta va fi introdusă ca \'mm/s\'
3.  Majoritatea mașinilor CNC se așteaptă ca rata de alimentare să fie sub formă de fie \'mm/min\' or \'in/min\'. Cele mai multe postprocesoare vor converti automat unitatea atunci când generează gcode.

Scheme:

1.  Schimbarea schemei din preferințe modifică șirul de unități implicit pentru câmpurile de introducere. Dacă sunteți un utilizator Path și preferați să proiectați în metrice, este foarte recomandat să utilizați schema \"Metric Small Parts & CNC\". Dacă proiectați în unități din SUA, fie Decimalul Imperial și Clădirea SUA vor funcționa
2.  Schimbarea schemei de unități preferate nu va avea niciun efect asupra ieșirii, dar va ajuta la evitarea erorilor de intrare

Ieşire:

1.  Generarea unității corecte în ieșire este responsabilitatea postprocesorului și se face numai la momentul respectiv
2.  Unitatea de ieșire a mașinii nu are nicio legătură cu schema unității selectată
3.  Postprocesoarele produc fie ieșire metrică (G21), ieșire Imperial (G20), fie configurabile.
4.  Implicit post-procesor configurabil la metric (G21)
5.  Dacă doriți ca postprocesorul dvs. configurabil să emită gcode imperiale (G20), Setați argumentul corect în configurația de ieșire a jobului (de ex. \--Inches pentru linuxcnc). Acest lucru poate fi stocat într-un șablon de lucru și setat ca șablon implicit pentru al face automat pentru toate lucrările viitoare

Căi de inspecție:

1.  Dacă utilizați instrumentul Path Inspect pentru a vedea codul g, îl veți vedea în \'mm/s\' deoarece nu este post-procesat

## Heights and depths 


<div class="mw-translate-fuzzy">

## Comenzi pentru Traiectorie 


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Job.png  style="width:32px;"> [Job](Path_Job/ro.md): Creează un nou CNC job


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.png  style="width:32px;"> [Post Process](Path_Post/ro.md): Exportă un proiect ca G-code


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Sanity.png  style="width:32px;"> [Path Errors](Path_Sanity/ro.md): Verifică lucrarea selectată pentru valori lipsă


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-ExportTemplate.png  style="width:32px;"> [Export Template](Path_ExportTemplate/ro.md): Exportă job-ul curent ca șablon


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.png  style="width:32px;"> [G-Code Inspector](Path_Inspect/ro.md): Arată G-code pentru verificare


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.png  style="width:32px;"> [Simulator](Path_Simulator/ro.md): Arată operațiunile de frezare ca și cum ar fi fost deja făcute pe mașina-unealtă


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-CompleteLoop.png  style="width:32px;"> [Complete Loop](Path_SelectLoop/ro.md): Completează o buclă de la două muchii selceționate


</div>

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](Path_OpActiveToggle.md): Activates or de-activates a path operation.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock.

### Basic Operations 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Pocket.png  style="width:32px;"> [Pocket](Path_Pocket_Shape/ro.md): Creează o operație de realizare a unor adâncituri dreptunghiulare pornind de la una sau mai multe buzunare -pocket(s)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.png  style="width:32px;"> [Drilling](Path_Drilling/ro.md): Realizează un ciclu de găurire


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Face.png  style="width:32px;"> [Mill Face](Path_MillFace/ro.md): Creează o traiectorie de suprafață


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Helix.png  style="width:32px;"> [Helix](Path_Helix/ro.md): Creează o traiectorie elicoidală


</div>

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptive](Path_Adaptive.md): Creates an adaptive clearing and profiling operation.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Slot](Path_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](Path_experimental.md).


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Engrave.png  style="width:32px;"> [Engrave](Path_Engrave/ro.md): Creează o gravură


</div>

-   <img alt="" src=images/Path_Deburr.svg  style="width:32px;"> [Deburr](Path_Deburr.md): Creates a deburr path.


<div class="mw-translate-fuzzy">

### Traiectorie suplimentară 


</div>

### 3D Operations 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DPocket.png  style="width:32px;"> [3D Pocket](Path_Pocket_3D/ro.md): Creează o traiectorie pentru o adâncitură 3D- 3D pocket


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DSurface.png  style="width:32px;"> [3D Surface](Path_Surface/ro.md): Creează o traiectorie de uzinare pentru o suprafață 3D


</div>

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Waterline](Path_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](Path_experimental.md).

### Path Dressup 

-   <img alt="" src=images/Path_DressupAxisMap.svg  style="width:32px;"> [Axis Map](Path_DressupAxisMap.md): Remaps one axis to another.

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Boundary](Path_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDogbone.png  style="width:32px;"> [Dogbone Dressup](Path_DressupDogbone/ro.md): Adaugă modificări de traiectorie pentru colțurile interne (dogbone)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDragKnife.png  style="width:32px;"> [Dragknife Dressup](Path_DressupDragKnife/ro.md): Adaugă o traiectorie suplimentară pentru un dragknife la traiectoria selectată


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupLeadInOut.png  style="width:32px;"> [Lead In Dressup](Path_DressupLeadInOut/ro.md):Adaugă un punct de intrare și / sau un punct de ieșire la o traiectorie selectată


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupRampEntry.png  style="width:32px;"> [Ramp Entry Dressup](Path_DressupRampEntry/ro.md): Adaugă o traiectorie suplimentară de intrare intrare în șpan


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupTag.png  style="width:32px;"> [Tag Dressup](Path_DressupTag/ro.md): Adaugă punți de susținere (holding tag) la traiectoria selectată


</div>

-   <img alt="" src=images/Path_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](Path_DressupZCorrect.md): Corrects the Z depth using Probe Map.




<div class="mw-translate-fuzzy">

### Comenzi Speciale 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.png  style="width:32px;"> [Fixture](Path_Fixture/ro.md): Schimbă poziția punctului de fixare


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.png  style="width:32px;"> [Comment](Path_Comment/ro.md): Inserează un comentariu în G-codul traiectoriei


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.png  style="width:32px;"> [Stop](Path_Stop/ro.md): Introduce o oprire completă a mașinii


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.png  style="width:32px;"> [Custom](Path_Custom/ro.md): Inserează G-cod personalizat


</div>

-   <img alt="" src=images/Path_Probe.svg  style="width:32px;"> [Probe](Path_Probe.md): Creates a Probing Grid from a job stock.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [From Shape](Path_Shape/ro.md): Creează un obiect traiectorie dintr-un obiect Piesă selectat


</div>




<div class="mw-translate-fuzzy">

### Modificarea Traiectoriei 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.png  style="width:32px;"> [Copy](Path_Copy/ro.md): Creează o Copie parametrică a obiectului traiectorie selectat


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.png  style="width:32px;"> [Array](Path_Array/ro.md): Creează o matrice de multiplicare a traiectoriei selectate


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.png  style="width:32px;"> [Simple Copy](Path_SimpleCopy/ro.md): Creează o copie neparametrică a unui obiect traiectorie selectat


</div>

### Specialty Operations 

-   <img alt="" src=images/Path_ThreadMilling.svg  style="width:32px;"> [Thread Milling](Path_ThreadMilling.md): Creates a Path Thread Milling operation from features of a base object. [**Experimental**](Path_experimental.md).

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area.png  style="width:32px;"> [Feature area](Path_Area/ro.md): Creează o zonă de caracteristici din obiectele selectate


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area-Workplane.png  style="width:32px;"> [Feature area workplane](Path_Area_Workplane/ro.md): Creează un plan de lucru pentru zona de caracteristici


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.png  style="width:32px;"> [Tool Manager](Path_ToolLibraryEdit/ro.md): Editează Tool Manager


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture.

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other


<div class="mw-translate-fuzzy">

Path Workbench partajează mai multe concepte cu alte pachete software CAM, dar are propriile particularități. Dacă ceva pare rău, ar putea fi un loc bun pentru a începe.


</div>




<div class="mw-translate-fuzzy">

### Preferințe


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Preferences\...](Path_Preferences/ro.md): Preferințe disponibile în Atelierul Traiectorie.


</div>



## Script


<div class="mw-translate-fuzzy">

A se vedea pagina [Path scripting](Path_scripting/ro.md).


</div>

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.

## Roadmap

-   [Path Development Roadmap](Path_Development_Roadmap.md): Read this if you are a developer and want to contribute to Path.


<div class="mw-translate-fuzzy">


{{Userdocnavi/ro}}


</div>


{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/ro
