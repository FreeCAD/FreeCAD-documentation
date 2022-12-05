# Installing Helpfile/de
{{TOCright}}

## Help module 

**Note:** The FreeCAD offline help files, described below, are being retired. The help system of FreeCAD is now managed by the [Help Addon](https://github.com/yorikvanhavre/FreeCAD-Help), which you can install via the [Addon manager](Std_AddonMgr.md). The Help Addon is able to access online documentation, without the need to download anything, or an offline, downloadable copy of the documentation, which can also be installed via the Addon manager.

## FreeCAD Hilfedateien 

Die FreeCAD Offline Dokumentation wird aus dem FreeCAD Wiki durch die Verwendung von Skripten erstellt. Sie ist auf eine Dateigröße von über 220 MB angewachsen. Diese großen Dateien sind nicht Teil der Installationsprogramme und ausführbaren Dateien von FreeCAD, können aber, wie hier dokumentiert, separat installiert werden.

Übersetzungen aus der Gemeinschaft sind erwünscht, daher ist die Offline Dokumentation jetzt auch in Französisch und Italienisch verfügbar. Andere Sprachen können sich in unterschiedlichen Stadien der Vollständigkeit befinden.

## Herunterladen Hilfedateien 

Eine funktionsfähige lokale Dokumentation besteht aus mindestens zwei Dateien: **freecad.qhc**, die Qt-Hilfedatei-Konfiguration und **freecad.qch**, die komprimierte Qt-Hilfedatei. Beide sind zusammen in ein ZIP-Archiv gepackt.

Die Hilfedateien können hier heruntergeladen werden: <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z>

Als zukünftige Option können sie auch innerhalb von FreeCAD mit dem [Addon-Manager](Std_AddonMgr/de.md) installiert werden.

Die Hilfedateien haben immer die gleichen Namen:**freecad.qhc** und **freecad.qch**. Um verschiedene Versionen dieser Hilfsdateien zu haben, müssen sie in unterschiedlichen Verzeichnissen gespeichert werden. Falls die Dokumentation manuell heruntergeladen wird, ist die ZIP-Datei lokal zu speichern und in das gewünschte Dateiverzeichnis zu extrahieren.

## Registrieren der Dokumentation 

Das Dokumentationssystem von FreeCAD verwendet Qt Assistant. Du solltest dieses Programm zuerst installieren, falls du es noch nicht hast.

Die aktuelle Gliederung der Offline Hilfe erlaubt es, dass nur eine Hilfedatei aktiv sein kann. Es ist daher nicht möglich, gleichzeitig Hilfedateien in verschiedenen Sprachen von FreeCAD aus zugänglich zu machen.

Um eine andere Version der FreeCAD Dokumentation aktiv zu machen, sind die folgenden Schritte anzuwenden:

-   Klicke innerhalb von FreeCAD im Menü **Hilfe → Hilfe**. Das Programm Qt-Assistenten sollte sich öffnen.
-   Klicke in Qt-Assistenten im Menü **Bearbeiten → Einstellungen**.
-   Im Einstellungsdialog klicke auf den **Dokumentation**s Reiter.
-   Wähle in der Liste der registrierten Dokumentationen den Eintrag `org.freecad.usermanual` und klicke auf die Schaltfläche **Entfernen**.
-   Schließe den Dialog mit **OK**, aber schließe nicht den Qt-Assistenten. Dies ist wichtig, da sonst eine weitere Hilfedatei nicht registriert wird.
-   Öffne erneut den Einstellungsdialog über das Menü **Bearbeiten→ Einstellungen**.
-   Wähle den Dokumentationsreiter und klicke auf die Schaltfläche **Hinzufügen...**
-   Navigiere im Dialog zu deiner neuen Hilfedatei und wähle **freecad.qch**
-   Schließe den Dialog durch Bestätigen deiner Auswahl. Im Reiter **Dokumentation** in den Voreinstellungen sollte nun eine Zeile mit `org.freecad.usermanual` vorhanden sein.
-   Schließe die **Einstellungen** mit **OK**.
-   Du solltest nun die neue Dokumentation im Qt-Assistenten zur Verfügung haben, der von FreeCAD aus zugänglich ist.

## Ein Hinweis zu Ubuntu 

Beim Versuch, die Dokumentationspakete unter Ubuntu zu installieren (z.B. `freecad-doc` oder `freecad-daily-doc`), können Schwierigkeiten auftreten. Sollte dies der Fall sein, kannst du durch die Ausführung der folgenden Schritte die Dokumentation offline verfügbar machen.

-   Lade die Hilfedateien **freecad.qch** und **freecad.qch** von <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z> herunter und entpacke sie mit 7zip.
-   Alternativ kannst du stattdessen die Entwicklungsversionen der Hilfedateien **freecad.qhc** und **freecad.qch** von [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Doc) erhalten. Du musst die .part Dateien zusammen [verketten](http://man7.org/linux/man-pages/man1/cat.1.html): `cat freecad.qch.part00 freecad.qch.part01 freecad.qch.part02 freecad.qch.part03 > freecad.qch`.
-   Mit administrativen Rechten (z. B. `sudo`) kopierst oder verschiebst du **freecad.qhc** und **freecad.qch** nach **/usr/share/doc/freecad-doc/**. Wenn du `freecad-daily` verwendest, wird dies stattdessen **/usr/share/doc/freecad-daily-doc/** sein.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing Helpfile/de
