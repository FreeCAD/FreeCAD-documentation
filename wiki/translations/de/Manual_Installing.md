# Manual:Installing/de
{{Manual:TOC}}

FreeCAD ist unter der [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)-Lizenz lizensiert, die erlaubt, FreeCAD herunterzuladen, zu installieren, weiterzugeben und für jeden Zweck zu verwenden, kommerziell oder nicht kommerziell, ohne Einschränkungen. Man behält sämtliche Rechte an seinen selbsterstellten Dateien.

FreeCAD arbeitet auf gleiche Weise unter Windows, macOS und Linux, obwohl sich die Installationsprozesse der vreschiedenen Plattformen unterscheiden. Für Windows- und Mac-Anwender stellt die FreeCAD-Gemeinschaft gebrauchsfertig vorkompilierte Installationspakete bereit. Unter Linux wird der Quellcode den Betreuern der Distributionen zur Verfügung gestellt, die dann die Pakete für ihr spezielles System zusammenstellen. Normalerweise können Linux-Anwender FreeCAD direkt aus ihrer Software-Verwaltung heraus installieren.

Die offizielle FreeCAD-Downloadseite findet man unter [FreeCAD-Downloadseite](https://www.freecad.org/downloads.php?lang=de). Zusätzliche Informationen über den Installationsprozess findet man auf der zugehörigen Wiki-Seite [Herunterladen](https://wiki.freecad.org/Download/de).

**FreeCAD-Versionen**

Die offiziellen stabilen Versionen von FreeCAD stehen auf der angegebenen Download-Seite zur Verfügung und innerhalb der Software-Verwaltung der Distribution. FreeCADs Entwicklung geht schnell voran, neue Funktionen und Fehlerbereinigungen werden beinahe täglich eingearbeitet! Fast täglich kommen neue Funktionen und Fehlerbereinigungen hinzu. Da zwischen den stabilen Versionen oft eine längere Zeit vergeht, besteht vielleicht der Wunsch, eine modernere nagelneue Version von FreeCAD auszuprobieren. Diese Entwicklungsversionen oder Vorabversionen findet man auf derselben Download-Seite. Für Ubuntu- oder Fedora-Anwender stellt die Gemeinschaft [PPAs](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Persönliche Paket-Archive) und [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) \'daily builds\' bereit, die regelmäßig mit den neuesten Entwicklungen aktualisiert werden.

Ist geplant, FreeCAD auf einer virtuellen Maschine zu installieren, sollte man nicht vergessen, dass ihre Leistung beeinträchtigt sein könnte und sie vielleicht unbenutzbar ist, aufgrund der begrenzten [OpenGL](https://en.wikipedia.org/wiki/OpenGL)-Unterstützung vieler virtueller Maschinen.



## Installation unter Windows 

1.  Ein Installationspaket (.exe) von der Download-Seite herunterladen. Die FreeCAD-Installationsprogramme sollten auf jeder Windows-Version ab Windows 7 funktionieren.
2.  Die Bedingungen der LGPL-Lizenz akzeptieren; dies ist einer der wenigen Fälle, wo man wirklich gefahrlos die Schaltfläche \"Akzeptieren\" drücken kann ohne den Text zu lesen. Kein Kleingedrucktes: ![](images/LicenseAgreement_0212.jpeg )
3.  Den Standardpfad hier unverändert lassen oder, wenn gewünscht, ändern: ![](images/Path0212.jpeg )
4.  Sicherstellen, dass alle zu installierenden Komponenten markiert sind: ![](images/Components0212.jpeg )
5.  Das war\'s. Die Installation ist jetzt komplett und das Erkunden von FreeCADs Fähigkeiten kann beginnen.

**Installation einer Entwicklungsversion**

Das Zusammenstellen von FreeCAD und das Entwickeln eines Installationsprogramms bedingt eine beträchtliche Investition an Zeit und Mühe. Als Ergebnis werden Entwicklungsversionen (auch als Vorabversionen bezeichnet) normalerweise als .zip- oder .7z-Archive die auf der [FreeCAD-Download-Seite](https://www.freecad.org/downloads.php) bereitgestellt. Ein formaler Installationsprozess für diese Dateien ist nicht nötig. Einfach den Inhalt entpacken und FreeCAD mit einem Doppelklick auf die darin enthaltene FreeCAD.exe-Datei starten. Diese Herangehensweise ermöglicht dem Anwender auch, die stabile und die \"instabile\" Version auf dem gleichen Computer zu betreuen. Dies ist, als hätte man einen zuverlässigen Alttags-Pkw neben einem Raketenrucksack in der Garage!



### Installation unter Linux 

Für Anwender moderner Linux-Distributionen wie Ubuntu, Fedora, openSUSE, Debian, Mint und Elementary ist das Installieren so einfach, wie ein einzelner Klick. Es kann direkt mit der Software-Verwaltung der Distribution installiert werden, auch wenn das Aussehen von den Abbildungen abweicht, da jede Distribution ihr eigenes Werkzeug verwendet.

1.  Den Softwaremanager öffnen und nach \"freecad\" suchen:
2.  Die Schaltfläche \"Installieren\" anklicken, das war\'s, FreeCAD wird installiert. Nicht vergessen, es danach zu bewerten!
    <img alt="" src=images/linuxInstallation.png  style="width:800px;">

**Alternative Wege**

Eine der großen Freuden bei der Verwendung von Linux ist die Vielzahl an Möglichkeiten zur Anpassung der Software, kein Grund zur Zurückhaltung. Für Anwender von Ubuntu und seiner Derivate kann FreeCAD auch von einem [PPA](https://launchpad.net/~freecad-maintainers) installiert werden, das von der FreeCAD-Gemeinschaft betreut wird und das sowohl stabile als auch Entwicklungsversionen beinhaltet. Unter Fedora kann auf die aktuellen FreeCAD-Entwicklungsversionen über [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) zugegriffen werden. Da FreeCAD quelloffen ist, hat der Anwender auch die Freiheit FreeCAD selber zu [kompilieren](Compiling/de.md).



### Installation unter Mac OS 

Die Installation von FreeCAD unter Mac OSX ist heutzutage genauso einfach wie auf anderen Plattformen. Da es jedoch weniger Leute in der Gemeinschaft gibt, die einen Mac besitzen, hinken die verfügbaren Pakete manchmal ein paar Versionen hinter den anderen Plattformen her.

1.  Ein deiner Version entsprechendes gezipptes Paket von der [Download-Seite](https://github.com/FreeCAD/FreeCAD/releases) herunterladen.
2.  Den Ordner Downloads öffnen und die heruntergeladene zip-Datei entpacken: ![](images/Freecad-mac-01.jpg )
3.  Die FreeCAD-Anwendung aus der zip-Datei in den Ordner Anwendungen ziehen: ![](images/Freecad-mac-02.jpg )
4.  Das war\'s, FreeCAD ist installiert! ![](images/Freecad-mac-03.jpg )

5\. Wenn das System den Start von FreeCAD aufgrund eingeschränkter Berechtigungen für Anwendungen, die nicht aus dem App-Store kommen, verhindert, muss dies in den Systemeinstellungen aktiviert werden: ![](images/Freecad-mac-04.jpg )



### Deinstallation

Idealerweise will man sich nicht von FreeCAD trennen nicht deinstallieren, aber sollte es einmal nötig sein, es zu deinstallieren, keine Sorge, der Prozess ist einfach. Unter Windows wird die bekannte Option \"Software entfernen\" der Systemsteuerung. Linux-Anwender verwenden dieselbe Software-Verwaltung, mit der das Programm installiert wurde. Mac-Anwender haben es am einfachsten - einfach FreeCAD aus dem Programme-Ordner in den Papierkorb ziehen



### Setzen der Grundeinstellungen 

Nach dem Installieren von FreeCAD, möchte man es wahrscheinlich personalisieren, indem man einige Einstellungen angepasst. Die Einstellungen in FreeCAD findet man unter dem Menüeintrag **Bearbeiten → Einstellungen**. Folgend sind einige Grundeinstellungen aufgelistet, die man eventuell gleich ändern möchte, aber man kann auch auf Entdeckungsreise durch die verschiedenen Einstellungsseiten gehen, um das Programm noch weiter auf die eigenen Bedürfnisse zuzuschneiden.



#### Kategorie Allgemein, Registerkarte Allgemein 

![](images/FreeCAD_022_GeneralGen.png )

1.  **Sprache**: Standardmäßig wählt FreeCAD die Sprache deines Betriebssystems aus, du hast jedoch die Möglichkeit, diese zu ändern. Dank des Engagements vieler Mitwirkender ist FreeCAD in einer Vielzahl von Sprachen verfügbar.
2.  **Einheiten**: Mit dieser Einstellung kannst du das Standardeinheitensystem für deine Projekte auswählen.



#### Kategorie „Allgemein", Registerkarte „Dokument" 

![](images/FreeCAD_022_GeneralDoc.png )

1.  **Beim Start ein neues Dokument erstellen**: FreeCAD öffnet bei jedem Programmstart automatisch ein neues Dokument.
2.  **Speicheroptionen**: Konfiguriere hier Einstellungen, die dir helfen, deine Arbeit im Falle eines Absturzes wiederherzustellen.
3.  **Erstellung und Lizenz**: In diesem Bereich kannst du die Einstellungen für neue Dateien festlegen. Um das Teilen zu erleichtern, solltest du mit einer freizügigeren Copyleft-Lizenz wie Creative Commons beginnen.



#### Kategorie Anzeige, Registerkarte Navigation 

![](images/FreeCAD_022_DisplayNav.png )

1.  **Zoom am Cursor**: Wenn aktiviert, werden Zoomaktionen auf den Mauszeiger zentriert. Wenn deaktiviert, wird der Zoom auf die Mitte der Ansicht fokussiert.
2.  **Zoom umkehren**: Diese Option kehrt die Zoomrichtung in Bezug auf die Mausbewegung um.



#### Registerkarte Arbeitsbereiche 

![](images/FreeCAD_022_WBMenu.png )

Obwohl FreeCAD normalerweise die Startseite öffnet, kannst du diese mit dieser Einstellung umgehen. Du kannst direkt in deinem bevorzugten Workbench beginnen. Darüber hinaus kannst du anpassen, welche Workbenches im Auswahlmenü angezeigt werden.



#### Registerkarte Import / Export 

![](images/FreeCAD_022_ImportExport.png )

Definiere hier grundlegende Parameter für den Import und Export in verschiedene Formate.



### Installieren zusätzlicher Inhalte 

So wie die FreeCAD-Gemeinschaft wächst und sich das Anpassen vereinfacht, tauchen auch mehr externe Beiträge und Nebenprojekte von Gemeinschaftsmitgliedern und anderen Begeisterten überall im Internet auf. Viele dieser Projekte liegen in Form von Arbeitsbereichen oder Makros vor und können einfach über den [Addon-Manager](Std_AddonMgr/de.md) dem eigenen Werkzeugkasten hinzugefügt werden. Der Addon-Manager ist über das Menü **Werkzeuge** zu erreichen, eröffnet eine Welt von Möglichkeiten und ermöglicht verschiedene interessante Komponenten zu installieren:

![](images/FreeCAD_022_AddonsMenu.png )

1.  Eine Bauteilbibliothek [Parts library](https://github.com/FreeCAD/FreeCAD-library). Diese Bibliothek ist eine Schatzkiste nützlicher Modelle oder Modellteile, die von FreeCAD-Anwendern erstellt wurden. Alle Elemente dieser Bibliothek stehen zur freien Verfügung für die Verwendung in eigenen Modellen und können direkt innerhalb der FreeCAD-Installation aufgerufen werden.
2.  [Zusätzliche Arbeitsbereiche](https://github.com/FreeCAD/FreeCAD-addons). Dies sind spezialisierte Ergänzungen die die Funktionalität von FreeCAD für bestimmte Aufgaben erweitern. Beispielanwendungen schließen die Animation von Modellteilen oder die Verwaltung bestimmter Konstruktionsprozesse, wie z.B. das Abkanten von Blechen oder BIM (Building Information Modeling = Bauwerksdatenmodellierung). Detaillierte Informationen über jeden Arbeitsbereich einschließlich eines Überblicks über die darin enthaltenen Werkzeuge stehen auf der jeweiligen Addon-Seite zur Verfügung, auf die über eine Verknüpfung im Addon-Manager zugegriffen werden kann.
3.  Eine große Anzahl von [Makros](https://github.com/FreeCAD/FreeCAD-macros), die auch zum herunterladen zur Verfügung stehen. Diese können einen Arbeitsablauf signifikant rationalisieren; die zugehörige detaillierte Dokumentation ihrer Verwendung findet man im [FreeCAD-Wiki](Macros_recipes/de.md)

Seit der FreeCAD-Version 0.17.9940 ist die empfohlene Methode zur installation aller oben beschriebener Werkzeuge die Verwendung des eingebauten Addon-Managers. Wenn diese Methode jedoch aus irgendwelchen Gründen nicht zur Verfügung steht, ist auch stets eine manuelle Installation möglich. Weitere Informationen finden sich auf der Seite [FreeCAD-Addons](https://github.com/FreeCAD/FreeCAD-addons).

**Weiterlesen**

-   [Weitere Optionen zum Herunterladen](Download/de.md)
-   [FreeCAD-PPA für Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [FreeCAD-Erweiterungs-PPA für Ubuntu](https://launchpad.net/freecad-extras)
-   [FreeCAD selbst kompilieren](Compiling/de.md)
-   [FreeCAD Übersetzungen](https://crowdin.com/project/freecad)
-   [FreeCADs github-Seite](https://github.com/FreeCAD)
-   [Der FreeCAD-Addon-Manager](Std_AddonMgr/de.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/de
