# Download/de
## Aktuelle stabile Version 

Die Version 0.21.2 von FreeCAD wurde am 14.11.2023 veröffentlicht. Um herauszufinden, was es Neues gibt, sIehe die [Veröffentlichungshinweise](Release_notes_0.21/de.md).

SHA256-Prüfsummen zur Überprüfung der Integrität eines Downloads findet man auf der [0.21.2 Release-Page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.21.2).

Frühere Versionen können von der Seite der veröffentlichten [Versionen](https://github.com/FreeCAD/FreeCAD/releases) heruntergeladen werden.

+::+::+::+
| ![](images/Windows.png )                                                                                                | ![](images/Mac.png )                                                                                                | ![](images/Linux_with_text.png )                                                                        |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [Install instructions](Installing_on_Windows.md)                                                                      | [Install instructions](Installing_on_Mac.md)                                                                  | [Install instructions](Installing_on_Linux.md)                                                                |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-WIN-x64-installer-1.exe)        | [ARM (M1/M2) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-arm64.dmg)  | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-x86_64.AppImage)   |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Windows-x86_64.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-intel-x86_64.dmg) | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-aarch64.AppImage) |
++++



### Hinweise für Windows-Anwender 

-   Die folgenden Windows Versionen werden unterstützt: 64-bit 7/8/10/11. 32-bit-Windows wird nicht unterstützt.
-   Das Paket kann auch vom [Chocolatey](https://chocolatey.org/packages/freecad)-Manager installiert werden. Das Chocolatey-Paket ist zurzeit nicht auf dem neuesten Stand



### Hinweise für macOS-Anwender 

-   MacOS 10.12 Sierra ist die älteste unterstützte Version.
-   Für macOS 12 und älter sollte das \"Unsignierte Intel disk image\" verwendet werden, da die signierte Version auf diesen Systemen nicht funktioniert.



### Hinweise für GNU/Linux-Anwender 

Die meisten Distributionen führen FreeCAD in ihren offiziellen Repositorien, aber wenn die Distribution nicht einem rollierenden Veröffentlichungs Modell folgt, kann die von ihnen bereitgestellte Version veraltet sein. Stattdessen kannst Du das AppImage oben herunterladen, als ausführbar markieren und ohne Installation starten.

Bitte schau auf der Seite [Installation unter Linux](Installing_on_Linux/de.md) nach weiteren Installationsoptionen, einschließlich täglicher Pakete für Ubuntu und Derivaten.

Eine portable Version, welche keine Installation benötigt, kann durch Starten von FreeCad mit diesen Befehlen erreicht werden:


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Weitere Informationen über die Umgebungsvariablen von FreeCAD können auf der [Konfigurationsseite](Start_up_and_Configuration/de#Environment_variables.md) gefunden werden.



## Entwicklungsversionen

Die Entwicklung von FreeCAD ist aktiv.

-   Für Entwicklungs-Builds und Entwicklungsquellcode siehe die Seite [Weekly-Builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).
-   Um den neuesten Quellcode zu kompilieren, siehe die Seite [Kompilieren](Compiling/de.md).



## Zusätzliche Module und Makros 

Die FreeCAD Gemeinschaft bietet viele zusätzliche Module und Makros. Seit 0.17 können sie einfach aus FreeCAD heraus mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr.md) installiert werden.



---
⏵ [documentation index](../README.md) > Download/de
