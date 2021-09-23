# Arch Workbench/es





<img alt="El icono del Ambiente de trabajo Arquitectura" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

## Introducción

El <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Ambiente de trabajo Arquitectura](Arch_Workbench/es.md) proporciona un moderno entorno de trabajo [BIM](http://es.wikipedia.org/wiki/Modelado_de_informaci%C3%B3n_de_construcci%C3%B3n) para FreeCAD, con soporte para características como entidades arquitectónicas totalmente paramétricas como paredes, vigas, techos, ventanas, escaleras, tuberías y muebles. Soporta clases de cimientos de la industria ([IFC](Arch_IFC/es.md)) archivos, y la producción de planos de planta en 2D en combinación con el <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Ambiente de trabajo TechDraw](TechDraw_Workbench/es.md).

El Ambiente de trabajo Arquitectura importa todas las herramientas del <img alt="" src=images/Workbench_Draft.svg  style="width:24px;">[Ambiente de Trabajo borrador](Draft_Workbench/es.md), ya que utiliza sus objetos 2D para construir objetos arquitectónicos paramétricos 3D. Sin embargo, Arquitectura también puede usar formas sólidas creadas con otros Ambientes de trabajo como <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Pieza](Part_Workbench/es.md) y <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [DiseñoPiezas](PartDesign_Workbench/es.md).

