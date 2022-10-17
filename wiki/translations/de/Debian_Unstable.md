# Debian Unstable/de
[Debian Unstable](https   *//wiki.debian.org/DebianUnstable) ist eine rollierende Distribution, die für [Debian Entwicklung](Debian_development/de.md) verwendet wird und für fortgeschrittene Benutzer in der FreeCAD Entwicklung und Paketierung empfohlen wird. Neue Pakete sind bereit, sobald sie hochgeladen und erstellt wurden, es sei denn, der Uploader hat sie für [Debian Experimental](https   *//wiki.debian.org/DebianExperimental) markiert, was eine explizite Installation (nach einigen Einstellungen, um die zusätzliche Verbreitung zu ermöglichen) über  erfordert.

Häufig sollten Leute, die Debian Testen verwenden, tatsächlich Debian Instabil verwenden; Debian Testen sollte nur als \"QA Versionshülle\" betrachtet werden, da es zwar stabiler zu sein scheint als Instabil, aber tatsächlich einen Nachteil hat. Neue Pakete werden zu Debian Instabil hochgeladen und nach einiger Zeit zu Testen migriert, so dass Sicherheitskorrekturen und wichtige Paketänderungen unangemessen verzögert werden können.

Es gibt zwei Schlüsselfaktoren für eine funktionierende Benutzererfahrung in Instabil. Die erste besteht darin, sudo apt full-upgrade oder seine Entsprechungen niemals blind auszuführen, ohne vorher die Ergebnisse der Operation zu überprüfen. Wenn es heißt, dass Sie Hunderte von MB Speicherplatz freigeben werden, gibt es einen Paketwechsel, der einen Großteil Ihres Systems entfernt. Stattdessen kann man sudo apt upgrade sicher ausführen und neue Pakete beziehen. Manchmal führt dies dazu, dass Pakete zurückgehalten werden, was bedeutet, dass es angebracht sein kann, full-upgrade auszuführen, da die Deinstallation von Paketen tatsächlich notwendig sein kann.

Der zweite Schlüssel ist, sich bewusst zu sein, dass du an der Debian Entwicklung teilnimmst, und die entsprechenden Werkzeuge und Methoden zu verwenden. Zum Beispiel kann das bedeuten, Pakete wie apt-listbugs oder apt-listchanges zu installieren oder Debian Mailinglisten wie [debian-devel-announce@lists.debian.org](https   *//lists.debian.org/debian-devel-announce/) zu abonnieren.

Obwohl Debian Instabil perfekt als langfristiger täglicher Treiber geeignet ist, ist es auch sehr einfach, in einer virtuellen Maschine zu laufen, wo Ausfälle keine so große Sache sind. Lade einfach eine Debian Test ISO herunter, installiere sie in eine VM und aktualisiere sie, und bearbeite sie dann /etc/apt/sources.list, um so etwas zu enthalten wie    *

deb [http   *//ftp.us.debian.org/debian/](http   *//ftp.us.debian.org/debian/) testing main contrib non-free
# deb-src [http   *//ftp.us.debian.org/debian/](http   *//ftp.us.debian.org/debian/) testing main contrib non-free
deb [http   *//security.debian.org/debian-security](http   *//security.debian.org/debian-security) testing/updates main contrib non-free
# deb-src [http   *//security.debian.org/debian-security](http   *//security.debian.org/debian-security) testing/updates main contrib non-free
deb [http   *//ftp.us.debian.org/debian/](http   *//ftp.us.debian.org/debian/) unstable main contrib non-free
# deb-src [http   *//ftp.us.debian.org/debian/](http   *//ftp.us.debian.org/debian/) unstable main contrib non-free

Wenn du Pakete aus Experimentell aktivieren möchtest, stelle dies in /etc/apt/sources.list.d/experimental.list   *

deb [http   *//deb.debian.org/debian](http   *//deb.debian.org/debian) experimental main contrib non-free
# deb-src [http   *//deb.debian.org/debian](http   *//deb.debian.org/debian) experimental main contrib non-free




[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > Debian Unstable/de
