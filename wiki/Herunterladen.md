 {{TOCright}}

## Aktuelle stabile Version 

Die erste Version 0.19.2 von FreeCAD (24291) wurde am 22.04.2021 veröffentlicht. Um herauszufinden, was es Neues gibt, lese bitte die [Veröffentlichungshinweise](Release_notes_0.19/de.md).

SHA256 Prüfsummen zur Überprüfung der Integrität Deines Downloads findest Du auf der [0.19.2 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).

Frühere Versionen können von der [Versionen](https://github.com/FreeCAD/FreeCAD/releases) Seite heruntergeladen werden.

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| [64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-installer1.exe) (includes installer) |   | [macOS](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD_0.19-24291-macOS-x86_64-conda.dmg) 64-bit |   | [AppImage](AppImage.md) 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+

### Hinweise für Windowsbenutzer 

-   Das 32-Bit Installationsprogramm (x86) unterstützt die folgenden Versionen von Windows: 7/8/10.
-   Das 64-Bit Installationsprogramm (x64) unterstützt die folgenden Versionen von Windows: 7/8/10.
-   Eine portable Version ([64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)), die keine Installation benötigt, befindet sich auf der Veröffentlichungsseite.
-   Das Paket kann auch vom [Chocolatey](https://chocolatey.org/packages/freecad) Verwalter installiert werden.

### Hinweise für Mac OS X Benutzer 

Mac OS X 10.12 *Sierra* ist die minimal unterstützte Version.

### Hinweise für GNU/Linux Anwender 

Die meisten Distributionen führen FreeCAD in ihren offiziellen Repositorien, aber wenn die Distribution nicht einem rollierenden Veröffentlichungs Modell folgt, kann die von ihnen bereitgestellte Version veraltet sein. Stattdessen kannst Du das AppImage oben herunterladen, als ausführbar markieren und ohne Installation starten.

Bitte schau auf der Seite [Installation unter Linux](Installing_on_Linux/de.md) nach weiteren Installationsoptionen, einschließlich täglicher Pakete für Ubuntu und Derivaten.

Eine portable Version, welche keine Installation benötigt, kann durch Starten von FreeCad mit diesen Befehlen erreicht werden: {{Version/de|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```

Weitere Informationen über die Umgebungsvariablen von FreeCAD können auf der [Konfigurationsseite](Start_up_and_Configuration/de#Environment_variables.md) gefunden werden.

## Entwicklungsversionen

Die Entwicklung von FreeCAD ist aktiv.

-   Für Linux Anwender probiere die Entwicklung [AppImage](AppImage/de.md) aus.
-   Für MacOS und Windows Entwicklungsbuilds und Entwicklungsquellcode siehe die [weekly builds](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds) Seite.
-   Um den neuesten Quellcode zu kompilieren, siehe [Kompilieren](Compiling/de.md).

## Zusätzliche Module und Makros 

Die FreeCAD Gemeinschaft bietet viele zusätzliche Module und Makros. Seit 0.17 können sie einfach aus FreeCAD heraus mit dem [Addon Manager](Addon_Manager/de.md) installiert werden. <img alt="" src=images/AddonManager.svg  style="width:22px;">.



