# <img alt="El icono del Ambiente de trabajo MEF" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/es


{{TOCright}}

## Introducción

El [Ambiente de trabajo MEF](FEM_Workbench/es.md) provee un moderno [Método de los elementos finitos](https://es.wikipedia.org/wiki/M%C3%A9todo_de_los_elementos_finitos) flujo de Análisis de Elementos Finitos (AEF) para FreeCAD. Principalmente estoy significa que todas las herramientas para hacer un Analisis de Elementos Finitos estan combinadas en una (GUI) Interface Grafica de Usuario.

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Flujo de Trabajo 

Los pasos para realizar un análisis de elementos finitos son:

1.  Preprocesamiento: configurar el problema de análisis.
    1.  Modelar la geometría: crear la geometría con FreeCAD, o importarla desde otra aplicación.
    2.  Crear un análisis.
        1.  Añadiendo restricciones de simulación como cargas y soportes fijos al modelo geométrico.
        2.  Añadiendo materiales a las partes del modelo geométrico.
        3.  Creando una malla de elementos finitos para el modelo geométrico, o importándola desde una aplicación diferente.
2.  Solucionar: ejecutar un solucionador externo desde FreeCAD.
3.  Solving: ejecutando un solver externo desde FreeCAD.
4.  Postproceso: visualizando los resultados del análisis desde dentro de FreeCAD, o exportando los resultados para que puedan ser postprocesados con otra aplicación.

El Ambiente de trabajo MEF puede utilizarse en Linux, Windows y Mac OSX. Dado que el ambiente de trabajo hace uso de solucionadores externos, la cantidad de configuración manual dependerá del sistema operativo que esté utilizando. Ver [Instalación de MEF](FEM_Install/es.md) para instrucciones sobre la configuración de las herramientas externas.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



*Flujo de trabajo del ambiente de trabajo MEF; el ambiente de trabajo llama a dos programas externos para realizar el mallado de un objeto sólido, y realizar la solución real del problema de elementos finitos*

## Menú: Modelo 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Contenedor Análisis](FEM_Analysis/es.md): Crea un nuevo contenedor para un análisis mecánico. Si se selecciona un sólido en la vista de árbol antes de hacer clic en él, se abrirá a continuación el diálogo de malla.

### Materiales

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Material para sólidos](FEM_MaterialSolid/es.md): Permite seleccionar un material de la base de datos.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Material para liquidos](FEM_MaterialFluid/es.md): Permite seleccionar un material de la base de datos.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Material mecánico no lineal](FEM_MaterialMechanicalNonlinear/es.md): Permite seleccionar un material de la base de datos.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Material reforzado (hormigón)](FEM_MaterialReinforced/es.md): Le permite seleccionar materiales reforzados compuestos por una matriz y una armadura de la base de datos.

-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Editor de materiales](Material_editor/es.md): Te permite abrir el editor de materiales para editarlos.

### Geometría Elementos 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Corte transversal de viga](FEM_ElementGeometry1D/es.md):

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Rotación de viga](FEM_ElementRotation1D/es.md):

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Espesor de caja de placa](FEM_ElementGeometry2D/es.md):

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Sección de fluido para flujo 1D](FEM_ElementFluid1D/es.md): Crea un elemento de sección de fluido FEM para redes neumáticas e hidráulicas.

### Restricciones electrostáticas 

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Restricción Potencial electrostático](FEM_ConstraintElectrostaticPotential/es.md):

### Restricciones Fluido 

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Restricción de velocidad inicial de flujo](FEM_ConstraintInitialFlowVelocity/es.md): Utilizada para definir una velocidad de flujo inicial para el dominio.

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Restricción de velocidad de flujo](FEM_ConstraintFlowVelocity/es.md): Utilizada para definir una velocidad de flujo como condición de contorno en un borde (2D) o cara (3D).

### Restricciones Geométricas 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Restricción de rotación de plano](FEM_ConstraintPlaneRotation/es.md): Utilizada para definir una restricción de rotación de plano sobre una cara plana.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Impresión de la sección de restricciones](FEM_ConstraintSectionPrint/es.md): {{Version/es|0.19}}


</div>

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Restricción de transformación](FEM_ConstraintTransform/es.md): Utilizada para definir una restricción de transformación en una cara.

### Restricciónes Mecánicas 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Restricción fija](FEM_ConstraintFixed/es.md): Utilizada para definir una restricción fija de un punto/arista/cara.

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Restricción de desplazamiento](FEM_ConstraintDisplacement/es.md): Utilizada para definir una restricción desplazamiento de un punto/arista/cara(s).

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Restricción de contacto](FEM_ConstraintContact/es.md): Utilizada para definir una restricción de contacto entre dos caras.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Empate de restricciones](FEM_ConstraintTie/es.md): {{Version/es|0.19}}

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Restricción de fuerza](FEM_ConstraintForce/es.md): Utilizada para definir una fuerza en Newtons aplicada uniformemente a una cara seleccionada en una dirección definida.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Restricción de presión](FEM_ConstraintPressure/es.md): Utilizada para definir una restricción de presión

