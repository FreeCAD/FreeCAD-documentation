# BIM Workbench/de
**In v1.0 wurden die Arbeitsbereiche BIM, Native-IFC und [Arch](Arch_Workbench/de.md) im integrierten Arbeitsbereich BIM zusammengefasst.<br>
Diese Seite wurde für diese Version aktualisiert.**

<img alt="Symbol des Arbeitsbereichs BIM" src=images/Workbench_BIM.svg  style="width:128px;">






## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/de.md) stellt einen modernen Arbeitsablauf für das Modellieren von Bauwerksdaten (siehe [Bauwerksdatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling) oder engl. [Building Information Modelling](https://en.wikipedia.org/wiki/Building_information_modeling), kurz BIM) in FreeCAD zur Verfügung, mit vollständig parametrischen Objekten wie Wänden, Balken, Dächern, Fenstern, Treppen, Rohrleitungen und Möbeln. Er unterstützt [Industry Foundation Classes](Arch_IFC/de.md) (IFC-Dateien), und die 2D-Zeichnungserstellung in Zusammenarbeit mit dem Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [TechDraw](TechDraw_Workbench/de.md).

Der Arbeitsbereich BIM importiert alle Werkzeuge des Arbeitsbereichs <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md), weil er dessen 2D-Objekte zur Erstellung von parametrischen 3D-Objekten verwendet. Er kann auch Festkörperformen verwenden, die in anderen Arbeitsbereichen wie <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) und <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) erstellt wurden.

Siehe [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) (engl.), ein schneller Überblick für Benutzer anderer BIM-Anwendungen.

Die Entwickler von Draft und BIM arbeiten auch mit der größeren [OSArch-Gemeinschaft](https://osarch.org) zusammen, mit dem ultimativen Ziel, den Entwurf von Gebäuden durch den Einsatz völlig freier Software zu verbessern.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">



## Erste Schritte 

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Wird der Arbeitsbereich BIM zum ersten Mal gestartet, wird ein Begrüßungsdialog angezeigt, der einen schnellen Überblick über die Funktionsweise des Arbeitsbereichs gibt und es dem Benutzer ermöglicht, eine [anwendungsinterne Anleitung](BIM_ingame_tutorial/de.md) zu starten. Der Begrüßungsdialog steht auch über das Menü **Hilfe** zur Verfügung. Wenn der Begrüßungsbildschirm durch Klicken auf OK geschlossen wird, wird der [BIM-Setup-Dialog](BIM_Setup/de.md) angezeigt, der es dem Benutzer ermöglicht, schnell einige der häufigsten BIM-bezogenen Einstellungen von FreeCAD vorzunehmen, ohne durch die vollständigen [FreeCAD-Einstellungsseiten](Preferences_Editor/de.md) blättern zu müssen.

Das Werkzeug [BIM Einrichten](BIM_Setup/de.md) ermöglicht dem Anwender ein BIM-Projekt schnell einzurichten, indem er einige grundlegende Informationen über das Projekt ausfüllt. Es können dann z. B. die verschiedenen 2D-Zeichenwerkzeuge verwendet werden, um Leit- und Basislinien zu skizzieren, und dann die verschiedenen 3D-Modellierungswerkzeuge, um daraus automatisch 3D-BIM-Objekte zu erstellen. Eine Linie kann z. B. zu einer Wand werden, indem sie einfach ausgewählt und die Schaltfläche [Wand](Arch_Wall/de.md) gedrückt wird.

Übliche Gebäudeelemente wie [Wände](Arch_Wall/de.md) oder [Stützen](BIM_Column/de.md) werden einfach durch Drücken der entsprechenden Schaltfläche in der Symbolleiste und Auswählen der Punkte in der 3D-Ansicht erstellt. Sie können verschoben, gedreht oder bearbeitet werden, sobald sie erstellt wurden. Die meisten BIM-Elemente werden auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) erstellt, daher erfordert ein typischer Arbeitsablauf, zuerst eine Arbeitsebene zu positionieren und dann ein BIM-Element zu erstellen. Komplexere Elemente können erstellt werden, indem zuerst 2D-Elemente erstellt werden und anschließend eins der BIM-Werkzeug eingesetzt wird, um sie in das gewünschten Element umzuwandeln.

Elemente von Gebäudeprojekten können geordnet werden, indem [Grundstücke](Arch_Site/de.md), [Gebäude](Arch_Building/de.md) und [Stockwerke](Arch_BuildingPart/de.md) verwendet werden, um nachzuahmen, was andere BIM-Anwendungen üblicherweise machen. In FreeCAD sind solche Strukturen jedoch nicht zwingend vorgeschrieben und jeder kann ohne Einschränkung die eigenen Modelle so ordnen, wie es passend erscheint, z.B. mit [Gruppen](Std_Group/de.md).

2D-Zeichnungen können von einem Modell abgeleitet werden, die Grundriss, Schnitt und Aufriss darstellen. Zum Erstellen solcher Zeichnungen werden [Schnittebenen](Arch_SectionPlane/de.md) im Modell positioniert, die anzeigen, wo es geschnitten wird oder wie die Blickrichtung verläuft. Sobald die Schnittebenen positioniert sind, stehen die beiden folgenden Methoden zur Verfügung:

