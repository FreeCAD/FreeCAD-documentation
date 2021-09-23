# AppImage/de
 **Seit dem 7. Juli 2019 beobachtet die FreeCAD Gemeinschaft, dass das Herunterladen von AppImages von Github vor der Fertigstellung eine Zeitüberschreitung zu haben scheint. Wir sind uns nicht sicher, warum dies geschieht. Wenn dies bei dir passiert, versuche bitte das Herunterladen erneut. Es dauert ein paar Versuche. Es wird empfohlen, die Funktion AppImage [https://www.freecadweb.org/wiki/Appimage#Automatic_updating Auto-Aktualisierungsfunktion] zu verwenden, die das Herunterladen an der Stelle wiederherstellt, an der er fehlgeschlagen ist.**


{{TOCright}}

## Was ist ein AnwendungsAbbild? 

![](images/AppImage-logo.png ) **Einmal verpackt und dann überall laufend. Erreiche Benutzer auf allen Haupt Linux Desktop Distributionen.**

AnwendungsAbbild ist ein \"universelles Binärpaket\", das dazu bestimmt ist, eine Anwendung an jede beliebige Linux Distribution zu verteilen. Lies mehr darüber auf der [Appimage Homepage](https://appimage.org) und [Wikipedia](https://en.wikipedia.org/wiki/AppImage).

Um es auszuführen, mache es zunächst ausführbar und gib dann den relativen oder vollständigen Pfad ein. 
```python
chmod +x FreeCAD_x86_64.AppImage
./FreeCAD_x86_64.AppImage
```

Für andere Installationsarten siehe [Herunterladen](Download/de.md).

## FreeCAD AnwendungsAbbilder 


**'''Note:''' Entwicklungs-Builds werden nun auf dem [https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds '''FreeCAD-Bundle'''] github repo bereitgestellt.<br/>Wenn die untenstehenden Download-Verknüpfungen nicht funktionieren, lade die Dateien bitte manuell aus dem eingeklappten Abschnitt "Assets" unter dem o.g. Link herunter.**

  Stabil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Entwicklung
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
  ![](images/AppImage-logo.png ) \[<https://github.com/FreeCAD/FreeCAD/releases/download/>{{:Template:Stable-Major-and-Minor-Version}}/FreeCAD\_{{:Template:Stable-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage {{:Template:Stable-Version}}\] (\[<https://github.com/FreeCAD/FreeCAD/releases/download/>{{:Template:Stable-Major-and-Minor-Version}}/FreeCAD\_{{:Template:Stable-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage-SHA256.txt SHA256\])   ![](images/AppImage-logo.png ) \[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{:Template:Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage {{:Template:Development-Version}}\] (\[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{:Template:Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage-SHA256.txt SHA256\])

  : style=\"text-align: center; font-size: 150%; \| Verfügbare FreeCAD AnwendungsAbbilder \|+

**Wichtige Hinweise:**.

-   Die Entwicklung erfolgt täglich und schnell, die Verknüpfung mit dem aktuellsten AnwendungsAbbild ist ein bewegliches Ziel.
-   Die obige Entwicklungsverknüpfung sollte aktuell sein, da er über ein Skript aktualisiert wird.
-   Viele Anwender im Forum nutzen die Entwicklungsversion.
-   Es kann auf dem gleichen System parallel zu einer anderen Version von FreeCAD ausgeführt werden.
-   Anwender verwenden die dev Version, um die neuesten Funktionen und Fehlerbehebungen zu nutzen (da FreeCAD einen langen Veröffentlichungszyklus hat). Sie nutzen es auch, um Fehler zu testen und zu finden, um die Entwicklung und Verbesserung von FreeCAD voranzutreiben.

#### Obligatorisches Wort der Vorsicht 

In den meisten Fällen ist die Entwicklungsversion stabil, aber natürlich ist es wichtig, die obligatorische Erklärung hinzuzufügen, dass die Verwendung auf eigenes Risiko erfolgt. Obwohl die meisten Leute, die Datensicherungen verwenden und \"oft speichern\", dies recht gut tun.

## Automatische Aktualisierung 

AnwendungsAbbild bietet eine intelligente und wirtschaftliche Möglichkeit der Aktualisierung. Es berechnet den Unterschied zwischen dem neuen und dem alten AnwendungsAbbild und lädt nur die Änderungen zwischen den Versionen herunter. Theoretisch lädt der Benutzer am Ende jedes Mal etwa 15% statt eines völlig neuen AnwendungsAbbild herunter.

Die automatische Aktualisierung erfolgt über mehrere optionale Methoden. Derzeit gibt es 4 Methoden, 2 über die grafische Oberfläche (GUI) und 2 über die Befehlszeilen-/Terminaloberfläche (CLI).

### Experimentelle In-Anwendungs-Aktualisierung 

Dank der Bemühungen mehrerer wichtiger Schlüsselentwickler gibt es [laufende Bemühungen](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324), eine Funktion zu integrieren, die es ermöglicht, das AnwendungsAbbild innerhalb von FreeCAD selbst zu aktualisieren. Beginnend mit FC 0.19.21514 gibt es nun einen Abschnitt AnwendungsAbbild, der über {{MenuCommand/de|Bearbeiten → Einstellungen → AnwendungsAbbild}} gefunden werden kann. Bitte teste diese Fähigkeit und berichte über deine Erfahrungen in der [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324).

### GUI Methode 1 (offiziell) 

Dies ist die offizielle AppImageUpdate GUI-Anwendung.

1.  Herunterladen [AppImageUpdate-x86\_64.AppImage](https://github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Mache es ausführbar, indem Du mit der rechten Maustaste auf die Datei klickst, in die Eigenschaften gehst und \"Als ausführbare Datei ausführen\".
3.  Doppelklicke auf das AppImage Symbol, ein Dialogfeld erscheint und Du wirst aufgefordert, anzugeben, welches AppImage Du aktualisieren möchtest.
4.  Gib den Pfad zu Deinem vorhandenen AppImage an.
5.  Sobald das AppImage aktualisiert ist, drücke die Schaltfläche **Run updated AppImage**.

### GUI Methode 2 (inoffiziell) 

Dies ist eine elegantere inoffizielle Version von AppImageUpdate von Drittanbietern mit dem Namen: **AppImageUpdater**. Es befindet sich noch in der Entwicklung (zum Zeitpunkt dieser Wiki-Bearbeitung), ist aber dennoch recht angenehm zu bedienen.

1.  Herunterladen [AppImageUpdater-\*-x86\_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Mache es ausführbar: 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Lauf es durch: 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Finde Dein aktuelles FreeCAD AppImage und ziehe es per Drag-and-Drop in den AppImageUpdater.

Ergebnis: Folge den Anweisungen des AppImageUpdaters.

### CLI Methode 1 (offiziell) 

Führe die folgenden Anweisungen in Deinem Terminal aus


```python
wget https://github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Anmerkungen:

-   Die Dateinamen werden einzigartig sein, da die Versionsinfo in sie eingebettet ist. Die obigen Anweisungen sind aus Gründen der Übersichtlichkeit vereinfacht.
-   Führen Sie `./appimageupdatetool-x86_64.AppImage --help` aus, um mehr über Funktionen wie `--remove-old`, `--overwrite` und `--self-update` zu erfahren.
-   Es gibt auch eine i386-Version; siehe die Seite [AppImageUpdate release](https://github.com/AppImage/AppImageUpdate/releases).

Zu erledigen: Teile ein Skript, das als Alias oder Cron Job hinzugefügt werden kann.

### CLI Methode 2 (inoffiziell) 

Ähnlich wie bei den grafischen Methoden mit offiziellen und inoffiziellen Ansätzen zum Herunterladen von AppImages gilt dies auch für die Befehlszeile. Dies ist eine elegantere Drittanbieter Befehlszeilenoption zum Herunterladen von AppImages.

1.  Herunterladen [appimageupdater-\*-x86\_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Mache es ausführbar: 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Ausführen: 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/oldd/FreeCAD-AppImage.AppImage```

**Ergebnis**\': Aktualisiert die angegebene AppImage-Datei, wenn ein Update existiert.

# Experimentell

## AppImage zsync korrigieren 

Es kann sein, dass ein AppImage nicht aktualisiert werden kann, weil die Zieldatei auf irgendeine Weise verändert wurde. Anstatt ein komplett neues appimage herunterzuladen, ist es möglich, die von AppImage verwendete zsync-Datei so umzuschreiben, dass nur das Delta heruntergeladen wird. Mehr Informationen gibt es unter [1](https://github.com/antony-jr/appimage-update-info-writer).

Dieser Abschnitt benötigt mehr Details.

## Herunterladen via Bittorrent 

Das FreeCAD-Paketierungs-Team erprobt gerade (Dank an die Arbeit von Antony-jr) das Herunterladen eines AppImage-Delta von FreeCAD via bittorrent. Das Repository-Thema findet sich unter <https://github.com/FreeCAD/FreeCAD-Bundle/issues/49>.

# Entwickler Abschnitt 


**Hinweis:**

Die folgenden Abschnitte sind für Entwickler gedacht.

## Entpacken von AnwendungsAbbildern 

Ein sehr komfortabler Aspekt von FreeCAD ist, dass ein Großteil davon in [Python](Python/de.md) gebaut ist, das nicht manuell wie C++ kompiliert werden muss. Im Wesentlichen kann eine Python Datei geändert werden, und beim Neustart von FreeCAD werden diese Änderungen in die Anwendung integriert. Ein Entwickler kann mit dieser Technik und einem AppImage schnell an der neuesten FreeCAD Version arbeiten. Darüber hinaus verändert die Verwendung eines AppImage die Systemumgebung Ihres Systems in keiner Weise, d.h. es wird nichts installiert und es werden keine Umgebungsvariablen geändert.

### AnwendungsAbbilder ändern 

Ein AnwendungsAbbild bettet ein Dateisystem mit allem ein, was zum Ausführen der Anwendung erforderlich ist. Um es zu modifizieren, muss das Dateisystem extrahiert werden.


```python
./FreeCAD_xxx.AppImage --appimage-extract
cd squashfs-root/
```

Öffne nun die gewünschten Python Quelldateien in Deinem bevorzugten Code Editor, ändere sie und speichere sie. Führe dann die Anwendung aus.


```python
./AppRun
```

### AnwendungsAbbilder neu packen 

Wenn du den Code geändert hast und nun das AnwendungsAbbild mit deinen letzten Änderungen neu packen möchtest, verwende das Werkzeug [appimagetool-x86\_64](https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) auf dem extrahierten Dateisystem.


```python
cd ..
wget "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```

## Personalisierte AnwendungsAbbilder 

Dank der Arbeit von **realthunder**, Autor von [Anwendungsverknüpfung](App_Link/de.md) und [Assembly3 Arbeitsbereich](Assembly3_Workbench/de.md), ist es möglich, benutzerdefinierte AnwendungsAbbilder mit Hilfe einer Reihe von Skripten zu erstellen.

Dies macht es sehr bequem, Bilder für einen bestimmten Zweig des Quellcodes für andere zum Testen freizugeben. Obwohl AnwendungsAbbilder nur unter Linux funktioniert, ermöglichen es die Skripte von realthunder, AnwendungsAbbilder auch unter Windows und MacOS zu generieren.

Das Repositorium für diese Skripte befindet sich unter [realthunder/FreeCADMakeImage](https://github.com/realthunder/FreeCADMakeImage). Bitte lies die [Readme.md](https://github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md) für weitere Einzelheiten.



[Category:Packaging](Category:Packaging.md) [Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Testing](Category:Testing.md)
