




<img alt="Arch Arbeitsbereichssymbol" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

## Einführung

Der <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Architektur Arbeitsbereich](Arch_Workbench/de.md) stellt einen modernen [Bauwerksdatenmodellierung](http://de.wikipedia.org/wiki/Building_Information_Modeling) (BIM) Arbeitsablauf für FreeCAD zur Verfügung mit Unterstützung für Funktionen wie vollständig parametrische Architektur Entitäten wie Wände, Balken, Dächer, Fenster, Treppen, Rohre und Möbel. Er unterstützt [1](http://de.wikipedia.org/wiki/Industry_Foundation_Classes) ([IFC](Arch_IFC.md)) Dateien und die Erstellung von 2D Geschossplänen in Kombination mit dem <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;">[TechDraw Arbeitsbereich](TechDraw_Workbench/de.md).

Der Arch-Arbeitsbereich importiert alle Werkzeuge des <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereichs](Draft_Workbench/de.md), weil er 2D-Objekte zur Erstellung von 3D parametrischen Architekturobjekten benutzt. Trotzdem kann Arch auch Volumenkörper aus Arbeitsbereichen wie <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) und <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) verwenden.

Die BIM Funktionalität von FreeCAD ist nun nach und nach aufgeteilt in diesen Arch Arbeitsbereich, der grundlegende Architekturwerkzeuge enthält, und die <img alt="" src=images/Workbench_BIM.svg  style="width:24px;">[BIM Arbeitsbereich](BIM_Workbench/de.md), die du über den <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/de.md) installieren kannst. Dieser Arbeitsbereich fügt eine neue Schnittstellenschicht über die Arch Werkzeuge hinzu, mit dem Ziel, den BIM Arbeitsablauf in FreeCAD intuitiver und benutzerfreundlicher zu gestalten. Siehe [FreeCAD BIM Migrationsanleitung](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Die Entwickler von Draft, Arch und BIM arbeiten auch mit der größeren [OSArch Gemeinschaft](https://osarch.org) zusammen, mit dem letztendlichen Ziel, den Gebäudeentwurf durch den Einsatz völlig freier Software zu verbessern.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Werkzeuge

Dies sind Werkzeuge zum Erstellen von Architekturobjekten.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wand](Arch_Wall/de.md): erstellt eine Wand von Grund auf oder mit einem ausgewählten Objekt als Basis.
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Vorhangfassade](Arch_CurtainWall/de.md): erstellt eine Vorhangfassade von Grund auf oder durch verwenden eines gewählten Objekts als eine Basis. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;">[Strukturelement](Arch_Structure/de.md): Erzeugt ein Strukturelement von Grund auf oder mit einem ausgewählten Objekt als Basis.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Bewehrungsstabwerkzeuge](Arch_CompRebarStraight/de.md): Die Verstärkungserweiterung ergänzt die Arch Arbeitsbereich Strukturen.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Gerader Bewehrungsstab](Arch_Rebar_Straight/de.md): Erstellt einen geraden Bewehrungsstab in einem ausgewählten Strukturelement
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [Uförmiger Bewehrungsstab](Arch_Rebar_UShape/de.md): Erstellt einen U-förmigen Bewehrungsstab in einem ausgewählten Strukturelement
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [Lförmiger Bewehrungsstab](Arch_Rebar_LShape/de.md): Erstellt einen L-förmigen Bewehrungsstab in einem ausgewählten Strukturelement
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Bogenförmiger Bewehrungsstab](Arch_Rebar_BentShape/de.md): Erstellt einen bogenförmigen Bewehrungsstab in einem ausgewählten Strukturelement
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Steigbügel Bewehrungsstab](Arch_Rebar_Stirrup/de.md): Erstellt einen bügelförmigen Bewehrungsstab in einem ausgewählten Strukturelement
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Spiralförmiger Bewehrungsstab](Arch_Rebar_Helical/de.md): Erstellt einen spiralförmigen Bewehrungsstab in einem ausgewählten Strukturelement
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:24px;"> [SäulenVerstärkung](Arch_Rebar_ColumnReinforcement/de.md): erzeugt einen Bewehrungsstab innerhalb eines Objekts der Stützenbogenstruktur.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:24px;"> [SäulenBewehrung ZweiVerbindungenSechsBewehrungsstäbe](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/de.md): erzeugt einen Verstärkungsstab innerhalb eines Stützenbogenstrukturobjekts.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.png  style="width:32px;"> [BeamReinforcement](Arch_Rebar_BeamReinforcement/de.md): Erzeugt Verstärkungsstäbe innerhalb eines Stabbogenstrukturobjekts.
    -   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Bewehrungsstab](Arch_Rebar/de.md): Erstellt einen maßgeschneiderten Bewehrungsstab in einem ausgewählten Strukturelement basierend auf einer Skizze

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Etage](Arch_Floor/de.md): Erzeugt eine Etage mit den ausgewählten Objekten
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Gebäudeteil](Arch_BuildingPart/de.md): Erzeugt ein Gebäudeteil mit den ausgewählten Objekten
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Gebäude](Arch_Building/de.md): Erzeugt ein Gebäude mit den ausgewählten Objekten
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Baugrund](Arch_Site/de.md): Erzeugt einen Baugrund mit den ausgewählten Objekten
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projekt](Arch_Project/de.md): Erstellt ein Projekt einschließlich ausgewählter Objekte
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Referenz](Arch_Reference/de.md): Verbindet Objekte aus einer anderen FreeCAD Datei in dieses Dokument
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenster](Arch_Window/de.md): Erzeugt ein Fenster im ausgewählten Objekt
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Schnittebene](Arch_SectionPlane/de.md): Fügt eine Schnittebene zum Dokument hinzu

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Achsenwerkzeuge](Arch_CompAxis/de.md): Das Achsen Werkzeug erlaubt dir das Platzieren einer Reihe von Achsen im aktuellen Dokument.
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Achsen](Arch_Axis/de.md): Fügt eine 1-Richtungsanordnung von Achsen zum Dokument hinzu
    -   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Achsensystem](Arch_AxisSystem/de.md): Fügt ein aus mehreren Achsen gebildetes Achsensystem dem Dokument hinzu
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Gitter](Arch_Grid/de.md): Fügt dem Dokument ein gitterartiges Objekt hinzu

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/de.md): Erzeugt eine Dachneigung aus der selektierten Fläche
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Raum](Arch_Space/de.md): Erstellt ein Raumobjekt im Dokument
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Treppe](Arch_Stairs/de.md): Erstellt ein Treppenobjekt im Dokument

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Paneelwerkzeuge](Arch_CompPanel/de.md): Erlaubt dir die Erstellung aller Arten von Paneel ähnlichen Elementen.
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Paneel](Arch_Panel/de.md): Erstellt ein Paneelobjekt eines gewählten 2D Objekts
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Tafel Schnitt](Arch_Panel_Cut/de.md): Erstellt eine 2D Schnittansicht eines Paneels <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panel Sheet](Arch_Panel_Sheet/de.md): Erstellt ein 2D Schnittbogen mit Schnittansichten eines Paneels oder anderer 2D Objekte <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nest](Arch_Nest/de.md): Erlaubt die \"Einschachtelung\" von mehreren flachen Objekten in einer Containerform <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Rahmen](Arch_Frame/de.md): Erstellt ein Rahmenobjekt aus einem gewählten Layout
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Zaun](Arch_Fence/de.md): Erstellt ein Zaunobjekt aus einem ausgewählten Pfosten und Pfad. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Fachwerk](Arch_Truss.md): Erstellt einen Fachwerkträger aus einer ausgewählten Zeile oder von Grund auf neu. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Ausstattung](Arch_Equipment/de.md): Erstellt ein Ausstattungs oder Möbelobjekt
-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/de.md): Erstellt ein parametrisches 2D Profil. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Rohrwerkzeuge](Arch_CompPipe/de.md) <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Rohr](Arch_Pipe/de.md): Erstellt ein Rohr <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_PipeConnector.png  style="width:32px;"> [RohrVerbinder](Arch_PipeConnector/de.md): Erstellt eine Eck- oder T-Verbindung zwischen zwei oder drei ausgewählten Rohren <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Material Werkzeuge](Arch_CompSetMaterial/de.md): Die Material Werkzeuge ermöglichen das Hinzufügen von Materialien zum aktiven Dokument.
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial/de.md): Erstellt ein Material und ordnet es ausgewählten Objekten zu, falls vorhanden
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Mehrfach-Material](Arch_MultiMaterial/de.md): Erstellt ein Mehrfach-Material und ordnet es ausgewählten Objekten zu, falls vorhanden <small>(v0.17)</small> 
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Zeitplan](Arch_Schedule/de.md): Erstellt verschiedene Arten von Zeitplänen

