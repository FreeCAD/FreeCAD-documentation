# Release notes 0.20/es
**Esta página registra las nuevas características a medida que se añaden a la versión de desarrollo de FreeCAD, que actualmente es la 0.20. Cuando se produzca la congelación de las características de la 0.20, se borrarán estos mensajes y no se añadirán más características a esta página. Se espera que FreeCAD 0.20 sea lanzado a finales de mayo 2022.**


**¡¡¡ Todas las imágenes de esta página deben utilizar el sufijo **_relnotes_0.20** !!!**


<div style="text-align   *center; background   *#e0e0ee; margin   *1em 7em; padding   *0.5em 2em; border   *2px solid #bb7736;">

¿Faltan características? Menciónelas en el hilo del foro [Notas de la versión 0.20](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=56135).

Vea [Ayuda FreeCAD](Help_FreeCAD/es.md) para saber cómo contribuir a FreeCAD.


</div>


<div>


{{TOCright}}

**FreeCAD 0.20** fue liberado el **DD de Mes del 2022**, consíguelo desde la página [Descarga](Download/es.md). Este es un resumen de las nuevas características y los cambios más interesantes.

Las notas de lanzamiento de versiones anteriores de FreeCAD se pueden encontrar en [Lista de características](Feature_list/es#Notas_de_lanzamiento.md).

## Destacados

## General

### Compilación

Desde esta versión de FreeCAD solo puede ser compilado usando Qt 5 y Python 3.

Para [compilar FreeCAD en Windows](Compile_on_Windows.md), hay diferentes Libpacks (bibliotecas pre-empaquetadas) disponibles   *

-   Libpack para Windows con Qt xx, OCC yy, y Python zz

La versión de Python más vieja soportada es 3.6.9 según este [hilo del foro de FC](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=62701).

Sistemas operativos soportados   *

-   Windows 7, 8 y 10
-   Linux Ubuntu Bionic Beaver (18.04) y Focal Fossa (20.04)
-   MacOS versión mínima 10.12 Sierra

### Seguimiento de problemas/bugs 

El seguimiento de problemas de FreeCAD se ha movido a GitHub   * <https   *//github.com/FreeCAD/FreeCAD/issues>

**Nota   *** Solo se considerarán los informes de errores con una discusión del foro anterior. Los informes sin esto serán cerrados.

### freecad.org

Estamos contentos de que el proyecto [KiCad](https   *//www.kicad.org/), a través de [KiCad Services Corp.](https   *//www.kipro-pcb.com/), nos patrocinó el dominio freecad.org. Ahora todos los sitios web de FreeCAD están disponibles en [freecadweb.org](https   *//freecadweb.org) y [freecad.org](https   *//freecad.org).

### Documentación

### Limitaciones conocidas 

## Interfaz de usuario 

+++
| ![](images/Navi_Cube_relnotes_0.20.gif ) | El cubo de navegación fue reelaborado para habilitar estas nuevas características   *                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                | -   Ahora hay caras en las aristas para ver la escena en ángulos de 45°.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                | -   La opción nueva de preferencias [Girar al más cercano](Preferences_Editor#Navigation.md) permite ver la escena en el estado sensible más cercano. Cuando está apagado, hacer clic en una cara del cubo terminará siempre en la misma posición, sin importar en qué estado se encontraba el cubo al hacer clic en la cara. Vea la animación a la izquierda para comprender lo que esto significa. Pruebe la misma secuencia de clics que en la animación sin la opción \'\' Girar al más cercano \'\' para experimentar la diferencia. |
|                                                                | -   Al hacer clic en el punto en la parte superior derecha del cubo, puede ver rápidamente la vista posterior de la escena actual.                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                | -   El tamaño del cubo se puede ajustar en la opción de preferencias [Tamaño del cubo](Preferences_Editor#Navigation.md).                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                | [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=52118), [Pull request \#4502](https   *//github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                                                                              |
+++

   
  ![](images/Improved_tooltips_relnotes_0.20.gif )   La información sobre herramientas ahora muestra el nombre del comando en el título, lo que facilita que los nuevos usuarios busquen ayuda. Al final de la información sobre herramientas, el nombre del comando \"interno\" se agrega entre paréntesis   * *(Std\_WhatsThis)*. Este es también el nombre de la página que documenta el comando en la Wiki. [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=34&t=58747), [Pull request \#4978](https   *//github.com/FreeCAD/FreeCAD/pull/4978).
   

   
  <img alt="" src=images/Std_UserEditMode_relnotes_0.20.gif  style="width   *384px;">   El nuevo comando [Std UserEditMode](Std_UserEditMode.md) permite al usuario elegir un modo de edición que será usado al dar doble clic a un objeto en la [vista de árbol](Tree_view.md). Dé clic en la imagen de la izquierda para ver una animación de la selección. Si un modo de edición no es aplicable, el modo de edición por defecto de del objeto es usado en su lugar. [Pull request \#5110](https   *//github.com/FreeCAD/FreeCAD/pull/5110).
   

+++
| ![](images/Dependencies-selection_relnotes_0.20.png ) | El menú contextual de la [vista de árbol](Tree_view.md) tiene la nueva entrada **Añadir objetos dependientes a la selección**. |
|                                                                                          | [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=13566), [Pull request \#4133](https   *//github.com/FreeCAD/FreeCAD/pull/4133).             |
|                                                                                          |                                                                                                                                                                  |
|                                                                                          | En la imagen se seleccionó el objeto *Hole001* y luego                                                                                                           |
|                                                                                          | se agregaron sus dependencias a la selección a través del menú contextual.                                                                                       |
+++

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.20.png  style="width   *200px;"> | La nueva herramienta **[Corte de sección](Part_SectionCut.md)** permite tener cortes no huecos y también persistentes de piezas y ensamblajes. |
|                                                                                                         | [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=27&t=52441), [Pull request \#4118](https   *//github.com/FreeCAD/FreeCAD/pull/4118).  |
+++

### Otras mejoras de la interfaz de usuario 

-   Ahora es posible utilizar el separador decimal perteneciente al idioma especificado para la interfaz de FreeCAD. Por ejemplo, en un Windows alemán, cuando establece el idioma de la interfaz en **Inglés** y selecciona la nueva opción **Usar formato de número de idioma seleccionado**, el punto se utilizará como separador decimal. Consulte [Preferencias](Preferences_Editor#General.md). [Pull request \#6364](https   *//github.com/FreeCAD/FreeCAD/pull/6364)**Nota**   * Para simulaciones [FEM](FEM_Workbench.md), usar el punto como separador decimal es muy recomendado para obtener resultados correctos.
-   Se han agregado dos nuevos estilos de navegación con el mouse. Uno basado en **[OpenSCAD](Mouse_navigation#OpenSCAD_navigation.md)**, el otro en **[TinkerCAD](Mouse_navigation#TinkerCAD_navigation.md)**. [Discusión en el foro OpenSCAD](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=60975), [Discusión en el foro TinkerCAD](https   *//forum.freecadweb.org/viewtopic.php?p=544639#p544376), [commit 1](https   *//github.com/FreeCAD/FreeCAD/commit/a1c9ab658c), [commit 2](https   *//github.com/FreeCAD/FreeCAD/commit/ef100d55e9d50), [commit 3](https   *//github.com/FreeCAD/FreeCAD/commit/549e5b5650).
-   Ahora es posible desplazar la vista del [gráfico de dependencia](Std_DependencyGraph.md) con el mouse. [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=34791), [Pull request \#4638](https   *//github.com/FreeCAD/FreeCAD/pull/4638).
-   Se solucionó un problema por el cual el uso de plumas para tablet (por ejemplo, tablet Wacom) era lento hasta el punto de ser completamente inutilizable. [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=45046), [Pull request \#4687](https   *//github.com/FreeCAD/FreeCAD/pull/4687).
-   El sistema de coordenadas en la vista 3D se puede cambiar de tamaño en las preferencias en la sección [Mostrar → Vista 3D](Preferences_Editor#3D_View.md). [Pull request \#5182](https   *//github.com/FreeCAD/FreeCAD/pull/5182)
-   Una nueva configuración en [Preferencias → General](Preferences_Editor#General.md) permite sustituir el separador decimal del teclado numérico con el separador local apropiado si son diferentes. [Pull request \#3256](https   *//github.com/FreeCAD/FreeCAD/pull/3256) [Pull request \#5150](https   *//github.com/FreeCAD/FreeCAD/pull/5150) [Pull request \#5203](https   *//github.com/FreeCAD/FreeCAD/pull/5203)
-   Ahora es posible configurar la tecla **Retroceso** como un atajo de tecla independiente sin necesidad de especificar una tecla modificadora adicional. [Pull request \#5428](https   *//github.com/FreeCAD/FreeCAD/pull/5428)

## Núcleo del sistema y API 

### Núcleo

   
  <img alt="" src=images/Object_selection_relnotes_0.20.png  style="width   *384px;">   Cuando se utiliza **Editar → Copiar** o **Editar → Duplicar selección** para un objeto con dependencias hay un botón nuevo **Usar selecciones originales** en el diálogo de selección de objetos. Haga clic en este botón para copiar/duplicar únicamente los objetos que seleccionó originalmente antes de abrir el cuadro de diálogo, ignorando las dependencias e ignorando cualquier acción que pudiera haber sido realizada mientras el cuadro de diálogo estaba abierto, como marcar o desmarcar algunas de las casillas de verificación. El efecto es el mismo a que si hubiera desmarcado todas las casillas de verificación junto a los objetos que no seleccionó originalmente y hubiera pulsado OK. Nota   * hay que tener especial cuidado al copiar/duplicar las páginas de TechDraw. Se recomienda copiar/duplicar también todos los hijos de la página (plantillas, vistas, dimensiones, etc.). De lo contrario, los cambios que se realicen en una de las páginas afectarán también a la otra, por ejemplo, si se elimina una de las vistas de una página también se eliminará de la otra. La eliminación de una de las páginas también eliminará todo el contenido de la otra página si no se hacen también copias del contenido.
   

   
  <img alt="" src=images/PrefPacks_relnotes_0.20.png  style="width   *384px;">   Se agregó un nuevo tipo de complemento llamado [Paquete de preferencias](Preference_Packs.md), que permite a un subconjunto de las preferencias (user.cfg) de un usuario ser guardadas, distribuidas y aplicadas fácilmente por otros usuarios. Los paquetes de preferencias se pueden usar para distribuir \"Temas\", por ejemplo, al permitir que un desarrollador incluya tanto una hoja de estilo Qt para widgets así como un conjunto de otros colores y estilos para elementos en la interfaz de usuario que no se pueden configurar usando una hoja de estilo ( por ejemplo, colores de texto en el editor de Python o en la vista de informe, etc.). Todo lo que se puede configurar a través de un archivo user.cfg se puede configurar mediante un paquete de preferencias. [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=62477)
   

   
  <img alt="" src=images/Autoload_relnotes_0.20.png  style="width   *384px;">   El panel de preferencias de los \"Entornos de trabajo\" fue modificado para permitir cargar automáticamente los entornos de trabajo mientras FreeCAD inicia.
   

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### Nueva API de Python 


<div class="mw-collapsible-content">

-   *Circle2dPy   *   *getCircleCenter*   * Obtiene el centro del círculo definido por tres puntos. [commit 3dc91fa2](https   *//github.com/FreeCAD/FreeCAD/commit/3dc91fa2)

-   *ComplexGeoDataPy   *   *applyRotation*   * Aplica una rotación adicional a la ubicación. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *applyTranslation*   * Aplica una traslación adicional a la ubicación. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *countSubElements*   * Devuelve el número de elementos de un tipo. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getElementTypes*   * Devuelve una lista de los tipos de elementos. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getFaces*   * Devuelve una tupla de puntos y triángulos con una exactitud dada. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getLines*   * Devuelve una tupla de puntos y líneas con una exactitud dada. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getLinesFromSubelement*   * Devuelve vértices y líneas de un subelemento. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getPoints*   * Devuelve una tupla de puntos y normales con una exactitud dada. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *transformGeometry*   * Aplica una transformación a la geometría subyacente. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)

-   *ControlPy   *   *showModelView*   * Muestra la vista del modelo. [commit 033bf619](https   *//github.com/FreeCAD/FreeCAD/commit/033bf619)

-   *DocumentPy   *   *clearDocument*   * Limpia todo el documento. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *getFileName*   * Para un documento regular devuelve su propiedad de nombre de archivo. Para un documento temporal devuelve su directorio transitorio. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *getProgramVersion*   * Obtiene la versión del programa con la que se creó un archivo de proyecto. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *isClosable*   * Checa si el documento puede ser cerrado. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *isSaved*   * Checa si el documento está guardado. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *isTouched*   * Checa si algún objeto está en un estado de tocado. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *mustExecute*   * Checa si algún objeto debe ser recalculado. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *purgeTouched*   * Purga el estado tocado de todos los objetos. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *setClosable*   * Establece una bandera que permite o prohíbe cerrar un documento. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)

-   *DrawPagePy   *   *requestPaint*   * Pinta una página de TechDraw. [commit 79f9fb68](https   *//github.com/FreeCAD/FreeCAD/commit/79f9fb68)

-   *HLRBRep\_AlgoPy*   * Para acceder a la eliminación de la línea oculta de la Parte (HLR). [commit 73a98671](https   *//github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *HLRBRep\_PolyAlgoPy*   * Para acceder a la poli-eliminación de la línea oculta de la Parte (HLR). [commit ea85cf5e](https   *//github.com/FreeCAD/FreeCAD/commit/ea85cf5e)
-   *HLRToShapePy*   * Para acceder a la eliminación de la línea oculta de la Parte (HLR). [commit 73a98671](https   *//github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *PolyHLRToShapePy*   * Para acceder a la poli-eliminación de la línea oculta de la Parte (HLR). [commit ea85cf5e](https   *//github.com/FreeCAD/FreeCAD/commit/ea85cf5e)

-   *MDIViewPy   *   *printPdf*   * Imprime un PDF. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *printPreview*   * Imprime una vista previa. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *printView*   * Imprime una vista. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *redoActions*   * Rehace acciones. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *undoActions*   * Deshace acciones. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)

-   *PrecisionPy*   * Para acceder a la precisión definida por el kernel de OpenCascade. [commit 20b86e55](https   *//github.com/FreeCAD/FreeCAD/commit/20b86e55)

-   *PropertyContainerPy   *   *setDocumentationOfProperty*   * Establece la cadena de documentación de una propiedad dinámica de esta clase. [commit 8cf3cf33](https   *//github.com/FreeCAD/FreeCAD/commit/8cf3cf33)
-   *PropertyContainerPy   *   *setGroupOfProperty*   * Establece el nombre del grupo de una propiedad dinámica. [commit 8cf3cf33](https   *//github.com/FreeCAD/FreeCAD/commit/8cf3cf33)

-   *PythonWorkbenchPy   *   *reloadActive*   * Recarga el entorno de trabajo activo después de cambiar menús o barras de herramientas. [commit 0bbc253d](https   *//github.com/FreeCAD/FreeCAD/commit/0bbc253d)

-   *RotationPy   *   *fromEuler*   * Establece los ángulos de Euler de una rotación u obtiene los ángulos de Euler en una secuencia dada para una rotación. [commit 951a0be9](https   *//github.com/FreeCAD/FreeCAD/commit/951a0be9)
-   *RotationPy   *   *toEulerAngles*   * Obtiene los ángulos de Euler en una secuencia dada para esta rotación.. [commit c1454dfb](https   *//github.com/FreeCAD/FreeCAD/commit/c1454dfb)

-   *SpreadsheetViewPy*   * Para acceder a las hojas de cálculo. [commit 6e713628](https   *//github.com/FreeCAD/FreeCAD/commit/6e713628)

-   *UnitsApi   *   *sToNumber*   * Convierte una cantidad o float a una cadena. [commit befbd95d](https   *//github.com/FreeCAD/FreeCAD/commit/befbd95d)

-   *View3DInventorPy   *   *getCornerCrossSize*   * Devuelve el tamaño actual de la cruz del eje de la esquina. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy   *   *setPopupMenuEnabled*   * Habilita un menú emergente. [commit 9def811a](https   *//github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy   *   *isCornerCrossVisible*   * Devuelve la visibilidad actual de de la cruz del eje de la esquina. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy   *   *isPopupMenuEnabled*   * Devuelve si el menú emergente está habilitado. [commit 9def811a](https   *//github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy   *   *projectPointToLine*   * Proyecta el punto 2D dado a una línea. [commit b6527a70](https   *//github.com/FreeCAD/FreeCAD/commit/b6527a70)
-   *View3DInventorPy   *   *setCornerCrossSize*   * Define el tamaño de la cruz del eje de la esquina. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy   *   *setCornerCrossVisible*   * Define la visibilidad de la cruz del eje de la esquina. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)

-   *ViewProviderSpreadsheetPy*   * Para manejar celdas de hojas de cálculo.[commit 16bbe123](https   *//github.com/FreeCAD/FreeCAD/commit/16bbe123) and [commit 093f15dc](https   *//github.com/FreeCAD/FreeCAD/commit/093f15dc)


</div>

#### API cambiada 

-   *MeshObject   *   *trim(base, normal)* fue cambiado a *MeshPy   *   *trimByPlane(base, normal)*   * Recorta la malla con un plano dado. [commit 837de28e](https   *//github.com/FreeCAD/FreeCAD/commit/837de28e)


</div>

## Gestor de complementos 

   
  <img alt="" src=images/AddonManagerExpanded_relnotes_0.20.png  style="width   *400px;">   El [Gestor de complementos](Std_AddonMgr.md) se modificó para permitir la distribución de paquetes de preferencias y para mostrar la información que se encuentra en los metadatos de los complementos. El gestor de complementos también incluye soporte mejorado para complementos cuyo código fuente se encuentra en varias ubicaciones de alojamiento git diferentes. Se mejoró el soporte de redes para proporcionar un manejo más sólido de las conexiones SSL y soporte para proxies que requieren autenticación. Se agregó soporte para agregar automáticamente botones de macro a la barra de herramientas después de la instalación, para deshabilitar complementos sin eliminarlos y para cambiar qué rama de git de un complemento es checada. Finalmente, se modificó la interfaz de usuario para mejorar la búsqueda y visualización de diferentes filtros de lista.
   

## Ambiente de Trabajo Arquitectura 

+++
| <img alt="" src=images/ArchWindow_Placement_1r_relnotes_0.20.png  style="width   *250px;"> <img alt="" src=images/ArchWindow_Placement_2r_relnotes_0.20.png  style="width   *250px;"> | **Entorno de trabajo SketchArch**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                         | Con la <img alt="" src=images/Attach_in_SketchArch.svg  style="width   *20px;"> [Adjuntar característica](https   *//github.com/paullee0/FreeCAD_SketchArch) es ahora posible colocar <img alt="" src=images/Arch_Window.svg  style="width   *20px;"> [Ventanas](Arch_Window.md) y <img alt="" src=images/Arch_Equipment.svg  style="width   *20px;"> [Equipo](Arch_Equipment.md) parametricamente e intuitivamente en relación to <img alt="" src=images/Arch_Wall.svg  style="width   *20px;"> [Muros](Arch_Wall.md). Para usar esta característica el entorno de trabajo experimental externo <img alt="" src=images/SketchArch_Workbench.svg  style="width   *20px;"> [Entorno de trabajo SketchArch](https   *//github.com/paullee0/FreeCAD_SketchArch) debe de ser instalado. [Complemento y leéme en Github](https   *//github.com/paullee0/FreeCAD_SketchArch) (No está disponible aún en el [gestor de complements](Std_AddonMgr.md)). |
|                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                         | [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=23&t=50802)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+++

+++
| <img alt="" src=images/NewArchStructureProperties_relnotes_0.20.jpg  style="width   *250px;"> | **Nuevas propiedadesel de los objetos de estructura de Arch**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               | **BasePerpendicularToTool**   * copia la Base (perfil de extrusión) al inicio de la herramienta (trayectoria de extrusión) y la coloca perpendicular a la primera arista de la herramienta. Es lo mismo que adjuntar la Base con MapMode=NormalToEdge, pero es automático y permite reutilizar el mismo objeto Base para múltiples Estructuras. Cuando BasePerpendicularToTool = True, hay más propiedades que controlan la colocación de la Base en relación con el eje de la Herramienta. Se muestran en la imagen adjunta.                                                                                      |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               | **ToolOffsetFirst** y **ToolOffsetLast**   * extender/recortar la estructura al principio y al final respectivamente (la longitud real de la estructura está disponible en la propiedad ComputedLength de solo lectura)                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               | -   BaseRotation   * rota la Base (la rotación es alrededor del punto \"(0,0)\" de la Base que es el centro para [Perfil de Arch](Arch_Profile.md), el origen para los croquis y usualmente el primer punto para [Draft Wires](Draft_Wire.md))                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                               | -   BaseOffsetX and BaseOffsetY   * mueve la Base (perfil de extrusión)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                               | -   BaseMirror   * refleja la Base (perfil de extrusión)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               | También se ha añadido un nuevo comando **Crear estructura de arco múltiple**. Utiliza el primer objeto seleccionado como Base, y crea objetos de Estructuras de Arco para cada Arista de los otros objetos seleccionados. A continuación, las propiedades de los objetos de estructura individuales pueden ajustarse en el editor de propiedades. Este comando se ha añadido para el flujo de trabajo con un croquis maestro (existe el riesgo de que se produzcan problema de denominación topológica a menos que se cree una copia no paramétrica del croquis maestro o se utilice la versión de Realthunder) |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               | [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=23&t=43228&start=60), [Pull request \#3229](https   *//github.com/FreeCAD/FreeCAD/pull/3229)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+++

## Ambiente de Trabajo Draft 

-   Se agregó una casilla de verificación **Global** al panel de tareas de muchos comandos de dibujo. Marcarla permite introducir coordenadas en el sistema global de coordenadas incluso si el [plano de trabajo](Draft_SelectPlane.md) no está alineado con el plano global XY.

-   Se introdujo el comando <img alt="" src=images/Draft_Hatch.svg  style="width   *24px;"> [Draft Hatch](Draft_Hatch.md). Crea sombreados en las caras de un objeto seleccionado utilizando patrones de archivos PAT de AutoCAD.

-   Se introdujo el comando <img alt="" src=images/Draft_AddNamedGroup.svg  style="width   *24px;"> [Draft AddNamedGroup](Draft_AddNamedGroup.md). El comando <img alt="" src=images/Draft_AddToGroup.svg  style="width   *24px;"> [Draft AddToGroup](Draft_AddToGroup.md) fue extendido con la misma funcionalidad.

-   El trabajo en el comando <img alt="" src=images/Draft_SetStyle.svg  style="width   *24px;"> [Draft SetStyle](Draft_SetStyle.md), que estaba en progreso en FreeCAD versión 0.19, fue completado.

-   Se ha añadido una opción de edición con doble clic para <img alt="" src=images/Draft_Text.svg  style="width   *24px;"> [Texto de Draft](Draft_Text.md). Abre el mismo panel de tareas de edición utilizado al crear un texto.

-   Para <img alt="" src=images/Draft_Dimension.svg  style="width   *24px;"> [Dimensiones de Draft](Draft_Dimension.md) la {{Value|arch}} **Sobreescritura de unidades** para las dimensiones arquitectónicas imperiales fue introducido.

-   Los objetos <img alt="" src=images/Draft_Shape2DView.svg  style="width   *24px;"> [Draft Shape2DView](Draft_Shape2DView.md) ahora tienen una propiedad de **Auto actualización**. Ponerlo en {{False}} puede ser útil si hay muchos Draft Shape2DViews en un documento o si son complejos.

-   Ahora es posible revertir un [Draft Wire](Draft_Wire.md) a través del menú contextual <img alt="" src=images/Draft_Edit.svg  style="width   *24px;"> [Draft Edit](Draft_Edit.md). [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [Pull request \#4811](https   *//github.com/FreeCAD/FreeCAD/pull/4811).

### Otras mejoras de Draft 

-   Se arregló [Draft Snap Grid](Draft_Snap_Grid.md) cuando el cursor está sobre una cara. [Discusión en el foro](https   *//forum.freecad.org/viewtopic.php?f=23&t=62274). [Git commit](https   *//github.com/FreeCAD/FreeCAD/commit/1761eb8ce).

-   Los nuevos [Textos de Draft](Draft_Text.md) ahora son alineados con el [plano de trabajo](Draft_SelectPlane.md), [Pull request \#5092](https   *//github.com/FreeCAD/FreeCAD/pull/5092).

-   Se ha añadido soporte para dos convertidores DWG   * [LibreDWG](https   *//www.gnu.org/software/libredwg) y [QCAD pro](https   *//qcad.org/en/qcad-command-line-tools#dwg2dwg). Vea [Preferencias de importación y exportación](Import_Export_Preferences#DWG.md) y [FreeCAD y la importación de DWG](FreeCAD_and_DWG_Import.md) para más información.

## Ambiente de Trabajo FEM 

   
  <img alt="" src=images/FEM_Z88-settings_relnotes_0.20.png  style="width   *384px;">Las nuevas configuraciones de Z88 y sus valores por defecto.                                                                          El [solucionador Z88](FEM_SolverZ88.md) ahora es totalmente usable. Ahora puede especificar el método del solucionador y cambiar la configuración de la memoria. Los nuevos valores por defecto le permiten realizar también simulaciones complejas directamente. [commit d035bbc1ca y siguientes](https   *//github.com/FreeCAD/FreeCAD/commit/d035bbc1ca)
  <img alt="" src=images/FEM_buckling-analysis_relnotes_0.20.gif  style="width   *384px;">Resultado de un análisis de pandeo lineal.Clic en la imagen para ver la animación.                            Ahora es posible realizar análisis de pandeo utilizando el solucionador [Calculix](FEM_SolverCalculixCxxtools.md). [Pull request \#4379](https   *//github.com/FreeCAD/FreeCAD/pull/4379)
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature_relnotes_0.20.png  style="width   *384px;">Efecto de *Tamaño de malla desde curvatura*; izquierda   * puesto a 12, derecha   * desactivado                 Hay una nueva propiedad para el creador de mallas [Gmsh](FEM_MeshGmshFromShape.md). Se puede especificar el número de elementos de malla por $2\pi$ veces el radio de la curvatura. El valor por defecto es 12 y para obtener una malla más fina en las esquinas o agujeros pequeños, este valor se puede aumentar para obtener mejores resultados. Esta característica requiere Gmsh 4.8 o más reciente. [Discusión en el foro](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=56401), [Pull request \#4596](https   *//github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm_relnotes_0.20.png  style="width   *384px;">Efecto del algoritmo de recombinación; izquierda   * usando *Simple*, derecha   * usando *Simple full-quad*   FreeCAD permite ahora seleccionar un algoritmo así como la recombinación de mallas 3D para el creador de mallas [Gmsh](FEM_MeshGmshFromShape.md). Para más detalles acerca de la recombinación de elementos de malla vea [FEM MeshGmshFromShape](FEM_MeshGmshFromShape#Element_Recombination.md). [Pull request \#4706](https   *//github.com/FreeCAD/FreeCAD/pull/4706)
   

### Otras mejoras de FEM 

-   **Important   *** Starting from this release, FreeCAD will use SI units (m, kg, s, K, A, mol, cd) to write the [Elmer solver](FEM_SolverElmer.md) input files (*case.sif* and *mesh.nodes*). This is independent of the used FreeCAD [unit system](Preferences_Editor#Units.md).
-   **Important   *** Starting from this release, the scale of [result pipelines](FEM_PostPipelineFromResult.md) and their [filters](FEM_Workbench#Menu__Results.md) will use SI units (m, kg, s, K, A, mol, cd). So the displacement is given in meter, the stress in Pascal. This applies for all SI-derived FreeCAD [unit systems](Preferences_Editor#Units.md).
-   Solving with the [Calculix](FEM_SolverCalculixCxxtools.md) solver now uses all CPU cores. [Pull request \#6374](https   *//github.com/FreeCAD/FreeCAD/pull/6374)
-   Meshing with [Gmsh](FEM_MeshGmshFromShape.md) now uses all CPU cores. [Pull request \#6370](https   *//github.com/FreeCAD/FreeCAD/pull/6370)
-   The element order of [Gmsh](FEM_MeshGmshFromShape.md) meshes can be changed via the mesh dialog. [Pull request \#4660](https   *//github.com/FreeCAD/FreeCAD/pull/4660)
-   A new constraint was added   * **Model → Mechanical Constraints → [<img src=images/FEM_ConstraintCentrif.svg style="width   *16px"> [Constraint Centrif](FEM_ConstraintCentrif.md)**. [Pull request \#4738](https   *//github.com/FreeCAD/FreeCAD/pull/4738)
-   A new solver was added   * **Solve → [<img src=images/FEM_SolverMystran.svg style="width   *16px"> [Solver Mystran](FEM_SolverMystran.md)**. Multiple commits.
-   A new constraint was added   * **Model → Mechanical Constraints → [<img src=images/FEM_ConstraintSpring.svg style="width   *16px"> [Constraint Spring](FEM_ConstraintSpring.md)**. [Pull request \#4982](https   *//github.com/FreeCAD/FreeCAD/pull/4982)
-   It is now possible to have [result pipelines](FEM_PostPipelineFromResult.md) with several filters, where some take other filters as input, some take the results directly from the pipeline. [commit 708a300b](https   *//github.com/FreeCAD/FreeCAD/commit/708a300b)
-   Material cards can now contain values for the electrical conductivity. [Pull request \#4647](https   *//github.com/FreeCAD/FreeCAD/pull/4647)
-   Material cards added for Nitrogen and Argon. [Pull request \#4649](https   *//github.com/FreeCAD/FreeCAD/pull/4649)
-   Support for the [Gmsh](FEM_MeshGmshFromShape.md) mesh algorithms \"HXT\" (3D) and \"Packing Parallelograms\" (2D) added. [Pull request \#4654](https   *//github.com/FreeCAD/FreeCAD/pull/4654)
-   Allow to set for the [Gmsh](FEM_MeshGmshFromShape#Properties.md) property **High Order Optimize** a certain algorithm. [Pull request \#4705](https   *//github.com/FreeCAD/FreeCAD/pull/4705)
-   Nonlinear solid materials with simple hardening can now have an arbitrary number of yield points. [Pull request \#5024](https   *//github.com/FreeCAD/FreeCAD/pull/5024)
-   Allow modal adding/removal of geometric entities to constraints acting on boundaries. [Pull request \#5117](https   *//github.com/FreeCAD/FreeCAD/pull/5117)
-   Most FEM constraint dialogs now behave uniformly and provide the same 3D object selection features. [Pull request \#5391](https   *//github.com/FreeCAD/FreeCAD/pull/5391)

## Import

## Export

-   DXF   * The missing unit block was added to the header14.rub file. [Pull request \#5793](https   *//github.com/FreeCAD/FreeCAD/issues/5793)

## Malla

### Improved support for NASTRAN GRID elements 

The Mesh import tool now supports the high-precision \"GRID\*\" element. The standard-precision \"GRID\" element was also improved, now supporting both space-delimited numeric input as well as fixed-field-width input, per the NASTRAN95 format documentation.

### Otras mejoras de Mesh 

Fixed false negatives during self-intersection tests when facets are coplanar   * [Pull request \#5002](https   *//github.com/FreeCAD/FreeCAD/pull/5002).

## Ambiente de Trabajo OpenSCAD 

Interoperability with OpenSCAD has been improved, adding support for several operations missing from earlier versions (linear extrude with rotations, rotational extrusions). Several operations are modified to provide improved FreeCAD object equivalents, particularly for twisted extrusions. Surface generation from discrete data was modified to give more OpenSCAD-like results, rather than splined surfaces.

New options were added to support running either FreeCAD, OpenSCAD, or both, in sandboxed environments such as AppImages and Snap packages   * data can now be transferred to and from OpenSCAD via the standard temporary directory mechanism, via a user-specified temp directory that both executables have access to, or new to OpenSCAD 2021.1, via a \"stdout pipe\" mechanism, bypassing temporary files entirely.

**Add OpenSCAD element** - now has additional options

Load    - load a scad file
Save    - save a scad file
Refresh - Update FreeCAD view
Clear   - Clear text input

There is also a text box for feedback of OpenSCAD errors.

![](images/OpenSCAD_AddElement_relnotes_0.20.png )

## Ambiente de Trabajo Pieza 

   
  <img alt="" src=images/Part_Extrusion-inner-structures_relnotes_0.20.png  style="width   *384px;">Tapered extrusion of a sketch with an inner structure.   A tapered [extrusion](Part_Extrude.md) of inner structures now creates usable results. Previously, inner structures were extruded as if they were stand-alone and not part of a structure. [Pull request \#5367](https   *//github.com/FreeCAD/FreeCAD/pull/5367)
   

### Otras mejoras de Part 

-   The dialog to edit [Cylinders](Part_Cylinder.md) now allows to specify an angle relative to the normal of the chosen attachment plane. This way one can create skew cylinders. [Pull request \#4708](https   *//github.com/FreeCAD/FreeCAD/pull/4708)
-   The following commands now support App   *   *Links   * [Loft](Part_Loft.md), [Sweep](Part_Sweep.md), [Extrude](Part_Extrude.md), [Revolve](Part_Revolve.md), [Reverse shapes](Part_ReverseShapes.md), [Mirror](Part_Mirror.md), [Offset2D](Part_Offset2D.md), [Offset3D](Part_Offset.md), [Check Geometry](Part_CheckGeometry.md), [Ruled Surface](Part_RuledSurface.md), [Cross-sections](Part_CrossSections.md), and [Thickness](Part_Thickness.md). [Pull request \#6478](https   *//github.com/FreeCAD/FreeCAD/pull/6478)

### Ambiente de Trabajo DiseñoPieza 

+++
| <img alt="" src=images/PD_Pad-Length-along-reference_relnotes_0.20.gif  style="width   *384px;">Padding along an edge from the model.Click on the image to see the animation.                                                                      | There is a new option to pad along the direction of an edge in the 3D model. [Pull request \#4685](https   *//github.com/FreeCAD/FreeCAD/pull/4685)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+++
| <img alt="" src=images/PartDesign_Chamfer_Face_Selection_relnotes_0.20.png  style="width   *384px;">                                                                                                                                                                           | When Distance and Angle is specified in the [Chamfer](PartDesign_Chamfer.md) tool and faces are selected, the distance will be applied along the selected faces. Likewise if two distances are specified then Size 1 will be applied along the selected face. This behaviour can be swapped to the other face using the flip direction button. [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=19&t=62084), [Pull request \#5039](https   *//github.com/FreeCAD/FreeCAD/pull/5039)                                                                                                                                                                                                                                                                     |
+++
| <img alt="" src=images/PartDesign_Loft_Vertex_relnotes_0.20.png  style="width   *384px;">A loft with multiple sections, the final one is a vertex.                                                                                                                      | It is now possible to create an [Additive](PartDesign_AdditiveLoft.md) or [Subtractive Loft](PartDesign_SubtractiveLoft.md), or an [Additive](PartDesign_AdditivePipe.md) or [Subtractive Pipe](PartDesign_SubtractivePipe.md) towards, or from, a [Vertex](Glossary#V.md) of either a sketch or a body. This allows to create pyramids for example.**Note**   * Vertices in sketches are created as construction geometry. To use them as endpoints of lofts, you must first [change them to normal geometry](Sketcher_ToggleConstruction.md). [Pull request \#5170](https   *//github.com/FreeCAD/FreeCAD/pull/5170) (for lofts), [Pull request \#5193](https   *//github.com/FreeCAD/FreeCAD/pull/5193) (for pipes) |
+++
| <img alt="" src=images/PD_Pad-Taper-angle_relnotes_0.20.png  style="width   *384px;">A tapered pocket within a non-tapered pad.                                                                                                                                             | The dialog for [Pad](PartDesign_Pad.md) and [Pocket](PartDesign_Pocket.md) offers to set a taper angle for the extrusion. [Pull request \#5357](https   *//github.com/FreeCAD/FreeCAD/pull/5357)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+++
| <img alt="" src=images/PD_Pocket-direction_relnotes_0.20.gif  style="width   *384px;">Pocketing along different directions.Click on the image to see the animation.                                                                                          | It is now possible to specify the direction for the pocket extrusion. [Pull request \#5164](https   *//github.com/FreeCAD/FreeCAD/pull/5164)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+++
| <img alt="" src=images/PartDesign_Cylinder_direction_relnotes_0.20.png  style="width   *384px;">                                                                                                                                                                                   | The dialog to edit [Cylinders](PartDesign_AdditiveCylinder.md) (additive and subtractive) now allows to specify an angle relative to the normal of the chosen attachment plane. This way one can create skew cylinders. [Pull request \#4708](https   *//github.com/FreeCAD/FreeCAD/pull/4708)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+++
| <img alt="" src=images/PartDesign_Helix_Growth_relnotes_0.20.png  style="width   *384px;">                                                                                                                                                                                               | The [Helix](PartDesign_AdditiveHelix.md) feature has the new mode **Height-Turns-Growth** to create flat spirals. [Forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=19&t=56378) [Pull request \#4590](https   *//github.com/FreeCAD/FreeCAD/pull/4590)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+++
| <img alt="" src=images/PartDesign_Islands-Extrude_relnotes_0.20.png  style="width   *384px;">A single Pad and a single [Revolution](PartDesign_Revolution.md) with nested profiles. The base block is only there to ensure that the part is a single solid. | All PartDesign features that can extrude sketches can now handle sketches with nested profiles that form islands. For example it is possible to revolve a sketch consisting of 3 nested circles with the same center point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                       | **Note**   * Extruding nested profiles only works if the result is still a single body. [Pull request \#6381](https   *//github.com/FreeCAD/FreeCAD/pull/6381)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+++
| <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width   *384px;">Effect of the new option *Length along sketch normal*.Click on the image to see the animation.                                                       | There is a new option to pad a certain length along the direction. The length is either measured along the sketch normal or along the custom direction. [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=50466), [Pull request \#3893](https   *//github.com/FreeCAD/FreeCAD/pull/3893)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+++
| <img alt="" src=images/PartDesign_Hole_thread_relnotes_0.20.PNG  style="width   *384px;">                                                                                                                                                                                                 | The [Hole](PartDesign_Hole.md) feature can now model true threads. [Forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=34&t=54240) [Pull request \#4274](https   *//github.com/FreeCAD/FreeCAD/pull/4274)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+++

### Otras mejoras de PartDesign 

-   In the [Helix](PartDesign_AdditiveHelix.md) feature one can now also use the sketch normal as axis. [Pull request \#5199](https   *//github.com/FreeCAD/FreeCAD/pull/5199)
-   The [Sprocket](PartDesign_Sprocket.md) feature can now also create ISO-normed sprockets. [Forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [Pull request \#4478](https   *//github.com/FreeCAD/FreeCAD/pull/4478)
-   The [Loft](PartDesign_AdditiveLoft.md) and [Pipe](PartDesign_AdditivePipe.md) features now allow using the body\'s faces for sections. [Pull request \#5155](https   *//github.com/FreeCAD/FreeCAD/pull/5155)
-   It is now possible to select several faces before calling the [Pad](PartDesign_Pad.md) or [Pocket](PartDesign_Pocket.md) dialog. In this case the first selected face will be used to determine the default padding/pocketing direction. [commit d34a5616](https   *//github.com/FreeCAD/FreeCAD/commit/d34a5616a2b38c96ad05f9a0763ba7504dfb814d)
-   It is possible to offset [SubShapeBinders](PartDesign_SubShapeBinder.md) if they are based on edges, wires or faces. [Pull request \#6338](https   *//github.com/FreeCAD/FreeCAD/pull/6338)
-   [SubShapeBinders](PartDesign_SubShapeBinder.md) now have the *Refine* property like all other PartDesign objects. [Pull request \#6550](https   *//github.com/FreeCAD/FreeCAD/pull/6550)
-   In the [Chamfer](PartDesign_Chamfer.md) and [Fillet](PartDesign_Fillet.md) dialogs all edges of a body can be selected via the context menu while in Add mode. [Pull request \#5269](https   *//github.com/FreeCAD/FreeCAD/pull/5269)
    When you selected a 3D object before clicking the icon to create a fillet or chamfer, all object edges will automatically be selected. [Pull request \#5328](https   *//github.com/FreeCAD/FreeCAD/pull/5328)
-   [Chamfer](PartDesign_Chamfer.md) and [Fillet](PartDesign_Fillet.md) dialogs now each have a new Use all edges checkbox, which is connected to the Use All Edges property for these objects. When the box is checked the property is set to True, when unchecked the property is set to False. When Use All Edges is True there is protection against the [topological naming problem](Topological_naming_problem.md) because then all of the edges of the base object are used regardless of how many edges there are. [Pull request \#5340](https   *//github.com/FreeCAD/FreeCAD/pull/5340)
-   Plane selection when [adding a new sketch](PartDesign_NewSketch.md) can now be achieved with a single-click in the 3D View. [Pull request](https   *//github.com/FreeCAD/FreeCAD/pull/5408) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=19&t=65020)
-   When a PartDesign tool is run without an active body, FreeCAD now offers to activate a body or create a new one. [Pull request \#4949](https   *//github.com/FreeCAD/FreeCAD/pull/4949)
-   The [Face Colors](Part_FaceColors.md) tool is now also available from the PartDesign workbench.

## Ambiente de Trabajo Trayectoria 

-   The Extensions feature was added to the [Adaptive](Path_Adaptive.md) operation. [Pull request \#4388](https   *//github.com/FreeCAD/FreeCAD/pull/4388)
-   The [Helix](Path_Helix.md) operation was refactored and Extra offset property was added to it. [Pull request \#5405](https   *//github.com/FreeCAD/FreeCAD/pull/5405)
-   The check if the current schema is using minutes for velocity expression and appropriate warning were added. [Pull request \#6357](https   *//github.com/FreeCAD/FreeCAD/pull/6357)
-   External threads were added to the thread milling operation. [Pull request \#6485](https   *//github.com/FreeCAD/FreeCAD/pull/6485)
-   The stability of engraving on sketches was improved. [Pull request \#6394](https   *//github.com/FreeCAD/FreeCAD/pull/6394)
-   The visibility of path objects was made more natural. [Pull request \#4911](https   *//github.com/FreeCAD/FreeCAD/pull/4911)

## Plot module 

-   FreeCAD now provides the Plot module by default, so any other module/workbench may create plots without requiring external tools [Pull request \#4971](https   *//github.com/FreeCAD/FreeCAD/pull/4971).

## Render Workbench 

## Ambiente de Trabajo Croquizador 

   
  <img alt="" src=images/SketcherSplitExample2_relnotes_0.20.png )                                                  New ![](images/Sketcher_Split.svg  style="width   *24px;"> [Split](Sketcher_Split.md) function to split existing lines or arcs. [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=55412) [Pull request \#4420](https   *//github.com/FreeCAD/FreeCAD/pull/4420)
  <img alt="" src=images/SketcherCreateRoundedRectangleExample_relnotes_0.20.png )                  New ![](images/Sketcher_CreateOblong.svg  style="width   *24px;"> [Rounded rectangle](Sketcher_CreateOblong.md) tool to create rectangles with rounded corners. [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main Pull request \#4835](https   *//github.com/FreeCAD/FreeCAD/pull/4835)
  <img alt="" src=images/SketcherCreateCenteredRectangleExample_relnotes_0.20.png  style="width   *384px;">   New <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width   *24px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md) tool to define rectangles via a center point. [Main commit](https   *//github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)
  <img alt="" src=images/Radiam_anim_relnotes_0.20.gif )                                                                      New ![](images/Sketcher_ConstrainRadiam.svg  style="width   *24px;"> [Radiam](Sketcher_ConstrainRadiam.md) function to automatically assign weight on B-spline pole, diameter on complete circle, or radius on arc. Support multi-selection as diameter/radius tools. [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Main Pull request \#4855](https   *//github.com/FreeCAD/FreeCAD/pull/4855)
  <img alt="" src=images/SketcherRemoveAxesAlignmentResult_relnotes_0.20.png )                          New ![](images/Sketcher_RemoveAxesAlignment.svg  style="width   *24px;"> [Remove Axes Alignment](Sketcher_RemoveAxesAlignment.md) constraint tool to remove axes alignment while trying to preserve the constraint relationship of the selection. [Main commit](https   *//github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)
  ![](images/SketcherSnapSlot_relnotes_0.20.gif )                                                            [Slots](Sketcher_CreateSlot.md) can be constrained horizontally or vertically either by snapping it manually with the **Ctrl** key, or by using the **Auto constraints** option of Sketcher. [Pull request \#5200](https   *//github.com/FreeCAD/FreeCAD/pull/5200)
  <img alt="" src=images/SketcherBSplineInsertKnot_relnotes_0.20.gif  style="width   *384px;">                             New <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width   *24px;"> [Insert Knot](Sketcher_BSplineInsertKnot.md) tool to insert a knot in an existing B-spline. [Pull request \#5311](https   *//github.com/FreeCAD/FreeCAD/pull/5311) and [Pull request \#6356](https   *//github.com/FreeCAD/FreeCAD/pull/6356)
   

### Otras mejoras de Sketcher 

-   Refactored Trim support. [Pull request \#4330](https   *//github.com/FreeCAD/FreeCAD/pull/4330) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=54441) \<\-- Needs screencasts
-   The behavior of the <img alt="" src=images/Sketcher_CreateSlot.svg  style="width   *24px;"> [Slot](Sketcher_CreateSlot.md) tool has changed. Slots can now be created by defining the center of both semicircles. [Pull request](https   *//github.com/FreeCAD/FreeCAD/pull/4843) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   Visibility automation allows to open Sketcher in [Section mode](Sketcher_ViewSection.md) when entering edit mode. [Pull request \#4742](https   *//github.com/FreeCAD/FreeCAD/pull/4742) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   Visibility automation allows to force camera in [Orthographic mode](Std_OrthographicCamera.md) when entering edit mode. [Pull request \#4778](https   *//github.com/FreeCAD/FreeCAD/pull/4778) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=44747)
-   Option to display the dimensional constraint name and use a custom format for it. [Pull request \#4966](https   *//github.com/FreeCAD/FreeCAD/pull/4966) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?t=61153)
-   When sketching a [3-point arc](Sketcher_Create3PointArc.md) with Autoconstraint enabled, [tangent constraint](Sketcher_ConstrainTangent.md) is proposed for all 3 points when hovering a line/curve. [Pull request \#4945](https   *//github.com/FreeCAD/FreeCAD/pull/4945) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=60596&p=520217#p520209)
-   Radius/diameter constraints are displayed using an angular rotation to ease visualization. Angle and optional randomness are user settable through parameters documented in [Fine-tuning](Fine-tuning.md). [Pull request \#4934](https   *//github.com/FreeCAD/FreeCAD/pull/4934) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=60370)
-   It is now possible to fix the angle of the direction when using the [Rectangular array](Sketcher_RectangularArray.md) tool. [commitc9eaa239](https   *//github.com/FreeCAD/FreeCAD/commit/c9eaa239) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?p=535691#p535691)
-   It is now possible to fix the angle of the direction when using the tools [Clone](Sketcher_Clone.md), [Copy](Sketcher_Copy.md) and [Move](Sketcher_Move.md). [commit](https   *//github.com/FreeCAD/FreeCAD/commit/6e4a09f569cf) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=62799)
-   By right-clicking a sketch in the Tree view you will now get a context menu entry \"Attachment editor\" that opens the [Attachment dialog](Part_EditAttachment.md) to modify the attachment. [commit c3511ba2f0](https   *//github.com/FreeCAD/FreeCAD/commit/c3511ba2f0)
-   Constraint selection is disabled when using a geometry or constraint tool. It can also be disabled manually at any time by pressing **Shift** key. [Pull request \#5398](https   *//github.com/FreeCAD/FreeCAD/pull/5398) [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=65465)
-   A versatile view filter has been added in the Sketcher task panel to ease constraints visibility management [Forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=60569)
-   It is now possible to set the degree of a B-Spline ([Pull request \#6463](https   *//github.com/FreeCAD/FreeCAD/pull/6463)) and undo the last defined control point ([Pull request \#6476](https   *//github.com/FreeCAD/FreeCAD/pull/6476)) at creation time.

## Ambiente de Trabajo Hoja de cálculo 

   
  <img alt="" src=images/Spreadsheet-Preferences-Spreadsheet_relnotes_0.20.png )   The workbench now has ![](images/Std_DlgPreferences.svg  style="width   *24px;"> [Preferences](Spreadsheet_Preferences.md). They are used by the <img alt="" src=images/Spreadsheet_Import.svg  style="width   *16px;"> [Spreadsheet Import](Spreadsheet_Import.md) and <img alt="" src=images/Spreadsheet_Export.svg  style="width   *16px;"> [Spreadsheet Export](Spreadsheet_Export.md) commands. [Pull request \#5073](https   *//github.com/FreeCAD/FreeCAD/pull/5073)
   

-   It is now possible to select in the row/column context-menu at what positions new rows/columns will be inserted. [Pull request \#4704](https   *//github.com/FreeCAD/FreeCAD/pull/4704).

### Further Spreadsheet improvements 

-   Import XLSX (used by [Std Import](Std_Import.md))   * Added support for floor and ceil functions. [Pull request \#5015](https   *//github.com/FreeCAD/FreeCAD/pull/5015).
-   Cell binding   * instruct a set of cells to display the contents of another set of cells. Part of [Pull request \#2862](https   *//github.com/FreeCAD/FreeCAD/pull/2862).
-   Improved navigation using the **Tab** and **Enter** keys.
-   Improved interface for cutting and pasting blocks of cells.

## Ambiente de Trabajo Inicio 

## Ambiente de Trabajo Superficie 

## Ambiente de Trabajo DibujoTécnico 

   
  <img alt="" src=images/TechDraw_ExtensionExample_relnotes_0.20.png  style="width   *400px;">   More than 30 new tools, so-called [Extensions](TechDraw_Workbench#Extensions.md), are now available. They offer new cosmetic features to enhance drawings.
   

### Otras mejoras de TechDraw 

-   It is now possible to [Share](TechDraw_ShareView.md) and [Move](TechDraw_MoveView.md) [Views](TechDraw_Workbench#Views.md) between pages.
-   When there are several [Pages](TechDraw_PageDefault.md) and a [View](TechDraw_View.md), [ProjectionGroup](TechDraw_ProjectionGroup.md) etc. is added, there is now a dialog to ask to what page the view should be added. [Pull request \#5309](https   *//github.com/FreeCAD/FreeCAD/pull/5309).
-   A new format specifier *%w* was added to print the given number of digits after dot and remove any trailing zeros. [Pull request \#5401](https   *//github.com/FreeCAD/FreeCAD/pull/5401).
-   The new *%w* format specifier is now the default. And the format specifier preference was moved from the Advanced tab to the Dimension tab. [Pull request \#6504](https   *//github.com/FreeCAD/FreeCAD/pull/6504).
-   Flipped diagonal hatch was added for the [Geometric Hatch](TechDraw_GeometricHatch.md) tool. [Pull request \#6429](https   *//github.com/FreeCAD/FreeCAD/pull/6429).
-   There is a new option to show a grid in a [page](TechDraw_PageDefault.md). Several related [preferences](TechDraw_Preferences#Grid.md) have been introduced. [Pull request \#6465](https   *//github.com/FreeCAD/FreeCAD/pull/6465).
-   The unit display in dimensions was fixed according to standards. The degree symbol is always present for the dimension value and tolerances, other units only appear if ShowUnits is set. The unit appears immediately after the dimension value unless there is a tolerance, then it appears after the tolerance. [Pull request \#6581](https   *//github.com/FreeCAD/FreeCAD/pull/6581)

## Web

Qt WebEngine is now considered the default option instead of Qt WebKit.

## Entornos de trabajo externos 


**Note   ***

these are the new workbenches created in this development cycle, or older workbenches that received updates. See [external workbenches](External_workbenches.md) for more workbenches that can be installed, and which cover a wide variety of topics. If you want to see your workbench added, join the [forum](https   *//forum.freecadweb.org/index.php) and present your code.

### 3D Printing Tools 

### A2plus

## Ensamblaje3

## Ensamblaje4

### ArchTextures

### BOLTSFC

### CurvedShapes Workbench 

### Dodo (formerly Flamingo) 

### Elementos de Unión 

### FCGear

The [FCGear Workbench](FCGear_Workbench.md) received a couple of improvements

-   For involute gears, the outside (aka tip) and root diameter are exposed as properties ([details](https   *//github.com/looooo/freecad.gears/pull/69))
-   Gear objects are now [attachable](Part_EditAttachment.md) ([details](https   *//github.com/looooo/freecad.gears/pull/72))
-   Gear objects can now be used as additive features in PartDesign Bodies ([details](https   *//github.com/looooo/freecad.gears/pull/74))
-   The creation of gear objects now appears in the undo stack ([details](https   *//github.com/looooo/freecad.gears/pull/83))

### MeshRemodel Workbench 

### MOOC Workbench 

### NodeEditor (PyFlow) 

### Plot

-   The Plot module has been stripped from the workbench since it is now provided by FreeCAD.

### Ship

The [Ship Workbench](Ship_Workbench.md) is back to life!

-   A new tool to compute the [static sink and trim](https   *//github.com/FreeCAD/freecad.ship#static-sink-and-trim) has been added.
-   A new tool to compute the [response amplitude operators](https   *//github.com/FreeCAD/freecad.ship#raos) has been added on top of [capytaine](https   *//github.com/mancellin/capytaine).

### Trails, PyTrails, Turns, pivy\_trackers, and Geomatics 

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.20/es
