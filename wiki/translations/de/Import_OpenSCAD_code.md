


{{TutorialInfo/de
|Topic=OpenSCAD Code importieren
|Level=Anfänger
|Time= 30 Minuten
|Author=r-frank
|FCVersion=0.16.6704
|Files=
}}

## Einführung

OpenSCAD ist, wie FreeCAD, ein quelloffenes 3D CAD Programm. Während FreeCAD einen visuellen Ansatz verwendet, nutzt OpenSCAD eine Programmierschnittstelle, um die 3D Operationen durchzuführen. Der OpenSCAD Arbeitsbereich kann verwendet werden, um OpenSCAD Objektcode zu importieren und um Zugang zu einigen der mit OpenSCAD möglichen Netzoperationen zu erhalten.

## Installation von OpenSCAD {#installation_von_openscad}

-   Linux Anwender können aus den entsprechenden Distributions Repositorien wie Debian, openSUSE, Mint, Unbuntu usw. oder von der [OpenSCAD Heimseite](http://www.openscad.org/) installieren.
-   Mac Anwender können die Binärdateien von der [OpenSCAD Homepage](http://www.openscad.org/) herunterladen.
-   Windows Anwender können das Programm von der [OpenSCAD Heimseite](http://www.openscad.org/) herunterladen.

Da nur die ausführbare OpenSCAD Datei von FreeCAD benötigt wird, können Windows Anwender die portable Version installieren, wenn sie möchten.

## Konfigurieren des OpenSCAD Arbeitsbereichs in FreeCAD {#konfigurieren_des_openscad_arbeitsbereichs_in_freecad}

-   Öffne FreeCAD
-   Wechsle zum [OpenSCAD-Arbeitsbereich](OpenSCAD_Workbench/de.md)
-   Wähle Bearbeiten → Einstellungen → OpenSCAD aus dem Hauptmenü
    -   Verweise FreeCAD auf die ausführbare OpenSCAD-Datei (Abschnitt: Allgemeine OpenSCAD-Einstellungen)
    -   alle anderen Werte auf der Einstellungsseite können auf den Standardwerten belassen werden

## Das Beispielmodell {#das_beispielmodell}

Hier verwenden wir die example005.scad Datei aus den (alten) OpenSCAD Beispielen, aber Du kannst auch jede andere scad Datei benutzen.
<img alt="" src=images/TutorialOpenSCAD_SampleFile.jpg  style="width:800px;">

<img alt="" src=images/TutorialOpenSCAD_SampleFile.jpg  style="width:800px;">

## Importieren des Modells in FreeCAD {#importieren_des_modells_in_freecad}

-   In FreeCAD wähle einfach **Datei** → **Öffnen** und wähle die .scad Datei, die du importieren möchtest.
-   Es ist nicht wichtig, welcher Arbeitsbereich aktiviert ist, der OpenSCAD Arbeitsbereich selbst wird nur benötigt, wenn du spezielle Funktionen auf dein Modell anwendest.
-   FreeCAD importiert die OpenSCAD Datei und baut einen Baum mit Grundkörpern und booleschen Operationen auf.
-   Tutorial beendet

<img alt="" src=images/TutorialOpenSCAD_ImportFile.jpg  style="width:800px;">

<img alt="" src=images/TutorialOpenSCAD_ImportFile.jpg  style="width:800px;">

## Verwandtes

-   [FreeCAD Wie Importieren Exportieren](FreeCAD_Howto_Import_Export/de.md)
-   [Import Export Einstellungen](Import_Export_Preferences/de.md)

[Category:OpenSCAD{{\#translation:}}](Category:OpenSCAD.md)
