# BIM Workbench/de
}

<img alt="BIM Externes Arbeitsbereichssymbol" src=images/IFC.svg  style="width:128px;">


{{TOCright}}



## Einführung

Der <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Arbeitsbereich](BIM_Workbench/de.md) ist ein [externer Arbeitsbereich](External_workbenches/de.md) mit dem Ziel, vollständige [Bauwerksdatenmodellierung](https://en.wikipedia.org/wiki/Building_information_modeling) (engl.: Building Information Modeling) (BIM) Werkzeuge und Arbeitsabläufe in FreeCAD zu implementieren. Er kann aus dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert werden.

Der BIM Arbeitsbereich basiert auf dem eingebauten <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Arbeitsbereich](Arch_Workbench/de.md), und beide werden wahrscheinlich in der Zukunft zusammengeführt werden. Der BIM Arbeitsbereich ist ein \"Meta Arbeitsbereich\", der viele nützliche Werkzeuge aus anderen Arbeitsbereichen an einem Ort versammeln und einen Arbeitsablauf schaffen soll, der sowohl für erfahrene BIM Anwender als auch für Anfänger bequemer und benutzerfreundlicher ist. Der BIM Arbeitsbereich verfügt auch über einige spezifische eigene Werkzeuge, hauptsächlich Assistenten und Verwaltungswerkzeuge, die sich im Menü **Verwaltung** befinden.

Siehe [FreeCAD BIM Umstiegsleitfaden](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) für einen schnellen Überblick, wenn Sie bereits Benutzer einer anderen BIM-Anwendung sind.

