# <img alt="Symbol des Arbeitsbereichs TechDraw" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/de



## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;">[TechDraw](TechDraw_Workbench/de.md) dient zur Erstellung einfacher technischer Zeichnungen aus 3D-Modellen, die mit einem anderen Arbeitsbereich erstellt wurden, wie z.B. [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md), [BIM](BIM_Workbench/de.md) oder die aus anderen Anwendungen importiert wurden. Jede Zeichnung ist ein Blatt, das verschiedene Ansichten von zeichnungsfähigen Objekten wie Part-Formelemente (Part::Features), PartDesign-Körper (PartDesign::Bodies), gruppierte Std-Parts (App::Part groups) und Std-Gruppen (App::DocumentObjectGroups) enthalten kann. Die daraus entstandenen Zeichnungen können für Dokumentationen, Fertigungsanweisungen, Verträge, Genehmigungen usw. verwendet werden.

Maße, Schnittansichten, schraffierte Bereiche, Beschriftungen und Symbole im Dateiformat[SVG](SVG/de.md) können dem Blatt hinzugefügt werden. Das Blatt (die Zeichnung) kann später in verschiedene Formate wie [DXF](DXF/de.md), [SVG](SVG/de.md) und [PDF](PDF/de.md) exportiert werden.

Wenn das Hauptziel die Erstellung komplexer 2D-Zeichnungen und [DXF](DXF/de.md)-Dateien ist und keine 3D-Modelle benötigt werden, ist FreeCAD möglicherweise nicht die richtige Wahl. Stattdessen sollte man eine spezielle (Software-)Anwendung für technisches Zeichnen in Betracht ziehen, wie [LibreCAD](https://de.wikipedia.org/wiki/LibreCAD) oder [QCad](https://de.wikipedia.org/wiki/QCad).




<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">



## Einrasten


{{Version/de|1.0}}

: Der Arbeitsbereich TechDraw besitzt eine Einrastfunktion. Sie kann eingesetzt werden, um Ansichten, Schnittansichten und Maße automatisch auszurichten, wenn sie durch Ziehen mir der Maus positioniert werden. Ist **Ausrichtung der Ansicht einrasten View Alignment** in den [Voreinstellungen](TechDraw_Preferences/de#Einrasten.md) aktiviert (Standardeinstellung), rasten Ansichten auf die korrekte Lage zu anderen Ansichten ein, sobald sie sich dicht genug an dieser Lage befinden (Einstellung **Einrastfaktor für Ansichten**). Maße rasten auch entlang anderer paralleler Maße ein und Maßtexte können in der Mitte der Maßlinie einrasten. Einrasten kann durch Gedrückthalten der **Alt**-Taste zeitweilig ausgeschaltet werden.



## Werkzeuge



### Zeichnungsblätter

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Neues Zeichnungsblatt aus der Standardvorlage erstellen](TechDraw_PageDefault/de.md): Fügt ein neues Zeichnungsblatt unter Verwendung der voreingestellten [Vorlage](TechDraw_Templates.md) hinzu.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Neues Zeichnungsblatt aus einer Vorlage erstellen](TechDraw_PageTemplate/de.md): Fügt ein neues Zeichnungsblatt unter Verwendung einer frei wählbaren [Vorlage](TechDraw_Templates/de.md) hinzu.

-   <img alt="" src=images/TechDraw_FillTemplateFields.svg  style="width:32px;"> [Vorlagenfelder aktualisieren](TechDraw_FillTemplateFields/de.md): <small>(v1.0)</small> 

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Seite neu zeichnen](TechDraw_RedrawPage/de.md): Erzwingt eine Aktualisierung des ausgewählten Zeichnungsblattes.

-   <img alt="" src=images/TechDraw_PrintAll.svg  style="width:32px;"> [Alle Seiten drucken](TechDraw_PrintAll/de.md): Druckt alle Zeichnungsblätter eines Dokuments. {{Version/de|0.21}}

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Seite als SVG-Datei exportieren](TechDraw_ExportPageSVG/de.md): Speichert die aktuelle Seite als [SVG](SVG/de.md)-Datei.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Seite als DXF-Datei exportieren](TechDraw_ExportPageDXF/de.md): speichert die aktuelle Seite als [DXF](DXF/de.md)-Datei.



