# Compile on Docker/de
}









## Überblick

Unter den Möglichkeiten, FreeCAD zu bauen und zu installieren, gibt es die Möglichkeit, Docker zu verwenden. Diese Methode ist vor allem für FreeCAD Entwickler nützlich, die Linux oder Mac OS Rechner verwenden.



### Vorteile

Alle Abhängigkeiten von FreeCAD sind bereits installiert, miteinander kompatibel und entsprechend konfiguriert, so dass Du sehr schnell mit der Entwicklung beginnen kannst.

-   Die Abhängigkeiten sind im Docker Container enthalten, wodurch verhindert wird, dass unerwünschte Pakete Ihre Arbeitsstation verunreinigen und dass es zu Kollisionen von Versionen kommt.
-   Der Quellcode und die Bauverzeichnisse befinden sich außerhalb des Docker Containers. Dies erlaubt es Dir, deine bevorzugten Bearbeitungsprogramme, Versionierungssysteme, Entwicklungswerkzeuge usw. zu verwenden, ohne sie im Docker Container einrichten zu müssen. Du kannst sie einfach wie gewohnt direkt von deinem Arbeitsplatzrechner aus benutzen. (Außerdem bedeutet es, dass du den Docker Container nicht jedes Mal neu aufbauen musst, wenn du FreeCAD bauen willst).
-   Für diejenigen, die obskure \*nix Distributionen und [Gebrauchsanweisungen sind nicht verfügbar](Compile_on_Linux/de#Erhalten_der_Abhängigkeiten.md) für das Holen von Abhängigkeiten verwenden, ist alles, was du auf deinem Arbeitsplatzrechner installieren musst, ein Docker, der in vielen Distributionen recht häufig verfügbar ist.
-   Er bietet eine statische, unveränderliche Entwicklungsumgebung. Ich persönlich finde das nützlich, wenn ich bei der Entwicklung die Anzahl der potentiellen Variablen, die ein Problem verursachen könnten, reduzieren möchte. Du weist, dass du zwischen den Builds nichts Esoterisches in der Umgebung verändert hast. Für Entwickler, die zusammenarbeiten und beide den gleichen Docker Container verwenden, kannst du sicher sein, dass ihr beide von der gleichen Umgebung aus arbeitet, was Kommunikationsfehler aufgrund von Unterschieden in der Umgebung reduziert.



## Docker Repositorien 

-   Original: <https://gitlab.com/daviddaish/freecad_docker_env>
-   Offiziell: <https://GitHub.com/FreeCAD/Docker>



## Vorbedingungen

-   10GB freier Speicherplatz
-   Docker

## Installation



### Herunterladen der Quelle 

Der beste Weg, den Quellcode von FreeCAD zu erhalten, ist das Klonen des [Git Repositorium](https://github.com/FreeCAD/FreeCAD). Dazu benötigst du das `git` Programm, das in den meisten Linux und Mac OS Distributionen einfach installiert werden kann, und es kann auch von der [offiziellen Website](http://git-scm.com/) bezogen werden.

Dadurch wird eine Kopie der neuesten Version des FreeCAD Quellcodes in einem neuen Verzeichnis namens `freecad_source` abgelegt.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git ~/my_code/freecad_source
}}

Weitere Informationen über die Verwendung von Git und das Einbringen von Code in das Projekt findest Du unter [Quellcodeverwaltung](Source_code_management/de.md).

### Quellarchiv

Alternativ kannst du den Quellcode als [archive](https://github.com/FreeCAD/FreeCAD/releases/latest), eine `.zip` oder `.tar.gz` Datei herunterladen und in das gewünschte Verzeichnis entpacken.



### Erstelle ein Build Verzeichnis 

Erstelle ein Verzeichnis, das deine kompilierten FreeCAD Quellen enthält.


{{Code|lang=bash|code=
mkdir ~/my_code/freecad_build
}}



### Docker Abbild ziehen 

Ziehe das Docker Abbild. (Offizielle Bild kommt bald.)


{{Code|lang=bash|code=
docker pull registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}



### Zugriff auf deinen Windowmanager erlauben 

Damit FreeCAD seine GUI aus dem Docker Container heraus starten kann, musst du Docker Zugriffsrechte für deinen Windowmanager geben. In den meisten Linux Distributionen ist dies das X Fenster System. Du kannst den unten stehenden Befehl verwenden, um einen pauschalen Zugriff auf X zu erlauben, bis du deinen Rechner neu startest oder dich abmeldest.


{{Code|lang=bash|code=
xhost +
}}

Wenn du mit nicht vertrauenswürdigen Systemen verbunden bist, z.B. über `ssh`, macht dich das anfällig für bösartigen Code. Schließe entweder alle `ssh` Verbindungen, oder schau dir sicherere xhost Berechtigungen an, was außerhalb des Umfanges dieses Tutorials liegt.



#### Mac OS Anwender 

Für diejenigen, die Mac OS verwenden, ist das X Fenster System möglicherweise nicht installiert. Das XQuartz Projekt ist ein seit langem laufendes quelloffenes Projekt, das es dir erlaubt, es auf deinem Computer zu installieren. [Du kannst es hier finden](https://www.xquartz.org/).



### Starte das Docker Abbild 

Weise Umgebungsvariablen zu, so dass der Docker Container den FreeCAD Quellcode und das Build Verzeichnis einhängen wird. Zusätzlich kannst du ein zusätzliches Verzeichnis einhängen, das alle Dateien enthält, die du zu Testzwecken verwenden möchtest. In dem untenstehenden Schnipsel haben wir es als dein Heimverzeichnis als einfache Standardvorgabe belassen.


{{Code|lang=bash|code=
fc_source=~/my_code/freecad_source
fc_build=~/my_code/freecad_build
other_files=~/
}}

Starte das Docker Abbild.


{{Code|lang=bash|code=
docker run -it --rm \
-v $fc_source:/mnt/source \
-v $fc_build:/mnt/build \
-v $other_files:/mnt/files \
-e "DISPLAY" -e "QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}



### FreeCAD bauen 

Du kannst FreeCAD mit dem installierten Build Skript oder mit deiner bevorzugten Methode bauen.


{{Code|lang=bash|code=
/root/build_script.sh
}}



### FreeCAD ausführen 

Sobald FreeCAD gebaut wurde, kann es wie gewohnt ausgeführt werden.


{{Code|lang=bash|code=
/mnt/build/bin/FreeCAD
}}

Du kannst die angehängten Verzeichnisse im `/mnt` Verzeichnis finden.



## Diskussion

-   [Docker env build container](https://forum.freecadweb.org/viewtopic.php?f=4&t=42954)
-   [VSCode setup with Docker (1)](https://forum.freecadweb.org/viewtopic.php?f=10&t=48266)
-   [VSCode setup with Docker (2)](https://forum.freecadweb.org/viewtopic.php?p=427812#p427812)



## Verwandt

-   [AppImage](AppImage.md)



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > Compile on Docker/de
