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

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width:32px;"> [Move View](TechDraw_MoveView.md): Moves a view and its dependents to a different page. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width:32px;"> [Share View](TechDraw_ShareView.md): Share a view between multiple pages. <small>(v0.20)</small> 

## Ausschnittfenster

Dies sind Werkzeuge zum Erstellen und Verwalten von Ausschnittfenstern.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Clipgruppe einfügen](TechDraw_ClipGroup/de.md): Fügt eine Clipgruppe in eine Seite ein.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Ausschnittfenster hinzufügen](TechDraw_ClipGroupAdd/de.md): Fügt eine vorhandene Ansicht zu einer Gruppe von Ausschnittfenstern hinzu.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Ausschnittfenster entfernen](TechDraw_ClipGroupRemove/de.md): Entfernt eine Ansicht aus einer Gruppe von Ausschnittfenstern.

## Ausgestaltung

Dies sind Werkzeuge zur Ausgestaltung von Seiten oder Ansichten:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Schraffierte Fläche unter Verwendung einer Bilddatei](TechDraw_Hatch/de.md): wendet ein Schraffurmuster aus einer Datei auf eine Fläche an.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Geometrische Schraffur auf Fläche anwenden](TechDraw_GeometricHatch/de.md): wendet ein Schraffurmuster unter Verwendung einer Autodesk PAT Spezifikation auf eine Fläche an.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [SVG Symbol einfügen](TechDraw_Symbol/de.md): fügt ein Symbol aus einer [SVG](SVG.md) Datei in eine Seite ein.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Bitmap Bild einfügen](TechDraw_Image/de.md): fügt ein PNG oder JPG [Bitmap](bitmap/de.md) Bild in eine Seite ein.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Ansichtsrahmen drehen On/Off](TechDraw_ToggleFrame/de.md): schaltet Rahmen und Beschriftungen, die eine Ansicht umgeben, an/aus.

## Bemaßungen

Dies sind Werkzeuge für die Erstellung und Arbeit mit Bemaßungs-Objekten.

Lineare Bemaßungen können auf zwei Punkten, auf einer Linie oder auf zwei Linien basieren.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Längenbemaßung einfügen](TechDraw_LengthDimension/de.md): Fügt eine Längenbemaßung hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Eine horizontale Abstands-Bemaßung einfügen](TechDraw_HorizontalDimension/de.md): Fügt eine horizontale Längenbemaßung hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Eine vertikale Abstands-Bemaßung einfügen](TechDraw_VerticalDimension/de.md): Fügt eine vertikale Längenbemaßung hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Einen Radius der gewählten Ansicht bemaßen](TechDraw_RadiusDimension/de.md): Fügt eine Radiusbemaßung zu einem Kreis oder Kreisbogen hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Ein neues Durchmessermaß in die gewählte Ansicht einfügen](TechDraw_DiameterDimension/de.md): Fügt eine Durchmesserbemaßung zu einem Kreis oder Kreisbogen hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Winkel bemaßen](TechDraw_AngleDimension/de.md): Fügt eine Winkelbemaßung zwischen zwei geraden Linienkanten hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Winkelbemaßung mittels 3 Eckpunkten](TechDraw_3PtAngleDimension/de.md): Fügt eine Winkelbemaßung mittels drei Eckpunkten hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Neue horizontale Ausdehnung](TechDraw_HorizontalExtentDimension/de.md): fügt eine horizontale Ausdehnungsbemaßung hinzu. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Neue vertikale Ausdehnung](TechDraw_VerticalExtentDimension/de.md): fügt eine vertikale Ausdehnungsbemaßung hinzu. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Eine Abmessung mit einer 3D-Geometrie verlinken](TechDraw_LinkDimension/de.md): Eine oder mehrere Bemaßungen mit einer 3D-Geometrie verlinken.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [New Balloon](TechDraw_Balloon/de.md): fügt einer Zeichnung eine \"Ballon\"-Anmerkung für Positionsnummern (z.B. für Stücklisten) hinzu. {{Version/de|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Neue Leitbemaßung](TechDraw_LandmarkDimension/de.md): fügt eine Leitbemaßung hinzu. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

## Anmerkung


</div>

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