### Ansichten



#### TechDraw-Ansichten 

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Ansicht einfügen](TechDraw_View/de.md): Fügt eine Darstellung eines oder mehrerer Objekte hinzu. {{Version/de|1.0}}: Es kann eine einzelne Ansicht, eine [Ansichtengruppe](TechDraw_ProjectionGroup/de.md), eine [Tabellenansicht](TechDraw_SpreadsheetView/de.md), eine [Arch-Ansicht](TechDraw_ArchView.md), ein [Zeichnungselement](TechDraw_Symbol/de.md) oder eine [Bildansicht](TechDraw_Image/de.md) erstellen.

-   <img alt="" src=images/TechDraw_BrokenView.svg  style="width:32px;"> [Unterbrochene Ansicht einfügen](TechDraw_BrokenView/de.md): Fügt eine unterbrochene Ansicht von einem oder mehreren Objekten hinzu. {{Version/de|1.0}}

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Schnittansicht einfügen](TechDraw_SectionView/de.md): Fügt eine Schnittansicht zu einer vorhandenen Ansicht ein.

-   <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Komplexe Schnittansicht einfügen](TechDraw_ComplexSection/de.md): Fügt eine, auf einer Kontur (Schnittprofil) basierende, Schnittansicht zu einer vorhandenen Ansicht ein. {{Version/de|0.21}}

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Detailansicht einfügen](TechDraw_DetailView/de.md): Fügt eine Detailansicht eines Bereiches einer vorhandenen Ansicht ein.

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md): Ruft einen Dialog auf, um mehrere (zusammenhängende) Ansichten eines Objekts aus verschiedenen Richtungen zu erstellen (Seitenansicht, Draufsicht usw.). {{Version/de|1.0}}: Das Werkzeug [Ansicht einfügen](TechDraw_View/de.md) kann anstatt dieses Werkzeugs verwendet werden.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Ausschnittsgruppe einfügen](TechDraw_ClipGroup/de.md): Fügt eine Ausschnittsgruppe ein.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [SVG-Zeichnungselement einfügen](TechDraw_Symbol/de.md): Fügt ein Symbol aus einer [SVG](SVG.md)-Datei in ein Zeichnungsblatt ein. {{Version/de|1.0}}: Das Werkzeug [Ansicht einfügen](TechDraw_View/de.md) kann anstatt dieses Werkzeugs verwendet werden.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Bitmap-Grafik einfügen](TechDraw_Image/de.md): Fügt ein PNG- oder JPG-[Bitmap](bitmap/de.md)-Bild in ein Zeichnungsblatt ein. {{Version/de|1.0}}: Das Werkzeug [Ansicht einfügen](TechDraw_View/de.md) kann anstatt dieses Werkzeugs verwendet werden.

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width:32px;"> [Ansicht teilen](TechDraw_ShareView/de.md): Eine Ansicht wird auf mehreren Blättern angezeigt (geteilt).

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Ansichtsrahmen ein- oder ausschalten](TechDraw_ToggleFrame/de.md): Schaltet Rahmen und Beschriftungen, die eine Ansicht umgeben, ein bzw. aus.

-   <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:32px;"> [Form projizieren](TechDraw_ProjectShape/de.md): Erstellt Projektionen von Formen in der [3D-Ansicht](3D_view/de.md).



#### Ansichten von anderen Arbeitsbereichen 

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Aktive (3D-)Ansicht einfügen](TechDraw_ActiveView/de.md): Fügt eine Ansicht des aktiven 3D-Fensters ein.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Objekt des Draft-Arbeitsbereiches einfügen](TechDraw_DraftView/de.md): Fügt eine Ansicht eines Objekts aus dem Arbeitsbereich [Draft](Draft_Workbench/de.md) ein.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Objekt des Arbeitsbereichs BIM einfügen](TechDraw_ArchView/de.md): Fügt eine Ansicht eines [Schnittebenen](Arch_SectionPlane/de.md)-Objekts aus dem Arbeitsbereich [BIM](BIM_Workbench/de.md) ein. {{Version/de|1.0}}: Das Werkzeug [Ansicht einfügen](TechDraw_View/de.md) kann anstatt dieses Werkzeugs verwendet werden.

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Tabellenkalkulationsansicht einfügen](TechDraw_SpreadsheetView/de.md): Fügt die Ansicht eines Tabellenblattes aus dem Arbeitsbereich [Spreadsheet](Spreadsheet_Workbench/de.md) (Tabellenkalkulation) hinzu. {{Version/de|1.0}}: Das Werkzeug [Ansicht einfügen](TechDraw_View/de.md) kann anstatt dieses Werkzeugs verwendet werden.



