# Topological naming problem/es
## Introducción




El [problema de denominación topológica](topological_naming_problem/es.md) en FreeCAD se refiere a la cuestión de que una forma cambie su nombre interno después de que se realice una operación de modelado (almohadilla, corte, unión, chaflán, filete, etc.). Esto dará lugar a que se rompan o se calculen incorrectamente otras características paramétricas que dependen de esa forma. Este problema afecta a todos los objetos de FreeCAD, pero es especialmente notable cuando se construyen sólidos con el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md), y al dimensionar esos sólidos con el <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Ambiente de trabajo DibujoTécnico](TechDraw_Workbench/es.md).

-   En <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [DiseñoPieza](PartDesign_Workbench/es.md), si un rasgo se apoya en una cara (o borde o vértice), el rasgo puede romperse si el sólido subyacente cambia de tamaño u orientación, ya que la cara (o borde o vértice) original puede ser renombrada internamente.
-   En <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [DibujoTécnico](TechDraw_Workbench/es.md), si una dimensión está midiendo la longitud de un borde proyectado, la dimensión puede romperse si se cambia el modelo 3D, ya que los vértices pueden ser renombrados cambiando así el borde medido.


<div class="mw-translate-fuzzy">

El problema de la denominación topológica es un problema complejo en el modelado CAD que se deriva de la forma en que las rutinas internas de FreeCAD manejan las actualizaciones de las formas geométricas creadas con el [OCCT kernel](OpenCASCADE/es.md). A partir de FreeCAD 0.19 se están realizando esfuerzos para mejorar el manejo del núcleo de las formas con el fin de reducir o eliminar tales problemas.

