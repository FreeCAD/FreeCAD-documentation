# BIM Workbench/es
}

<img alt="El icono del Ambiente de trabajo BIM" src=images/IFC.svg  style="width   *128px;">


{{TOCright}}

## Introducción

El <img alt="" src=images/Workbench_BIM.svg  style="width   *24px;"> [Ambiente de trabajo BIM](BIM_Workbench/es.md) es un [Ambiente de trabajo externo](External_workbenches/es.md) destinado a implementar herramientas completas de [Building Information Modeling](https   *//en.wikipedia.org/wiki/Building_information_modeling) (BIM) y flujo de trabajo en FreeCAD. Se puede instalar desde el <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr/es.md).


<div class="mw-translate-fuzzy">

El ambiente de trabajo BIM

se basa en el <img alt="" src=images/Workbench_Arch.svg  style="width   *24px;"> incorporado [Ambiente de trabajo Arch](Arch_Workbench/es.md), y probablemente ambos se fusionarán en el futuro. El ambiente de trabajo BIM es un \"metabanco\", que pretende reunir muchas herramientas útiles de otros ambiente de trabajo en un único lugar, y crear un flujo de trabajo más cómodo y fácil de usar tanto para los usuarios experimentados de BIM como para los principiantes. El ambiente de trabajo BIM también cuenta con algunas herramientas específicas propias, sobre todo asistentes y herramientas de gestión, situadas en el menú **Gestión**.


</div>

Véase [Guía de migración a FreeCAD BIM](https   *//yorik.uncreated.net/blog/2020-010-freecad-bim-guide) para una rápida visión general si ya eres usuario de otra aplicación BIM.

Los desarrolladores de Draft, Arch y BIM también colaboran con la gran [OSArch community](https   *//osarch.org), con el objetivo final de mejorar el diseño de los edificios mediante el uso de software totalmente libre.

<img alt="" src=images/BIM_workbench_presentation.png  style="width   *800px;">

## Instalación

El ambiente de trabajo BIM no está incluido en el paquete predeterminado de FreeCAD, pero puede ser instalado fácilmente a través de la <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr/es.md). Invóquelo desde **Herramientas → [Addons Manager](Std_AddonMgr/es.md)**. El código del ambiente de trabajo BIM es [alojado y desarrollado en github](https   *//github.com/yorikvanhavre/BIM_Workbench) y también puede ser instalado manualmente copiándolo en el directorio **MOD** de FreeCAD.

**Nota**

El ambiente de trabajo BIM es un trabajo en progreso, y cambiará a menudo. ¡Asegúrese de actualizarlo regularmente! Si tiene instalado el módulo [Python-Git](https   *//github.com/chidimo/python-git), el ambiente de trabajo de BIM buscará automáticamente las actualizaciones disponibles al inicio, y mostrará un icono en la barra de estado si hay una actualización disponible.

Las herramientas que se enumeran a continuación pueden no estar todas presentes si su versión de FreeCAD no está totalmente actualizada. Sin embargo, el ambiente de trabajo BIM debería funcionar sin problemas en todas las versiones de FreeCAD, sólo eliminará las herramientas no disponibles.

## Cómo empezar 

<img alt="" src=images/BIM_welcome_screen.png  style="width   *800px;">

Al iniciar el ambiente de trabajo BIM por primera vez, se muestra un cuadro de diálogo de bienvenida que ofrece una rápida visión general de cómo funciona el banco de trabajo y permite al usuario iniciar un [tutorial dentro del juego](BIM_ingame_tutorial/es.md). El diálogo de bienvenida también está disponible en el menú **ayuda**. Cuando la pantalla de bienvenida se cierra haciendo clic en OK, se mostrará el diálogo [Configuración BIM](BIM_Setup/es.md), que permite al usuario configurar rápidamente algunas de las preferencias más comunes de FreeCAD relacionadas con BIM sin necesidad de navegar por las páginas completas de preferencias de FreeCAD.

La herramienta [Configuración del proyecto BIM](BIM_Project/es.md) le permite configurar rápidamente un proyecto BIM rellenando algunos datos básicos sobre su proyecto. A continuación, puede utilizar, por ejemplo, las diferentes herramientas de dibujo 2D para trazar directrices y líneas de base, y luego utilizar las diferentes herramientas de modelado 3D para construir automáticamente objetos BIM 3D a partir de ellos. Una línea, por ejemplo, puede convertirse en un muro simplemente seleccionándola y pulsando el botón [Muro](Arch_Wall/es.md).

Si estás acostumbrado a otra aplicación BIM, consulta nuestra [Tabla de compatibilidad de aplicaciones BIM](BIM_application_compatibility_table/es.md) para obtener tus notas al empezar con FreeCAD.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width   *800px;">

The [in-game tutorial](BIM_ingame_tutorial.md) is an easy way to quickly get on track with the BIM workbench.

## Herramientas

El ambiente de trabajo BIM reúne herramientas de otros ambientes de trabajo de FreeCAD, principalmente [Borrador](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md) y [Pieza](Part_Workbench/es.md), reorganizados a grandes rasgos en categorías lógicas   * **dibujo 2D**, **modelado 3D**, **anotación** y **modificación**. La categoría **gestión** contiene herramientas específicas del ambiente de trabajo BIM.


<div class="mw-translate-fuzzy">

Además, si se instalan estos [addons](External_workbenches/es.md), las herramientas de [Refuerzo](Arch_Rebar/es.md) (herramientas para barras de refuerzo adicionales), [Fijadores](Fasteners_Workbench/es.md) (pernos y tornillos), [Flamingo/Dodo](Flamingo_Workbench/es.md) (herramientas de estructura metálica y tuberías) y [Biblioteca de piezas](Parts_Library_Workbench/es.md) se incluyen automáticamente en el ambiente de trabajo BIM.


</div>

El ambiente de trabajo BIM también añade una serie de elementos en la **barra de estado** de FreeCAD, y un par de elementos del **menú contextual**\', accesibles haciendo clic con el botón derecho en la vista 3D o en la vista de árbol.

### 2D Elaboración 

Los objetos 2D se utilizan habitualmente como ayudas al dibujo, o para dibujar líneas y perfiles base sobre los que construir objetos BIM. También pueden utilizarse para dibujar símbolos y anotaciones en el modelo. Aparte de los bocetos, que utilizan su propio sistema de coordenadas, los objetos 2D se dibujarán en el [plano de trabajo](Draft_SelectPlane/es.md) actual.

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> [Boceto](Sketcher_NewSketch/es.md)   * Crea un nuevo boceto y entra en el modo de dibujo de bocetos. Los bocetos son objetos 2D avanzados con soporte de restricciones
-   <img alt="" src=images/Draft_Line.svg  style="width   *32px;"> [Línea](Draft_Line/es.md)   * Dibuja un segmento de línea entre 2 puntos
-   <img alt="" src=images/Draft_Wire.svg  style="width   *32px;"> [Alambre](Draft_Wire/es.md)   * Dibuja una línea hecha de múltiples segmentos de línea (polilínea)
-   <img alt="" src=images/Draft_Circle.svg  style="width   *32px;"> [Círculo](Draft_Circle/es.md)   * Dibuja un círculo de centro y radio
-   <img alt="" src=images/Draft_Arc.svg  style="width   *32px;"> [Arco](Draft_Arc/es.md)   * Dibuja un segmento de arco a partir del centro, radio, ángulo inicial y ángulo final
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width   *32px;"> [Arco 3Puntos](Draft_Arc_3Points/es.md)   * dibuja un segmento de arco circular a partir de tres puntos que se encuentran en la circunferencia
-   <img alt="" src=images/Draft_Ellipse.svg  style="width   *32px;"> [Elipse](Draft_Ellipse/es.md)   * Dibuja una elipse a partir de dos puntos de esquina
-   <img alt="" src=images/Draft_Polygon.svg  style="width   *32px;"> [Polígono](Draft_Polygon/es.md)   * Dibuja un polígono regular a partir de un centro y un radio
-   <img alt="" src=images/Draft_Rectangle.svg  style="width   *32px;"> [Rectángulo](Draft_Rectangle/es.md)   * Dibuja un rectángulo a partir de 2 puntos opuestos
-   <img alt="" src=images/Draft_BSpline.svg  style="width   *32px;"> [BSpline](Draft_BSpline/es.md)   * Dibuja una B-Spline a partir de una serie de puntos
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width   *32px;"> [Curva cúbica de Bezier](Draft_CubicBezCurve/es.md)   * dibuja una curva de Bezier de tercer grado arrastrando dos puntos.
-   <img alt="" src=images/Draft_BezCurve.svg  style="width   *32px;"> [Curva de Bézier](Draft_BezCurve/es.md)   * Dibuja una curva de Bézier a partir de una serie de puntos
-   <img alt="" src=images/Draft_Point.svg  style="width   *32px;"> [Punto](Draft_Point/es.md)   * Inserta un objeto de punto

### Anotación

Anotaciones son objetos de ayuda visual que se pueden colocar dentro de su modelo. Pueden utilizarse para exportar su modelo directamente a un formato 2D como [DXF](Draft_DXF/es.md), o reutilizarse al crear vistas 2D de su modelo con el [TechDraw ambiente de trabajo](TechDraw_Workbench/es.md).


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_Text.svg  style="width   *32px;"> [Texto](Draft_Text/es.md)   * Dibuja una anotación de texto de varias líneas
-   <img alt="" src=images/Draft_ShapeString.svg  style="width   *32px;"> [CadenaForma](Draft_ShapeString/es.md)   * Dibuja una línea de texto como geometría
-   <img alt="" src=images/Draft_Dimension.svg  style="width   *32px;"> [Dimensión](Draft_Dimension/es.md)   * Dibuja una dimensión lineal, angular, radial o de diámetro
-   <img alt="" src=images/Draft_Label.svg  style="width   *32px;"> [Etiqueta](Draft_Label/es.md)   * Coloca una etiqueta con una flecha que apunta a un elemento seleccionado
-   <img alt="" src=images/Arch_Axis.svg  style="width   *32px;"> [Eje](Arch_Axis/es.md)   * Crea un único eje o una matriz de ejes de 1 dirección al documento
-   <img alt="" src=images/Arch_Axis_System.svg  style="width   *32px;"> [Sistema de ejes](Arch_AxisSystem/es.md)   * Crea un sistema de ejes compuesto por hasta 3 series de ejes
-   <img alt="" src=images/Arch_Grid.svg  style="width   *32px;"> [Rejilla](Arch_Grid/es.md)   * Crea un objeto similar a una cuadrícula en el documento
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width   *32px;"> [Plano de sección](Arch_SectionPlane/es.md)   * Añade un objeto de plano de sección al documento. Los planos de sección definen vistas en 2D como planos, secciones y alzados
-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width   *32px;"> [Página](TechDraw_PageDefault/es.md)   * Crea una nueva página [TechDraw](TechDraw_Workbench/es.md) a partir de una plantilla [SVG](TechDraw_Templates/es.md) new [TechDraw](TechDraw_Workbench.md) page from a [SVG plantilla](TechDraw_Templates/es.md)
-   <img alt="" src=images/TechDraw_ArchView.svg  style="width   *32px;"> [Vista](TechDraw_ArchView/es.md)   * Inserta una vista de un plano de sección en una página


</div>

### 3D / BIM Modelado 

Los objetos 3D y BIM son los elementos del mundo real que compondrán tu proyecto BIM.

**Estructura del edificio**   * Estas herramientas te ayudan a organizar tu modelo

-   <img alt="" src=images/Arch_Project.svg  style="width   *32px;"> [Proyecto](Arch_Project/es.md)   * Crea un proyecto que incluye los objetos seleccionados
-   <img alt="" src=images/Arch_Site.svg  style="width   *32px;"> [Ubicación](Arch_Site/es.md)   * Crea un ubicación incluyendo los objetos seleccionados
-   <img alt="" src=images/Arch_Building.svg  style="width   *32px;"> [Edificio](Arch_Building/es.md)   * Crea un edificio incluyendo los objetos seleccionados
-   <img alt="" src=images/Arch_BuildingPart.png  style="width   *32px;"> [Nivel](Arch_BuildingPart/es.md) (Parte de edificio)   * Crea una parte de edificio incluyendo los objetos seleccionados. Las partes de edificios se usan comúnmente para representar niveles
-   <img alt="" src=images/Arch_Space.svg  style="width   *32px;"> [Espacio](Arch_Space/es.md)   * Crea un objeto espacial en el documento
-   <img alt="" src=images/Arch_Reference.svg  style="width   *32px;"> [Referencia](Arch_Reference/es.md)   * Enlaza objetos de otro archivo de FreeCAD en este documento

**Herramientas BIM**   * Estas herramientas construyen componentes BIM

-   <img alt="" src=images/Arch_Wall.svg  style="width   *32px;"> [Wall](Arch_Wall.md)   * Creates a wall from scratch or using a selected object as a base
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width   *32px;"> [Curtain Wall](Arch_CurtainWall.md)   * creates a curtain wall from scratch or using a selected object as a base
-   <img alt="" src=images/BIM_Column.svg  style="width   *32px;"> [Column](Arch_Structure.md)   * Creates a vertical [structural](Arch_Structure.md) element at a given point, optionally using a selected object as a profile
-   <img alt="" src=images/BIM_Beam.svg  style="width   *32px;"> [Beam](Arch_Structure.md)   * Creates a horizontal [structural](Arch_Structure.md) element between two points, optionally using a selected object as a profile
-   <img alt="" src=images/BIM_Slab.svg  style="width   *32px;"> [Slab](Arch_Structure.md)   * Creates a flat [structural](Arch_Structure.md) element by extruding a selected flat object
-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width   *32px;"> <img alt="" src=images/Arch_Rebar_UShape.png  style="width   *32px;"> <img alt="" src=images/Arch_Rebar_LShape.png  style="width   *32px;"> <img alt="" src=images/Arch_Rebar_BentShape.png  style="width   *32px;"> <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width   *32px;"> <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width   *32px;"> <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width   *32px;"> <img alt="" src=images/Arch_Rebar_Helical.png  style="width   *32px;"> <img alt="" src=images/Arch_Rebar.svg  style="width   *32px;"> [Rebar](Arch_Rebar.md)   * Creates a reinforcement bar in a selected structural element using a sketch. Requires the [Reinforcement](Reinforcement_Addon.md) addon
-   <img alt="" src=images/Arch_Window.svg  style="width   *32px;"> [Window](Arch_Window.md)   * Creates a window using a selected object as a base
-   <img alt="" src=images/BIM_Door.svg  style="width   *32px;"> [Door](Arch_Window.md)   * Creates a [Window](Arch_Window.md) object using door presets
-   <img alt="" src=images/Arch_Pipe.svg  style="width   *32px;"> <img alt="" src=images/Arch_PipeConnector.svg  style="width   *32px;"> [Pipe tools](Arch_Pipe.md)   * Creates pipes and corner or tee connection between 2 or 3 selected pipes
-   <img alt="" src=images/Arch_Stairs.svg  style="width   *32px;"> [Stairs](Arch_Stairs.md)   * Creates a stairs object in the document
-   <img alt="" src=images/Arch_Roof.svg  style="width   *32px;"> [Roof](Arch_Roof.md)   * Creates a sloped roof from a selected face
-   <img alt="" src=images/Arch_Panel.svg  style="width   *32px;"> <img alt="" src=images/Arch_Panel_Cut.svg  style="width   *32px;"> <img alt="" src=images/Arch_Panel_Sheet.svg  style="width   *32px;"> [Panel tools](Arch_Panel.md)   * Creates panel objects, and 2D cutouts from these panels
-   <img alt="" src=images/Arch_Frame.svg  style="width   *32px;"> [Frame](Arch_Frame.md)   * Creates a frame object from a selected layout
-   <img alt="" src=images/Arch_Fence.svg  style="width   *32px;"> [Fence](Arch_Fence.md)   * Creates a fence object from a selected post object and path
-   <img alt="" src=images/Arch_Truss.svg  style="width   *32px;"> [Truss](Arch_Truss.md)   * Creates a truss from a selected line of from scratch
-   <img alt="" src=images/BIM_Library.png  style="width   *32px;"> [Library](BIM_Library.md)   * Inserts an equipment or furniture object. Requires the [Parts Library](Parts_Library.md) addon
-   <img alt="" src=images/Arch_Component.png  style="width   *32px;"> [BIM Component](Arch_Component.md)   * Turns any selected object into a BIM object, with complete IFC support

**Herramientas 3D genéricas**   * Estas herramientas construyen objetos 3D genéricos que pueden convertirse o utilizarse en componentes BIM

-   <img alt="" src=images/Arch_Profile.svg  style="width   *32px;"> [Perfil](Arch_Profile/es.md)   * Crea un perfil 2D paramétrico para ser utilizado, por ejemplo, en extrusiones
-   <img alt="" src=images/BIM_Box.png  style="width   *32px;"> [Caja](BIM_Box/es.md)   * Dibuja una caja especificando sus dimensiones gráficamente
-   <img alt="" src=images/Part_Builder.svg  style="width   *32px;"> [Constructor formas](Part_Builder/es.md)   * Una herramienta para crear formas más complejas a partir de varias primitivas geométricas paramétricas
-   <img alt="" src=images/Draft_Facebinder.svg  style="width   *32px;"> [Facebinder](Draft_Facebinder/es.md)   * Crea un nuevo objeto a partir de caras seleccionadas en objetos existentes

### Herramientas de modificación 

-   <img alt="" src=images/Draft_Move.svg  style="width   *32px;"> [Move](Draft_Move.md)   * Moves object(s) from one location to another
-   <img alt="" src=images/BIM_Copy.png  style="width   *32px;"> [Copy](BIM_Copy.md)   * Copies object(s) from one location to another
-   <img alt="" src=images/Draft_Rotate.svg  style="width   *32px;"> [Rotate](Draft_Rotate.md)   * Rotates object(s) from a start angle to an end angle
-   <img alt="" src=images/Draft_Clone.svg  style="width   *32px;"> [Clone](BIM_Clone.md)   * Clones the selected objects
-   <img alt="" src=images/Draft_Offset.svg  style="width   *32px;"> [Offset](Draft_Offset.md)   * Moves segments of an object about a certain distance
-   <img alt="" src=images/Part_Offset2D.svg  style="width   *32px;"> [2D Offset](Part_Offset2D.md)   * Constructs a parallel wire at certain distance from original, or enlarges/shrinks a planar face ((parametric version)
-   <img alt="" src=images/Draft_Trimex.svg  style="width   *32px;"> [Trim/Extend (Trimex)](Draft_Trimex.md)   * Trims or extends an object
-   <img alt="" src=images/Draft_Scale.svg  style="width   *32px;"> [Scale](Draft_Scale.md)   * Scales selected object(s) around a base point
-   <img alt="" src=images/Draft_Stretch.svg  style="width   *32px;"> [Stretch](Draft_Stretch.md)   * Stretches the selected objects
-   <img alt="" src=images/Draft_Array.svg  style="width   *32px;"> [Array](Draft_Array.md)   * Creates a polar or rectangular array from selected objects
-   <img alt="" src=images/Draft_PathArray.svg  style="width   *32px;"> [Path Array](Draft_PathArray.md)   * Creates an array of objects by placing the copies along a path
-   <img alt="" src=images/Draft_Mirror.svg  style="width   *32px;"> [Mirror](Draft_Mirror.md)   * Mirrors the selected objects
-   <img alt="" src=images/Part_Extrude.svg  style="width   *32px;"> [Extrude](Part_Extrude.md)   * Extrudes planar faces of an object
-   <img alt="" src=images/Part_Cut.svg  style="width   *32px;"> [Cut](Part_Cut.md)   * Cuts (subtracts) one object from another
-   <img alt="" src=images/Part_Fuse.svg  style="width   *32px;"> [Union](Part_Fuse.md)   * Fuses (unions) two objects
-   <img alt="" src=images/Part_Common.svg  style="width   *32px;"> [Common](Part_Common.md)   * Extracts the common (intersection) part of two objects
-   <img alt="" src=images/Part_Compound.svg  style="width   *32px;"> [Compound](Part_Compound.md)   * Creates a compound from the selected objects
-   <img alt="" src=images/Part_SimpleCopy.svg  style="width   *32px;"> [Simple copy](Part_SimpleCopy.md)   * Creates a non-parametric copy of a selected object
-   <img alt="" src=images/Draft_Upgrade.svg  style="width   *32px;"> [Upgrade](Draft_Upgrade.md)   * Joins objects into a higher-level object
-   <img alt="" src=images/Draft_Downgrade.svg  style="width   *32px;"> [Downgrade](Draft_Downgrade.md)   * Explodes objects into lower-level objects
-   <img alt="" src=images/Draft_Shape2DView.svg  style="width   *32px;"> [Shape 2D View](Draft_Shape2DView.md)   * Creates a 2D object which is a flattened 2D view of another 3D object
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width   *32px;"> [Draft to Sketch](Draft_Draft2Sketch.md)   * Converts a Draft object to Sketch and vice-versa
-   <img alt="" src=images/Arch_CutPlane.svg  style="width   *32px;"> [Cut with plane](Arch_CutPlane.md)   * Cut an object according to a plan.
-   <img alt="" src=images/Arch_Add.svg  style="width   *32px;"> [Add component](Arch_Add.md)   * Adds objects to a component
-   <img alt="" src=images/Arch_Remove.svg  style="width   *32px;"> [Remove component](Arch_Remove.md)   * Subtracts or removes objects from a component

### Herramientas de gestión 

-   <img alt="" src=images/BIM_Setup.png  style="width   *32px;"> [BIM setup](BIM_Setup.md)   * Configures some of the FreeCAD preferences most commonly used for BIM
-   <img alt="" src=images/BIM_Project.png  style="width   *32px;"> [Project setup](BIM_Project.md)   * Allows to create some basic objects such as a [site](Arch_Site.md), a [building](Arch_Building.md) and [axes](Arch_Axis.md) by filling basic project information.
-   <img alt="" src=images/BIM_Views.png  style="width   *32px;"> [Views and levels manager](BIM_Views.md)   * Manage the different views and levels of your project
-   <img alt="" src=images/BIM_Windows.png  style="width   *32px;"> [Windows manager](BIM_Windows.md)   * Manage the doors and windows of your project
-   <img alt="" src=images/BIM_IfcElements.png  style="width   *32px;"> [IFC elements manager](BIM_IfcElements.md)   * Manage how the different elements of your project will be exported to IFC
-   <img alt="" src=images/BIM_IfcProperties.svg  style="width   *32px;"> [IFC properties manager](BIM_IfcProperties.md)   * Manage the IFC properties attached to each of your objects
-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width   *32px;"> [IFC quantities manager](BIM_IfcQuantities.md)   * Manage how the quantities of your objects are explicitely exported to IFC
-   <img alt="" src=images/BIM_Classification.png  style="width   *32px;"> [Classification manager](BIM_Classification.md)   * Manage how objects and materials of your project relate to classifications systems such as [Uniclass](https   *//en.wikipedia.org/wiki/Uniclass)
-   <img alt="" src=images/Draft_VisGroup.svg  style="width   *32px;"> [Layers manager](BIM_Layers.md)   * Manage the layers of your document
-   <img alt="" src=images/Arch_Material_Group.svg  style="width   *32px;"> [Material](Arch_SetMaterial.md)   * Manages materials or [multimaterials](Arch_MultiMaterial.md) of selected objects
-   <img alt="" src=images/Arch_Schedule.svg  style="width   *32px;"> [Schedule](Arch_Schedule.md)   * Creates different types of schedules
-   <img alt="" src=images/BIM_Preflight.svg  style="width   *32px;"> [Preflight checks](BIM_Preflight.md)   * Perform different checks on your model before exporting to IFC
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width   *32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md)   * Manages annotation styles used by texts and dimensions

## Tutoriales y aprendizaje 


<div class="mw-translate-fuzzy">

-   [Arch & BIM tutoriales en esta wiki](Tutorials#Architecture_and_BIM.md)
-   [\"BIM con FreeCAD\" serie de vídeos de Yorik](https   *//www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutoriales\" serie de vídeos de Regis](https   *//www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" serie de vídeos de Regis](https   *//www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)


</div>

## Ambiente de trabajo externos 

Ambientes de trabajo de FreeCAD son fáciles de programar en [Python](Python/es.md), por lo que hay mucha gente desarrollando ambientes de trabajo adicionales fuera de los desarrolladores principales de FreeCAD.

La página [Ambientes de trabajo externos](External_workbenches/es.md) tiene información y tutoriales sobre algunos de ellos, y el proyecto [FreeCAD Addons](https   *//github.com/FreeCAD/FreeCAD-addons) pretende reunirlos y hacerlos fácilmente instalables desde FreeCAD.

Nuevos ambientes de trabajo están en desarrollo, esté atento!




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md) [Category   *BIM](Category_BIM.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [BIM](Category_BIM.md) > BIM Workbench/es