### Stapeln

Diese Werkzeuge ändern die Stapelreihenfolge, welche die scheinbare Tiefe von Ansichten auf einem Zeichnungsblatt steuert.

-   <img alt="" src=images/TechDraw_StackTop.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Stapelreihenfolge der Ansichten anpassen:

  - <img alt="" src=images/TechDraw_StackTop.svg  style="width:32px;"> [Ansicht auf die Stapeloberseite bewegen](TechDraw_StackTop/de.md): bewegt die Ansicht auf die Oberseite des Stapels. {{Version/de|0.21}}

  - <img alt="" src=images/TechDraw_StackBottom.svg  style="width:32px;"> [Ansicht zur Stapelunterseite bewegen](TechDraw_StackBottom/de.md): bewegt die Ansicht auf die Unterseite des Stapels. {{Version/de|0.21}}

  - <img alt="" src=images/TechDraw_StackUp.svg  style="width:32px;"> [Ansicht um eine Ebene nach oben bewegen](TechDraw_StackUp/de.md): Bewegt Ansichten um eine Ebene nach oben. {{Version/de|0.21}}

  - <img alt="" src=images/TechDraw_StackDown.svg  style="width:32px;"> [Ansicht um eine Ebene nach unten bewegen](TechDraw_StackDown/de.md): Bewegt Ansichten um eine Ebene nach unten. {{Version/de|0.21}}



### Maße