-   Hilo del foro: [Denominación Topológica, Mi Toma](https://forum.freecadweb.org/viewtopic.php?t=27278)


</div>

Starting with FreeCAD 0.19 there are ongoing development efforts to improve the core handling of shapes by adding heuristics that reduce the impact of these issues. The [naming algorithm](#Topological_naming_algorithm.md) is designed to reduce manual effort, sometimes by automatically fixing up problems, and other times presenting a likely solution, and otherwise at least clearly showing what caused the problem. The first stable release of FreeCAD to feature this new naming algorithm is 1.0. Over time, this algorithm will be applied to more parts of FreeCAD, and more automatic and assisted repair will be added in later versions.

El problema de la denominación topológica afecta y confunde con mayor frecuencia a los nuevos usuarios de FreeCAD. En DiseñoPieza, se aconseja al usuario que siga las mejores prácticas discutidas en la página [edición de características](feature_editing/es.md). Se recomienda encarecidamente el uso de objetos de referencia de apoyo como [planos](PartDesign_Plane/es.md) y [sistemas de coordenadas locales](PartDesign_CoordinateSystem/es.md) para producir modelos que no estén fácilmente sujetos a tales errores topológicos. En DibujoTécnico, se aconseja al usuario que añada dimensiones sólo cuando el modelo 3D esté completo y no se modificará más.



## Ejemplo

1\. En la <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md), crear un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [DiseñoPieza Cuerpo](PartDesign_Body/es.md), luego use <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [DiseñoPieza NuevoBoceto](PartDesign_NewSketch/es.md) y seleccionar el plano XY para dibujar el boceto base; luego realizar un <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [DiseñoPieza Pad](PartDesign_Pad/es.md) para crear un primer sólido.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Seleccione la cara superior del sólido anterior y, a continuación, utilice <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [DiseñoPieza NuevoBoceto](PartDesign_NewSketch/es.md) para dibujar otro boceto; a continuación, realice una segunda almohadilla.

+++
| <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;"> |
+++

3\. Selecciona la cara superior de la extrusión anterior, y una vez más crea un boceto, y un pad.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Ahora, haz doble clic en el segundo croquis, y modifícalo para que su longitud sea a lo largo de la dirección X; haciendo esto se recreará el segundo pad. El tercer croquis y la almohadilla permanecerán en el mismo lugar.

+++
| <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;"> |
+++

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. Ahora, haz doble clic en el segundo croquis de nuevo, y ajusta sus puntos para que una parte de él esté fuera de los límites definidos por el primer pad. Al hacer esto, el segundo pad volverá a calcular correctamente, sin embargo, al mirar la [vista de árbol](Tree_view/es.md), se indicará un error en el tercer pad.

+++
| <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;"> |
+++

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. Al hacer visibles el tercer croquis y la pastilla, queda claro que el cálculo del nuevo sólido no se ha realizado correctamente. El tercer croquis, en lugar de apoyarse en la cara superior del segundo pastilla, aparece en un lugar extraño, con su normal orientada hacia la dirección X. Esto da lugar a un pastilla no válido, ya que este pastilla estaría desconectado del resto del <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [DiseñoPieza Cuerpo](PartDesign_Body/es.md), lo que no está permitido.

El problema parece ser que cuando se modificó el segundo croquis, la cara superior de la segunda pastilla pasó de llamarse `Face13` a `Face14`. El tercer croquis está unido a `Face13` como lo estaba originalmente, pero como esta cara está ahora en el lateral (no en la parte superior), el croquis sigue su orientación y ahora está colocado incorrectamente.

+++
| <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;"> |
+++

7\. Para solucionar el problema, el tercer croquis debe ser mapeado a la cara superior de nuevo. Seleccione el croquis, haga clic en la elipsis (tres puntos) junto a la propiedad **Map Mode** y vuelva a elegir la cara superior del segundo pastilla. Entonces el croquis se mueve a la parte superior del sólido existente, y el tercer pastilla se genera sin problemas.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

+++
| <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;"> |
+++

Reasignar un boceto de esta manera puede hacerse cada vez que haya un error de denominación topológica, sin embargo, esto puede ser tedioso si el modelo es complicado y hay muchos bocetos de este tipo que necesitan ser ajustados.



## Solución

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

El [grafo de dependencia](Std_DependencyGraph/es.md) es una herramienta útil para observar las relaciones entre los distintos cuerpos del documento. El uso del flujo de trabajo de modelado original revela la relación directa que existe entre los bocetos y las almohadillas. Al igual que una cadena, es fácil ver que esta dependencia directa estará sujeta a problemas de nomenclatura topológica si cambia alguno de los eslabones de la secuencia.


<div class="mw-translate-fuzzy">

Como se explica en la página [edición de características](feature_editing/es.md), una solución a este problema es admitir bocetos no en las caras sino en los planos de referencia que están desplazados de los planos principales del [DiseñoPieza cuerpo](PartDesign_Body/es.md) Origen.


</div>

1\. Seleccione el origen del [ DiseñoPieza Cuerpo](PartDesign_Body/es.md) y asegúrese de que es visible. A continuación, seleccione el plano XY y haga clic en [DiseñoPieza Plano](PartDesign_Plane/es.md). En el cuadro de diálogo de desplazamiento del accesorio, dele un desplazamiento en la dirección Z para que el plano de referencia sea coplanario con la cara superior del primer pad.

2\. Repita el proceso pero esta vez añada un desplazamiento mayor para que el segundo plano de referencia sea coplanario con la cara superior de la segunda almohadilla.




+++
| <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;"> |
+++

3\. Seleccione el segundo croquis, haga clic en la elipsis junto a la propiedad **Modo mapa** y, a continuación, seleccione el primer plano de referencia. El plano de referencia ya está desplazado desde el plano XY del cuerpo, por lo que no es necesario un desplazamiento Z adicional para el croquis.

4\. Repita el proceso con el tercer croquis y seleccione el segundo plano de referencia como soporte. De nuevo, no es necesario ningún otro desplazamiento Z.

5\. El gráfico de dependencia muestra ahora que los croquis y los pads se apoyan en los planos de referencia. Este modelo es más estable, ya que cada croquis puede modificarse de forma esencialmente independiente de los demás.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Haz doble clic en el segundo croquis y modifica la forma. El segundo pad debería actualizarse inmediatamente sin causar problemas topológicos con el tercer croquis y el tercer pad.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. De hecho, cada boceto puede ser modificado sin interferir con los pads de los demás. Siempre que los pads tengan una longitud de extrusión suficiente, de modo que se toquen y formen un sólido contiguo, todo el cuerpo será válido.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">

## Tradeoffs

Añadir objetos de datos supone más trabajo para el usuario, pero en última instancia produce modelos más estables que están menos sujetos al problema de los nombres topológicos.

Naturalmente, los objetos de referencia pueden crearse antes de dibujar los bocetos y producir las almohadillas. Esto puede ser útil para visualizar la forma y las dimensiones aproximadas del cuerpo final.

Los planos de referencia también pueden basarse en otros planos de referencia. Esto crea una cadena de dependencias que también podría dar lugar a problemas topológicos; sin embargo, como los planos de referencia son objetos muy simples, los riesgos de tener estos problemas son menores que si se utiliza la cara de un objeto sólido como soporte.

Los objetos Datum, [puntos](PartDesign_Point/es.md), [líneas](PartDesign_Line/es.md), [planos](PartDesign_Plane/es.md), y [sistemas de coordenadas](PartDesign_CoordinateSystem/es.md), también pueden ser útiles como geometría de referencia, es decir, como ayudas visuales para mostrar las características importantes en el modelo, incluso si no se adjunta ningún croquis directamente a ellos.

## Topological naming algorithm 

Realthunder\'s topological naming algorithm, described in forum thread [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278), which was selected to reduce the impact of this problem, has been widely described as \"fixing the topological naming problem.\" This has unintentionally misled many users into thinking that it will no longer be helpful to use techniques like datums, explicit sketch placement, and [Feature editing](Feature_editing#Advice_for_creating_stable_models.md) to make models more stable. The algorithm is not intended to fix every failure introduced by topological naming ambiguity. Rather, it has three purposes.

1.  The first and most important purpose is, whenever possible, to **identify** broken references from topological changes and display an error to the user. Instead of having to work through a series of operations to find the first operation that diverges from the design intent, the operation that changes the names will normally be flagged with an error, making it much easier to manually fix model problems introduced by changes to operations or parameters.
2.  Sometimes, FreeCAD will be able to identify a **likely** fix for a broken reference, so that when the user is manually fixing up the flagged broken reference, a candidate will be presented for them to accept or change. A common example of this is dress-up operations like fillets and chamfers, where user might have to to edit the operation and either accept the proposed replacement feature selection or change it to correct it.
3.  In some cases, FreeCAD will be able to **automatically** resolve the broken reference, because enough information about the reference is stored to have high confidence that the replacement is correct. For example, when sketching directly on a face, the algorithm will frequently (but not always) correctly repair the reference to the face when the underlying geometry is changed parametrically. (When changing the structure, such as by adding or deleting operations in the middle of a Part Design Body, this kind of automatic repair will be less likely.) However, FreeCAD will do this only with high confidence in the correctness of the repair, because an incorrect automatic repair may re-introduce the problem of having to hunt for where a problem was introduced in order to repair a model after a modification. *First, do no harm.*

In FreeCAD 1.0, the implementation of this algorithm in the official FreeCAD release reached feature parity with Realthunder\'s \"Linkstage 3\" fork, where he originally developed the algorithm, as of the time the integration work started. There are new FreeCAD features that could use the algorithm but do not yet, and there will always be more opportunities to add candidate fixes and automatic repair. The initial work has provided a *framework* to use for these additional improvements over time, both in core FreeCAD and in Addons.



## Enlaces


<div class="mw-translate-fuzzy">

-   [PartDesign Redondeo - Denominación topológica](PartDesign_Fillet#Topological_naming/es.md)
-   [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278), a possible solution, by realthunder.
-   [Proyecto de denominación topológica](Topological_Naming_Project/es.md): idea para resolver el problema, por ickby.
-   [Scripting de datos topológicos](Topological_data_scripting/es.md)
-   [Edición de artículos](Feature_editing/es.md): contiene consejos alternativos para las técnicas de modelado estable.


</div>



## Vídeos

-   [Why do my FreeCAD models break? - \"Topological Naming Problem\"](https://youtu.be/6p2vqEEmWq4): Una explicación en vídeo de los problemas subyacentes de [Problema de denominación topológica](Topological_naming_problem/es.md)
-   [¡FreeCAD Está Fundamentalmente Roto! - ¿Ahora qué?\... Ayudame a decidir\...](https://www.youtube.com/watch?v=QSsVFu929jo): Un video de Maker Tales


 {{TechDraw Tools navi}} {{PartDesign Tools navi}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common%20Questions.md) > [TechDraw](Category_TechDraw.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Topological naming problem/es