Die Entwickler von Entwurf, Architektur und BIM arbeiten auch mit der größeren [OSArch Gemeinschaft](https://osarch.org) zusammen, mit dem ultimativen Ziel, den Entwurf von Gebäuden durch den Einsatz völlig freier Software zu verbessern.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">



## Installieren

Der BIM Arbeitsbereich ist nicht mit dem Standard FreeCAD Paket gebündelt, kann aber einfach über den <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert werden. Rufe ihn vom **Werkzeuge → [Erweiterungsverwalter](Std_AddonMgr/de.md)** auf. Der BIM Arbeitsbereichscode ist [bereitgestellt und entwickelt auf github](https://github.com/yorikvanhavre/BIM_Workbench) und kann auch manuell installiert werden, indem er in das FreeCAD Verzeichnis **MOD** kopiert wird.

**Hinweis**

Der BIM Arbeitsbereich ist noch in Arbeit und wird sich häufig ändern. Achte darauf, sie regelmäßig zu aktualisieren! Wenn du das [Python-Git](https://github.com/chidimo/python-git) Modul installiert hast, sucht der BIM Arbeitsbereich beim Start automatisch nach verfügbaren Aktualisierungen und zeigt ein Symbol in der Statusleiste an, wenn eine Aktualisierung verfügbar ist.

Die unten aufgeführten Werkzeuge sind möglicherweise auch nicht alle vorhanden, wenn deine FreeCAD Version nicht vollständig aktuell ist. Der BIM Arbeitsbereich sollte jedoch nahtlos auf allen FreeCAD Versionen funktionieren, er wird nur die nicht verfügbaren Werkzeuge auslassen.



## Erste Schritte 

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Beim ersten Start des BIM Arbeitsbereichs wird ein Begrüßungsdialog angezeigt, der einen schnellen Überblick über die Funktionsweise des Arbeitsbereichs gibt und es dem Benutzer ermöglicht, ein [BIM im Spiel Tutorium](BIM_ingame_tutorial/de.md) zu starten. Der Begrüßungsdialog ist auch über das Menü **Hilfe** verfügbar. Wenn der Begrüßungsbildschirm durch Klicken auf OK geschlossen wird, wird der [BIM Setup Dialog](BIM_Setup/de.md) angezeigt, der es dem Benutzer ermöglicht, schnell einige der häufigsten BIM-bezogenen Einstellungen von FreeCAD vorzunehmen, ohne durch die vollständigen FreeCAD Einstellungsseiten blättern zu müssen.

Das [BIM Projekt Einrichtung](BIM_Project/de.md) Werkzeug ermöglicht es dir, ein BIM Projekt schnell einzurichten, indem du einige grundlegende Informationen über dein Projekt ausfüllst. Du kannst dann z. B. die verschiedenen 2D Zeichenwerkzeuge verwenden, um Richtlinien und Grundlinien zu skizzieren, und dann die verschiedenen 3D Modellierungswerkzeuge verwenden, um daraus automatisch 3D BIM Objekte zu erstellen. Eine Linie kann z. B. zu einer Wand werden, indem du sie einfach auswählst und die [Wand](Arch_Wall/de.md) Schaltfläche drückst.

Wenn du an eine andere BIM Anwendung gewöhnt bist, prüfe unserere [BIM Anwendungskompatibilitätstabelle](BIM_application_compatibility_table/de.md) um beim Start mit FreeCAD deine Schulnoten zu erhalten.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

Das [in-game tutorial](BIM_ingame_tutorial/de.md) ist ein einfacher Weg, um schnell mit dem BIM Arbeitsbereich zurechtzukommen.



## Werkzeuge

Der BIM Arbeitsbereich versammelt Werkzeuge aus mehreren anderen FreeCAD Arbeitsbereichen, hauptsächlich [Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md) und [Part](Part_Workbench/de.md), die grob in logische Kategorien eingeteilt sind: **2D Zeichnungs\'\',**3D Modellierungs\'\', **Anmerkungs** und **Änderungs** Werkzeuge. Die **verwalten** Kategorie enthält Werkzeuge, die spezifisch für den BIM Arbeitsbereich sind.

Zusätzlich, falls solche [Erweiterungen](External_workbenches/de.md) installiert sind, Werkzeuge von [Reinforcement](Arch_Rebar/de.md) (zusätzliche Werkzeuge für Bewehrungsstäbe), [Verbindungselemente](Fasteners_Workbench/de.md) (Bolzen und Schrauben), [Flamingo/Dodo](Flamingo_Workbench/de.md) (Metallstruktur- und Rohrleitungswerkzeuge) und [Teilebibliothek](Parts_Library_Workbench/de.md) sind automatisch im BIM Arbeitsbereich enthalten.

Der BIM Arbeitsbereich fügt auch eine Reihe von Elementen in der **Statusleiste** von FreeCAD und einige **Kontextmenüelemente** hinzu, die durch einen Rechtsklick in der 3D Ansicht oder in der Baumansicht zugänglich sind.



### 2D Entwurf 

2D Objekte werden häufig als Zeichenhilfe oder zum Zeichnen von Grundlinien und Profilen verwendet, auf denen BIM Objekte aufgebaut werden. Sie können auch zum Zeichnen von Symbolen und Anmerkungen in deinem Modell verwendet werden. Abgesehen von Skizzen, die ein eigenes Koordinatensystem verwenden, werden 2D Objekte auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) gezeichnet.

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Skizze](Sketcher_NewSketch/de.md): Erstellt eine neue Skizze und wechselt in den Skizzenzeichnungsmodus. Skizzen sind erweiterte 2D Objekte mit Unterstützung für Beschränkungen
-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linie](Draft_Line/de.md):Zeichnet ein Liniensegment zwischen 2 Punkten
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Draht](Draft_Wire/de.md): Zeichnet eine Linie, die aus mehreren Liniensegmenten besteht (Polylinie)
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Kreis](Draft_Circle/de.md): Zeichnet einen Kreis aus Mittelpunkt und Radius
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Bogen](Draft_Arc/de.md): Zeichnet ein Bogensegment aus Mittelpunkt, Radius, Startwinkel und Endwinkel
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Bogen 3Punkte](Draft_Arc_3Points/de.md): zeichnet ein Kreisbogensegment aus drei Punkten, die sich auf dem Umfang befinden
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/de.md): Zeichnet eine Ellipse aus zwei Eckpunkten
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon/de.md): Zeichnet ein regelmäßiges Polygon aus einem Mittelpunkt und einem Radius
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rechteck](Draft_Rectangle/de.md): Zeichnet ein Rechteck aus 2 gegenüberliegenden Punkten
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline/de.md): Zeichnet einen B-Spline aus einer Reihe von Punkten
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Kubische Bézierkurve](Draft_CubicBezCurve/de.md): zeichnet eine Bézierkurve dritten Grades durch Ziehen von zwei Punkten.
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézierkurve](Draft_BezCurve/de.md): Zeichnet eine Bézierkurve aus einer Reihe von Punkten
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/de.md): Fügt ein Punktobjekt ein



### Anmerkung

