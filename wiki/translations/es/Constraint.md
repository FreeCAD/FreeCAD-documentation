# Constraint/es
## Introducción


{{TOCright}}

En FreeCAD la palabra \"[Restricción](Constraint/es.md)\" se usa normalmente para referirse a una \"regla\" para dibujar formas geométricas dentro de un <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketch](Sketch/es.md) (`Sketcher::SketchObject` clase). Una restricción limita la posición de un determinado elemento geométrico de diferentes maneras, por ejemplo, puede especificar si el elemento es horizontal, vertical, tangente, paralelo, perpendicular, coincidente con un punto, concéntrico a otro objeto, etc.

Hay dos grandes tipos de restricciones:

-    **Restricciones geométricas**definen características de las formas sin especificar dimensiones exactas, por ejemplo, horizontalidad, verticalidad, paralelismo, perpendicularidad y tangencia.

-    **Datum**o **restricciones dimensionales** definen las características de las formas especificando dimensiones, por ejemplo, una longitud numérica o un ángulo.

Vea la información en el <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Ambiente de trabajo Coquizador](Sketcher_Workbench/es.md) para una lista de todas las restricciones que pueden ser aplicadas. Algunas de ellas se aplican a líneas, otras a curvas y otras a vértices. Ver también el [tutorial básico de boceto](Basic_Sketcher_Tutorial/es.md).

## Utilización

1.  Crear un boceto ya sea desde el <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Ambiente de trabajo croquizador](Sketcher_Workbench/es.md) o a través del <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md).
2.  Presiona
    -   
        **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher NuevoBoceto](Sketcher_NewSketch/es.md)**
        
        , o

    -   
        **[<img src=images/PartDesign_Body.svg style="width:16px"> [DiseñoPieza Cuerpo](PartDesign_Body/es.md)**
        
        seguido de **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [DiseñoPieza NuevoBoceto](PartDesign_NewSketch/es.md)**.
3.  Haga doble clic en el boceto creado para entrar en su modo de edición.
4.  Dibuja una serie de líneas usando **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Crear polilínea](Sketcher_CreatePolyline/es.md)**.
5.  Escoge una de las líneas, y usa **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Restringir vertical](Sketcher_ConstrainVertical/es.md)**.
6.  Escoge una de las líneas, y usa **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Restringir horizontal](Sketcher_ConstrainHorizontal/es.md)**.
7.  Escoge la línea vertical, y usa **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Restringir distancia Y](Sketcher_ConstrainDistanceY/es.md)**; asignar una distancia.
8.  Escoge la línea horizontal, y usa **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Constrain distancia X](Sketcher_ConstrainDistanceX/es.md)**; asignar una distancia.

## Notas


<div class="mw-translate-fuzzy">

-   Las restricciones son útiles para crear perfiles muy precisos que pueden ser convertidos en extrusiones sólidas usando el **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad/es.md)** o**[<img src=images/Part_Extrude.svg style="width:16px"> [Pieza extrusión](Part_Extrude/es.md)** operaciones.
-   Las restricciones sólo se utilizan dentro de [Sketches](Sketch/es.md); otros objetos 2D como los creados con el <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Ambiente de trabajo Borrador](Draft_Workbench/es.md) no entienden de restricciones; estas últimas simplemente se colocan en el espacio 3D, y sus propiedades definen su forma y posición.


</div>


{{Sketcher Tools navi

}} {{Document objects navi}} 

[<img src="images/Property.png" style="width:16px"> Glossary](Category_Glossary.md)

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Constraint/es
