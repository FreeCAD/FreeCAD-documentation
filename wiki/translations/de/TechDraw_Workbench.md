# <img alt="TechDraw Arbeitsbereich Symbol" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/de

## Einführung

Der <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;">[TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) dient zur Erstellung grundlegender technischer Zeichnungen aus 3D-Modellen, die mit einem anderen Arbeitsbereich erstellt wurden, wie z.B. [Part](Part_Workbench/de.md)-, [PartDesign](PartDesign_Workbench/de.md)-, [Arch](Arch_Workbench/de.md)-Arbeitsbereich oder die aus anderen Anwendungen importiert wurden. Jede Zeichnung ist eine Seite, die verschiedene Ansichten von zeichnungsfähigen Objekten wie Part::Features, PartDesign::Bodies, App::Part groups und Document Object Groups enthalten kann. Die daraus entstandenen Zeichnungen können für Dinge wie Dokumentation, Fertigungsanweisungen, Verträge, Genehmigungen usw. verwendet werden.

Bemaßungen, Abschnitte, schraffierte Bereiche, Anmerkungen und Symbole im Dateiformat[SVG](SVG/de.md) können der Seite hinzugefügt werden. Die Seite / Zeichnung kann später in verschiedene Formate wie [DXF](DXF/de.md), [SVG](SVG/de.md) und [PDF](PDF/de.md) exportiert werden.

TechDraw wurde ab Version 0.17 offiziell in FreeCAD aufgenommen; es soll den nicht mehr unterstützten [Drawing-Arbeitsbereich](Drawing_Workbench/de.md) ersetzen. Beide Arbeitsbereiche sind in v0.17 noch vorhanden, aber der Drawing-Arbeitsbereich kann in zukünftigen Releases entfernt werden. Um mit den Plänen und Entwicklungen von TechDraw Schritt zu halten, besuchen Sie die [TechDraw-Planung](TechDraw_Roadmap/de.md).


<div class="mw-translate-fuzzy">

FreeCAD ist in erster Linie eine 3D-Modellierungsanwendung und verfügt daher nicht über viele 2D-Zeichenwerkzeuge, die in den Programmen [Draft](Draft_Workbench/de.md) und [Sketcher](Sketcher_Workbench/de.md) enthalten sind. Wenn Ihr Hauptziel die Erstellung komplexer 2D-Zeichnungen und [DXF](DXF/de.md)-Dateien ist und Sie keine 3D-Modellierung benötigen, können Sie ein spezielles Softwareprogramm für die technischen Zeichnungen in Betracht ziehen, wie z.B. [LibreCAD](https://de.wikipedia.org/wiki/LibreCAD), [QCad](https://de.wikipedia.org/wiki/QCad), TurboCad und andere.


</div>


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Seiten

Diese Werkzeuge sind zum Erstellen von Seiten.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Einfügen Standardseite](TechDraw_PageDefault/de.md): Fügt eine neue Seite mit der Standard [Vorlage](TechDraw_Templates.md) hinzu.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Seite mittels Vorlage einfügen](TechDraw_PageTemplate/de.md): Fügt eine neue Seite mit einer ausgewählten [Vorlage](TechDraw_Templates/de.md) hinzu, die nicht die Standardvorlage ist.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Seite neu zeichnen](TechDraw_RedrawPage/de.md): Erzwingt eine Aktualisierung der ausgewählten Seite. {{Version/de|0.19}}

## Ansichten

Dies sind Werkzeuge zum Erstellen von Ansichtsobjekten.

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Ansicht einfügen](TechDraw_View/de.md): Fügt eine ausgewählte Ansicht eines 3D-Objekts ein.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Aktive Ansicht einfügen](TechDraw_ActiveView/de.md): Fügt eine Ansicht des aktiven 3D-Fensters ein. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md): Ruft einen Dialog auf, um eine Projektionsansicht eines 3D-Objekts zu erstellen, aus der weitere Ansichten abgeleitet werden können (Seitenansicht, Draufsicht usw.).

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Schnittansicht einfügen](TechDraw_SectionView/de.md): Fügt eine Schnittsansicht einer vorhandenen Ansicht ein.

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Detailansicht einfügen](TechDraw_DetailView/de.md): Fügt eine Detailansicht eines Teils einer vorhandenen Ansicht ein.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Entwurf Arbeitsbereich Objekt einfügen](TechDraw_DraftView/de.md): Fügt eine Ansicht eines [Entwurf Arbeitsbereichs](Draft_Workbench/de.md)-Objekts ein.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Arch Arbeitsbereichsobjekt einfügen](TechDraw_ArchView/de.md): Fügt eine Ansicht eines [Arch Arbeitsbereichs](Arch_Workbench/de.md) [Schnittebenen](Arch_SectionPlane/de.md)-Objekts ein.

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Tabellenkalkulationsansicht einfügen](TechDraw_SpreadsheetView/de.md): Fügt die Ansicht eines [Tabellenkalkulation Arbeitsbereichsblatts](Spreadsheet_Workbench/de.md) hinzu.