Anmerkungen sind visuelle Hilfsobjekte, die in deinem Modell platziert werden können. Sie können verwendet werden, um dein Modell direkt in ein 2D Format wie [DXF](Draft_DXF/de.md) zu exportieren, oder bei der Erstellung von 2D Ansichten deines Modells mit der [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) wiederverwendet werden.

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text/de.md): Zeichnet eine mehrzeilige Textanmerkung
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [FormZeichenkette](Draft_ShapeString/de.md): Zeichnet eine Textlinie als Geometrie
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Abmessung](Draft_Dimension/de.md): Zeichnet eine lineare, winklige, radiale oder Durchmesserabmessung
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Beschriftung](Draft_Label/de.md): Platziert eine Beschriftung mit einem Pfeil, der auf ein ausgewähltes Element zeigt
-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Achse](Arch_Axis/de.md): Erstellt eine einzelne Achse oder eine 1-Richtungs Anordnung von Achsen für das Dokument
-   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Achsensystem](Arch_AxisSystem/de.md): Erzeugt ein Achsensystem, das aus bis zu 3 Achsreihen gebildet wird
-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Gitter](Arch_Grid/de.md): Erzeugt ein gitterartiges Objekt zum Dokument
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Schnittebene](Arch_SectionPlane/de.md): Fügt dem Dokument ein Schnittebenenobjekt hinzu. Schnittebenen definieren 2D Aznsichten wie Pläne, Schnitte und Erhebungen.
-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Seite](TechDraw_PageDefault/de.md): Erstellt eine neue [TechDraw](TechDraw_Workbench.md) Seite aus einer [SVG Vorlage](TechDraw_Templates/de.md)
-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Ansicht](TechDraw_ArchView/de.md): fügt eine Ansicht einer Schnittebene auf eine Seite ein



### 3D / BIM Modellierung 

3D und BIM Objekte sind die realen Elemente, aus denen sich dein BIM Projekt zusammensetzt.

**Gebäudestruktur**: Diese Werkzeuge helfen dir, dein Modell zu organisieren

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projekt](Arch_Project/de.md): Erstellt ein Projekt einschließlich ausgewählter Objekte
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Baugrund](Arch_Site/de.md): Erstellt ein Baugrundstück mit ausgewählten Objekten
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Gebäude](Arch_Building/de.md): Erstellt ein Gebäude einschließlich ausgewählter Objekte
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Ebene](Arch_BuildingPart/de.md) (Gebäudeteil): Erstellt einen Gebäudeteil mit ausgewählten Objekten. Gebäudeteile werden häufig zur Darstellung von Ebenen verwendet
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Raum](Arch_Space/de.md): Erstellt ein Raumobjekt im Dokument
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Referenz](Arch_Reference/de.md): Verknüpft Objekte aus einer anderen FreeCAD Datei mit diesem Dokument

**BIM Werkzeuge**: Diese Werkzeuge erstellen BIM Komponenten

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wand](Arch_Wall/de.md): Erstellt eine Wand von Grund auf oder mit einem ausgewählten Objekt als Basis
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Vorhangfassade](Arch_CurtainWall/de.md): erstellt eine Vorhangfassade von Grund auf oder mit einem ausgewählten Objekt als Basis
-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Säule](Arch_Structure/de.md): Erzeugt ein vertikales [Struktur](Arch_Structure/de.md) Element an einem bestimmten Punkt, optional unter Verwendung eines ausgewählten Objekts als Profil
-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Balken](Arch_Structure/de.md): Erzeugt ein horizontales [Struktur](Arch_Structure/de.md) Element zwischen zwei Punkten, wahlweise unter Verwendung eines ausgewählten Objekts als Profil
-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Platte](Arch_Structure/de.md): Erzeugt ein flaches [Struktur](Arch_Structure/de.md) Element durch Extrudieren eines ausgewählten flachen Objekts
-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Bewehrung](Arch_Rebar/de.md): Erzeugt einen Bewehrungsstab in einem ausgewählten Strukturelement unter Verwendung einer Skizze. Erfordert die [Bewehrung](Reinforcement_Addon/de.md) Erweiterung
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenster](Arch_Window/de.md): Erstellt ein Fenster mit einem ausgewählten Objekt als Basis
-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Tür](Arch_Window/de.md): Erstellt ein Objekt [Fenster](Arch_Window/de.md) unter Verwendung von Türvoreinstellungen
-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Rohrwerkzeuge](Arch_Pipe/de.md): Erzeugt Rohre und Eck- oder T-Stück Verbindungen zwischen 2 oder 3 ausgewählten Rohren
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Treppen](Arch_Stairs/de.md): Erstellt ein Treppenobjekt im Dokument
-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/de.md): Erzeugt ein geneigtes Dach aus einer ausgewählten Fläche
-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Tafel Werkzeuge](Arch_Panel/de.md): Erstellt Tafelobjekte und 2D Ausschnitte aus diesen Tafeln
-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Rahmen](Arch_Frame/de.md): Erzeugt ein Rahmenobjekt aus einem ausgewählten Layout
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Zaun](Arch_Fence/de.md): Erstellt ein Zaunobjekt aus einem ausgewählten Pfostenobjekt und Pfad
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Fachwerk](Arch_Truss/de.md): Erzeugt einen Fachwerkträger aus einer ausgewählten Linie oder von Grund auf
-   <img alt="" src=images/BIM_Library.png  style="width:32px;"> [Bibliothek](BIM_Library/de.md): Fügt ein Ausrüstungs- oder Möbelobjekt ein. Benötigt [Teilebibliothek](Parts_Library/de.md) Erweiterung
-   <img alt="" src=images/Arch_Component.png  style="width:32px;"> [BIM Komponente](Arch_Component/de.md): Wandelt jedes ausgewählte Objekt in ein BIM Objekt um, mit vollständiger IFC Unterstützung

