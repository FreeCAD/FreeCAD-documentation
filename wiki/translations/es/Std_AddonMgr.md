---
- GuiCommand   */es
   Name   *Std AddonMgr
   Name/es   *Std GestorComplementos
   MenuLocation   *Herramientas → Gestor Complementos
   Workbenches   *Todo
   Version   *0.17
   SeeAlso   *[Ambientes de trabajo externos](External_workbenches/es.md), [Macros](Macros/es.md)
---

# Std AddonMgr/es

## Descripción


<div class="mw-translate-fuzzy">

El comando **Std GestorComplementos** abre el gestor de complementos. Con el gestor de complementos puedes instalar y gestionar [Ambientes de trabajo externos](external_workbenches/es.md) y [Macros](macros/es.md) proporcionados por la comunidad de FreeCAD. Las Ambientes de trabajo y macros disponibles se toman de dos repositorios, [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) y [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/), y de la página [Recetas de macros](Macros_recipes/es.md).


</div>


<div class="mw-translate-fuzzy">

Debido a los cambios en la plataforma GitHub en el año 2020 el gestor de Addons ya no funciona si utilizas la versión 0.17 o anterior de FreeCAD. Necesitas actualizar a la versión [0.18.5](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) o a una versión reciente [0.19](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre). Alternativamente puedes instalar addons manualmente, ver [Notas](#Notas.md) abajo.


</div>

## Utilización


<div class="mw-translate-fuzzy">

1.  Seleccione la opción **Herramientas → <img src="images/Std_AddonMgr.svg" width=16px> Gestor complementos** en el menú.
2.  Si es la primera vez que utiliza el gestor complementos, se abrirá un cuadro de diálogo advirtiéndole de que los complementos del gestor de complementos no forman parte oficialmente de FreeCAD. Pulsa el botón **OK** para confirmar y continuar.
3.  Se abre el cuadro de diálogo del Gestor complementos. Para más información ver [Opciones](#Opciones.md).
4.  El botón **<img src="images/Button_valid.svg" width=16px> Actualizar todo** no funciona en este momento.
5.  Pulse el botón **<img src="images/Process-stop.svg" width=16px> Cerrar** para cerrar el cuadro de diálogo.
6.  Si has instalado o actualizado un ambiente de trabajo se abrirá un nuevo cuadro de diálogo informando de que tienes que reiniciar FreeCAD para que los cambios surtan efecto.


</div>

## Opciones

<img alt="" src=images/AddonManager_Main.png  style="width   *600px;">

1.  The Addon manager provides two view layouts   * \"Condensed\" and \"Expanded\". In \"Condensed\" view, each addon takes a single line, and its description is truncated to fit the available space. \"Expanded\" shows additional details, including more of the description text as well as maintainer information, more installation details, etc.
2.  Three different types of addons are supported   * [workbenches](external_workbenches.md), [macros](macros.md), and [preference packs](Preference_Packs.md). You can choose to show just one type, or all of them in a single list.
3.  The list can be limited to show just installed packages, just packages with available updates, or just packages that are not yet installed.
4.  The list can be filtered, searching for a keyword in the title, description, and tags (description and tags must be specified by the addon developer in their addon\'s metadata). The filter can even be a regular expression, for fine-grained control of the exact search term.
5.  The expanded view shows available version information, description, maintainer information, and installation version information, for packages that provide a [package metadata](Package_Metadata.md) file (or for macros with embedded metadata).
6.  Addon data is cached locally, with a variable cache update frequency set in the user preferences.
7.  At any time you can choose to manually update your local cache to see the latest updates available for each addon.
8.  Update checks may be set up to be automatic, or done manually via a button click (configured in user preferences). If GitPython and git are installed on your system then update information is fetched using git. If not, then update information is obtained from any present metadata file.

Clicking on an addon in this view brings up the addon\'s Details page   *

<img alt="" src=images/AddonManager_Details.png  style="width   *600px;">

The details page shows buttons allowing installing, uninstalling, updating, and temporarily disabling an addon. For installed addons it lists the currently installed version and the installation date, and whether that is the most recent version available. Below is an embedded web browser window showing the addon\'s README page (for workbenches and preference packs), or Wiki page (for macros).

## Preferences

The preferences for the Addon manager can be found in the [Preferences Editor](Preferences_Editor#Addon_Manager.md). <small>(v0.20)</small> 

## Notas


<div class="mw-translate-fuzzy">

-   El uso de los complementos no está restringido a la versión de FreeCAD desde la que fueron instalados. También podrás utilizarlos en cualquier otra versión de FreeCAD, soportada por el complemento, que puedas tener en tu sistema.
-   Los complementos disponibles en el gestor complementos no son parte del programa oficial de FreeCAD y no están soportados por el equipo de desarrollo de FreeCAD. Debes leer la información proporcionada cuidadosamente para asegurarte de que sabes lo que estás instalando.
-   Los informes de errores y las peticiones de características deben hacerse directamente al creador del addon visitando el sitio web indicado. Muchos desarrolladores de complementos son usuarios habituales del [foro de FreeCAD](https   *//forum.freecadweb.org), y también pueden ser contactados allí.
-   Si el paquete [GitPython](https   *//github.com/gitpython-developers/GitPython) está instalado en tu ordenador, el gestor complementos lo utilizará, haciendo que las descargas sean más rápidas.
-   También puedes instalar complementos manualmente. Ver [Cómo instalar ambientes de trabajo adicionales](How_to_install_additional_workbenches/es.md) y [Cómo instalar macros](How_to_install_macros/es.md).


</div>

## Información para desarrolladores 

See [Addon](Addon#Information_for_developers.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/es
