# Manual:Installing/de
{{Manual:TOC/de}}

FreeCAD verwendet die [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) Lizenz; Du darfst FreeCAD herunterladen, installieren, weitergeben und verwenden, wie du willst, unabhängig von der Art der Arbeit, die du damit machst (kommerziell oder nicht kommerziell). Du bist an keine Klausel oder Einschränkungen gebunden, und die Dateien, die du damit erstellst, gehören dir vollständig. Das einzige, was die Lizenz wirklich verbietet, ist zu behaupten, dass Sie FreeCAD selbst programmiert haben!

FreeCAD verhält sich unter Windows, Mac OS und Linux gleich. Allerdings unterscheidet sich die Art und Weise der Installation je nach Plattform leicht. Unter Windows und Mac stellt die FreeCAD-Community vorkompilierte Pakete (Installierer) zum Download bereit; unter Linux wird der Quellcode den Maintainern der Linux Distributionen zur Verfügung gestellt, die dann für die Paketierung von FreeCAD für ihre spezifische Distribution verantwortlich sind. Daher können Sie unter Linux FreeCAD in der Regel direkt aus der Software-Manager-Anwendung heraus installieren.

Die offizielle FreeCAD Downloadseite für Windows und Mac OS ist <https://github.com/FreeCAD/FreeCAD/releases>

**FreeCAD Versionen**