1.  Im Dokument mit [Form in 2D-Ansicht](Draft_Shape2DView/de.md) projizierte Ansichten erstellen, anschließend alle benötigten Beschriftungen wie Texte und Maße hinzufügen und schließlich alle Ansichten auf einem Zeichnungsblatt anordnen. Dies ist der empfohlene Weg, da er mehr Flexibilität bietet.
2.  Eine Ansicht direkt aus einer Schnittebene auf einem Zeichnungsblatt erstellen. Dann müssen alle erforderlichen 2D-Beschriftungen entweder zur Schnittebene hinzugefügt werden oder direkt auf dem Zeichnungsblatt erfolgen. Dies ist weniger flexibel.

Schließlich können mit den Werkzeug [Schedule](Arch_Schedule/de.md) Quantities-Schedules erstellt werden

Wenn man mit einer anderen BIM-Anwendung vertraut ist, sollte man unsere [BIM Anwendungskompatibilitätstabelle](BIM_application_compatibility_table/de.md) lesen, um sich zu orientieren, wenn man mit FreeCAD beginnt.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

Die [Anwendungsinterne Anleitung](BIM_ingame_tutorial/de.md) ist ein einfacher Weg, um schnell mit dem Arbeitsbereich BIM zurechtzukommen.



## Werkzeuge

Der Arbeitsbereich BIM stellt Werkzeuge aus mehreren anderen Arbeitsbereichen, hauptsächlich [Draft](Draft_Workbench/de.md) und [Part](Part_Workbench/de.md) zusammen, die grob in lokale Kategorien umverteilt werden.

Außerdem werden, falls solche [Addons](External_workbenches/de.md) installiert wurden, Werkzeuge von [Reinforcement](Reinforcement_Workbench/de.md) (zusätzliche Werkzeuge für Bewehrungsstäbe), [Fasteners](Fasteners_Workbench/de.md) (Verbindungselemente wie Bolzen, Schrauben usw.), [Flamingo/Dodo](Flamingo_Workbench/de.md) (Metallstruktur- und Rohrleitungswerkzeuge) und [Parts-Library](Parts_Library_Workbench/de.md) (Teilebibliothek) automatisch im Arbeitsbereich BIM integriert.

Der Arbeitsbereich BIM fügt auch eine Reihe von Elementen in der **Statusleiste** von FreeCAD hinzu sowie einige **Kontextmenüelemente**, die durch einen Rechtsklick in der 3D-Ansicht oder in der Baumansicht zu erreichen sind.



### 2D-Zeichnen 

2D-Objekte werden häufig als Zeichenhilfen oder zum Zeichnen von Grundlinien und Profilen verwendet, auf denen BIM-Objekte aufgebaut werden. Sie können auch zum Zeichnen von Symbolen und zur Beschriftung im Modell eingesetzt werden. Anders als Skizzen, die ihr eigenes Koordinatensystem verwenden, werden 2D-Objekte auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) gezeichnet.

-   <img alt="" src=images/BIM_Sketch.svg‎‎  style="width:32px;"> [Skizze](BIM_Sketch/de.md): Erstellt eine neue Skizze und wechselt in den Skizzenbearbeitungsmodus. Skizzen sind weiterentwickelte 2D-Objekte mit Unterstützung von Randbedingungen.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linie](Draft_Line/de.md): Erstellt eine gerade Linie.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polylinie](Draft_Wire/de.md): Erstellt eine Polylinie (auch Linienzug oder Draht genannt), eine Folge von mehreren miteinander verbundenen Liniensegmenten.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Kreis](Draft_Circle/de.md): Erstellt einen Kreis aus Mittelpunkt und Radius.

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Bogen](Draft_Arc/de.md): Erstellt einen Kreisbogen aus einem Mittelpunkt, einem Radius, einem Startwinkel und einem Öffnungswinkel.

  - <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Bogen durch 3 Punkte](Draft_Arc_3Points/de.md): Erstellt einen Kreisbogen aus drei Punkten, die seinen Umfang festlegen.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Verrundung](Draft_Fillet/de.md): Erstellt eine Verrundung, eine abgerundete Ecke, oder eine Fase, eine gerade Kante, zwischen zwei [Draft-Linien](Draft_Line/de.md).

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/de.md): Erstellt eine Ellipse aus zwei Punkten, die ein Rechteck definieren, in das die Ellipse hineinpasst.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Vieleck](Draft_Polygon/de.md): Erstellt ein regelmäßiges Vieleck aus Mittelpunkt und Radius.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rechteck](Draft_Rectangle/de.md): Erstellt ein Rechteck aus zwei Punkten.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-Spline](Draft_BSpline/de.md): Erstellt eine B-Spline-Kurve aus mehreren Punkten.

  - <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézierkurve](Draft_BezCurve/de.md): Erstellt eine Bézierkurve aus mehreren Punkten.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Kubische Bézierkurve](Draft_CubicBezCurve/de.md): Erstellt eine Bézierkurve dritten Grades.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/de.md): Erstellt einen einfachen Punkt.



### 3D/BIM

3D- und BIM-Objekte sind die Elemente der realen Welt, aus denen sich ein BIM-Projekt zusammensetzt.