-   <img alt="" src=images/TechDraw_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Maße:

  - <img alt="" src=images/TechDraw_Dimension.svg  style="width:32px;"> [Maß einfügen](TechDraw_Dimension/de.md): Fügt ein kontextabhängiges Maß hinzu. {{Version/de|1.0}}

  - <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Längenmaß einfügen](TechDraw_LengthDimension/de.md): Fügt ein Längenmaß hinzu.

  - <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Horizontales Maß einfügen](TechDraw_HorizontalDimension/de.md): Fügt ein horizontales Längenmaß hinzu.

  - <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Vertikales Maß einfügen](TechDraw_VerticalDimension/de.md): Fügt ein vertikales Längenmaß hinzu.

  - <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Radienmaß einfügen](TechDraw_RadiusDimension/de.md): Fügt einem Kreis oder Kreisbogen ein Radienmaß hinzu.

  - <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Durchmessermaß einfügen](TechDraw_DiameterDimension/de.md): Fügt einem Kreis oder Kreisbogen ein Durchmessermaß hinzu.

  - <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Winkelmaß einfügen](TechDraw_AngleDimension/de.md): Fügt ein Winkelmaß zwischen zwei geraden Kanten hinzu.

  - <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Winkelmaß über 3 Punkte einfügen](TechDraw_3PtAngleDimension/de.md): Fügt ein Winkelmaß unter Verwendung dreier Punkte hinzu.

  - <img alt="" src=images/TechDraw_AreaDimension.svg  style="width:32px;"> [Insert Area Annotation](TechDraw_AreaDimension/de.md): Fügt einen Hinweis mit dem Flächeninhalt zu einer Fläche hinzu. {{Version/de|1.0}}

  - <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width:32px;"> [Bogenmaß](TechDraw_ExtensionCreateLengthArc/de.md): Erstellt ein Maß für die (gestreckte) Länge eines Bogens.

  -  <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Maß für die horizontale Ausdehnung einfügen](TechDraw_HorizontalExtentDimension/de.md): fügt ein Maß für die horizontale Ausdehnung hinzu.

  - <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Maß für die vertikale Ausdehnung einfügen](TechDraw_VerticalExtentDimension/de.md): Fügt ein Maß für die vertikale Ausdehnung hinzu.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width:32px;"> [Horizontale Maßkette erstellen](TechDraw_ExtensionCreateHorizChainDimension/de.md): Erstellt ein Abfolge horizontal fluchtender Maße.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width:32px;"> [Vertikale Maßkette erstellen](TechDraw_ExtensionCreateVertChainDimension/de.md): Erstellt ein Abfolge vertikal fluchtender Maße.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width:32px;"> [Schräge Maßkette erstellen](TechDraw_ExtensionCreateObliqueChainDimension/de.md): Erstellt ein Abfolge schräger fluchtender Maße.

  -  <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width:32px;"> [Horizontale Koordinatenmaße erstellen](TechDraw_ExtensionCreateHorizCoordDimension/de.md): Erstellt eine horizontale Stufenbemaßung, d.h. mehrere horizontale Maße, die untereinander den gleichen Abstand aufweisen und die von derselben Grundlinie starten.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width:32px;"> [Vertikale Koordinatenmaße erstellen](TechDraw_ExtensionCreateVertCoordDimension/de.md): Erstellt eine vertikale Stufenbemaßung, d.h. mehrere vertikale Maße, die untereinander den gleichen Abstand aufweisen und die von derselben Grundlinie starten.

  - <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width:32px;"> [Schräge Stufenbemaßung](TechDraw_ExtensionCreateObliqueCoordDimension/de.md): Erstellt eine schräge Stufenbemaßung, d.h. mehrere schräge Maße, die untereinander den gleichen Abstand aufweisen und die von derselben Grundlinie starten.

  - <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:32px;"> [Horizontales Maß an Fase einfügen](TechDraw_ExtensionCreateHorizChamferDimension/de.md): Erstellt ein horizontales Fasenmaß mit Fasenhöhe und -winkel.

  - <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:32px;"> [Vertikales Maß an Fase einfügen](TechDraw_ExtensionCreateVertChamferDimension/de.md): Erstellt ein vertikales Fasenmaß mit Fasenhöhe und -winkel.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Hinweisfeld einfügen](TechDraw_Balloon/de.md): Fügt einer Zeichnung ein Hinweisfeld (Balloon) hinzu.

-   <img alt="" src=images/TechDraw_AxoLengthDimension.svg  style="width:32px;"> [Axonometrisches Längenmaß](TechDraw_AxoLengthDimension/de.md): Fügt ein axonometrisches Längenmaß hinzu. {{Version/de|0.21}}

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width:32px;"> [Maß zwischen Orientierungspunkten einfügen - EXPERIMENTELL](TechDraw_LandmarkDimension/de.md): Fügt ein Maß zwischen zwei Orientierungspunkten hinzu.

-   <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:32px;"> [Maßreferenzen Reparieren](TechDraw_DimensionRepair/de.md): Kann die 2D- oder 3D-Geometriereferenzen eines Maßes anpassen. {{Version/de|0.21}}

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Maß mit 3D-Geometrie verknüpfen](TechDraw_LinkDimension/de.md): Verknüpft ein vorhandenes Maß mit der 3D-Geometrie (veraltet).



### Schraffieren

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Fläche mit Muster aus einer Bilddatei schraffieren](TechDraw_Hatch/de.md): Wendet ein Schraffurmuster aus einer Datei auf eine Fläche an.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Fläche mit einer geometrischen Schraffur versehen](TechDraw_GeometricHatch/de.md): Wendet ein Schraffurmuster, das auf der Spezifikation einer AutoDesk-PAT-Schraffur basiert, auf eine Fläche an.