-   <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Constraint centrif](FEM_ConstraintCentrif.md): Used to define a centrifugal body load constraint. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Restricción de peso propio](FEM_ConstraintSelfWeight/es.md): Utilizado para definir una aceleración de gravedad actuando sobre un modelo.

### Restricciónes Térmicas 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Restricción inicial de temperatura](FEM_ConstraintInitialTemperature/es.md): Utilizado para definir una restricción inicial de temperatura de un cuerpo.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Restricción de flujo de calor](FEM_ConstraintHeatflux/es.md): Utilizado para definir una restricción de flujo de calor sobre una(s) cara(s).

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Restricción de temperatura](FEM_ConstraintTemperature/es.md): Utilizado para definir una restricción de temperatura sobre un punto/arista/cara(s).

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Restricción de cuerpo de fuente de calor](FEM_ConstraintBodyHeatSource/es.md):

### Restricciones sin solucionador 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Condición límite del fluido](FEM_ConstraintFluidBoundary/es.md):

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Restricción de rodamiento](FEM_ConstraintBearing/es.md): Utilizado para definir una restricción de rodamiento.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Restricción de engrane](FEM_ConstraintGear/es.md): Utilizado para definir una restricción de engrane.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Restricción de polea](FEM_ConstraintPulley/es.md): Utilizado para definir una restricción de polea.

### Sobrescribir Constantes 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Permisividad constante del vacío](FEM_ConstantVacuumPermittivity/es.md): {{Version/es|0.19}}

## Menú de Malla 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Malla MEF a partir de forma por Netgen](FEM_MeshNetgenFromShape/es.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Malla MEF a partir de forma por Gmsh](FEM_MeshGmshFromShape/es.md):


</div>

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Capa límite de la malla FEM](FEM_MeshBoundaryLayer/es.md):

Crea mallas anisotrópicas para realizar cálculos precisos cerca de los límites.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Region de malla MEF](FEM_MeshRegion/es.md): Crea una(s) zona(s) localizada(s) para mallar, lo que optimiza el tiempo de análisis.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Grupo de malla MEF](FEM_MeshGroup/es.md): Agrupa y etiqueta los elementos de una malla (vértice, arista, superficie), útil para exportar la malla a resolvedores externos.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Colocar nodos](FEM_CreateNodesSet/es.md): Crea/define una colocacion de nodo en una malla MEF.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [Malla MEF a malla](FEM_FemMesh2Mesh/es.md): Convierte la superficie de una malla MEF a una malla.

## Menú: Solve 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Herramientas del Solucionador CalculiX Estándar](FEM_SolverCalculixCxxtools/es.md): Crea un nuevo solucionador para este analisis. En la mayoria de los casos el solucionador es creado junto con el analisis.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solucionador CalculiX (experimental)](FEM_SolverCalculiX/es.md):

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solucionador Elmer](FEM_SolverElmer/es.md): Crea el controlador del Solucionador para Elmer. Es independiente de otros objetos solucionadores.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md):

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solucionador Z88](FEM_SolverZ88/es.md):

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Ecuación de elasticidad](FEM_EquationElasticity/es.md):

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Ecuación de la fuerza eléctrica](FEM_EquationElectricforce/es.md): <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Ecuación electrostatica](FEM_EquationElectrostatic/es.md):

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Ecuación de flujo](FEM_EquationFlow/es.md):

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Ecuación de flujo](FEM_EquationFlux/es.md):

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Ecuación de calor](FEM_EquationHeat/es.md):

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Control del trabajo del solucionador](FEM_SolverControl/es.md): Abre un nuevo menu para ajustar y iniciar el solucionador seleccionado.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Ejecutar calculo de solucionador](FEM_SolverRun/es.md): Ejecuta el solucionador seleccionado del análisis activo.

## Menú de Resultados 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Purga de resultados](FEM_ResultsPurge/es.md): Elimina los resultados del análisis activos.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Mostrar resultados](FEM_ResultShow/es.md): Used to display the result of an analysis.

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Aplicar cambios a la canaliza](FEM_PostApplyChanges/es.md):


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Pos canaliza a resultado](FEM_PostPipelineFromResult/es.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Filtro de deformación](FEM_PostFilterWarp/es.md):


</div>

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Filtro de clip Escalar](FEM_PostFilterClipScalar/es.md)

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Función Filtro de corte](FEM_PostFilterCutFunction/es.md):

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Filtro de clip de región](FEM_PostFilterClipRegion/es.md):

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Filtro clip de línea](FEM_PostFilterDataAlongLine/es.md):

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Gráfico de linealización de tensiones](FEM_PostFilterLinearizedStresses/es.md):

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Datos en el filtro de clip de punto](FEM_PostFilterDataAtPoint/es.md):

-   [Funciones del filtro](FEM_PostCreateFunctions/es.md):
    -   <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;">
    -   <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;">

