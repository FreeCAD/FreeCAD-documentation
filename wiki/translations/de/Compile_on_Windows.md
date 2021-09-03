





{{TOCright}}

Diese Seite erklärt Schritt für Schritt, **wie man FreeCAD 0.19 oder neuer unter Windows kompiliert**. Für andere Plattformen siehe [Compiling](Compiling.md).

## Voraussetzungen

Kompilieren von FreeCAD unter Windows erfordert einige Werkzeuge und Bibliotheken.

### Erforderlich

-   Einen Compiler. FreeCAD wurde mit Visual Studio (MSVC) getestet - andere Compiler können funktionieren, aber eine Anleitung zur Verwendung ist hier nicht enthalten. Mehr Details in [\#Compiler](#Compiler.md), unten.

-   [Git](http://git-scm.com/) (Es gibt auch für Git verfügbare GUI Frontends, siehe den nächsten Abschnitt.)

-   [CMake](https://cmake.org/download/) Version 3.11.x oder neuer. *Tipp:* Wenn du bei der Installation von CMake die Option *CMake zum System PFAD für alle Benutzer hinzufügen* wählst, ist CMake von der Windows Eingabeaufforderung aus zugänglich, was nützlich sein kann.

-   LibPack (auch FreeCADLibs genannt). Dies ist ein einzelnes Paket, das alle Bibliotheken enthält, die notwendig sind, um FreeCAD unter Windows zu kompilieren.

Lade die Version von LibPack herunter, die zur FreeCAD-Version passt, die du kompilieren möchtest. Um FreeCAD 0.19 oder die letzte Entwicklerversion 0.20 zu kompilieren, lade [LibPack for 0.19/0.20](https://github.com/apeltauer/FreeCAD/releases/tag/LibPack_12.5.2) herunter (nur 64-bit). Entpacke LibPack an einem geeigneten Ord. (Wenn dein Computer die Erweiterung .7z nicht erkennt, solltest du das Programm [7-zip](https://www.7-zip.org) installieren.)  **Hinweis**: Es wird dringend empfohlen, FreeCAD mit der Compiler-Version zu kompilieren, für die das LibPack vorgesehen ist. Du könntest bspw. Probleme bekommen, FreeCAD 0.19 mit MSVC 15 zu kompilieren, weil das LibPack für 0.19 für den Compile mit MSVC 17 vorgesehen ist.

### Optionale Programme 

-   Ein GUI Frontend für Git. Es stehen mehrere Frontends zur Verfügung, siehe [diese Liste](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs). Der Hauptvorteil eines Frontends besteht darin, dass Sie die Git-Befehle nicht erlernen müssen, um den Quellcode von FreeCAD zu erhalten oder Patches an das GitHub-Repository von FreeCAD zu senden.

Im Folgenden beschreiben wir die Handhabung des Quellcodes über das [TortoiseGit](https://tortoisegit.org/) Frontend. Dieses Frontend integriert sich direkt in den Windows Dateiexplorer und verfügt über eine große Benutzer Gemeinschaft, um Hilfe bei Problemen zu erhalten.

-   [NSIS](http://sourceforge.net/projects/nsis/) wird verwendet, um das FreeCAD Windows Installationsprogramm zu generieren.

### Quellcode

Jetzt kannst Du den Quellcode von FreeCAD bekommen:

#### Verwendung eines Frontend 

Bei Verwendung des [Git Frontends](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Erstelle einen neuen Ordner, in den der Quellcode heruntergeladen werden soll.
2.  Klicke mit der rechten Maustaste auf diesen Ordner im Windows Dateiexplorer und wähle **Git Clone** im Kontextmenü.
3.  Es erscheint ein Dialogfeld. Gib darin die Internetadresse für das FreeCAD Git Repositorium ein

*<https://github.com/FreeCAD/FreeCAD.git>*

und klicke auf **OK**.

Der neueste Quellcode wird aus dem FreeCAD Git Repositorium heruntergeladen und der Ordner wird von Git verfolgt.

#### Verwendung der Kommandozeile 

Um einen lokalen Trackingzweig zu erstellen und den Quellcode herunterzuladen, öffne ein Terminal (Eingabeaufforderung) und wechsle dort in das Verzeichnis, in dem die Quelle gespeichert werden soll, und gib dann ein:


```python
git clone https://github.com/FreeCAD/FreeCAD.git
```

### Kompilierer

Der Standard Compiler (empfohlen) ist MS Visual Studio (MSVC). Die Verwendung anderer Compiler, z. B. gcc über Cygwin oder MinGW, ist zwar möglich, wird hier aber nicht getestet oder behandelt.

Du kannst eine kostenlose Version von MSVC (für den persönlichen Gebrauch) erhalten, indem Du die [*Gemeinschafts* Edition von MS Visual Studio](https://visualstudio.microsoft.com/vs/community/) herunterlädst.

Für diejenigen, die die Installation des riesigen MSVC für den reinen Zweck, einen Compiler zu haben, vermeiden wollen, siehe [CompileOnWindows - Reducing Disk Footprint](CompileOnWindows_-_Reducing_Disk_Footprint.md).

**Hinweis:** Obwohl die *Gemeinschafts*ausgabe von MSVC kostenlos ist, musst du ein Microsoft Konto erstellen, um die IDE länger als eine 30-tägige Testphase zu verwenden. Wenn du nur über die Kommandozeile kompilieren willst, brauchst du die IDE nicht und somit auch kein Microsoft Konto.

Als freie und OpenSource alternative IDE kannst du [KDevelop](https://www.kdevelop.org/download) verwenden. Du kannst KDevelop zum Ändern und Schreiben von C++ Code verwenden, musst aber die Kommandozeile zum Kompilieren verwenden.

### Optionale Systempfad Konfiguration 

Optional können die Pfade zu einigen Ordnern in die Systemvariable PATH aufgenommen werden. Dies ist hilfreich, wenn du über die Befehlszeile/Powershell auf Programme in diesen Ordnern zugreifen möchtest oder wenn du möchtest, dass spezielle Programme vom Compiler oder CMake gefunden werden. Außerdem kann es notwendig sein, Ordner zum PATH hinzuzufügen, wenn du bei der Installation des Programms nicht die entsprechenden Optionen verwendet hast.

-   Du kannst den Ordner deines LibPacks in deine System PATH Variable aufnehmen. Dies ist nützlich, wenn du vorhast, mehrere Konfigurationen/Versionen von FreeCAD zu erstellen.
-   Wenn du die Option zum Hinzufügen von CMake zum PFAD während der Installation nicht verwendet hast, füge seinen Installationsordner hinzu.

\"C:\\\\Program Files\\CMake\\CMake\\\" zum PATH.

-   Wenn du die Option, TortoiseGit während der Installation zum PFAD hinzuzufügen, nicht genutzt hast, füge seinen Installationsordner hinzu.

*C:\\Program Files\\TortoiseGit\\bin* zum PATH.

Um der PATH Variablen Ordnerpfade hinzuzufügen:

1.  Klicke im Windows-Startmenü mit der rechten Maustaste auf *Computer* und wähle *Eigenschaften*.
2.  Klicke im erscheinenden Dialog auf *Erweiterte Systemeinstellungen*.
3.  Es öffnet sich ein weiterer Dialog. Klicke dort in der Registerkarte *Erweitert* auf **Umgebungsvariablen**.
4.  Wieder öffnet sich ein weiterer Dialog. Wähle dann die Variable *Pfad* und klicke auf **Bearbeiten**.
5.  Und wieder öffnet sich ein weiterer Dialog. Klicke dort auf **New**\' und füge zum PATH zum Ordner von Git oder dem LibPack hinzu.
6.  Abschließend drücke **OK** und schließe alle Dialoge, indem Du ebenfalls **OK**\' drückst.

## Konfiguration

Sobald du alle notwendigen Werkzeuge, Bibliotheken und den FreeCAD-Quellcode hast, bist du bereit für die Konfiguration und den Kompilierungsprozess. Dieser Prozess durchläuft fünf Schritte:

1.  Führe CMake einmal aus, um dein System zu untersuchen und den Konfigurationsprozess zu beginnen (dieser wird melden, dass er fehlgeschlagen ist).
2.  Passe die notwendigen CMake-Einstellungen an, um die Position des LibPack zu setzen und Qt5 zu aktivieren.
3.  Starte CMake erneut, um die Konfiguration zu finalisieren (dieses Mal sollte es ohne Fehler durchlaufen).
4.  Benutze CMake, um das Visual Studio Build System zu generieren.
5.  Benutze Visual Studio, um FreeCAD zu kompilieren.

### CMake

Konfiguriere zunächst die Bauumgebung mit CMake:

1.  Öffne das CMake GUI.
2.  Gib den Quellordner von FreeCAD an.
3.  Gib einen Bauordner an (verwende nicht den Quellordner \-- CMake erstellt diesen Ordner, wenn er nicht existiert).
4.  Klicke auf *Konfigurieren*\'.
5.  In dem erscheinenden Dialog gib den gewünschten Generator an: In den meisten Fällen wirst du die Voreinstellungen in diesem Dialogfeld verwenden. Für das standardmäßige MS Visual Studio verwende *Visual Studio xx 2yyy*, wobei xx die Compiler Version und 2yyy das Jahr der Veröffentlichung ist. Es wird empfohlen, die Standardoption *Use default native compilers* zu verwenden.

**Hinweis:** Es ist wichtig, die richtige Bitvariante anzugeben. Wenn du die 64-bit Variante von LibPack hast, musst du auch den x64 Compiler verwenden.

Dies wird die Konfiguration beginnen und *wird fehlschlagen* wegen fehlender Einstellungen. Dies ist normal, du hast den Speicherort des LibPack noch nicht angegeben. Es können jedoch auch andere Fehler auftreten, die weitere Maßnahmen deinerseits erfordern.

Wenn es mit der Meldung fehlschlägt, dass Visual Studio nicht gefunden werden konnte, ist die CMake Unterstützung in MSVC noch nicht installiert. Um das zu tun:

1.  Öffne die MSVC IDE.
2.  Verwende das Menü Werkzeuge → Werkzeuge und Funktionen erhalten
3.  Aktiviere im Reiter *Arbeitsauslastungen* die *Desktop Entwicklung mit C++*.
4.  Auf der rechten Seite solltest Du nun sehen, dass die Komponente *Visual C++ Werkzeuge für CMake* installiert wird.
5.  Installiere es.

Wenn es mit einer Meldung über eine falsche Python-Version oder fehlendes Python fehlschlägt, dann:

1.  Verwende das Feld \"Suchen:\" in CMake, um nach der Zeichenkette \"Python\" zu suchen.
2.  Wenn du dort einen Pfad wie *C:/Programme/Python38/python.exe* siehst, hat CMake das Python erkannt, das bereits auf deinem PC installiert ist, aber diese Version ist nicht kompatibel mit dem LibPack. Da das LibPack eine kompatible Version von Python enthält, ändere die folgenden Python Einstellungen in CMake auf dessen Pfade (unter der Annahme, dass das LibPack im Ordner *D:\\FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17* liegt):

![](images/CMake_Python_settings.png )

Wenn es keinen Fehler zu Visual Studio oder Python gibt, ist alles in Ordnung, aber CMake kennt noch nicht alle notwendigen Einstellungen. Deshalb jetzt:

1.  Suche in CMake nach der Variable **FREECAD\_LIBPACK\_DIR** und gib den Ort des LibPack Ordners an, den du zuvor heruntergeladen hast.
2.  Nur beim Kompilieren von FreeCAD 0.19 suche nach der Variable **BUILD\_QT5** und aktiviere diese Option.
3.  Klicke erneut auf **Configure**.

Es sollten nun keine Fehler mehr auftreten. Wenn du weiterhin auf Fehler stößt, die du nicht diagnostizieren kannst, besuche das [Install/Compile forum](https://forum.freecadweb.org/viewforum.php?f=4) auf der FreeCAD Forum Webseite. Wenn CMake korrekt vorgegangen ist, klicke auf **Generieren**. Nachdem dies geschehen ist, kannst du CMake schließen und die Kompilierung von FreeCAD mit Visual Studio starten. Lasse es jedoch für die erste Kompilierung geöffnet, falls du einige Optionen für den Bauprozess ändern willst oder musst.

**Hinweis:** Beim Kompilieren von FreeCAD 0.19 wird die CMake-Variable **BUILD\_ENABLE\_CXX\_STD** auf **C++14** gesetzt, während sie für FreeCAD 0.20 auf **C++17** gesetzt wird. Das ist nötig, weil FreeCAD 0.20 mindestens den C++-Sprachstandard Version 17 benötigt. Falls du also das letzte Mal FreeCAD 0.19 kompiliert hast, musst du CMake für FreeCAD 0.20 erneut starten, um den C++-Sprachstandard zu ändern.

### Optionen für den Bauprozess 

Das CMake Bau System gibt dir die Kontrolle über einige Aspekte des Bauprozesses. Insbesondere kannst du einige Funktionen oder Module mit CMake Variablen ein- und ausschalten.

Hier ist eine Beschreibung einiger dieser Variablen:

  Variablenname                            Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Vorgabewert
  ---------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------
  BUILD\_XXX                               Erstelle FreeCAD mit der Komponente XXX. Falls du bspw. den Arbeitsbereich *OpenSCAD* nicht willst/brauchst, deaktiviere die Variable *BUILD\_OPENSCAD*. FreeCAD wird diesen Arbeitsbereich dann nicht enthalten. **Hinweis:** Einige Komponenten werden für andere Komponenten benötigt. Wenn du bspw. *BUILD\_ROBOT* deaktivierst, wird CMake dich darüber informieren, dass die Komponente *Path* nicht korrekt kompiliert werden kann. Prüfe daher die CMake-Ausgaben nach dem Ändern einer BUILD\_XXX-Option!                                                                                                                                      hängt davon ab
  BUILD\_ENABLE\_CXX\_STD                  Die Version des C++-Sprachstandards. **C++14** ist der höchstmögliche für FreeCAD 0.19, während wenigstens **C++17** für FreeCAD 0.20 erforderlich ist. Siehe auch den Hinweis im Abschnitt [\#Bau\_mit\_Visual\_Studio\_15\_(2017)\_und\_16\_(2019)](#Bau_mit_Visual_Studio_15_(2017)_und_16_(2019).md)                                                                                                                                                                                                                                                                                                                                        hängt davon ab
  CMAKE\_INSTALL\_PREFIX                   Das Ausgabeverzeichnis bei der Erstellung des Ziels *INSTALL*, siehe auch Abschnitt [\#Ausführen\_und\_Installieren\_von\_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Windows Standard-Programminstallationsverzeichnis
  FREECAD\_COPY\_DEPEND\_DIRS\_TO\_BUILD   Kopiert abhängige Bibliotheken in den Build-Ordner, die zur Ausführung von FreeCAD.exe benötigt werden. Siehe auch Abschnitt [\#Ausführen\_und\_Installieren\_von\_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md). **Hinweis:** Die Optionen FREECAD\_COPY\_XXX erscheinen nur, falls die Bibliotheken nicht bereits kopiert wurden. Falls du also zu einer LibPack-Version wechselst, ist es wichtig, alle Verzeichnisse in deinem Build-Ordner zu löschen AUSSER dem LibPack-Verzeichnis. Lösche in CMake den Cache und starte, als ob du das erste Mal kompilierst und du wirst die FREECAD\_COPY\_XXX-Optionen sehen.   OFF
  FREECAD\_COPY\_LIBPACK\_BIN\_TO\_BUILD   Kopiert LibPack-Binaries in den Build-Ordner, die zur Ausführung von FreeCAD.exe benötigt werden. Siehe auch Abschnitt [\#Ausführen\_und\_Installieren\_von\_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                               OFF
  FREECAD\_COPY\_PLUGINS\_BIN\_TO\_BUILD   Kopiert Qt-Plugin-Dateien in den Build-Ordner, die zur Ausführung von FreeCAD.exe benötigt werden. Siehe auch Abschnitt [\#Ausführen\_und\_Installieren\_von\_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                              OFF
  FREECAD\_LIBPACK\_USE                    Schaltet die Verwendung von FreeCAD LibPack ein/aus (ON/OFF)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ON
  FREECAD\_LIBPACK\_DIR                    Verzeichnis, in dem sich LibPack befindet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               FreeCAD\'s Quell-Code-Verzeichnis
  FREECAD\_RELEASE\_PDB                    Erstelle Debug-Bibliotheken auch für Freigabe-Versionen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ON

## FreeCAD bauen 

Abhängig von deinem Compiler wird der Prozess zur Erstellung von FreeCAD etwas anders ablaufen. In den folgenden Abschnitten werden die bekannten Arbeitsabläufe beschrieben. Wenn Du mit Qt Creator baust, gehe zu [Bau mit Qt Erzeuger](#Building_with_Qt_Creator/de.md), ansonsten fahre direkt fort:


<div class="mw-collapsible mw-collapsed toccolours">

### Bau mit Visual Studio 15 (2017) und 16 (2019) 


<div class="mw-collapsible-content">

#### Bau freigeben 

1.  Starte das Visual Studio IDE. Dies kann entweder durch Drücken der Schaltfläche *Projekt öffnen* in der CMake GUI oder durch Doppelklicken auf die Datei *FreeCAD.sln*, die Du in Deinem Bauordner findest, geschehen.
2.  In der Werkzeugleiste der MSVC IDE versichere dich, dass du für die erste Kompilierung *Release* verwendest.
3.  Es gibt ein Fenster namens *Solution Explorer*. Es listet alle möglichen Kompilierungsziele auf.

Um eine vollständige Kompilierung zu starten, klicke mit der rechten Maustaste auf das Ziel **ALL\_BUILD** und wählen dann **Build**. Dies wird nun recht lange dauern.

Um ein einsatzbereites FreeCAD zu kompilieren, kompiliere das Ziel *INSTALL*, siehe Abschnitt [Ausführen und Installieren von FreeCAD](#Running_and_installing_FreeCAD/de.md).

Wenn Du keine Fehler bekommst, ist das erledigt. **Herzlichen Glückwunsch!** Du kannst MSVC beenden oder offen lassen.

**Hinweis:** FreeCAD 0.20 erfordert mindestens den C++Sprachstandard Version 17, aber die Drittanbieterkomponente ist noch nicht bereit dafür. Deshalb wirst du Kompilierungsfehler für das Ziel *ReverseEngineering* bekommen. Um dies zu beheben, rechtsklicke im MSVC-Solution-Explorer auf dieses Target und wähle im Kontextmenü den letzten Eintrag *Properties* (Eigenschaften). Im erscheinenden Dialog ändere **C++ Language Standard** auf **ISO C++14**. Erstelle das Target **ALL\_BUILD** erneut.

#### Fehlersuch Bau 

Für einen Fehlersuch Bau ist es notwendig, dass das Python verwendet wird, das im LibPack enthalten ist. Um dies zu gewährleisten:

1.  Suche in der CMake GUI nach \"Python\".
2.  Wenn du dort einen Pfad wie *C:/Programme/Python38/python.exe* siehst, hat CMake das auf deinem PC installierte Python erkannt und nicht das des LibPack. In diesem Fall passe die verschiedenen Python Einstellungen in CMake wie folgt an (unter der Annahme, dass das LibPack im Ordner *D:\\FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17* liegt):

![](images/CMake_Python_settings.png )

Jetzt

1.  Starte die Visual Studio IDE. Dies kann entweder durch Drücken der Schaltfläche *Öffne Projekt* in der CMake GUI geschehen oder durch Doppelklick auf die Datei *FreeCAD.sln*, die du in deinem Bau Ordner findest.
2.  In der Werkzeugleiste der MSVC IDE versichere dich, dass du für die erste Kompilierung *Debug* verwendest.
3.  Es gibt ein Fenster namens *Solution Explorer*. Es listet alle möglichen Kompilierziele auf. Um eine vollständige Kompilierung zu starten, klicke mit der rechten Maustaste auf das Ziel **ALL\_BUILD** und wähle dann **Build** im Kontextmenü.

Dies wird nun recht lange dauern. Wenn keine Kompilierungsfehler aufgetreten sind, kannst du den Debug Build starten:

1.  Klicke mit der rechten Maustaste auf das Ziel **FreeCADMain** und wähle dann im Kontextmenü **Set as Startup Project**.
2.  Klicke anschließend in der Werkzeugleiste auf die Schaltfläche mit dem grünen Dreieck **Local Windows Debugger**.

Dies startet die Erstellung der Debug-Version von FreeCAD und du kannst die MSVC-IDE verwenden, um eine Fehlersuche durchzuführen.

#### Video Ressource 

Ein englischsprachiges Tutorium das mit der Konfiguration in CMake Gui beginnt und mit dem \Build\ Befehl in Visual Studio 16 2019 fortgesetzt wird, ist ungelistet auf YouTube unter [Tutorium: FreeCAD aus dem Quellcode unter Windows 10 bauen](https://youtu.be/s4pHvlDOSZQ).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Bau mit Qt Creator (veraltet) 


<div class="mw-collapsible-content">

#### Installation und Konfiguration des Qt Creators 

-   Herunterladen und installieren [Qt Creator](https://www.qt.io/offline-installers)
-   Werkzeuge → Optionen → Texteditor → Registerkarte Verhalten:
    -   Dateikodierungen → Standard-Kodierungen:
    -   Gesetzt auf: **ISO-8859-1 /\...csISOLatin1**\' (Bestimmte Zeichen erzeugen Fehler/Warnungen mit Qt Creator, wenn sie auf UTF-8 gesetzt sind. Das scheint es zu beheben.)
-   Werkzeuge → Optionen → Bau & Lauf:
    -   CMake Registerkarte
        -   Fülle das Feld Ausführung mit dem Pfad zu cmake.exe aus.
    -   Registerkarte Kits
        -   Name: MSVC 2008
        -   Compiler: Microsoft Visual C++ Compiler 9.0 (x86)
        -   Debugger: Automatische Erkennung\.....
        -   Qt-Version: Keine
    -   Registerkarte Allgemein
        -   Deaktiviere das Kontrollkästchen: Erstelle immer ein Projekt, bevor Du es einsetzt.
        -   Deaktiviere das Kontrollkästchen: Stelle das Projekt immer vor der Ausführung bereit.

#### Projektimport und Bau 

-   Datei → Datei oder Projekt öffnen
-   Öffne **CMakeLists.txt**\', das sich in der obersten Ebene der Quelle befindet.
-   Dadurch wird CMake gestartet.
-   Wähle das Build Verzeichnis und klicke auf Weiter.
-   Setze den Generator auf **NMake Generator (MSVC 2008)**\'.
-   Klicke auf CMake ausführen. Folge den oben dargestellten Anweisungen, um CMake nach Deinen Wünschen zu konfigurieren.

Jetzt kann FreeCAD erstellt werden.

-   Bau → Baue alle
-   Das wird lange dauern\.....

Nach Fertigstellung kann es ausgeführt werden: Unten links befinden sich 2 grüne Dreiecke. Eine davon ist Fehlersuche. Der andere wird ausgeführt. Wähle, was immer du willst.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Kommandozeilen Bau 


<div class="mw-collapsible-content">

Die Schritte, wie man von der Kommandozeile aus kompiliert, hängen vom Compiler ab. Für MSVC 2017 sind die Schritte:

1.  In Windows\' Startmenü gehen Sie zu {{MenuCommand/de|Visual Studio 2017 → Visual Studio Tools}} und wähle **Developer Command Prompt for VS 2017**.
2.  Wechsle in deinen Buildordner.
3.  Führe den Befehl aus


```pythonmsbuild ALL_BUILD.vcxproj /p:Configuration=Release```

oder


```pythonmsbuild INSTALL.vcxproj /p:Configuration=Release```

Diese Schritte können auch automatisiert werden. Hier ist zum Beispiel eine Lösung für MSVC 2017:

1.  Lade das Skript herunter [compile-FC.txt](https://forum.freecadweb.org/download/file.php?id=92135).
2.  Umbenennen in *compile-FC.bat*\'.
3.  Klicke im Datei Explorer von Windows mit der rechten Maustaste auf Dein Build Verzeichnis und benutze aus dem Kontextmenü *Befehlszeile hier*.
4.  Führe den Befehl aus


```pythoncompile-FC install```

Anstatt **compile-FC** mit der Option *install* aufzurufen, kannst Du auch *debug* oder *release* verwenden:

*debug*   - FreeCAD in Fehlersuchkonfiguration kompilieren

*release* - kompiliere FreeCAD in der Veröffentlichungskonfiguration.

*install*     - kompiliert FreeCAD in der Freigabekonfiguration und erstellt ein Installationssetup.


</div>


</div>

## Ausführen und Installieren von FreeCAD 

Es gibt 2 Methoden, um das kompilierte FreeCAD auszuführen:

Methode 1\'\': Du führst die FreeCAD.exe aus, die du in deinem Build Verzeichnis findest, im Unterverzeichnis *bin*\'.

*Methode 2*: Du baust das Ziel *INSTALL*

Methode 2 ist die einfachere, da sie automatisch sicherstellt, dass sich alle für die Ausführung der FreeCAD.exe erforderlichen Bibliotheken im richtigen Ordner befinden. Die FreeCAD.exe und die Bibliotheken werden in dem Ordner ausgegeben, den du in der CMake-Variablen *CMAKE\_INSTALL\_PREFIX* angegeben hast.

Für Methode 1 müssen die Bibliotheken in den Ordner *bin* deines Buildordners (wo sich die FreeCAD.exe befindet) gelegt werden. Dies ist einfach zu bewerkstelligen:

1.  Öffne die CMake GUI.
2.  Suche dort nach der Variablenoption *FREECAD\_COPY\_DEPEND\_DIRS\_TO\_BUILD* und überprüfe sie. Wenn es keine solche Option gibt, wurden die Bibliotheken bereits kopiert, siehe [Beschreibung der Optionen](#Options_for_the_build_process/de.md).
3.  Suche dort nach der Variablenoption *FREECAD\_LIBPACK\_BIN\_TO\_BUILD* und überprüfe diese.
4.  Suche dort nach der Variablenoption *FREECAD\_PLUGINS\_BIN\_TO\_BUILD* und überprüfe sie.
5.  Klicke auf **Konfigurieren**. Am Ende der Konfiguration kopiert CMake automatisch die notwendigen Bibliotheken aus dem LibPack Ordner.

## Aktualisierung des Build 

FreeCAD ist sehr aktiv entwickelt. Daher ändert sich der Quellcode fast täglich. Neue Funktionen wurden hinzugefügt und Fehler behoben. Um von diesen Quellcode-Änderungen zu profitieren, musst Du Dein FreeCAD neu erstellen. Dies geschieht in zwei Schritten:

1.  Aktualisierung des Quellcodes
2.  Rekompilierung

### Aktualisierung des Quellcodes 

#### Verwendung eines Frontends 

Bei Verwendung des [Git Frontend](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Klicke mit der rechten Maustaste auf deinen FreeCAD Quellcode Ordner im Windows Datei Explorer und wähle im Kontextmenü **Pull**\'.
2.  Es erscheint ein Dialogfeld. Wähle dort aus, welchen Entwicklungszweig Du bekommen möchtest. **master**\' ist der Hauptzweig. Verwendedies daher, es sei denn, du möchtest ein spezielles neues Feature aus einem Zweig kompilieren, der noch nicht mit *master* zusammengeführt wurde. (Für weitere Informationen über Git-Zweige siehe [Git development process](Source_code_management#Git_development_process.md).)

Klicke abschließend auf *OK*\'.

#### Verwendung der Kommandozeile 

Öffne ein Terminal (Eingabeaufforderung) und wechsle dort in dein Quellverzeichnis. Dann tippe:


```python
git pull https://github.com/FreeCAD/FreeCAD.git master
```

wobei *master* der Name des Hauptentwicklungszweiges ist. Wenn du Code von einem anderen Zweig erhalten möchtest, verwende dessen Namen anstelle von *master*.

### Rekompilierung

1.  Öffne die MSVC-IDE, indem Du entweder auf die Datei *FreeCAD.sln* oder auf die Datei *ALL\_BUILD.vcxproj* in Deinem Build-Verzeichnis doppelklickst.
2.  Fahre mit Schritt 2 aus Abschnitt [Building with Visual Studio 15 2017](#Building_with_Visual_Studio_15_2017.md) fort.

## Werkzeuge

Um an der FreeCAD Entwicklung teilzunehmen, solltest du die folgenden Werkzeuge kompilieren und installieren:

### Qt Designer Zusatzprogramm 

FreeCAD verwendet [Qt](https://en.wikipedia.org/wiki/Qt_(software)) als Werkzeugsatz für seine Benutzeroberfläche. Alle Dialoge sind in UI-Dateien eingerichtet, die mit dem Programm [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) bearbeitet werden können, das Teil jeder Qt Installation ist und auch im LibPack enthalten ist. FreeCAD hat seinen eigenen Satz von Qt Widgets, um spezielle Funktionen wie das Hinzufügen einer Einheit zu Eingabefeldern und das Setzen von Voreinstellungen zu ermöglichen.

#### Einrichtung

Um Qt Designer auf die FreeCAD Widgets aufmerksam zu machen, musst du

1.  Laden [diese ZIP Datei](https://forum.freecadweb.org/download/file.php?id=124239) herunter. (Kompiliert mit Qt 5.12, siehe [unten](#Compilation/de.md)).
2.  Entpacke die DLL Datei in der ZIP Datei und kopiere sie

-   Wenn du das LibPack verwendest: in den Ordner*\~\\FreeCADLibs\_12.5.2\_x64\_VC17\\bin\\designer* Da es nur einen *bin* Ordner geben wird und du zuerst den Unterordner *designer* erstellen musst.
-   Wenn du eine vollständige Qt-Installation hast: du kannst wählen zwischen dem Ordner*C:\\Qt\\Qt5.15.2\\msvc2019\_64\\plugins\\designer*oder*C:\\Qt\\Qt5.15.2\\msvc2019\_64\\bin\\designer*(du musst zuerst den Unterordner *designer* anlegen.)(passe die Pfade an deine Installation an!).

Starte den Qt Designer (erneut) und überprüfe sein Menü **Hilfe → Zusatzprogramme**. Wenn das Zusatzprogramm **FreeCAD\_widgets.dll** als geladen aufgeführt ist, kannst du nun FreeCADs .ui Dateien entwerfen und ändern. Falls nicht, musst du die DLL selbst [Kompilieren](#Compilation/de.md).

Wenn du lieber [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator) anstelle von Qt Designer verwenden möchtest, muss die DLL in diesem Ordner abgelegt werden:*C:\\Qt\\Qt5.15.2\\Tools\\QtCreator\\bin\\plugins\\designer*(Re)Start Qt Creator, wechsle in den Modus **Design** und überprüfe dann das Menü **Werkzeuge → Formular Editor → Über Qt Designer Zusatzprogramme**. Wenn das Zusatzprogramm **FreeCAD\_widgets.dll** als geladen aufgeführt ist, kannst du nun FreeCADs .ui Dateien entwerfen und ändern. Falls nicht, musst du die DLL selbst [Kompilieren](#Compilation/de.md).

#### Kompilierung

Die DLL kann nicht als Zusatzprogramm geladen werden, wenn sie mit einer anderen Qt Version kompiliert wurde als die, auf der dein Qt Designer/Qt Creator basiert. In diesem Fall musst du die DLL selbst kompilieren. Dies geschieht auf folgende Weise:

1.  Wechsle zum FreeCAD-Quell-Code-Verzeichnis*\~\\src\\Tools\\plugins\\widget*
2.  Öffne eine MSVC x64-Kommandozeile über das Windows-Start-Menü und wechsle darin zum o.g. Verzeichnis. Es ist wichtig, dass es die x64-Version der MSVC-Kommandozeile ist!
3.  Führe diesen Befehl aus *D:\\FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17\\bin\\qmake -t vclib plugin.pro*für eine volle Qt-Installation ist es*C:\\Qt\\5.15.2\\msvc2019\_64\\bin\\qmake -t vclib plugin.pro* (passe die Pfade entsprechend deiner Installation an!)
4.  Der Aufruf von *qmake* erstellte die Datei **FreeCAD\_widgets.vcxproj** im Verzeichnis *\~\\src\\Tools\\plugins\\widget*. Doppelklicke darauf und die MSVC-IDE wird sich öffnen.
5.  Stelle in der Werkzeugleiste der MSVC-IDE sicher, dass du das Kompilationsziel *Release* verwendest.
6.  Es gibt ein Fenster namens *Solution Explorer*. Rechtklicke dort auf **FreeCAD\_widgets** und wähle dann **Build**.
7.  Als Ergebnis solltest du nun eine Datei **FreeCAD\_widgets.dll** im Verzeichnis *\~\\src\\Tools\\plugins\\widget\\release* haben, die du als Plugin wie oben beschrieben installieren kannst.

====Miniaturansicht Anbieter===

FreeCAD hat die Funktion, Vorschau Miniaturbilder für \*.FCStd Dateien bereitzustellen. Das bedeutet, dass im Windows Datei Explorer \*.FCStd Dateien mit einem Bildschirmfoto des darin enthaltenen Modells angezeigt werden. Um diese Funktion anbieten zu können, muss FreeCAD die Datei **FCStdThumbnail.dll** unter Windows installiert haben.

#### Einrichtung 

Die DLL wird auf diese Weise installiert:

1.  Lade [diese ZIP Datei](https://forum.freecadweb.org/download/file.php?id=13404) herunter und entpacke sie.
2.  Öffne eine Windows Befehlseingabeaufforderung mit Administratorrechten (diese Rechte sind eine Voraussetzung).
3.  Wechsle in den Ordner, in dem sich die DLL befindet.
4.  Führe diesen Befehl aus 
```pythonregsvr32 FCStdThumbnail.dll```

Prüfe also, ob es funktioniert, stelle sicher, dass in FreeCAD die Voreinstellungsoption **[Speichern der Miniaturansicht in Projektdatei beim speichern des Dokuments](Preferences_Editor/de#Dokument.md)** aktiviert ist und speichere ein Modell. Zeige dann im Windows Explorer den Ordner des gespeicherten Modells in einer Symbolansicht an. Du solltest nun ein Bildschirmfoto des Modells in der Ordneransicht sehen.

#### Kompilierung 

Zum Kompilieren von FCStdThumbnail.dll

1.  Wechsle zum FreeCAD-Quell-Code-Verzeichnis*\~\\src\\Tools\\thumbs\\ThumbnailProvider*
2.  Öffne die CMake-GUI
3.  Gibt dort als Quellverzeichnis das an, in dem du dich gerade befindest.
4.  Verwende den gleichen Ordner als build-Verzeichnis.
5.  Klicke **Konfigurieren**
6.  Gib im erscheinenden Dialog den Generator an, den du verwenden möchtest. Für den Standard MS Visual Studio benutze *Visual Studio xx 2yyy* wobei xx die Compiler-Version und 2yyy das Jahr ihrer Freigabe ist. Es wird empfohlen, die Vorgabeoption *Use default native compilers* zu verwenden.**Hinweis:** Es ist wichtig, die richtige Bit-Variante anzugeben. Wenn du die 64-bit-Variante von LibPack hast, musst du auch den x64-Compiler verwenden.
7.  Klicke auf **Generieren**.
8.  Du sollte nun die Datei **ALL\_BUILD.vcxproj** im Verzeichnis *\~\\src\\Tools\\thumbs\\ThumbnailProvider* haben. Doppelklicke darauf und die MSVC-IDE wird sich öffnen.
9.  Stelle in der Werkzeugleiste der MSVC-IDE sicher, dass du das Kompilationsziel *Release* verwendest.
10. Es gibt ein Fenster namens *Solution Explorer*. Rechtklicke dort auf **ALL\_BUILD** und wähle dann **Build**.
11. Als Ergebnis solltest du nun eine Datei **FCStdThumbnail.dll** im Verzeichnis *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release* haben, die du wie oben beschrieben installieren kannst.

## OpenCASCADE Kompilieren 

Das Standard Libpack kommt mit einer Version von OpenCASCADE, die für den allgemeinen Gebrauch geeignet ist. Unter bestimmten Umständen kann es jedoch sinnvoll sein, gegen eine andere Version von OpenCASCADE zu kompilieren, wie z.B. eine der offiziellen Versionen oder einem gepatchten Abzweig. Beachte, dass es keine Garantie dafür gibt, dass FreeCAD mit allen Versionen von OpenCASCADE funktioniert, und dass die Verwendung einer Nicht-Libpack Version nur für fortgeschrittene Benutzer geeignet ist. Beachte auch, dass die Netgen Bibliothek für einige ihrer Funktionen OpenCASCADE verwendet und gegen dieselbe Version von OpenCASCADE kompiliert werden muss, die du beim Kompilieren von FreeCAD verwendest.

Der Prozess zur Erstellung einer benutzerdefinierten Version von OpenCASCADE ähnelt dem von FreeCAD und kann das FreeCAD Libpack nutzen, das du bereits heruntergeladen hast, um die benötigten Abhängigkeiten von Drittanbietern (Freetype und Tcl/Tk) bereitzustellen.

Zuerst beschaffe den OpenCASCADE Quellcode, entweder direkt von der Veröffentlichungsseite [OpenCASCADE.org](https://old.opencascade.com/content/latest-release), über [git](https://git.dev.opencascade.org/repos/occt.git), oder durch klonen der Abspaltung eines anderen, wie z.B. [the \"blobfish\" fork](https://gitlab.com/blobfish/occt), der von FreeCAD Forumsmitglied [tanderson69](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208) gepflegt wird.

Als nächstes benutze CMake zum konfigurieren des Build-Systems in einer ähnlichen Weise wie bei der Erstellung von FreeCAD. Bemerkenswerte CMake-Options für OpenCASCADE sind:

-   **3RDPARTY\_DIR** - Der Ablageort deiner Drittanbieter-Bibliotheken, typischerweise auf dein FreeCAD-Libpack-Verzeichnis eingestellt
-   **INSTALL\_DIR** - Wohin die fertigen Bibliotheken installiert werden sollen. Eine gute Praxis ist es, ein isoliertes (eigenes) Verzeichnis auf deinem System zu benutzen, anstatt \"global\" zu installieren oder die Libpack-Version zu überschreiben.

Schließlich öffne das Projekt in Visual Studio und erstelle die ALL\_BUILD- und dann die INSTALL-Targets.

Sobald du die entsprechenden DLLs für OpenCASCADE erstellt hast (es gibt viele von ihnen), musst du FreeCAD erneut erstellen. Öffne CMake und setze die Quell- und Build-Verzeichnisse für eine FreeCAD-Version wie oben angegeben. Es ist generell eine gute Idee, für diese alternative OpenCASCADE-Version ein neues Build-Verzeichnis zu verwenden, weil es dann einfach ist, auf deine alte FreeCAD-Version zu wechseln, falls etwas schief geht und ein Installationverzeichnis aufzubauen, so dass du sicher bist, dass die richtigen Bibliotheken zur Verfügung stehen. Zusätzlich zu den o.g. CMake-Variable setze die OpenCASCADE\_DIR-Variable auf den cmake-Ordner, der deine OpenCASCADE-Build-Informationen enthält.
Beispiel:

CMAKE_INSTALL_PREFIX    C:/Users/JaneDoe/Work/FreeCAD_occt751-install/
OpenCASCADE_DIR         C:/Users/JaneDoe/Work/opencascade-7.5.1-install/cmake/

Once you have used CMake to generate the build files for FreeCAD, open it in Visual Studio, build it, and then run build on the INSTALL target.

## Referenzen

Siehe auch

-   [Kompilieren unter Windows mit Visual Studio 2013](Compile_on_Windows_with_VS2013.md)
-   [Kompilieren - Beschleunigen](Compiling_(Speeding_up).md)







[Category:Developer\_Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Developer{{\#translation:}}](Category:Developer.md)
