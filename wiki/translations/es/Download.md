 {{TOCright}}

## Actual Versión Estable {#actual_versión_estable}

La primera versión 0.19.2 de FreeCAD (24291) fue publicada el 22 abril 2021. Para conocer las novedades, consulta las [notas de lanzamiento](Release_notes_0.18/es.md).

Encontrará checksums SHA256 para verificar la integridad de su descarga en el [página de lanzamiento](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).

Las versiones anteriores pueden descargarse de la página [lanzamientos](https://github.com/FreeCAD/FreeCAD/releases)

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| [64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-installer1.exe) (includes installer) |   | [macOS](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD_0.19-24291-macOS-x86_64-conda.dmg) 64-bit |   | [AppImage](AppImage.md) 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+

### Notas para usuarios de Windows {#notas_para_usuarios_de_windows}

-   El instalador 32-Bit (x86) admite las siguientes versiones de Windows: 7/8/10.
-   El instalador 64-Bit (x64) admite las siguientes versiones de Windows: 7/8/10.
-   Una versión portátil ([64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)) que no necesita instalación está en la página de lanzamiento.
-   El paquete también puede instalarse desde el gestor [Chocolatey](https://chocolatey.org/packages/freecad).

### Notas para usuarios de Mac OS X {#notas_para_usuarios_de_mac_os_x}

Mac OS X 10.12 *Sierra* es la versión mínima que está soportada.

### Notas para usuarios de GNU/Linux {#notas_para_usuarios_de_gnulinux}

La mayoría de las distribuciones llevan FreeCAD en sus repositorios oficiales, sin embargo, si la distribución no sigue un modelo de lanzamiento rodante la versión que proporcionan puede estar desactualizada. En su lugar, puede descargar la AppImage mostrada mas arriba , marcarla como ejecutable e iniciarla sin instalación.

Por favor, consulte la página [Instalar en Linux](Installing_on_Linux/es.md) para más opciones de instalación, incluyendo paquetes diarios para Ubuntu y derivados.

Una versión portátil que no necesita instalación se puede conseguir iniciando FreeCAD con estos comandos: {{Version/es|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```

Puedes encontrar más información sobre las variables de entorno de FreeCAD en [la página de configuración](Start_up_and_Configuration/es#Variables_de_entorno.md).

## Versiones en desarrollo {#versiones_en_desarrollo}

El desarrollo de FreeCAD es activo.

-   Para los usuarios de Linux, comprueben el desarrollo [AppImage](AppImage/es.md).
-   Para las compilaciones de desarrollo de MacOS y Windows y el código fuente de desarrollo, consulte la página [compositiones semanales](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Para compilar el último código fuente, vea [compilar](Compiling/es.md).

## Módulos y Macros Adicionales {#módulos_y_macros_adicionales}

La comunidad de FreeCAD provee una multitud de módulos y macros adicionales. Desde el 0.17 pueden ser instalados fácilmente desde dentro de FreeCAD usando el [Gestor de Addon](AddonManager/es.md)<img alt="" src=images/AddonManager.svg  style="width:22px;">.



