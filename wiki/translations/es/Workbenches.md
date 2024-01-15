# Workbenches/es
<div class="mw-translate-fuzzy">

FreeCAD, al igual que muchas aplicaciones de diseño moderno como [Revit](https://es.wikipedia.org/wiki/Revit) o [CATIA](https://es.wikipedia.org/wiki/CATIA), se basa en el concepto de [de trabajo](https://es.wikipedia.org/wiki/Banco_de_trabajo%7CBanco). Un banco de trabajo puede considerarse como un conjunto de herramientas especialmente agrupadas para una determinada tarea. En un taller de muebles tradicional, se tendría una mesa de trabajo para el que trabaja con la madera, otra para el que trabaja con las piezas de metal, y quizá una tercera para el que monta todas las piezas juntas.


</div>

En FreeCAD se aplica el mismo concepto. Las herramientas se agrupan en bancos de trabajo según las tareas con las que están relacionadas.

Cuando pasas de un ambiente de trabajo a otro, las herramientas disponibles en la interfaz cambian. Barras de herramientas, barras de comandos y posiblemente otras partes de la interfaz cambian al nuevo banco de trabajo, pero el contenido de tu escena no cambia. Por ejemplo, puedes empezar a dibujar formas 2D con el Banco de trabajo Borradores y luego seguir trabajando en ellas con el Banco de trabajo Pieza.

Tenga en cuenta que a veces se hace referencia a un Banco de trabajo como un *Módulo*. Sin embargo, los Bancos de trabajo y los Módulos son entidades diferentes. Un Módulo es cualquier extensión de FreeCAD, mientras que un Banco de trabajo es un tipo especial de Módulo con una configuración de interfaz gráfica de usuario (barras herramientas y menús).



## Bancos de trabajo incorporados 

### Current

Los siguientes bancos de trabajo se incluyen en cada instalación de FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base/es.md). No se trata realmente de un banco de trabajo, sino de una categoría de comandos y herramientas \"estándar\" que pueden utilizarse en todos los bancos de trabajo.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> El [Banco de Trabajo Arquitectura](Arch_Workbench/es.md) para trabajar con elementos arquitectónicos.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> El [Banco de Trabajo de Borradores](Draft_Workbench/es.md) contiene herramientas 2D y operaciones CAD básicas en 2D y 3D.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> El [Banco de Trabajo MEF](FEM_Workbench/es.md) proporciona un flujo de trabajo de análisis de elementos finitos (FEA).


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> El [Banco de Trabajo de Inspecciónh](Inspection_Workbench/es.md) está hecho para dar herramientas específicas para el examen de formas. Todavía está en desarrollo.


</div>

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> El [Ambiente de Trabajo Malla](Mesh_Workbench/es.md) para trabajar con mallas trianguladas.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> El [Banco de trabajo OpenSCAD](OpenSCAD_Workbench/es.md) para la interoperabilidad con OpenSCAD y la reparación de [geometría sólida constructiva](constructive_solid_geometry/es.md) (CSG) del historial del modelo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> El [Banco de Trabajo Pieza](Part_Workbench/es.md) para trabajar con piezas CAD.


</div>

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> El [Banco de Trabajo DiseñoPiezas](PartDesign_Workbench/es.md) para construir formas de piezas a partir de croquis.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> El [Banco de Trabajo de Rutas](Path_Workbench/es.md) se utiliza para producir instrucciones de código G. Todavía está en desarrollo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> El [Banco de Trabajo Puntos](Points_Workbench/es.md) para trabajar con nubes de puntos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> El [Banco de Trabajo de Ingeniería Inversa](Reverse_Engineering_Workbench/es.md) pretende proporcionar herramientas específicas para convertir formas/sólidos/mallas en características paramétricas compatibles con FreeCAD. Todavía está en desarrollo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> El [Banco de Trabajo de Robots](Robot_Workbench/es.md) para estudiar los movimientos de los robots.


</div>

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> El [Banco de Trabajo Croquizador](Sketcher_Workbench/es.md) para trabajar con croquis de geometría restringida.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> El [Banco de Trabajo de Hojas de Cálculo](Spreadsheet_Workbench/es.md) para crear y manipular datos de hojas de cálculo.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> El [Centro de Trabajo Inicio](Start_Workbench/es.md) te permite saltar rápidamente a uno de los bancos de trabajo más comunes.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> El [Banco de Trabajo de Superficies](Surface_Workbench/es.md) proporciona herramientas para crear y modificar superficies. Es similar al constructor de formas de piezas Cara desde las aristas.


</div>

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> El [Banco de Trabajo DibujoTécnico](TechDraw_Workbench/es.md) para producir dibujos técnicos a partir de modelos 3D. Es el sucesor del [Banco de Trabajo de Dibujo](Drawing_Workbench/es.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> El [Banco de Trabajo del Prueba Estructura del marco](Testing/es.md) es para depurar FreeCAD.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> El [Ambiente de Trabajo Web](Web_Workbench/es.md) te proporciona una ventana de navegador en lugar de la [Vista 3D](3D_view/es.md) dentro de FreeCAD.


</div>

### Obsolete

The following workbenches are no longer included after version 0.20:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> El [Banco de trabajo de Dibujo](Drawing_Workbench/es.md) se utilizaba para la producción de dibujos técnicos, pero ahora ha quedado obsoleto. Todavía es necesario para leer archivos antiguos de FreeCAD que contengan objetos creados con este banco de trabajo. El [Banco de trabajo de DibujosTécnicos](TechDraw_Workbench/es.md) es su reemplazo más avanzado. {{Obsolete/es|0.17}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> El [Banco de Trabajo de Imágenes](Image_Workbench/es.md) para trabajar con imágenes de mapa de bits.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> El [Banco de Trabajo de Trazado de Rayos](Raytracing_Workbench/es.md) para trabajar con el trazado de rayos (renderizado).


</div>



## Ambiente de trabajo externos 

Los Ambientes de Trabajo de FreeCAD son fáciles de programar en [Python](Python/es.md), por lo que hay mucha gente desarrollando Ambientes de Trabajo adicionales fuera del área principal de desarrollo de FreeCAD.


<div class="mw-translate-fuzzy">

Los [Ambiente de trabajo externos](external_workbenches/es.md) página lista todo lo que se conoce en esta comunidad. La mayoría son fácilmente instalables desde dentro de FreeCAD, usando el [Gerente de Addon](Std_AddonMgr/es.md), que se encuentra en el menú **Herramientas → <img src="images/Std_AddonMgr.svg" width=24px> Gerente de Addon**.


</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/es
