# Part Module/es
<div class="mw-translate-fuzzy">





</div>

<img alt="El icono del Ambiente de trabajo Pieza" src=images/Workbench_Part.svg  style="width:128px;">


{{TOCright}}

## Introducción

Las sólidas capacidades de modelado de FreeCAD se basan en la [OpenCASCADE](OpenCASCADE/es.md) (OCCT), un sistema CAD de calidad profesional que presenta una creación y manipulación avanzada de geometría 3D. El <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo pieza](Part_Workbench/es.md) es una capa que se encuentra en la parte superior de las bibliotecas de la OCCT, que da al usuario acceso a las primitivas y funciones geométricas de la OCCT. Esencialmente todas las funciones de dibujo 2D y 3D en cada ambiente de trabajo (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Borrador](Draft_Workbench/es.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Croquizador](Sketcher_Workbench/es.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [DiseñoPieza](PartDesign_Workbench/es.md), etc.), se basan en estas funciones expuestas por el ambiente de trabajo DiseñoPieza. Por lo tanto, el Ambiente de trabajo DiseñoPieza se considera el componente central de las capacidades de modelado de FreeCAD.

Una discusión más detallada sobre el ambiente de trabajo Pieza frente al ambiente de trabajo de DiseñoPieza se puede encontrar aquí: [Pieza y DiseñoPieza](Part_and_Part_Design/es.md).

Los objetos creados con el ambiente de trabajo de pieza son relativamente sencillos; están pensados para ser utilizados con operaciones booleanas (uniones y cortes) para construir formas más complejas. **Este paradigma de modelado se conoce como la [geometría sólida constructiva](constructive_solid_geometry/es.md) (CSG), y era la metodología tradicional usada en los primeros sistemas de CAD.** Por otro lado, el [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md) proporciona un flujo de trabajo más moderno para construir formas: utiliza un boceto definido paramétricamente, que se extruye para formar un cuerpo sólido básico, que luego se modifica mediante transformaciones paramétricas ([edición características](feature_editing/es.md)), hasta obtener el objeto final.

Los objetos de las partes son más complejos que los objetos de malla creados con el [Ambiente de trabajo Malla](Mesh_Workbench/es.md), ya que permiten operaciones más avanzadas como operaciones booleanas coherentes, historial de modificaciones y comportamiento paramétrico.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">


*El ambiente de trabajo de pieza es la capa básica que expone las funciones de dibujo de la OCCT a todos los ambientes de trabajo de FreeCAD.*

## Herramientas

Las herramientas se encuentran en el menú **Pieza** o en el menú **Medida**.

### Primitivas

Estas son las herramientas para crear primitivas de objetos.

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Caja](Part_Box/es.md): Crea una caja.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/es.md): Crea un cilindro.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Esfera](Part_Sphere/es.md): Crea una esfera.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cono](Part_Cone/es.md): Crea un cono.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus/es.md): Crea un toro (anillo).

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tubo](Part_Tube/es.md): Crea un tubo. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Primitivas](Part_Primitives/es.md): Una herramienta para crear una de las siguientes primitivas:
    -   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plano](Part_Plane/es.md): Crea un plano.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Caja](Parte_Caja/es.md): Crea una caja. Este objeto también puede ser creado con el <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Caja](Part_Box/es.md).
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Cilindro](Part_Cylinder/es.md): Crea un cilindro. Este objeto también puede ser creado con el <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/es.md).
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Cono](Part_Cone/es.md): Crea un cono. Este objeto también se puede crear con el <img alt="" src=images/Part_Cone.svg  style="width:32px;"> Herramienta [Cono](Part_Cone/es.md).
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Esfera](Part_Sphere/es.md): Crea una esfera. Este objeto también puede ser creado con el <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Esfera](Parte_esfera/es.md).
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoide](Part_Ellipsoid/es.md): Crea un elipsoide.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [\|Toro](Part_Torus/es.md): Crea un toroide. Este objeto también puede ser creado con el <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus/es.md).
    -   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/es.md): Crea un prisma.
    -   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Cuña](Part_Wedge/es.md): Crea una cuña.
    -   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Hélice](Part_Helix/es.md): Crea una hélice.
    -   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Espiral](Part_Spiral/es.md): Crea una espiral.
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Círculo](Part_Circle/es.md): Crea un borde circular.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/es.md): Crea un borde elíptico.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punto](Part_Point/es.md): Crea un punto (vértice).
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Línea](Part_Line/es.md): Crea una línea (arista).
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [PolígonoRegular](Part_RegularPolygon/es.md): Crea un polígono regular.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Creador](Part_Builder/es.md): Crea formas a partir de varias primitivas.