-   <img alt="" src=images/BIM_Project.svg  style="width:32px;"> [Projekt](BIM_Project/de.md): Erstellt ein IFC-Projekt, das die ausgewählten Objekte enthält.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Grundstück](Arch_Site/de.md): Erstellt ein Grundstück, das die ausgewählten Objekte enthält.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Gebäude](Arch_Building/de.md): Erstellt ein Gebäude, das die ausgewählten Objekte enthält.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Stockwerk](Arch_Floor/de.md): Erstellt ein Stockwerk, das die ausgewählten Objekte enthält.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Raum](Arch_Space/de.md): Erstellt ein Raumobjekt.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wand](Arch_Wall/de.md): Erstellt eine Wand von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Vorhangwand](Arch_CurtainWall/de.md): Erstellt eine Vorhangwand von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Stütze](BIM_Column/de.md): Erstellt ein vertikales [Strukturelement](Arch_Structure/de.md) an einem bestimmten Punkt, optional unter Verwendung eines ausgewählten Objekts als Profil.

-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Balken](BIM_Beam/de.md): Erstellt ein horizontales [Strukturelement](Arch_Structure/de.md) zwischen zwei Punkten, optional unter Verwendung eines ausgewählten Objekts als Profil.

-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Platte](BIM_Slab/de.md): Erstellt ein flaches [Strukturelement](Arch_Structure/de.md), indem ein ausgewähltes flaches Objekt extrudiert wird.

-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Tür](BIM_Door/de.md): Erstellt ein [Fensterobjekt](Arch_Window/de.md) unter Verwendung von Türvorgaben.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenster](Arch_Window/de.md): Erstellt ein Fenster von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Rohr](Arch_Pipe/de.md): Erstellt ein Rohr.

-   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Rohrverbinder](Arch_PipeConnector/de.md): Erstellt eine Bogen- oder T-Verbindung zwischen 2 bzw 3 ausgewählten Rohren.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Treppe](Arch_Stairs/de.md): Erstellt eine Treppe.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/de.md): Erstellt ein geneigtes Dach aus einer ausgewählten Polylinie.

-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Platte](Arch_Panel/de.md): Erstellt ein Plattenobjekt aus einem ausgewählten 2D-Objekt.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Rahmen](Arch_Frame/de.md): Erstellt ein Rahmenobjekt aus einem ausgewählten Layout.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Zaun](Arch_Fence/de.md): Erstellt ein Zaunobjekt aus einem ausgewählten Pfosten und Pfad.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Fachwerkträger](Arch_Truss/de.md): Erstellt einen Fachwerkträger aus einer ausgewählten Linie oder von Grund auf.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Ausstattung](Arch_Equipment/de.md): Erstellt ein Ausstattungs- oder Möbelobjekt.

-   Reinforcement-Werkzeuge:

:   Diese Werkzeuge, außer dem ersten, stehen nur zur Verfügung, wenn der Arbeitsbereich [Reinforcement](Reinforcement_Workbench/de.md) installiert wurde.

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Bewehrung](Arch_Rebar/de.md): Erstellt unter Verwendung einer Skizze ein individuell angepasstes Bewehrungselement in einem ausgewählten Strukturelement.

  - <img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Gerade Bewehrung](Reinforcement_StraightRebar/de.md): Erstellt einen geraden Bewehrungsstab in einem ausgewählten Strukturelement.

  - <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [U-förmige Bewehrung](Reinforcement_UShapeRebar/de.md): Erstellt einen U-förmigen Bewehrungsstab in einem ausgewählten Strukturelement.

  - <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [L-förmige Bewehrung](Reinforcement_LShapeRebar/de.md): Erstellt einen L-förmigen Bewehrungsstab in einem ausgewählten Strukturelement

  - <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Bewehrungsbügel](Reinforcement_StirrupRebar/de.md): Erstellt einen Bewehrungsbügel in einem ausgewählten Strukturelement.

  - <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Abgesetzte Bewehrung](Reinforcement_BentShapeRebar/de.md): Erstellt einen Bewehrungsstab mit Absatz in einem ausgewählten Strukturelement.

  - <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Wendelbewehrung](Reinforcement_HelicalRebar/de.md): Erstellt eine Wendelbewehrung in einem ausgewählten Strukturelement.

  - <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Stützenbewehrung](Reinforcement_ColumnRebars/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einer ausgewählten Stütze.

  - <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Balkenbewehrung](Arch_Rebar_BeamReinforcement/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einem ausgewählten Balken.

  - <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Plattenbewehrung](Reinforcement_SlabRebars/de.md): Erstellt Bewehrungsstäbe in einer ausgewählten Platte.

  - <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Fundamentbewehrung](Arch_Rebar_Footing_Reinforcement/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einem ausgewählten Fundament.

-   Allgemeine 3D-Werkzeuge:

:   Diese Werkzeuge erstellen generische 3D-Objekte, die in BIM-Komponenten umgewandelt oder verwendet werden können.

  - <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/de.md): Erstellt ein parametrisches 2D-Profil.

  - <img alt="" src=images/BIM_Box.svg  style="width:32px;"> [Quader](BIM_Box/de.md): Erstellt einen Quader durch grafische Angabe seiner Abmessungen.

  - <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Formgenerator](Part_Builder/de.md): Erstellt komplexere Formen aus verschiedenen geometrischen Primitiven.

  - <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;">[Flächenbinder](Draft_Facebinder/de.md): Erstellt ein Oberflächenobjekt aus ausgewählten Flächen.

  - <img alt="" src=images/BIM_Library.svg  style="width:32px;"> [Objektbibliothek](BIM_Library/de.md): Fügt ein Ausrüstungs- oder Möbelobjekt ein. Erfordert den Arbeitsbereich [Parts Library](Parts_Library/de.md).

  - <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Komponente](Arch_Component/de.md): Erstellt eine nicht-parametrische Arch-Komponente.

  - <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Externe Referenz](Arch_Reference/de.md): Verknüpft Objekte aus einer anderen FreeCAD-Datei mit dem aktuellen Dokument.



