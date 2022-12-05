---
- TutorialInfo:/ro
   Topic:Path Workbench
   Level:
   Time:
   Author:Chrisb
   FCVersion:
   Files:
---

# Path Walkthrough for the Impatient/ro




<div class="mw-translate-fuzzy">




</div>

## Aim


<div class="mw-translate-fuzzy">

Iată o demonstrație care arată modul de creare a unei sarcini WB Path plecând de la un model 3D, generând un cod G corect pentru dialectul unei mașini de frezat CNC anume.


</div>

## Modelul 3D 


<div class="mw-translate-fuzzy">

Proiectul începe cu un simplu model FreeCAD: un cub cu buzunar dreptunghiular,


</div>


<div class="mw-translate-fuzzy">

![](images/Path-SquarePocketModel.png )


</div>


<div class="mw-translate-fuzzy">

creat [Part Design](PartDesign_Workbench.md) incluzând un Corp/Body, o casetă/Box cu o Adâncitură/Pocket, bazat pe o schiță/Sketch orientată în planul XY plane.


</div>


<div class="mw-translate-fuzzy">

With the 3D Model completed, the Path Workbench is selected.


</div>


<div class="mw-translate-fuzzy">

## Sarcina de lucru 

The <img alt="" src=images/Path-Job.png  style="width:32px;"> [Job](Path_Job.md) is created.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-JobCreationDialog.png )


</div>


<div class="mw-translate-fuzzy">

În fereastra de creare a sarcinilor de muncă, faceți clic pe OK pentru a accepta Corpul ca model de bază, fără șablon.


</div>

### Definirea Sarcinii de lucru 


<div class="mw-translate-fuzzy">

Fereastra Edit Job se deschide în fereastra Task și fereastra Model afișează Stock ca un cub definit din polilinii care înconjoară corpul de bază. Este selectat Tab-ul de Configurare.


</div>

### REzultatul sarcinii de lucru 


<div class="mw-translate-fuzzy">

Tab-ul Output definește calea spre fișierul rezultat, numele și extensia fișierului de ieșire, precum și postprocesorul folosit. Pentru utilizatorii avansați, indicii arătați sub mouse arată argumente comune.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-JobOutput.png )


</div>

### Instrumentele Sarcinii de lucru 


<div class="mw-translate-fuzzy">

![](images/Path-JobTools.png )


</div>


<div class="mw-translate-fuzzy">

Modificați instrumentul Implicit prin selectarea lui și click pe butonul Edit. Aceasta deschide fereastra de editarea a controlerului de instrumente.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-ToolConfig.gif )


</div>


<div class="mw-translate-fuzzy">

Denumirea dată sculei și numărul sculei corespunde numărului sculei aparatului. Aici este instrumentul Nr. 4. Controlerul de scule este configurat pentru viteze de avans orizontale și verticale de 2mm / s și o viteză a axului de 2000 rpm.


</div>


<div class="mw-translate-fuzzy">

Selectați subpanelul Sculă a controlerului de scule. Setați diametrul și - dacă doriți să utilizați simularea acțiunii sculei mai târziu-adăugați unghiul de așchiere și adâncimea de așchiere.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-ToolAdd.gif )


</div>


<div class="mw-translate-fuzzy">

Valorile sunt confirmate prin apăsare lui OK.


</div>


<div class="mw-translate-fuzzy">

Pentru accesul facil, toate instrumentele pot fi predefinite <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:24px;">[Tool manager](Path_ToolLibraryEdit.md).


</div>

### Planul de lucru al Sarcinii de Lucru 


<div class="mw-translate-fuzzy">

Fila Planul de lucru începe și este populată de secvența Operațiuni de lucru, Comenzi parțiale de traiectorie și Dressup de traiectorie. Secvența acestor elemente este comandată aici.


</div>

Această arborescență este afișată după configurarea Sarcinii de lucru odată ce lucrarea Path Job is unfolded:


<div class="mw-translate-fuzzy">

![](images/Path-TreeWithJob.png )


</div>

## Operații cu Traiectoria 


<div class="mw-translate-fuzzy">

Două operații vor adăugate petnru a genera triectoria de frezare pentru this Path Job. Operația [Profile](Path_Profile.md) creează o traiectorie în jurul casetei și

[Pocket](Path_Pocket_Shape.md)  creează o traiectorie pentru frezarea interiorului buzunarului.


</div>


<div class="mw-translate-fuzzy">

For now we will keep it simple. The <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Contour](Path_Profile.md) button opens the Contour panel. After confirming with OK using the default values, see the green path around the object is visible.


</div>


<div class="mw-translate-fuzzy">

Selecting the bottom of the pocket and then the <img alt="" src=images/Path_Pocket.png  style="width:32px;"> [Pocket](Path_Pocket_Shape.md) button opens the Pocket Shape window. The default values for Base Geometry, Depths, and Heights are used, and the Operation subpanel is selected, and the Step Over Percent is set at 50.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-PocketOperation.gif )


</div>


<div class="mw-translate-fuzzy">

The pattern is changed to \"Offset\" and the Job Operation is confirmed for the pocket configuration with OK.


</div>

The result is a model with two paths:


<div class="mw-translate-fuzzy">

![](images/Path-WalkThroughResult.gif )


</div>

## Verificarea Traiectoriei 

Există două modalități de verificare a traiectoriilor create. Codul G poate fi inspectat, incluzând evidențierea segmentelor de cale corespunzătoare. Procesul de frezare a traiectoriei de lucru poate fi, de asemenea, simulat pentru a demonstra traiectoriile de unelte idealizate, necesare pentru ca geometria uneltelor să frezeze Semifabricatul.


<div class="mw-translate-fuzzy">

To inspect the G-Code use the <img alt="" src=images/Path_Inspect.png  style="width:32px;"> tool. Selecting the corresponding G-Code lines within the G-Code Inspection window highlights individual path segments.

![](images/Path-InspectWindow.gif )


</div>


<div class="mw-translate-fuzzy">

To start the simulation use the <img alt="" src=images/Path_Simulator.png  style="width:32px;"> [Path Simulator](Path_Simulator.md) tool.


</div>


<div class="mw-translate-fuzzy">

Adjust speed and accuracy and start the simulation with the play button.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-Simulation.gif )


</div>


<div class="mw-translate-fuzzy">

If you want to end the simulation click the Cancel button, it will remove the stock created for the simulation. If you click Ok this object will be kept in your Job.


</div>

## Postprocess the Job 

Ultimul pas în generarea Codului G pentru mașina de frezare țintă este post-procesarea sarcinii de lucru. Aceasta generează codurile G într-un fișier care poate fi încărcat la controlerul de mașinii țintă CNC. Pentru a apela postprocesorul:


<div class="mw-translate-fuzzy">

-   Select the Job object in the tree
-   Select the Path Postprocessing <img alt="" src=images/Path_PostProcess.png  style="width:32px;"> tool to postprocess the file. This opens a G-Code window allowing inspection of the final output file before it is saved.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-PostOutput.gif )


</div>


 {{Path Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Path](Path_Workbench.md) > Path Walkthrough for the Impatient/ro