## Ausschnittfenster

Dies sind Werkzeuge zum Erstellen und Verwalten von Ausschnittfenstern.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Clipgruppe einfügen](TechDraw_ClipGroup/de.md): Fügt eine Clipgruppe in eine Seite ein.

-   <img alt="" src=images/techdraw-clipplus.svg  style="width:32px;"> [Ausschnittfenster hinzufügen](TechDraw_ClipPlus/de.md): Fügt eine vorhandene Ansicht zu einer Gruppe von Ausschnittfenstern hinzu.

-   <img alt="" src=images/techdraw-clipminus.svg  style="width:32px;"> [Ausschnittfenster entfernen](TechDraw_ClipMinus/de.md): Entfernt eine Ansicht aus einer Gruppe von Ausschnittfenstern.

## Bemaßungen

Dies sind Werkzeuge für die Erstellung und Arbeit mit Bemaßungs-Objekten.

Lineare Bemaßungen können auf zwei Punkten, auf einer Linie oder auf zwei Linien basieren.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Length.svg  style="width:32px;"> [Längenbemaßung einfügen](TechDraw_Dimension_Length/de.md): Fügt eine Längenbemaßung hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Horizontal.svg  style="width:32px;"> [Eine horizontale Abstands-Bemaßung einfügen](TechDraw_Dimension_Horizontal/de.md): Fügt eine horizontale Längenbemaßung hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Vertical.svg  style="width:32px;"> [Eine vertikale Abstands-Bemaßung einfügen](TechDraw_Dimension_Vertical/de.md): Fügt eine vertikale Längenbemaßung hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Radius.svg  style="width:32px;"> [Einen Radius der gewählten Ansicht bemaßen](TechDraw_Dimension_Radius/de.md): Fügt eine Radiusbemaßung zu einem Kreis oder Kreisbogen hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Diameter.svg  style="width:32px;"> [Ein neues Durchmessermaß in die gewählte Ansicht einfügen](TechDraw_Dimension_Diameter/de.md): Fügt eine Durchmesserbemaßung zu einem Kreis oder Kreisbogen hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Angle.svg  style="width:32px;"> [Winkel bemaßen](TechDraw_Dimension_Angle/de.md): Fügt eine Winkelbemaßung zwischen zwei geraden Linienkanten hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Angle3Pt.svg  style="width:32px;"> [Winkelbemaßung mittels 3 Eckpunkten](TechDraw_Dimension_Angle3Pt/de.md): Fügt eine Winkelbemaßung mittels drei Eckpunkten hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Horizontal_Extent.svg  style="width:32px;"> [Neue horizontale Ausdehnung](TechDraw_Dimension_Horizontal_Extent/de.md): fügt eine horizontale Ausdehnungsbemaßung hinzu. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Vertical_Extent.svg  style="width:32px;"> [Neue vertikale Ausdehnung](TechDraw_Dimension_Vertical_Extent/de.md): fügt eine vertikale Ausdehnungsbemaßung hinzu. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Link.svg  style="width:32px;"> [Eine Abmessung mit einer 3D-Geometrie verlinken](TechDraw_Dimension_Link/de.md): Eine oder mehrere Bemaßungen mit einer 3D-Geometrie verlinken.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [New Balloon](TechDraw_Balloon/de.md): fügt einer Zeichnung eine \"Ballon\"-Anmerkung für Positionsnummern (z.B. für Stücklisten) hinzu. {{Version/de|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Dimension_Landmark.svg  style="width:32px;"> [Neue Leitbemaßung](TechDraw_Dimension_Landmark/de.md): fügt eine Leitbemaßung hinzu. <small>(v0.19)</small> 


</div>

## Ausgestaltung

