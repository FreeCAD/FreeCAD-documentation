# DXF/de
{{TOCright}}

## Hintergrundgeschichte

Das Drawing Exchange Format (DXF) ist ein proprietäres CAD Datenformat, das von Autodesk entwickelt wurde, um den Dateiaustausch zwischen dem Flaggschiffprodukt AutoCAD und anderer Software zu ermöglichen. Es gibt eine Reihe von guten Softwarebibliotheken zum Lesen/Schreiben des DXF Formats.

Es gibt viele Versionen des DXF Formats. Du wirst von bestimmten Schlüsselversionen hören, wie z. B. R12 (von 1992) oder R14 (von 1997, die Splines hatte). Spätere Versionen von DXF haben 3D Elemente, aber diese werden nur selten verwendet oder implementiert. Wie du DXF nutzt, um CAD Daten zwischen Programmen auszutauschen, hängt hauptsächlich von den Begrenzungen und Fehlern in den entsprechenden Lesern/Importeuren und Schreibern/Exporteuren ab. Diese sind selten vollständig dokumentiert und können eine große Quelle der Frustration sein.

Wenn du DXF Dateien bearbeitest und möchtest, dass sie beim Speichern nahezu unverändert bleiben, empfehlen wir dir die Programme [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) oder [QCad](https://en.wikipedia.org/wiki/QCad), da die internen Datenstrukturen dieser Programme mit den Objekten in der DXF Datei kompatibel sind.

In FreeCAD müssen die DXF Leser die Geometrie (z. B. Spline Formen) aus der DXF Datei in die spezifischen internen Darstellungen des Arbeitsbereichs übersetzen.

## Methoden zum Importieren von DXF in FreeCAD 

Wenn Du die Einstellungen häufig überprüfen willst, empfehlen wir, in **Bearbeiten → Einstellungen → Import-Export → DXF** das Kästchen \"\[ \] Diesen Dialog beim importieren und exportieren anzeigen\" zu aktivieren.

Mehr Informationen gibt es auf den Seiten [Draft DXF](Draft_DXF/de.md) und [FreeCAD und DXF Import](FreeCAD_and_DXF_Import/de.md).

Wenn Du die importierte Geometrie nutzen willst, um 3D-Formen im PartDesign-Arbeitsbereich zu erstellen, dann versuche [Skizzierer überprüfen](Sketcher_ValidateSketch/de.md), nachdem Du DXF in eine Skizze importiert hast.

### C++ DXF Importeur 

Diese Implementation ist schnell, überspringt aber Merkmale, die nicht erkannt werden, wie etwa DXF-Splines. Es kann außerdem nur Geometrien als einzelne Einträge im Modellbaum in den Draft-Arbeitsbereich importieren. Diese können die Farben aus der Datei importieren, wenn diese Option aktiviert ist. Weitere Informationen gibt es im (engl.) [Forumseintrag](https://forum.freecadweb.org/viewtopic.php?f=3&t=32493).

### Python DXF Importeur 

Dieser Importer muss vor der Verwendung heruntergeladen und installiert werden. Siehe [Dxf Importer-Installation](Dxf_Importer_Install/de.md) oder benutze die Option \"\[ \] FreeCAD das automatische Herunterladen und Aktualisieren der DXF-Bibliotheken erlauben\" (in **Bearbeiten → Einstellungen → Import/Export → DXF**).

Dieser Importeur hat mehr Funktionen (wie das Importieren von Splines) und hat die Option zum Laden der DXF Formen in den Skizzierer. Sei jedoch gewarnt, dass alle Elemente der Skizze ein weiteres Mal einzeln im Modellbaum erscheinen, was verwirrend sein kann. Du kannst all diese einzelnen Objekte löschen und die einzelne Skizze beibehalten (die als zweiter Eintrag in der Liste der neuen Elemente erscheint).

Unglücklicherweise implementiert der Arbeitsbereich Skizze keine Farben, so dass alle Geometrien auf einer Ebene erscheinen, was zum Problem wird, wenn die Datei viele Konstruktionslinien enthält. Eine Umgehungslösung besteht darin, die Datei in LibreCAD zu öffnen und all die Geometrien zu löschen, die nicht erscheinen sollen, so dass eine Datei gespeichert wird, die genau die Geometrien enthält, die Du laden möchtest.

### Makros

Hab\' ein Auge auf das FreeCAD Forum oder die [Makro Rezepte](Macros_recipes/de.md), um alternative Ausführungen von DXF Import und Aufräumroutinen kennenzulernen, während sie entwickelt werden.

## DXF speichern 

Zusätzlich zu den Optionen unter Bearbeiten → Voreinstellungen kann der [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) auch Zeichnungsseiten mit der Funktion [TechDraw ExportSeiteDXF](TechDraw_ExportPageDXF/de.md) nach DXF exportieren.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Draft](Category_Draft.md) > [TechDraw](Category_TechDraw.md) > [File_Formats](Category_File_Formats.md) > DXF/de
