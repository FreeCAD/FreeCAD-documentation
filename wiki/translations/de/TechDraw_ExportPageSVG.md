---
- GuiCommand:
   Name:TechDraw ExportPageSVG
   Name/de:TechDraw BlattExportierenSVG
   MenuLocation:TechDraw - Page - Seite als SVG-Datei exportieren
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Vorlagen](TechDraw_Templates/de.md), [Draft SVG](Draft_SVG/de.md)
---

# TechDraw ExportPageSVG/de



## Beschreibung

Das Werkzeug **TechDraw BlattExportierenSVG** speichert das aktuelle Zeichnungsblatt als [SVG](SVG/de.md)-Datei.



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ExportPageSVG.svg" width=16px> [Seite als SVG-Datei exportieren](TechDraw_ExportPageSVG/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Page  → <img src="images/TechDraw_ExportPageSVG.svg" width=16px> Seite als SVG-Datei exportieren** auswählen.
    -   Wenn ein Zeichnungsblatt im [Hauptansichtsbereich](Main_view_area/de.md) angezeigt wird: Mit der rechten Maustaste in das Fenster des Blattes klicken und im Kontextmenü die Option **Export SVG** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Das Dialogfenster **Seite als SVG-Datei exportieren** wird geöffnet.
5.  Einen Speicherort und einen Dateinamen auswählen.



## Hinweise

-   [TechDraw Schraffur](TechDraw_Hatch/de.md) Muster werden aufgrund einer Begrenzung in der SVG Unterstützung von Qt4 nicht nach [SVG](SVG/de.md) exportiert.
-   Textpositionen und -größen sind in der exportierten Datei nicht korrekt. Die Verwendung der \"System\" Standardschriftart in der Zeichnung verbessert das Größenproblem erheblich.



## Skripten


**Siehe auch:**

[TechDrawGui API](TechDrawGui_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das SpeichereSVG Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen benutzt werden:


```python
TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath)
```

Beachte, dass das FreeCADGui Modul aktiv sein muss, um diese Funktion nutzen zu können.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageSVG/de
