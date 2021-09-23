---
- GuiCommand:/de
   Name:TechDraw ExportPageDXF
   Name/de:TechDraw ExportSeiteDXF
   MenuLocation:TechDraw → Exportiere Seite als DXF
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.18
   SeeAlso:[TechDraw Exportiere Seite als SVG](TechDraw_ExportPageSVG/de.md), [Entwurf DXF](Draft_DXF/de.md)
---

# TechDraw ExportPageDXF/de

## Beschreibung

Das ExportSeiteDXF Werkzeug speichert eine Zeichnungsseite als [DXF](DXF/de.md) Datei.

## Anwendung

1.  Wähle eine Seite in der Baumansicht, wenn das Dokument mehrere Seiten enthält.
2.  Drücke die **<img src="images/TechDraw_ExportPageDXF.svg" width=16px> [Exportiere Seite als DXF](TechDraw_ExportPageDXF/de.md)** Schaltfläche.
3.  Wähle einen Speicherort und einen Dateinamen.

### Begrenzungen

-   Radien und Durchmesserbemaßungen werden nur dann korrekt exportiert, wenn sie \"innerhalb\" des Bogens liegen.
-   Skalierung wird nicht unterstützt. Das DXF wird in der tatsächlichen Größe der TechDraw Seite gezeichnet.
-   Einheiten werden nicht unterstützt. Das DXF wird in Millimetern (mm) gezeichnet. Bemaßungstext wird genau wie in TechDraw angezeigt.
-   TechDraw kann keine [Einfügen eines Entwurf Arbeitsbereichsobjekts ](TechDraw_DraftView/de.md) oder ein [Einfügen eines Arch Arbeitsbereichsobjekt](TechDraw_ArchView.md) zu DXF exportieren. Diese Ansichten sind [SVG](SVG/de.md) Elemente, die intern vom [Entwurf Arbeitsbereich](Draft_Workbench/de.md) generiert werden, so dass es keine geometrische Form zum Exportieren gibt. Um eine Ansicht als DXF zu exportieren, muss sie mit [Ansicht einfügen](TechDraw_View/de.md) oder [Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md) erstellt worden sein. Wähle z. B. eine [Arch SchnittEbene](Arch_SectionPlane/de.md), dann verwende [Entwurf Form2DAnsicht](Draft_Shape2DView/de.md) um eine flache Projektionsform zu erstellen, und verwende dann [Ansicht einfügen](TechDraw_View/de.md) für dieses Objekt. Alternativ wähle die Objekte in der Baumansicht oder im 3D Ansichtsfenster aus und exportiere sie mit **Datei → [Export](Std_Export/de.md)**.
-   Der Titelblock einer Seite ist ebenfalls eine [SVG](SVG/de.md) Vorlage, daher wird er auch nicht nach DXF exportiert.
-   Im Allgemeinen kann TechDraw nur die Elemente nach DXF exportieren, die von der `Import::ImpExpDxfWrite` Klasse des [Import Moduls](Import_Module/de.md).

## Hinweise

-   Diese Funktion exportiert die Versionen R12 (AC1009) und R14 (AC1014) von [DXF](DXF/de.md).
    -   R12 ist eine ältere, einfachere Version des Standards, sollte aber für die meisten anderen Programme lesbar sein.
    -   R14 ist die Standardversion. Sie enthält unter anderem Unterstützung für Splines und Ellipsen.
-   Diese Parameter beeinflussen die Ausgabe:
    -   
        **Werkzeuge → Parameter Berabeiten → BasisApp/Einstellungen/Mod/Import → DxfVersionOut**
        
        . Dies ist ein ganzzahliger Wert. Gültige Einträge sind 12 oder 14. Der Standardwert ist 14.

    -   
        **Werkzeuge → Parameter Berabeiten → BasisApp/Einstellungen/Mod/Import → DiscretizeEllipses**
        
        . Dies ist ein boolescher Wert. Wenn `True`, werden Splines und Ellipsen in Polylinien umgewandelt; wenn `False`, werden Splines und Ellipsen als Splines- und Ellipsenobjekte geschrieben. Die Vorgabe ist `False`. Wenn der Parameter DxfVersionOut 12 ist, werden Splines und Ellipsen immer in Polylinien konvertiert.

    -   
        **Werkzeuge → Parameter Berabeiten → BasisApp/Einstellungen/Mod/Import → maxsegmentlength**
        
        . Dies ist ein Gleitkommawert. Wenn Splines und Ellipsen in Polylinien umgewandelt werden, bestimmt dieser Parameter die Segmentlänge.

## Skripten


**Siehe auch:**

[TechDrawGui API](TechDrawGui_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das SpeichereDXF Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen benutzt werden:


```python
TechDraw.writeDXFPage(page,filename)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageDXF/de
