

## Einführung

Ein [Ubuntu Snap](Ubuntu_Snap/de.md) Paket oder einfach nur [Snap](Ubuntu_Snap/de.md) ist ein Distributionsformat, das dem [AppImage](AppImage/de.md) insofern ähnelt, als es als \"universell installierbares Paket\" für die Bereitstellung von Software in Linux Systemen gedacht ist. Snaps wurden von Ubuntu eingeführt, aber sie sollen in allen Linux Distributionen laufen, solange der Snap Daemon, oder `snapd`, im Zielsystem verfügbar ist.

Ein Snap Paket hat zwei Hauptmerkmale:

-   Programme sind in einem Sandkasten untergebracht, so dass sie den Rest Ihres Betriebssystems nicht stören.
-   Programme werden automatisch im Hintergrund aktualisiert, um die neueste Version der Anwendung zu erhalten.

Weitere Möglichkeiten zur Installation der Software siehe [Installation unter Linux](Installing_on_Linux/de.md).

## Einrichtung

Ab v0.19 ist die Verwendung von Snaps experimentell. Die aktuellen Snaps werden von Freiwilligen generiert und bereitgestellt.

In allen Systemen, in denen Snaps installiert werden sollen, muss zuerst der Snap Daemon installiert werden. Das Paket heißt normalerweise `snapd`.

Für Debian/Ubuntu und ähnliche Systeme, die den APT Verwalter verwenden, wird der Daemon wie folgt installiert: {{Code|lang=bash|code=
sudo apt install snapd
}}

Um die stabile Version des Snap zu installieren, verwende {{Code|lang=bash|code=
sudo snap install freecad
}}

Um die Entwicklungsversion des Snap zu installieren, verwende: {{Code|lang=bash|code=
sudo snap install --edge freecad-ppd
}}

## Verweise

Weitere Informationen über die aktuellen Bemühungen, mit Snaps umzugehen.

-   [0.19 Snap Vorschau benötigt \"Tester\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=46044), ältere Snap von **vejmarie**
-   [Diskussion: Zustand des Snap (Snap Pakete)](https://forum.freecadweb.org/viewtopic.php?f=42&t=46853), neuere Version des Snap von **ppd**