### Anmerkung

Anmerkungen sind visuelle Hilfsobjekte, die in einem Modell platziert werden können. Sie können eingesetzt werden, wenn ein Modell direkt in ein 2D-Format wie [DXF](Draft_DXF/de.md) exportiert werden soll, oder sie werden bei der Erstellung von 2D-Ansichten des Modells mit dem Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) wiederverwendet.

-   <img alt="" src=images/BIM_Text.svg  style="width:32px;"> [Text](BIM_Text/de.md): Erstellt einen 2D-Text in einem Dokument oder auf einem TechDraw-Zeichnungsblatt.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Textform](Draft_ShapeString/de.md): Erstellt eine Verbundform, die eine Textzeichenfolge darstellt.

-   <img alt="" src=images/BIM_DimensionAligned.svg  style="width:32px;"> [Ausgerichtetes Maß](BIM_DimensionAligned/de.md): Erstellt ein Maß, das zwischen zwei Punkten oder entlang einer ausgewählten Kante ausgerichtet wird.

-   <img alt="" src=images/BIM_DimensionHorizontal.svg  style="width:32px;"> [Horizontales Maß](BIM_DimensionHorizontal/de.md): Erstellt ein horizontales Maß zwischen zwei Punkten oder von einer ausgewählten Kante.

-   <img alt="" src=images/BIM_DimensionVertical.svg  style="width:32px;"> [Vertikales Maß](BIM_DimensionVertical/de.md): Erstellt ein vertikales Maß zwischen zwei Punkten oder von einer ausgewählten Kante.

-   <img alt="" src=images/BIM_Leader.svg  style="width:32px;"> [Hinweislinie](BIM_Leader/de.md): Erstellt einen Linienzug mit zwei Abschnitten und einer Pfeilsymbol ein seinem Ende, der als Hinweislinie im Zusammenhang mit einem [Text](BIM_Text/de.md) eingesetzt wird.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Hinweis](Draft_Label/de.md): erstellt einen mehrzeiligen Text an einer zweiteiligen Hinweislinie mit Pfeilspitze.

-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Achse](Arch_Axis/de.md): Fügt eine eindimensionale Anordnung von Achsen hinzu.

-   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [AchsenSystem](Arch_AxisSystem/de.md): Fügt ein Achsensystem hinzu, das aus mehreren Achsen besteht.

-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Raster](Arch_Grid/de.md): Fügt ein gitterartiges Objekt hinzu.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Schnittebene](Arch_SectionPlane/de.md): Fügt eine Schnittebene (section plane object) hinzu.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Schraffur](Draft_Hatch/de.md): erstellt Schraffuren auf den ebenen Flächen eines ausgewählten Objekts.

-   <img alt="" src=images/BIM_TDPage.svg  style="width:32px;"> [Zeichnungsblatt](BIM_TDPage/de.md): Erstellt ein [TechDraw-Zeichnungsblatt](TechDraw_PageTemplate/de.md) aus einer SVG-Vorlagendatei.

-   <img alt="" src=images/BIM_TDView.svg  style="width:32px;"> [Ansicht](BIM_TDView/de.md): Erstellt eine Ansicht auf ein oder mehrere ausgewählte Objekte wie eine [Schnittebene](Arch_SectionPlane/de.md) oder einer Gruppe, die die unterschiedlichen Elemente einer 2D-Ansicht enthält.

-   <img alt="" src=images/BIM_Shape2DView.svg  style="width:32px;"> [Formbasierte Ansicht](BIM_Shape2DView/de.md): Erstellt eine projizierte 2D-Ansicht aus einem ausgewählten Objekt, wie z. B. einer [Schnittebene](Arch_SectionPlane/de.md) oder einem [Stockwerk](Arch_Floor/de.md).



### Einrasten

Dieses Menü enthält die Werkzeuge unter [Draft-Einrasten](Draft_Snap/de.md) sowie die folgenden Werkzeuge:

-   <img alt="" src=images/BIM_SetWPTop.svg  style="width:32px;"> [Arbeitsebene Draufsicht](BIM_SetWPTop/de.md): Legt die Arbeitsebene auf die globale XY-Ebene (Draufsicht).

-   <img alt="" src=images/BIM_SetWPFront.svg  style="width:32px;"> [Arbeitsebene Vorderansicht](BIM_SetWPFront/de.md): Legt die Arbeitsebene auf die globale XZ-Ebene (Vorderansicht).