### Änderungswerkzeuge

Hier die Werkzeuge zur Änderung von Architekturobjekten:

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Mit einer Linie schneiden](Arch_CutLine/de.md): Ein Objekt in Übereinstimmung mit einer Linie schneiden. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Schnitt mit Ebene](Arch_CutPlane.md): Ein Objekt in Übereinstimmung mit einer Ebene schneiden.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Komponente hinzufügen](Arch_Add/de.md): Fügt Objekte zu einer Komponente hinzu
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Komponente entfernen](Arch_Remove/de.md): Subtrahiert oder entfernt Objekte von einer Komponente
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Übersicht](Arch_Survey/de.md): betritt oder verlässt den Übersichtsmodus

### Hilfsmittel

Hier sind zusätzliche Hilfsmittel für spezifische Aufgaben:

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Komponente](Arch_Component/de.md): Erzeugt eine nichtparametrische Arch Komponente
-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Komponente klonen](Arch_CloneComponent/de.md): Erzeugt Arch Komponenten, die Klone von ausgewählten Arch Objekten sind (nicht zu verwechseln mit [ Entwurf Klon](Draft_Clone/de.md))
-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Netz aufteilen](Arch_SplitMesh/de.md): Teilt ein ausgewähltes Netz in separate Komponenten
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Netz Zu Form](Arch_MeshToShape/de.md): Wandelt ein Netz in eine Form um, wobei koplanare Flächen vereinigt werden
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [Wähle nicht-feste Netze](Arch_SelectNonSolidMeshes/de.md): Wählt alle nicht-feste Netze aus der aktuellen Auswahl oder aus dem Dokument
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Form entfernen](Arch_RemoveShape/de.md): Dreht kubische formbasierte Arch Objekte vollständig parametrisch
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Löcher schließen](Arch_CloseHoles/de.md): Schließt Löcher in einem ausgewählten formbasierten Objekt
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Mauern zusammenführen](Arch_MergeWalls/de.md): Zwei oder mehr Wände zusammenführen
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Prüfen](Arch_Check/de.md): Prüfen, ob die ausgewählten Objekte Festkörper sind und keine Defekte enthalten
-   <img alt="" src=images/IFC.svg  style="width:32px;"> [Ifc Explorer](Arch_IfcExplorer/de.md): Durchsuche den Inhalt einer [IFC](Arch_IFC/de.md) Datei
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Umschalten der IFC Brep Fahne](Arch_ToggleIfcBrepFlag/de.md): Erzwingt, dass ein ausgewähltes Objekt als [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) exportiert wird.
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Ansichten vom Netz](Arch_3Views/de.md): Erzeugt Draufsicht, Frontansicht und Seitenansichten aus einem [Netz](Mesh_Workbench/de.md).
-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [IFC Kalkulationstabelle erstellen](Arch_IfcSpreadsheet/de.md): Erstellt eine Kalkulationstabelle zum Speichern der [IFC](Arch_IFC/de.md) Eigenschaften eines Objekts
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Unterkomponenten umschalten](Arch_ToggleSubs/de.md): Blendet die Unterkomponenten eines Arch Objekts ein oder aus.

