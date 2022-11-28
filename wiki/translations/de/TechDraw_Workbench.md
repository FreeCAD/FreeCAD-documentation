# <img alt="TechDraw Arbeitsbereichssymbol" src=images/Workbench_TechDraw.svg  style="width   *64px;"> TechDraw Workbench/de

## Einführung

Der Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width   *24px;">[TechDraw](TechDraw_Workbench/de.md) dient zur Erstellung einfacher technischer Zeichnungen aus 3D-Modellen, die mit einem anderen Arbeitsbereich erstellt wurden, wie z.B. [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md), [Arch](Arch_Workbench/de.md) oder die aus anderen Anwendungen importiert wurden. Jede Zeichnung ist ein Blatt, das verschiedene Ansichten von zeichnungsfähigen Objekten wie Part-Formelemente (Part   *   *Features), PartDesign-Körper (PartDesign   *   *Bodies), gruppierte Std-Parts (App   *   *Part groups) und Std-Gruppen (App   *   *DocumentObjectGroups) enthalten kann. Die daraus entstandenen Zeichnungen können für Dokumentationen, Fertigungsanweisungen, Verträge, Genehmigungen usw. verwendet werden.

Maße, Schnittansichten, schraffierte Bereiche, Beschriftungen und Symbole im Dateiformat[SVG](SVG/de.md) können dem Blatt hinzugefügt werden. Das Blatt (die Zeichnung) kann später in verschiedene Formate wie [DXF](DXF/de.md), [SVG](SVG/de.md) und [PDF](PDF/de.md) exportiert werden.

TechDraw ist seit Version 0.17 offiziell in FreeCAD enthalten; es soll den nicht mehr unterstützten Arbeitsbereich [Drawing](Drawing_Workbench/de.md) ersetzen. Der Arbeitsbereich Drawing ist in Version 0.20 noch vorhanden, wird aber in zukünftigen Veröffentlichungen nicht mehr enthalten sein ({{VersionPlus/de|1.0}}). Um mit den Plänen und Entwicklungen von TechDraw Schritt zu halten, siehe [TechDraw-Roadmap](TechDraw_Roadmap.md) (engl.).

