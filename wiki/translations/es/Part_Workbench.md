# Part Workbench/es
<div class="mw-translate-fuzzy">





</div>

<img alt="El icono del Ambiente de trabajo Pieza" src=images/Workbench_Part.svg  style="width:128px;">






## Introducción


<div class="mw-translate-fuzzy">

Las sólidas capacidades de modelado de FreeCAD se basan en la [OpenCASCADE](OpenCASCADE/es.md) (OCCT), un sistema CAD de calidad profesional que presenta una creación y manipulación avanzada de geometría 3D. El <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo pieza](Part_Workbench/es.md) es una capa que se encuentra en la parte superior de las bibliotecas de la OCCT, que da al usuario acceso a las primitivas y funciones geométricas de la OCCT. Esencialmente todas las funciones de dibujo 2D y 3D en cada ambiente de trabajo (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Borrador](Draft_Workbench/es.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Croquizador](Sketcher_Workbench/es.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [DiseñoPieza](PartDesign_Workbench/es.md), etc.), se basan en estas funciones expuestas por el ambiente de trabajo DiseñoPieza. Por lo tanto, el Ambiente de trabajo DiseñoPieza se considera el componente central de las capacidades de modelado de FreeCAD.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The Part Workbench can also create objects that are not solids, such as faces, shells, and objects with only edges or vertices. It also provides a variety of general purpose tools for geometry manipulation, geometry validation, and making copies.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) uses an alternative workflow for creating solids. For a detailed discussion of the Part Workbench versus the Part Design Workbench see [Part and Part Design](Part_and_PartDesign.md).


</div>

![](images/Part_Workbench_Example.jpg )



## Herramientas


<div lang="en" dir="ltr" class="mw-content-ltr">

### Solids toolbar 


</div>

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Caja](Part_Box/es.md): Crea una caja.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/es.md): Crea un cilindro.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Esfera](Part_Sphere/es.md): Crea una esfera.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cono](Part_Cone/es.md): Crea un cono.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube.md): Creates a tube.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Create primitives\...](Part_Primitives.md): A tool to create one of the following primitives:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plane](Part_Plane.md): Creates a plane.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md): Creates a box. This object can also be created with the [Box](Part_Box.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder. This object can also be created with the [Cylinder](Part_Cylinder.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone. This object can also be created with the [Cone](Part_Cone.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere. This object can also be created with the [Sphere](Part_Sphere.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid.md): Creates a ellipsoid.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus. This object can also be created with the [Torus](Part_Torus.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prism](Part_Prism.md): Creates a prism.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Wedge](Part_Wedge.md): Creates a wedge.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix.md): Creates a helix.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spiral](Part_Spiral.md): Creates a spiral.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Circle](Part_Circle.md): Creates a circular arc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse.md): Creates an elliptical arc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Creates a point.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line.md): Creates a line.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regular polygon](Part_RegularPolygon.md): Creates a regular polygon.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shape builder\...](Part_Builder.md): Creates shapes from various primitives.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Part tools toolbar 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.


</div>

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrusión](Part_Extrude/es.md): Extruye caras planas.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolve](Part_Revolve.md): Creates a solid by revolving an object (not a solid) around an axis.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Mirror](Part_Mirror.md): Mirrors the selected object across a mirror plane.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scale](Part_Scale.md): Scales one or more shapes. <small>(v1.0)</small> 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Fillet](Part_Fillet.md): Fillets (rounds) edges of an object.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chamfer](Part_Chamfer.md): Chamfers edges of an object.


</div>

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Hacer cara a partir de alambres](Part_MakeFace/es.md): Hace una cara a partir de un conjunto de hilos (contornos).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Superficie reglada](Part_RuledSurface/es.md): Crea una superficie reglada.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft.md): Lofts from one profile to another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep.md): Sweeps one or more profiles along a path.


</div>

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Sección](Part_Section/es.md): Crea una sección por la intersección de un objeto con un plano de sección.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Secciones transversales\...](Part_CrossSections/es.md): Crea una o más secciones transversales a través de un objeto.

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Relleno:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Relleno](Part_Offset/es.md): Construye una forma paralela a cierta distancia de un original.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Relleno](Part_Offset2D/es.md): Construye un cable paralelo a cierta distancia de un original, o amplía/contrae una cara plana.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Espesor](Part_Thickness/es.md): Ahueca un sólido.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Proyección sobre superficie](Part_ProjectionOnSurface/es.md): Proyecta un logo, texto o cualquier cara, cable, borde a una superficie.

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Establecer colores](Part_FaceColors/es.md): Asigna colores a las caras individuales de los objetos.




<div class="mw-translate-fuzzy">

### Booleano


