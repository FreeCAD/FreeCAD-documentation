# Release notes 0.20/es
**FreeCAD 0.20** fue liberado el **14 de junio del 2022**, consíguelo desde la página [Descarga](Download/es.md). Este es un resumen de las nuevas características y los cambios más interesantes.

Las notas de lanzamiento de versiones anteriores de FreeCAD se pueden encontrar en la [Lista de características](Feature_list/es#Notas_de_lanzamiento.md).

+++
| ![](images/FreeCAD_highlight_relnotes_0.20.gif ) | *Modelo de un motor CD 775 por el usuario \"jimmihenry\", ver [Users Showcase](https://forum.freecadweb.org/viewtopic.php?p=551765#p551765).El modelo fue hecho completamente con las [versiones de desarrollo](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) de FreeCAD 0.20. Las imágenes para el gráfico animado fueron hechas con la macro de FreeCAD [ Screen Wiki](Macro_Screen_Wiki.md). El GIF animado en sí fue creado usando [GIMP](https://en.wikipedia.org/wiki/GIMP). Para las notas de lanzamiento fue redimensionado usando [ezgif](https://ezgif.com/crop).* |
+++

## General

### freecad.org

Estamos contentos de que el proyecto [KiCad](https://www.kicad.org/), a través de [KiCad Services Corp.](https://www.kipro-pcb.com/), nos patrocinó el dominio freecad.org. Ahora todos los sitios web de FreeCAD están disponibles en [freecadweb.org](https://freecadweb.org) y [freecad.org](https://freecad.org).



### Seguimiento de problemas/bugs 

El seguimiento de problemas de FreeCAD se ha movido a GitHub: <https://github.com/FreeCAD/FreeCAD/issues>

**Nota:** Solo se considerarán los informes de errores con una discusión del foro anterior. Los informes sin esto serán cerrados.



### Nuevo sistema de ayuda 

El sistema de ayuda ha sido reescrito y actualizado para mostrar información directamente de nuestra [Wiki](User_hub.md). El sistema ahora confía en el [Complemento de Ayuda](https://github.com/FreeCAD/FreeCAD-Help). Cuando usas por primera vez la herramienta de [Ayuda](Std_Help.md) o la herramienta de [¿Qué es esto?](Std_WhatsThis.md) se le pedirá instalarlo.



## Interfaz de usuario 

+++
| ![](images/Navi_Cube_relnotes_0.20.gif ) | El cubo de navegación fue reelaborado:                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                | -   Ahora hay caras en las aristas para rotar la escena 45°.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                | -   Una preferencia nueva [Girar al más cercano](Preferences_Editor#Navigation.md) ha sido introducida. Si se selecciona, la escena 3D es rotada a la posición más cercana lógica basada en la orientación actual del cubo al dar clic en una cara del cubo. De lo contrario, hacer clic en una cara siempre dará como resultado la misma rotación. Pruebe la misma secuencia de clics que en la animación con y sin la opción *Girar al más cercano* para experimentar la diferencia. |
|                                                                | -   Al hacer clic en el nuevo botón redondo en la parte superior derecha del cubo, puede cambiar rápidamente a la vista posterior de la escena actual.                                                                                                                                                                                                                                                                                                                                         |
|                                                                | -   El tamaño del cubo ahora puede ser ajustado en la opción de preferencias [Tamaño del cubo](Preferences_Editor#Navigation.md).                                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                | [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=3&t=52118), [Pull request #4502](https://github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                            |
+++

+++
| ![](images/Improved_tooltips_relnotes_0.20.gif ) | La información sobre herramientas ahora muestra el nombre del comando en el título, lo que facilita que los nuevos usuarios busquen ayuda. Al final de la información sobre herramientas, el nombre del comando \"interno\" se agrega entre paréntesis: *(Std_WhatsThis)*. Este es también el nombre de la página que documenta el comando en la Wiki. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=34&t=58747), [Pull request #4978](https://github.com/FreeCAD/FreeCAD/pull/4978). |
+++

+++
| <img alt="" src=images/Std_UserEditMode_relnotes_0.20.gif  style="width:384px;"> | El nuevo comando [Std UserEditMode](Std_UserEditMode.md) permite al usuario elegir un modo de edición que será usado al dar doble clic a un objeto en la [vista de árbol](Tree_view.md). Dé clic en la imagen de la izquierda para ver una animación de la selección. Si un modo de edición no es aplicable, el modo de edición por defecto de del objeto es usado en su lugar. [Pull request #5110](https://github.com/FreeCAD/FreeCAD/pull/5110). |
+++

+++
| ![](images/Dependencies-selection_relnotes_0.20.png ) | El menú contextual de la [vista de árbol](Tree_view.md) tiene la nueva entrada **Añadir objetos dependientes a la selección**. |
|                                                                                          | [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=8&t=13566), [Pull request #4133](https://github.com/FreeCAD/FreeCAD/pull/4133).              |
|                                                                                          |                                                                                                                                                                  |
|                                                                                          | En la imagen se seleccionó el objeto *Hole001* y luego                                                                                                           |
|                                                                                          | se agregaron sus dependencias a la selección a través del menú contextual.                                                                                       |
+++

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.20.png  style="width:200px;"> | La nueva herramienta [Corte de sección](Part_SectionCut.md) permite tener cortes no huecos y también persistentes de piezas y ensamblajes.   |
|                                                                                                         | [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=27&t=52441), [Pull request #4118](https://github.com/FreeCAD/FreeCAD/pull/4118). |
+++



### Otras mejoras de la interfaz de usuario 

-   Ahora es posible utilizar el separador decimal perteneciente al idioma especificado para la interfaz de FreeCAD. Por ejemplo, en un Windows alemán, cuando establece el idioma de la interfaz en **Inglés** y selecciona la nueva opción **Usar formato de número de idioma seleccionado**, el punto se utilizará como separador decimal. Consulte [Preferencias](Preferences_Editor#General.md). [Pull request #6364](https://github.com/FreeCAD/FreeCAD/pull/6364)**Nota**: Para simulaciones [FEM](FEM_Workbench.md), usar el punto como separador decimal es muy recomendado para obtener resultados correctos.
-   Se han agregado dos nuevos estilos de navegación con el mouse. Uno basado en [OpenSCAD](Mouse_navigation#OpenSCAD_navigation.md), el otro en [TinkerCAD](Mouse_navigation#TinkerCAD_navigation.md). [Discusión en el foro OpenSCAD](https://forum.freecadweb.org/viewtopic.php?f=8&t=60975), [Discusión en el foro TinkerCAD](https://forum.freecadweb.org/viewtopic.php?p=544639#p544376), [commit 1](https://github.com/FreeCAD/FreeCAD/commit/a1c9ab658c), [commit 2](https://github.com/FreeCAD/FreeCAD/commit/ef100d55e9d50), [commit 3](https://github.com/FreeCAD/FreeCAD/commit/549e5b5650).
-   Ahora es posible desplazar la vista del [gráfico de dependencia](Std_DependencyGraph.md) con el mouse. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=3&t=34791), [Pull request #4638](https://github.com/FreeCAD/FreeCAD/pull/4638).
-   Se solucionó un problema por el cual al usar una pluma para tablet (por ejemplo, tablet Wacom) era lento hasta el punto de ser completamente inutilizable. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=8&t=45046), [Pull request #4687](https://github.com/FreeCAD/FreeCAD/pull/4687).
-   El sistema de coordenadas en la vista 3D se puede cambiar de tamaño en las preferencias en la sección [Mostrar → Vista 3D](Preferences_Editor#3D_View.md). [Pull request #5182](https://github.com/FreeCAD/FreeCAD/pull/5182)
-   Una nueva configuración en [Preferencias → General](Preferences_Editor#General.md) permite sustituir el separador decimal del teclado numérico con el separador local apropiado si son diferentes. [Pull request #3256](https://github.com/FreeCAD/FreeCAD/pull/3256) [Pull request #5150](https://github.com/FreeCAD/FreeCAD/pull/5150) [Pull request #5203](https://github.com/FreeCAD/FreeCAD/pull/5203)
-   Ahora es posible configurar la tecla **Retroceso** como un atajo de tecla independiente sin necesidad de especificar una tecla modificadora adicional. [Pull request #5428](https://github.com/FreeCAD/FreeCAD/pull/5428)



## Núcleo del sistema y API 



### Núcleo

+++
| <img alt="" src=images/Object_selection_relnotes_0.20.png  style="width:384px;"> | Cuando se utiliza **Editar → Copiar** o **Editar → Duplicar selección** para un objeto con dependencias hay un botón nuevo **Usar selecciones originales** en el diálogo de selección de objetos. Haga clic en este botón para copiar/duplicar únicamente los objetos que seleccionó originalmente antes de abrir el cuadro de diálogo, ignorando las dependencias e ignorando cualquier acción que pudiera haber sido realizada mientras el cuadro de diálogo estaba abierto, como marcar o desmarcar algunas de las casillas de verificación. El efecto es el mismo a que si hubiera desmarcado todas las casillas de verificación junto a los objetos que no seleccionó originalmente y hubiera pulsado OK. Nota: hay que tener especial cuidado al copiar/duplicar las páginas de TechDraw. Se recomienda copiar/duplicar también todos los hijos de la página (plantillas, vistas, dimensiones, etc.). De lo contrario, los cambios en una página afectarán a las otras. Por ejemplo, al eliminar la Vista de una página también se eliminará de la otra, o eliminar una página también eliminará todo el contenido de la otra página. |
+++

+++
| <img alt="" src=images/PrefPacks_relnotes_0.20.png  style="width:384px;"> | Se agregó un nuevo tipo de complemento llamado [Paquete de preferencias](Preference_Packs.md), que permite a un subconjunto de las preferencias de un usuario (user.cfg) ser guardadas, distribuidas y aplicadas fácilmente por otros usuarios. Los paquetes de preferencias se pueden usar para distribuir \"Temas\", por ejemplo, al permitir que un desarrollador incluya tanto una hoja de estilo Qt para widgets así como un conjunto de otros colores y estilos para elementos en la interfaz de usuario que no se pueden configurar usando una hoja de estilo ( por ejemplo, colores de texto en el editor de Python o en la vista de informe, etc.). Todo lo que se puede configurar a través de un archivo user.cfg se puede configurar mediante un paquete de preferencias. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=17&t=62477) |
+++

+++
| <img alt="" src=images/Autoload_relnotes_0.20.png  style="width:384px;"> | El panel de preferencias de los \"Entornos de trabajo\" fue modificado para permitir cargar automáticamente los entornos de trabajo mientras FreeCAD inicia. |
+++

En Linux, la ubicación por defecto de los archivos de configuración de FreeCAD, datos y caché fue cambiada para seguir la [Especificación de Directorios Base XDG](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html). [Discusión del foro](https://forum.freecadweb.org/viewtopic.php?f=9&t=63648). Aquí hay una comparación de las ubicaciones anteriores y nuevas:

  Descripción                 Ubicación anterior   Ubicación nueva             Por defecto a
     
  Archivos de configuración   \$HOME/.FreeCAD      \$XDG_CONFIG_HOME/FreeCAD   \$HOME/.config/FreeCAD
  Archivos de datos           \$HOME/.FreeCAD      \$XDG_DATA_HOME/FreeCAD     \$HOME/.local/share/FreeCAD
  Archivos de caché           /tmp                 \$XDG_CACHE_HOME/FreeCAD    \$HOME/.cache/FreeCAD

Si desea seguir utilizando las ubicaciones anteriores, puede iniciar FreeCAD con la opción `--keep-deprecated-paths`.

### API

FreeCAD recibió muchas nuevas funciones de la API de Python:


<div class="mw-collapsible mw-collapsed toccolours">



#### Nueva API de Python 


<div class="mw-collapsible-content">

-   *ChFi2d_AnaFilletAlgoPy*: Un algoritmo analítico para el cálculo de filetes. [commit f94ab3ec](https://github.com/FreeCAD/FreeCAD/commit/f94ab3ec)
-   *ChFi2d_ChamferAPIPy*: Algoritmp que crea un chaflán entre dos aristas lineales. [commit 30f8015e7](https://github.com/FreeCAD/FreeCAD/commit/30f8015e7)

-   *Circle2dPy::getCircleCenter*: Obtiene el centro del círculo definido por tres puntos. [commit 3dc91fa2](https://github.com/FreeCAD/FreeCAD/commit/3dc91fa2)

-   *ComplexGeoDataPy::applyRotation*: Aplica una rotación adicional a la ubicación. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::applyTranslation*: Aplica una traslación adicional a la ubicación. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::countSubElements*: Devuelve el número de elementos de un tipo. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getElementTypes*: Devuelve una lista de los tipos de elementos. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getFaces*: Devuelve una tupla de puntos y triángulos con una exactitud dada. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getLines*: Devuelve una tupla de puntos y líneas con una exactitud dada. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getLinesFromSubelement*: Devuelve vértices y líneas de un subelemento. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getPoints*: Devuelve una tupla de puntos y normales con una exactitud dada. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::transformGeometry*: Aplica una transformación a la geometría subyacente. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)

-   *ControlPy::showModelView*: Muestra la vista del modelo. [commit 033bf619](https://github.com/FreeCAD/FreeCAD/commit/033bf619)

-   *DocumentPy::clearDocument*: Limpia todo el documento. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::getFileName*: Para un documento regular devuelve su propiedad de nombre de archivo. Para un documento temporal devuelve su directorio transitorio. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::getProgramVersion*: Obtiene la versión del programa con la que se creó un archivo de proyecto. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::isClosable*: Checa si el documento puede ser cerrado. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::isSaved*: Checa si el documento está guardado. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::isTouched*: Checa si algún objeto está en un estado de tocado. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::mustExecute*: Checa si algún objeto debe ser recalculado. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::purgeTouched*: Purga el estado tocado de todos los objetos. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::setClosable*: Establece una bandera que permite o prohíbe cerrar un documento. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)

-   *DrawPagePy::requestPaint*: Pinta una página de TechDraw. [commit 79f9fb68](https://github.com/FreeCAD/FreeCAD/commit/79f9fb68)

-   *HLRBRep_AlgoPy*: Para acceder a la eliminación de la línea oculta de la Parte (HLR). [commit 73a98671](https://github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *HLRBRep_PolyAlgoPy*: Para acceder a la poli-eliminación de la línea oculta de la Parte (HLR). [commit ea85cf5e](https://github.com/FreeCAD/FreeCAD/commit/ea85cf5e)
-   *HLRToShapePy*: Para acceder a la eliminación de la línea oculta de la Parte (HLR). [commit 73a98671](https://github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *PolyHLRToShapePy*: Para acceder a la poli-eliminación de la línea oculta de la Parte (HLR). [commit ea85cf5e](https://github.com/FreeCAD/FreeCAD/commit/ea85cf5e)

-   *MDIViewPy::printPdf*: Imprime un PDF. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::printPreview*: Imprime una vista previa. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::printView*: Imprime una vista. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::redoActions*: Rehace acciones. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::undoActions*: Deshace acciones. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)

-   *PrecisionPy*: Para acceder a la precisión definida por el kernel de OpenCascade. [commit 20b86e55](https://github.com/FreeCAD/FreeCAD/commit/20b86e55)

-   *PropertyContainerPy::setDocumentationOfProperty*: Establece la cadena de documentación de una propiedad dinámica de esta clase. [commit 8cf3cf33](https://github.com/FreeCAD/FreeCAD/commit/8cf3cf33)
-   *PropertyContainerPy::setGroupOfProperty*: Establece el nombre del grupo de una propiedad dinámica. [commit 8cf3cf33](https://github.com/FreeCAD/FreeCAD/commit/8cf3cf33)

-   *PythonWorkbenchPy::reloadActive*: Recarga el entorno de trabajo activo después de cambiar menús o barras de herramientas. [commit 0bbc253d](https://github.com/FreeCAD/FreeCAD/commit/0bbc253d)

-   *RotationPy::fromEuler*: Establece los ángulos de Euler de una rotación u obtiene los ángulos de Euler en una secuencia dada para una rotación. [commit 951a0be9](https://github.com/FreeCAD/FreeCAD/commit/951a0be9)
-   *RotationPy::toEulerAngles*: Obtiene los ángulos de Euler en una secuencia dada para esta rotación.. [commit c1454dfb](https://github.com/FreeCAD/FreeCAD/commit/c1454dfb)

-   *SpreadsheetViewPy*: Para acceder a las hojas de cálculo. [commit 6e713628](https://github.com/FreeCAD/FreeCAD/commit/6e713628)

-   *UnitsApi::sToNumber*: Convierte una cantidad o float a una cadena. [commit befbd95d](https://github.com/FreeCAD/FreeCAD/commit/befbd95d)

-   *View3DInventorPy::getCornerCrossSize*: Devuelve el tamaño actual de la cruz del eje de la esquina. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy::setPopupMenuEnabled*: Habilita un menú emergente. [commit 9def811a](https://github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy::isCornerCrossVisible*: Devuelve la visibilidad actual de de la cruz del eje de la esquina. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy::isPopupMenuEnabled*: Devuelve si el menú emergente está habilitado. [commit 9def811a](https://github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy::projectPointToLine*: Proyecta el punto 2D dado a una línea. [commit b6527a70](https://github.com/FreeCAD/FreeCAD/commit/b6527a70)
-   *View3DInventorPy::setCornerCrossSize*: Define el tamaño de la cruz del eje de la esquina. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy::setCornerCrossVisible*: Define la visibilidad de la cruz del eje de la esquina. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)

-   *ViewProviderSpreadsheetPy*: Para manejar celdas de hojas de cálculo.[commit 16bbe123](https://github.com/FreeCAD/FreeCAD/commit/16bbe123) and [commit 093f15dc](https://github.com/FreeCAD/FreeCAD/commit/093f15dc)


</div>



#### API de Python cambiada 

-   *MeshObject::trim(base, normal)* fue cambiado a *MeshPy::trimByPlane(base, normal)*: Recorta la malla con un plano dado. [commit 837de28e](https://github.com/FreeCAD/FreeCAD/commit/837de28e)


</div>



## Gestor de complementos 

+++
| <img alt="" src=images/AddonManagerExpanded_relnotes_0.20.png  style="width:400px;"> | El [Gestor de complementos](Std_AddonMgr.md) se modificó para permitir la distribución de paquetes de preferencias y para mostrar la información que se encuentra en los metadatos de los complementos. El gestor de complementos también incluye soporte mejorado para complementos cuyo código fuente se encuentra en varias ubicaciones de alojamiento git diferentes. Se mejoró el soporte de redes para proporcionar un manejo más sólido de las conexiones SSL y soporte para proxies que requieren autenticación. Se agregó soporte para agregar automáticamente botones de macro a la barra de herramientas después de la instalación, para deshabilitar complementos sin eliminarlos y para cambiar qué rama de git de un complemento es checada. Finalmente, se modificó la interfaz de usuario para mejorar la búsqueda y visualización de diferentes filtros de lista. |
+++



## Ambiente de Trabajo Arquitectura 

+++
| <img alt="" src=images/ArchWindow_Placement_1r_relnotes_0.20.png  style="width:250px;"> <img alt="" src=images/ArchWindow_Placement_2r_relnotes_0.20.png  style="width:250px;"> | **Entorno de trabajo SketchArch**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                 | Con la <img alt="" src=images/Attach_in_SketchArch.svg  style="width:20px;"> [Adjuntar característica](https://github.com/paullee0/FreeCAD_SketchArch) es ahora posible colocar <img alt="" src=images/Arch_Window.svg  style="width:20px;"> [Ventanas](Arch_Window.md) y <img alt="" src=images/Arch_Equipment.svg  style="width:20px;"> [Equipo](Arch_Equipment.md) parametricamente e intuitivamente en relación to <img alt="" src=images/Arch_Wall.svg  style="width:20px;"> [Muros](Arch_Wall.md). Para usar esta característica el entorno de trabajo experimental externo <img alt="" src=images/SketchArch_Workbench.svg  style="width:20px;"> [Entorno de trabajo SketchArch](https://github.com/paullee0/FreeCAD_SketchArch) debe de ser instalado. [Complemento y leéme en Github](https://github.com/paullee0/FreeCAD_SketchArch) (No está disponible aún en el [gestor de complements](Std_AddonMgr.md)). |
|                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                 | [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=23&t=50802)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+++

+++
| <img alt="" src=images/NewArchStructureProperties_relnotes_0.20.jpg  style="width:250px;"> | **Nuevas propiedades para los objetos de estructura de Arch**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               | -   **BasePerpendicularToTool**: crea una copia de la Base (perfil de extrusión) al inicio de la herramienta (trayectoria de extrusión) y la coloca perpendicular a la primera arista de la herramienta. Es lo mismo que adjuntar la Base con MapMode=NormalToEdge, pero es automático y permite reutilizar el mismo objeto Base para múltiples Estructuras. Cuando BasePerpendicularToTool = True, hay más propiedades que controlan la colocación de la Base en relación con el eje de la Herramienta. Se muestran en la imagen adjunta.                                                                       |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               | -   **ToolOffsetFirst** y **ToolOffsetLast**: extiende/recorta la estructura al principio y al final respectivamente (la longitud real de la estructura está disponible en la propiedad de solo lectura ComputedLength).                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               | -   **BaseRotation**: rota la Base (la rotación es alrededor del punto \"(0,0)\" de la Base que es el centro para [Perfil de Arch](Arch_Profile.md), el origen para los croquis y usualmente el primer punto para [Draft Wires](Draft_Wire.md)).                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               | -   **BaseOffsetX** and **BaseOffsetY**: mueve la Base (perfil de extrusión).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               | -   **BaseMirror**: refleja la Base (perfil de extrusión).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               | También se ha añadido un nuevo comando **Crear estructura de arco múltiple**. Utiliza el primer objeto seleccionado como Base, y crea objetos de Estructuras de Arco para cada Arista de los otros objetos seleccionados. A continuación, las propiedades de los objetos de estructura individuales pueden ajustarse en el editor de propiedades. Este comando se ha añadido para el flujo de trabajo con un croquis maestro (existe el riesgo de que se produzcan problema de denominación topológica a menos que se cree una copia no paramétrica del croquis maestro o se utilice la versión de Realthunder). |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               | El soporte para **Datos 2D**, como el trabajo de línea, el achurado, los textos y las dimensiones, ahora está habilitado en la importación y exportación IFC, lo que contribuye a hacer al formato IFC cada vez más adecuado para el trabajo CAD 2D tradicional. Se está haciendo un esfuerzo similar en [BlenderBIM](https://blenderbim.org). Más mejoras en el flujo de trabajo 2D están documentadas [en este hilo del foro](https://forum.freecadweb.org/viewtopic.php?p=563067#p563067).                                                                                                                    |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                               | [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=23&t=43228&start=60), [Pull request #3229](https://github.com/FreeCAD/FreeCAD/pull/3229)                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+++



## Ambiente de Trabajo Draft 

-   Se agregó una casilla de verificación **Global** al panel de tareas de muchos comandos de dibujo. Marcarla permite introducir coordenadas en el sistema global de coordenadas incluso si el [plano de trabajo](Draft_SelectPlane.md) no está alineado con el plano global XY.

-   Se introdujo el comando <img alt="" src=images/Draft_Hatch.svg  style="width:24px;"> [Draft Hatch](Draft_Hatch.md). Crea sombreados en las caras de un objeto seleccionado utilizando patrones de archivos PAT de AutoCAD.

-   Se introdujo el comando <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:24px;"> [Draft AddNamedGroup](Draft_AddNamedGroup.md). El comando <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> [Draft AddToGroup](Draft_AddToGroup.md) fue extendido con la misma funcionalidad.

-   El trabajo en el comando <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> [Draft SetStyle](Draft_SetStyle.md), que estaba en progreso en FreeCAD versión 0.19, fue completado.

-   Se ha añadido una opción de edición con doble clic para <img alt="" src=images/Draft_Text.svg  style="width:24px;"> [Texto de Draft](Draft_Text.md). Abre el mismo panel de tareas de edición utilizado al crear un texto.

-   Para <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Dimensiones de Draft](Draft_Dimension.md) la {{Value|arch}} **Sobreescritura de unidades** para las dimensiones arquitectónicas imperiales fue introducido.

-   Los objetos <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> [Draft Shape2DView](Draft_Shape2DView.md) ahora tienen una propiedad de **Auto actualización**. Ponerlo en {{False}} puede ser útil si hay muchos Draft Shape2DViews en un documento o si son complejos.

-   Ahora es posible revertir un [Draft Wire](Draft_Wire.md) a través del menú contextual <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> [Draft Edit](Draft_Edit.md). [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [Pull request #4811](https://github.com/FreeCAD/FreeCAD/pull/4811).



### Otras mejoras de Draft 

-   Se arregló [Draft Snap Grid](Draft_Snap_Grid.md) cuando el cursor está sobre una cara. [Discusión en el foro](https://forum.freecad.org/viewtopic.php?f=23&t=62274). [Git commit](https://github.com/FreeCAD/FreeCAD/commit/1761eb8ce).

-   Los nuevos [Textos de Draft](Draft_Text.md) ahora son alineados con el [plano de trabajo](Draft_SelectPlane.md), [Pull request #5092](https://github.com/FreeCAD/FreeCAD/pull/5092).

-   Se ha añadido soporte para dos convertidores DWG: [LibreDWG](https://www.gnu.org/software/libredwg) y [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg). Vea [Preferencias de importación y exportación](Import_Export_Preferences#DWG.md) y [FreeCAD y la importación de DWG](FreeCAD_and_DWG_Import.md) para más información.



## Ambiente de Trabajo FEM 

   
  <img alt="" src=images/FEM_Z88-settings_relnotes_0.20.png  style="width:384px;">Las nuevas configuraciones de Z88 y sus valores por defecto.                                                                          El [solucionador Z88](FEM_SolverZ88.md) ahora es totalmente usable. Puede especificar el método del solucionador y cambiar la configuración de la memoria. Los nuevos valores por defecto le permiten realizar también simulaciones complejas directamente. [commit d035bbc1ca y siguientes](https://github.com/FreeCAD/FreeCAD/commit/d035bbc1ca)
  <img alt="" src=images/FEM_buckling-analysis_relnotes_0.20.gif  style="width:384px;">Resultado de un análisis de pandeo lineal.Clic en la imagen para ver la animación.                            Ahora es posible realizar análisis de pandeo utilizando el solucionador [Calculix](FEM_SolverCalculixCxxtools.md). [Pull request #4379](https://github.com/FreeCAD/FreeCAD/pull/4379)
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature_relnotes_0.20.png  style="width:384px;">Efecto de *Tamaño de malla desde curvatura*; izquierda: puesto a 12, derecha: desactivado                 Hay una nueva propiedad para el creador de mallas [Gmsh](FEM_MeshGmshFromShape.md). Se puede especificar el número de elementos de malla por $2\pi$ veces el radio de la curvatura. El valor por defecto es 12 y para obtener una malla más fina en las esquinas o agujeros pequeños, este valor se puede aumentar para obtener mejores resultados. Esta característica requiere Gmsh 4.8 o más reciente. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=18&t=56401), [Pull request #4596](https://github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm_relnotes_0.20.png  style="width:384px;">Efecto del algoritmo de recombinación; izquierda: usando *Simple*, derecha: usando *Simple full-quad*   FreeCAD permite ahora seleccionar un algoritmo así como la recombinación de mallas 3D para el creador de mallas [Gmsh](FEM_MeshGmshFromShape.md). Para más detalles acerca de la recombinación de elementos de malla vea [FEM MeshGmshFromShape](FEM_MeshGmshFromShape#Element_Recombination.md). [Pull request #4706](https://github.com/FreeCAD/FreeCAD/pull/4706)
   



### Otras mejoras de FEM 

-   **Importante:** A partir de esta versión, FreeCAD utilizará [las unidades del SI](https://en.wikipedia.org/wiki/International_System_of_Units) (m, kg, s, K, A, mol, cd) para escribir los archivos de entrada [Solucionador Elmer](FEM_SolverElmer.md) (*case.sif* y *mesh.nodes*). Esto es independiente del [Sistema de unidades](Preferences_Editor#Units.md) de FreeCAD.
-   **Importante:** A partir de esta versión, la escala de [resultados de pipelines](FEM_PostPipelineFromResult.md) y sus [filtros](FEM_Workbench#Menu__Results.md) usarán las unidades del SI (m, kg, s, K , A, mol, cd). Entonces el desplazamiento se da en metros, la tensión en Pascal. Esto se aplica a todos los [sistemas de unidades](Preferences_Editor#Units.md) derivados del SI FreeCAD .
-   Resolver con el solucionador [Calculix](FEM_SolverCalculixCxxtools.md) ahora usa todos los núcleos de la CPU. [Pull request #6374](https://github.com/FreeCAD/FreeCAD/pull/6374)
-   Hacer mallas con [Gmsh](FEM_MeshGmshFromShape.md) ahora usa todos los núcleos de la CPU. [Pull request #6370](https://github.com/FreeCAD/FreeCAD/pull/6370)
-   El orden de los elementos de las mallas [Gmsh](FEM_MeshGmshFromShape.md) se puede cambiar a través de la ventana de diálogo de malla. [Pull request #4660](https://github.com/FreeCAD/FreeCAD/pull/4660)
-   El resultado del filtro [Clip de datos en el punto](FEM_PostFilterDataAtPoint.md) ahora está funcionando: Uno obtiene información de las mallas de resultados haciendo clic en ellas o especificando una coordenada de malla.
-   Se agregó una nueva restricción: **Modelo → Restricciones mecánicas → [<img src=images/FEM_ConstraintCentrif.svg style="width:16px"> [Restricción centrífuga](FEM_ConstraintCentrif.md)**. [Pull request #4738](https://github.com/FreeCAD/FreeCAD/pull/4738)
-   Se agregó un nuevo solucionador: **Solve → [<img src=images/FEM_SolverMystran.svg style="width:16px"> [Solucinoador Mystran](FEM_SolverMystran.md)**. Multiple commits.
-   Se agregó una nueva restricción: **Modelo → Restricciones mecánicas → [<img src=images/FEM_ConstraintSpring.svg style="width:16px"> [Restricción de resorte](FEM_ConstraintSpring.md)**. [Pull request #4982](https://github.com/FreeCAD/FreeCAD/pull/4982)
-   Ahora es posible tener [resultados de pipelines](FEM_PostPipelineFromResult.md) con varios filtros, donde algunos toman otros filtros como entrada, y algunos toman los resultados directamente del pipeline. [commit 708a300b](https://github.com/FreeCAD/FreeCAD/commit/708a300b)
-   Las tarjetas de materiales ahora pueden contener valores para la conductividad eléctrica. [Pull request #4647](https://github.com/FreeCAD/FreeCAD/pull/4647)
-   Se agregaron tarjetas de materiales para nitrógeno y argón. [Pull request #4649](https://github.com/FreeCAD/FreeCAD/pull/4649)
-   Se agregó soporte para los algoritmos de malla [Gmsh](FEM_MeshGmshFromShape.md) *HXT* (3D) y *Packing Parallelograms* (2D). [Pull request #4654](https://github.com/FreeCAD/FreeCAD/pull/4654)
-   Se permite especificar un algoritmo para la propiedad **High Order Optimize** [Gmsh](FEM_MeshGmshFromShape#Properties.md) . [Pull request #4705](https://github.com/FreeCAD/FreeCAD/pull/4705)
-   Los materiales sólidos no lineales con endurecimiento simple ahora pueden tener un número arbitrario de puntos de fluencia. [Pull request #5024](https://github.com/FreeCAD/FreeCAD/pull/5024)
-   Permitir la adición/eliminación modal de entidades geométricas a las restricciones que actúan sobre los límites. [Pull request #5117](https://github.com/FreeCAD/FreeCAD/pull/5117)
-   La mayoría de los cuadros de diálogo de restricciones FEM ahora se comportan de manera uniforme y brindan las mismas funciones de selección de objetos 3D. [Pull request #5391](https://github.com/FreeCAD/FreeCAD/pull/5391)



## Exportar

-   DXF: El bloque de unidad faltante se agregó al archivo header14.rub. [Pull request #5793](https://github.com/FreeCAD/FreeCAD/issues/5793)



## Malla



### Compatibilidad mejorada con los elementos NASTRAN GRID 

La herramienta de importación de malla ahora es compatible con el elemento \"GRID\*\" de alta precisión. También se mejoró el elemento \"GRID\" de precisión estándar, que ahora admite tanto la entrada numérica delimitada por el espacio como la entrada de ancho de campo fijo, según la documentación del formato NASTRAN95.



### Otras mejoras de Mesh 

Se corrigieron falsos negativos durante las pruebas de autointersección cuando las caras son coplanares: [Pull request #5002](https://github.com/FreeCAD/FreeCAD/pull/5002).



## Ambiente de Trabajo OpenSCAD 

Se ha mejorado la interoperabilidad con OpenSCAD, añadiendo soporte para varias operaciones faltantes en versiones anteriores (extrusión lineal con rotaciones, extrusiones rotacionales). Varias operaciones se modificaron para proporcionar mejores objetos FreeCAD equivalentes, particularmente para extrusiones retorcidas. La generación de superficies a partir de datos discretos se modificó para dar resultados más similares a OpenSCAD, en lugar de superficies con splines.

Se agregaron nuevas opciones para soportar la ejecución de FreeCAD, OpenSCAD o ambos, en entornos de espacio aislado como AppImages y paquetes Snap: los datos ahora se pueden transferir hacia y desde OpenSCAD a través del mecanismo de directorio temporal estándar, a través de un directorio temporal especificado por el usuario al que ambos ejecutables tienen acceso, o nuevo en OpenSCAD 2021.1, a través de un mecanismo de \"stdout pipe\", omitiendo por completo los archivos temporales.

+++
| <img alt="" src=images/OpenSCAD_AddElement_relnotes_0.20.png  style="width:384px;"> | Las siguientes opciones fueron agregadas al panel de tareas de la característica [Añadir elemento OpenSCAD](OpenSCAD_AddOpenSCADElement.md): |
|                                                                                                 |                                                                                                                                                      |
|                                                                                                 | Cargar    - carga un archivo scad                                                                                                                  |
|                                                                                                 | Guardar   - guarda un archivo scad                                                                                                                 |
|                                                                                                 | Refrescar - actualiza la vista de FreeCAD                                                                                                          |
|                                                                                                 | Limpiar   - limpia el texto de entrada                                                                                                             |
|                                                                                                 |                                                                                                                                                      |
|                                                                                                 | Una nueva caja de texto da retroalimentación de los erroes de OpenSCAD.                                                                              |
+++



## Ambiente de Trabajo Part 

   
  <img alt="" src=images/Part_Extrusion-inner-structures_relnotes_0.20.png  style="width:384px;">Extrusión cónica de un croquis con una estructura interna.   La [extrusión](Part_Extrude.md) cónica de estructuras internas ahora crea resultados utilizables. Anteriormente, las estructuras internas se extruían como si fueran independientes y no fueran parte de una estructura.. [Pull request #5367](https://github.com/FreeCAD/FreeCAD/pull/5367)
   



### Otras mejoras de Part 


<div class="mw-translate-fuzzy">

-   El diálogo para editar [Cilindros](Part_Cylinder.md) ahora permite especificar un ángulo relativo a la normal de el plano seleccionado. De esta manera se pueden crear cilindros oblicuos. [Pull request #4708](https://github.com/FreeCAD/FreeCAD/pull/4708)
-   La herramienta [Face Colors](Part_FaceColors.md) ahora permite establecer una transparencia (*Canal alfa*) a las caras. Esta transparencia puede ser [exportada](Import_Export.md), haciendo, por ejemplo, crear archivos STEP con partes transparentes posible.
-   Los siguientes comandos ahora soportan App::Links: [Puente](Part_Loft.md), [Barrido](Part_Sweep.md), [Extruir](Part_Extrude.md), [Revolución](Part_Revolve.md), [Invertir formas](Part_ReverseShape.md), [Espejo](Part_Mirror.md), [Offset2D](Part_Offset2D.md), [Offset3D](Part_Offset.md), [Comprobar geometría](Part_CheckGeometry.md), [Superficie reglada](Part_RuledSurface.md), [Cortes transversales](Part_CrossSections.md), y [Espesor](Part_Thickness.md). [Pull request #6478](https://github.com/FreeCAD/FreeCAD/pull/6478)


</div>



## Ambiente de Trabajo PartDesign 

+++
| <img alt="" src=images/PD_Pad-Length-along-reference_relnotes_0.20.gif  style="width:384px;">Extruir a lo largo del un borde del modelo.Clic en la imagen para ver la animación.                                                                          | Hay una nueva opción para [extruir](PartDesign_Pad.md) a lo largo de la dirección de un borde en el modelo 3D. [Pull request #4685](https://github.com/FreeCAD/FreeCAD/pull/4685)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+++
| <img alt="" src=images/PartDesign_Chamfer_Face_Selection_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                                 | Cuando la distancia y el ángulo es especificadoo en la herramienta [Chaflán](PartDesign_Chamfer.md) y las caras son seleccionadas, la distancia se aplicará a lo largo de las caras seleccionadas. Del mismo modo, si se especifican dos distancias, se aplicará el tamaño 1 a lo largo de la cara seleccionada. Este comportamiento se puede cambiar a la otra cara utilizando el botón de dirección de giro. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=19&t=62084), [Pull request #5039](https://github.com/FreeCAD/FreeCAD/pull/5039)                                                                                                                                                                                                                                                               |
+++
| <img alt="" src=images/PartDesign_Loft_Vertex_relnotes_0.20.png  style="width:384px;">Una proyección aditiva con múltiples secciones, el último es un vértice.                                                                                                                 | Ahora es posible crear una [Proyección aditiva](PartDesign_AdditiveLoft.md) o una [Proyección substractiva](PartDesign_SubtractiveLoft.md), o un [Barrido aditivo](PartDesign_AdditivePipe.md) o un [Barrido substractivo](PartDesign_SubtractivePipe.md) hacia, o desde, un [Vértice](Glossary#V.md) o de un croquis o un cuerpo. Esto permite crear pirámides por ejemplo.**Nota**: Los Vértices en los croquis son creados como geometría de construcción. Para usarlos como puntos finales de una proyección, primero debe [cambiarlos a geometría normal](Sketcher_ToggleConstruction.md). [Pull request #5170](https://github.com/FreeCAD/FreeCAD/pull/5170) (para proyecciones), [Pull request #5193](https://github.com/FreeCAD/FreeCAD/pull/5193) (para barridos) |
+++
| <img alt="" src=images/PD_Pad-Taper-angle_relnotes_0.20.png  style="width:384px;">Un hueco cónico dentro de una extrusión no cónica.                                                                                                                                               | El diálogo para [Relleno](PartDesign_Pad.md) y [Hueco](PartDesign_Pocket.md) permite poner un ángulo cónico para la extrusión. [Pull request #5357](https://github.com/FreeCAD/FreeCAD/pull/5357)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
| <img alt="" src=images/PD_Pocket-direction_relnotes_0.20.gif  style="width:384px;">Haciendo huecos a lo largo de diferentes direcciones.Clic en la imagen para ver la animación.                                                                                    | Ahora es posible especificar la dirección del [hueco](PartDesign_Pocket.md). [Pull request #5164](https://github.com/FreeCAD/FreeCAD/pull/5164)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+++
| <img alt="" src=images/PartDesign_Cylinder_direction_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                                         | El diálogo para editar [Cilindros](PartDesign_AdditiveCylinder.md) (aditivos y substractivos) ahora permite especificar un ángulo relativo a la normal de el plano seleccionado. De esta manera se pueden crear cilindros oblicuos. [Pull request #4708](https://github.com/FreeCAD/FreeCAD/pull/4708)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+++
| <img alt="" src=images/PartDesign_Helix_Growth_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                                                     | La característica [Hélice](PartDesign_AdditiveHelix.md) ahora tiene un nuevo modo **Altura-Vueltas-Incremento** para crear espirales planas. [Hilo del foro](https://forum.freecadweb.org/viewtopic.php?f=19&t=56378) [Pull request #4590](https://github.com/FreeCAD/FreeCAD/pull/4590)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+++
| <img alt="" src=images/PartDesign_Islands-Extrude_relnotes_0.20.png  style="width:384px;">Una sola extrusión y una sola [Revolución](PartDesign_Revolution.md) con perfiles anidados. El bloque base está solo para asegurarse de que la parte es un único cuerpo. | Todas las características de PartDesign que pueden extruir croquis ahora pueden manejar croquis con perfiles anidados que forman islas. Por ejemplo, es posible [revolucionar](PartDesign_Revolution.md) un croquis que consta de 3 círculos anidados con el mismo punto central.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                             | **Nota**: La extrusión de perfiles anidados solo funciona si el resultado sigue siendo un solo cuerpo. [Pull request #6381](https://github.com/FreeCAD/FreeCAD/pull/6381)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+++
| <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width:384px;">Efecto de la nueva opción *Longitud a lo largo de la normal del croquis*.Clic en la imagen para ver la animación.                                              | Hay una nueva opción para [extruir](PartDesign_Pad.md) una cierta longitud a lo largo de la dirección. La longitud puede medirse a lo largo del croquis normal o a lo largo de la dirección personalizada. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=17&t=50466), [Pull request #3893](https://github.com/FreeCAD/FreeCAD/pull/3893)                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+++
| <img alt="" src=images/PartDesign_Hole_thread_relnotes_0.20.PNG  style="width:384px;">                                                                                                                                                                                                       | La característica [Agujero](PartDesign_Hole.md) ahora puede modelar cuerdas reales. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=34&t=54240) [Pull request #4274](https://github.com/FreeCAD/FreeCAD/pull/4274)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+++
|                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+++



### Otras mejoras de PartDesign 

-   En la característica [Hélice](PartDesign_AdditiveHelix.md) ahora también se puede utilizar la normal del croquis como eje. [Pull request #5199](https://github.com/FreeCAD/FreeCAD/pull/5199)
-   La característica [Rueda dentada](PartDesign_Sprocket.md) ahora puede crear ruedas dentadas con la norma ISO. [Hilo del foro](https://forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [Pull request #4478](https://github.com/FreeCAD/FreeCAD/pull/4478)
-   las características [Proyección](PartDesign_AdditiveLoft.md) y [Barrido](PartDesign_AdditivePipe.md) ahora permiten usar las caras de los cuerpos para las secciones. [Pull request #5155](https://github.com/FreeCAD/FreeCAD/pull/5155)
-   Ahora es posible selecionar varias caras antes de llamar al diálogo de [Relleno](PartDesign_Pad.md) o [Hueco](PartDesign_Pocket.md). En este caso, la primer cara seleccionada se utilizará para determinar la dirección predeterminada de relleno/hueco. [commit d34a5616](https://github.com/FreeCAD/FreeCAD/commit/d34a5616a2b38c96ad05f9a0763ba7504dfb814d)
-   Es posible compensar los [SubShapeBinders](PartDesign_SubShapeBinder.md) si están basados en bordes, alambres o caras. [Pull request #6338](https://github.com/FreeCAD/FreeCAD/pull/6338)
-   [SubShapeBinders](PartDesign_SubShapeBinder.md) ahora tiene la propiedad *Refinar* como todos los objetos de PartDesign. [Pull request #6550](https://github.com/FreeCAD/FreeCAD/pull/6550)
-   En los diálogos de [Bisel](PartDesign_Chamfer.md) y [Redondeo](PartDesign_Fillet.md) todos los bordes de un cuerpo pueden ser seleccionados a través del menú contextual mientras se está en modo agregar. [Pull request #5269](https://github.com/FreeCAD/FreeCAD/pull/5269)
    Cuando seleccionas un objeto 3D antes de hacer clic en el icono para crear un redondeo o bisel, todos los bordes del objeto se seleccionarán automáticamente. [Pull request #5328](https://github.com/FreeCAD/FreeCAD/pull/5328)
-   Los diálogos de [Bisel](PartDesign_Chamfer.md) y [Redondeo](PartDesign_Fillet.md) ahora cada uno tiene una nueva casilla de verificación para usar todos los bordes, que está conectada a la propiedad Usar todos los bordes para estos objetos. Cuando la casilla está marcada, la propiedad se establece en Verdadero, cuando no está marcada, la propiedad se establece en Falso. Cuando Usar todos los bordes es Verdadero, hay una protección contra el [problema de denominación topológica](Topological_naming_problem.md) porque entonces se usan todos los bordes del objeto base independientemente de cuántos bordes haya. [Pull request #5340](https://github.com/FreeCAD/FreeCAD/pull/5340)
-   Ahora se puede lograr la selección de planos cuando se agrega [un nuevo croquis](PartDesign_NewSketch.md) con un solo clic en la vista 3D. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/5408) [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=19&t=65020)
-   Cuando una herrramienta de PartDesign se ejecuta sin un cuerpo activo, ahora FreeCAD ofrece activar un cuerpo o crear uno nuevo. [Pull request #4949](https://github.com/FreeCAD/FreeCAD/pull/4949)
-   La herramienta [Colores de cara](Part_FaceColors.md) está ahora disponible en el entorno de trabajo PartDesign.



## Ambiente de Trabajo Path 

-   La característica Extensiones fue agregada a la operación [Adaptive](Path_Adaptive.md). [Pull request #4388](https://github.com/FreeCAD/FreeCAD/pull/4388)
-   La operación [Hélice](Path_Helix.md) se refactorizó y se le agregó la propiedad Extra offset. [Pull request #5405](https://github.com/FreeCAD/FreeCAD/pull/5405)
-   Se agregó la comprobación de si el esquema actual está utilizando minutos para la expresión de velocidad y la advertencia adecuada. [Pull request #6357](https://github.com/FreeCAD/FreeCAD/pull/6357)
-   Se agregaron roscas externas a la operación de fresado de roscas. [Pull request #6485](https://github.com/FreeCAD/FreeCAD/pull/6485)
-   Se mejoró la estabilidad del grabado en croquis. [Pull request #6394](https://github.com/FreeCAD/FreeCAD/pull/6394)
-   La visibilidad de objetos path se hizo más natural. [Pull request #4911](https://github.com/FreeCAD/FreeCAD/pull/4911)



## Módulo Plot 

-   FreeCAD ahora proporciona el módulo Plot de forma predeterminada, por lo que cualquier otro módulo/entorno de trabajo puede crear gráficas sin necesidad de herramientas externas. [Pull request #4971](https://github.com/FreeCAD/FreeCAD/pull/4971).



## Ambiente de Trabajo Sketcher 

+++
| <img alt="" src=images/SketcherSplitExample2_relnotes_0.20.png )                                                | La nueva función ![](images/Sketcher_Split.svg  style="width:24px;"> [Dividir](Sketcher_Split.md) divide líneas o arcos existentes. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=9&t=55412) [Pull request #4420](https://github.com/FreeCAD/FreeCAD/pull/4420)                                                                                                                                                                                                            |
+++
| <img alt="" src=images/SketcherCreateRoundedRectangleExample_relnotes_0.20.png )                | La nueva herramienta ![](images/Sketcher_CreateOblong.svg  style="width:24px;"> [Rectángulo redondeado](Sketcher_CreateOblong.md) crea un rectángulo con esquinas redondeadas. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main Pull request #4835](https://github.com/FreeCAD/FreeCAD/pull/4835)                                                                                                                                                    |
+++
| <img alt="" src=images/SketcherCreateCenteredRectangleExample_relnotes_0.20.png  style="width:384px;"> | La nueva herramienta <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:24px;"> [Rectángulo centrado](Sketcher_CreateRectangle_Center.md) crea un rectángulos a partir del centro. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)                                                                                                                                                                                  |
+++
| <img alt="" src=images/Radiam_anim_relnotes_0.20.gif )                                                                    | La nueva función ![](images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Radiam](Sketcher_ConstrainRadiam.md) para asignar automáticamente el peso en el polo en una B-spline, el diámetro en el círculo completo o el radio en el arco. Admite selección múltiple como herramientas de diámetro/radio. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Main Pull request #4855](https://github.com/FreeCAD/FreeCAD/pull/4855) |
+++
| <img alt="" src=images/SketcherRemoveAxesAlignmentResult_relnotes_0.20.png )                        | La nueva herramienta de restricción ![](images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Eliminar Alineación de Ejes](Sketcher_RemoveAxesAlignment.md) elimina la alineación de los ejes mientras trata de preservar las relaciones de restricciones de la selección. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)                                                                                              |
+++
| ![](images/SketcherSnapSlot_relnotes_0.20.gif )                                                          | Las [Ranuras](Sketcher_CreateSlot.md) pueden ser restringidas horizontalmente o verticalementeya ya sea ajustándolo manualmente con la tecla **Ctrl**, o usando la opción **Restricciones automáticas** de Sketcher. [Pull request #5200](https://github.com/FreeCAD/FreeCAD/pull/5200)                                                                                                                                                                                             |
+++
| <img alt="" src=images/SketcherBSplineInsertKnot_relnotes_0.20.gif )                                        | La nueva herramienta ![](images/Sketcher_BSplineInsertKnot.svg  style="width:24px;"> [Insertar Nodo](Sketcher_BSplineInsertKnot.md) inserta un nodo en una B-splina ya existente. [Pull request #5311](https://github.com/FreeCAD/FreeCAD/pull/5311) and [Pull request #6356](https://github.com/FreeCAD/FreeCAD/pull/6356)                                                                                                                                                          |
+++



### Otras mejoras de Sketcher 

-   Soporte para Dividir refactorizado. [Pull request #4330](https://github.com/FreeCAD/FreeCAD/pull/4330) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=10&t=54441)
-   El comportamiento de la herramienta <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Ranura](Sketcher_CreateSlot.md) cambiado. Las ranuras ahora pueden ser creadas definiendo el centro de ambos semicírculos. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4843) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   La automatización de la visibilidad permite abrir Sketcher en [ Modo de sección](Sketcher_ViewSection.md) al entrar en el modo de edición. [Pull request #4742](https://github.com/FreeCAD/FreeCAD/pull/4742) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   La automatización de la visibilidad permite forzar la cámara en [Modo Orthográfico](Std_OrthographicCamera.md) al entrar en modo de edición. [Pull request #4778](https://github.com/FreeCAD/FreeCAD/pull/4778) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=22&t=44747)
-   Opción para mostrar el nombre de la restricción dimensional y utilizar un formato personalizado para ello. [Pull request #4966](https://github.com/FreeCAD/FreeCAD/pull/4966) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?t=61153)
-   Al realizar un [arco de 3 puntos](Sketcher_Create3PointArc.md) con restricciones automáticas habilitadas, la [restricción tangente](Sketcher_ConstrainTangent.md) se propone para los 3 puntos al desplazarse sobre una línea/curva. [Pull request #4945](https://github.com/FreeCAD/FreeCAD/pull/4945) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=3&t=60596&p=520217#p520209)
-   Las restricciones de radio/diámetro se muestran mediante una rotación angular para facilitar la visualización. El ángulo y la aleatoriedad opcional son configurables por el usuario a través de parámetros documentados en [Ajuste fino](Fine-tuning.md). [Pull request #4934](https://github.com/FreeCAD/FreeCAD/pull/4934) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=22&t=60370)
-   Ahora es posible fijar el ángulo de la dirección cuando se utiliza la herramienta [Arreglo Rectangular](Sketcher_RectangularArray.md). [commitc9eaa239](https://github.com/FreeCAD/FreeCAD/commit/c9eaa239) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?p=535691#p535691)
-   Ahora es posible fijar el ángulo de la dirección cuando se utiliza las herramientas [Clonar](Sketcher_Clone.md), [Copiar](Sketcher_Copy.md) and [Mover](Sketcher_Move.md). [commit](https://github.com/FreeCAD/FreeCAD/commit/6e4a09f569cf) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=8&t=62799)
-   Al hacer clic con el botón derecho en un croquis en la vista de árbol, ahora obtendrá una entrada de menú contextual \"Editor de datos adjuntos\" que abre el [Diálogo adjunto](Part_EditAttachment.md) para el modificar el adjunto. [commit c3511ba2f0](https://github.com/FreeCAD/FreeCAD/commit/c3511ba2f0)
-   La selección de restricciones está deshabilitada cuando se usa una herramienta de geometría o restricción. También se puede desactivar manualmente en cualquier momento presionando la tecla **Shift**. [Pull request #5398](https://github.com/FreeCAD/FreeCAD/pull/5398) [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=10&t=65465)
-   Se ha agregado un filtro de vista versátil en el panel de tareas de Sketcher para facilitar la gestión de la visibilidad de las restricciones. [Discusión en el foro](https://forum.freecadweb.org/viewtopic.php?f=17&t=60569)
-   Ahora es posible establecer el grado de una B-Spline ([Pull request #6463](https://github.com/FreeCAD/FreeCAD/pull/6463)) y deshacer el último punto de control definido ([Pull request #6476](https://github.com/FreeCAD/FreeCAD/pull/6476)) en el momento de la creación.
-   Se revisó los atajos de teclado por defecto para eliminar los atajos conflictivos y hacer atajos fáciles de recordar. [Discusión enm el foro](https://forum.freecadweb.org/viewtopic.php?f=3&t=41272); Capturas de pantalla de los atajos para [restricciones](https://wiki.freecadweb.org/images/0/0c/Sketcher_Shortcuts_v0.20_Screenshot_Constraints.png), [geometría](https://wiki.freecadweb.org/images/4/48/Sketcher_Shortcuts_v0.20_Screenshot_Geometry.png) y [herramientas varias](https://wiki.freecadweb.org/images/9/90/Sketcher_Shortcuts_v0.20_Screenshot_variousTools.png)



## Ambiente de Trabajo Spreadsheet 

+++
| <img alt="" src=images/Spreadsheet-Preferences-Spreadsheet_relnotes_0.20.png )      | El entorno de trabajo ahora tiene ![](images/Std_DlgPreferences.svg  style="width:24px;"> [Preferencias](Spreadsheet_Preferences.md). Son usadas por los comandos <img alt="" src=images/Spreadsheet_Import.svg  style="width:16px;"> [Spreadsheet Importar](Spreadsheet_Import.md) y <img alt="" src=images/Spreadsheet_Export.svg  style="width:16px;"> [Spreadsheet Exportar](Spreadsheet_Export.md). [Pull request #5073](https://github.com/FreeCAD/FreeCAD/pull/5073) |
+++
| <img alt="" src=images/Spreadsheet_configuration_table_relnotes_0.20.png  style="width:384px;"> | Ahora es posible configurar [tablas de configuración](Spreadsheet_Workbench#Configuration_tables.md). De esta forma se puede definir diferentes conjuntos de parámetros para la misma pieza. Parte de [Pull request #2862](https://github.com/FreeCAD/FreeCAD/pull/2862).                                                                                                                                                                                                                      |
+++
| ![](images/Spreadsheet_binding-dialog_relnotes_0.20.png )                        | Las celdas ahora pueden ser [enlazadas a otras celdas](Spreadsheet_Workbench#Cell_binding.md) de la misma o diferente hoja de cálculo. Parte de [Pull request #2862](https://github.com/FreeCAD/FreeCAD/pull/2862).                                                                                                                                                                                                                                                                            |
+++



### Otras mejoras de Spreadsheet 

-   En el menú contextual de fila/columna ahora es posible especificar la posición al insertar filas/columnas. [Pull request #4704](https://github.com/FreeCAD/FreeCAD/pull/4704).
-   Importar XLSX (usado por [Std Import](Std_Import.md)): Soporte agregado para funciones de piso y techo. [Pull request #5015](https://github.com/FreeCAD/FreeCAD/pull/5015).
-   Navegación mejorada usando las teclas **Tab** y **Enter**.
-   Interfaz mejorada para cortar y pegar bloques de celdas.



## Ambiente de Trabajo TechDraw 

+++
| <img alt="" src=images/TechDraw_ExtensionExample_relnotes_0.20.png  style="width:400px;"> | Más de 30 nuevas herramientas, llamadas [Extensiones](TechDraw_Workbench#Extensions.md), ahora están disponibles. Ofrecen nuevas funciones cosméticas para mejorar los dibujos. |
+++



### Otras mejoras de TechDraw 

-   Ahora es posible [Compartir](TechDraw_ShareView.md) y [Mover](TechDraw_MoveView.md) [Vistas](TechDraw_Workbench#Views.md) entre páginas.
-   Cuando hay muchas [Páginas](TechDraw_PageDefault.md) y una [Vista](TechDraw_View.md), [Grupo de proyección](TechDraw_ProjectionGroup.md) etc. es agregado, ahora hay un cuadro de diálogo para preguntar a qué página se debe agregar la vista. [Pull request #5309](https://github.com/FreeCAD/FreeCAD/pull/5309).
-   Se agregó un nuevo especificador de formato *%w* para imprimir el número dado de dígitos después del punto y eliminar los ceros finales. [Pull request #5401](https://github.com/FreeCAD/FreeCAD/pull/5401).
-   El nuevo especificador de formato *%w* ahora es el predeterminado. Y la preferencia del especificador de formato se movió de la pestaña Avanzado a la pestaña Dimensión. [Pull request #6504](https://github.com/FreeCAD/FreeCAD/pull/6504).
-   Se agregó un achurado diagonal invertido para la herramienta [Achurado Geometrico](TechDraw_GeometricHatch.md). [Pull request #6429](https://github.com/FreeCAD/FreeCAD/pull/6429).
-   Ahora hay una nueva opción para mostrar una grilla en una [página](TechDraw_PageDefault.md). Muchas [preferencias](TechDraw_Preferences#Grid.md) relacionadas han sido añadidas. [Pull request #6465](https://github.com/FreeCAD/FreeCAD/pull/6465).
-   La visualización de la unidad en dimensiones se corrigió de acuerdo con los estándares. El símbolo de grado siempre está presente para el valor de cota y las tolerancias, otras unidades solo aparecen si se establece en ShowUnits. La unidad aparece inmediatamente después del valor de cota a menos de que haya una tolerancia, aparecerá después de la tolerancia. [Pull request #6581](https://github.com/FreeCAD/FreeCAD/pull/6581)

## Web

Qt WebEngine es ahora considerado la opción por defecto en lugar de Qt WebKit.



## Entornos de trabajo externos 


**Nota:**

estos son los nuevos entornos de trabajo creados en este ciclo de desarrollo o los entornos de trabajo antiguos que recibieron actualizaciones. Consulte [entornos de trabajo externos](External_workbenches.md) para más entornos de trabajo que se pueden instalar y que cubren una amplia variedad de temas. Si desea que se agregue su entorno de trabajo, únase al \[foro de <https://forum.freecadweb.org/index.php>\] y presente su código.

### A2plus

Se agregaron varias características para ver, inspeccionar y editar restricciones existentes. Uno puede ahora, por ejemplo resaltar las restricciones con una etiqueta, borrar una restricción temporalmente o ejecutar el solucionador solo para una restricción en particular.

Para más información véa [la descripción de manejo de restricciones](A2plus_Workbench#Constraint_Handling.md).

### Assembly3

+++
| <img alt="" src=images/Asm3_relnotes_0.20.jpg  style="width:384px;">     | El entorno de trabajo Assembly3 está disponible (desde marzo de 2022) a través del [Administrador de Complementos](Std_AddonMgr.md). Esto facilita la instalación y gestión de las dependencias externas del entorno de trabajo.                                                                                                         |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                  |
|                                                                       | Assembly3 se utiliza para crear ensamblajes de diferentes cuerpos contenidos en un solo archivo o en múltiples documentos que aprovechan la potencia completa del sistema de enlace de FreeCAD. Obtenga más información sobre [ Enlace](App_link.md) en esta [presentación](https://www.youtube.com/watch?v=ytdkj7jzaws) de RealThunder. |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                  |
|                                                                       | El entorno de trabajo Assembly3 usa [SolveSpace](https://solvespace.com) como su solucionador.                                                                                                                                                                                                                                                   |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                  |
|                                                                       | Se puede encontrar una documentación extensa en la página principal de la [wiki de Assembly3](Assembly3.md) de FreeCAD o en la [wiki de Assembly3](https://github.com/realthunder/FreeCAD_assembly3/wiki) de Realthunder en GitHub                                                                                                       |
+++
| <img alt="" src=images/Asm3_1_relnotes_0.20.jpg  style="width:384px;"> | **Main features:**                                                                                                                                                                                                                                                                                                                               |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                  |
|                                                                       | -   Solucionador dinámico/interactivo: mueve partes con el ratón mientras el solucionador restringe el movimiento.                                                                                                                                                                                                                               |
|                                                                       | -   Enlaces: usa una sola parte varias veces en un ensamble.                                                                                                                                                                                                                                                                                     |
|                                                                       | -   Enlaces externos: permite usar partes de documentos externos.                                                                                                                                                                                                                                                                                |
|                                                                       | -   Ensambles jerárquicos: permite la creación de subensambles.                                                                                                                                                                                                                                                                                  |
|                                                                       | -   Congelamiento del ensamble: Los ensamblajes que no necesitan permanecer dinámicos pueden excluirse de los cálculos y son considerados como geometría fija por el solucionador asm3.                                                                                                                                                          |
|                                                                       | -   Y mucho más.                                                                                                                                                                                                                                                                                                                                 |
+++

### Assembly4

   
  <img alt="" src=images/A4_veriant-beam_relnotes_0.20.png  style="width:384px;">Diferentes longitudes de una barra como variantes.                                     Nueva característica para agregar variantes. Estos son [enlaces](App_Link.md) a una parte con parámetros variables, lo que significa que puede insertar la misma parte varias veces y ajustar los parámetros de cada instancia. Para más información vea [este hilo del foro](https://forum.freecadweb.org/viewtopic.php?p=538666#p538666).
  <img alt="" src=images/A4_veriant-animation_relnotes_0.20.gif  style="width:384px;">Un ensamble animado.Clic en la imagen para ver la animación.   Las animaciones pueden ser exportadas a los formatos MP4 o GIF.
   

### FCGear

El [entorno de trabajo FCGear](FCGear_Workbench.md) recibió un par de mejoras:

-   Para engranajes involutivos, el exterior (también conocido como punta) y el diámetro de la raíz se exponen como propiedades. ([detalles](https://github.com/looooo/freecad.gears/pull/69)).
-   Los objetos Gear ahora se pueden [unir](Part_EditAttachment.md) ([detalles](https://github.com/looooo/freecad.gears/pull/72)).
-   Los objetos Gear ahora se pueden usar como características aditivas en los cuerpos de PartDesign ([detalles](https://github.com/looooo/freecad.gears/pull/74)).
-   La creación de objetos Gear ahora aparece en la pila de deshacer ([detalles](https://github.com/looooo/freecad.gears/pull/83)).

### Plot

-   El módulo Plot ha sido eliminado del [Entorno de trabajo Plot](Plot_Workbench.md) ya que ahora es proporcionado por FreeCAD.

### Ship

¡El [entorno de trabajo Ship](Ship_Workbench.md) a vuelto a la vida!

-   Una nueva herramienta para calcular el [hudimiento estático y recorte](https://github.com/FreeCAD/freecad.ship#static-sink-and-trim) ha sido añadida.
-   Una nueva herramienta para calcular los [operadores de amplitud de respuesta](https://github.com/FreeCAD/freecad.ship#raos) ha sido añadida encima de [capytaine](https://github.com/mancellin/capytaine).



## Compilación

Desde esta versión de FreeCAD solo puede ser compilado usando Qt 5.x y Python 3.x. La versión más baja soportada es Python 3.6.9 de acuerdo a [este hilo del foro](https://forum.freecadweb.org/viewtopic.php?f=10&t=62701).

Para compilar FreeCAD vea las instrucciones para [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) y [MacOS](Compile_on_MacOS.md).

Los sistemas operativos soportados:

-   Windows 7, 8, 10 y 11
-   Linux Ubuntu Bionic Beaver (18.04) y Focal Fossa (20.04)
-   MacOS: 10.12 Sierra o más nuevo



## Limitaciones conocidas 



#### Windows de 32 bits 

Desde FreeCAD 0.19 no soportamos oficialmente Windows de 32 bits. FreeCAD podría funcionar en estos sistemas pero no se brinda soporte.



#### Escritorio remoto en Windows 

Dependiendo de las capacidades gráficas OpenGL de una computadora, podría ser que se encuentre un bloqueo cuando se ejecuta Freecad a través de un escritorio remoto. Para solucionar esto actualice su controlador OpenGL. Solo si esto no ayuda:

-   Descargar [esta](https://downloads.fdossena.com/geth.php?r=mesa64-latest) biblioteca OpenGL para Windows de 64 bits y extraerla.
-   Cambie el nombre del archivo DLL a *OpenGL32SW.DLL* y cópielo a la subcarpeta *bin* de la carpeta de instalación de FreeCAD (sobrescriba el DLL existente allí).



### MacOS: Entorno de trabajo Start Workbench muestra una página en blanco 

Si el [entorno de trabajo Start](Start_Workbench/es.md) muestra solo una página en blanco, debe de habilitar la opción **Usar OpenGL software** en el menú **Editar → Preferencias → Mostrar**.



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.20/es