## Menú: Utilidades 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Plano de recorte en la cara](FEM_ClippingPlaneAdd/es.md):

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Eliminar todos los planos de recorte](FEM_ClippingPlaneRemoveAll/es.md):

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Abrir ejemplos MEF](FEM_Examples/es.md): Abre la interfaz gráfica de usuario para acceder a los ejemplos de MEF.

## Menú de contexto 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Limpiar malla MEF](FEM_MeshClear/es.md): Elimina el archivo de malla del archivo de FreeCAD. Útil para aligerar un archivo de FreeCAD.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Mostrar información de la malla MEF](FEM_MeshDisplayInfo/es.md):

## Preferencias

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferencias\...](FEM_Preferences/es.md): Preferencias disponibles en las herramientas MEF.

## Información

En las siguientes páginas se explican diferentes temas del ambiente de trabajo MEF.

[MEF Instalación](FEM_Install/es.md): una descripción detallada sobre cómo configurar los programas externos utilizados en el ambiente de trabajo.

[Malla en MEF](FEM_Mesh/es.md) más información sobre la obtención de una malla para el análisis de elementos finitos.

[Solucionador MEF](FEM_Solver/es.md): más información sobre los diferentes solvers disponibles en el banco de trabajo, y los que podrían utilizarse en el futuro.

[MEF CalculiX](FEM_CalculiX/es.md): más información sobre CalculiX, el solucionador por defecto utilizado en el ambiente de trabajo para el análisis estructural.

[Hormigón MEF](FEM_Concrete.md) interesante información sobre el tema de la simulación de estructuras de hormigón.

## Tutorials


<div class="mw-translate-fuzzy">

## Tutoriales

Tutorial 1: [MEF CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/es.md); un análisis básico de los rayos de apoyo.


</div>

Tutorial 2: [Tutorial MEF](FEM_tutorial/es.md); un simple análisis de tensión de una estructura.

Tutorial 3: [Tutorial MEF en Python](FEM_Tutorial_Python/es.md); establecer el ejemplo del voladizo completamente a través de la escritura en Python, incluyendo la malla.

Tutorial 4: [MEF cizalla de un bloque compuesto](FEM_Shear_of_a_Composite_Block/es.md); ver la deformación de un bloque que está compuesto por dos materiales.

Tutorial 5: [Análisis MEF transitorio](Transient_FEM_analysis/es.md)

Tutorial 6: [Post-proceso de los resultados de MEF con Paraview](Post-Processing_of_FEM_Results_with_Paraview/es.md)

Tutorial 7: [Ejemplo MEF Capacitancia Dos Bolas](FEM_Example_Capacitance_Two_Balls/es.md); Tutorial GUI 6 de Elmer \"Electrostática Capacitancia Dos Bolas\" usando Ejemplos MEF.

Tutoriales de análisis termomecánico acoplado por [openSIM](https://opensimsa.github.io/training.html)

Video Tutorial 1 [Vídeo de MEF para principiantes](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (incluye enlace a YouTube)

Video Tutorial 2 [Vídeo de MEF para principiantes](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (incluye enlace a YouTube)

Más video Tutoriales [anisim Software de ingeniería de código abierto](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (en alemán)

## Extendiendo el Ambiente de trabajo MEF 

The FEM Workbench is under constant development. An objective of the project is to find ways to easily interact with various FEM solvers, so that the end user can streamline the process of creating, meshing, simulating, and optimizing an engineering design problem, all within FreeCAD.

The following information is aimed at power users and developers who want to extend the FEM Workbench in different ways. Familiarity with C++ and Python is expected, and also some knowledge of the \"document object\" system used in FreeCAD is necessary; this information is available in the [Power users hub](Power_users_hub.md) and the [Developer hub](Developer_hub.md). Please notice that since FreeCAD is under active development, some articles may be too old, and thus obsolete. The most up to date information is discussed in the [FreeCAD forums](https://forum.freecadweb.org/index.php), in the Development section. For FEM discussions, advice or assistance in extending the workbench, the reader should refer to the [FEM subforum](https://forum.freecadweb.org/viewforum.php?f=18).


<div class="mw-translate-fuzzy">

Los siguientes artículos explican cómo se puede ampliar el banco de trabajo, por ejemplo, añadiendo nuevos tipos de condiciones de contorno (restricciones) o ecuaciones.

-   [Extender modulo MEF](Extend_FEM_Module/es.md)
-   [Tutorial de adición de restricciones MEF](Add_FEM_Constraint_Tutorial/es.md)
-   [Añadir el tutorial de la ecuación MEF](Add_FEM_Equation_Tutorial/es.md)


</div>

A developer\'s guide has been written to help power users in understanding the complex FreeCAD codebase and the interactions between the core elements and the individual workbenches. The book is hosted at github so multiple users can contribute to it and keep it updated.

-   [Early preview of ebook: Module developer\' guide to FreeCAD source](https://forum.freecadweb.org/viewtopic.php?t=17581) forum thread.
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) github repository.

## Extender la documentación de Ambiente de trabajo MEF 

-   Se puede encontrar más información sobre la ampliación o la falta de documentación de MEF en el foro: [Documentación MEF que falta en la Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/es