La funcionalidad BIM de FreeCAD ahora se divide progresivamente entre este ambiente de trabajo Arch, que contiene herramientas arquitectónicas básicas, y el <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [Ambiente de Trabajo BIM](BIM_Workbench/es.md), que está disponible en el <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestor de complementos](Std_AddonMgr/es.md). Este BIM Workbench añade una nueva capa de interfaz sobre las herramientas de Arquitectura, con el objetivo de hacer el flujo de trabajo de BIM más intuitivo y fácil de usar. Ver [Guía de migración del BIM de FreeCAD](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Los desarrolladores de Borrador, Arquitectura y BIM también colaboran con la gran [comunidad OSArch](https://osarch.org), con el objetivo final de mejorar el diseño de los edificios mediante el uso de software totalmente libre.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Herramientas

Estas son herramientas para crear objetos arquitectónicos.

-   <img alt="" src=images/Arch_Wall.png  style="width:32px;"> [Muro](Arch_Wall/es.md): Crea un muro utilizando un objeto seleccionado como base
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Muro Cortina](Arch_CurtainWall/es.md): crea un muro cortina desde cero o usando un objeto seleccionado como base. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Structure.png  style="width:32px;"> [Elemento estructural](Arch_Structure/es.md): Crea un elemento estructural utilizando un objeto seleccionado como base

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Herramientas barra de refuerzo](Arch_CompRebarStraight/es.md): el complemento de refuerzo aumenta las estructuras del ambiente de trabajo en Arch.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Barra de refuerzo recta](Arch_Rebar_Straight/es.md): Crea una barra de refuerzo recta en un elemento estructural seleccionado
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [Barra de refuerzo forma U](Arch_Rebar_UShape/es.md): Crea una barra de refuerzo UShape en un elemento estructural seleccionado
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [Barra de refuerzo forma L](Arch_Rebar_LShape/es.md): Crea una barra de armadura LShape en un elemento estructural seleccionado
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Barra de refuerzo doblada](Arch_Rebar_BentShape/es.md): Crea una barra de refuerzo Bent Shape en un elemento estructural seleccionado
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Barra de refuerzo estribo](Arch_Rebar_Stirrup/es.md): crea una barra de refuerzo Stirrup en un elemento estructural seleccionado
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Barra de refuerzo forma helicoidal](Arch_Rebar_Helical/es.md): Crea una barra de armadura helicoidal en un elemento estructural seleccionado
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [RefuerzoColumna](Arch_Rebar_ColumnReinforcement/es.md): crea una barra de refuerzo dentro de un objeto de la estructura del arco de la columna.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [RefuerzoColumnaDosLazosSeisRefuerzos](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/es.md): crea una barra de refuerzo dentro de un objeto de la Estructura del Arco de la Columna.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.png  style="width:32px;"> [RefuerzoBarra](Arch_Rebar_BeamReinforcement/es.md): crea barras de refuerzo dentro de un objeto de la estructura del arco del haz.
    -   <img alt="" src=images/Arch_Rebar.png  style="width:32px;"> [Barra de refuerzo](Arch_Rebar/es.md): crea una barra de refuerzo personalizada en un elemento estructural seleccionado utilizando un croquis.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piso](Arch_Floor/es.md): Crea un piso incluyendo los objetos seleccionados
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [EdificioParte](Arch_BuildingPart/es.md): Crea una parte del edificio que incluye objetos seleccionados
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Edificio](Arch_Building/es.md): Crea un edificio que incluye objetos seleccionados
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Sitio](Arch_Site/es.md): Crea un sitio incluyendo los objetos seleccionados
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Proyecto](Arch_Project/es.md): Crea un proyecto que incluye objetos seleccionados
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Referencia](Arch_Reference/es.md): Enlaza objetos de otro archivo de FreeCAD en este documento
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Ventana](Arch_Window/es.md): Crea una ventana utilizando un objeto seleccionado como base
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Plano de sección](Arch_SectionPlane/es.md): Añade un objeto plano de sección al documento

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Herramientas del eje](Arch_CompAxis/es.md): La herramienta Eje permite colocar una serie de ejes en el documento actual.
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Ejes](Arch_Axis/es.md): Agrega una matriz de ejes de una dirección al documento
    -   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Sistema de ejes](Arch_AxisSystem/es.md): Agrega un sistema de ejes compuesto por varios ejes al documento
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Regilla](Arch_Grid/es.md): Agrega un objeto similar a una cuadrícula al documento

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Techo](Arch_Roof/es.md): Crea un techo con pendiente a partir de la cara seleccionada
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Espacio](Arch_Space/es.md): Crea un objeto de espacio en el documento
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Escaleras](Arch_Stairs/es.md): crea un objeto de escaleras en el documento

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Herramientas del panel](Arch_CompPanel/es.md): Permite construir todo tipo de elementos de tipo panel.
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel/es.md): crea un objeto de panel a partir de un objeto 2D seleccionado
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Corte de panel](Arch_Panel_Cut/es.md): crea una vista en Z de corte 2D desde un panel <small>(v0.17/es)</small> 
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [hoja de panel](Arch_Panel_Sheet/es.md): crea una hoja en 2D que incluye recortes de paneles u otros objetos en 2D <small>(v0.17/es)</small> 
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nido](Arch_Nest/es.md): Permite anidar varios objetos planos dentro de una forma como contenedor <small>(v0.17/es)</small> 

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Marco](Arch_Frame/es.md): Crea un objeto de marco a partir de un diseño seleccionado
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Valla](Arch_Fence/es.md): Crea un objeto de valla a partir de un poste y un camino seleccionado. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Celosía](Arch_Truss/es.md): Crea un braguero a partir de una línea seleccionada desde cero. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Equipamento](Arch_Equipment/es.md): Crea un equipo u objeto de mobiliario
-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Perfil](Arch_Profile/es.md): Crea un perfil 2D paramétrico. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Herramientas conductos](Arch_CompPipe/es.md) <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Conductos](Arch_Pipe/es.md): Crea un conducto <small>(v0.17/es)</small> 
    -   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Conector de conductos](Arch_PipeConnector/es.md): Crea una conexión de esquina o T entre 2 o 3 conductos seleccionados <small>(v0.17/es)</small> 

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Herramientas materiales](Arch_CompSetMaterial/es.md): Las herramientas materiales permiten añadir materiales al documento activo.
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial/es.md): Crea un material y lo atribuye a objetos seleccionados, si hay alguno
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Material](Arch_MultiMaterial/es.md): Crea un multi-material y lo atribuye a objetos seleccionados, si hay alguno <small>(v0.17/es)</small> 
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Lista](Arch_Schedule/es.md): Crea diferentes tipos de listas

### Herramientas de modificación 

Estas son herramientas para modificar objetos de arquitectura.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cortar con una línea](Arch_CutLine/es.md): Cortar un objeto según una línea.<small>(v0.19)</small> 
-   <img alt="" src=images/Arch_CutPlane.png  style="width:32px;"> [Corte con plano](Arch_CutPlane/es.md): Corta un objeto de acuerdo con un plano.
-   <img alt="" src=images/Arch_Add.png  style="width:32px;"> [Añadir](Arch_Add/es.md): Añade objetos a un componente
-   <img alt="" src=images/Arch_Remove.png  style="width:32px;"> [Eliminar](Arch_Remove/es.md): Resta o elimina objetos de un componente
-   <img alt="" src=images/Arch_Survey.png  style="width:32px;"> [Inspección](Arch_Survey/es.md): ingresa o abandona el modo de inspección

