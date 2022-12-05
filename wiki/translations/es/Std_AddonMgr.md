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

El comando **Std AddonMgr** abre el gestor de complementos. Con el gestor de complementos puedes instalar y gestionar [Ambientes de trabajo externos](external_workbenches/es.md), [Macros](macros/es.md) y [paquetes de preferencias](Preference_Packs.md) proporcionados por la comunidad de FreeCAD. Por defecto los complementos disponibles son tomados de dos repositorios, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) y de la página [Recetas de macros](Macros_recipes/es.md). Si GitPython y git están instalados en su sistema, se cargarán macros adicionales desde [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/). Se pueden agregar repositorios personalizados en [Preferencias del administrador de complementos](Preferences_Editor#Addon_Manager.md).

Debido a los cambios en la plataforma GitHub en el año 2020 el gestor de Addons ya no funciona si utilizas la versión 0.17 o anterior de FreeCAD. Necesitas actualizar a la versión [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) o más reciente. Alternativamente puedes instalar addons manualmente, ver [Notas](#Notas.md) abajo.

## Utilización

1.  Seleccione la opción **Herramientas → <img src="images/Std_AddonMgr.svg" width=16px> Gestor complementos** en el menú.
2.  Si es la primera vez que utiliza el gestor complementos, se abrirá un cuadro de diálogo advirtiéndole de que los complementos del gestor de complementos no forman parte oficialmente de FreeCAD. Adjuste esas opciones a su gusto y pulse el botón **OK** para confirmar y continuar.
3.  Se abre el cuadro de diálogo del Gestor complementos. Para más información ver [Opciones](#Opciones.md).
4.  Si has instalado o actualizado un ambiente de trabajo se abrirá un nuevo cuadro de diálogo informando de que tienes que reiniciar FreeCAD para que los cambios surtan efecto.

## Opciones

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  El administrador de complementos proporciona dos diseños de vista: \"Condensada\" y \"Expandida\". En la vista \"Condensada\", cada complemento ocupa una sola línea y su descripción se trunca para ajustarse al espacio disponible. La vista \"Expandida\" muestra detalles adicionales, incluido más texto de descripción, así como información del mantenedor, más detalles de instalación, etc.
2.  Se admiten tres tipos diferentes de complementos: [entornos de trabajo](external_workbenches.md), [macros](macros.md) y [paquetes de preferencia](Preference_Packs.md). Puede optar por mostrar solo un tipo o todos en una sola lista.
3.  La lista se puede limitar para mostrar únicamente a los paquetes instalados, solo paquetes con actualizaciones disponibles o solo paquetes que aún no están instalados.
4.  La lista se puede filtrar, buscando una palabra clave en el título, la descripción y las etiquetas (el desarrollador del complemento debe especificar la descripción y las etiquetas en los metadatos de su complemento). El filtro puede ser incluso una expresión regular, para un control detallado del término de búsqueda exacto.
5.  La vista ampliada muestra la información de la versión disponible, la descripción, la información del mantenedor y la información de la versión de instalación, para los paquetes que proporcionan un archivo de [metadatos del paquete](Package_Metadata.md) (o para macros con metadatos incrustados).
6.  Los datos adicionales se almacenan en caché localmente, con una frecuencia de actualización de caché variable establecida en las preferencias del usuario.
7.  En cualquier momento, puede optar por actualizar manualmente su caché local para ver las últimas actualizaciones disponibles para cada complemento.
8.  Las comprobaciones de actualización pueden configurarse para que sean automáticas o manuales mediante un clic de botón (configurado en las preferencias del usuario). Si GitPython y git están instalados en su sistema, la información de actualización se obtiene mediante git. De lo contrario, la información de actualización se obtiene de cualquier archivo de metadatos presente.

Al hacer clic en un complemento en esta vista, aparece la página Detalles del complemento:

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

La página de detalles muestra botones que permiten instalar, desinstalar, actualizar y deshabilitar temporalmente un complemento. Para los complementos instalados, enumera la versión instalada actualmente y la fecha de instalación, y si esa es la versión más reciente disponible. A continuación se muestra una ventana de navegador web incrustada que muestra la página LÉAME (README) del complemento (para entornos de trabajo y paquetes de preferencias) o la página Wiki (para macros).

## Preferencias

Las preferencias para el administrador de complementos pueden ser encontradas en el [Editor de preferencias](Preferences_Editor#Addon_Manager.md). <small>(v0.20)</small> 

## Notas

-   El uso de los complementos no está restringido a la versión de FreeCAD desde la que fueron instalados. También podrás utilizarlos en cualquier otra versión de FreeCAD, soportada por el complemento, que puedas tener en tu sistema.
-   Los complementos disponibles en el gestor complementos no son parte del programa oficial de FreeCAD y no están soportados por el equipo de desarrollo de FreeCAD. Debes leer la información proporcionada cuidadosamente para asegurarte de que sabes lo que estás instalando.
-   Los informes de errores y las peticiones de características deben hacerse directamente al creador del addon visitando el sitio web indicado. Muchos desarrolladores de complementos son usuarios habituales del [foro de FreeCAD](https://forum.freecadweb.org), y también pueden ser contactados allí.
-   Si el paquete [GitPython](https://github.com/gitpython-developers/GitPython) está instalado en tu ordenador, el gestor complementos lo utilizará, haciendo que las descargas sean más rápidas.
-   También puedes instalar complementos manualmente. Ver [Cómo instalar ambientes de trabajo adicionales](How_to_install_additional_workbenches/es.md) y [Cómo instalar macros](How_to_install_macros/es.md).

## Información para desarrolladores 

Vea [Complemento](Addon#Information_for_developers.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/es
