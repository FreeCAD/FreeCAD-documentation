# Ubuntu Snap/de
{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

Ein [Ubuntu Snap](Ubuntu_Snap/de.md) Paket oder einfach nur [Snap](Ubuntu_Snap/de.md) ist ein Distributionsformat, das dem [AppImage](AppImage/de.md) insofern ähnelt, als es als \"universell installierbares Paket\" für die Bereitstellung von Software in Linux Systemen gedacht ist. Snaps wurden von Ubuntu eingeführt, aber sie sollen in allen Linux Distributionen laufen, solange der Snap Daemon, oder `snapd`, im Zielsystem verfügbar ist.


</div>


<div class="mw-translate-fuzzy">

Ein Snap Paket hat zwei Hauptmerkmale   *

-   Programme sind in einem Sandkasten untergebracht, so dass sie den Rest Ihres Betriebssystems nicht stören.
-   Programme werden automatisch im Hintergrund aktualisiert, um die neueste Version der Anwendung zu erhalten.


</div>

Weitere Möglichkeiten zur Installation der Software siehe [Installation unter Linux](Installing_on_Linux/de.md).

## Einrichtung


<div class="mw-translate-fuzzy">

Ab v0.19 ist die Verwendung von Snaps experimentell. Die aktuellen Snaps werden von Freiwilligen generiert und bereitgestellt.


</div>


<div class="mw-translate-fuzzy">

In allen Systemen, in denen Snaps installiert werden sollen, muss zuerst der Snap Daemon installiert werden. Das Paket heißt normalerweise `snapd`.


</div>

### Debian/Ubuntu

Für Debian/Ubuntu und ähnliche Systeme, die den APT Verwalter verwenden, wird der Daemon wie folgt installiert   *


{{Code|lang=bash|code=
sudo apt install snapd
}}

Um die stabile Version des Snap zu installieren, verwende


{{Code|lang=bash|code=
sudo snap install freecad
}}

Um die Entwicklungsversion des Snap zu installieren, verwende   *


{{Code|lang=bash|code=
sudo snap install --edge freecad
}}

### Manjaro

To install the stable version of the Snap use   *


{{Code|lang=bash|code=
snap install freecad
}}

To install the development version of the Snap use   *


{{Code|lang=bash|code=
snap install --edge freecad
}}

## Notes

#### What FC version am I running 

To figure out which development version is installed type the following in the Command-line interface   *


{{Code|lang=bash|code=
snap info freecad
}}

#### Changing between different Snaps 

Starting from the tail end of the v0.20 release cycle, the FreeCAD snap maintainers added the ability to test experimental FreeCAD builds. Snaps allow for this by easily toggling between different snaps (terminology is \'[channels or tracks](https   *//snapcraft.io/docs/channels)\'). For example   *

Testing the Topological Naming (\'toponaming\') branch (created at the start of the v0.21/v1.0 release cycle)   *


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge/toponaming
}}

Using the `refresh` command will switch and update the snap channel you\'re switching to   *


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge/toponaming
}}

Toggling back to the nightly \'edge\' channel   *


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge
}}

## Advanced

The following commands are geared towards users that are familiar with `git` and have a locally cloned repository of the upstream FreeCAD repository.


{{Code|lang=bash|code=
git clone https   *//github.com/FreeCAD/FreeCAD
cd FreeCAD/
}}

To find out the latest upstream revision number (also known as \'HEAD\')   *


{{Code|lang=bash|code=
git pull upstream master  # first make sure we have the most up-to-date commits
git rev-list --count HEAD # 'HEAD' refers to the current commit you are viewing (tip of the master branch)
}}

To translate the current snap development version in to a revision number (make sure you\'re within your cloned FreeCAD repository as mentioned above)   *


{{Code|lang=bash|code=
snap info freecad <nowiki>|</nowiki>\
grep -e '^\s\+latest/edge' <nowiki>|</nowiki>\
awk -F ' ' '{ print $2 }' <nowiki>|</nowiki>\
xargs -I{} git rev-list --count {}
}}

**Note   *** the above bash script 1 liner assumes user has \'edge\' (nightly) installed

The difference between HEAD and the snap edge revision numbers indicates the amount of revisions trailing behind upstream the snap development (edge) is.

Taking it a step further, if you want a short summary of the commits between the current snap edge and HEAD   *


{{Code|lang=bash|code=
snap info freecad <nowiki>|</nowiki>\
grep -e '^\s\+latest/edge' <nowiki>|</nowiki>\
awk -F ' ' '{ print $2 }' <nowiki>|</nowiki>\
xargs -I{} git log --oneline --ancestry-path {}..HEAD
}}

**Note   *** The output will indicate what commits **are not** in the current \'edge\' (but will be on the next nightly update).

## Verweise


<div class="mw-translate-fuzzy">

Weitere Informationen über die aktuellen Bemühungen, mit Snaps umzugehen.

-   [0.19 Snap Vorschau benötigt \"Tester\"](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=46044), ältere Snap von **vejmarie**
-   [Diskussion   * Zustand des Snap (Snap Pakete)](https   *//forum.freecadweb.org/viewtopic.php?f=42&t=46853), neuere Version des Snap von **ppd**


</div>

### Repositories

-   <https   *//github.com/FreeCAD/FreeCAD-snap>
-   <https   *//snapcraft.io/freecad>

### Maintainer(s)

-   ppd ([forum](https   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=24042), [github](https   *//github.com/ppd))
-   luzpaz ([forum](https   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=12229), [github](https   *//github.com/luzpaz))

## Related

-   [AppImage](AppImage.md) - another self-contained \'binary\' like format to run FreeCAD
-   [Flatpak](Flatpak.md) packages



[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > Ubuntu Snap/de
