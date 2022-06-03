# Git buildpackage/de
Moderne Debian Entwicklungs Arbeitsabläufe beinhalten [Paketerstellung mit Git](https   *//wiki.debian.org/PackagingWithGit) und das primäre Werkzeug dafür ist [git-buildpackage](http   *//honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html). git-buildpackage bietet einen Befehl gbp mit mehreren Optionen ähnlich dem Befehl git selbst. Viele dieser Befehle sind selbst nur ein Hülle von untergeordneten Debian Werkzeugen, so dass die Komplexität beim Erlernen von Paketerstellung ziemlich hoch sein kann.

Um das zu umgehen, hier sind die kurzen und einfachen Schritte, um mit dem git-buildpackage zu beginnen. Dies sollte auf fast jeder Debian basierten Distribution funktionieren, aber ich empfehle, in einer sauberen und separaten Umgebung eine [Debian Instabil](Debian_Unstable/de.md) virtuelle Maschine zu betreiben.

1.  Installiere es mit sudo apt install git-buildpackage.
2.  Schnapp dir die Punktdateien am Ende dieser Seite. Du wirst es brauchen   * ~/.gbp.conf, ~/.pbuilderrc, und ~/.quiltrc.
3.  Der Paketaufbau erfolgt in einer sauberen Umgebung. Erstelle es mit sudo git-pbuilder create.
4.  Finde die URL eines Pakets, das Du erstellen möchtest, auf <https   *//salsa.debian.org>, der selbst gehosteten GitLab Instanz des Debian Projekts.
5.  Erstelle einen Klon davon mit 
6.  Gib das Verzeichnis des geklonten Repos mit cd ein.
7.  Den Build mit gbp buildpackage ausführen -us -uc
8.  Wenn es fertig ist, befinden sich deine Pakete bei ../build-area/.

##### gbp.conf

Location   * ~/.gbp.conf

<https   *//gitlab.com/kkremitzki/dotfiles/blob/master/.gbp.conf>

##### pbuilderrc

Location   * ~/.pbuilderrc

<https   *//gitlab.com/kkremitzki/dotfiles/blob/master/.pbuilderrc>

##### pbuilderrc 

Location   * ~/.pbuilderrc

<https   *//gitlab.com/kkremitzki/dotfiles/blob/master/.quiltrc>


 

[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > Git buildpackage/de