### Beschriftung

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Anmerkung einfügen](TechDraw_Annotation/de.md): Fügt einen einfachen Textblock als Beschriftung hinzu.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Hinweislinie zur Ansicht hinzufügen](TechDraw_LeaderLine/de.md): Fügt einer Ansicht eine Hinweislinie hinzu.

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> [Formatierten Beschriftungstext einfügen](TechDraw_RichTextAnnotation/de.md): Fügt einen formatierten Textblock als Beschriftungstext einer Hinweislinie oder einer Ansicht hinzu.

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Hilfspunkte einfügen:

  - <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Hilfspunkt hinzufügen](TechDraw_CosmeticVertex/de.md): Fügt einen Knoten hinzu, der nicht Teil der Quellgeometrie ist.

  - <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Kantenmittelpunkte hinzufügen](TechDraw_Midpoints/de.md): Fügt Hilfspunkte an den Mittenpunkten der ausgewählten Kanten hinzu.

  - <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Quadrantengrenzpunkte hinzufügen](TechDraw_Quadrants/de.md): Fügt Hilfspunkte an Viertelpunkten ausgewählter (kreisförmiger) Kanten hinzu.

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Mittellinien einfügen:

  - <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Mittellinie zu Flächen hinzufügen](TechDraw_FaceCenterLine/de.md): Fügt ausgewählten Flächen eine Mittellinie hinzu.

  - <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md): Fügt eine Mittellinie zwischen 2 Linien hinzu.

  - <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Mittellinie zwischen 2 Punkten hinzufügen](TechDraw_2PointCenterLine/de.md): Fügt eine Mittellinie zwischen 2 Punkten hinzu.

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Hilfslinie durch 2 Punkte hinzufügen](TechDraw_2PointCosmeticLine/de.md): Fügt eine Hilfslinie hinzu, die 2 Knoten verbindet

-   <img alt="" src=images/TechDraw_CosmeticCircle.svg  style="width:32px;"> [Hilfskreis hinzufügen](TechDraw_CosmeticCircle/de.md): Fügt einen Hilfskreis hinzu. {{Version/de|1.0}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:32px;"> [Liniendarstellung ändern](TechDraw_DecorateLine/de.md): Ändert das Aussehen ausgewählter Linien.

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Ausgeblendete Kanten ein-/ausblenden](TechDraw_ShowAll/de.md): Blendet als unsichtbar gekennzeichnete Linien/Kanten einer Ansicht ein bzw. (wieder) aus.

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Schweißinformationen zur Hinweislinie hinzufügen](TechDraw_WeldSymbol/de.md): Fügt Schweißspezifikationen zu einer vorhandenen Hinweislinie hinzu.

-   <img alt="" src=images/TechDraw_SurfaceFinishSymbols.svg  style="width:32px;"> [Oberflächensymbol erstellen](TechDraw_SurfaceFinishSymbols/de.md): Fügt ein Oberflächensymbol auf einem Zeichnungsblatt hinzu. {{Version/de|0.21}}

-   <img alt="" src=images/TechDraw_HoleShaftFit.svg  style="width:32px;"> [Wellen- oder Bohrungspassung hinzufügen](TechDraw_HoleShaftFit/de.md): Fügt einem Maß Bohrungs- oder Wellentoleranzen nach ISO 286 hinzu. {{Version/de|0.21}}



### Ergänzungen