### Creación y modificación 

Estas son herramientas para crear nuevos objetos y modificar los existentes.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrusión](Part_Extrude/es.md): Extruye caras planas.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolución](Part_Revolve/es.md): Crea un sólido girando un objeto (no un sólido) alrededor de un eje.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Espejo](Part_Mirror/es.md): Refleja el objeto seleccionado a través de un plano de espejo.

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Redondear](Part_Fillet/es.md): Redondea las aristas de un objeto.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chaflán](Part_Chamfer/es.md): Crea un chaflán en las aristas de un objeto.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Hacer cara a partir de alambres](Part_MakeFace/es.md): Hace una cara a partir de un conjunto de hilos (contornos).{{Version/es|0.19}}

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Superficie reglada](Part_RuledSurface/es.md): Crea una superficie reglada.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft/es.md): Lofts de un perfil a otro.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Barrido](Part_Sweep/es.md): Barre uno o más perfiles a lo largo de un camino.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Sección](Part_Section/es.md): Crea una sección por la intersección de un objeto con un plano de sección.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Secciones transversales\...](Part_CrossSections/es.md): Crea una o más secciones transversales a través de un objeto.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Herramientas relleno](Part_CompOffsetTools/es.md):
    -   <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Relleno](Part_Offset/es.md): Construye una forma paralela a cierta distancia de un original.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Relleno](Part_Offset2D/es.md): Construye un cable paralelo a cierta distancia de un original, o amplía/contrae una cara plana.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Espesor](Part_Thickness/es.md): Ahueca un sólido.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Proyección sobre superficie](Part_ProjectionOnSurface/es.md): Proyecta un logo, texto o cualquier cara, cable, borde a una superficie. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Attachment.svg  style="width:32px;"> [Adjuntar](Part_Attachment/es.md): Adjunta un objeto a otro objeto.


</div>

### Booleano

Estas herramientas realizan operaciones booleanas.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width:48px;"> [Herramientas compuestas](Part_CompCompoundTools/es.md):
    -   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Hacer compuesto](Part_Compound/es.md): Crea un compuesto a partir de los objetos seleccionados.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explotar compuesto](Part_ExplodeCompound/es.md): Divide los compuestos.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Filtro compuesto](Part_Compound‏‎Filter/es.md): Extrae las partes individuales de los compuestos.

-   <img alt="" src=images/Part_Booleans.svg  style="width:32px;"> [Operaciones Booleanas](Part_Boolean/es.md): Realiza operaciones booleanas sobre objetos.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cortar](Part_Cut/es.md): Corta (resta) un objeto de otro.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Fusión](Part_Fuse/es.md): Fusión (unión) de dos objetos.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Común](Part_Common/es.md): Extrae la parte común (intersección) de dos objetos.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Características de unión](Part_CompJoinFeatures/es.md):
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Conectar](Part_JoinConnect/es.md): Conecta los interiores de los objetos huecos.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Incrustar](Part_JoinEmbed/es.md): Incrusta un objeto hueco en otro objeto hueco.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Recorte](Part_JoinCutout/es.md): Crea un recorte en una pared de un objeto para otro objeto hueco.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Herramientas de división](Part_CompSplittingTools/es.md):
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Fragmentos booleanos](Part_BooleanFragments/es.md): Crea todas las piezas obtenidas de las operaciones booleanas.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Recorta una pieza](Part_SliceApart/es.md): Rebana y divide un objeto intersectándolo con otros objetos.
    -   <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Corte](Part_Slice/es.md): Corta un objeto intersectándolo con otros objetos.
    -   <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [XOR](Part_XOR/es.md): Elimina el espacio compartido por un número par de objetos (versión simétrica de [Cortar](Part_Cut/es.md)).

