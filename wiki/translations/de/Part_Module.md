# <img alt="Part Arbeitsbereichsymbol" src=images/Workbench_Part.svg  style="width:64px;"> Part Module/de


{{TOCright}}

## Einführung

Die Festkörper Modellierungsfähigkeiten von FreeCAD basieren auf dem _ ist eine Schicht, die sich auf der Oberseite der OCCT Bibliotheken befindet und dem Benutzer Zugriff auf geometrische OCCT Grundkörper und -funktionen gewährt. Grundsätzlich basieren alle 2D und 3D Zeichenfunktionen in jedem Arbeitsbereich (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> _, <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md), usw.) auf diesen Funktionen, die vom Part Arbeitsbereich herausgestellt werden. Daher gilt der Part Arbeitsbereich als die Kernkomponente der Modellierungsfunktionen von FreeCAD.

Eine detaillierte Diskussion des Arbeitsbereichs Part im Vergleich mit dem Arbeitsbereich Part Design findest du hier: [Part und Part Design](Part_and_Part_Design/de.md).

Die mit dem Part Arbeitsbereich erstellten Objekte sind relativ einfach; sie sind für die Verwendung mit booleschen Operationen (Verbindungen und Schnitte) vorgesehen, um komplexere Formen zu erstellen. **Dieses Modellierungsparadigma ist bekannt als _) modifiziert wird, bis das endgültige Objekt vorliegt.

Part Objekte sind komplexer als Polygonnetz Objekte, die mit dem [Arbeitsbereich Polygonnetz](Mesh_Workbench/de.md) erstellt wurden, da sie fortgeschrittene Abläufe wie kohärente boolesche Operationen, Änderungshistorie und parametrisches Verhalten ermöglichen.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*Der Part Arbeitsbereich ist die Basisschicht, die die OCCT Zeichenfunktionen allen Arbeitsbereichen in FreeCAD zur Verfügung stellt.*

## Werkzeuge

Die Werkzeuge befinden sich alle im **Part** Menü oder dem **Messung** Menü.

### Grundelemente

Dies sind Werkzeuge zum Erstellen von Grundobjekten.

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Quader](Part_Box/de.md): Zeichnet einen Quader

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Zylinder](Part_Cylinder/de.md): Zeichnet einen Zylinder.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Kugel](Part_Sphere/de.md): Zeichnet eine Kugel.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Kegel](Part_Cone/de.md): Zeichnet einen Kegel.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus/de.md): Zeichnet einen Torus (Ring).

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Rohr](Part_Tube/de.md): zeichnet ein Rohr. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Grundelemente](Part_Primitives/de.md): Ein Werkzeug zum Erstellen eines der folgenden Grundelemente:
    -   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Ebene](Part_Plane/de.md): Erzeugt eine Ebene.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> _ Werkzeug erzeugt werden.
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> _ Werkzeug erzeugt werden.
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> _ Werkzeug erzeugt werden.
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> _ Werkzeug erzeugt werden.
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid/de.md): Erzeugt einen Ellipsoid.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> _ Werkzeug erzeugt werden.
    -   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/de.md): Erzeugt ein Prisma.
    -   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Keil](Part_Wedge/de.md): Erzeugt einen Keil.
    -   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix/de.md): Erzeugt eine Helix.
    -   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spiral](Part_Spiral/de.md): Erzeugt einen Spirale.
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Kreis](Part_Circle/de.md): Erzeugt einen kreisförmige Kante.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/de.md): Erzeugt ein elliptische Kante.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punkt](Part_Point/de.md): Erzeugt einen Punkt (Knoten).
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linie](Part_Line/de.md): Erzeugt eine Linie (Kante).
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regelmäßiges Polygon](Part_RegularPolygon/de.md): Erzeugt eine regelmäßiges Polygon.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Bauer](Part_Builder/de.md): Erzeugt Formen aus verschiedenen Grundelementen.

### Erstellung und Änderung 

