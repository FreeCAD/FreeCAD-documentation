---
- GuiCommand:/es
   Name:Std AddonMgr
   Name/es:Std GestorComplementos
   MenuLocation:Herramientas → Gestor Complementos
   Workbenches:Todo
   Version:0.17
   SeeAlso:[Ambientes de trabajo externos](External_workbenches/es.md), [Macros](Macros/es.md)
---

# Std AddonMgr/es

## Descripción

El comando **Std GestorComplementos** abre el gestor de complementos. Con el gestor de complementos puedes instalar y gestionar [Ambientes de trabajo externos](external_workbenches/es.md) y [Macros](macros/es.md) proporcionados por la comunidad de FreeCAD. Las Ambientes de trabajo y macros disponibles se toman de dos repositorios, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) y [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/), y de la página [Recetas de macros](Macros_recipes/es.md).

Los Complementos marcados como {{emphasis|Sólo Python 2}} no funcionarán en FreeCAD versión 0.19 o superior.

Debido a los cambios en la plataforma GitHub en el año 2020 el gestor de Addons ya no funciona si utilizas la versión 0.17 o anterior de FreeCAD. Necesitas actualizar a la versión [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) o a una versión reciente [0.19](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre). Alternativamente puedes instalar addons manualmente, ver [Notas](#Notas.md) abajo.

![](images/Std_AddonMgr_dialog.png ) *El cuadro diálogo del gestor complementos*

## Utilización

1.  Seleccione la opción **Herramientas → <img src="images/Std_AddonMgr.svg" width=16px> Gestor complementos** en el menú.
2.  Si es la primera vez que utiliza el gestor complementos, se abrirá un cuadro de diálogo advirtiéndole de que los complementos del gestor de complementos no forman parte oficialmente de FreeCAD. Pulsa el botón **OK** para confirmar y continuar.
3.  Se abre el cuadro de diálogo del Gestor complementos. Para más información ver [Opciones](#Opciones.md).
4.  El botón **<img src="images/Button_valid.svg" width=16px> Actualizar todo** no funciona en este momento.
5.  Pulse el botón **<img src="images/Process-stop.svg" width=16px> Cerrar** para cerrar el cuadro de diálogo.
6.  Si has instalado o actualizado un ambiente de trabajo se abrirá un nuevo cuadro de diálogo informando de que tienes que reiniciar FreeCAD para que los cambios surtan efecto.

## Opciones

El cuadro diálogo del gestor complementos tiene dos pestañas a la izquierda, una con los ambientes de trabajo disponibles y otra con las macros disponibles. El panel de información de la derecha mostrará la página de inicio del complemento seleccionado.

### Desinstalación

1.  Seleccione un complemento instalado en la <img alt="" src=images/Folder.svg  style="width:16px;"> **Ambientes de trabajo** o en la pestaña <img alt="" src=images/Applications-python.svg  style="width:16px;"> Pestaña **Macros**.
2.  Pulse el **<img src="images/Delete.svg" width=16px> Desinstalar seleccionado** botón.

### Instalación/actualización

1.  Seleccione un complemento en la <img alt="" src=images/Folder.svg  style="width:16px;"> **Ambiente de trabajo** o en la pestaña <img alt="" src=images/Applications-python.svg  style="width:16px;"> Pestaña **Macros**.
2.  Pulse el **<img src="images/Edit_OK.svg" width=16px> Instalar/actualizar seleccionada** botón.
3.  Si desea añadir una macro a una barra de herramientas personalizada, no olvide descargar manualmente el archivo de imagen del icono, si está disponible, haciendo clic en el enlace de la página principal del panel de información. Ver [Personalización de la interfaz](Interface_Customization/es#Barras_de_herramientas.md).
4.  Para cambiar la posición de un ambiente de trabajo complemento en la lista [Selector de ambientes de trabajo](Std_Workbench/es.md) vea [Interface\_Customization/es\#Ambientes de trabajo](Interface_Customization/es#Ambientes_de_trabajo.md).

### Configuración

1.  Pulse el **<img src="images/Preferences-general.svg" width=16px> Configurar...** botón.
2.  Se abre el cuadro de diálogo de opciones del gestor complementos.
3.  Opcionalmente, marque la casilla {{CheckBox|TRUE|Automatically check for updates at start (requires GitPython)}} casilla de verificación.
4.  Opcionalmente añada repositorios a la lista de **Repositorios personalizados**. Los complementos de estos repositorios se añadirán en la <img alt="" src=images/Folder.svg  style="width:16px;"> **Ambientes de trabajo** o en la pestaña <img alt="" src=images/Applications-python.svg  style="width:16px;"> Pestaña **Macros**.
5.  Opcionalmente elige la configuración del proxy.
6.  Pulse el botón **Aceptar** o el botón **Cancelar** para cerrar el cuadro de diálogo.

## Notas

-   El uso de los complementos no está restringido a la versión de FreeCAD desde la que fueron instalados. También podrás utilizarlos en cualquier otra versión de FreeCAD, soportada por el complemento, que puedas tener en tu sistema.
-   Los complementos disponibles en el gestor complementos no son parte del programa oficial de FreeCAD y no están soportados por el equipo de desarrollo de FreeCAD. Debes leer la información proporcionada cuidadosamente para asegurarte de que sabes lo que estás instalando.
-   Los informes de errores y las peticiones de características deben hacerse directamente al creador del addon visitando el sitio web indicado. Muchos desarrolladores de complementos son usuarios habituales del [foro de FreeCAD](https://forum.freecadweb.org), y también pueden ser contactados allí.
-   Si el paquete [GitPython](https://github.com/gitpython-developers/GitPython) está instalado en tu ordenador, el gestor complementos lo utilizará, haciendo que las descargas sean más rápidas.
-   También puedes instalar complementos manualmente. Ver [Cómo instalar ambientes de trabajo adicionales](How_to_install_additional_workbenches/es.md) y [Cómo instalar macros](How_to_install_macros/es.md).

## Información para desarrolladores 

Si has desarrollado un ambiente de trabajo o macro, y quieres verlo incluido en el gestor complementos, lee cómo hacerlo en las páginas del repositorio: ([FreeCAD-complementos](https://github.com/FreeCAD/FreeCAD-addons/) y [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). Si añades tu macro a la página [Recetas de macros](Macros_recipes/es.md), no hay nada más que hacer, será automáticamente recogida por el gestor complementos.

### Ambientes de trabajo Python 

Para las ambientes de trabajo en python, no necesitas ninguna aprobación específica para que tu ambientes de trabajo sea añadido al gestor de complementos y, al estar fuera del código fuente de FreeCAD, puedes elegir la licencia que quieras. Si solicitas que tu ambiente de trabajo sea añadido a la lista (no añadiremos ningún nuevo ambiente de trabajo sin una petición de sus autores), ya sea pidiéndolo en el foro o abriendo una incidencia en el repositorio [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/), tu código permanecerá en tu propio repositorio git, sólo lo añadiremos como un submódulo al repositorio [FreeCAD-complementos](https://github.com/FreeCAD/FreeCAD-addons/). Por supuesto, antes de añadir tu ambiente de trabajo, le echaremos un vistazo y nos aseguraremos de que no hay nada potencialmente problemático en él.

### Ambientes de trabajo C++ 

Si desarrollas un ambiente de trabajo en C++, no puede ser ejecutado directamente por los usuarios y debe ser compilado primero. Entonces tienes dos opciones, o proporcionas versiones precompiladas de tu ambiente de trabajo tú mismo, para los diferentes sistemas operativos, o debes solicitar que tu código se fusione con el código fuente de FreeCAD. Para ello, debes utilizar la licencia LGPL (o una licencia totalmente compatible como MIT o BSD), y debes presentar tus nuevas herramientas a la comunidad en el [FreeCAD forum](https://forum.freecadweb.org) para su revisión. Una vez que tu código ha sido probado y aprobado, debes hacer un fork del repositorio de FreeCAD, si no lo has hecho todavía, crear una nueva rama, empujar tu código a ella, y abrir una solicitud de pull para que tu rama se fusione con el repositorio principal.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std AddonMgr/es
