# Migrating to FreeCAD from Fusion360/es
{{TOCright}}

## Fondo

Esta página está dirigida a los usuarios interesados en migrar a FreeCAD desde el mundo de Fusion 360.

## ¿Qué hago? 

1.  Lo primero que debes hacer es sacar tus archivos de los formatos y almacenamientos propietarios. Empieza por exportar tus modelos desde la nube a tu máquina local.
    -   Un método popular es usar este script [Exportador total Fusion360](https://github.com/Jnesselr/fusion-360-total-exporter).
2.  Recomendamos exportar al formato STEP.

## Glosario


**Por favor, consulte también el proyecto en curso [CAD Rosetta Stone](CAD_Rosetta_Stone/es.md) para aprender los nombres análogos que usan los CADs propietarios populares**

Consulte la página [Glossary](Glossary/es.md) en general, pero aquí hay una breve lista de términos específicos que los amigos de F360 pueden encontrar especialmente útiles:

-   Restricción Tangente - La forma de FreeCAD de **Restricción Colineal**. Ver <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Croquizador RestringirTangente](Sketcher_ConstrainTangent#Entre_dos_líneas_.28collinear.29.md).
-   Pastilla - La función **extruir** en FreeCAD. Lee el <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [DiseñoPiezas Pastilla](PartDesign_Pad/es.md) para saber más.
-   Topodenominación - Abreviatura de [Problema de denominación topológica](Topological_naming_problem/es.md). Cubierto muy bien en [Brodie Fairhall\'s youtube clip](https://www.youtube.com/watch?v=6p2vqEEmWq4)\].
--   

## PREGUNTAS MÁS FRECUENTES 

1.  ¿Qué formatos soporta FreeCAD?
    -   El formato de archivo nativo en FreeCAD es BREP, [representación de límites](https://en.wikipedia.org/wiki/Boundary_representation), proporcionado por el núcleo de geometría interno [OpenCASCADE (OCCT)](OpenCASCADE/es.md).
    -   FreeCAD soporta todos los formatos que soporta OCCT, así que STEP e IGES al menos.
2.  ¿Qué formatos debería usar para migrar a FreeCAD?
    -   STEP es el mejor formato porque es un formato de [Forma](Shape/es.md) sólido, en contraposición a un [Malla](Mesh/es.md) (STL, OBJ, DAE). Ejemplo, [Importar Paso con Colores](https://forum.freecadweb.org/viewtopic.php?f=3&t=50308).
    -   Importar un STL es posible, pero este formato de malla será difícil de modificar posteriormente. Recomendamos convertir las mallas importadas en Shapes sólidos usando **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Piezas FormaDeMalla](Part_ShapeFromMesh/es.md)**. Remodelar el objeto en FreeCAD, usando la malla como referencia, es el mejor consejo.

## Consejos

-   \@MPetrika ([twitter](https://twitter.com/MPetrikas/status/1362051484704264198)) recomienda instalar el programa de HakanSeven12 [Ambiente de trabajo ModernUI](ModernUI_Workbench/es.md)

## Recursos de aprendizaje 

-   [Fusion360 a FreeCAD - Introducción](https://www.youtube.com/watch?v=_GxJkB23ZHM), video par Brodie Fairhall.
-   [Fusion360 a FreeCAD - Parte 2](https://www.youtube.com/watch?v=IESZD4QS3P8), vídeo de Brodie Fairhall.
-   [V0.19 Benchmarking\--2019 Monthly Challenges](https://forum.freecadweb.org/viewtopic.php?f=36&t=50492), una serie de objetos creados con Fusion360 son remodelados usando FreeCAD, por el experimentado usuario ppemawm.
-   [Tutorial escrito para principiantes: desde la primera parte hasta el dibujo técnico](https://github.com/macdroid53/LearningFreeCAD) par macdroid53.
-   [Un recurso online para nosotros, usuarios habituales de FreeCAD](https://www.freecad.info/).

## Vídeos de comparación 

-   [Modelar una turbina de compresor en FreeCAD y Fusion360](https://www.youtube.com/watch?v=kirDbZd0dvI&feature=youtu.be)

## Ayuda

A esta página wiki le falta algo. Por favor, solicite [permisos wiki](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) en el foro para editar esta página.

## Relacionados

-   [Migración a FreeCAD desde OnShape](Migrating_to_FreeCAD_from_OnShape/es.md)

---
[documentation index](../README.md) > Migrating to FreeCAD from Fusion360/es
