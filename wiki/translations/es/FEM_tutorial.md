# FEM tutorial/es



<div class="mw-translate-fuzzy">


{{TutorialInfo/es
|Topic= Análisis de Elemento Finito
|Level= Principiante
|Time= 10 minutos + tiempo del Solver
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16 o superior
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

### Introducción

Este tutorial tiene como propósito el introducir al lector a la forma de trabajo básica del módulo FEM, así como a la mayoría de las herramientas disponibles para realizar un análisis estático.


</div>

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Requirements


<div class="mw-translate-fuzzy">

### Requisitos

-   FreeCAD versión 0.16 superior
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) y/o [GMSH](http://geuz.org/gmsh/) está instalado en el sistema
-   Para el caso de GMSH, se recomienda instalar el macro de [psicofil\'s macro](https://github.com/psicofil/Macros_FreeCAD)
-   [Calculix](http://www.calculix.de/) está instalado en el sistema
-   El lector tiene el conocimiento básico para utilizar los módulo Part y PartDesign


</div>


<div class="mw-translate-fuzzy">

### Procedimiento


</div>

### Modeling


<div class="mw-translate-fuzzy">

#### Modelado

En este ejemplo un Cubo es utilizado como objeto de estudio, pero modelos creados en los bancos de trabajo Parte y Diseño de Parte pueden ser utilizados en su lugar.


</div>


<div class="mw-translate-fuzzy">

1.  Crear un nuevo documento
2.  Activar el módulo Part
3.  Crear un Cubo
4.  Cambiar sus **Dimensiones** a las siguientes:
    1.  Altura: 1.000 mm
    2.  Longitud: 8.000 mm
    3.  Ancho: 1.000 mm


</div>

Ahora tenemos un modelo con el que se puede trabajar.

### Creating the Analysis 

#### Netgen


<div class="mw-translate-fuzzy">

#### Creando el análisis 

##### Netgen 

1.  Seleccione el modelo
2.  Clic en <img alt="" src=images/FEM_Analysis.png  style="width:32px;"> [Nuevo Análisis Mecánico](Fem_Analysis/es.md) desde el menú para crear un análisis con el objeto seleccionado
3.  En el diálogo de mallado, dé clic en **OK**


</div>


<div class="mw-translate-fuzzy">

También es posible arrastrar y depositar una malla a un Análisis Mecánico que no contenga una malla desde la vista del árbol


</div>

#### GMSH


<div class="mw-translate-fuzzy">

##### GMSH 

El uso del macro de psicofil es recomendado, y es usado para este ejemplo.

1.  Active el macro
2.  Seleccione el objeto que desee utilizar, en este caso nuestro Cubo
3.  Habilite la opción **Create Mechanical Analysis from mesh**
4.  Clic **OK**


</div>

Hemos mallado nuestro objeto y estamos listos para agregar restricciones y fuerzas.

### Constraints and Forces 


<div class="mw-translate-fuzzy">

#### Restricciones y Fuerzas 

1.  Oculte la malla desde la Vista de Árbol
2.  Muestre el modelo original
3.  Seleccione <img alt="" src=images/FEM_FixedConstraint.png  style="width:16px;"> [Crear una restricción FEM fija](FEM_ConstraintFixed/es.md)
4.  Seleccione la cara trasera del Cubo (la cara ubicada en el plano **YZ** ) y dé clic en OK
5.  Seleccione <img alt="" src=images/FEM_ForceConstraint.png  style="width:16px;"> [Crear una restricción FEM de fuerza](FEM_ConstraintForce/es.md)
6.  Seleccione la cara frontal del Cubo (la cara paralela a la cara trasera) y especifique el valor de **Carga Superficial** a 9000000.00
7.  Fije la **Direcciónn** a **-Z** seleccionando una de las aristas paralelas a esa dirección
8.  Clic OK


</div>

Hemos establecido las restricciones y fuerzas para nuestro estudio estático.

### Final preparations 


<div class="mw-translate-fuzzy">

#### Preparaciones finales 

1.  Seleccione <img alt="" src=images/FEM_Material.png  style="width:32px;"> [Material Mecánico\...](Fem_MechanicalMaterial/es.md) y seleccione Calculix como el material
2.  Clic **OK**


</div>

### Running the Solver 

#### Standard Procedure 

1.  Select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contained in the 
**Mechanical Analysis**
2.  Select <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Start calculation](FEM_SolverControl.md) from the menu
3.  Select **Write Calculix Input File**
4.  Select **Run Calculix**
5.  Click **Close**

#### Quick Procedure 

1.  Select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contained in the 
**Mechanical Analysis**
2.  Click on <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Quick Analysis](FEM_SolverRun.md).

### Analyzing Results 

1.  From the **Object Tree**, select the **Results** object
2.  Select <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow.md)
3.  Choose among the different Result types to view the results
4.  The slider at the bottom can be used to alter the mesh visualization. This allows us to visualize the deformation experienced by the object, keep in mind that this is an approximation.
5.  To remove the results select <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purge results](FEM_ResultsPurge.md)


{{Note|Comparison to previous example file|If you select the '''Z displacement''' result type, you can see that the obtained value is almost identical to the test example provided by FreeCAD. Differences may occur due to the quality of the mesh and the number of nodes it possesses.}}

We are now finished with the basic workflow for the [FEM Workbench](FEM_Workbench.md).


{{Tutorials navi

}} {{FEM Tools navi}} 
