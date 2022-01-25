# PCB Workbench/es
## Introducción


{{TOCright}}

[Placas de Circuitos Impreso](https://es.wikipedia.org/wiki/Circuito_impreso) Ambiente de trabajo para FreeCAD (PCB)

Ambiente de trabajo de placas de circuitos impresos flexibles para FreeCAD (PCB)

Módulo que permite importar/crear placas de circuito impreso en FreeCAD. Alcance del módulo:

-   soporte para muchas capas diferentes,
-   posibilidad de elegir colores, transparencia y nombres para cada capa,
-   el módulo permite importar modelos IGES/STP con colores,
-   posibilidad de mostrar agujeros/vías independientes

## Referencias

-   Autor: marmni
-   Página de inicio: <https://sourceforge.net/projects/eaglepcb2freecad/>
-   Código fuente en github: <https://github.com/marmni/FreeCAD-PCB>

## Herramientas

Para una descripción detallada del uso del ambiente de trabajo, véase **index.pdf** en el código fuente o [manual](https://raw.githubusercontent.com/marmni/FreeCAD-PCB/master/index.pdf)

Barra de herramientas

![](images/PCB-menu-orizz.png )

Menú desplegable

![](images/PCB-export-BOM.png ) ![](images/PCB-export-hole.png ) ![](images/PCB-create-new.png ) ![](images/PCB-explode.png ) ![](images/PCB-bounding-box.png )

## Instalación

### Instalación automática 

Este ambiente de trabajo se puede instalar desde el [Gestor de complementos](Std_AddonMgr/es.md).

### Para GitHub 

**Prerrequisitos**

FreeCAD-PCB requiere la versión 0.18 o superior de FreeCAD y la versión 2.7 o superior de Python.

**Instrucciones de instalación en Linux** (de GitHub)

Descomprima el archivo zip descargado y copie la carpeta extraída al directorio donde está instalado FreeCAD (subcarpeta Mod).

Ejemplo:

-   Ruta de FreeCAD:

 ~/Programs/FreeCAD

-   Copiar mod a la carpeta

 ~/Programs/FreeCAD/Mod

-   También puede copiar los archivos en la carpeta

 ~/.FreeCAD/Mod

-   A continuación, cambie el permiso de lectura/escritura a 777. ¡Por favor, no olvide el parámetro -R!

Ejemplo:

 chmod 777 -R PCB

**Instrucciones de instalación en Windows** (de GitHub)

Descomprima el archivo zip descargado y copie la carpeta extraída a la dirección donde está instalado FreeCAD (subcarpeta Mod).

Ejemplo:

-   Ruta de FreeCAD:

 C:/Archivos de programa/FreeCAD-0.18

-   Así que copie el mod a la carpeta

 C:/Archivos de Programa/FreeCAD-0.18/Mod

-   A continuación cambie el permiso de lectura/escritura para todos los usuarios. Haga clic en el botón derecho de la carpeta PCB y elija Propiedades → Seguridad → Editar → Usuarios y marcas.

Seguridad → Editar → Usuarios y marque todas las casillas de verificación en la opción \'Permitir\'.

**Instrucciones de instalación en MacOS** (de GitHub)

## Enlaces a FreeCAD-PCB Ambiente de trabajo 

-   Wiki del ambiente de trabajo: [Ambiente de trabajo xternal](https://wiki.freecadweb.org/External_workbenches)
-   FreeCAD Wiki: [Página principal de la Wiki](https://wiki.freecadweb.org/Main_Page)
-   FreeCAD Foro: [EaglePCB importador para FreeCAD](http://forum.freecadweb.org/viewtopic.php?f=9&t=5107)
-   Tutoriales:
-   Videos: [EaglePCB\_2\_FreeCAD - FreeCAD odczyt plików brd z programu Eagle](https://www.youtube.com/watch?v=81NsljRJx8c&feature=youtu.be)
-   Files: [PCB biblioteca](https://github.com/marmni/FreeCAD-PCB-library)
-   Informe de errores: Por favor, informe de los errores en <https://github.com/marmni/FreeCAD-PCB/issues>

## Otros enlaces útiles 

-   [EaglePCB en sourceforge](https://sourceforge.net/projects/eaglepcb2freecad/)
-   [Recetas de macros](Macros_recipes/es.md)
-   [Descarga FreeCAD](Download/es.md)
-   [Portal de la comunidad FreeCAD](FreeCAD_Community_Portal/es.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sandbox](Category_Sandbox.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > PCB Workbench/es