### Eigenschaften und Änderungen 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:32px;"> [Ansicht](TechDraw_ExtensionSelectLineAttributes/de.md): Wähle Stil, Breite und Farbe der Linien. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width:32px;"> [Aussehen ändern](TechDraw_ExtensionChangeLineAttributes/de.md): Ändern von Stil, Breite und Farbe von Linien. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:32px;"> [Dehnen](TechDraw_ExtensionExtendLine/de.md): Verlängern einer Linie an beiden Enden. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width:32px;"> [Verkürzen](TechDraw_ExtensionShortenLine/de.md): Verkürzen einer Linie an beiden Enden. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width:32px;"> [Sperren/Entsperren](TechDraw_ExtensionLockUnlockView/de.md): Sperren/Entsperren einer Ansicht. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width:32px;"> [Schnittansicht ausrichten](TechDraw_ExtensionPositionSectionView/de.md): Richte eine Schnittansicht rechtwinkelig zur Quellansicht aus. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:32px;"> [Horizontales Ausrichten](TechDraw_ExtensionPosHorizChainDimension/de.md): Richte eine horizontale Kettenbemaßung aus. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width:32px;"> [Vertikal ausrichten](TechDraw_ExtensionPosVertChainDimension/de.md): Richte eine vertikale Kettenbemaßung aus. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width:32px;"> [Schräg ausrichten](TechDraw_ExtensionPosObliqueChainDimension/de.md): Richte eine schräge Kettenbemaßung aus. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:32px;"> [Horizontale Abstände](TechDraw_ExtensionCascadeHorizDimension/de.md): Bilde Abstände zwischen horizontalen Maßen. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width:32px;"> [Vertikale Abstände](TechDraw_ExtensionCascadeVertDimension/de.md): Bilde Abstände zwischen vertikalen Maßen. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width:32px;"> [Schräge Abstände](TechDraw_ExtensionCascadeObliqueDimension/de.md): Bilde Abstände zwischen schrägen Maßen. <small>(v0.20)</small> 

### Mittellinien und Gewinde 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Mittellinien bei Kreisbogen-Kreis](TechDraw_ExtensionCircleCenterLines/de.md): Erzeuge Mittellinien bei Kreisen und Kreisbögen. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width:32px;"> [Loch/Bolzenkreis Mittellinien](TechDraw_ExtensionHoleCircle/de.md): Zeichne die Mittellinien eines Loch/Bolzenkreises. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Bohrungsgewinde im Schnitt](TechDraw_ExtensionThreadHoleSide/de.md): Füge ein symbolisches Gewinde zum Schnitt einer Bohrung hinzu. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Bohrungsgewinde](TechDraw_ExtensionThreadHoleBottom/de.md): Füge ein symbolisches Gewinde zu einer von oben gesehenen Bohrung hinzu. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [Bolzengewinde Seitenansicht](TechDraw_ExtensionThreadBoltSide/de.md): Füge ein symbolisches Gewinde zur Seitenansicht eines Bolzens hinzu. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Bolzengewinde](TechDraw_ExtensionThreadBoltBottom/de.md): Füge ein symbolisches Gewinde zu einem von oben gesehenen Bolzen hinzu. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:32px;"> [Schnittpunkt](TechDraw_ExtensionVertexAtIntersection/de.md): Erzeuge Konstruktionspunkte im Schnittpunkt von Linien. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:32px;"> [Kreislinie](TechDraw_ExtensionDrawCosmCircle/de.md): Zeichne eine Kreislinie durch Mittelpunkt und Radiuspunkt. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawArc.svg  style="width:32px;"> [Kreisbogen](TechDraw_ExtensionDrawArc.md): Zeichne einen gegen den Uhrzeiger rotierenden Kreisbogen. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width:32px;"> [Add Cosmetic Circle 3 Points](TechDraw_ExtensionDrawCosmCircle3Points.md): fügt einen hilfslinien 3 Punkte Kreis ein. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:32px;"> [Parallel](TechDraw_ExtensionLineParallel/de.md): Zeichne eine Linie parallel zu einer Anderen durch einen Konstruktionspunkt. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width:32px;"> [Rechtwinkelig](TechDraw_ExtensionLinePerpendicular/de.md): Zeichne eine Linie im rechten Winkel auf eine Andere, durch einen Konstruktionspunkt. <small>(v0.20)</small> 

