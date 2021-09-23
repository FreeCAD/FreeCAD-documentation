# PCB Workbench/de


## Einführung


{{TOCright}}

Arbeitsbereich [Gedruckte Leiterplatte](https://de.wikipedia.org/wiki/Leiterplatte) für FreeCAD (englisch.: Printed Circuit Board)(PCB)

Arbeitsbereich Flexible Gedruckte Leiterplatte für FreeCAD (FPCB)

Mit dem Modul kannst Du Leiterplatten in FreeCAD importieren/erstellen. Umfang des Moduls:

-   Unterstützung für viele verschiedene Schichten,
-   Möglichkeit, Farben, Transparenz und Namen für jede Schicht zu wählen,
-   Modul ermöglicht den Import von IGES/STP Modellen mit Farben,
-   Möglichkeit, Löcher/Durchkontaktierungen unabhängig darzustellen.

## Referenzen

-   Autor: marmni
-   Hauptseite: <https://sourceforge.net/projects/eaglepcb2freecad/>
-   Quellcode auf github: <https://github.com/marmni/FreeCAD-PCB>

## Werkzeuge

Für eine detaillierte Beschreibung der Arbeitsbereichsnutzung siehe **index.pdf** im Quellcode oder [Handbuch](https://raw.githubusercontent.com/marmni/FreeCAD-PCB/master/index.pdf)

Werkzeugleiste

![](images/PCB-menu-orizz.png )

Aufklappmenü

![](images/PCB-export-BOM.png ) ![](images/PCB-export-hole.png ) ![](images/PCB-create-new.png ) ![](images/PCB-explode.png ) ![](images/PCB-bounding-box.png )

## Einrichtung

### Automatische Einrichtung 

Dieser Arbeitsbereich kann über den [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert werden.

### Von GitHub 

**Voraussetzungen**

FreeCAD-PCB benötigt FreeCAD in der Version 0.18 oder höher und Python in der Version 2.7 oder höher.

**Linux-Installationsanweisungen** (von GitHub)

Entpacke die heruntergeladene Zip Datei und kopiere den extrahierten Ordner in das Verzeichnis, in dem FreeCAD installiert ist (Unterordner Mod).

Beispiel:

-   FreeCAD Pfad:

~/Programs/FreeCAD

-   Kopiere also Mod in den Ordner

~/Programs/FreeCAD/Mod

-   Du kannst Dateien auch in den Ordner kopieren

~/.FreeCAD/Mod 

-   Ändere anschließend die Lese-/Schreibberechtigung auf 777. Bitte vergiß nicht den Parameter -R!

Beispiel:

chmod 777 -R PCB

**Windows Installationsanweisungen** (von GitHub)

Entpacke die heruntergeladene Zip Datei und kopiere den extrahierten Ordner in das Verzeichnis, in dem FreeCAD installiert ist (Unterordner Mod).

Beispiel:

-   FreeCAD Pfad:

C:/Programme/FreeCAD-0.18

-   So kopiere mod in den Ordner

C:/Programme/FreeCAD-0.18/Mod

-   Als nächstes ändere die Lese-/Schreibrechte für alle Benutzer. Klicke mit der rechten Maustaste auf den Ordner PCB und wähle Eigenschaften → Sicherheit → Bearbeiten → Benutzer und Markierung.

Sicherheit → Bearbeiten → Benutzer und markiere alle Kontrollkästchen unter der Option \'Zulassen\'.

**MacOS Installationsanweisungen** (von GitHub)

## Verweise zum FreeCAD-PCB Arbeitsbereich 

-   Arbeitsbereich Wiki: [Externe Arbeitsbereiche](https://wiki.freecadweb.org/External_workbenches/de)
-   FreeCAD Wiki: [Wiki Hauptseite](https://wiki.freecadweb.org/Main_Page/de)
-   FreeCAD Forum: [EaglePCB Importeur für FreeCAD](http://forum.freecadweb.org/viewtopic.php?f=9&t=5107)
-   Tutorien:
-   Videos: [EaglePCB\_2\_FreeCAD - FreeCAD odczyt plików brd z programu Eagle](https://www.youtube.com/watch?v=81NsljRJx8c&feature=youtu.be)
-   Dateien: [PCB Bibliothek](https://github.com/marmni/FreeCAD-PCB-library)
-   Fehler melden: Bitte melde Fehler unter <https://github.com/marmni/FreeCAD-PCB/issues>

## Andere nützliche Verweise 

-   [EaglePCB auf sourceforge](https://sourceforge.net/projects/eaglepcb2freecad/)
-   [Makrorezepte](Macros_recipes/de.md)
-   [FreeCAD Herunterladen](Download/de.md)
-   [FreeCAD Gemeinschaft Portal](FreeCAD_Community_Portal/de.md)



[Category:Sandbox](Category:Sandbox.md) [Category:User Documentation](Category:User_Documentation.md) [Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)
