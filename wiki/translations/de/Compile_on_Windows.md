# Compile on Windows/de
Diese Seite erklärt Schritt für Schritt, **wie man FreeCAD 0.19 oder neuer unter Windows kompiliert** unter Verwendung von Microsofts MSVC-Kompiler. Für Informationen über die Verwendung von MSYS2/MinGW, siehe [Auf MinGW kompilieren](Compile_on_MinGW/de.md). Für andere Plattformen siehe [Kompilieren](Compiling/de.md).



## Voraussetzungen

Kompilieren von FreeCAD unter Windows erfordert einige Werkzeuge und Bibliotheken.



### Erforderlich

-   Ein Compiler. FreeCAD wurde mit Visual Studio (MSVC) getestet - andere Compiler können funktionieren, aber eine Anleitung zur Verwendung ist hier nicht enthalten. Für weitere Details siehe Abschnitt [Compiler](#Compiler.md), unten.

-   [Git](http://git-scm.com/) (Es gibt auch für Git verfügbare GUI Frontends, siehe den nächsten Abschnitt.)

-   [CMake](https://cmake.org/download/) Version 3.11.x oder neuer. *Tipp:* Wenn du bei der Installation von CMake die Option *CMake zum System PFAD für alle Benutzer hinzufügen* wählst, ist CMake von der Windows Eingabeaufforderung aus zugänglich, was nützlich sein kann.

-   Das [LibPack](https://github.com/FreeCAD/FreeCAD-LibPack). Dies ist ein einzelnes Paket, das alle Bibliotheken enthält, die notwendig sind, um FreeCAD unter Windows zu kompilieren.

Lade die Version von LibPack herunter, die zur FreeCAD-Version passt, die du kompilieren möchtest. Um FreeCAD 0.20 zu kompilieren, lade [LibPack version 2.6](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/2.6) herunter, für FreeCAD 0.19 lade [LibPack version 1.0](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/1.0). Entpacke LibPack an einem geeigneten Ort. (Wenn dein Computer die Erweiterung .7z nicht erkennt, musst du das Programm [7-zip](https://www.7-zip.org) installieren.)  **Hinweis**: Es wird dringend empfohlen, FreeCAD mit der Compiler-Version zu kompilieren, für die das LibPack vorgesehen ist. Du könntest bspw. Probleme bekommen, FreeCAD 0.20 mit MSVC 2017 zu kompilieren, weil das LibPack für den Aufbau mit MSVC 2019 oder neuer vorgesehen ist.Um das LibPack später zu aktualisieren, siehe den Abschnitt [Updating the LibPack](#Updating_the_LibPack.md).



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
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git
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
3.  Gib einen Bauordner an. Dies kann **build** in dem Verzeichnis sein, der aus dem das repo geklont wurde, da dieser Pfad von git ignoriert wird. Verwende nicht den Quellordner. CMake erstellt diesen Ordner, wenn er nicht existiert.
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
2.  Wenn du dort einen Pfad wie *C:/Programme/Python38/python.exe* siehst, hat CMake das Python erkannt, das bereits auf deinem PC installiert ist, aber diese Version ist nicht kompatibel mit dem LibPack. Da das LibPack eine kompatible Version von Python enthält, ändere die folgenden Python Einstellungen in CMake auf dessen Pfade (unter der Annahme, dass das LibPack im Ordner *D:/FreeCAD-build/FreeCADLibs_2_8_x64_VC2019* liegt):

![](images/CMake_Python_settings.png )

Wenn es keinen Fehler zu Visual Studio oder Python gibt, ist alles in Ordnung, aber CMake kennt noch nicht alle notwendigen Einstellungen. Deshalb jetzt:

1.  Suche in CMake nach der Variable **FREECAD_LIBPACK_DIR** und gib den Ort des LibPack Ordners an, den du zuvor heruntergeladen hast.
2.  (*Nur beim Kompilieren von FreeCAD 0.19*) Suche nach der Variable **BUILD_QT5** und aktiviere diese Option.
3.  (*Soll direkt aus dem Build-Verzeichnis heraus ausgeführt werden wie beir Fehlersuche*) Suche nach den folgenden Optionen und aktiviere sie:
    -   **FREECAD_COPY_DEPEND_DIRS_TO_BUILD**
    -   **FREECAD_COPY_LIBPACK_BIN_TO_BUILD**
    -   **FREECAD_COPY_PLUGINS_BIN_TO_BUILD**
4.  Klicke erneut auf **Configure**.

Es sollten nun keine Fehler mehr auftreten. Wenn du weiterhin auf Fehler stößt, die du nicht diagnostizieren kannst, besuche das [Install/Compile forum](https://forum.freecadweb.org/viewforum.php?f=4) auf der FreeCAD Forum Webseite. Wenn CMake korrekt vorgegangen ist, klicke auf **Generieren**. Nachdem dies geschehen ist, kannst du CMake schließen und die Kompilierung von FreeCAD mit Visual Studio starten. Lasse es jedoch für die erste Kompilierung geöffnet, falls du einige Optionen für den Bauprozess ändern willst oder musst.



### Optionen für den Bauprozess 

Das CMake Bau System gibt dir die Kontrolle über einige Aspekte des Bauprozesses. Insbesondere kannst du einige Funktionen oder Module mit CMake Variablen ein- und ausschalten.

Hier ist eine Beschreibung einiger dieser Variablen:

  Variablenname                       Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Vorgabewert
    
  BUILD_XXX                           FreeCAD mit der Komponente XXX erstellt. Falls z.B. der Arbeitsbereich *OpenSCAD* nicht gebraucht wird, kann man die Variable *BUILD_OPENSCAD* deaktivieren. FreeCAD wird diesen Arbeitsbereich dann nicht enthalten. **Hinweis:** Einige Komponenten werden für andere Komponenten benötigt. Ist z.B. *BUILD_ROBOT* deaktiviert, wird CMake darüber informieren, dass die Komponente *Path* nicht korrekt kompiliert werden kann. Daher sollte die Ausgabe von CMake nach dem Ändern einer BUILD_XXX-Option geprüft werden!                                                                                                                                                                                                                         Auswahlabhängig
  BUILD_ENABLE_CXX_STD                Die Version des C++-Sprachstandards. **C++14** ist der höchstmögliche für FreeCAD 0.19, während wenigstens **C++17** für FreeCAD 0.20 erforderlich ist. Siehe auch den Hinweis im Abschnitt [#Bau mit Visual Studio 15 (2017) oder neuer](#Bau_mit_Visual_Studio_15_(2017)_oder_neuer.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                    Auswahlabhängig
  BUILD_DESIGNER_PLUGIN               Zum Bau des Qt Designer-Plugins, siehe [diesen folgenden Abschnitt](#Qt_Designer_Zusatzprogramm.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          OFF
  BUILD_FLAT_MESH                     Wird benötigt für einen Bau, der die Funktion [EbenesNetzErstellen](MeshPart_CreateFlatMesh/de.md) enthält                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   OFF
  CMAKE_INSTALL_PREFIX                Das Ausgabeverzeichnis bei der Erstellung des Ziels *INSTALL*, siehe auch den Abschnitt [#Ausführen_und_Installieren_von_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Windows Standard-Programminstallationsverzeichnis
  FREECAD_COPY_DEPEND_DIRS_TO_BUILD   Kopiert abhängige Bibliotheken in den Build-Ordner, die zur Ausführung von FreeCAD.exe benötigt werden. Siehe auch den Abschnitt [#Ausführen_und_Installieren_von_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md). **Hinweis:** Die Optionen FREECAD_COPY_XXX erscheinen nur, falls die Bibliotheken nicht bereits kopiert wurden. Wird nur ein Upgrade bzw. Wechsel auf eine andere LibPack-Version benötigt, siehe den Abschnitt[LibPack aktualisieren](#LibPack_aktualisieren.md). Soll zu den Optionen zurückgekehrt werden, müssen alle Verzeichnisse im Build-Ordner gelöscht werden, außer dem LibPack-Verzeichnis. In CMake den Cache löschen und so starten, als würde man zum ersten Mal kompilieren.   OFF
  FREECAD_COPY_LIBPACK_BIN_TO_BUILD   Kopiert LibPack-Binaries in den Build-Ordner, die zur Ausführung von FreeCAD.exe benötigt werden. Siehe auch Abschnitt [#Ausführen_und_Installieren_von_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 OFF
  FREECAD_COPY_PLUGINS_BIN_TO_BUILD   Kopiert Qt-Plugin-Dateien in den Build-Ordner, die zur Ausführung von FreeCAD.exe benötigt werden. Siehe auch Abschnitt [#Ausführen_und_Installieren_von_FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                OFF
  FREECAD_LIBPACK_USE                 Schaltet die Verwendung von FreeCAD LibPack ein bzw. aus (ON/OFF)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ON
  FREECAD_LIBPACK_DIR                 Verzeichnis, in dem sich LibPack befindet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            FreeCADs Quellcodeverzeichnis
  FREECAD_RELEASE_PDB                 Debug-Bibliotheken auch für Freigabe-Versionen erstellen. Dies hat keinen Einfluss auf die Geschwindigkeit (wie es ein echter Debug-Build hätte) und kann sehr nützlich sein, bei der Ermittlung von Absturzstellen im FreeCAD-Code. Sollte FreeCAD abstürzen, wird eine Datei *crash.dmp* erstellt, die mit MSVC geladen werden kann und wenn die zugehörigen PDB-Dateien vorhanden sind sowie der Quellcode jener Version, kann man mit diesem Code debuggen. Ohne diese PDB-Dateien ist es nicht möglich den Code zu debuggen und alles was der Debugger anzeigt, ist der Name der DLL in der der Absturz auftrat.                                                                                                                                ON
  FREECAD_USE_MP_COMPILE_FLAG         Fügt die /MP-Opzion (Multiprocessor-Option) zu Visual Studio-Projekten hinzu, und ermöglicht so eine Beschleunigung auf Mehr-Kern-CPUs. Dies kann den Bau auf modernen Prozessoren wesentlich beschleunigen.**Hinweis:** Wird **FREECAD_USE_PCH** ausgeschaltet, kann das Kompilieren schnell den Zusatzdatenspeicher überladen, auch wenn 16 GB RAM vorhanden sind.                                                                                                                                                                                                                                                                                                                                                                   ON
  FREECAD_USE_PCH                     Header vorkompilieren (siehe [Precompiles the headers](https://en.wikipedia.org/wiki/Precompiled_header) (engl.)), um Kompilierungszeit zu sparen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ON
  FREECAD_USE_PYBIND11                Schließt die Bibliothek [PyBind11](https://github.com/pybind/pybind11) ein. Wird benötigt für einen Build, der die Funktion [CreateFlatMesh feature](MeshPart_CreateFlatMesh/de.md) enthält zu erhalten.**Hinweis:** Nach dem Aktivieren kann man eine Konfigurationsfehlermeldung erhalten. Eifach erneut konfigurieren, und das Problem sollte gelöst sein.                                                                                                                                                                                                                                                                                                                                                                  OFF



## FreeCAD bauen 

Abhängig vom Compiler wird der Prozess zur Erstellung von FreeCAD etwas anders ablaufen. In den folgenden Abschnitten werden die bekannten Arbeitsabläufe beschrieben. Wird mit Qt Creator gebaut, geht es mit [Bau mit Qt Creator (veraltet)](#Bau_mit_Qt_Creator_(veraltet).md) weiter, ansonsten direkt hier:

### Building from cmd.exe command line 

If you want build from the command line, CMake output will show you the proper command to run (which depends on the configured release directory). But this command will produce a *Debug* build which does not work on Windows and results in a Numpy import error in FreeCAD (which is a known issue but hard to fix). You need to specify the *\--config Release* option to force a *Release* build:


```python
cmake --build E:/release --config Release
```

Please note that setting CMake variables like *CMAKE_BUILD_TYPE* does not have any effect, only specifying the *\--config* option as shown above works.


<div class="mw-collapsible mw-collapsed toccolours">



### Bau mit Visual Studio 15 (2017) oder neuer 


<div class="mw-collapsible-content">



#### Bau freigeben 

1.  Starte das Visual Studio IDE. Dies kann entweder durch Drücken der Schaltfläche *Projekt öffnen* in der CMake GUI oder durch Doppelklicken auf die Datei *FreeCAD.sln*, die Du in Deinem Bauordner findest, geschehen.
2.  In der Werkzeugleiste der MSVC IDE versichere dich, dass du für die erste Kompilierung *Release* verwendest.
3.  Es gibt ein Fenster namens *Solution Explorer*. Es listet alle möglichen Kompilierungsziele auf.

Um eine vollständige Kompilierung zu starten, klicke mit der rechten Maustaste auf das Ziel **ALL_BUILD** und wählen dann **Build**. Dies wird nun recht lange dauern.

Um ein einsatzbereites FreeCAD zu kompilieren, kompiliere das Ziel *INSTALL*, siehe Abschnitt [Ausführen und Installieren von FreeCAD](#Ausführen_und_Installieren_von_FreeCAD.md).

Wenn Du keine Fehler bekommst, ist das erledigt. **Herzlichen Glückwunsch!** Du kannst MSVC beenden oder offen lassen.

**Wichtig:** Seit Visual Studio 17.4 kann die Code-Optimierung, die standardmäßig für das Ziel **SketcherGui** aktiviert ist, nicht verwendet werden. Wird sie dennoch eingesetzt, werden Randbedingungen für Winkel in Skizzen nicht richtig platziert. Um dies zu beheben: Ein Rechtsklick auf das Ziel im MSVC solution explorer und der letzte Eintrag **Properties** im Kontextmenü auswählen. Im Dialogfenster, das geöffnet wird, wechselt man zu C/C++ → Optimization und deaktiviert dort die Einstellung **Optimization**. Abschließend das Ziel **ALL_BUILD** erneut erstellen.



#### Fehlersuch Bau 

Für einen Fehlersuch Bau ist es notwendig, dass das Python verwendet wird, das im LibPack enthalten ist. Um dies zu gewährleisten:

1.  Suche in der CMake GUI nach \"Python\".
2.  Wenn du dort einen Pfad wie *C:/Programme/Python38/python.exe* siehst, hat CMake das auf deinem PC installierte Python erkannt und nicht das des LibPack. In diesem Fall passe die verschiedenen Python Einstellungen in CMake wie folgt an (unter der Annahme, dass das LibPack im Ordner *D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17* liegt):

![](images/CMake_Python_settings.png )

As prerequisite for the debug build, you need to do this:

1.  Copy the content of the LibPack folder *bind* to the *bin* folder of the FreeCAD build folder (overwrite the existing files).
2.  Copy the content of the LibPack folder *libd* to the *lib* folder of the FreeCAD build folder.

Jetzt kann kompiliert werden:

1.  Starte die Visual Studio IDE. Dies kann entweder durch Drücken der Schaltfläche *Öffne Projekt* in der CMake GUI geschehen oder durch Doppelklick auf die Datei *FreeCAD.sln*, die du in deinem Bau Ordner findest.
2.  In der Werkzeugleiste der MSVC IDE versichere dich, dass du für die erste Kompilierung *Debug* verwendest.
3.  Es gibt ein Fenster namens *Solution Explorer*. Es listet alle möglichen Kompilierziele auf. Um eine vollständige Kompilierung zu starten, klicke mit der rechten Maustaste auf das Ziel **ALL_BUILD** und wähle dann **Build** im Kontextmenü.

Dies wird nun recht lange dauern.

If there were no compilation errors, and if the **FREECAD_COPY\_\*** options mentioned in the [CMake Configuration step](#CMake.md) above were enabled, you can start the debug build:

1.  Right-click on the target **FreeCADMain** and then choose **Set as Startup Project** in the context menu.
2.  Finally click in the toolbar on the button with the green triangle named **Local Windows Debugger**.

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

1.  Im Windows-Startmenü zu **Visual Studio 2017 → Visual Studio Tools** wechseln und **Developer Command Prompt for VS 2017** auswählen.
2.  Wechsle in deinen Buildordner.
3.  Führe den Befehl aus


```pythonmsbuild ALL_BUILD.vcxproj /p:Configuration=Release```

oder


```pythonmsbuild INSTALL.vcxproj /p:Configuration=Release```

Diese Schritte können auch automatisiert werden. Hier ist zum Beispiel eine Lösung für MSVC 2017:

1.  Lade das Skript herunter [compile-FC.txt](https://forum.freecadweb.org/download/file.php?id=92135).
2.  Umbenennen in *compile-FC.bat*\'.
3.  Klicke im Datei-Explorer von Windows mit der rechten Maustaste auf Dein Build-Verzeichnis und benutze aus dem Kontextmenü *Befehlszeile hier*.
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

Methode 1*: Du führst die FreeCAD.exe aus, die du in deinem Build Verzeichnis findest, im Unterverzeichnis*bin\'\'\'.

*Methode 2*: Du baust das Ziel *INSTALL*

Methode 2 ist die einfachere, da sie automatisch sicherstellt, dass sich alle für die Ausführung der FreeCAD.exe erforderlichen Bibliotheken im richtigen Ordner befinden. Die FreeCAD.exe und die Bibliotheken werden in dem Ordner ausgegeben, den du in der CMake-Variablen *CMAKE_INSTALL_PREFIX* angegeben hast.

Für Methode 1 müssen die Optionen **FREECAD_COPY\_\*** aktiviert werden, die oben in den [CMake](#CMake.md)-Konfigurationsschritten erwähnt wurden.

### Troubleshooting

When running FreeCAD you may encounter missing DLLs when using certain workbenches or features of workbenches. The error message in FreeCAD\'s console will not tell you what DLL is missing. To find this out you must use an external tool:

-   Download the latest release of the program **Dependencies**: <https://github.com/lucasg/Dependencies/releases> (choose the file *Dependencies_x64_Release.zip*)
-   In the FreeCAD [Python console](Python_console.md) execute these commands:

import os
os.system(r"~\DependenciesGui.exe")

**Note**: Instead of the \~ you must specify the full path to the *DependenciesGui.exe* on your system.

-   Now drag in the \*.pyd file of the workbench with which you get missing DLLs reported.



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

1.  Öffne die MSVC-IDE, indem Du entweder auf die Datei *FreeCAD.sln* oder auf die Datei *ALL_BUILD.vcxproj* in Deinem Build-Verzeichnis doppelklickst.
2.  Fahre mit Schritt 2 aus dem Abschnitt [Building with Visual Studio 15 2017](#Building_with_Visual_Studio_15_.282017.29_or_newer.md) fort.

## Updating the LibPack 

If a new major version of a third-party dependency like Open Cascade is released, or if a third-party dependency has important bug fixes, a new LibPack is released. You can find the latest version [here](https://github.com/FreeCAD/FreeCAD-LibPack/releases/).

To update your LibPack the following recipe is best practice:

1.  Delete the *bin* folder in your build folder.
2.  Switch to your local LibPack folder and delete everything there.
3.  Extract the content of the new LibPack ZIP file into the existing, but now empty, local LibPack folder.
4.  Open CMake and there press the button **Configure** and then the button **Generate**. This recreates the *bin* folder you just deleted and also copies the new LibPack files into it.
5.  In CMake click the button **Open Project** and the MSVC IDE will open.
6.  In the MSVC IDE build the target *INSTALL*.



## Werkzeuge

Um an der FreeCAD Entwicklung teilzunehmen, solltest du die folgenden Werkzeuge kompilieren und installieren:



### Qt Designer Zusatzprogramm 

FreeCAD verwendet [Qt](https://en.wikipedia.org/wiki/Qt_(software)) als Werkzeugsatz für seine Benutzeroberfläche. Alle Dialoge sind in UI-Dateien eingerichtet, die mit dem Programm [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) bearbeitet werden können, das Teil jeder Qt Installation ist und auch im LibPack enthalten ist. FreeCAD hat seinen eigenen Satz von Qt Widgets, um spezielle Funktionen wie das Hinzufügen einer Einheit zu Eingabefeldern und das Setzen von Voreinstellungen zu ermöglichen.



#### Kompilierung

Das Plugin kann nicht vom Qt Designer geladen werden, wenn es mit einer anderen Qt-Version kompiliert wurde, als der, auf der der aktuelle Qt Designer/Qt Creator basiert. Deshalb muss das Plugin mit FreeCAD zusammen kompiliert werden.

-   In the CMake options (see [this section above](Compile_on_Windows#Options_for_the_build_process.md)) enable the option BUILD_DESIGNER_PLUGIN and reconfigure.
-   open MSVC and build the target **FreeCAD_widgets**

As result you will get the plugin file *\'FreeCAD_widgets.dll* in the folder*\~\\src\\Tools\\plugins\\widget\\Release*



#### Einrichtung

Um das Plugin zu installieren, wird die DLL wie folgt kopiert:

-   Wird das LibPack verwendet, in den Ordner *\~\\FreeCADLibs_2_8_x64_VC2019\\plugins\\designer*

-   Ist eine vollständige Qt-Installation vorhanden, kann zwischen den Ordnern*C:\\Qt\\Qt5.15.2\\msvc2019_64\\plugins\\designer*oder*C:\\Qt\\Qt5.15.2\\msvc2019_64\\bin\\designer* ausgewählt werden (zuerst muss der Unterordner *designer* angelegt werden.)(\... und die Pfade an die Installation angepasst!).

Abschließend den Qt Designer (erneut) starten und sein Menü **Hilfe → Zusatzprogramme** überprüfen. Wenn das Plugin **FreeCAD_widgets.dll** als geladen aufgeführt ist, können jetzt FreeCADs .ui-Dateien entworfen und geändert werden. Falls nicht, musst man die DLL selbst [kompilieren](#Kompilierung.md).

Soll lieber der [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator) anstelle des Qt Designers verwenden werden, muss die Plugin-Datei in diesem Ordner abgelegt werden:*C:\\Qt\\Qt5.15.2\\Tools\\QtCreator\\bin\\plugins\\designer*Dann den Qt Creator (erneut) Starten, in den Modus **Design** wechseln und dann das Menü **Werkzeuge → Formular Editor → Über Qt Designer Zusatzprogramme** überprüfen. Wenn das Plugin **FreeCAD_widgets.dll** als geladen aufgeführt ist, können nun FreeCADs .ui-Dateien entworfen und geändert werden. Falls nicht, musst man die DLL selbst [kompilieren](#Kompilierung.md).

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
8.  Du sollte nun die Datei **ALL_BUILD.vcxproj** im Verzeichnis *\~\\src\\Tools\\thumbs\\ThumbnailProvider* haben. Doppelklicke darauf und die MSVC-IDE wird sich öffnen.
9.  Stelle in der Werkzeugleiste der MSVC-IDE sicher, dass du das Kompilationsziel *Release* verwendest.
10. Es gibt ein Fenster namens *Solution Explorer*. Rechtklicke dort auf **ALL_BUILD** und wähle dann **Build**.
11. Als Ergebnis solltest du nun eine Datei **FCStdThumbnail.dll** im Verzeichnis *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release* haben, die du wie oben beschrieben installieren kannst.



## Open Cascade kompilieren 

Das LibPack kommt mit einer Version von [Open Cascade](https://en.wikipedia.org/wiki/Open_Cascade), die für den allgemeinen Gebrauch geeignet ist. Unter bestimmten Umständen kann es jedoch wünschenswert sein, gegen eine alternative Version von Open Cascade zu kompilieren, wie z.B. eine der offiziellen Versionen oder einem gepatchten Zweig.

When compiling Open Cascade for FreeCAD note that there is no guarantee that FreeCAD will work with all versions of Open Cascade. Note also that when you are using the Netgen library, you must use the a NetGen version that it approved to compile with the Open Cascade version you like to compile.

Zum Kompilieren:

-   Zuerst den Open Cascade-Quellcode beschaffen, entweder direkt von [Open Cascade\'s git repository](https://github.com/Open-Cascade-SAS/OCCT) oder durch klonen des Zweiges eines dritten, wie z.B. [der \"blobfish\"-Zweig](https://gitlab.com/blobfish/occt), der von dem Mitglied des FreeCAD-Forums [tanderson69](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=208) gepflegt wird.

-   Dann die CMake-GUI öffnen, um das Build-System in einer ähnlichen Weise zu konfigurieren, wie den FreeCAD-Bau. Diese CMake-Optionen müssen gesetzt werden (oder explizit nicht gesetzt werden):

  Variablenname                      Beschreibung                                                                                                                                                                                                                                                                                                                                                                     Vorgabewert
    
  3RDPARTY_DIR                       Der Pfad zu Drittanbieterkomponenten. Es wird empfohlen, den Ordner als Quellordner zu verwenden, der das LibPack enthält. Daher dieses Feld leer lassen.                                                                                                                                                                                                                        leer
  3RDPARTY_DOXYGEN_EXECUTABLE        Der Pfad zu der ausführbaren Datei der Drittanbieterkomponente [Doxygen](https://en.wikipedia.org/wiki/Doxygen). Es wird empfohlen Doxygen zu installieren. CMake findet es dann automatisch.                                                                                                                                                                                    leer
  3RDPARTY_FREETYPE_DIR              Der Pfad zu der benötigten Drittanbieterkomponente [Freetype](https://en.wikipedia.org/wiki/FreeType). Es wird empfohlen, den Ordner als Quellordner zu verwenden, der das LibPack enthält.                                                                                                                                                                                      leer
  3RDPARTY_RAPIDJSON_DIR             Only available if **USE_RAPIDJSON** is used. Der Pfad zu der Drittanbieterkomponente [RapidJSON](https://rapidjson.org/). Es wird empfohlen, den Ordner, der das LibPack enthält, NICHT als Quellordner zu verwenden. Man kann den RapidJSOn-Ordner eines LibPacks verwenden, aber er sollte in einen neuen Ordner kopiert werden und dieser als Quellordner verwendet werden.   leer
  3RDPARTY_TCL_DIR                   Der Pfad zu der benötigten Drittanbieterkomponente [TCL](https://en.wikipedia.org/wiki/Tcl). Es wird empfohlen, den Ordner, der das LibPack enthält, NICHT als Quellordner zu verwenden. Man nimmt beispielsweise eine [dieser Veröffentlichungen](https://github.com/teclab-at/tcltk/releases), extrahiert sie und verwendet sie als Quellordner für CMake.                     leer
  3RDPARTY_TK_DIR                    Der Pfad zu der benötigten Drittanbieterkomponente [TK](https://en.wikipedia.org/wiki/Tk_(software)). Es wird empfohlen, den Ordner, der das LibPack enthält, NICHT als Quellordner zu verwenden. Man nimmt beispielsweise eine [dieser Veröffentlichungen](https://github.com/teclab-at/tcltk/releases), extrahiert sie und verwendet sie als Quellordner für CMake.            leer
  3RDPARTY_VTK_DIR                   Only available if **USE_VTK** is used. Der Pfad zu der necessary 3rdparty component [VTK](https://en.wikipedia.org/wiki/VTK). Es wird empfohlen, den Ordner als Quellordner zu verwenden, der das LibPack enthält. Wird ein anderer Ordner verwendet, sollte sichergestellt sein, dass nicht VTK 9.x oder neuer verwendet wird.                                                  leer
  BUILD_RELEASE_DISABLE_EXCEPTIONS   Deaktiviert das Error-Handling für Release-Builds. Fur FreeCAD muss es auf **OFF** gesetzt werden.                                                                                                                                                                                                                                                                               ON
  INSTALL_DIR                        Der Ausgabeordner, wenn das Ziel *INSTALL* erstellt wird. War die Erstellung erfolgreich, können Dateien aus diesem Ordner zum Aktualisieren des LibPacks verwendet werden.                                                                                                                                                                                                      Windows standardmäßiger Ordner zur Installation von Programmen
  INSTALL_DIR_BIN                    Der Ausgabe-Unterordner für die DLLs, wenn das Ziel *INSTALL**erstellt wird. Er muss zu**bin*\' geändert werden.                                                                                                                                                                                                                                                                 win64/vc14/bin
  INSTALL_DIR_LIB                    Der Ausgabe-Unterordner für die .lib-Dateien, wenn das Ziel *INSTALL**erstellt wird. Er muss zu**lib*\' geändert werden.                                                                                                                                                                                                                                                         win64/vc14/lib
  USE_RAPIDJSON                      Zum Kompilieren von Open Cascade mit Unterstützung für RapidJSON. Dies ist zwingend zu aktivieren, um Unterstützung für das Dateiformat [glTF](https://en.wikipedia.org/wiki/Gltf) zu erhalten.                                                                                                                                                                                  OFF
  USE_VTK                            Zum Kompilieren von Open Cascade mit Unterstützung für VTK. Dies zu aktivieren ist optimal (optional?). Es kann zum Bau von Open Cascades VTK-Bridge verwendet werden.                                                                                                                                                                                                           OFF

-   Open the project in Visual Studio and first build the ALL_BUILD and then INSTALL targets in the **Release** mode.
-   Repeat building the two targets in the **Debug** mode.

To build FreeCAD using the self-compiled Open Cascade, you must do the following:

-   Copy all folders from the INSTALL_DIR to your LibPack folder (overwrite the existing files)
-   Switch to the LibPack folder and go there to the subfolder *cmake*
-   Open there the file *OpenCASCADEDrawTargets.cmake* with a text editor
-   Search there for absolute paths to your LibPack folder and remove them. So e.g. the absolute path*D:/FreeCADLibs_12.5.4_x64_VC17/lib/freetype.lib*becomes just *freetype.lib*
-   Do the same for the file *OpenCASCADEVisualizationTargets.cmake*



## Netgen kompilieren 

The LibPack comes with a version of [Netgen](https://ngsolve.org) that will was tested to be build with the Open Cascade version of the LibPack. The problem is that every new release of Netgen changes the API. Also every new release of Open Cascade does the same. Therefore one cannot just easily change the Netgen version.

However, you might build Netgen nevertheless. This is an easy task:

-   First obtain the Netgen source code, either directly from [Netgen \'s git repository](https://github.com/NGSolve/netgen).
-   Then open the CMake GUI to configure the build system in a similar manner to building FreeCAD. These CMake options have to be set:

  Variable name          Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Default
    
  CMAKE_INSTALL_PREFIX   The output folder when building the target *INSTALL*. If the build was successful, take the files from this folder to update your LibPack.                                                                                                                                                                                                                                                                                                                                                                                                        C:/netgen
  OpenCasCade_DIR        The path to the CMake files of Open Cascade. If you built Open Cascade as described in the section [Compiling Open Cascade](#Compiling_Open_Cascade.md) you can use the subfolder *cmake* of there folder you used as INSTALL_DIR. If not, use the subfolder *cmake* of your LibPack. Note hereby that the LibPack must then already contain a proper Open Cascade build. Independent what folder you use, you must now also create there a subfolder *lib* and copy in the files *freetype.lib* and *freetyped.lib* from your LibPack.   empty
  USE_GUI                set it to **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ON
  USE_NATIVE_ARCH        set it to **OFF**; this is only necessary important to support older CPU that don\'t have the [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) instruction set                                                                                                                                                                                                                                                                                                                                                                    ON
  USE_OCC                set it to **ON**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  OFF
  USE_PYTHON             set it to **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ON
  USE_SUPERBUILD         set it to **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ON
  ZLIB_INCLUDE_DIR       The path to the necessary 3rdparty component [zlib](https://en.wikipedia.org/wiki/Zlib). It is recommended to use the folder as input where your used LibPack is.                                                                                                                                                                                                                                                                                                                                                                                 empty
  ZLIB_LIBRARY_DEBUG     The path to the ZLib file *zlibd.lib*. It is located in the subfolder *lib* of your LibPack folder.                                                                                                                                                                                                                                                                                                                                                                                                                                               empty
  ZLIB_LIBRARY_RELEASE   The path to the ZLib file *zlib.lib*. It is located in the subfolder *lib* of your LibPack folder.                                                                                                                                                                                                                                                                                                                                                                                                                                                empty

-   Additionally you need to add a new CMake entry:

name: *CMAKE_DEBUG_POSTFIX*, type: *string*, content: **\_d** This assures that he file names of the debug libraries get another name than the release libraries and can later not be accidentally exchanged.

-   Press the *Configure* button in CMake to generate the \*.cmake files.
-   Only necessary if older CPU should be supported that don\'t have the AVX2 instruction set:
    -   Search your Netgen build folder for the file *netgen-targets.cmake* and open it with a text editor. Remove the setting *;/arch:AVX2* in the Option INTERFACE_COMPILE_OPTIONS.
    -   Press the *Configure* button in CMake again.
-   Press the *Generate* button in CMake.
-   Open the project in Visual Studio and first build the ALL_BUILD and then INSTALL targets in the **Release** mode.
-   Repeat building the two targets in the **Debug** mode.

To build FreeCAD using the self-compiled Netgen, you must do the following:

-   Copy all folders from the CMAKE_INSTALL_PREFIX to your LibPack folder (overwrite the existing files)



## Referenzen

Siehe auch

-   [Kompilieren - Beschleunigen](Compiling_(Speeding_up).md)



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Windows/de