### Maße

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Horizontales Kettenmaß](TechDraw_ExtensionCreateHorizChainDimension/de.md): Erzeuge ein horizontales Kettenmaß. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Vertikales Kettenmaß](TechDraw_ExtensionCreateVertChainDimension/de.md): Erzeuge ein vertikales Kettenmaß. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Schräges Kettenmaß](TechDraw_ExtensionCreateObliqueChainDimension/de.md): Erzeuge ein schräges Kettenmaß. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Horizontale Stufenbemaßung](TechDraw_ExtensionCreateHorizCoordDimension/de.md): erzeuge eine horizontale Stufenbemaßung. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Vertikale Stufenbemaßung](TechDraw_ExtensionCreateVertCoordDimension/de.md): Erzeuge eine vertikale Stufenbemaßung. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Schräge Stufenbemaßung](TechDraw_ExtensionCreateObliqueCoordDimension/de.md): Erzeuge eine schräge Stufenbemaßung. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Horizontale Fasenbemaßung](TechDraw_ExtensionCreateHorizChamferDimension/de.md): erzeuge eine horizontale Fasenbemaßung. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Vertikale Fasenbemaßung](TechDraw_ExtensionCreateVertChamferDimension/de.md): erzeuge eine vertikale Fasenbemaßung. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Kreisbogen Längenmaß](TechDraw_ExtensionCreateLengthArc/de.md): erzeuge ein Kreisbogen Längenmaß. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:32px;"> [Durchmesserzeichen](TechDraw_ExtensionInsertDiameter/de.md): Füge ein Durchmesserzeichen als erstes Zeichen ein. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width:32px;"> [Rohrsymbol](TechDraw_ExtensionInsertSquare/de.md): Füge eine Rohrsymbol als erstes Zeichen ein. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width:32px;"> [Remove Prefix](TechDraw_ExtensionRemovePrefixChar.md): entfernt alle Symbole am Anfang eines Maßtextes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:32px;"> [Genauigkeit vergrößern](TechDraw_ExtensionIncreaseDecimal/de.md): vergrößere die Anzahl der Dezimalstellen . <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width:32px;"> [Genauigkeit verkleinern](TechDraw_ExtensionDecreaseDecimal/de.md): verkleinere die Anzahl der Dezimalstellen . <small>(v0.20)</small> 

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
-   TechDraw Objekte dürfen in der Baumansicht nicht ausgeschnitten, kopiert und eingefügt werden, da dies im Allgemeinen nicht gut funktioniert.


</div>

## Tutorien


<div class="mw-translate-fuzzy">

-   [TechDraw Grundlagentutorium](Basic_TechDraw_Tutorial/de.md): Einführung in die Zeichnungserstellung mit dem TechDraw Arbeitsbereich.
-   [Erstellen einer neuen Vorlage](TechDraw_TemplateHowTo/de.md): Anweisungen in die Erstellung einer neuen Seitenvorlage in Inkscape zur Benutzung mit dem TechDraw Arbeitsbereich.
-   [Winkelbemaßung an Bohrungen](Measurement_Of_Angles_On_Holes/de.md): Anweisungen zum Hinzufügen von Mittellinien und nachfolgenden Winkeldarstellungen auf Bohrungen.
-   [Verschiedenes](TechDraw_HowTo_Page/de.md): Anweisungen für verschiedene Einstellungen wie Zentriermarken usw.
-   [Erstellen eines Teilkreises](TechDraw_Pitch_Circle_Tutorial.md): Anweisungen zum Hinzufügen eines Teilkreises.


</div>

Video Tutorien von sliptonic

-   TechDraw Arbeitsbereich [Part 1 (Grundlagen)](https://www.youtube.com/watch?v=7LbOmSGW9F0),[Part 2 (Abmessungen)](https://www.youtube.com/watch?v=z3w84RfvqaE),[Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI).
-   TechDraw Arbeitsbereich [Part 4 (Abschnitt und Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Vorlagen anpassen)](https://www.youtube.com/watch?v=kcmdJ7xa7gg).





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [TechDraw](Category_TechDraw.md) > TechDraw Workbench/de