-   <img alt="" src=images/BIM_SetWPSide.svg  style="width:32px;"> [Arbeitsebene Seitenansicht](BIM_SetWPSide/de.md): Legt die Arbeitsebene auf die globale YZ-Ebene (Seitenansicht).



### Modifitieren

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Verschieben](Draft_Move/de.md): Verschiebt oder kopiert ausgewählte Objekte von einem Punkt zum anderen.

-   <img alt="" src=images/BIM_Copy.svg  style="width:32px;"> [Kopieren](BIM_Copy/de.md): Kopiert ausgewählte Objekte von einem Punkt zum anderen.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Drehen](Draft_Rotate/de.md): Dreht oder kopiert ausgewählte Objekte um einen Mittelpunkt um einen bestimmten Winkel.

-   <img alt="" src=images/BIM_Clone.svg  style="width:32px;"> [Klon](BIM_Clone/de.md): Klont ausgewählte Objekte.

-   <img alt="" src=images/BIM_SimpleCopy.svg  style="width:32px;"> [Einfache Kopie erstellen](BIM_SimpleCopy/de.md): Erstellt eine nichtparametrische Kopie eines ausgewählten Objekts. Dies ist das gleiche Werkzeug wie [Part SimpleCopy](Part_SimpleCopy/de.md).

-   <img alt="" src=images/BIM_Compound.svg  style="width:32px;"> [Teileverbindung](BIM_Compound/de.md): Erstellt eine Verbindung aus ausgewählten Objekten. Dies ist das gleiche Werkzeug wie [Teileverbindung](Part_Compound/de.md).

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset/de.md): Verschiebt jedes Segment eines ausgewählten Objekts über eine bestimmte Distanz oder erstellt eine versetzte Kopie des ausgewählten Objekts

-   <img alt="" src=images/BIM_Offset2D.svg  style="width:32px;"> [2D Offset](BIM_Offset2D/de.md): Erstellt einen parallelen Linienzug in einem bestimmten Abstand vom Original oder vergrößert/verkleinert eine ebene Fläche (parametrische Version). Dies ist das gleiche Werkzeug wie [Part Offset2D](Part_Offset2D/de.md).

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex/de.md): Trimmt oder erweitert ein ausgewähltes Objekt.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join/de.md): Fügt [Entwurfslinien](Draft_Line/de.md) und [Entwurfsdrähte](Draft_Wire/de.md) zu einem einzigen Linienzug zusammen.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Teilen](Draft_Split/de.md): Teilt eine [Entwurfslinie](Draft_Line.md) oder einen [Linienzug](Draft_Wire.md) an einem angegebenen Punkt oder einer angegebenen Kante.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale/de.md): Skaliert oder kopiert ausgewählte Objekte um einen Basispunkt.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch/de.md): Streckt Objekte durch Verschieben ausgewählter Punkte.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Entwurf zu Skizze](Draft_Draft2Sketch/de.md): Wandelt Entwurfsobjekte in [Sketcher-Skizzen](Sketcher_NewSketch/de.md) um und umgekehrt.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade/de.md): Aktualisiert ausgewählte Objekte.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade/de.md): Stuft ausgewählte Objekte herab.

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Komponente hinzufügen](Arch_Add/de.md): Fügt einer Komponente Objekte hinzu.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Komponente entfernen](Arch_Remove/de.md): Subtrahiert oder entfernt Objekte aus einer Komponente.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Array](Draft_OrthoArray/de.md): Erstellt ein orthogonales Array aus einem ausgewählten Objekt. Es kann optional ein [Link](App_Link/de.md)-Array erstellen.

-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Pfadarray](Draft_PathArray/de.md): Erstellt ein Array aus einem ausgewählten Objekt, indem Kopien entlang eines Pfads platziert werden.

-   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar-Array](Draft_PolarArray/de.md): Erstellt ein Array aus einem ausgewählten Objekt, indem Kopien entlang eines Umfangs platziert werden. Es kann optional ein [Link](App_Link/de.md)-Array erstellen.

-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Punkt-Array](Draft_PointArray/de.md): Erstellt ein Array aus einem ausgewählten Objekt, indem Kopien an den Punkten einer Punktverbindung platziert werden.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Mit Ebene schneiden](Arch_CutPlane/de.md): Schneidet ein Objekt entlang einer Ebene.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Spiegel](Draft_Mirror/de.md): Erstellt gespiegelte Kopien von ausgewählten Objekten.

-   <img alt="" src=images/BIM_Extrude.svg  style="width:32px;"> [Extrude](BIM_Extrude/de.md): Extrudiert planare Flächen eines Objekts. Dies ist das gleiche Werkzeug wie [Teile-Extrudieren](Part_Extrude/de.md).

-   <img alt="" src=images/BIM_Cut.svg  style="width:32px;"> [Differenz](BIM_Cut/de.md): Subtrahiert ein Objekt von einem anderen. Dies ist das gleiche Werkzeug wie [Part Cut](Part_Cut/de.md).

-   <img alt="" src=images/BIM_Fuse.svg  style="width:32px;"> [Union](BIM_Fuse/de.md): Verbindet zwei Objekte. Dies ist das gleiche Werkzeug wie [Part Fuse](Part_Fuse/de.md).