Dies sind Werkzeuge zum Erstellen neuer und Ändern vorhandener Objekte.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrudieren](Part_Extrude/de.md): Extrudiert ebene Flächen.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Drehen](Part_Revolve/de.md): Erzeugt einen Festkörper, indem ein anderes Objekt (nicht Volumenkörper) um eine Achse gedreht wird.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Soiegeln](Part_Mirror/de.md): Spiegelt das ausgewählte Objekt auf einer bestimmten Spiegelebene.

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Verrundung](Part_Fillet/de.md): Verrundet die Kanten eines Objekts.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Fase](Part_Chamfer/de.md): Anfasen von Kanten eines Objekts.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Fläche aus Drähten machen](Part_MakeFace/de.md): Erzeugt eine Fläche aus einem Satz von Drähten (Konturen). <small>(v0.19)</small> 

-   <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> [Regelfläche](Part_RuledSurface/de.md): Erzeugt eine Regelfläche.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Ausformung](Part_Loft/de.md): Ausformung von einem Profil zum anderen.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Austragung](Part_Sweep/de.md): Austragung von ein oder mehrerer Profile entlang eines Pfades.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Schnitt](Part_Section/de.md): Erzeugt einen Schnitt durch Überschneiden eines Objekts mit einer Schnittebene.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Querschnitte\...](Part_CrossSections/de.md): Erzeugt einen oder mehrere Querschnitte durch ein Objekt.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Versatz Werkzeuge](Part_CompOffsetTools/de.md):
    -   <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Versatz](Part_Offset/de.md): Konstruiert eine parallele Form in einem bestimmten Abstand zu einem Original.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Versatz](Part_Offset2D/de.md): Konstruiert einen parallelen Draht in einem bestimmten Abstand von einem Original oder vergrößert/schrumpft eine ebene Fläche.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Dicke](Part_Thickness/de.md): Höhlt einen Festkörper aus.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projektion auf Oberfläche](Part_ProjectionOnSurface/de.md): Projiziert ein Logo, einen Text oder eine beliebige Fläche, Draht, Kante auf eine Oberfläche. {{Version/de|0.19}}

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Anhang](Part_EditAttachment/de.md): Hängtt ein Objekt an ein anderes Objekt an.

### Boolesch

Diese Werkzeuge führen boolesche Operationen aus.

-   <img alt="" src=images/Part_Compound.svg  style="width:48px;"> [Verbund Werkzeuge](Part_CompCompoundTools/de.md):
    -   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Verbund herstellen](Part_Compound/de.md): Erzeugt einen Verbund aus den ausgewählten Objekten.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Sprenge Verbund](Part_ExplodeCompound/de.md): Teilt Verbünde auf.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Verbund Filter](Part_Compound‏‎Filter/de.md): Entnimmt den Verbünden die einzelnen Teile.

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolesche Operationen](Part_Boolean/de.md): Führt boolesche Operationen an Objekten durch.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Schneiden](Part_Cut/de.md): Schneidet (subtrahiert) ein Objekt von einem anderen.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Verschmelzen](Part_Fuse/de.md): Verschmilzt (vereinigt) zwei Objekte.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Vereinigung](Part_Common/de.md): Entnimmt den gemeinsamen Teil (Vereinigungsmenge) von zwei Objekten.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Fügt Funktionen](Part_CompJoinFeatures/de.md):
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Verbinden](Part_JoinConnect/de.md): Verbindet Innenräume von Hohlobjekten.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Einbetten](Part_JoinEmbed/de.md): Bettet ein Hohlobjekt in ein anderes Hohlobjekt ein.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Ausschneiden](Part_JoinCutout/de.md): Erzeugt einen Ausschnitt in einer Wand eines Objekts für ein anderes Hohlobjekt.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Teilungswerkzeuge](Part_CompSplittingTools/de.md):
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Boolesche Fragmente](Part_BooleanFragments/de.md): erzeugt alle Teile, die durch boolesche Operationen erhalten werden.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Zerteilen eines Teils](Part_SliceApart/de.md):

Zerschneidet und teilt ein Objekt, indem er es mit anderen Objekten überschneidet.

-   -   <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Zerschneiden](Part_Slice/de.md): Zerschneidet ein Objekt, indem es mit anderen Objekten überschnitten wird.
    -   <img alt="" src=images/Part_XOR.svg  style="width:32px;"> _).

### Messung