### Einstellungen

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Einstellungen](Arch_Preferences/de.md): Einstellungen für das Standard-Aussehen von Wänden, Strukturen, Bewehrungen, Fenstern, Treppen, Paneelen, Rastern und Achsen.

### Dateiformate

-   [IFC](Arch_IFC/de.md) : Industrie Fundament Klassen
-   [DAE](Arch_DAE/de.md) : Collada Netz Format
-   [OBJ](Arch_OBJ/de.md) : Obj Netz Format (nur Export)
-   [JSON](Arch_JSON/de.md) : JavaScript JavaScript Objekt Notationsformat

(nur Export)

-   [3DS](Arch_3DS/de.md) : 3DS Format (nur Import)
-   [SHP](Arch_SHP.md): GIS Formdateien (nur Import)

## API

Der Arch-Arbeitsbereich kann mit den [Arch Python API](http://www.freecadweb.org/api/Arch.html)-Funktionen in [Python](Python/de.md)-Skripten und [Makros](macros/de.md) benutzt werden.

## Übungen

-   [Architektur Arbeitsablauf](http://yorik.uncreated.net/guestblog.php?tag=freecad): Ein Beispiel, wie FreeCAD anfangen kann, einen vorbereitenden Platz in einem Architektur Arbeitsablauf einzunehmen.
-   [Arch Tutorium](Arch_tutorial/de.md)(v0.14)
-   [Schnelle Arch Übersicht auf Yorik\'s Blog](http://yorik.uncreated.net/guestblog.php?2012=180)(v0.13)
-   [Video Präsentation des Arch Arbeitsbereichs](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Arch Paneel Tutorium](Arch_panel_tutorial/de.md) (v0.15)
-   [BIM Modellierungskapitel aus dem FreeCAD Handbuch](Manual:BIM_modeling/de.md)
-   [Import von STL oder OBJ](Import_from_STL_or_OBJ/de.md)
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
