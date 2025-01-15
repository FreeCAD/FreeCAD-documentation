# Constructive solid geometry/es
## Introducción

[Geometría sólida constructiva](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (**CSG**) es un paradigma de modelización que se utiliza en muchos sistemas tradicionales de CAD. Consiste esencialmente en utilizar objetos sólidos primitivos y hacer operaciones booleanas con ellos, como la fusión, la sustracción y la intersección, para crear una forma final.

En FreeCAD, este método se utiliza principalmente con el <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo de pieza](Part_Workbench/es.md), que tiene la capacidad de crear objetos primitivos como <img alt="" src=images/Part_Box.svg  style="width:24px;"> [cajas](Part_Box/es.md), <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [cilindros](Part_Cylinder/es.md), y <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [esferas](Part_Sphere/es.md) y fusionarlos, o utilizarlos para cortar otros objetos con herramientas como **<img src="images/Part_Cut.svg" width=24px> [Corte Pieza](Part_Cut/es.md)**.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



*Flujo de trabajo de geometría sólida constructiva (CSG); se puede realizar cualquier número de operaciones sobre primitivos sólidos para crear otros objetos sólidos, y luego fusionarlos o cortarlos hasta producir la forma final.*

Alternativamente, el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md) utiliza un enfoque más moderno que el simple CSG; este método se llama [edición de características](feature_editing/es.md), lo que significa crear un sólido base, y luego añadir transformaciones paramétricas secuenciales para obtener un cuerpo final.


**Nota:**

Un [Cuerpo DiseñoPieza](PartDesign_Body/es.md) creado con el [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/es.md) también puede utilizarse en una operación booleana con otros objetos.

## Ejemplo

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



*Ejemplo de flujo de trabajo de geometría sólida constructiva (CSG): se fusionan partes primitivas (unión); se calcula la intersección de otras dos partes primitivas (común); se obtiene la diferencia (corte) de las dos formas anteriores.*

## Tutoriales

La página de [tutoriales](tutorials/es.md) proporciona algunos ejemplos sobre la creación de sólidos con el <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo Pieza](Part_Workbench/es.md) que utilizan el método **CSG**.

-   [Modelado tradicional, el método CSG](Manual:Traditional_modeling,_the_CSG_way/es.md)
-   [Tutorial de pelota de béisbol](Whiffle_Ball_tutorial/es.md)
-   [Tutorial de modelado básico](Basic_modeling_tutorial/es.md)



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common%20Questions.md) > [Part](Category_Part.md) > Constructive solid geometry/es