-   <img alt="" src=images/BIM_Common.svg  style="width:32px;"> [Schnittpunkt](BIM_Common/de.md): Extrahiert den gemeinsamen Teil zweier Objekte. Dies ist das gleiche Werkzeug wie [Teil gemeinsam](Part_Common/de.md).

### Manage

-   <img alt="" src=images/BIM_Setup.svg  style="width:32px;"> [BIM-Setup\...](BIM_Setup/de.md): Konfiguriert einige der am häufigsten für BIM verwendeten FreeCAD-Einstellungen.

-   <img alt="" src=images/BIM_Views.svg  style="width:32px;"> [Ansichtenmanager](BIM_Views/de.md): Verwalte die verschiedenen Ansichten und Ebenen deines Projekts.

-   <img alt="" src=images/BIM_ProjectManager.svg  style="width:32px;"> [Projekt verwalten](BIM_ProjectManager/de.md): Ermöglicht das Erstellen einiger grundlegender Objekte wie einer [Site](Arch_Site/de.md), eines [Gebäudes](Arch_Building/de.md) und von [Achsen](Arch_Axis/de.md) durch Ausfüllen der grundlegenden Projektinformationen.

-   <img alt="" src=images/BIM_Windows.svg  style="width:32px;"> [Türen und Fenster verwalten](BIM_Windows/de.md): Verwalte die Türen und Fenster deines Projekts.

-   <img alt="" src=images/BIM_IfcElements.svg  style="width:32px;"> [IFC-Elemente verwalten](BIM_IfcElements/de.md): Verwalte, wie die verschiedenen Elemente deines Projekts nach IFC exportiert werden.

-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [IFC-Mengen verwalten](BIM_IfcQuantities/de.md): Verwalte, wie die Mengen deiner Objekte explizit nach IFC exportiert werden

-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [IFC-Eigenschaften verwalten\...](BIM_IfcProperties/de.md): Verwalte die IFC-Eigenschaften, die jedem deiner Objekte zugeordnet sind.

-   <img alt="" src=images/BIM_Classification.svg  style="width:32px;"> [Klassifizierung verwalten\...](BIM_Classification/de.md): Verwalte, wie Objekte und Materialien deines Projekts mit Klassifizierungssystemen wie [Uniclass](https://en.wikipedia.org/wiki/Uniclass) in Beziehung stehen.

-   <img alt="" src=images/BIM_Layers.svg  style="width:32px;"> [Ebenen verwalten](BIM_Layers/de.md): Verwalte die Ebenen deines Dokuments.

-   <img alt="" src=images/BIM_Material.svg  style="width:32px;"> [Material](BIM_Material/de.md): Verwaltet [Materialien](Arch_SetMaterial/de.md) oder [Multimaterialien](Arch_MultiMaterial/de.md) ausgewählter Objekte

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Zeitplan](Arch_Schedule/de.md): Erstellt verschiedene Arten von Zeitplänen.

-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Preflight-Prüfungen](BIM_Preflight/de.md): Führe vor dem Exportieren nach IFC verschiedene Prüfungen an deinem Modell durch.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotationsstile](Draft_AnnotationStyleEditor/de.md): Ermöglicht dir, Stile zu definieren, die die visuellen Eigenschaften von annotationsähnlichen Objekten beeinflussen.



### Dienstprogramme

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Untere Bedienfelder umschalten](BIM_TogglePanels/de.md): Zeigt oder verbirgt Ausgabefenster (die Berichtsansicht und die Python-Konsole).

-   <img alt="" src=images/BIM_Trash.svg  style="width:32px;"> [In den Papierkorb verschieben](BIM_Trash/de.md): Verschiebt ausgewählte Objekte in eine Papierkorbgruppe, die bei Bedarf erstellt wird.

-   <img alt="" src=images/BIM_WPView.svg  style="width:32px;"> [Arbeitsebenenansicht](BIM_WPView/de.md): Richtet die Kamera auf die aktuelle Arbeitsebene aus

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Gruppe auswählen](Draft_SelectGroup/de.md): Wählt den Inhalt von [Std-Gruppen](Std_Group.md) oder gruppenähnlichen [Arch](Arch_Workbench/de.md)-Objekten aus.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Neigung festlegen](Draft_Slope/de.md): neigt ausgewählte [Draft-Linien](Draft_Line/de.md) oder [Draft-Linienzüge](Draft_Wire/de.md), indem die Werte der Z-Koordinaten aller Punkte nach dem ersten erhöht oder verringert werden.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Arbeitsebenen-Proxy erstellen](Draft_WorkingPlaneProxy/de.md): Erstellt einen Arbeitsebenen-Proxy zum Speichern der aktuellen [Entwurfsarbeitsebene](Draft_SelectPlane/de.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Zur Konstruktionsgruppe hinzufügen](Draft_AddConstruction/de.md): Verschiebt Objekte in die [Entwurfs-Konstruktionsgruppe](Draft_ToggleConstructionMode/de.md).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Split Mesh](Arch_SplitMesh/de.md): Teilt ein ausgewähltes Mesh in einzelne Komponenten auf.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Mesh to Shape](Arch_MeshToShape/de.md): Wandelt ein Mesh in eine Form um und vereinheitlicht koplanare Flächen.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Nicht-mannigfaltige Netze auswählen](Arch_SelectNonSolidMeshes/de.md): Wählt alle nicht-mannigfaltigen Netze aus der aktuellen Auswahl oder aus dem Dokument aus.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Form aus Arch entfernen](Arch_RemoveShape/de.md): Macht ein kubisches, formbasiertes Arch-Objekt vollständig parametrisch.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Löcher schließen](Arch_CloseHoles/de.md): Schließt Löcher in einem ausgewählten formbasierten Objekt.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Wände zusammenführen](Arch_MergeWalls/de.md): Führt Wände zusammen.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check/de.md): Überprüfen, ob die ausgewählten Objekte fest sind und keine Defekte aufweisen.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [IFC B-rep-Flag umschalten](Arch_ToggleIfcBrepFlag/de.md): Erzwingt den Export eines ausgewählten Objekts als [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Unterkomponenten umschalten](Arch_ToggleSubs/de.md): Zeigt oder verbirgt die Unterkomponenten eines Arch-Objekts.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Vermessung](Arch_Survey/de.md): Wechselt in den Vermessungsmodus oder verlässt ihn.

