# FreeCAD and DXF Import/de
{{TOCright}}



## Hintergrund

DXF ist ein proprietäres CAD Datenformat für 2D Zeichnungen, das seinen Ursprung in AutoCAD hat. Weitere Details findest du auf der [DXF](DXF/de.md) Wiki Seite.



## Einführung

Seit FreeCAD Version 0.18 gibt es einen neuen C++ DXF Importeur, und seit Version 0.19 auch einen neuen C++ DXF Exporteur. Diese neuen Komponenten werden mit FreeCAD installiert.

Um den älteren, veralteten DXF Importeur und -Exporteur zu verwenden, musst du mehrere Dateien installieren. Diese Dateien können nicht in FreeCAD enthalten sein, da sie Bibliotheken verwenden, die unter einer Lizenz veröffentlicht wurden, die nicht mit FreeCAD kompatibel ist.



## Wie den alten DXF Importeur und -Exporteur installieren 



### Automatisch

Wenn die Dateien noch nicht installiert sind, gehe in das Menü **Bearbeiten → Voreinstellungen → Import-Export → DXF** und aktiviere die Option **FreeCAD erlauben, die DXF Bibliotheken automatisch herunterzuladen und zu aktualisieren**, damit FreeCAD sie automatisch herunterlädt und installiert.

Für FreeCAD 0.14 oder älter muss es manuell installieren werden:



### Manuell

1.  Gehe zu [Yoriks Github Konto](https://github.com/yorikvanhavre/Draft-dxf-importer) und lade diese Dateien herunter (auf der rechten Seite kannst Du \"Als ZIP herunterladen\" wählen).
2.  Lege die Dateien in Deinen Makro Ordner.
3.  Wenn du unsicher bist, wo dieser Ordner ist, gehe zu **Bearbeiten → Einstellungen → Allgemein → Makro** und überprüfe das Feld namens **Makropfad**.

-   Unter Ubuntu ist dein Makro Ordner normalerweise (der Ordner ist ausgeblendet, du musst ihn eventuell wieder einblenden):

/home/dein_Benutzername/.FreeCAD 

-   Unter Windows ist dein Makro Ordner normalerweise unter:

C:\Benutzer\dein_Benutzername\AppData\Roaming\FreeCAD

Siehe auch: [Dxf Einrichtung Importeur](Dxf_Importer_Install/de.md)



## Tips und Tricks 

Manchmal lassen sich DXF Dateien nicht importieren, obwohl sie sich in anderen CAD Programmen problemlos öffnen lassen.

Du kannst versuchen:

1.  Gehe zu **Bearbeiten → Einstellungen → Import-Export → DXF** und deaktiviere die Option **Geometrie vereinen** und versuche es erneut.
2.  Denke daran, dass du jetzt vielleicht keine deckungsgleichen Endpunkte haben wirst. Du kannst sie dann selbst mit [Sketcher SkizzeÜberprüfen](Sketcher_ValidateSketch/de.md) deckungsgleich festlegen.

Du kannst auch versuchen:

1.  Gehe zu **Bearbeiten → Einstellungen → Entwurf → Allgemeine Einstellungen** und stelle den Wert von **Toleranz** (Standard: 0,05) ein und versuche es erneut.

Für eine Übersicht über alle DXF bezogenen Voreinstellungen siehe [Import Export Einstellungen](Import_Export_Preferences/de#DXF.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DXF Import/de