Wenn das Hauptziel die Erstellung komplexer 2D-Zeichnungen und [DXF](DXF/de.md)-Dateien ist und keine 3D-Modelle benötigt werden, ist FreeCAD möglicherweise nicht die richtige Wahl. Stattdessen sollte man eine spezielle (Software-)Anwendung für technisches Zeichnen in Betracht ziehen, wie [LibreCAD](https   *//de.wikipedia.org/wiki/LibreCAD) oder [QCad](https   *//de.wikipedia.org/wiki/QCad).


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width   *600px;">

## Blätter (Seiten) 

Diese Werkzeuge sind zum Erstellen von Zeichnungsblättern (Page-Objekte).

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width   *32px;"> [Neues Zeichnungsblatt aus der Standardvorlage erstellen](TechDraw_PageDefault/de.md)   * Fügt ein neues Zeichnungsblatt unter Verwendung der voreingestellten [Vorlage](TechDraw_Templates.md) hinzu.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width   *32px;"> [Neues Zeichnungsblatt aus einer Vorlage erstellen](TechDraw_PageTemplate/de.md)   * Fügt ein neues Zeichnungsblatt unter Verwendung einer frei wählbaren [Vorlage](TechDraw_Templates/de.md) hinzu.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width   *32px;"> [Seite neu zeichnen](TechDraw_RedrawPage/de.md)   * Erzwingt eine Aktualisierung des ausgewählten Zeichnungsblattes. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width   *32px;"> [Alle Seiten drucken](TechDraw_PrintAll/de.md)   * Druckt alle Zeichnungsblätter eines Dokuments. {{Version/de|1.0}}

## Ansichten

Dies sind Werkzeuge zum Erstellen von Ansichten (View-Objekten).

-   <img alt="" src=images/TechDraw_View.svg  style="width   *32px;"> [Ansicht einfügen](TechDraw_View/de.md)   * Fügt eine ausgewählte Ansicht eines 3D-Objekts ein.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width   *32px;"> [Aktive (3D-)Ansicht einfügen](TechDraw_ActiveView/de.md)   * Fügt eine Ansicht des aktiven 3D-Fensters ein. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width   *32px;"> [Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md)   * Ruft einen Dialog auf, um mehrere (zusammenhängende) Ansichten eines Objekts aus verschiedenen Richtungen zu erstellen (Seitenansicht, Draufsicht usw.).

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Schnittansichten einfügen   *

   ** <img alt="" src=images/TechDraw_SectionView.svg  style="width   *32px;"> [Schnittansicht einfügen](TechDraw_SectionView/de.md)   * Fügt eine Schnittansicht zu einer vorhandenen Ansicht ein.

   ** <img alt="" src=images/TechDraw_ComplexSection.svg  style="width   *32px;"> [Zusammengesetzte Schnittansicht einfügen](TechDraw_ComplexSection/de.md)   * Fügt eine auf einem (Schnitt-) Profil basierende Schnittansicht zu einer vorhandenen Ansicht ein. <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width   *32px;"> [Detailansicht einfügen](TechDraw_DetailView/de.md)   * Fügt eine Detailansicht eines Teils einer vorhandenen Ansicht ein.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width   *32px;"> [Objekt des Draft-Arbeitsbereiches einfügen](TechDraw_DraftView/de.md)   * Fügt eine Ansicht eines Objekts aus dem Arbeitsbereich [Draft](Draft_Workbench/de.md) ein.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width   *32px;"> [Objekt des Arch-Arbeitsbereiches einfügen](TechDraw_ArchView/de.md)   * Fügt eine Ansicht eines [Schnittebenen](Arch_SectionPlane/de.md)-Objekts aus dem Arbeitsbereich [Arch](Arch_Workbench/de.md) ein.

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width   *32px;"> [Tabellenkalkulationsansicht einfügen](TechDraw_SpreadsheetView/de.md)   * Fügt die Ansicht eines Tabellenblattes aus dem Arbeitsbereich [Spreadsheet](Spreadsheet_Workbench/de.md) (Tabellenkalkulation) hinzu.

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width   *32px;"> [Ansicht verschieben](TechDraw_MoveView/de.md)   * Verschiebt eine Ansicht samt Inhalt auf ein anderes Blatt. {{Version/de|0.20}}

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width   *32px;"> [Ansicht teilen](TechDraw_ShareView/de.md)   * Eine Ansicht wird auf mehreren Blättern gezeigt (geteilt). {{Version/de|0.20}}

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width   *32px;"> [Projiziere Formstück](TechDraw_ProjectShape/de.md)   * erzeugt Projektionen von Formstücken im [3D view](3D_view.md). <small>(v0.20)</small> 

## Stapeln

Diese Werkzeuge ändern die Stapel Reihenfolge welche die Tiefe der Sichtbarkeit von Ansichten auf einer Seite kontrolliert.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Reihenfolge im Stapel einstellen   *

   ** <img alt="" src=images/TechDraw_StackTop.svg  style="width   *32px;"> [Bewege die Ansicht auf die Oberseite des Stapels](TechDraw_StackTop/de.md)   * bewegt die Ansicht auf die Oberseite des Stapels. {{Version/de|1.0}}

   ** <img alt="" src=images/TechDraw_StackBottom.svg  style="width   *32px;"> [Bewege die Ansicht auf die Unterseite des Stapels](TechDraw_StackBottom/de.md)   * bewegt die Ansicht auf die Unterseite des Stapels. {{Version/de|1.0}}

   ** <img alt="" src=images/TechDraw_StackUp.svg  style="width   *32px;"> [Hebe die Ansichten um eine Stufe](TechDraw_StackUp/de.md)   * hebt die Ansichten um eine Stufe. {{Version/de|1.0}}

   ** <img alt="" src=images/TechDraw_StackDown.svg  style="width   *32px;"> [Senke die Ansichten um eine Stufe](TechDraw_StackDown/de.md)   * senkt die Ansichten um eine Stufe. {{Version/de|1.0}}

## Ausschnittfenster

Dies sind Werkzeuge zum Erstellen und Verwalten von Ausschnittfenstern.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width   *32px;"> [Ausschnittsgruppe einfügen](TechDraw_ClipGroup/de.md)   * Fügt eine Ausschnittsgruppe in eine Seite ein.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width   *32px;"> [Ansicht zu Ausschnittsgruppe hinzufügen](TechDraw_ClipGroupAdd/de.md)   * Fügt eine vorhandene Ansicht zu einer Ausschnittsgruppe hinzu.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width   *32px;"> [Ansicht aus Ausschnittsgruppe entfernen](TechDraw_ClipGroupRemove/de.md)   * Entfernt eine Ansicht aus einer Ausschnittsgruppe.

## Ausgestaltung

Dies sind Werkzeuge zur Ausgestaltung von Seiten oder Ansichten   *

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width   *32px;"> [Fläche mit Muster aus einer Bilddatei schraffieren](TechDraw_Hatch/de.md)   * wendet ein Schraffurmuster aus einer Datei auf eine Fläche an.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *32px;"> [Fläche mit einer geometrischen Schraffur versehen](TechDraw_GeometricHatch/de.md)   * wendet ein Schraffurmuster unter Verwendung einer Autodesk PAT Spezifikation auf eine Fläche an.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width   *32px;"> [SVG-Zeichnungselement einfügen](TechDraw_Symbol/de.md)   * fügt ein Symbol aus einer [SVG](SVG.md)-Datei in eine Seite ein.

-   <img alt="" src=images/TechDraw_Image.svg  style="width   *32px;"> [Bitmap-Grafik einfügen](TechDraw_Image/de.md)   * fügt ein PNG- oder JPG-[Bitmap](bitmap/de.md)-Bild in eine Seite ein.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width   *32px;"> [Ansichtsrahmen ein- oder ausschalten](TechDraw_ToggleFrame/de.md)   * schaltet Rahmen und Beschriftungen, die eine Ansicht umgeben, an/aus.

## Maße

Dies sind Werkzeuge für die Erstellung und Arbeit mit Maßen (Dimension-Objekten).

Lineare Maße können auf zwei Punkten, auf einer Linie oder auf zwei Linien basieren.

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width   *32px;"> [Längenmaß einfügen](TechDraw_LengthDimension/de.md)   * Fügt eine Längenmaß hinzu.

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width   *32px;"> [Horizontales Maß einfügen](TechDraw_HorizontalDimension/de.md)   * Fügt ein horizontales Längenmaß hinzu.

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width   *32px;"> [Vertikales Maß einfügen](TechDraw_VerticalDimension/de.md)   * Fügt ein vertikales Längenmaß hinzu.

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width   *32px;"> [Radienmaß einfügen](TechDraw_RadiusDimension/de.md)   * Fügt einem Kreis oder Kreisbogen ein Radienmaß hinzu.

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width   *32px;"> [Durchmessermaß einfügen](TechDraw_DiameterDimension/de.md)   * Fügt einem Kreis oder Kreisbogen ein Durchmessermaß hinzu.

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width   *32px;"> [Winkelmaß einfügen](TechDraw_AngleDimension/de.md)   * Fügt ein Winkelmaß zwischen zwei geraden Kanten hinzu.

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width   *32px;"> [Winkelmaß über 3 Punkte einfügen](TechDraw_3PtAngleDimension/de.md)   * Fügt ein Winkelmaß unter Verwendung dreier Punkte hinzu.

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Maß für Ausdehnung hinzufügen   *

   ** <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width   *32px;"> [Maß für die horizontale Ausdehnung einfügen](TechDraw_HorizontalExtentDimension/de.md)   * fügt ein Maß für die horizontale Ausdehnung hinzu. {{Version/de|0.19}}

   ** <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width   *32px;"> [Maß für die vertikale Ausdehnung einfügen](TechDraw_VerticalExtentDimension/de.md)   * fügt ein Maß für die vertikale Ausdehnung hinzu. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width   *32px;"> [Maß mit 3D-Geometrie verknüpfen](TechDraw_LinkDimension/de.md)   * Verknüpft ein vorhandenes Maß mit der 3D-Geometrie.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width   *32px;"> [Ballon-Anmerkung einfügen](TechDraw_Balloon/de.md)   * fügt einer Zeichnung eine \"Ballon\"-Anmerkung hinzu. {{Version/de|0.19}}


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width   *32px;"> [Neue Leitbemaßung](TechDraw_LandmarkDimension/de.md)   * fügt eine Leitbemaßung hinzu. <small>(v0.19)</small> 


</div>

## Anmerkungen

Die Anmerkungswerkzeuge dienen dazu, eine Zeichnung mit zusätzlichen Informationen zu \"markieren\".

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width   *32px;"> [Anmerkung einfügen](TechDraw_Annotation/de.md)   * fügt einen reinen Textblock als Anmerkung hinzu.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width   *32px;"> [Hinweislinie zur Ansicht hinzufügen](TechDraw_LeaderLine/de.md)   * fügt einer Ansicht eine Hinweislinie hinzu. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width   *32px;"> [Rich-Text-Anmerkung einfügen](TechDraw_RichTextAnnotation/de.md)   * fügt einen Formatierten Text Block als Hinweistext einer Hinweislinie oder einer Ansicht hinzu. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Cosmetische Hilfspunkte einfügen   *

   ** <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width   *32px;"> [Hilfspunkt hinzufügen](TechDraw_CosmeticVertex/de.md)   * fügt einen Knoten hinzu, der nicht Teil der Quellgeometrie ist. {{Version/de|0.19}}

   ** <img alt="" src=images/TechDraw_Midpoints.svg  style="width   *32px;"> [Kantenmittelpunkte hinzufügen](TechDraw_Midpoints/de.md)   * fügt Hilfspunkte an den Mittenpunkten der ausgewählten Kanten hinzu. {{Version/de|0.19}}

   ** <img alt="" src=images/TechDraw_Quadrants.svg  style="width   *32px;"> [Quadrantengrenzpunkte hinzufügen](TechDraw_Quadrants/de.md)   * fügt Hilfspunkte an Viertelpunkten ausgewählter (kreisförmiger) Kanten hinzu. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Mittellinien einfügen   *

   ** <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width   *32px;"> [Mittellinie zu Fläche(n) hinzufügen](TechDraw_FaceCenterLine/de.md)   * fügt der/den ausgewählten Fläche(n) eine Mittellinie hinzu. {{Version/de|0.19}}

   ** <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width   *32px;"> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md)   * fügt eine Mittellinie zwischen 2 Linien hinzu. {{Version/de|0.19}}

   ** <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width   *32px;"> [Mittellinie zwischen 2 Punkten hinzufügen](TechDraw_2PointCenterLine/de.md)   * fügt eine Mittellinie zwischen 2 Punkten hinzu. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width   *32px;"> [Hilfslinie durch 2 Punkte hinzufügen](TechDraw_2PointCosmeticLine/de.md)   * fügt eine Hilfslinie hinzu, die 2 Knoten verbindet. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width   *32px;"> [Hilfsobjekt entfernen](TechDraw_CosmeticEraser/de.md)   * Entfernt Hilfsobjekte von einer Seite. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width   *32px;"> [Liniendarstellung ändern](TechDraw_DecorateLine/de.md)   * ändert das Aussehen der ausgewählten Linie(n). {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width   *32px;"> [Verdeckte Kanten ein-/ausblenden](TechDraw_ShowAll/de.md)   * zeigt/verbirgt unsichtbare Linien/Kanten in einer Ansicht. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width   *32px;"> [Hinzufügen von Schweißinformationen zur Hinweislinie](TechDraw_WeldSymbol/de.md)   * fügt Schweißspezifikationen zu einer vorhandenen Hinweislinie hinzu. {{Version/de|0.19}}

-   <img alt="" src=images/TechDraw_SurfaceFinishSymbol.svg  style="width   *32px;"> [Füge Oberflächen Fertigungssymbol ein](TechDraw_SurfaceFinishSymbol/de.md)   * fügt ein Oberflächen Fertigungssymbol ein. {{Version/de|1.0}}

## Erweiterungspaket

Das Erweiterungspaket enthält viele nützliche Werkzeuge, um deine TechDraw-Zeichnungen zu verfeinern.

### Eigenschaften und Änderungen 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width   *32px;"> [Ansicht](TechDraw_ExtensionSelectLineAttributes/de.md)   * Wähle Stil, Breite und Farbe der Linien. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width   *32px;"> [Aussehen ändern](TechDraw_ExtensionChangeLineAttributes/de.md)   * Ändern von Stil, Breite und Farbe von Linien. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Ändern der Länge von kosmetischen Linien oder Mittellinien    *

   ** <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width   *32px;"> [Dehnen](TechDraw_ExtensionExtendLine/de.md)   * Verlängern einer Linie an beiden Enden. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width   *32px;"> [Verkürzen](TechDraw_ExtensionShortenLine/de.md)   * Verkürzen einer Linie an beiden Enden. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width   *32px;"> [Sperren/Entsperren](TechDraw_ExtensionLockUnlockView/de.md)   * Sperren/Entsperren einer Ansicht. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width   *32px;"> [Schnittansicht ausrichten](TechDraw_ExtensionPositionSectionView/de.md)   * Richte eine Schnittansicht rechtwinkelig zur Quellansicht aus. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Bemaßungen ausrichten   *

   ** <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width   *32px;"> [Horizontales Ausrichten](TechDraw_ExtensionPosHorizChainDimension/de.md)   * Richte eine horizontale Kettenbemaßung aus. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width   *32px;"> [Vertikal ausrichten](TechDraw_ExtensionPosVertChainDimension/de.md)   * Richte eine vertikale Kettenbemaßung aus. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width   *32px;"> [Schräg ausrichten](TechDraw_ExtensionPosObliqueChainDimension/de.md)   * Richte eine schräge Kettenbemaßung aus. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Abstände zwischen Bemaßungen   *

   ** <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width   *32px;"> [Horizontale Abstände](TechDraw_ExtensionCascadeHorizDimension/de.md)   * Bilde Abstände zwischen horizontalen Maßen. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width   *32px;"> [Vertikale Abstände](TechDraw_ExtensionCascadeVertDimension/de.md)   * Bilde Abstände zwischen vertikalen Maßen. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width   *32px;"> [Schräge Abstände](TechDraw_ExtensionCascadeObliqueDimension/de.md)   * Bilde Abstände zwischen schrägen Maßen. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width   *32px;"> [Flächenangabe](TechDraw_ExtensionAreaAnnotation/de.md)   * Berechnet den Flächeninhalt von ausgewählten Flächen und fügt ihn als Hinweistext mit Rahmen ein. {{Version/de|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width   *32px;"> [Formatierung anpassen](TechDraw_ExtensionCustomizeFormat/de.md)   * Passt die Formatierung von Hinweistexten und Maßeinträgen an. Es können Symbole für Form- und Lagetolerierung (GD&T) und andere Sonderzeichen hinzugefügt werden. {{Version/de|0.20}}

### Mittellinien und Gewinde 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Mittellinien einfügen   *

   ** <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width   *32px;"> [Mittellinien bei Kreisbogen-Kreis](TechDraw_ExtensionCircleCenterLines/de.md)   * Erzeuge Mittellinien bei Kreisen und Kreisbögen. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width   *32px;"> [Loch/Bolzenkreis Mittellinien](TechDraw_ExtensionHoleCircle/de.md)   * Zeichne die Mittellinien eines Loch/Bolzenkreises. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Kosmetische Gewinde einfügen   *

   ** <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width   *32px;"> [Bohrungsgewinde im Schnitt](TechDraw_ExtensionThreadHoleSide/de.md)   * Füge ein symbolisches Gewinde zum Schnitt einer Bohrung hinzu. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width   *32px;"> [Bohrungsgewinde](TechDraw_ExtensionThreadHoleBottom/de.md)   * Füge ein symbolisches Gewinde zu einer von oben gesehenen Bohrung hinzu. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width   *32px;"> [Bolzengewinde Seitenansicht](TechDraw_ExtensionThreadBoltSide/de.md)   * Füge ein symbolisches Gewinde zur Seitenansicht eines Bolzens hinzu. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width   *32px;"> [Bolzengewinde](TechDraw_ExtensionThreadBoltBottom/de.md)   * Füge ein symbolisches Gewinde zu einem von oben gesehenen Bolzen hinzu. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width   *32px;"> [Schnittpunkt](TechDraw_ExtensionVertexAtIntersection/de.md)   * Erzeuge Konstruktionspunkte im Schnittpunkt von Linien. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Kosmetische Kreise und Kreisbögen einfügen   *

   ** <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width   *32px;"> [Kreislinie](TechDraw_ExtensionDrawCosmCircle/de.md)   * Zeichne eine Kreislinie durch Mittelpunkt und Radiuspunkt. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width   *32px;"> [Kreisbogen](TechDraw_ExtensionDrawCosmArc/de.md)   * Zeichne einen gegen den Uhrzeiger rotierenden Kreisbogen. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width   *32px;"> [Kreislinie durch 3 Punkte](TechDraw_ExtensionDrawCosmCircle3Points/de.md)   * fügt einen hilfslinien 3 Punkte Kreis ein. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Parallele oder rechtwinkelige kosmetische Linien einfügen   *

   ** <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width   *32px;"> [Parallel](TechDraw_ExtensionLineParallel/de.md)   * Zeichne eine Linie parallel zu einer Anderen durch einen Konstruktionspunkt. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width   *32px;"> [Rechtwinkelig](TechDraw_ExtensionLinePerpendicular/de.md)   * Zeichne eine Linie im rechten Winkel auf eine Andere, durch einen Konstruktionspunkt. <small>(v0.20)</small> 

### Maße 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Kettenmaße erzeugen   *

   ** <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width   *32px;"> [Horizontales Kettenmaß](TechDraw_ExtensionCreateHorizChainDimension/de.md)   * Erzeuge ein horizontales Kettenmaß. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width   *32px;"> [Vertikales Kettenmaß](TechDraw_ExtensionCreateVertChainDimension/de.md)   * Erzeuge ein vertikales Kettenmaß. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width   *32px;"> [Schräges Kettenmaß](TechDraw_ExtensionCreateObliqueChainDimension/de.md)   * Erzeuge ein schräges Kettenmaß. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Stufenbemaßungen erzeugen   *

   ** <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width   *32px;"> [Horizontale Stufenbemaßung](TechDraw_ExtensionCreateHorizCoordDimension/de.md)   * erzeuge eine horizontale Stufenbemaßung. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width   *32px;"> [Vertikale Stufenbemaßung](TechDraw_ExtensionCreateVertCoordDimension/de.md)   * Erzeuge eine vertikale Stufenbemaßung. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width   *32px;"> [Schräge Stufenbemaßung](TechDraw_ExtensionCreateObliqueCoordDimension/de.md)   * Erzeuge eine schräge Stufenbemaßung. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Fasenbemaßung erzeugen   *

   ** <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width   *32px;"> [Horizontale Fasenbemaßung](TechDraw_ExtensionCreateHorizChamferDimension/de.md)   * erzeuge eine horizontale Fasenbemaßung. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width   *32px;"> [Vertikale Fasenbemaßung](TechDraw_ExtensionCreateVertChamferDimension/de.md)   * erzeuge eine vertikale Fasenbemaßung. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width   *32px;"> [Bogenmaß](TechDraw_ExtensionCreateLengthArc/de.md)   * Erzeugt ein Maß für die (gestreckte) Länge eines Bogens. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Präfix Zeichen erzeugen   *

   ** <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width   *32px;"> [Durchmesserzeichen](TechDraw_ExtensionInsertDiameter/de.md)   * Füge ein Durchmesserzeichen als erstes Zeichen ein. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width   *32px;"> [Rohrsymbol](TechDraw_ExtensionInsertSquare/de.md)   * Füge eine Rohrsymbol als erstes Zeichen ein. <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width   *32px;"> [Entferne das Präfix](TechDraw_ExtensionRemovePrefixChar/de.md)   * entfernt alle Symbole am Anfang eines Maßtextes. <small>(v0.20)</small> 

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width   *" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width   *" height="32px;"> Anzahl der Dezimalstellen ändern   *

   ** <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width   *32px;"> [Genauigkeit vergrößern](TechDraw_ExtensionIncreaseDecimal/de.md)   * vergrößere die Anzahl der Dezimalstellen . <small>(v0.20)</small> 

   ** <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width   *32px;"> [Genauigkeit verkleinern](TechDraw_ExtensionDecreaseDecimal/de.md)   * verkleinere die Anzahl der Dezimalstellen . <small>(v0.20)</small> 

## Importieren/Exportieren

Dies sind Werkzeuge zum Exportieren von Seiten in andere Anwendungen.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width   *32px;"> [Seite als SVG-Datei exportieren](TechDraw_ExportPageSVG/de.md)   * Speichert die aktuelle Seite als [SVG](SVG/de.md)-Datei.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width   *32px;"> [Seite als DXF-Datei exportieren](TechDraw_ExportPageDXF/de.md)   * speichert die aktuelle Seite als [DXF](DXF/de.md)-Datei.

## Zusatzfunktionen

-   [Liniengruppe](TechDraw_LineGroup/de.md)   * um das Aussehen verschiedener Linientypen zu steuern.
-   [Vorlagen](TechDraw_Templates/de.md)   * Die definierten Standardvorlagen für die Zeichnungsseiten.
-   [Schraffur](TechDraw_Hatching/de.md)   * Erklärung der verschiedenen Schraffurtechniken.
-   [Geometrische Bemaßung und Tolerierung](TechDraw_Geometric_dimensioning_and_tolerancing/de.md) (GD&T)   * Erklärung zur Form- und Lagetolerierung.

## Einstellungen

-   <img alt="" src=images/Preferences-techdraw.svg  style="width   *32px;"> [Einstellungen](TechDraw_Preferences/de.md)   * Einstellungen für die Standardwerte der Zeichnungsseite wie Projektionswinkel, Farben, Textgrößen und Linienstile.

## Skripten

Die TechDraw-Werkzeuge können in [Makros](Macros/de.md) oder von der [Python](Python/de.md)-Konsole aus verwendet werden. Für weitere Informationen siehe   *

-   [Autogenerated API documentation](https   *//freecad.github.io/SourceDoc/)
-   [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md)
-   [Editierbare Textfelder](TechDraw_PageDefault/de#Editierbare_Textfelder.md)

## Einschränkungen

-   TechDraw Zeichnungen und ihre API sind nicht mit dem [Drawing Arbeitsbereich](Drawing_Workbench/de.md) austauschbar. Es ist möglich, Zeichnungsseiten mit einem Pythonskript (`moveViews.py`) in TechDraw Seiten umzuwandeln.
-   Es ist möglich, sowohl TechDraw Seiten als auch Drawing Seiten im selben FreeCAD Dokument zu verwenden, weil die Seiten vollständig unabhängig voneinander sind.
-   Es gibt geringfügige Unterschiede bei der Angabe editierbarer Texte in [SVG](SVG/de.md)-Vorlagen im Vergleich zum Zeichnungsmodul. In TechDraw beeinflusst die Skalierung des SVG-Dokuments die Position der editierbaren Textfelder. Weitere Einzelheiten findet man in der Forumsdiskussion [TechDraw templates scale](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271).
-   TechDraw Objekte dürfen in der [Baumansicht](Tree_view/de.md) nicht ausgeschnitten, kopiert und eingefügt werden, da dies im Allgemeinen nicht gut funktioniert.
-   TechDraw Objekte dürfen in der [Baumansicht](Tree_view/de.md) nicht mit der Maus bewegt werden.

## Tutorien

-   [TechDraw Grundlagentutorium](Basic_TechDraw_Tutorial/de.md)   * Einführung in die Zeichnungserstellung mit dem Arbeitsbereich TechDraw.
-   [Erstellen einer neuen Vorlage](TechDraw_TemplateHowTo/de.md)   * Anweisungen für die Erstellung einer neuen Seitenvorlage mit Inkscape zur Verwendung im Arbeitsbereich TechDraw.
-   [TechDraw Vorlagengenerator](TechDraw_TemplateGenerator/de.md)   * Anleitung zum Erstellen eines Makros für die Erstellung einer einfachen Vorlage.

   *   Ein \"paar\" Zeilen Kode, die ein Werkzeug ähnlich dem [Makro TemplateHelper](Macro_TemplateHelper/de.md) ergeben.

-   [Maßeintrag für Bohrungswinkel](Measurement_Of_Angles_On_Holes/de.md)   * Anweisungen zum Hinzufügen von Mittellinien und der nachfolgenden Eintragung der Neigungswinkel von Bohrungen.
-   [Verschiedenes](TechDraw_HowTo_Page/de.md)   * Anweisungen für verschiedene Einstellungen wie Mittelpunktsmarkierungen usw.
-   [TechDraw Pitch Circle Tutorial](TechDraw_Pitch_Circle_Tutorial.md)   * Anweisungen zum Hinzufügen eines Teilkreises.

Video Tutorien von sliptonic

-   TechDraw Arbeitsbereich [Part 1 (Grundlagen)](https   *//www.youtube.com/watch?v=7LbOmSGW9F0),[Part 2 (Abmessungen)](https   *//www.youtube.com/watch?v=z3w84RfvqaE),[Part 3 (Multiview)](https   *//www.youtube.com/watch?v=uNjXg-m38aI).
-   TechDraw Arbeitsbereich [Part 4 (Abschnitt und Detail)](https   *//www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Vorlagen anpassen)](https   *//www.youtube.com/watch?v=kcmdJ7xa7gg).





{{TechDraw_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/de