-   <img alt="" src=images/BIM_Diff.svg  style="width:32px;"> [IFC Diff](BIM_Diff/de.md): Zeigt einen visuellen Unterschied zwischen zwei IFC-Dateien

-   <img alt="" src=images/BIM_IfcExplorer.svg  style="width:32px;"> [IFC-Explorer](BIM_IfcExplorer/de.md): Öffnet ein Tool zum Erkunden der Struktur einer IFC-Datei vor dem Importieren

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [IFC-Tabelle erstellen](Arch_IfcSpreadsheet/de.md): Dieses Tool erstellt eine Tabelle zum Speichern der IFC-Eigenschaften eines Objekts.

-   <img alt="" src=images/BIM_ImagePlane.svg  style="width:32px;"> [Image plane](BIM_ImagePlane.md): Inserts an image plane in the document.

-   <img alt="" src=images/BIM_Unclone.svg  style="width:32px;"> [Unclone](BIM_Unclone.md): Makes a cloned object independent from its original object

-   <img alt="" src=images/BIM_Rewire.svg  style="width:32px;"> [Rewire](BIM_Rewire.md):

-   <img alt="" src=images/BIM_Glue.svg  style="width:32px;"> [Glue](BIM_Glue.md):

-   <img alt="" src=images/BIM_Reextrude.svg  style="width:32px;"> [Reextrude](BIM_Reextrude.md): Recreates an extrusion from a shape that has lost its parametric extrusion by selecting a base face

-   Plattenwerkzeuge:

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Platte](Arch_Panel/de.md): Erstellt ein Plattenobjekt aus einem ausgewählten 2D-Objekt.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Plattenzuschnitt](Arch_Panel_Cut/de.md): Erstellt eine 2D-Zuschnittansicht von einer Platte.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Plattenzeichnung](Arch_Panel_Sheet/de.md): Erstellt eine 2D-Zuschnittzeichnung, die Plattenzuschnitte und andere 2D-Objekte enthält.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Verschachteln](Arch_Nest/de.md): Ermöglicht mehrere ebene Objekte in einer Container-Form anzuordnen.

-   Strukturwerkzeuge:

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Struktur](Arch_Structure/de.md): Erstellt ein Strukturelement von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

  - <img alt="" src=images/Arch_StructuralSystem.svg  style="width:32px;"> [Structural System](Arch_StructuralSystem.md):

  - <img alt="" src=images/Arch_StructuresFromSelection.svg  style="width:32px;"> [Multiple Structures](Arch_StructuresFromSelection.md):

-   <img alt="" src=images/IFC_Diff.svg  style="width:32px;"> [IFC Diff\...](IFC_Diff.md):

-   <img alt="" src=images/IFC_Expand.svg  style="width:32px;"> [IFC Expand](IFC_Expand.md):

-   <img alt="" src=images/IFC_MakeProject.svg  style="width:32px;"> [Make IFC project](IFC_MakeProject.md):

-   <img alt="" src=images/IFC_UpdateIOS.svg  style="width:32px;"> [IfcOpenShell update](IFC_UpdateIOS.md):

-   Nudge:

  - [Nudge Switch](BIM_Nudge_Switch.md):

  - [Nudge Up](BIM_Nudge_Up.md):

  - [Nudge Down](BIM_Nudge_Down.md):

  - [Nudge Left](BIM_Nudge_Left.md):

  - [Nudge Right](BIM_Nudge_Right.md):

  - [Nudge Rotate Left](BIM_Nudge_RotateLeft.md):

  - [Nudge Rotate Right](BIM_Nudge_RotateRight.md):

  - [Nudge Extend](BIM_Nudge_Extend.md):

  - [Nudge Shrink](BIM_Nudge_Shrink.md):



### Statusleiste

Die Statusleiste enthält einige Schaltflächen, mit denen sich verschiedene Zustände einfach ändern lassen:

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Untere Bedienfelder umschalten](BIM_TogglePanels/de.md): Zeigt oder verbirgt Ausgabefenster (die Berichtsansicht und die Python-Konsole).

-   <img alt="" src=images/BIM_ToggleViews.svg  style="width:32px;"> Ansichten umschalten: Blendet das Bedienfeld [BIM-Ansichten](BIM_Views/de.md) ein oder aus.

