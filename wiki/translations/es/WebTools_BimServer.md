---
- GuiCommand:
   Name:WebTools BimServer
   Name/es:HerramientasWeb BimServer
   MenuLocation:Herramientas Web - BIM server
   Workbenches:[HerramientasWeb](WebTools_Workbench/es.md)
---

# WebTools BimServer/es


<div class="mw-translate-fuzzy">


**A partir de FreeCAD v0.17, esta herramienta se ha eliminado del Ambiente de trabajos Arquitectura y ahora forma parte del [Ambiente de trabajos HerramientasWeb](WebTools_Workbench/es.md) externo que puedes instalar a través del menú Herramientas → <img src="images/AddonManager.svg" width=24px>. [Administrador de complementos](Std_AddonMgr/es.md).
**


</div>

## Descripción

Este comando permite interactuar con una instancia de [BIMServer](http://www.bimserver.org), abrir archivos almacenados en el servidor BIM y guardar nuevas revisiones de esos archivos. BIMServer es un sistema de servidor gratuito y de código abierto hecho para trabajar con archivos IFC. En su estado actual, permite gestionar proyectos con múltiples archivos IFC y gestionar las revisiones. Su sistema de base de datos altamente extensible y su arquitectura de plugins también permiten diseñar herramientas avanzadas de consulta/validación y flujos de trabajo de fusión inteligentes.

Para utilizar este comando, se deben cumplir las siguientes condiciones:

-   Los módulos Python **json** y **requests** deben estar instalados en tu sistema
-   Necesitas tener acceso a una instancia de BIMServer (lee la [BIMServer documentation](https://github.com/opensourceBIM/BIMserver/wiki) para instalar un BIMServer localmente), y tener credenciales (login y contraseña) para ese servidor. En el momento de escribir esto, la versión estable de BIMServer es la 1.4, pero te recomendamos que instales una de las versiones beta 1.5.X disponibles, que instala muchos plugins automáticamente (en la versión 1.4 tienes que instalar los plugins manualmente).
-   Todas las transferencias de archivos con el BIMServer se hacen con archivos IFC. Por lo tanto, es necesario saber trabajar con [Archivos IFC](Arch_IFC/es.md).

## Utilización

1.  Asegúrate de que se cumplen los requisitos anteriores y de que tienes acceso a una instancia de BIMServer en funcionamiento.
2.  Selecciona el menú **Herramientas Web → <img src="images/WebTools_BimServer.svg" width=16px> [BIM Server](WebTools_BimServer/es.md)
**
3.  Pulse el botón **Conectar** y rellene los datos de sus credenciales.
4.  Una vez realizada la conexión con el BIMServer, elige un proyecto con el que trabajar en el cuadro desplegable **Proyecto**

## Opciones

![](images/Arch_Bimserver_panel.jpg )

-   Si es la primera vez que te conectas a un BIMServer desde FreeCAD, pulsa el botón **Conectar**\', y rellena la URL del servidor, tu login (que siempre es una dirección de correo electrónico) y tu contraseña en el cuadro de diálogo que aparecerá. Si deseas conectarte automáticamente la próxima vez que utilices el comando BimServer, marca la opción **guardar credenciales** (tu nombre de usuario y contraseña no son guardados por FreeCAD, sólo una cookie de sesión).
-   Una vez que FreeCAD se ha conectado con éxito a una instancia de BIMServer, el botón **Conectar**\' se convertirá en **Conectado**\'. Haga clic en el botón de nuevo para desconectarse. Esto también borrará la cookie de sesión almacenada, por lo que tendrá que introducir sus credenciales de nuevo la próxima vez.
-   Para borrar la cookie de sesión manualmente y restablecer todo, puedes simplemente borrar la URL de BIMServer almacenada en **Edición → Preferencias → Arquitectura → BimServer**.
-   El botón **Abrir en el navegador** abrirá la interfaz web de BIMServer bien en el navegador web interno de FreeCAD, o, si has marcado esa opción en **Edición → Preferencias → Arquitectura → BimServer**, en un navegador web externo. Esto permite, por ejemplo, crear nuevos proyectos, o analizar los contenidos almacenados en el BIMServer.

### Descarga revisiones 

-   El cuadro desplegable **Proyecto** mostrará los proyectos disponibles almacenados en el BIMServer. Elija uno para ver las revisiones disponibles para ese proyecto.
-   Selecciona una revisión y haz clic en **Abrir** para descargar y abrir el archivo IFC correspondiente a esa revisión en FreeCAD.
-   Al pulsar el botón **Abrir**, se abrirá un cuadro de diálogo que te permitirá guardar el archivo IFC descargado en una ubicación de tu elección antes de abrirlo. Si pulsas **Cancelar**, el archivo se guardará con un nombre temporal en el directorio temporal del sistema.

### Carga revisiones 

-   Si desea cargar una nueva revisión, asegúrese de que se ha seleccionado el proyecto correcto en el cuadro desplegable **Proyecto**.
-   Elija el **Objeto raíz**\' que desea cargar. Debe ser un [Arquitectura Site](Arch_Site/es.md) o un [Arquitectura Edificio](Arch_Building/es.md). Sólo se subirán los objetos que pertenezcan a ese objeto raíz.
-   Escribe un **Comentario**\', que será la descripción (nombre) de la revisión.
-   Pulse el botón **Subir**. Se abrirá un cuadro de diálogo que le permitirá guardar el archivo IFC producido en una ubicación de su elección antes de cargarlo. Si pulsa **Cancelar**, el archivo se guardará con un nombre temporal en el directorio temporal del sistema.



---
![](images/Button_right.svg) [documentation index](../README.md) > WebTools BimServer/es
