# Download/es
{{TOCright}}

## Versión estable actual 

La versión 0.19.3 de FreeCAD (24366) fue publicada el 04 de diciembre de 2021. Para conocer las novedades, consulta las [notas de lanzamiento](Release_notes_0.19/es.md).

Encontrará checksums SHA256 para verificar la integridad de su descarga en la [página de lanzamiento](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.19.3).

Las versiones anteriores pueden descargarse de la página [lanzamientos](https   *//github.com/FreeCAD/FreeCAD/releases)

+   *   *+---+   *   *+---+   *   *+
| ![](images/Windows.png )                                                                                                    |   | ![](images/Mac.png )                                                                                          |   | ![](images/AppImage-logo.png )         |
|                                                                                                                                   |   |                                                                                                                 |   |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                            |   | [Install on Mac](Installing_on_Mac.md)                                                                  |   | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                                   |   |                                                                                                                 |   |                                                    |
| [64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD-0.19.3-WIN-x64-installer-4.exe) (includes installer) |   | [macOS 64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD_0.19.3-OSX-x86_64-conda.dmg) |   | [AppImage 64-bit](AppImage.md)             |
++---++---++

### Notas para usuarios de Windows 

-   Las siguientes versiones de Windows son soportadas   * 7/8/10/11.
-   Una versión portable que no necesita instalación está disponible en la poágina de [lanzamientos](https   *//github.com/FreeCAD/FreeCAD/releases/).
-   El paquete también puede instalarse desde el gestor [Chocolatey](https   *//chocolatey.org/packages/freecad).

### Notas para usuarios de Mac OS X 

Mac OS X 10.12 *Sierra* es la versión mínima soportada.

### Notas para usuarios de GNU/Linux 

La mayoría de las distribuciones tienen FreeCAD en sus repositorios oficiales, sin embargo, si la distribución no sigue un modelo de lanzamiento rodante (rolling) la versión que proporcionan puede estar desactualizada. En su lugar, puede descargar la AppImage mostrada más arriba , marcarla como ejecutable e iniciarla sin instalación.

Por favor, consulte la página [Instalar en Linux](Installing_on_Linux/es.md) para más opciones de instalación, incluyendo paquetes diarios para Ubuntu y derivados.

Una versión portable que no necesita instalación se puede conseguir iniciando FreeCAD con estos comandos   * <small>(v0.19)</small>  
```python
cd ruta/al/directorio_que__contiene_AppImage/
chmod +x ./FreeCAD_0.19-24366-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-24366-Linux-Conda_glibc2.12-x86_64.AppImage
```

Puedes encontrar más información sobre las variables de entorno de FreeCAD en [ la página de configuración](Start_up_and_Configuration#Environment_variables.md).

## Versiones en desarrollo 

El desarrollo de FreeCAD es activo.

-   Para los usuarios de Linux, comprueben el desarrollo [AppImage](AppImage/es.md).
-   Para las compilaciones de desarrollo de MacOS y Windows y el código fuente de desarrollo, consulte la página [compositiones semanales](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Para compilar el último código fuente, vea [compilar](Compiling/es.md).

## Módulos y Macros Adicionales 

La comunidad de FreeCAD provee una multitud de módulos y macros adicionales. Desde la versión 0.17 pueden ser instalados fácilmente dentro de FreeCAD usando el [Administrador de Complementos](Std_AddonMgr.md) <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;">.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/es
