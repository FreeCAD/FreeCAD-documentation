# Report view/es
## Introducción

La [Vista de informe](Report_view/es.md) es un panel que muestra los mensajes de texto de los procesos y herramientas de FreeCAD. Está disponible en el menú **{{StdMenu|[Vista](Std_View_Menu/es.md)** → Paneles → Vista de informe}}.

Ciertas propiedades de este panel, como el color del texto y si se muestra automáticamente en caso de advertencias o errores, se pueden configurar en la pestaña **General → Ventana de salida** del [editor de preferencias](Preferences_Editor/es.md).

<img alt="" src=images/FreeCAD_Report_view.png  style="width:800px;">



*La vista del informe que muestra los mensajes cuando FreeCAD acaba de iniciarse.*

## Mensajes


**Ver también:**

[AIP de la consola](Console_API/es.md), y [Fundamentos de scripting de FreeCAD](FreeCAD_Scripting_Basics/es.md).

La vista de informe muestra mensajes de la clase interna de FreeCAD `Console`.

-    `FreeCAD.Console.PrintMessage("text")`, imprime cualquier tipo de mensaje informativo, que no implique ningún mal comportamiento; por ejemplo, imprime las coordenadas de los puntos, el resultado de un cálculo de distancia, el número de vértices de una forma, etc. Por defecto, en color negro.

-    `FreeCAD.Console.PrintWarning("text")`, imprime mensajes que pretenden advertir al usuario sobre comportamientos extraños en la aplicación. Las advertencias deben mostrarse cuando falta alguna funcionalidad pero el software sigue funcionando aceptablemente. Por defecto, en color amarillo.

-    `FreeCAD.Console.PrintError("text")`, imprime mensajes que pretenden ser mensajes de error, es decir, cuando falta un componente crítico que hace fallar una determinada operación. Por defecto, en color rojo.

-    `FreeCAD.Console.PrintLog("text")`, imprimir los mensajes que van a los registros. Estos mensajes pueden ser cualquier cosa que sea valiosa para solucionar un problema en el futuro mediante la lectura de los registros, por ejemplo, iniciar o cerrar un banco de trabajo. Por defecto, en color azul.

Estas funciones pueden usarse desde la [consola de Python](Python_console/es.md) directamente, o desde [macros](Macros/es.md) y ambientes de trabajo personalizados.

<img alt="" src=images/FreeCAD_Report_view_example.png  style="width:800px;">



*Ejemplos de mensajes en la vista del informe: un mensaje general, una advertencia, un error y un mensaje registrado.*

## Acciones

Al hacer clic con el botón derecho del ratón en la vista del informe se muestran algunos comandos:

-    **Opciones**: registro, advertencia, error, redirigir la salida de Python, redirigir los errores de Python, ir al final.

-    **Copiar**: almacena el texto seleccionado en el portapapeles para su posterior pegado; se desactiva si no hay nada seleccionado.

-    **Seleccionar todo**: selecciona todo el texto en la vista del informe.

-    **Borrar**: borra todos los mensajes de la vista del informe. Esto es útil si quiere solucionar un problema con una herramienta que imprime mensajes en la vista del informe, y quiere estar seguro de que no hay mensajes antiguos de herramientas anteriores.

-    **Guardar como**: guarda los mensajes de la vista de informe en un archivo de texto.


{{Interface navi

}} {{Std Base navi}}

---
[documentation index](../README.md) > Report view/es
