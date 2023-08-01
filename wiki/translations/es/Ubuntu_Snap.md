# Ubuntu Snap/es
## Introducción


<div class="mw-translate-fuzzy">

Un [Ubuntu Snap](Ubuntu_Snap/es.md) paquete, o simplemente [Snap](Ubuntu_Snap/es.md) es un formato de distribución similar a [AppImage](AppImage/es.md) en el que se pretende que sea un \"paquete instalable universal\" para desplegar software en sistemas Linux. Los Snaps fueron introducidos por Ubuntu pero están pensados para ejecutarse en todas las distribuciones de Linux siempre y cuando el demonio Snap, o `snapd`, esté disponible en el sistema objetivo.


</div>


<div class="mw-translate-fuzzy">

Un paquete de Snap tiene dos características principales:

-   Los programas están en una caja de arena para que no interfieran con el resto del sistema operativo.
-   Los programas se actualizan automáticamente en segundo plano para obtener la última versión de la aplicación.


</div>

Para otras formas de instalar el software, vea [Instalación en Linux](Installing_on_Linux/es.md).

## Instalación


<div class="mw-translate-fuzzy">

A partir del v0.19 el uso de Snaps es experimental. Los Snaps actuales son generados y alojados por voluntarios.


</div>


<div class="mw-translate-fuzzy">

En todos los sistemas donde se instalen Snaps, el demonio Snap debe ser instalado primero. El paquete se llama normalmente `snapd`.


</div>

### Debian/Ubuntu

Para Debian/Ubuntu y sistemas similares que utilizan el gestor APT el demonio se instala de la siguiente manera:


{{Code|lang=bash|code=
sudo apt install snapd
}}

Para instalar la versión estable del Snap use:


{{Code|lang=bash|code=
sudo snap install freecad
}}

Para instalar la versión de desarrollo del Snap use:


{{Code|lang=bash|code=
sudo snap install --edge freecad
}}

### Manjaro

To install the stable version of the Snap use:


{{Code|lang=bash|code=
snap install freecad
}}

To install the development version of the Snap use:


{{Code|lang=bash|code=
snap install --edge freecad
}}

## Notes

#### What FC version am I running 

To figure out which development version is installed type the following in the Command-line interface:


{{Code|lang=bash|code=
snap info freecad
}}

#### Changing between different Snaps 

Starting from the tail end of the v0.20 release cycle, the FreeCAD snap maintainers added the ability to test experimental FreeCAD builds. Snaps allow for this by easily toggling between different snaps (terminology is \'[channels or tracks](https://snapcraft.io/docs/channels)\'). For example:

Testing the Topological Naming (\'toponaming\') branch (created at the start of the v0.21/v1.0 release cycle):


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge/toponaming
}}

Using the `refresh` command will switch and update the snap channel you\'re switching to:


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge/toponaming
}}

Toggling back to the nightly \'edge\' channel:


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge
}}

## Advanced

The following commands are geared towards users that are familiar with `git` and have a locally cloned repository of the upstream FreeCAD repository.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD/
}}

To find out the latest upstream revision number (also known as \'HEAD\'):


{{Code|lang=bash|code=
git pull upstream master  # first make sure we have the most up-to-date commits
git rev-list --count HEAD # 'HEAD' refers to the current commit you are viewing (tip of the master branch)
}}

To translate the current snap development version in to a revision number (make sure you\'re within your cloned FreeCAD repository as mentioned above):


{{Code|lang=bash|code=
snap info freecad <nowiki>|</nowiki>\
grep -e '^\s\+latest/edge' <nowiki>|</nowiki>\
awk -F ' ' '{ print $2 }' <nowiki>|</nowiki>\
xargs -I{} git rev-list --count {}
}}

**Note:** the above bash script 1 liner assumes user has \'edge\' (nightly) installed

The difference between HEAD and the snap edge revision numbers indicates the amount of revisions trailing behind upstream the snap development (edge) is.

Taking it a step further, if you want a short summary of the commits between the current snap edge and HEAD:


{{Code|lang=bash|code=
snap info freecad <nowiki>|</nowiki>\
grep -e '^\s\+latest/edge' <nowiki>|</nowiki>\
awk -F ' ' '{ print $2 }' <nowiki>|</nowiki>\
xargs -I{} git log --oneline --ancestry-path {}..HEAD
}}

**Note:** The output will indicate what commits **are not** in the current \'edge\' (but will be on the next nightly update).

## Enlaces


<div class="mw-translate-fuzzy">

Más información sobre los esfuerzos actuales para tratar con Snaps.

-   [0.19 Snap previsión necesita \"probadores\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=46044), más viejo Snap de **vejmarie**
-   [Discusión: Estado del snap (paquete Snap)](https://forum.freecadweb.org/viewtopic.php?f=42&t=46853), nueva versión del Snap de **ppd**


</div>

### Repositories

-   <https://github.com/FreeCAD/FreeCAD-snap>
-   <https://snapcraft.io/freecad>

### Maintainer(s)

-   ppd ([forum](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=24042), [github](https://github.com/ppd))
-   luzpaz ([forum](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=12229), [github](https://github.com/luzpaz))

## Related

-   [AppImage](AppImage.md) - another self-contained \'binary\' like format to run FreeCAD
-   [Flatpak](Flatpak.md) packages



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > Ubuntu Snap/es
