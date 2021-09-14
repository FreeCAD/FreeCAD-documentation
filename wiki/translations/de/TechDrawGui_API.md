# TechDrawGui API/de

 {{VeryImportantMessage|(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation].}} Diese Funktionen sind Teil des [TechDraw-Arbeitsbereichs](TechDraw_Workbench/de.md) und können in [Makros](macros/de.md) oder mit dem [Python](Python/de.md)-Interpreter verwendet werden, sobald das TechDrawGui importiert wurde.

Siehe die [TechDraw API](TechDraw_API/de.md) für weitere Funktionen.

Beispiel: 
```python
import FreeCAD
import TechDrawGui

p = FreeCAD.ActiveDocument.Page

f = "/home/localuser/myPdfDirectory/savePage.pdf"
TechDrawGui.exportPageAsPdf(p, f)

f = "/home/localuser/mySvgDirectory/savePage.svg"
TechDrawGui.exportPageAsSvg(p, f)
```


{{APIFunction|exportPageAsPdf|pageObject, filePath|eine Kopie des pageObject im PDF Format im Speicherort filePath speichern|none}}


{{APIFunction|exportPageAsSvg|pageObject, filePath|eine Kopie des pageObject im SVG Format im Speicherort filePath speichern|none}}


{{APIFunction|copyActiveViewToSvgFile|document, filePath, (options)|eine Kopie der aktiven Ansicht für "document" in der Datei "filePath" speichern|double (estimated scale)}}

Optionen:

-   width - float - Breite des erzeugten svg in mm
-   height - float - Höhe des erzeugten svg in mm
-   paintBackground - bool - Hintergrund malen/nicht malen
-   backgroundColor - tuple - (r,g,b,a)
-   lineWidth - float - Linienstärke
-   border - float - Leerraum um Bild
-   mode - int - Rendermodus (AS\_IS, WIREFRAME, POINTS, WIREFRAME\_OVERLAY, HIDDEN\_LINE, BOUNDING\_BOX)

{{APIFunction|addQGIToView|view, QGraphicsItem|Hinzufügen eines QGraphicsItems (erstellt mit PySide) zu einer Ansicht|none}}


{{TechDraw Tools navi

}}  

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