### Merkmale und Änderungen 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:32px;"> [Linienmerkmale, Zeilenabstand und Längendifferenz auswählen](TechDraw_ExtensionSelectLineAttributes/de.md): Legt die Merkmale (Linienart, Linienbreite und Farbe) für neue Hilfslinien und Mittellinien fest sowie den Zeilenabstand von Maßlinien und die Längendifferenz für Längenänderungen.

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width:32px;"> [Linienmerkmale ändern](TechDraw_ExtensionChangeLineAttributes/de.md): Ändert die Merkmale (Linienart, Linienbreite und Farbe) von Hilfslinien und Mittellinien.

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Ändert die Länge von Hilfslinien oder Mittellinien:

  - <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width:32px;"> [Linie verlängern](TechDraw_ExtensionExtendLine/de.md): Verlängert eine Hilfslinie oder Mittellinie an beiden Enden.

  - <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width:32px;"> [Linie kürzen](TechDraw_ExtensionShortenLine/de.md): Verkürzt eine Hilfslinie oder Mittellinie an beiden Enden.

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width:32px;"> [Ansicht sperren/entsperren](TechDraw_ExtensionLockUnlockView/de.md): Sperrt bzw. entsperrt die Position einer Ansicht.

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width:32px;"> [Schnittansicht ausrichten](TechDraw_ExtensionPositionSectionView/de.md): Richte eine Schnittansicht rechtwinklig zur Quellansicht aus.

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Kettenmaße anordnen:

  - <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width:32px;"> [Horizontale Kettenmaße anordnen](TechDraw_ExtensionPosHorizChainDimension/de.md): Ordnet horizontale Maße fluchtend zu einer Maßkette an.

  - <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width:32px;"> [Vertikale Kettenmaße anordnen](TechDraw_ExtensionPosVertChainDimension/de.md): Ordnet vertikale Maße fluchtend zu einer Maßkette an.

  - <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width:32px;"> [Schräge Kettenmaße anordnen](TechDraw_ExtensionPosObliqueChainDimension/de.md): Ordnet schräge Maße fluchtend zu einer Maßkette an.

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Maße anordnen:

  - <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width:32px;"> [Horizontale Maße anordnen](TechDraw_ExtensionCascadeHorizDimension/de.md): Ordnet horizontale Maße mit gleichen Abständen an.

  - <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width:32px;"> [Vertikale Maße anordnen](TechDraw_ExtensionCascadeVertDimension/de.md): Ordnet vertikale Maße mit gleichen Abständen an.

  - <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width:32px;"> [Schräge Maße anordnen](TechDraw_ExtensionCascadeObliqueDimension/de.md): Ordnet schräge Maße mit gleichen Abständen an.

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width:32px;"> [Flächeninhalt der ausgewählten Flächen berechnen](TechDraw_ExtensionAreaAnnotation/de.md): Berechnet den Flächeninhalt von ausgewählten Flächen und fügt ihn als Hinweistext mit Rahmen ein.

-   <img alt="" src=images/TechDraw_ExtensionArcLengthAnnotation.svg  style="width:32px;"> [Bogenlänge der ausgewählten Kanten berechnen](TechDraw_ExtensionArcLengthAnnotation/de.md): Berechnet die Bogenlänge ausgewählter Kanten und fügt sie als Hinweistext ein. {{Version/de|1.0}}

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width:32px;"> [Formatierung anpassen](TechDraw_ExtensionCustomizeFormat/de.md): Passt die Formatierung von Hinweistexten und Maßeinträgen an. Es können Symbole für Form- und Lagetolerierung (GD&T) und andere Sonderzeichen hinzugefügt werden.



