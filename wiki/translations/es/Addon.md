# Addon/es
## Introducción

En FreeCAD y en esta documentación, un [complemento](addon/es.md) es cualquier componente que no es parte de la instalación base, pero que puede ser añadido al sistema por ciertos métodos.

## Diferentes tipos 

Existen tres tipos de complementos:

-   [Macros](Macros/es.md): breve fragmento de código [Python](Python/es.md) que proporciona una nueva herramienta o funcionalidad en un único archivo que termina en `.FCMacro`.
-   [Ambiente de trabajo](External_workbenches/es.md): colecciones de archivos Python que proporcionan [Comandos Gui](Gui_Command/es.md) relacionados (herramientas) centradas en un tema concreto, por ejemplo, herramientas para diseñar armarios, o herramientas para trabajar con arquitectura, o herramientas para diseñar barcos, etc. Estos bancos de trabajo suelen definir nuevas barras de herramientas donde los [comandos](Gui_Command/es.md) se colocan como botones.
-   [Paquetes de preferencias](Preference_Packs/es.md): colecciones de preferencias de usuario distribuibles. <small>(v0.20)</small> 

## Instalación

La forma recomendada de instalar los complementos es con el <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestor complementos](Std_AddonMgr/es.md).

Pero para macros y ambientes de trabajo la instalación manual sigue siendo posible.

-   [Cómo instalar macros](How_to_install_macros/es.md)
-   [Instalar más ambientes de trabajo](Installing_more_workbenches/es.md)

## Información para desarrolladores 

Si ha desarrollado una macro o un ambiente de trabajo y desea verlo incluido en el administrador de complementos, lea cómo hacerlo en las páginas del repositorio: ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) y [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). Si agrega su macro a la página [Recetas de macros](Macros_recipes.md), no hay nada más que hacer, el administrador de complementos la recogerá automáticamente.

See also:

-   [Distribution of a Python workbench](Workbench_creation#Distribution.md)
-   [Distribution of a C++ workbench](Workbench_creation#Distribution_2.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/es
