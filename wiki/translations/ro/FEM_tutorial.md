---
 TutorialInfo:o
   Topic:  Finite Element Analysis
   Level:  Beginner
   Time:  10 minutes + Solver time
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.16.6700 or above
   Files: 
---

# FEM tutorial/ro




<div class="mw-translate-fuzzy">




</div>

## Introduction


<div class="mw-translate-fuzzy">

### Introducere

Acest tutorial are rolul de a introduce cititorul în fluxul de lucru de bază al Atelierului MEF, precum și majoritatea instrumentelor disponibile pentru a efectua o analiză statică.


</div>

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Requirements


<div class="mw-translate-fuzzy">

### Cerințe

-   FreeCAD version 0.16.6700 sau mai modernă
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) and/or [GMSH](http://geuz.org/gmsh/) este instalat în sistem
-   In cazul GMSH, instalarea este recomandată [psicofil\'s macro](https://github.com/psicofil/Macros_FreeCAD)
-   [Calculix](http://www.calculix.de/) este instalat în sistem
-   Cititorul are cunoștințele de bază pentru a utiliza Atelierele Piese (Part) PartDesign


</div>




<div class="mw-translate-fuzzy">

### Procedură


</div>

### Modeling


<div class="mw-translate-fuzzy">

#### Modelarea

În acest exemplu, un Cub este folosit ca obiect de studiu, dar modelele create în atelierele de lucru Part sau PartDesign pot fi folosite în schimb.


</div>


<div class="mw-translate-fuzzy">

1.  Creați un nou document
2.  Activați Atelierul Part Workbench
3.  Creați un Cube
4.  Schimbați-i dimensiunile**Dimensions** după cum urmează:
    1.  Height: 1.000 mm
    2.  Length: 8.000 mm
    3.  Width: 1.000 mm


</div>


<div class="mw-translate-fuzzy">

Acum avem un model cu care să lucrăm.


</div>

### Creating the Analysis 

1.  Activate the <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md).
2.  Select the **Model → <img src="images/FEM_Analysis.svg" width=16px> Analysis container‏‎** option from the menu.

### Constraints and Forces 


<div class="mw-translate-fuzzy">

#### Constrângeri și Forțe 

1.  Ascundeți plasa din vederea arorescentă Tree View.
2.  Arătați modelul original
3.  Selectați <img alt="" src=images/FEM_FixedConstraint.png  style="width:16px;"> [Create FEM fixed constraint](FEM_ConstraintFixed.md)
4.  Selectați fațeta din spate a Cube (fațeta de pe planul definit de axele **YZ**) și click OK
5.  Selectați <img alt="" src=images/FEM_ForceConstraint.png  style="width:16px;"> [Create FEM force constraint](FEM_ConstraintForce.md)
6.  Selectați fațeta din față a Cube (Fațeta paralelă cu fațeta din spate) și definiți **Area load** cu valoarea de 9000000.00
7.  Definiți **Direction** la **-Z** prin selectarea unei adintre fațetele paralele cu această direcție.
8.  Click OK


</div>

Am stabilit restricțiile și forțele pentru studiul nostru static.

### Material


<div class="mw-translate-fuzzy">

#### finalul Pregătirilor 

1.  Select <img alt="" src=images/FEM_Material.png  style="width:16px;"> [Mechanical material\...](FEM_MaterialSolid.md) and choose Calculix as the material
2.  Click **OK**


</div>

### Meshing

It is recommended to make a mesh as the last step in the analysis preparations due to association to a geometry in FreeCAD. Depending on FreeCAD installation, there can be Netgen or GMSH meshers, you can use any of them.

#### Netgen


<div class="mw-translate-fuzzy">

#### Crearea Analizei 

##### Netgen 

1.  Selectați modelull
2.  Click pe <img alt="" src=images/FEM_Analysis.png  style="width:16px;"> [New mechanical analysis](FEM_Analysis.md) din meniu pentru a crea o analiză a obiectului care a fost selectat
3.  In caseta de dialogul pentru crearea plasei, click **OK**


</div>


<div class="mw-translate-fuzzy">

Puteți, de asemenea, să glisați și să plasați o plasă într-o Analiză Mecanică care nu are o plasă în Vederea Arborescentă(Tree View).


</div>

#### GMSH

1.  Select the model
2.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md): Generates a finite element mesh for a model using Gmsh.
3.  In the meshing dialog, click **Apply** and **OK**.

Ne-am discretizat într-o plasă cu ochiuri acum obiectul și suntem gata să adăugăm constrângeri și forțe.

### Running the Solver 

#### Standard Procedure 


<div class="mw-translate-fuzzy">

#### Rularea Rezolvitorului 

##### Procedura Standard 

1.  Selectați obiectul rezolvitor <img alt="" src=images/FEM_Solver.png  style="width:16px;"> contained in the 
**Mechanical Analysis**
2.  Selectați <img alt="" src=images/FEM_Calculation.png  style="width:16px;"> [Start calculation](FEM_SolverControl.md) din meniul
3.  Selectați **Write Calculix Input File**
4.  Selectați **Run Calculix**
5.  Click pe **Close**


</div>

#### Quick Procedure 


<div class="mw-translate-fuzzy">

##### Procedură rapidă 

1.  Selectați obeictul rezolvitor <img alt="" src=images/FEM_Solver.png  style="width:16px;"> conținut în 
**Mechanical Analysis**
2.  Click pe <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:16px;"> [Quick Analysis](FEM_SolverRun.md).


</div>

### Analyzing Results 


<div class="mw-translate-fuzzy">

#### Analizarea Rezultatelor 

1.  Din arborescența obiect **Object Tree**, selectați obeictul **Results**
2.  Selectați <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Show result](FEM_ResultShow.md)
3.  Alegeți printre diferite tipuri de *Result* pentru a vedea rezultatele
4.  sliderul din partea de jos poate fi utilizat pentru a modifica vizulizarea plasei. Aceasta ne permite să vizualizăm deformația suferită de obiect, rețineți că este o aproximație.
5.  Pentru a șterge rezultatul selectați <img alt="" src=images/FEM_PurgeResults.png  style="width:16px;"> [Purge results](FEM_ResultsPurge.md)


</div>


{{Note|Compararea cu exemplele de fișiere  precedente|dacă selectați '''Z displacement''' result type, puteți vedea că valoarea obținută este aproape identică cu exemplul test oferit de FreeCAD. Diferențele pot să apară datorită calității plasei și a numărul de noduri pe care le posedă aceata.}}


<div class="mw-translate-fuzzy">

Am terminat acum cu fluxul de lucru de bază pentru [FEM Workbench](FEM_Workbench.md).


</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM tutorial/ro
