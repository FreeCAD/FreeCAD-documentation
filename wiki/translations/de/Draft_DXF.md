








{{TOCright}}

## Beschreibung

DXF Entwurf ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Öffnen](Std_Open/de.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import/de.md) und <img alt="" src=images/Std_Export.svg  style="width:24px;">[Std Export](Std_Export/de.md) Befehlen verwendet wird, um das DXF Dateiformat handzuhaben.

![](images/Screenshot_qcad.jpg ) *Qcad-Zeichnung nach DXF exportiert, die anschließend in FreeCAD geöffnet wird*

## Importieren

Der Importeur hat zwei Modi, einstellbar unter **Bearbeiten → Einstellungen → Import/Export → DXF**: Der eine ist eingebaut, C++ basiert und schnell, der andere ist eine Altlast, in Python kodiert, langsamer und erfordert die Installation einer Erweiterung, kann aber manche Objekte besser handhaben und kann verfeinerte FreeCAD Objekte erzeugen. Beide unterstützen alle DXF Versionen beginnend ab R12.

3D Objekte innerhalb einer DXF Datei werden unter einem binären ACIS/SAT Klecks gespeichert, der zur Zeit von FreeCAD nicht gelesen werden kann. Einfachere Objekte wie 3DFACEs werden jedoch unterstützt.

Die folgenden DXF Objekte können importiert werden:

-   Linien
-   Polylinien und Lwpolylinien
-   Kreise
-   Bögen
-   Lagen
-   Texte und Mtexte
-   Bemaßungen
-   Blöcke (nur Geometrie, Texte, Bemaßungen und Attribute innerhalb von Blöcken werden übersprungen)
-   Punkte
-   Führungen
-   Papierraumobjekte

## Exportieren

Dateien werden im R14 DXF Format exportiert, das von vielen Anwendungen verarbeitet werden kann.

Die folgenden FreeCAD Objekte können exportiert werden:

-   die gesamte 2D Geometrie von FreeCAD, wie z. B. Entwurfsobjekte oder Skizzen
-   3D Objekte werden als verflachte 2D Ansicht exportiert
-   Zusammengesetzte Objekte werden als Blöcke exportiert
-   Texte
-   Farben werden von den RGB Farben der Objekte auf den Autocad Farbindex (ACI) abgebildet. Schwarz wird immer \"nach Lagen\" sein
-   Lagen werden von Gruppennamen abgebildet. Wenn Gruppen verschachtelt sind, gibt die tiefste Gruppe den Lagennamen an.
-   Bemaßungen, die mit dem Dimstyle \"Standard\" exportiert werden.

## Installieren

Aus lizenzrechtlichen Gründen sind die benötigten [DXF](DXF/de.md) Import/Export Bibliotheken, die von der Legacy Version des Importeurs benötigt werden, nicht Teil des FreeCAD Quellcodes. Für weitere Informationen siehe: [FreeCAD und DXF Import](FreeCAD_and_DXF_Import/de.md).

## Einstellungen

Für weitere Informationen siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Elemente können durch die folgende Funktion nach DXF exportiert werden: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Beispiel: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```





 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
