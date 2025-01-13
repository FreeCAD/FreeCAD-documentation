# Arch Workbench/de
**In v1.0 the BIM, Native-IFC and Arch Workbenches have been merged into the integrated [BIM Workbench](BIM_Workbench.md).**

<img alt="Arch Arbeitsbereichssymbol" src=images/Workbench_Arch.svg  style="width:128px;">






## Einführung

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) provides a modern [**B**uilding **I**nformation **M**odelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) workflow to FreeCAD, with support for features like fully parametric architectural entities such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports [**I**ndustry **F**oundation **C**lasses](Arch_IFC.md) (IFC) files, and production of 2D floor plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

Der Arbeitsbereich Arch importiert alle Werkzeuge des Arbeitsbereichs <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md), weil er dessen 2D-Objekte zur Erstellung von parametrischen 3D-Architekturobjekten benutzt. Trotzdem kann Arch auch Festkörperformen aus Arbeitsbereichen wie <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) und <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) verwenden.

Die BIM-Funktionalität von FreeCAD ist nun dem (Konstruktions-) Ablauf entsprechend aufgeteilt in diesen Arbeitsbereich Arch, der grundlegende Architekturwerkzeuge enthält, und dem Arbeitsbereich <img alt="" src=images/Workbench_BIM.svg  style="width:24px;">[BIM](BIM_Workbench/de.md), den der <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) zur Verfügung stellt. Dieser Arbeitsbereich BIM fügt eine neue Schnittstellenebene, zusätzlich zu den Arch-Werkzeugen, hinzu, mit dem Ziel, den BIM-Arbeitsablauf in FreeCAD intuitiver und benutzerfreundlicher zu gestalten. Siehe [FreeCAD BIM Migrationsanleitung](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Die Entwickler von Draft, Arch und BIM arbeiten auch mit der größeren [OSArch-Gemeinschaft](https://osarch.org) zusammen, mit dem letztendlichen Ziel, den Gebäudeentwurf durch den Einsatz völlig freier Software zu verbessern.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">



## Werkzeuge

Dies sind Werkzeuge zum Erstellen von Architekturobjekten.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wand](Arch_Wall/de.md): Erstellt eine Wand von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Struktur](Arch_Structure/de.md): Erstellt ein Strukturelement von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Armierungswerkzeuge](Arch_CompRebarStraight/de.md): Diese Werkzeuge, außer dem letzten, stehen nur zur Verfügung, wenn der Arbeitsbereich [Reinforcement](Reinforcement_Workbench/de.md) (Bewehrung)installiert wurde.

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

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Bewehrung](Arch_Rebar/de.md): Erstellt unter Verwendung einer Skizze ein individuell angepasstes Bewehrungselement in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Vorhangwand](Arch_CurtainWall/de.md): Erstellt eine Vorhangwand von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Gebäudeteil](Arch_BuildingPart/de.md): Erstellt einen Gebäudeteil inklusive der ausgewählten Objekte.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projekt](Arch_Project/de.md): Erstellt ein Projekt inklusive der ausgewählten Objekte.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Grundstück](Arch_Site/de.md): Erstellt ein Grundstück inklusive der ausgewählten Objekte.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Building](Arch_Building.md): Erstellt ein Gebäude inklusive der ausgewählten Objekte.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Stockwerk](Arch_Floor/de.md): Erstellt ein Geschoss inklusive der ausgewählten Objekte.

-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Externe Referenz](Arch_Reference/de.md): Verknüpft Objekte aus einer anderen FreeCAD-Datei mit dem aktuellen Dokument.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenster](Arch_Window/de.md): Erstellt ein Fenster von Grund auf oder unter Verwendung eines ausgewählten Objekts als Basis.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/de.md): Erstellt ein geneigtes Dach aus einer ausgewählten Polylinie.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Achsenwerkzeuge](Arch_CompAxis/de.md)

  - <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Achse](Arch_Axis/de.md): Fügt eine eindimensionale Anordnung von Achsen hinzu.

  - <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Achsensystem](Arch_AxisSystem/de.md): Fügt ein Achsensystem, das aus mehreren Achsen besteht, hinzu.

  - <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Raster](Arch_Grid/de.md): Fügt ein gitterartiges Objekt hinzu.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Schnittebene](Arch_SectionPlane/de.md): Fügt eine Schnittebene (section plane object) hinzu.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Raum](Arch_Space/de.md): Erstellt ein Raumobjekt.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Treppe](Arch_Stairs/de.md): Erstellt eine Treppe (stairs object).

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Plattenwerkzeuge](Arch_CompPanel/de.md)

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Platte](Arch_Panel/de.md): Erstellt ein Plattenobjekt aus einem ausgewählten 2D-Objekt.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Plattenzuschnitt](Arch_Panel_Cut/de.md): Erstellt eine 2D-Zuschnittansicht von einer Platte.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Plattenzeichnung](Arch_Panel_Sheet/de.md): Erstellt eine 2D-Zuschnittzeichnung, die Plattenzuschnitte und andere 2D-Objekte enthält.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Verschachteln](Arch_Nest/de.md): Ermöglicht mehrere ebene Objekte in einer Container-Form anzuordnen.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Equipment](Arch_Equipment.md): Creates an equipment or furniture object.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Frame](Arch_Frame.md): Creates a frame object from a selected layout.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Fence](Arch_Fence.md): Creates a fence object from a selected post and path.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Truss](Arch_Truss.md): Creates a truss from a selected line or from scratch.

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profile](Arch_Profile.md): Creates a parametric 2D profile.

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Material tools](Arch_CompSetMaterial.md)

  - <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial.md): Creates a material and attributes it to selected objects, if any.

  - <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Material](Arch_MultiMaterial.md): Creates a multi-material and attributes it to selected objects, if any.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule.md): Creates different types of schedules.

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Pipe tools](Arch_CompPipe.md)