</div>

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Compuesto:

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Hacer compuesto](Part_Compound/es.md): Crea un compuesto a partir de los objetos seleccionados.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explotar compuesto](Part_ExplodeCompound/es.md): Divide los compuestos.


</div>

  - <img alt="" src=images/Part_CompoundFilter.svg  style="width:32px;"> [Filtro compuesto](Part_CompoundFilter/es.md): Extrae las partes individuales de los compuestos.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Booleans.svg  style="width:32px;"> [Operaciones Booleanas](Part_Boolean/es.md): Realiza operaciones booleanas sobre objetos.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts one object from another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse.md): Fuses two or more objects.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Común](Part_Common/es.md): Extrae la parte común (intersección) de dos objetos.


</div>

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Unión:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Conectar](Part_JoinConnect/es.md): Conecta los interiores de los objetos huecos.

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Incrustar](Part_JoinEmbed/es.md): Incrusta un objeto hueco en otro objeto hueco.

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Recorte](Part_JoinCutout/es.md): Crea un recorte en una pared de un objeto para otro objeto hueco.

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> División:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Fragmentos booleanos](Part_BooleanFragments/es.md): Crea todas las piezas obtenidas de las operaciones booleanas.

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Recorta una pieza](Part_SliceApart/es.md): Rebana y divide un objeto intersectándolo con otros objetos.

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Corte](Part_Slice/es.md): Corta un objeto intersectándolo con otros objetos.

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [XOR](Part_XOR/es.md): Elimina el espacio compartido por un número par de objetos (versión simétrica de [Cortar](Part_Cut/es.md)).

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Comprobar geometría](Part_CheckGeometry/es.md): Comprueba la geometría de los objetos seleccionados en busca de errores.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Derrotar](Part_Defeaturing/es.md): Elimina las características de un objeto.



### Otras herramientas 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Importar](Part_Import/es.md): Importa desde archivos \*.IGES, \*.STEP o \*.BREP.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Exportar](Part_Export/es.md): Exporta a archivos \*.IGES, \*.STEP o \*.BREP.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [CajaSelección](Part_BoxSelection/es.md): Selecciona las caras de un área rectangular.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Forma a partir malla](Part_ShapeFromMesh/es.md): Crea un objeto de forma a partir de un objeto de malla.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Puntos desde malla](Part_PointsFromMesh/es.md): Crea un objeto de forma hecho de puntos a partir de un objeto de malla.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convertir en sólido](Part_MakeSolid/es.md): Convierte un objeto de forma en un objeto sólido.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Invertir formas](Part_ReverseShape/es.md): Invierte las normales de todas las caras de los objetos seleccionados.


</div>

-   Crear una copia:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Crear copia simple](Part_SimpleCopy/es.md): Crea una copia simple de un objeto seleccionado.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Crear copia transformada](Part_TransformedCopy/es.md): Crea una copia transformada de un objeto seleccionado.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Crear copia de elemento de forma](Part_ElementCopy/es.md): Crea una copia de un elemento (vértice, arista, cara) de un objeto seleccionado.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refinar forma](Part_RefineShape/es.md): Limpia las caras eliminando las líneas innecesarias.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Attachment](Part_EditAttachment/es.md): Adjunta un objeto a otro objeto.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Obsolete tools 


</div>



### Medida


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Std Measure](Std_Measure.md) tool replaces the tools listed below. <small>(v1.0)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Medida Lineal](Part_Measure_Linear/es.md): Crea una medida lineal.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Medida Angular](Part_Measure_Angular/es.md): Crea una medida angular.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Actualización de medidas](Part_Measure_Refresh/es.md): Actualiza todas las mediciones.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Borrar todo](Part_Measure_Clear_All/es.md): Borra todas las mediciones.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Alternar todo](Part_Measure_Toggle_All/es.md): Muestra u oculta todas las mediciones.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Alternar 3D](Part_Measure_Toggle_3D/es.md): Muestra u oculta las medidas 3D.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Alternar Delta](Part_Measure_Toggle_Delta/es.md): Muestra u oculta las medidas delta.


</div>



## Preferencias


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferencias](PartDesign_Preferences/es.md): Preferencias disponibles para las Herramientas de Pieza (el ambiente de trabajo de Pieza también utiliza las Preferencias de PartDesign).
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferencias de importación-exportación](Import_Export_Preferences/es.md): Preferencias disponibles para importar desde y exportar a diferentes formatos de archivo.
-   [Ajuste fino](Fine-tuning/es.md): Algunos parámetros extra para afinar el comportamiento de la Parte.


</div>



## Guión

Ver [Guiones Pieza](Part_scripting/es.md).



## Tutoriales

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md) : How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md) : How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md) : How to use the Part Workbench


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/es
