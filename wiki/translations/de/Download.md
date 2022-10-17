# Download/de
{{TOCright}}

## Aktuelle stabile Version 


<div class="mw-translate-fuzzy">

Die Version 0.20 von FreeCAD (29177) wurde am 14.06.2022 veröffentlicht. Um herauszufinden, was es Neues gibt, sIehe die [Veröffentlichungshinweise](Release_notes_0.20/de.md).

Die erste Version 0.19.2 von FreeCAD (24291) wurde am 22.04.2021 veröffentlicht. Um herauszufinden, was es Neues gibt, lese bitte die [Veröffentlichungshinweise](Release_notes_0.19/de.md).


</div>


<div class="mw-translate-fuzzy">

SHA256 Prüfsummen zur Überprüfung der Integrität eines Downloads kann man auf der [0.20 Release-Page](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.20).


</div>

Frühere Versionen können von der Seite der veröffentlichten [Versionen](https   *//github.com/FreeCAD/FreeCAD/releases) heruntergeladen werden.

+   *   *+   *   *+   *   *+
| ![](images/Windows.png )                                                                                         | ![](images/Mac.png )                                                                                                             | ![](images/Linux_with_text.png )     |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                 | [Install on Mac](Installing_on_Mac.md)                                                                                     | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [64-bit installer](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20.1/FreeCAD-0.20.1-WIN-x64-installer-1.exe) | [macOS 64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20.1/FreeCAD_0.20-1-2022-08-20-conda-macOS-x86_64-py310.dmg) | [AppImage 64-bit](AppImage.md)             |
++++

### Hinweise für Windowsbenutzer 

-   Die folgenden Windows Versionen werden unterstützt   * 64-bit 7/8/10/11. 32-bit-Windows wird nicht unterstützt.
-   Eine portable Version, die keine Installation benötigt, steht unter [Veröffentlichungen](https   *//github.com/FreeCAD/FreeCAD/releases/) zur Verfügung.
-   Das Paket kann auch vom [Chocolatey](https   *//chocolatey.org/packages/freecad)-Manager installiert werden.

### Hinweise für Mac OS X Benutzer 

Mac OS X 10.12 Sierra ist die minimal unterstützte Version.

### Hinweise für GNU/Linux Anwender 

Die meisten Distributionen führen FreeCAD in ihren offiziellen Repositorien, aber wenn die Distribution nicht einem rollierenden Veröffentlichungs Modell folgt, kann die von ihnen bereitgestellte Version veraltet sein. Stattdessen kannst Du das AppImage oben herunterladen, als ausführbar markieren und ohne Installation starten.

Bitte schau auf der Seite [Installation unter Linux](Installing_on_Linux/de.md) nach weiteren Installationsoptionen, einschließlich täglicher Pakete für Ubuntu und Derivaten.


<div class="mw-translate-fuzzy">

Eine portable Version, welche keine Installation benötigt, kann durch Starten von FreeCad mit diesen Befehlen erreicht werden   * {{Version/de|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD-0.20.0-Linux-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD-0.20.0-Linux-x86_64.AppImage
```


</div>


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Weitere Informationen über die Umgebungsvariablen von FreeCAD können auf der [Konfigurationsseite](Start_up_and_Configuration/de#Environment_variables.md) gefunden werden.

## Entwicklungsversionen

Die Entwicklung von FreeCAD ist aktiv.

-   Für Linux Anwender probiere die Entwicklung [AppImage](AppImage/de.md) aus.
-   Für MacOS und Windows Entwicklungsbuilds und Entwicklungsquellcode siehe die [weekly builds](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds) Seite.
-   Um den neuesten Quellcode zu kompilieren, siehe [Kompilieren](Compiling/de.md).

## Zusätzliche Module und Makros 

Die FreeCAD Gemeinschaft bietet viele zusätzliche Module und Makros. Seit 0.17 können sie einfach aus FreeCAD heraus mit dem [Addon-Manager](Std_AddonMgr/de.md) installiert werden <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;">.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/de
