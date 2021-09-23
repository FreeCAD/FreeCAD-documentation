# Installing on Mac/de
FreeCAD kann unter macOS aus einem .dmg-Paket installiert werden, das du per Drag & Drop in deinen Programme Ordner ziehen kannst:


{{DownloadMacStable}}

und der wöchentliche Bau kann heruntergeladen werden von

<img alt="" src=images/Nightly.png  style="width:30px;">[Wöchentlich](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

Du kannst auch einen Paketmanager wie HomeBrew verwenden, um deine Software auf dem neuesten Stand zu halten. Eine Anleitung zur Installation von HomeBrew findest du [hier](https://brew.sh/). Wenn HomeBrew installiert ist, kannst du FreeCAD 0.18.4 einfach über dein Bash Terminal installieren mit


```python
brew install --cask freecad
```

und um die neueste verfügbare Version (0.19pre) auf HomeBrew zu verwenden, kannst du


```python
brew install freecad
```

Wenn es irgendwelche Probleme mit dem HomeBrew Cask oder Formula gibt, kannst du diese an [hier](https://github.com/FreeCAD/homebrew-freecad) melden.

Diese Seite beschreibt die Verwendung und die Funktionen des FreeCAD Installationsprogramms. Sie enthält auch Anweisungen zur Deinstallation. Nach der Installation kannst du [loslegen](Getting_started/de.md)!

## Einfache Installation 

Das FreeCAD Installationsprogramm wird in Form eines Anwendungspakets (.app) bereitgestellt, das in einer Datenträgerabbild Datei enthalten ist.

Du kannst das neueste Installationsprogramm von der Seite [Download](Download/de.md) herunterladen. Nachdem du die Datei heruntergeladen hast, mounte einfach das Datenträgerabbild und ziehen es dann in den Anwendungsordner oder in einen Ordner deiner Wahl.

![](images/mac_installer_1.png )

Das wars. Klicke einfach auf die App, um FreeCAD zu starten. Wenn du diese Meldung hast \"FreeCAD kann nicht geöffnet werden, da es von einem nicht identifizierten Entwickler stammt. \"Öffne den Ordner (Application) und klicke mit der rechten Maustaste auf die App. Klicke dann auf Öffnen und akzeptieren, um die Applikation zu öffnen.

## Deinstallation

Derzeit gibt es kein Deinstallationsprogramm für FreeCAD. Um FreeCAD und alle installierten Komponenten vollständig zu entfernen, ziehe die folgenden Dateien und Ordner in den Papierkorb:

-   In /Applications:
    -   FreeCAD

Wenn du FreeCAD mit Homebrew installiert hast, verwende einfach den Befehl `brew uninstall freecad`. Das war\'s.

---
[documentation index](../README.md) > Installing on Mac/de