Dies sind Werkzeuge zur Ausgestaltung von Seiten oder Ansichten:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Schraffierte Fläche unter Verwendung einer Bilddatei](TechDraw_Hatch/de.md): wendet ein Schraffurmuster aus einer Datei auf eine Fläche an.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Geometrische Schraffur auf Fläche anwenden](TechDraw_GeometricHatch/de.md): wendet ein Schraffurmuster unter Verwendung einer Autodesk PAT Spezifikation auf eine Fläche an.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [SVG Symbol einfügen](TechDraw_Symbol/de.md): fügt ein Symbol aus einer [SVG](SVG.md) Datei in eine Seite ein.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Bitmap Bild einfügen](TechDraw_Image/de.md): fügt ein PNG oder JPG [Bitmap](bitmap/de.md) Bild in eine Seite ein.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Ansichtsrahmen drehen On/Off](TechDraw_ToggleFrame/de.md): schaltet Rahmen und Beschriftungen, die eine Ansicht umgeben, an/aus.

## Anmerkung

Die Anmerkungswerkzeuge dienen dazu, eine Zeichnung mit zusätzlichen Informationen zu \"markieren\".

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Anmerkung einfügen](TechDraw_Annotation/de.md): fügt einen reinen Textblock als Anmerkung hinzu.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Führungslinie zur Ansicht hinzufügen](TechDraw_LeaderLine/de.md): fügt einer Ansicht eine Führungslinie hinzu. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Formatierte Text Anmerkung einfügen](TechDraw_RichTextAnnotation/de.md): fügt einen Formatierten Text Block als Anmerkung zu einer Führungslinie oder einer Ansicht hinzu. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Kosmetischen Knoten Hinzufügen](TechDraw_CosmeticVertex/de.md): fügt einen Knoten hinzu, der nicht Teil der Quellgeometrie ist. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Mittenpunktknoten hinzufügen](TechDraw_Midpoints/de.md): fügt kosmetische Knoten an den Mittenpunkten der ausgewählten Kanten hinzu. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Quadrantenknoten hinzufügen](TechDraw_Quadrants/de.md): fügt kosmetische Knoten an Viertelpunkten ausgewählter (kreisförmiger) Kanten hinzu. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Mittellinie zu Flächen hinzufügen](TechDraw_FaceCenterLine/de.md): fügt der/den ausgewählten Fläche(n) eine Mittellinie hinzu. <small>(v0.19)</small> 

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md): fügt eine Mittellinie zwischen 2 Linien hinzu. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Mittellinie zwischen 2 Punkten hinzufügen](TechDraw_2PointCenterLine/de.md): fügt eine Mittellinie zwischen 2 Punkten hinzu. {{Version/de|0.19}}


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Eine kosmetische Linie hinzufügen](TechDraw_2PointCosmeticLine/de.md): fügt eine kosmetische Linie hinzu, die 2 Knoten verbindet. <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Entferne Kosmetische Objekt](TechDraw_CosmeticEraser/de.md): entfernt kosmetische Objekte von einer Seite. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Aussehen von Linien ändern](TechDraw_DecorateLine/de.md): ändert das Aussehen der ausgewählten Linie(n). {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Unsichtbare Kanten anzeigen/verbergen](TechDraw_ShowAll/de.md): zeigt/verbirgt unsichtbare Linien/Kanten in einer Ansicht. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Schweißinformationen zu Führungslinie hinzufügen](TechDraw_WeldSymbol/de.md): fügt Schweißspezifikationen zu einer vorhandenen Führungslinie hinzu. {{Version/de|0.19}}

## Erweiterungspaket

Das Erweiterungspaket enthält viele nützliche Werkzeuge, um deine TechDraw-Zeichnungen zu verfeinern.


**Einige dieser Werkzeuge müssen noch freigegeben werden.**

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [CircleCenterLines](TechDraw_ExtensionCircleCenterLines.md): adds center lines to circles and arcs. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [ThreadHoleSide](TechDraw_ExtensionThreadHoleSide.md): adds a symbolic thread to the side view of a hole. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [ThreadHoleBottom](TechDraw_ExtensionThreadHoleBottom.md): adds symbolic threads to the bottom view of holes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [ThreadBoltSide](TechDraw_ExtensionThreadBoltSide.md): adds a symbolic thread to the side view of a bolt. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [ThreadBoltBottom](TechDraw_ExtensionThreadBoltBottom.md): adds symbolic threads to the bottom view of bolts. <small>(v0.20)</small> 

## Importieren/Exportieren

