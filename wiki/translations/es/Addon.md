# Addon/es
## Introducción

En FreeCAD y en esta documentación, un [complemento](addon/es.md) es cualquier componente que no es parte de la instalación base, pero que puede ser añadido al sistema por ciertos métodos.

## Diferentes tipos 

Existen aproximadamente tres tipos de addons:

-   [Macro](Macros/es.md): breve fragmento de código [Python](Python/es.md) que proporciona una nueva herramienta o funcionalidad en un único archivo que termina en `.FCMacro`.
-   Módulo: un único archivo fuente de Python, o una colección de archivos de Python, que amplía el software de alguna manera. Los módulos no definen necesariamente un \"ambiente de trabajo\" gráfico, pero pueden proporcionar una característica de apoyo, por ejemplo, una biblioteca que realiza la conversión de formatos, o el código que modifica la [interfaz](interface/es.md) gráfica.
-   [Ambiente de trabajo](External_workbenches/es.md): colecciones de archivos Python que proporcionan [Comandos Gui](Gui_Command/es.md) relacionados. (herramientas) centradas en un tema concreto, por ejemplo, herramientas para diseñar armarios, o herramientas para trabajar con arquitectura, o herramientas para diseñar barcos, etc. Estos bancos de trabajo suelen definir nuevas barras de herramientas donde los [comandos](Gui_Command/es.md) se colocan como botones.

Las macros se instalan en el directorio `Macro/` del usuario, mientras que los módulos y los ambientes de trabajo están en el directorio `Mod/`. {{Code|lang=bash|code=
$HOME/.FreeCAD/Macro/
$HOME/.FreeCAD/Mod/
}}

Las macros suelen comenzar como una forma de simplificar o automatizar la tarea de dibujar o editar un objeto concreto. Si muchas de estas macros se reúnen dentro de un directorio, y se proporciona una estructura para recoger esas herramientas, entonces todo el directorio puede distribuirse como un ambiente de trabajo.

En otras palabras, las macros, los módulos y las ambientes de trabajo son esencialmente lo mismo, piezas de código Python que amplían la instalación base. Las macros suelen ser cortas y se centran en una sola tarea, los módulos suelen proporcionar nuevas funciones o interfaces, y las ambientes de trabajo son colecciones de herramientas (botones, menús) e interfaces gráficas para realizar tareas relacionadas.

Si un ambiente de trabajo está suficientemente desarrollado y está bien documentado, puede ser incluido como uno de los [Ambientes de trabajo](workbenches/es.md) base en FreeCAD.

## Instalación

A partir de FreeCAD 0.17, la forma recomendada de instalar los complementos es con el <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestor complementos](Std_AddonMgr/es.md).

Sin embargo, la instalación manual sigue siendo posible.

-   [Cómo instalar macros](How_to_install_macros/es.md)
-   [Instalar más ambientes de trabajo](Installing_more_workbenches/es.md)




[<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md)

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/es
