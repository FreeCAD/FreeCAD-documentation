# Gui Command/es
<div class="mw-translate-fuzzy">

Los comandos de la interfaz gráfica de usuario (GuiCommand) son una de las funciones más importantes de FreeCAD en el principal punto de interacción del usuario. Cada vez que el usuario selecciona un elemento del menú o presiona un botón de una barra de herramientas se activa un comando de la interfaz gráfica de usuario. Alguno de los atributos de un comandos de la interfaz gráfica de usuario (GuiCommand) son:

-   Define un nombre
-   Contiene un icono
-   Define el alcance para deshacer/rehacer
-   Tiene una página de ayuda
-   Abre y controla letreros de diálogo
-   Grabación de macros
-   etc\...


</div>


<div class="mw-translate-fuzzy">

### Denominación

Los comandos de la interfaz gráfica de usuario se denominan de cierta forma: *ModuleName\_CommandName* Por ejemplo \"Base\_Open\" este es el comando Abrir de la interfaz gráfica de usuario en el sistema base. Los comandos de la interfaz gráfica de usuario en un módulo determinado se denominan con el nombre del módulo como prefijo. Por ejemplo \"Part\_Cylinder\".


</div>


<div class="mw-translate-fuzzy">

Si la documentación no está terminada utiliza la plantilla [Template:UnfinishedDocu](Template_UnfinishedDocu.md)


</div>


<div class="mw-translate-fuzzy">

### Página de ayuda 

Todos los comandos de la interfaz gráfica de usuario deben tener una página de ayuda. La página de ayuda está alojada en la wiki de documentación de FreeCAD. El artículo tiene el mismo nombre que el comando de la interfaz gráfica de usuario. Por ejemplo [Draft ShapeString](Draft_ShapeString/es.md).


</div>


<div class="mw-translate-fuzzy">

Para crear tus propias páginas de ayuda puedes utilizar la plantilla: [GuiCommand model](GuiCommand_model.md)


</div>


<div class="mw-translate-fuzzy">

Ejemplo:

-   [Draft ShapeString](Draft_ShapeString/es.md)
-   [Draft Line](Draft_Line/es.md)


</div>


<div class="mw-translate-fuzzy">

### Iconos

<img alt="" src=images/Tango-Palette.png  style="width:400px;">


</div>


<div class="mw-translate-fuzzy">

Todos los comandos de la interfaz gráfica de usuario deben tener un icono. Utilizamos la [Colección de iconos Tango](http://tango.freedesktop.org/Tango_Desktop_Project) y sus recomendaciones. A la derecha puedes ver la paleta de colores del proyecto Tango.


</div>


<div class="mw-translate-fuzzy">

Preferiblemente todos los iconos serán dibujados en formato de Gráficos Vectoriales Escalables (SVG) por ejemplo con [Inkscape](http://inkscape.org). Esto hace que sea más sencillo aplicar cambios y crear iconos adicionales similares en el mismo espacio de la aplicación.


</div>

### Icons color coding chart 

<img alt="" src=images/Colorchart.png  style="width:200px;">

We try as much as possible to respect this chart, so the color of the icons has a direct meaning.


<div class="mw-translate-fuzzy">

### Requerimientos de Calidad 

Existen muchos comandos de la interfaz gráfica de usuario (operaciones) en FreeCAD que son experimentales o utilizados brevemente con propósitos de implementación. Estos comandos de la interfaz gráfica de usuario están la mayoría en los entornos de trabajo dedicados como los de Piezas, Mallas o Mecanizado (CAM). Para asegurar una buena experiencia al usuario se ha creado el entorno de trabajo *Completo*. Este es el entorno de trabajo de inicio por defecto de FreeCAD e incorpora todos los comandos de la interfaz gráfica de usuario que cumplan con ciertos **Requerimientos de Calidad** los cuales se describen aquí:


</div>

There are a lot of GuiCommands (tools) in FreeCAD which are experimental or used for a short time to test implementation of new features. These GuiCommands are mostly in the dedicated workbenches like Part, Mesh or Cam. To ensure a good user experience the workbench *Complete* was created. This workbench incorporates all GuiCommands which meet certain quality requirements which are described here:


<div class="mw-translate-fuzzy">

-   El comando/operación debe estar **terminado**. No en desarrollo!
-   Debe tener una **página de ayuda** como [esta](Std_ViewScreenShot/es.md)
    -   Todos los campos de la plantilla [Template:GuiCommand](Template_GuiCommand.md) deben estar cubiertos
    -   Una imagen de los letreros de diálogo que el comando eventualmente muestra
    -   Descripción detallada del comando y de todos sus parámetros y configuración
    -   Descripción de las interfaces de Python relacionadas y las clases con código de ejemplo
-   Definir un icono apropiado y la posición en los menús


</div>


<div class="mw-translate-fuzzy">

Se espera que esto sea cierto para todos los comandos de la interfaz gráfica de usuario en la [Lista de comandos](List_of_Commands/es.md).


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Gui Command/es
