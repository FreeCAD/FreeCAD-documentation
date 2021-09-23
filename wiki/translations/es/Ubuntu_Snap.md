# Ubuntu Snap/es


## Introducción

Un [Ubuntu Snap](Ubuntu_Snap/es.md) paquete, o simplemente [Snap](Ubuntu_Snap/es.md) es un formato de distribución similar a [AppImage](AppImage/es.md) en el que se pretende que sea un \"paquete instalable universal\" para desplegar software en sistemas Linux. Los Snaps fueron introducidos por Ubuntu pero están pensados para ejecutarse en todas las distribuciones de Linux siempre y cuando el demonio Snap, o `snapd`, esté disponible en el sistema objetivo.

Un paquete de Snap tiene dos características principales:

-   Los programas están en una caja de arena para que no interfieran con el resto del sistema operativo.
-   Los programas se actualizan automáticamente en segundo plano para obtener la última versión de la aplicación.

Para otras formas de instalar el software, vea [Instalación en Linux](Installing_on_Linux/es.md).

## Instalación

A partir del v0.19 el uso de Snaps es experimental. Los Snaps actuales son generados y alojados por voluntarios.

En todos los sistemas donde se instalen Snaps, el demonio Snap debe ser instalado primero. El paquete se llama normalmente `snapd`.

Para Debian/Ubuntu y sistemas similares que utilizan el gestor APT el demonio se instala de la siguiente manera: {{Code|lang=bash|code=
sudo apt install snapd
}}

Para instalar la versión estable del Snap use: {{Code|lang=bash|code=
sudo snap install freecad
}}

Para instalar la versión de desarrollo del Snap use: {{Code|lang=bash|code=
sudo snap install --edge freecad-ppd
}}

## Enlaces

Más información sobre los esfuerzos actuales para tratar con Snaps.

-   [0.19 Snap previsión necesita \"probadores\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=46044), más viejo Snap de **vejmarie**
-   [Discusión: Estado del snap (paquete Snap)](https://forum.freecadweb.org/viewtopic.php?f=42&t=46853), nueva versión del Snap de **ppd**