**Generische 3D Werkzeuge**: Diese Werkzeuge erstellen generische 3D Objekte, die in BIM Komponenten umgewandelt oder verwendet werden können.

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/de.md): Erzeugt ein parametrisches 2D Profil, das z.B. bei Extrusionen verwendet wird
-   <img alt="" src=images/BIM_Box.png  style="width:32px;"> [Kasten](BIM_Box/de.md): Zeichnet einen Kasten, durch Angabe seiner grafischen Abmessungen
-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Formbauer](Part_Builder/de.md): Ein Werkzeug zum Erstellen komplexerer Formen aus verschiedenen parametrischen geometrischen Grundelementen
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Flächenbinder](Draft_Facebinder/de.md): Erstellt ein neues Objekt aus ausgewählten Flächen auf vorhandenen Objekten



### Änderungswerkzeuge

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Bewegen](Draft_Move/de.md): Verschiebt Objekt(e) von einem Ort zu einem anderen
-   <img alt="" src=images/BIM_Copy.png  style="width:32px;"> [Kopie](BIM_Copy/de.md): Kopiert Objekt(e) von einem Ort an einen anderen
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Drehen](Draft_Rotate/de.md): Dreht Objekt(e) von einem Startwinkel zu einem Endwinkel
-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Klonen](BIM_Clone/de.md): Klont die ausgewählten Objekte
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Versatz](Draft_Offset/de.md): Verschiebt Segmente eines Objekts um einen bestimmten Abstand
-   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Versatz](Part_Offset2D/de.md): Konstruiert einen parallelen Draht in einem bestimmten Abstand zum Original oder vergrößert/verkleinert eine planare Fläche ((parametrische Version)
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Stutzen/Erweitern (Trimex)](Draft_Trimex/de.md): Stutzt oder erweitert ein Objekt
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skalieren](Draft_Scale/de.md): Skaliert das/die ausgewählte(n) Objekt(e) um einen Basispunkt
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Dehnen](Draft_Stretch/de.md): Dehnt die ausgewählten Objekte
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Anordnung](Draft_Array/de.md): Erstellt eine polare oder rechtwinklige Anordnung aus ausgewählten Objekten
-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Pfad Anordnung](Draft_PathArray/de.md): Erstellt eine Anordnung von Objekten, indem die Kopien entlang eines Pfades platziert werden
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Spiegel](Draft_Mirror/de.md): Spiegelt die ausgewählten Objekte
-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrudieren](Part_Extrude/de.md): Extrudiert planare Flächen eines Objekts
-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Schnitt](Part_Cut/de.md): Schneidet (subtrahiert) ein Objekt von einem anderen
-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Vereinigen](Part_Fuse/de.md): Verschmilzt (vereinigen) zweier Objekte
-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Schnittmenge](Part_Common/de.md): Extrahiert den gemeinsamen (Kreuzungs) Teil von zwei Objekten
-   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Verbund](Part_Compound/de.md): Erstellt einen Verbund aus den ausgewählten Objekten
-   <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Einfache Kopie](Part_SimpleCopy/de.md): Erstellt eine nicht-parametrische Kopie eines ausgewählten Objekts
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Höherstufung](Draft_Upgrade/de.md): Verbindet Objekte zu einem höherwertigen Objekt
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Herabstufung](Draft_Downgrade/de.md): Explodiert Objekte in niederwertige Objekte
-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Form 2D Ansicht](Draft_Shape2DView/de.md): Erstellt ein 2D Objekt, bei dem es sich um eine abgeflachte 2D Ansicht eines anderen 3D Objekts handelt.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Entwurf zur Skizze](Draft_Draft2Sketch/de.md): Konvertiert ein Entwurfsobjekt in eine Skizze und umgekehrt
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Schnitt mit Ebene](Arch_CutPlane/de.md): Ein Objekt nach einem Plan schneiden.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Komponente hinzufügen](Arch_Add/de.md): Fügt Objekte zu einer Komponente hinzu
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Komponente entfernen](Arch_Remove/de.md): Subtrahiert oder entfernt Objekte von einer Komponente



