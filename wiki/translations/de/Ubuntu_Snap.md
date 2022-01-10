# Ubuntu Snap/de
{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

Ein [Ubuntu Snap](Ubuntu_Snap/de.md) Paket oder einfach nur [Snap](Ubuntu_Snap/de.md) ist ein Distributionsformat, das dem [AppImage](AppImage/de.md) insofern ähnelt, als es als \"universell installierbares Paket\" für die Bereitstellung von Software in Linux Systemen gedacht ist. Snaps wurden von Ubuntu eingeführt, aber sie sollen in allen Linux Distributionen laufen, solange der Snap Daemon, oder `snapd`, im Zielsystem verfügbar ist.


</div>


<div class="mw-translate-fuzzy">

Ein Snap Paket hat zwei Hauptmerkmale:

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

Für Debian/Ubuntu und ähnliche Systeme, die den APT Verwalter verwenden, wird der Daemon wie folgt installiert:


{{Code|lang=bash|code=
sudo apt install snapd
}}

Um die stabile Version des Snap zu installieren, verwende


{{Code|lang=bash|code=
sudo snap install freecad
}}

Um die Entwicklungsversion des Snap zu installieren, verwende:


{{Code|lang=bash|code=
sudo snap install --edge freecad-ppd
}}

### Manjaro

To install the stable version of the Snap use:


{{Code|lang=bash|code=
snap install freecad
}}

To install the development version of the Snap use:


{{Code|lang=bash|code=
snap install --edge freecad-ppd
}}

## Notes

To figure out which development version is installed type the following in the Command-line interface:


{{Code|lang=bash|code=
snap info freecad-ppd
}}

## Advanced

The following commands are geared towards users that are familiar with git and have a locally cloned repository of the upstream FreeCAD repository.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD/
}}

To find out the latest upstream revision number (also known as \'HEAD\'):


{{Code|lang=bash|code=
git rev-list --count HEAD
}}

To translate the current snap development version in to a revision number (make sure you\'re within your cloned FreeCAD repository as mentioned above):


{{Code|lang=bash|code=
snap info freecad-ppd {{!}}

grep -e \'\^installed:\' {{!}} awk -F \' \' \'{ print \$2 }\' {{!}} cut -d\'\~\' -f2 {{!}} xargs -I{} git rev-list \--count {} }}

The difference between the numbers will tell you how many revisions behind upstream the snap development (edge) is.

## Verweise


<div class="mw-translate-fuzzy">

Weitere Informationen über die aktuellen Bemühungen, mit Snaps umzugehen.

-   [0.19 Snap Vorschau benötigt \"Tester\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=46044), ältere Snap von **vejmarie**
-   [Diskussion: Zustand des Snap (Snap Pakete)](https://forum.freecadweb.org/viewtopic.php?f=42&t=46853), neuere Version des Snap von **ppd**


</div>

-   [AppImage](AppImage.md) - another self-contained \'binary\' like format to run FreeCAD
-   [Flatpak](Flatpak.md)

---
[documentation index](../README.md) > Ubuntu Snap/de