Die offiziellen Versionen von FreeCAD, die Sie auf der oben genannten Seite und im Softwaremanager Ihrer Distribution finden, sind stabile Versionen. Die Entwicklung von FreeCAD geht jedoch schnell voran! Fast täglich kommen neue Funktionen und Fehlerbehebungen hinzu. Da zwischen den stabilen Versionen oft eine lange Zeit liegt, könntest du daran interessiert sein, eine modernere Version von FreeCAD auszuprobieren. Diese Entwicklungsversionen oder Vorabversionen werden von Zeit zu Zeit auf die oben erwähnte [Downloadseite](https://github.com/FreeCAD/FreeCAD/releases) hochgeladen, oder, wenn du Ubuntu oder Fedora verwenden, die FreeCAD Gemeinschaft unterhält auch [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Persönliche Paketarchive) und [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) \'tägliche Builds\', die regelmäßig mit den neuesten Änderungen aktualisiert werden.

Wenn du FreeCAD in einer virtuellen Maschine installierst, sei dir bitte bewusst, dass die Leistung aufgrund der Grenzen der [OpenGL](https://en.wikipedia.org/wiki/OpenGL) Unterstützung auf den meisten virtuellen Maschinen schlecht (in einigen Fällen unbenutzbar) sein kann.

## Installation unter Windows 

1.  Lade ein Installationspaket (.exe) entsprechend deiner Windows Version (32bit oder 64bit) von der [Downloadseite](https://github.com/FreeCAD/FreeCAD/releases) herunter. Die FreeCAD Installationsprogramme sollten auf jeder Windows Version ab Windows 7 funktionieren.
2.  Doppelklicke auf das heruntergeladene Installationsprogramm.
3.  Akzeptiere die Bedingungen der LGPL Lizenz, dies wird einer der wenigen Fälle sein, in denen Du wirklich, sicher auf den \"Akzeptieren\" Knopf klicken kannst, ohne den Text zu lesen. Keine versteckten Klauseln: ![](images/Freecad-windows-install-01.jpg )
4.  Du kannst den Standardpfad hier belassen oder auf Wunsch ändern: ![](images/Freecad-windows-install-02.jpg )
5.  Du brauchst die PYTHONPATH Variable nicht zu setzen, es sei denn, du hast vor, fortgeschrittene Python Programmierung zu machen, in diesem Fall weißt du wahrscheinlich schon, wofür das gedacht ist: ![](images/Freecad-windows-install-03.jpg )
6.  Während der Installation werden einige zusätzliche Komponenten, die im Installer gebündelt sind, ebenfalls installiert: ![](images/Freecad-windows-install-04.jpg )
7.  Das war\'s, FreeCAD ist installiert. Du findest es in deinem Startmenü. ![](images/Freecad-windows-install-05.jpg )

**Installation einer Entwicklungsversion**

Das Zusammenstellen von FreeCAD und das Erstellen eines Installationsprogramms erfordert einige Zeit und Engagement, daher werden Entwicklungsversionen (auch als Vorabversionen bezeichnet) normalerweise als .zip (oder .7z) Archive bereitgestellt. Diese müssen nicht installiert werden; entpacke sie einfach und starte FreeCAD durch einen Doppelklick auf die darin enthaltene FreeCAD.exe-Datei. Dies ermöglicht es dir auch, die stabile und die \"instabile\" Version zusammen auf dem gleichen Computer zu behalten.

### Installation unter Linux 

Auf den meisten modernen Linux Distributionen (Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary, usw.) kann FreeCAD per Knopfdruck direkt aus der Software-Verwaltungsanwendung deiner Distribution installiert werden (das Aussehen kann sich von den untenstehenden Abbildungen unterscheiden, jede Distribution verwendet ihr eigenes Werkzeug).

1.  Öffne den Softwaremanager und suche nach \"freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Klicke auf die Schaltfläche \"Installieren\" und das war\'s, FreeCAD wird installiert. Vergiss nicht, es danach zu bewerten!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">

**Alternative Wege**

Eine der großen Freuden bei der Verwendung von Linux ist die Vielzahl an Möglichkeiten zur Anpassung deiner Software, also schränke dich nicht ein. Unter Ubuntu und Derivaten kann FreeCAD auch von einem [PPA](https://launchpad.net/~freecad-maintainers) installiert werden, das von der FreeCAD Gemeinschaft betreut wird (es enthält sowohl stabile als auch Entwicklungsversionen). Auf Fedora können aktuelle Entwicklungsversionen von FreeCAD von [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) installiert werden, und da es sich um Open Source Software handelt, kannst du auch einfach [Kompiliere FreeCAD selbst](Compiling/de.md).

### Installation unter Mac OS 

Die Installation von FreeCAD unter Mac OSX ist heutzutage genauso einfach wie auf anderen Plattformen. Da es jedoch weniger Leute in der Community gibt, die einen Mac besitzen, hinken die verfügbaren Pakete manchmal ein paar Versionen hinter den anderen Plattformen her.

1.  Lade ein deiner Version entsprechendes gezipptes Paket von der [Downloadseite](https://github.com/FreeCAD/FreeCAD/releases) herunter.
2.  Öffne den Ordner Downloads und entpacke die heruntergeladene zip Datei: ![](images/Freecad-mac-01.jpg )
3.  Ziehe die FreeCAD Anwendung aus der zip Datei in den Ordner Anwendungen: ![](images/Freecad-mac-02.jpg )
4.  Das war\'s, FreeCAD ist installiert! ![](images/Freecad-mac-03.jpg )

5\. Wenn das System den Start von FreeCAD aufgrund eingeschränkter Berechtigungen für Anwendungen, die nicht aus dem App Store kommen, verhindert, musst Du dies in den Systemeinstellungen aktivieren: ![](images/Freecad-mac-04.jpg )

### Deinstallation

Hoffentlich willst du FreeCAD nicht deinstallieren, aber es ist gut zu wissen, wie. Unter Windows und Linux ist die Deinstallation von FreeCAD sehr einfach. Unter Windows verwendest du die Standardoption \"Software entfernen\" in der Systemsteuerung; unter Linux entfernst du es mit demselben Software Manager, mit dem du es installiert hast. Unter Mac OS entfernst du sie einfach aus dem Ordner \"Programme\".

### Setzen der Grundeinstellungen 

Sobald FreeCAD installiert ist, möchtest du es vielleicht öffnen und einige Einstellungen ändern. Die Einstellungen in FreeCAD befinden sich im Menü **Bearbeiten → Einstellungen**. Im Folgenden sind einige grundlegende Einstellungen aufgelistet, die du eventuell ändern möchtest; Du kannst durch die Einstellungsseiten blättern, um zu sehen, ob es noch etwas anderes gibt, das du ändern möchtest.

1.  **Sprache**\': (Kategorie *Allgemein*, Reiter *Allgemein*) FreeCAD wählt automatisch die Sprache deines Betriebssystems aus, aber vielleicht möchtest du das ändern. FreeCAD ist fast vollständig in fünf oder sechs Sprachen übersetzt; andere sind derzeit nur teilweise übersetzt. Du kannst einfach [Hilf bei der Übersetzung von FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
2.  **Auto-Lademodul**: (Kategorie *Allgemein*, Reiter *Allgemein*) Normalerweise zeigt FreeCAD zunächst die Startseite an. Du kannst dies überspringen und eine FreeCAD Sitzung direkt im Arbeitsbereich deiner Wahl starten, die unter *Startup*, *Auto-Lademodul nach dem Start* aufgelistet ist. [Workbenches/de](Workbenches/de.md) wird ausführlich im [nächstes Kapitel](Manual:The_FreeCAD_Interface/de.md) erklärt.
3.  **Erstelle neues Dokument beim Start**: (Kategorie *Allgemein*, Reiter *Dokument*) Kombiniert mit der *Auto-Lademodul* Option oben, wenn diese angehakt ist, startet FreeCAD betriebsbereit. ![](images/Freecad-basic-options02.jpg )
4.  **Speicheroptionen**: (Kategorie *Allgemein*, Reiter *Dokument*) Wie jede komplexe Anwendung enthält FreeCAD wahrscheinlich Fehler, die es gelegentlich zum Absturz bringen. Hier kannst Du Optionen konfigurieren, die dir helfen, deine Arbeit im Falle eines Absturzes wiederherzustellen.
5.  **Autor und Lizenz**: (Kategorie *Allgemein*, Reiter *Dokument*) Hier stellst du die Werte ein, die für neue Dateien, die du erstellst, verwendet werden sollen. Berücksichtige, deine Dateien von Anfang an tauschbar zu machen, indem du eine benutzerfreundlichere [copyleft](https://en.wikipedia.org/wiki/Copyleft) Lizenz wie [Creative Commons](https://creativecommons.org/) verwendest.
6.  **Interne Python Meldungen umleiten**: (Kategorie *Allgemein*, Reiter *Ausgabefenster*) Es ist immer gut diese beiden Optionen anzuhaken, da sie dazu führen, dass Meldungen des internen Python Interpreters im [Ausgabefenster](Manual:The_FreeCAD_Interface#Report_view.md) angezeigt werden, wenn es ein Problem beim Ausführen eines Python Skripts gibt. ![](images/Freecad-basic-options03.jpg )
7.  **Einheiten**: (Kategorie *Allgemein*, Reiter *Einheiten*) Hier kannst du das Standard Einheitensystem einstellen, das du verwenden möchtest. ![](images/Freecad-basic-options04.jpg )
8.  \'\'\'Zoom am Mauszeiger \'\'\': (Kategorie *Anzeige* , Reiter *3D*) Wenn gesetzt, werden Zoomoperationen am Mauszeiger fokussiert. Wenn nicht gesetzt, ist das Zentrum der aktuellen Ansicht der Zoom Fokus.
9.  **Zoom umkehren**: (Kategorie *Anzeige* , Reiter *3D*) Kehrt die Richtung des Zooms relativ zur Mausbewegung um. ![](images/FreeCAD-v0-18-Preferences-Display.png )

## Installieren zusätzlicher Inhalte 

Da das FreeCAD Projekt und seine Gemeinschaft schnell wächst, und auch weil es einfach zu erweitern ist, beginnen externe Beiträge und Nebenprojekte von Gemeinschaftsmitgliedern und anderen Enthusiasten überall im Internet zu erscheinen. Die meisten dieser externen Projekte sind Arbeitsbereiche oder Makros, und können einfach direkt aus FreeCAD heraus über den [Addon-Manager](Std_AddonMgr/de.md) im Menü **Werkzeuge** installiert werden. Der Addon Manager erlaubt es z.B. viele interessante Komponenten zu installieren:

1.  Eine [Teilebibliothek](https://github.com/FreeCAD/FreeCAD-library), die alle Arten von nützlichen Modellen oder Modellteilen enthält, die von FreeCAD Anwendern erstellt wurden und in deinen Projekten frei verwendet werden kann. Die Bibliothek kann direkt aus deiner FreeCAD Installation heraus verwendet und aufgerufen werden.
2.  [Zusätzliche Arbeitsbereiche](https://github.com/FreeCAD/FreeCAD-addons), die die Funktionalität von FreeCAD für bestimmte Aufgaben erweitern, z.B. für die Animation von Teilen deiner Modelle oder Bereichen, wie z.B. Blechbiegen oder BIM. Weitere Erläuterungen zu den einzelnen Arbeitsbereichen und den darin enthaltenen Werkzeugen findest du auf jeder Addon Seite, die du durch einen Klick auf den entsprechenden Link im Addon Manager aufrufen kannst.
3.  Eine [Sammlung von Makros](https://github.com/FreeCAD/FreeCAD-macros), die auch [im FreeCAD-Wiki](Macros_recipes/de.md) zusammen mit einer Dokumentation über deren Verwendung verfügbar sind.

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

Wenn du das Ubuntu Betriebssystem benutzt, sind einige der oben genannten Addons auch als Pakete auf der [FreeCAD Addons PPA](https://launchpad.net/freecad-extras) verfügbar.

**Weiterlesen**

-   [Weitere Herunterladeoptionen](Download/de.md)
-   [FreeCAD PPA für Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [FreeCAD Erweiterungs PPA für Ubuntu](https://launchpad.net/freecad-extras)
-   [Kompiliere FreeCAD selbst](Compiling/de.md)
-   [FreeCAD Übersetzungen](https://crowdin.com/project/freecad)
-   [FreeCAD github Seite](https://github.com/FreeCAD)
-   [Der FreeCAD Erweiterungsverwalter](Std_AddonMgr/de.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/de