### Medida

<img alt="" src=images/Part_Measure_Menu.png  style="width:64px;"> [Medir](Part_Measure_Menu/es.md): Herramientas para mediciones lineales y angulares.

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Medida Lineal](Part_Measure_Linear/es.md): Crea una medida lineal.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Medida Angular](Part_Measure_Angular/es.md): Crea una medida angular.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Actualización de medidas](Part_Measure_Refresh/es.md): Actualiza todas las mediciones.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Borrar todo](Part_Measure_Clear_All/es.md): Borra todas las mediciones.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Alternar todo](Part_Measure_Toggle_All/es.md): Muestra u oculta todas las mediciones.

-   <img alt="" src=images/Part_Measure_Toggle_3d.svg  style="width:32px;"> [Alternar 3D](Part_Measure_Toggle_3d/es.md): Muestra u oculta las medidas 3D.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Alternar Delta](Part_Measure_Toggle_Delta/es.md): Muestra u oculta las medidas delta.

### Otras herramientas 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Importar](Part_Import/es.md): Importa desde archivos \*.IGES, \*.STEP o \*.BREP.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Exportar](Part_Export/es.md): Exporta a archivos \*.IGES, \*.STEP o \*.BREP.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [CajaSelección](Part_BoxSelection/es.md): Selecciona las caras de un área rectangular.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Forma a partir malla](Part_ShapeFromMesh/es.md): Crea un objeto de forma a partir de un objeto de malla.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Puntos desde malla](Part_PointsFromMesh/es.md): Crea un objeto de forma hecho de puntos a partir de un objeto de malla. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convertir en sólido](Part_MakeSolid/es.md): Convierte un objeto de forma en un objeto sólido.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width:32px;"> [Invertir formas](Part_ReverseShapes/es.md): Invierte las normales de todas las caras de los objetos seleccionados.

-   Crear una copia:
    -   <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Crear copia simple](Part_SimpleCopy/es.md): Crea una copia simple de un objeto seleccionado.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Crear copia transformada](Part_TransformedCopy/es.md): Crea una copia transformada de un objeto seleccionado. {{Versión|0.19}}
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Crear copia de elemento de forma](Part_ElementCopy/es.md): Crea una copia de un elemento (vértice, arista, cara) de un objeto seleccionado. {{Versión|0.19}}
    -   <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refinar forma](Part_RefineShape/es.md): Limpia las caras eliminando las líneas innecesarias.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Comprobar geometría](Part_CheckGeometry/es.md): Comprueba la geometría de los objetos seleccionados en busca de errores.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Derrotar](Part_Defeaturing/es.md): Elimina las características de un objeto.

### Elementos del menú contextual 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Apariencia](Std_SetAppearance/es.md): Determina la apariencia de un objeto completo (color, transparencia, etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;">

[Establecer colores](Part_FaceColors/es.md): Asigna colores a las caras individuales de los objetos.

## Preferencias

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferencias](PartDesign_Preferences/es.md): Preferencias disponibles para las Herramientas de Pieza (el ambiente de trabajo de Pieza también utiliza las Preferencias de PartDesign).
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferencias de importación-exportación](Import_Export_Preferences/es.md): Preferencias disponibles para importar desde y exportar a diferentes formatos de archivo.
-   [Ajuste fino](Fine-tuning/es.md): Algunos parámetros extra para afinar el comportamiento de la Parte.

## Guión

Ver [Guiones Pieza](Part_scripting/es.md).

## Tutoriales

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md) : How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md) : How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md) : How to use the Part Module


<div class="mw-translate-fuzzy">





</div>


 

[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Module/es
