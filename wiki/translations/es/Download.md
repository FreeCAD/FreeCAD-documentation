# Download/es
## Versión estable actual 


<div class="mw-translate-fuzzy">

La versión 0.21.1 de FreeCAD fue publicada el 2023-09-01. Para conocer las novedades, consulte las [notas de lanzamiento](Release_notes_0.21/es.md).


</div>


<div class="mw-translate-fuzzy">

Encontrará sumas de verificación SHA256 para comprobar la integridad de su descarga en la [página de lanzamiento](https://github.com/FreeCAD/FreeCAD/releases/tag/0.21.1).


</div>

Las versiones anteriores pueden descargarse de la página [lanzamientos](https://github.com/FreeCAD/FreeCAD/releases)

+::+::+::+
| ![](images/Windows.png )                                                                                                | ![](images/Mac.png )                                                                                                | ![](images/Linux_with_text.png )                                                                        |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [Install instructions](Installing_on_Windows.md)                                                                      | [Install instructions](Installing_on_Mac.md)                                                                  | [Install instructions](Installing_on_Linux.md)                                                                |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-WIN-x64-installer-1.exe)        | [ARM (M1/M2) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-arm64.dmg)  | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-x86_64.AppImage)   |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Windows-x86_64.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-intel-x86_64.dmg) | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-aarch64.AppImage) |
++++



### Notas para usuarios de Windows 

-   Las siguientes versiones de Windows son soportadas: 64-bit 7/8/10/11. Windows de 32-bit no está soportado.
-   Una versión portable que no necesita instalación está disponible en la página de [lanzamientos](https://github.com/FreeCAD/FreeCAD/releases/).
-   El paquete también puede instalarse desde el gestor [Chocolatey](https://chocolatey.org/packages/freecad).



### Notas para usuarios de macOS 

-   Mac OS X 10.12 *Sierra* es la versión mínima soportada.
-   Para macOS 12 y anteriores la \"imagen de disco Intel sin firmar\" debe ser usada, la versión firmada no funciona en esos sistemas.



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



## Versiones de desarrollo 

El desarrollo de FreeCAD es activo.

-   Para lanzamientos de desarrollo y código fuente de desarrollo, véa la página [lanzamientos semanales](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).
-   Para compilar el último código fuente, vea [compilar](Compiling/es.md).



## Módulos y Macros Adicionales 

La comunidad de FreeCAD provee una multitud de módulos y macros adicionales. Desde la versión 0.17 pueden ser instalados fácilmente dentro de FreeCAD usando el <img alt="" src=images/:Std_AddonMgr.svg  style="width:24px;"> [Administrador de Complementos](Std_AddonMgr.md).



---
⏵ [documentation index](../README.md) > Download/es