#### Mittellinien und Gewinde 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Mittellinien hinzufügen:

  - <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Kreismittellinien hinzufügen](TechDraw_ExtensionCircleCenterLines/de.md): Fügt Mittellinien zu Kreisen und Kreisbögen hinzu.

  - <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width:32px;"> [Lochkreismittellinien hinzufügen](TechDraw_ExtensionHoleCircle/de.md): Fügt die Mittellinien zu einer kreisförmigen Anordnung von Kreisen hinzu.

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Hilfslinien für Gewinde hinzufügen:

  - <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Hilfslinien für Innengewinde in Seitenansicht hinzufügen](TechDraw_ExtensionThreadHoleSide/de.md): Fügt Gewindelinien zur Seitenansicht einer Bohrung hinzu.

  - <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Hilfslinien für Innengewinde in Achsansicht hinzufügen](TechDraw_ExtensionThreadHoleBottom/de.md): Fügt eine Gewindelinie zur Ansicht einer Bohrung von oben oder unten hinzu.

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [\|Hilfslinien für Außengewinde in Seitenansicht hinzufügen](TechDraw_ExtensionThreadBoltSide/de.md): Fügt Gewindelinien zur Seitenansicht eines Außengewindes (Bolzen, Schraube oder Gewindestange) hinzu.

  - <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Hilfslinien für Außengewinde in Achsansicht hinzufügen](TechDraw_ExtensionThreadBoltBottom/de.md): Fügt eine Gewindelinie zur Ansicht eines Außengewindes (Schraube, Bolzen oder Gewindestange) von oben oder unten hinzu.

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Hilfspunkte hinzufügen:

  - <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:32px;"> [Hilfsschnittpunkte hinzufügen](TechDraw_ExtensionVertexAtIntersection/de.md): Fügt Hilfspunkte an Schnittpunkten ausgewählter Kanten hinzu.

  - <img alt="" src=images/TechDraw_CommandAddOffsetVertex.svg  style="width:32px;"> [Add an offset vertex](TechDraw_CommandAddOffsetVertex/de.md): Fügt einen Hilfspunkt mit einem bestimmten Versatz von einem ausgewählten Knoten hinzu. {{Version/de|1.0}}

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Hilfskreise und Hilfskreisbögen einfügen:

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width:32px;"> [HIlfskreis hinzufügen](TechDraw_ExtensionDrawCosmCircle/de.md): Fügt einen Hilfskreis auf Basis zweier Punkte (Mittelpunkt und Punkt auf der Kreislinie) hinzu.

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width:32px;"> [Hilfsbogen hinzufügen](TechDraw_ExtensionDrawCosmArc/de.md): Fügt einen durch drei Punkte festgelegten und gegen den Uhrzeigersinn verlaufenden Kreisbogen hinzu.

  - <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width:32px;"> [Hilfskreis über 3 Punkte hinzufügen](TechDraw_ExtensionDrawCosmCircle3Points/de.md): Fügt einen durch 3 Punkte (der Kreislinie) festgelegten Hilfskreis hinzu.

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Parallele oder rechtwinklige Hilfslinien hinzufügen:

  - <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width:32px;"> [Parallele Hilfslinie hinzufügen](TechDraw_ExtensionLineParallel/de.md): Fügt eine Hilfslinie parallel zu einer anderen Linie durch einen Knotenpunkt verlaufend hinzu.

  - <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width:32px;"> [Rechtwinklige Hilfslinie hinzufügen](TechDraw_ExtensionLinePerpendicular/de.md): Fügt eine Hilfslinie rechtwinklig zu einer anderen Linie durch einen Knotenpunkt verlaufend hinzu.



#### Maßeinträge

Einige der in den Ergänzungen enthaltenen Werkzeuge für Maßeinträge sind weiter oben unter [Maße](#Maße.md) gelistet.

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Präfixsymbole einfügen:

  - <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:32px;"> [\'⌀\'-Symbol einfügen](TechDraw_ExtensionInsertDiameter/de.md): Fügt ein Durchmessersymbol (⌀) am Anfang des Maßtextes ein.

  - <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width:32px;"> [\'□\'-Symbol einfügen](TechDraw_ExtensionInsertSquare/de.md): Fügt ein Vierkantsymbol (□) am Anfang des Maßtextes ein.

  - <img alt="" src=images/TechDraw_ExtensionInsertRepetition.svg  style="width:32px;"> [Anzahl-Präfix (\'n×\') einfügen](TechDraw_ExtensionInsertRepetition.md): Fügt einen Multiplikator am Anfang des Maßtextes ein, der angibt, wie oft das zu diesem Maß gehörende Formelement in der Ansicht vorkommt. {{Version/de|1.0}}

  - <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width:32px;"> [Präfixsymbol entfernen](TechDraw_ExtensionRemovePrefixChar/de.md): Entfernt alle Symbole am Anfang des Maßtextes.

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Anzahl der Dezimalstellen ändern:

  - <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width:32px;"> [Dezimalstellenanzahl erhöhen](TechDraw_ExtensionIncreaseDecimal/de.md): Erhöht die Anzahl der Dezimalstellen der Maßzahl.

  - <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width:32px;"> [Dezimalstellenanzahl verringern](TechDraw_ExtensionDecreaseDecimal/de.md): verringert die Anzahl der Dezimalstellen der Maßzahl.



### Sonstiges

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Hilfsobjekt entfernen](TechDraw_CosmeticEraser/de.md): Entfernt Hilfsobjekte von einem Zeichnungsblatt.



### Veraltete Werkzeuge 

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Ansicht zu Ausschnittsgruppe hinzufügen](TechDraw_ClipGroupAdd/de.md): Fügt eine vorhandene Ansicht zu einer Ausschnittsgruppe hinzu. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Ansicht aus Ausschnittsgruppe entfernen](TechDraw_ClipGroupRemove/de.md): Entfernt eine Ansicht aus einer Ausschnittsgruppe. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width:32px;"> [Ansicht verschieben](TechDraw_MoveView/de.md): Verschiebt eine Ansicht samt Inhalt auf ein anderes Blatt. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.



