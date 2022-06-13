# Addon/es
{{TOCright}}

## Introducción

En FreeCAD y en esta documentación, un [complemento](addon/es.md) es cualquier componente que no es parte de la instalación base, pero que puede ser añadido al sistema por ciertos métodos.

## Diferentes tipos 


<div class="mw-translate-fuzzy">

Existen aproximadamente tres tipos de addons   *

-   [Macro](Macros/es.md)   * breve fragmento de código [Python](Python/es.md) que proporciona una nueva herramienta o funcionalidad en un único archivo que termina en `.FCMacro`.
-   Módulo   * un único archivo fuente de Python, o una colección de archivos de Python, que amplía el software de alguna manera. Los módulos no definen necesariamente un \"ambiente de trabajo\" gráfico, pero pueden proporcionar una característica de apoyo, por ejemplo, una biblioteca que realiza la conversión de formatos, o el código que modifica la [interfaz](interface/es.md) gráfica.
-   [Ambiente de trabajo](External_workbenches/es.md)   * colecciones de archivos Python que proporcionan [Comandos Gui](Gui_Command/es.md) relacionados. (herramientas) centradas en un tema concreto, por ejemplo, herramientas para diseñar armarios, o herramientas para trabajar con arquitectura, o herramientas para diseñar barcos, etc. Estos bancos de trabajo suelen definir nuevas barras de herramientas donde los [comandos](Gui_Command/es.md) se colocan como botones.


</div>

## Instalación


<div class="mw-translate-fuzzy">

A partir de FreeCAD 0.17, la forma recomendada de instalar los complementos es con el <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestor complementos](Std_AddonMgr/es.md).


</div>


<div class="mw-translate-fuzzy">

Sin embargo, la instalación manual sigue siendo posible.

-   [Cómo instalar macros](How_to_install_macros/es.md)
-   [Instalar más ambientes de trabajo](Installing_more_workbenches/es.md)


</div>

## Information for developers 

If you have developed a macro or workbench, and want to see it included in the Addon manager, read how to do so on the repository pages   * ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

### Python workbenches 

For Python workbenches, you don\'t need any specific approval to have your workbench added to the Addon Manager. In addition, because your Addon is outside the FreeCAD source code, you can choose the license you want. If you request for your workbench to be added to the Addon Manager\'s default list (we will not add any new workbench without a request from its authors), either by asking so on the forum or by opening an issue on the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository, your code will stay on your own git repository, we will just add it as a submodule to the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository. Of course, before adding your workbench, we will take a look at it and make sure there is nothing potentially problematic with it. For more details about structuring your Addon, including information about metadata used by the Addon Manager, see [Workbench creation](Workbench_creation.md).

### C++ workbenches 

If you develop a workbench in C++, it cannot be run directly by users and must be compiled first. You then have two options, either you provide precompiled versions of your workbench yourself, for the different operating systems, or you should request to have your code merged into the FreeCAD source code. For that, you should use the LGPL license (or a fully compatible license like MIT or BSD), and you must present your new tools to the community in the [FreeCAD forum](https   *//forum.freecadweb.org) for review. Once your code has been tested and approved, you should fork the FreeCAD repository, if not done yet, create a new branch, push your code to it, and open a pull request so that your branch is merged into the main repository.




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/es
