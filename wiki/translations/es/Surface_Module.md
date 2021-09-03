


<div class="mw-translate-fuzzy">





</div>

<img alt="El icono del Ambiente de trabajo superficie" src=images/Workbench_Surface.svg  style="width:128px;">


{{TOCright}}

## Introducción

El <img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> <img src=images/Part_Builder.svg style="width:Ambiente de trabajo Superficie](Surface_Workbench/es.md) proporciona herramientas para crear y modificar simples [NURBS surfaces](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline). Estas herramientas tienen una funcionalidad similar a la del **[16px"> <img src=images/PartDesign_AdditiveLoft.svg style="width:Creador Piezas](Part_Builder/es.md)** cuando se utiliza la opción **Cara de los bordes**. Sin embargo, a diferencia de esa herramienta, las herramientas del ambientes de Trabajo de Superficies son paramétricas y proporcionan opciones adicionales. En este sentido, las herramientas de este ambientes de trabajo son similares a **[16px"> <img src=images/PartDesign_AdditivePipe.svg style="width:DiseñoPieza LoftAditivo](PartDesign_AdditiveLoft/es.md)** y **[16px"> [DiseñoPieza TuberíaAditivos](PartDesign_AdditivePipe/es.md)**.

Algunas de las funciones que ofrece son:

-   Creación de superficies a partir de los bordes de los límites.
-   Alineación de la curvatura desde las caras vecinas.
-   Restricción de superficies a curvas y vértices adicionales.
-   Extensión de caras.
-   Una malla puede utilizarse como plantilla para crear curvas spline en su superficie.

<img alt="" src=images/Surface_example.png  style="width:350px;">

## Utilización

El ambiente de trabajo de superficies pretende crear caras con formas, lo que no es posible hacer con las herramientas estándar de otros ambientes de trabajo.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">


*Superficie creada con bocetos colocados en planos de referencia con las herramientas del [DiseñoPieza ambiente de trabajo](PartDesign_Workbench/es.md)*

El ambiente de trabajo de superficies se integra con otros ambientes de trabajo de FreeCAD. El ejemplo anterior fue creado a partir de **<img src=images/Sketcher_NewSketch.svg style="width:16px"> <img src=images/PartDesign_Plane.svg style="width:Bocetos](Sketch/es.md)** colocado en **[16px"> [DiseñoPieza Planos de referencia](PartDesign_Plane/es.md)** en el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md). El diseño puede ser totalmente paramétrico si todos los planos de referencia y los bocetos se definen en consecuencia. En la mayoría de los casos es suficiente dibujar un croquis cerrado para definir el límite de una cara, y luego utilizar diferentes opciones para modificar aún más su forma.

La superficie generada no puede colocarse dentro de un **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Std_Part.svg style="width:DiseñoPiezas Cuerpo](PartDesign_Body/es.md)**. Sin embargo, la superficie generada puede estar contenida dentro de un **[16px"> <img src=images/PartDesign_Body.svg style="width:Std Pieza](Std_Part/es.md)** junto con el **[16px"> asociado <img src=images/Part_Builder.svg style="width:Cuerpo](PartDesign_Body/es.md)** que contiene los planos de referencia y los bocetos. El botón no paramétrico **[16px"> [Pieza Creador](Part_Builder/es.md)** se puede utilizar para crear un [shell](Glossary#Shell.md) y finalmente un [solid](Glossary#Solid.md).

## Herramientas

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Relleno](Surface_Filling/es.md): rellena una serie de curvas límite con una superficie.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Rellenar curvas límite](Surface_GeomFillSurface/es.md): crea una superficie a partir de dos, tres o cuatro aristas límite.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Secciones](Surface_Sections/es.md): crea una superficie a partir de aristas que representan secciones transversales de la superficie.<small>(v0.19)</small> 

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extender cara](Surface_ExtendFace/es.md): extrapola la superficie en los límites con su parámetro local U y V.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> [Curva sobre malla](Surface_CurveOnMesh/es.md): crea segmentos de splines aproximados sobre una [malla](Mesh_Workbench/es.md) seleccionada.


<div class="mw-translate-fuzzy">





</div>


{{Surface Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