-   <img alt="" src=images/BIM_ToggleBackground.svg  style="width:32px;"> Hintergrund wechseln: Wechselt zwischen vertikalen, radialen und einfachen Farbhintergrundmodi. Damit kann zwischen einem dunklen Hintergrund für die Modellierung und einem weißen Hintergrund für 2D-Zeichnungen umgeschaltet werden.

-   <img alt="" src=images/IFC.svg  style="width:32px;"> IFC sperren: Wechselt zwischen [gesperrtem und entsperrtem IFC-Modus](NativeIFC#Locked_and_unlocked_modes.md)



### Kontextmenü der Baumansicht 

TBD



### Kontextmenü der 3D-Ansicht 

TBD



### Veraltete Werkzeuge 

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [Arch 3Views](Arch_3Views.md): Creates top, front and side views from a [mesh](Mesh_Workbench.md). Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arch BuildingPart](Arch_BuildingPart.md): Creates a building part including selected objects. Not available in <small>(v1.0)</small> . Use [Arch Floor](Arch_Floor.md) instead.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Arch CloneComponent](Arch_CloneComponent.md): Produces Arch Components that are clones of selected Arch objects. Not available in <small>(v1.0)</small> . Use [Draft Clone](Draft_Clone.md) instead.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Arch CutLine](Arch_CutLine.md): Cuts an object according to a line. Not available in <small>(v1.0)</small> . Use [Arch CutPlane](Arch_CutPlane.md) instead.

-   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Arch MultiMaterial](Arch_MultiMaterial.md): Creates a multi-material and attributes it to selected objects, if any. Not available in <small>(v1.0)</small> . Use [BIM Material](BIM_Material.md) instead.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Arch Project](Arch_Project.md): Creates a project including selected objects. Not available in <small>(v1.0)</small> . Use [BIM Project](BIM_Project.md) instead.

-   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Arch SetMaterial](Arch_SetMaterial.md): Creates a material and attributes it to selected objects, if any. Not available in <small>(v1.0)</small> . Use [BIM Material](BIM_Material.md) instead.



## Einstellungen

-   <img alt="" src=images/Preferences-bim.svg  style="width:32px;"> [Preferences](BIM_Preferences/de.md): Allgemeine Einstellungen für den BIM Workbench.
-   [Fine-tuning](Fine-tuning#BIM_Workbench/de.md): Zusätzliche Parameter zur Feinabstimmung des BIM-Verhaltens.



## Arbeiten mit IFC 

Die BIM-Workbench arbeitet nativ mit [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC)-Dateien. Nativ bedeutet, dass keine weitere Übersetzung zwischen den IFC-Inhalten und FreeCAD erforderlich ist: Die IFC-Inhalte werden direkt in FreeCAD gerendert und jede Änderung wirkt sich direkt auf die IFC-Inhalte aus. Lese mehr über [NativeIFC](NativeIFC/de.md).

Wenn du nicht vorhast, mit anderen zusammenzuarbeiten, und IFC nicht benötigest, kannst du trotzdem die BIM-Workbench-Tools verwenden und alles, was mit IFC zu tun hat, einfach ignorieren. Du kannst dein Modell trotzdem jederzeit in IFC exportieren.

Der alte [Arch IFC](Arch_IFC.md)-Importer ist in FreeCAD standardmäßig deaktiviert, in Python aber weiterhin verfügbar.



## Dateiformate

-   [IFC](Arch_IFC.md): Industrie-Grundlagenklassen
-   [DAE](Arch_DAE.md): Collada-Netzformat
-   [OBJ](Arch_OBJ.md): OBJ-Netzformat (nur Export)
-   [JSON](Arch_JSON.md): JavaScript Object Notation-Format (nur Export)
-   [3DS](Arch_3DS.md): 3DS-Format (nur Import)
-   [SHP](Arch_SHP.md): GIS-Shapefiles (nur Import)



## API

Das Arch-Modul kann in [Python](Python.md)-Skripten und [Makros](Makros.md) mithilfe der [Arch Python API](Arch_API/de.md)-Funktionen verwendet werden.



## Anleitungen und Lernen 

-   [Umstieg von Revit auf FreeCAD](Migrating_to_FreeCAD_from_Revit/de.md)
-   [Arch- & BIM-Anleitungen in diesem Wiki](Tutorials#Architecture_and_BIM/de.md)
-   [Videoserie \"BIM with FreeCAD\" von Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [Videoserie \"FreeCAD tutorials\" von Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [Videoserie \"Quinta Monroy\" von Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)
-   [YouTube-Kanal \"HRCompacta\" (Inhalt ist hauptsächlich in Portugiesisch)](https://www.youtube.com/@HRCompacta)
-   [YouTube-Kanal \"FreeCADBIM\" (Inhalt ist hauptsächlich in Portugiesisch)](https://www.youtube.com/@FreeCadBIM)



## Beispieldateien

-   FreeCAD bietet auf der Startseite eine BIM-Beispieldatei.
-   Weitere BIM-Beispieldateien sind unter <https://github.com/yorikvanhavre/FreeCAD-BIM-examples> verfügbar. Verwende in FreeCAD das Menü „Hilfe" -\> „BIM-Beispiele".



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > BIM Workbench/de