<img alt="" src=images/Part_Measure_Menu.png  style="width:64px;"> [Messung](Part_Measure_Menu/de.md): Werkzeuge für lineare und winklige Messungen.

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Linear messen](Part_Measure_Linear/de.md) Erzeugt eine lineare Messung.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Winkel messen](Part_Measure_Angular/de.md) Erzeugt eine Winkelmessung.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Messung aktualisieren](Part_Measure_Refresh/de.md) Aktualisiert alle Messungen.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Lösche Alles](Part_Measure_Clear_All/de.md) Löscht alle Messungen.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Alles umschalten](Part_Measure_Toggle_All/de.md) Zeigt oder blendet alle Messungen aus.

-   <img alt="" src=images/Part_Measure_Toggle_3d.svg  style="width:32px;"> [3D umschalten](Part_Measure_Toggle_3d/de.md) Zeigt oder blendet 3D Messungen aus.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Delta umschalten](Part_Measure_Toggle_Delta/de.md) Zeigt oder blendet Delta Messungen aus.

### Andere Werkzeuge 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Import](Part_Import/de.md): Importiert aus \*.IGES, \*.STEP, oder \*.BREP Dateien.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Export](Part_Export/de.md): Exportiert aus \*.IGES, \*.STEP, oder \*.BREP Dateien.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Rechteckauswahl](Part_BoxSelection/de.md): Zur Wählt Flächen aus Rechteckflächen aus.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Form aus Netz](Part_ShapeFromMesh/de.md): Erzeugt ein Formobjekt aus einem Netzobjekt.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Punkte aus Netz](Part_PointsFromMesh/de.md): erzeugt ein Formobjekt, erstellt aus Punkten eines Netzobjekts.

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;">[Umwandeln in Festkörper](Part_MakeSolid/de.md): Wandelt ein Formobjekt in ein Festkörperobjekt um.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width:32px;"> [Umgekehrte Formen](Part_ReverseShapes/de.md): Kehrt die Normalen aller Flächen des ausgewählten Objekts um.

-   Erstelle eine Kopie:
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"><img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Einfache Kopie erstellen](Part_SimpleCopy/de.md): Erstellt eine einfache Kopie eines ausgewählten Objekts.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Erstelle eine transformierte Kopie](Part_TransformedCopy/de.md): Erstellt eine transformierte Kopie des ausgewählten Objekts. {{Version/de|0.19}}
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [erstelle eine Kopie des Formelements](Part_ElementCopy/de.md): Erstellt eine Kopie eines Elements (Knoten, Kante, Fläche) eines ausgewählten Objekts. {{Version/de|0.19}}
    -   <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Form verfeinern](Part_RefineShape/de.md): Säubert Flächen durch entfernen unnötiger Linien.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Geometrie prüfen](Part_CheckGeometry/de.md): Prüft die Geometrie von ausgewählten Objekte auf Fehler.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing/de.md): Entfernt Formelemente aus einem Objekt.

### Kontextmenü Elemente 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Aussehen](Std_SetAppearance/de.md): Bestimmt das Aussehen des gesamten Objekts (Farbe, Transparenz usw.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Farben festlegen](Part_FaceColors/de.md): Weist den einzelnen Flächen von Objekten Farben zu.

## Einstellungen

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Einstellungen](PartDesign_Preferences/de.md): Einstellungen für Teilewerkzeuge verfügbar (der Part Arbeitsbereich verwendet auch die PartDesign Einstellungen).
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Einstellungen](Import_Export_Preferences/de.md): Einstellungen verfügbar für den Import aus und Export in verschiedene Dateiformate.
-   [Feinabstimmung](Fine-tuning/de.md): Einige zusätzliche Parameter zur Feineinstellung des Bauteilverhaltens.

## Skripten

Siehe [Part Skripten](Part_scripting/de.md)

## Tutorien

-   [Import aus STL oder OBJ](Import_from_STL_or_OBJ/de.md) : Kurzanleitung zum Import von STL/OBJ Dateien in FreeCAD
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md) : Kurzanleitung zum Export von STL/OBJ Dateien aus FreeCAD
-   [Whiffle Ball Tutorium](Whiffle_Ball_tutorial/de.md) : Kurzanleitung zur Verwendung des Part-Moduls





 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Part_Workbench.md) > Part Module/de
