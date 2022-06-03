# Installing on Mac/es
FreeCAD puede instalarse en macOS desde un paquete .dmg que puedes arrastrar y soltar en tu carpeta de aplicaciones   *


{{DownloadMacStable}}

y la composición semanal puede descargarse de

<img alt="" src=images/Nightly.png  style="width   *30px;">[Semanal](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

También puede utilizar un gestor de paquetes como HomeBrew para mantener su software actualizado. Las instrucciones para instalar HomeBrew pueden verse [aquí](https   *//brew.sh/). Cuando HomeBrew esté instalado puedes simplemente instalar FreeCAD 0.18.4 a través de tu terminal bash con


```python
brew install --cask freecad
```

y para utilizar la última versión disponible (0.19pre) en HomeBrew puede ejecutar


```python
brew install freecad
```

Si hay algún problema con el HomeBrew Cask o Formula, puede informar de ello a [aquí](https   *//github.com/FreeCAD/homebrew-freecad).

Esta página describe el uso y las características del instalador de FreeCAD. También incluye instrucciones de desinstalación. Una vez instalado, puedes [empezar](Getting_started/es.md)!

## Instalación simple 

El instalador de FreeCAD se proporciona como un paquete de aplicaciones (.app) incluido en un archivo de imagen de disco.

Puedes descargar el último instalador desde la página [Descarga](Download/es.md). Una vez descargado el archivo, sólo tienes que montar la imagen de disco y arrastrarla a la carpeta de aplicaciones o a una carpeta de tu elección.

![](images/mac_installer_1.png )

Eso es todo.Solo da clic sobre app para ejecutar FreeCAD. Si tu tienes este mensaje \"FreeCAD can\'t be open as it is from unidentified developer.\" Abre la carpeta (Application) y da clic derecho sobre app luego da clic en abrir y acepta abrir la aplicación.

## Desinstalación

Actualmente no hay un desinstalador para FreeCAD instalado con el paquete dmg. Para eliminar completamente FreeCAD y todos los componentes instalados, arrastre los siguientes archivos y carpetas a la Papelera   *

-   En /Aplicaciones   *
    -   FreeCAD

Si instalaste FreeCAD con homebrew simplemente usa el comando `brew uninstall freecad`. Eso es todo.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Mac/es