Dies sind Werkzeuge zum Exportieren von Seiten in andere Anwendungen.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Seite exportieren als SVG](TechDraw_ExportPageSVG/de.md): Speichert die aktuelle Seite als [SVG](SVG/de.md) Datei.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Seite Exportieren als DXF](TechDraw_ExportPageDXF/de.md): speichert die aktuelle Seite als [DXF](DXF/de.md) Datei.

## Zusatzfunktionen


<div class="mw-translate-fuzzy">

-   [Liniengruppe](TechDraw_LineGroup/de.md): um das Aussehen verschiedener Linientypen zu steuern.
-   [Vorlagen](TechDraw_Templates/de.md): Die definierten Standardvorlagen für die Zeichnungsseiten.
-   [Schraffur](TechDraw_Hatching/de.md): Erklärung der verschiedenen Schraffurtechniken.
-   [Geometrische Bemaßung und Tolerierung](TechDraw_Geometric_dimensioning_and_tolerancing/de.md): Erklärung, wie geometrische Bemaßung und Tolerierung erreicht werden.


</div>

## Preferences


<div class="mw-translate-fuzzy">

## Einstellungen

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Einstellungen](TechDraw_Preferences/de.md): Einstellungen für die Standardwerte der Zeichnungsseite wie Projektionswinkel, Farben, Textgrößen und Linienstile.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Programmierung

Die TechDraw Werkzeuge können in [Makros](macros/de.md) oder aus der [Python](Python/de.md) Konsole heraus durch Verwendung von zwei API\'s genutzt werden.

-   [TechDraw API](TechDraw_API/de.md)
-   [TechDrawGui API](TechDrawGui_API/de.md)


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Begrenzungen

-   TechDraw Zeichnungen und ihre API sind nicht mit dem [Drawing Arbeitsbereich](Drawing_Workbench/de.md) austauschbar. Es ist möglich, Zeichnungsseiten mit einem Pythonskript (`moveViews.py`) in TechDraw Seiten umzuwandeln.
-   Es ist möglich, sowohl TechDraw Seiten als auch Drawing Seiten im selben FreeCAD Dokument zu verwenden, weil jede Seite vollständig unabhängig voneinander ist.
-   Es gibt geringfügige Unterschiede bei der Angabe editierbarer Texte in [SVG](SVG/de.md) Vorlagen im Vergleich zum Zeichnungsmodul. In TechDraw beeinflusst die Skalierung des SVG Dokuments die Position der editierbaren Textfelder. Weitere Einzelheiten findest du in der Forumsdiskussion [TechDraw templates scale](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271).
-   Gewinde sind nicht implementiert. Eine mögliche Abhilfe besteht darin, eine [Durchmesserbemaßung](TechDraw_Dimension_Diameter/de.md) zu verwenden und einen geeigneten Text in die \"Format Spec\" Eigenschaft einzufügen, z.B. \"M4x15\".
-   TechDraw Objekte dürfen in der Baumansicht nicht ausgeschnitten, kopiert und eingefügt werden, da dies im Allgemeinen nicht gut funktioniert.


</div>

## Tutorien

-   [TechDraw Grundlagentutorium](Basic_TechDraw_Tutorial/de.md): Einführung in die Zeichnungserstellung mit dem TechDraw Arbeitsbereich.
-   [Erstellen einer neuen Vorlage](TechDraw_TemplateHowTo/de.md): Anweisungen in die Erstellung einer neuen Seitenvorlage in Inkscape zur Benutzung mit dem TechDraw Arbeitsbereich.
-   [Winkelbemaßung an Bohrungen](Measurement_Of_Angles_On_Holes/de.md): Anweisungen zum Hinzufügen von Mittellinien und nachfolgenden Winkeldarstellungen auf Bohrungen.
-   [Verschiedenes](TechDraw_HowTo_Page/de.md): Anweisungen für verschiedene Einstellungen wie Zentriermarken usw.
-   [Erstellen eines Teilkreises](TechDraw_Pitch_Circle.md): Anweisungen zum Hinzufügen eines Teilkreises

Video Tutorien von sliptonic

-   TechDraw Arbeitsbereich [Part 1 (Grundlagen)](https://www.youtube.com/watch?v=7LbOmSGW9F0),[Part 2 (Abmessungen)](https://www.youtube.com/watch?v=z3w84RfvqaE),[Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI).
-   TechDraw Arbeitsbereich [Part 4 (Abschnitt und Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Vorlagen anpassen)](https://www.youtube.com/watch?v=kcmdJ7xa7gg).





{{TechDraw Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > TechDraw Workbench/de