## Zusatzfunktionen

-   [Liniengruppe](TechDraw_LineGroup/de.md): um das Aussehen verschiedener Linientypen zu steuern.
-   [Vorlagen](TechDraw_Templates/de.md): Die definierten Standardvorlagen für die Zeichnungsseiten.
-   [Schraffur](TechDraw_Hatching/de.md): Erklärung der verschiedenen Schraffurtechniken.
-   [Geometrische Bemaßung und Tolerierung](TechDraw_Geometric_dimensioning_and_tolerancing/de.md) (GD&T): Erklärung zur Form- und Lagetolerierung.



## Einstellungen

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Einstellungen](TechDraw_Preferences/de.md): Einstellungen für die Standardwerte des Zeichnungsblattes wie Projektionsmethode, Farben, Textgrößen und Linienarten.



## Skripten

Die TechDraw-Werkzeuge können in [Makros](Macros/de.md) oder von der [Python](Python/de.md)-Konsole aus verwendet werden. Für weitere Informationen siehe:

-   [Autogenerated API documentation](https://freecad.github.io/SourceDoc/)
-   [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md)
-   [Editierbare Textfelder](TechDraw_PageTemplate/de#Editierbare_Textfelder.md)



## Einschränkungen

-   TechDraw-Objekte sollten nicht in der [Baumansicht](Tree_view/de.md) kopiert und eingefügt werden, da dies im Allgemeinen nicht gut funktioniert.
-   TechDraw-Objekte sollten nicht mit der Maus in die (der?) [Baumansicht](Tree_view/de.md) gezogen werden.



## Anleitungen

-   [TechDraw Grundlagentutorium](Basic_TechDraw_Tutorial/de.md): Einführung in die Zeichnungserstellung mit dem Arbeitsbereich TechDraw.
-   [Erstellen einer neuen Vorlage](TechDraw_TemplateHowTo/de.md): Anweisungen für die Erstellung einer neuen Seitenvorlage mit Inkscape zur Verwendung im Arbeitsbereich TechDraw.
-   [TechDraw Vorlagengenerator](TechDraw_TemplateGenerator/de.md): Anleitung zum Erstellen eines Makros für die Erstellung einer einfachen Vorlage.

:   Ein \"paar\" Zeilen Kode, die ein Werkzeug ähnlich dem [Makro TemplateHelper](Macro_TemplateHelper/de.md) ergeben.

-   [Maßeintrag für Bohrungswinkel](Measurement_Of_Angles_On_Holes/de.md): Anweisungen zum Hinzufügen von Mittellinien und der nachfolgenden Eintragung der Neigungswinkel von Bohrungen.
-   [Verschiedenes](TechDraw_HowTo_Page/de.md): Anweisungen für verschiedene Einstellungen wie Mittelpunktsmarkierungen usw.
-   [TechDraw Pitch Circle Tutorial](TechDraw_Pitch_Circle_Tutorial.md): Anweisungen zum Hinzufügen eines Teilkreises.

Video-Anleitungen von sliptonic

-   TechDraw Arbeitsbereich [Part 1 (Grundlagen)](https://www.youtube.com/watch?v=7LbOmSGW9F0),[Part 2 (Abmessungen)](https://www.youtube.com/watch?v=z3w84RfvqaE),[Part 3 (Multiview)](https://www.youtube.com/watch?v=uNjXg-m38aI).
-   TechDraw Arbeitsbereich [Part 4 (Abschnitt und Detail)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Vorlagen anpassen)](https://www.youtube.com/watch?v=kcmdJ7xa7gg).



## Entwicklung

Wie sieht die Zukunft von TechDraw aus? Siehe [TechDraw Roadmap](TechDraw_Roadmap.md), um mehr zu erfahren.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [TechDraw](Category_TechDraw.md) > TechDraw Workbench/de
