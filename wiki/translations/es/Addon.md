# Addon/es
{{TOCright}}

## Introducción

En FreeCAD y en esta documentación, un [complemento](addon/es.md) es cualquier componente que no es parte de la instalación base, pero que puede ser añadido al sistema por ciertos métodos.

## Diferentes tipos 

Existen tres tipos de complementos   *

-   [Macros](Macros/es.md)   * breve fragmento de código [Python](Python/es.md) que proporciona una nueva herramienta o funcionalidad en un único archivo que termina en `.FCMacro`.
-   [Ambiente de trabajo](External_workbenches/es.md)   * colecciones de archivos Python que proporcionan [Comandos Gui](Gui_Command/es.md) relacionados (herramientas) centradas en un tema concreto, por ejemplo, herramientas para diseñar armarios, o herramientas para trabajar con arquitectura, o herramientas para diseñar barcos, etc. Estos bancos de trabajo suelen definir nuevas barras de herramientas donde los [comandos](Gui_Command/es.md) se colocan como botones.
-   [Paquetes de preferencias](Preference_Packs/es.md)   * colecciones de preferencias de usuario distribuibles. <small>(v0.20)</small> 

## Instalación

La forma recomendada de instalar los complementos es con el <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestor complementos](Std_AddonMgr/es.md).

Pero para macros y ambientes de trabajo la instalación manual sigue siendo posible.

-   [Cómo instalar macros](How_to_install_macros/es.md)
-   [Instalar más ambientes de trabajo](Installing_more_workbenches/es.md)

## Información para desarrolladores 

Si ha desarrollado una macro o un ambiente de trabajo y desea verlo incluido en el administrador de complementos, lea cómo hacerlo en las páginas del repositorio   * ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) y [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). Si agrega su macro a la página [Recetas de macros](Macros_recipes.md), no hay nada más que hacer, el administrador de complementos la recogerá automáticamente.

### Ambientes de trabajo Python 

Para los ambientes de trabajo de Python, no necesita ninguna aprobación específica para agregar su banco de trabajo al Administrador de complementos. Además, debido a que su complemento está fuera del código fuente de FreeCAD, puede elegir la licencia que desee. Si solicita que su ambiente de trabajo se agregue a la lista predeterminada del administrador de complementos (no agregaremos ningún ambiente de trabajo nuevo sin una solicitud de sus autores), ya sea solicitándolo en el foro o abriendo un problema (issue) en [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/), su código permanecerá en su propio repositorio de git, solo lo agregaremos como un submódulo al repositorio [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons). Por supuesto, antes de agregar su ambiente de trabajo, lo revisaremos y nos aseguraremos de que no haya nada potencialmente problemático con él. Para obtener más detalles sobre cómo estructurar su complemento, incluyendo información sobre los metadatos utilizados por el administrador de complementos, consulte [Creación de ambiente de trabajo](Workbench_creation.md).

### Ambientes de trabajo C++ 

Si desarrolla un banco de trabajo en C++, los usuarios no pueden ejecutarlo directamente y debe compilarse primero. Entonces tiene dos opciones, usted mismo proporciona versiones precompiladas de su ambiente de trabajo, para los diferentes sistemas operativos, o debe solicitar que su código se fusione con el código fuente de FreeCAD. Para eso, debe usar la licencia LGPL (o una licencia totalmente compatible como MIT o BSD), y debe presentar sus nuevas herramientas a la comunidad en el foro de [FreeCAD](https   *//forum.freecadweb.org) para su revisión. Una vez que su código haya sido probado y aprobado, debe bifurcar (hacer fork) al repositorio de FreeCAD, si aún no lo ha hecho, cree una nueva rama, envíe su código y abra un pull request para que su rama se fusione con el repositorio principal.




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/es
