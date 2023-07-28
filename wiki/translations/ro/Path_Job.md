---
- GuiCommand:
   Name:Path Job
   Name/ro:Path: Job/Prelucrare
   Workbenches:[Path](Path_Workbench.md)
   MenuLocation:Path → Job
   Shortcut:**P** **F**
   SeeAlso:
---

# Path Job/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Job (Sarcină/Task) creează un nou obiect Lucru în documentul activ. Obiectul de activitate conține următoarele informații:

1.  O listă de definiții ale parametrilor instrumentului, specificând geometria, parametrii de tăiere și vitezele pentru instrumentele pentru operațiile de cale.
2.  O listă secvențială a fluxului de lucru Path Operations.
3.  Un corp de bază: O clonă folosită pentru deplasare.
4.  A Raw reprezentând materia primă care va fi prelucrată în atelierul Path.
5.  O foaie de calcul, care conține intrările utilizate de operațiile Path, inclusiv valorile și formulele statice.
6.  Parametrii de configurare care specifică calea de destinație, numele fișierului și extensia fișierului G-Code, precum și postprocesorul utilizat pentru a genera limbajul corespunzător pentru controlerul CNC țintă și personaliza unitățile de măsură, modificările sculei, spațiul de parcarea a sculei, etc.


</div>



## Utilizare


<div class="mw-translate-fuzzy">

1.  Press the **<img src="images/Path-Job.png" width=16px> [Job](Path_Job.md)** button


</div>


<div class="mw-translate-fuzzy">

GUI-ul de lucrări are cinci file aliniate orizontal, general, ieșire, configurare, instrumente și plan de lucru. Puteți confirma sau anula dialogul.


</div>



## General

![](images/Job_1.jpg )


<div class="mw-translate-fuzzy">

-   **Label**: The label of the Job as displayed in the tree view.
-   **Model**: The Base Object which defines by its shape the paths of the job. If it is a Part Design object it is usually the Body which you select here. If you have an element selected in the tree *before* you click the \"Add Job\" icon that element is already entered here. You can change it by selecting a different element from the dropdown menue.
-   **Description**: You can add some notes to the job here. Notes are only for your information and have no effect on the path.


</div>



## Rezultat

![](images/Job_2.jpg )

-   **Output File**: Set the name, extension, and the file path of the G-Code output. You can use the following placeholders:
    -   **%D** directory of the active document
    -   **%d** name of the active document (without extension)
    -   **%M** user macro directory
    -   **%j** name of the job


<div class="mw-translate-fuzzy">

-   **Processor**: Select the postprocesser for your machine.
-   **Arguments**: Add arguments for the postprocessor as needed.


</div>

## Setup

![](images/Job_3.jpg )

-   **Stock**: set the size and shape of the raw material.
-   **Orientation**: Selected Edge or Face is used to orient Base or Stock accordingly.
-   **Alignment**: select a Vertex to set origin or move Base or Stock



## Instrumente

![](images/Job_4.jpg )


<div class="mw-translate-fuzzy">

Add the tool(s) from your [Tooltable](Path_ToolLibraryEdit.md) which you need for the operations at this job.


</div>


<div class="mw-translate-fuzzy">

After adding a tool, you can set/change the feedrate and spindle speed if you need a different feedrate in this job. A change here dosn\'t change the parameters stored in the tooltable.


</div>

The default tool you can delete if you have a own tool added.



## Plan de lucru 

![](images/Job_5.jpg )

Dacă aveți o activitate care susține mai multe operațiuni de traiectorie, puteți stabili în ce ordine operațiile ar trebui efectuate. Pentru a reordona, selectați o operație și apăsați butonul sus sau jos.


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Job/ro