-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Rohr](Arch_Pipe/de.md): Erstellt eine Rohrleitung.

-   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Rohrverbinder](Arch_PipeConnector/de.md): Erstellt eine Bogen- oder T-Verbindung zwischen 2 bzw 3 ausgewählten Rohrleitungen.



### Änderungswerkzeuge

Hier die Werkzeuge zur Änderung von Architekturobjekten:

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cut with plane](Arch_CutPlane.md): Cuts an object according to a plane.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cut with line](Arch_CutLine.md): Cuts an object according to a line.

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add component](Arch_Add.md): Adds objects to a component.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove component](Arch_Remove.md): Subtracts or removes objects from a component.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey.md): Enters or leaves surveying mode.



### Hilfsmittel

Hier sind zusätzliche Hilfsmittel für spezifische Aufgaben:

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Component](Arch_Component.md): Creates a non-parametric Arch component.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Clone component](Arch_CloneComponent.md): Produces Arch Components that are clones of selected Arch objects (not to be confused with [Draft Clone](Draft_Clone.md)).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Split Mesh](Arch_SplitMesh.md): Splits a selected mesh into separate components.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Mesh to Shape](Arch_MeshToShape.md): Converts a mesh into a shape, unifying coplanar faces.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Select non-manifold meshes](Arch_SelectNonSolidMeshes.md): Selects all non-manifold meshes from the current selection or from the document.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remove Shape from Arch](Arch_RemoveShape.md): Turns cubic shape-based Arch object fully parametric.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Close holes](Arch_CloseHoles.md): Closes holes in a selected shape-based object.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Merge Walls](Arch_MergeWalls.md): Merge two or more walls.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check.md): Check if the selected objects are solids and don\'t contain defects.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Toggle IFC Brep flag](Arch_ToggleIfcBrepFlag.md): Forces a selected object to be exported as an [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Views from mesh](Arch_3Views.md): Creates top, front and side views from a [mesh](Mesh_Workbench.md).

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Create IFC spreadsheet\...](Arch_IfcSpreadsheet.md): Creates a spreadsheet to store [IFC](Arch_IFC.md) properties of an object.

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Toggle subcomponents](Arch_ToggleSubs.md): Shows or hides the subcomponents of an Arch object.



### Einstellungen

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Einstellungen](Arch_Preferences/de.md): Einstellungen für das Standard-Aussehen von Wänden, Strukturen, Bewehrungen, Fenstern, Treppen, Paneelen, Rastern und Achsen.



### Dateiformate

-   [IFC](Arch_IFC/de.md) : Industrie-Fundament-Klassen
-   [DAE](Arch_DAE/de.md) : Collada-Netz-Format
-   [OBJ](Arch_OBJ/de.md) : OBJ-Netz-Format (nur Export)
-   [JSON](Arch_JSON/de.md) : JavaScript-Object-Notation-Format (nur Export)
-   [3DS](Arch_3DS/de.md) : 3DS-Format (nur Import)
-   [SHP](Arch_SHP.md): GIS-Formdateien (nur Import)

## API

Der Arbeitsbereich Arch kann mit den Funktionen der [Arch Python API](http://www.freecadweb.org/api/Arch.html) in [Python](Python/de.md)-Skripten und [Makros](macros/de.md) verwendet werden.



## Übungen

-   [Umstieg auf FreeCAD von Revit](Migrating_to_FreeCAD_from_Revit/de.md)
-   [Architektur Arbeitsablauf](http://yorik.uncreated.net/guestblog.php?tag=freecad): Ein Beispiel, wie FreeCAD anfangen kann, einen vorbereitenden Platz in einem Architektur Arbeitsablauf einzunehmen.
-   [Arch Tutorium](Arch_tutorial/de.md)(v0.14)
-   [Schnelle Arch Übersicht auf Yorik\'s Blog](http://yorik.uncreated.net/guestblog.php?2012=180)(v0.13)
-   [Video Präsentation des Arch Arbeitsbereichs](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Arch Paneel Tutorium](Arch_panel_tutorial/de.md) (v0.15)
-   [BIM Modellierungskapitel aus dem FreeCAD Handbuch](Manual:BIM_modeling/de.md)
-   [Import von STL oder OBJ](Import_from_STL_or_OBJ/de.md)
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md)



---
⏵ [documentation index](../README.md) > [Obsolete_Workbenches](Category_Obsolete_Workbenches.md) > Arch Workbench/de
