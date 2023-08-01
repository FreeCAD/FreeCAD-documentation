# Download/es
{{TOCright}}



## Versión estable actual 


<div class="mw-translate-fuzzy">

La versión 0.20.1 de FreeCAD (29410) fue publicada el 2022-08-10. Para conocer las novedades, consulte las [notas de lanzamiento](Release_notes_0.20/es.md).


</div>


<div class="mw-translate-fuzzy">

Encontrará checksums SHA256 para verificar la integridad de su descarga en la [página de lanzamiento](https://github.com/FreeCAD/FreeCAD/releases/tag/0.20.1).


</div>

Las versiones anteriores pueden descargarse de la página [lanzamientos](https://github.com/FreeCAD/FreeCAD/releases)

+::+::+::+
| ![](images/Windows.png )                                                                                         | ![](images/Mac.png )                                                                                                             | ![](images/Linux_with_text.png )     |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                 | [Install on Mac](Installing_on_Mac.md)                                                                                     | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD-0.20.2-WIN-x64-installer-3.exe) | [macOS 64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD_0.20.2-2022-12-27-conda-macOS-x86_64-py310.dmg) | [AppImage 64-bit](AppImage.md)             |
++++

### Notas para usuarios de Windows 

-   Las siguientes versiones de Windows son soportadas: 64-bit 7/8/10/11. Windows de 32-bit no está soportado.
-   Una versión portable que no necesita instalación está disponible en la página de [lanzamientos](https://github.com/FreeCAD/FreeCAD/releases/).
-   El paquete también puede instalarse desde el gestor [Chocolatey](https://chocolatey.org/packages/freecad).


<div class="mw-translate-fuzzy">

### Notas para usuarios de Mac OS X 

Mac OS X 10.12 *Sierra* es la versión mínima soportada.


</div>



### Notas para usuarios de GNU/Linux 

La mayoría de las distribuciones tienen FreeCAD en sus repositorios oficiales, sin embargo, si la distribución no sigue un modelo de lanzamiento rodante (rolling) la versión que proporcionan puede estar desactualizada. En su lugar, puede descargar la AppImage mostrada más arriba , marcarla como ejecutable e iniciarla sin instalación.

Por favor, consulte la página [Instalar en Linux](Installing_on_Linux/es.md) para más opciones de instalación, incluyendo paquetes diarios para Ubuntu y derivados.

Una versión portable que no necesita instalación se puede conseguir iniciando FreeCAD con estos comandos:


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Puedes encontrar más información sobre las variables de entorno de FreeCAD en [ la página de configuración](Start_up_and_Configuration#Environment_variables.md).


<div class="mw-translate-fuzzy">

## Versiones en desarrollo 

El desarrollo de FreeCAD es activo.

-   Para los usuarios de Linux, comprueben el desarrollo [AppImage](AppImage/es.md).
-   Para las compilaciones de desarrollo de MacOS y Windows y el código fuente de desarrollo, consulte la página [compositiones semanales](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Para compilar el último código fuente, vea [compilar](Compiling/es.md).


</div>



## Módulos y Macros Adicionales 


<div class="mw-translate-fuzzy">

La comunidad de FreeCAD provee una multitud de módulos y macros adicionales. Desde la versión 0.17 pueden ser instalados fácilmente dentro de FreeCAD usando el [Administrador de Complementos](Std_AddonMgr.md) <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;">.


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > Download/es
