# FEM CalculiX Cantilever 3D/es
<div class="mw-translate-fuzzy">


{{TutorialInfo/es
|Topic= Finite Element Analysis
|Level= Beginner
|Time= 10 minutes
|Author=[http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd]
|FCVersion=0.16.6377 or above
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

### Introducción

Este ejemplo pretende mostrar cómo se ve un simple Análisis de elementos finitos (FEA) en FreeCADs [FEM Workbench](FEM_Workbench.md) y cómo se pueden visualizar los resultados. Se muestra cómo activar un FEA y cómo cambiar el valor de la carga y la dirección de la carga. Además, dado que el archivo de ejemplo se proporciona con cualquier instalación de FreeCAD, es fácil verificar si el módulo FEM está configurado correctamente.


</div>

<img alt="" src=images/FEM_example01_pic00.jpg  style="width:700px;">

## Requirements


<div class="mw-translate-fuzzy">

### Requisitos

-   Versión de FreeCAD = 0.16.6377 o superior.
-   Esto se puede verificar en el menú Ayuda -\> acerca de FreeCAD. El número de Revisión tiene que ser superior a 6377
-   No se necesita software externo para cargar el archivo de ejemplo, ver la malla y la geometría, así como para visualizar los resultados.
-   Para volver a ejecutar el FEA, el software de resolución de problemas CalculiX debe estar instalado en su computadora. Probablemente el solucionador ya se haya instalado junto con FreeCAD. Si el solucionador CalculiX no está instalado, consulte [ FEM Install](FEM_Install.md).


</div>

## Set up the example file 

### Load Start Workbench 

-   Start FreeCAD
-   The Start Workbench should be loaded

### Load the example file 

-   Go to the example projects and click on \"Load an FEM analysis example\"
-   If due to further operations some geometry, constraints or the results are broken or deleted just repeat the steps above.

<img alt="" src=images/FEM_example01_pic01.jpg  style="width:700px;">

### Activate the analysis container 

-   To work with an analysis the analysis has to be activated.
-   In the [tree view](Tree_view.md), right click on the <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> 
**MechanicalAnalysis**
-   Choose **Activate analysis**

<img alt="" src=images/FEM_example01_pic02.jpg  style="width:700px;">

### Analysis container and its objects 

-   If the analysis is activated FreeCAD itself will change the current workbench to FEM.
-   There are at least the 5 objects needed to make a static mechanical analysis.
-   <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> analysis container

1.  <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> a solver
2.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> a material
3.  <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> a fixed constraint
4.  <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> a force constraint
5.  <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> a FEM mesh

-   Since in the example here the results are included as well there is a sixth object, the results <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;">, elaborated on in the next paragraph.

### Visualizing Results 

1.  Be sure the analysis is activated.
2.  Be sure the analysis still contains the result object, if not just reload the example file.
3.  Click the <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow.md) button in the FEM toolbar.
4.  In task window choose `z-Displacement`. It shows `-88.443 mm` in negative z-direction. This makes sense since the force is in negative z-direction as well.
5.  Activate the check box besides the bottom slider of displacement show.
6.  The slider can be used to alter the mesh to view the deformation in a simplified manner.
7.  Choose among the different Result types to view all in the GUI available result types.

<img alt="" src=images/FEM_example01_pic03.jpg  style="width:400px;">

### Purging Results 

1.  Be sure the analysis is activated.
2.  To remove the results: select in the icon toolbar the <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purge results](FEM_ResultsPurge.md) button.

### Running the FEA 

-   In the [tree view](Tree_view.md) double click on the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">.
-   In the [task panel](Task_panel.md) of the solver object make sure static analysis is selected.
-   Click on write .inp file in the same task window. Watch the log window until it prints \"write completed.\"
-   Click on **Run CalculiX**. Since this is a very small analysis it should take less than a second to run.
-   In the text window it should print in green letters \"CalculiX done!\" and in the next line \"loading result sets \...\"
-   You just have finished your first FEA in FreeCAD if there has not been any error message.
-   Click on **Close** in the task window.
-   A new result object should be created. You know how to visualize the results already.
-   If you get an error message no solver binary or similar when triggering the analysis check [FEM Install](FEM_Install.md).

<img alt="" src=images/FEM_example01_pic04.jpg  style="width:400px;">

### Running the FEA the fast Way 

-   In tree view select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> of the analysis <img alt="" src=images/FEM_Analysis.svg  style="width:24px;">.
-   In the icon toolbar click on <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Quick Analysis](FEM_SolverRun.md).
-   The Calculix input file will be written, CalculiX will be triggered and the result object should be created.

### Changing Load Direction and Load Value 

-   In the [tree view](Tree_view.md) select the FEM mesh object <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> and press the **Space** key.
    -   **Result:** The visibility of the FEM mesh will be turned off. The geometrical model is still visible.
-   In the [tree view](Tree_view.md) double click on the force constraint object to open its [task panel](Task_panel.md)
-   In the task window change the load value to **500000000 N = 500 MN** (**Note:** force unit in task window has to be in N)
-   Click on the **Direction** button.
-   On the geometrical model click on one of the long edges in x-direction.
    -   **Result:** The red arrows that illustrate force will change their direction in x-direction. They indicate the fixed direction.
-   Since tension should be applied to the box the Reverse Direction needs to be triggered by clicking on it.
-   The red arrows of the force will change their direction.
-   Click on **OK** in task window.

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Toggle the [visibility](Std_ToggleVisibility.md) of the FEM mesh <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> \'On\' by selecting it in tree view and pressing the **Space** key.
-   You know how to trigger an analysis and how to visualize results already.
-   The deformation in x-direction should be 19.05 mm.

<img alt="" src=images/FEM_example01_pic06.jpg  style="width:400px;">

## What next? 


<div class="mw-translate-fuzzy">

#### ¿Qué sigue? 

-   Ahora hemos terminado con el flujo de trabajo básico para el [ Módulo FEM](FEM_Workbench/es.md).
-   Ahora está preparado para hacer el segundo [ FEM tutorial](FEM_tutorial.md).
-   Crearemos el cantilever CalculiX por nosotros mismos y compararemos los resultados con la teoría del haz.


</div>


{{Tutorials navi

}} {{FEM Tools navi}}

---
[documentation index](../README.md) > FEM CalculiX Cantilever 3D/es