### Utilidades

Estas son herramientas adicionales para ayudarte en tareas específicas.

!!FUZZY!!\* <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Componente](Arch_Component/es.md): Crea un componente Arch no paramétrico

-   <img alt="" src=images/Arch_Component_Clone.svg  style="width:32px;"> [Clone componente](Arch_CloneComponent/es.md): Produce Componentes de Arch que son clones de objetos de Arch seleccionados (no confundir con [Borrador de Clon](Draft_Clone/es.md))
-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Dividir malla](Arch_SplitMesh/es.md): Divide una malla seleccionada en componentes separados
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Malla a forma](Arch_MeshToShape/es.md): Convierte una malla en una forma, unificando caras coplanares
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [Seleccionar mallado no-sólido](Arch_SelectNonSolidMeshes/es.md): Selecciona todos los mallados no-sólidos de la selección actual o del documento
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remover forma](Arch_RemoveShape/es.md): vuelve el objeto de arquitectura basado en la forma cúbica completamente paramétrico
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Tapar agujeros](Arch_CloseHoles/es.md): Cierra los agujeros en el objeto basado en formas seleccionado
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Fusionar las paredes](Arch_MergeWalls/es.md): Fusionar dos o más paredes
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Comprobar](Arch_Check/es.md): Comprueba si los objetos seleccionados son sólidos y no contienen defectos
-   <img alt="" src=images/Ifc.svg  style="width:32px;"> [Explorador IFC](Arch_IfcExplorer/es.md): explore los contenidos de un archivo [IFC](Arch_IFC/es.md)
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Cambia IFC-Brep bandera](Arch_ToggleIfcBrepFlag/es.md): Obliga a exportar un objeto seleccionado como [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 vistas de malla](Arch_3Views/es.md): Crea vistas superior, frontal y lateral desde una [malla](Mesh_Workbench/es.md).
-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Crear hoja de cálculo IFC\...](Arch_IfcSpreadsheet/es.md): Crea una hoja de cálculo para almacenar las propiedades [IFC](Arch_IFC/es.md) de un objeto
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Alternar subcomponentes](Arch_ToggleSubs/es.md): Muestra u oculta los subcomponentes de un objeto Arch.

### Preferencias

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferencias](Arch_Preferences/es.md): preferencias por el aspecto predeterminado de los muros, estructuras, armaduras, ventanas, escaleras, paneles, tuberías, rejillas y hachas.

### Formatos de archivo 

-   [IFC](Arch_IFC/es.md) : Industry foundation Classes
-   [DAE](Arch_DAE/es.md) : Formato de malla de Collada
-   [OBJ](Arch_OBJ/es.md) : Formato Obj de malla (sólo exportar)
-   [JSON](Arch_JSON/es.md): formato de notación de objetos JavaScript (solo exportación)
-   [3DS](Arch_3DS/es.md): formato 3DS (solo importación)
-   [SHP](Arch_SHP/es.md): GIS Archivos de forma (solo importación)

## API

El Módulo de arquitectura puede usarse en scripts de [Python](Python/es.md) y en [macros](macros/es.md) usando las funciones de [Arch Python API](http://www.freecadweb.org/api/Arch.html)

## Tutoriales

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): Un ejemplo de cómo FreeCAD puede empezar a tener su lugar preliminar en un flujo de trabajo de arquitectura.
-   [Tutorial de Arch](Arch_tutorial/es.md) (v0.14)
-   [Descripción rápida de Arch en el blog de Yorik](http://yorik.uncreated.net/guestblog.php?2012=180) (v0.13)
-   [Presentación en video del Ambiente de trabajo Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Tutorial del panel de Arch](Arch_panel_tutorial/es.md) (v0.15)
-   [capítulo de modelado BIM del manual de FreeCAD](Manual:_modelado_BIM/es.md)
-   [Importar desde STL u OBJ](Import_from_STL_or_OBJ/es.md)
-   [Exportar a STL u OBJ](Export_to_STL_or_OBJ/es.md)





 

[Category:Workbenches](Category:Workbenches.md)