### Verwaltungswerkzeuge

-   <img alt="" src=images/BIM_Setup.png  style="width:32px;"> [BIM Einrichtung](BIM_Setup/de.md): Konfiguriert einige der am häufigsten für BIM verwendeten FreeCAD Einstellungen
-   <img alt="" src=images/BIM_Project.png  style="width:32px;"> [Projekt einrichten](BIM_Project/de.md): Ermöglicht die Erstellung einiger grundlegender Objekte wie z.B. einer [Baugrund](Arch_Site/de.md), eines [Gebäude](Arch_Building/de.md) und [Achsen](Arch_Axis/de.md) durch Ausfüllen grundlegender Projektinformationen.
-   <img alt="" src=images/BIM_Views.png  style="width:32px;"> [Ansichten und Ebenenverwalter](BIM_Views/de.md): Verwalte die verschiedenen Ansichten und Ebenen deines Projekts
-   <img alt="" src=images/BIM_Windows.png  style="width:32px;"> [Fensterverwalter](BIM_Windows/de.md): Verwalten Sie die Türen und Fenster Ihres Projekts
-   <img alt="" src=images/BIM_IfcElements.png  style="width:32px;"> [IFC Elementeverwalter](BIM_IfcElements/de.md): Verwalte, wie die verschiedenen Elemente deines Projekts nach IFC exportiert werden
-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [IFC Eigenschaftenverwalter](BIM_IfcProperties/de.md): Verwalte die an jedes deiner Objekte angehängten IFC Eigenschaften
-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [IFC Mengenverwalter](BIM_IfcQuantities/de.md): Verwalte, wie die Mengen deiner Objekte explizit nach IFC exportiert werden
-   <img alt="" src=images/BIM_Classification.png  style="width:32px;"> [Klassifizierungsmanager](BIM_Classification/de.md): Verwalte wie Objekte und Materialien deines Projekts in Beziehung zu Klassifizierungssystemen wie [Uniclass](https://en.wikipedia.org/wiki/Uniclass)
-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [Ebenenverwalter](BIM_Layers/de.md): Verwalte die Ebenen deines Dokuments
-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Material](Arch_SetMaterial/de.md): Verwaltet Materialien oder [Mehrfachmaterialien](Arch_MultiMaterial/de.md) von ausgewählten Objekten
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Zeitplan](Arch_Schedule/de.md): Erstellt verschiedene Arten von Zeitplänen
-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Vorflugkontrollen](BIM_Preflight/de.md): Führe vor dem Export nach IFC verschiedene Prüfungen an deinem Modell durch
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): Manages annotation styles used by texts and dimensions



## Tutorien und Lernen 

-   [Umstieg auf FreeCAD von Revit](Migrating_to_FreeCAD_from_Revit/de.md)
-   [Arch & BIM Tutorien in diesem Wiki](Tutorials#Architecture_and_BIM/de.md)
-   [\"BIM mit FreeCAD\" Videoserie von Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD Tutorien\" Videoserie von Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" Videoserie von Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)



## Externe Arbeitsbereiche 

FreeCAD Arbeitsbereiche sind einfach in [Python](Python.md) zu programmieren. Daher entwickeln viele Leute zusätzliche Arbeitsbereiche außerhalb der FreeCAD Hauptentwickler.

Die Seite [externe Arbeitsbereiche](External_workbenches/de.md) enthält einige Informationen und Anleitungen zu einigen von ihnen, und das Projekt [FreeCAD Erweiterungen](https://github.com/FreeCAD/FreeCAD-addons) hat sich zum Ziel gesetzt, diese zu sammeln und sie von FreeCAD aus leicht installierbar zu machen.

Neue Arbeitsbereiche sind in der Entwicklung, bleib\' dran!



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [BIM](Category_BIM.md) > BIM Workbench/de
