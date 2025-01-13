# <img alt="Symbol des Arbeitsbereichs Part" src=images/Workbench_Part.svg  style="width:64px;"> Part Workbench/de






## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> **Part** verwendet einen herkömmlichen Arbeitsabläuf entsprechend der Methodik [konstruktive Festkörpergeometrie](Constructive_solid_geometry/de.md) (engl.: Constructive Solid Geometry, kurz CSG). In diesem Arbeitsablauf ist jedes Objekt ein unabhängiger Festkörper. Der Arbeitsbereich Part kann diese aus parametrisch festgelegten [Skizzen](Sketcher_Workbench/de.md) und dem Einsatz von Werkzeugen wie [Extrudieren\...](Part_Extrude/de.md), [Drehen\...](Part_Revolve/de.md), [Ausformung\...](Part_Loft/de.md) usw. erstellen. Außerdem können auch Grundkörper wie [Quader](Part_Box/de.md), [Zylinder](Part_Cylinder/de.md) usw. erstellt werden. Diese Objekte können durch [boolesche Verknüpfungen](Part_Boolean/de.md) kombiniert werden, um komplexere Festkörper zu erstellen.

Der Arbeitsbereiche Part kann auch Objekte erstellen, die keine Festkörper sind wie Flächen, Hüllen oder Objekte, die nur aus Kanten und Punkten bestehen. Er enthält auch unterschiedliche Werkzeuge für allgemeine Aufgaben wie das Bearbeiten von Geometrien, Prüfen von Geometrien und Erstellen von Kopien.

Der Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/de.md) verwendet einen alternativen Arbeitsabläufe zum Erstellen von Festkörpern. Eine detaillierte Diskussion der Arbeitsbereiche Part und Part Design im Vergleich befindet sich unter [Part und Part Design](Part_and_PartDesign/de.md).

![](images/Part_Workbench_Example.jpg )



## Werkzeuge



### Symbolleiste Volumenkörper 

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Quader](Part_Box/de.md): Erstellt einen Quader.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Zylinder](Part_Cylinder/de.md): Erstellt einen Zylinder.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Kugel](Part_Sphere/de.md): Erstellt eine Kugel.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Kegel](Part_Cone/de.md): Erstellt einen Kegel.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus/de.md): Erstellt einen Torus.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Rohr](Part_Tube/de.md): Erstellt ein Rohr (Hohlzylinder).

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Grundelemente erstellen\...](Part_Primitives/de.md): Ein Werkzeug zum Erstellen eines der folgenden Grundelemente:

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Ebene](Part_Plane/de.md): Erstellt eine Ebene.

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Quader](Part_Box/de.md): Erstellt einen Quader. Dieses Objekt kann auch mit dem Werkzeug [Quader](Part_Box/de.md) erstellt werden.

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Zylinder](Part_Cylinder/de.md): Erstellt einen Zylinder. Dieses Objekt kann auch mit dem Werkzeug [Zylinder](Part_Cylinder/de.md) erstellt werden.

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Kegel](Part_Cone/de.md): Erstellt einen Kegel. Dieses Objekt kann auch mit dem Werkzeug [Kegel](Part_Cone/de.md) erstellt werden.

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Kugel](Part_Sphere/de.md): Erstellt eine Kugel. Dieses Objekt kann auch mit dem Werkzeug [Kugel](Part_Sphere/de.md) erstellt werden.

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid/de.md): Erstellt einen Ellipsoid.

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus/de.md): Erstellt einen Torus. Dieses Objekt kann auch mit dem Werkzeug [Torus](Part_Torus/de.md) erstellt werden.

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/de.md): Erstellt ein Prisma.

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Keil](Part_Wedge/de.md): Erstellt einen Keil.

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix/de.md): Erstellt eine Wendel (Helix).

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/de.md): Erstellt einen Spirale.

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Kreis](Part_Circle/de.md): Erstellt einen kreisförmigen Bogen.

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/de.md): Erstellt einen elliptischen Bogen.

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punkt](Part_Point/de.md): Erstellt einen Punkt (Knoten).

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linie](Part_Line/de.md): Erstellt eine Linie.

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regelmäßiges Polygon](Part_RegularPolygon/de.md): Erstellt ein regelmäßiges Vieleck (Polygon).

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Formgenerator](Part_Builder/de.md): Erstellt Formen aus verschiedenen Grundelementen.



### Symbolleiste Part-Werkzeuge 

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Skizze erstellen](Sketcher_NewSketch/de.md): Erstellt eine neue Skizze und öffnet den [Sketcher-Dialog](Sketcher_Dialog/de.md), um sie zu bearbeiten.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrudieren](Part_Extrude/de.md): Extrudiert ebene Flächen.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Drehen](Part_Revolve/de.md): Erstellt einen Festkörper, indem ein Objekt (das kein Festkörper ist) um eine Achse gedreht wird.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Spiegeln](Part_Mirror/de.md): Spiegelt das ausgewählte Objekt über eine Spiegelebene.

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Skalieren](Part_Scale/de.md): Skaliert eine oder mehrere Formen. {{Version/de|1.0}}

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Verrundung](Part_Fillet/de.md): Verrundet die Kanten eines Objekts.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Fase](Part_Chamfer/de.md): Erstellt Fasen an den Kanten eines Objekts.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Fläche aus Linienzügen](Part_MakeFace/de.md): Erstellt eine Fläche aus einem Satz geschlossener Drähte (Konturen/Linienzüge).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Regelfläche](Part_RuledSurface/de.md): Erstellt eine Regelfläche.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Ausformung](Part_Loft/de.md): Erstellt eine Ausformung von einem Profil zu einem anderen.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Austragung](Part_Sweep/de.md): Erstellt eine Austragung eines oder mehrerer Profile entlang eines Pfades.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Schnittkurve](Part_Section/de.md): Erstellt Schnittkurven durch Überschneiden eines Objekts mit einem anderen Objekt.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Querschnitte\...](Part_CrossSections/de.md): Erzeugt einen oder mehrere Querschnitte durch ein Objekt.

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Versatz:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Versatz](Part_Offset/de.md): Konstruiert eine parallele Form in einem bestimmten Abstand zu einem Original.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Versatz](Part_Offset2D/de.md): Konstruiert einen parallelen Draht in einem bestimmten Abstand von einem Original oder vergrößert/schrumpft eine ebene Fläche.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Dicke](Part_Thickness/de.md): Höhlt einen Festkörper aus.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projektion auf Oberfläche](Part_ProjectionOnSurface/de.md): Projiziert ein Logo, einen Text oder eine beliebige Fläche, Draht, Kante auf eine Oberfläche.

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Farbe pro Fläche](Part_ColorPerFace.md): Weist den einzelnen Flächen von Objekten Farben zu.



### Symbolleiste Boolesche Verknüpfung 

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Verbund:

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Verbund erstellen](Part_Compound/de.md): Erstellt einen Verbund aus den ausgewählten Objekten.

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Verbund sprengen](Part_ExplodeCompound/de.md): Teilt Verbundobjekte auf.

  - <img alt="" src=images/Part_CompoundFilter.svg  style="width:32px;"> [Verbundfilter](Part_CompoundFilter/de.md): Entnimmt die einzelnen Stücke aus Verbundobjekten.

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolesche Verknüpfungen](Part_Boolean/de.md): Führt boolesche Verknüpfungen mit zwei Objekten durch.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Differenz](Part_Cut/de.md): Beschneidet ein Objekt mit einem anderen.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Vereinigung](Part_Fuse/de.md): Vereinigt zwei oder mehr Objekte.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Schnitt](Part_Common/de.md): Entnimmt den gemeinsamen Teil (Schnittmenge) von zwei Objekten.

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Objekte verbinden:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Objekte verbinden](Part_JoinConnect/de.md): Vereinigt die umschlossenen Volumen von Hohlobjekten.

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Objekt einbetten](Part_JoinEmbed/de.md): Bettet ein Hohlobjekt in ein anderes Hohlobjekt ein.

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Für Objekt ausschneiden](Part_JoinCutout/de.md): Erzeugt einen Ausschnitt in einer Wand eines Objekts für ein anderes Hohlobjekt.

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Aufteilung:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [BoolescheFragmente](Part_BooleanFragments/de.md): erzeugt alle Teile, die durch boolesche Operationen erhalten werden.

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Auseinanderschneiden](Part_SliceApart/de.md): Zerschneidet und teilt ein Objekt, indem es mit anderen Objekten geschnitten wird.

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Schneiden zu Verbund](Part_Slice/de.md): Zerschneidet ein Objekt, indem es mit anderen Objekten geschnitten wird.

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [Boolesches exklusives Oder (XOR)](Part_XOR/de.md): Entfernt Bereiche, die zu einer geraden Anzahl von Objekten gehören.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Geometrie prüfen](Part_CheckGeometry/de.md): Prüft die Geometrie von ausgewählten Objekte auf Fehler.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing/de.md): Entfernt Formelemente aus einem Objekt.



### Andere Werkzeuge 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Aus CAD-Datei importieren\...](Part_Import/de.md): Importiert aus \*.IGES-, \*.STEP-, oder \*.BREP-Dateien.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [In CAD-Datei exportieren\...](Part_Export/de.md): Exportiert in \*.IGES-, \*.STEP-, oder \*.BREP- Dateien.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Rechteckauswahl](Part_BoxSelection/de.md): Wählt Flächen mit einem Auswahlrechteck aus.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Form aus Dreiecksnetz erstellen](Part_ShapeFromMesh/de.md): Erstellt Formen aus Netzobjekten.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Punktobjekt aus Geometrie erstellen](Part_PointsFromMesh/de.md): erstellt Punkteobjekte aus geometrischen Objekten.

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;">[In Festkörper umwandeln](Part_MakeSolid/de.md): Erstellt Festkörper aus Formobjekten.

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Formen umkehren](Part_ReverseShape/de.md): Erstellt aus ausgewählten Objekten parametrische Kopien mit umgekehrten Flächennormalen.

-   Erstelle eine Kopie:

  - <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Einfache Kopie erstellen](Part_SimpleCopy/de.md): Erstellt nichtparametrische Kopien ausgewählter Objekte.

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Transformierte Kopie erstellen](Part_TransformedCopy/de.md): Erstellt nichtparametrische Kopien von Objekten. Dies ist gedacht für Objekte, die in Behältern eingebettet sind.

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Formelement-Kopie erstellen](Part_ElementCopy/de.md): Erstellt nichtparametrische Kopien von Unterelementen: Knoten, Kanten und Flächen.

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Form aufbereiten](Part_RefineShape/de.md): Erstellt aus ausgewählten Objekten parametrische Kopien mit aufbereiteten Formen. Dies entfernt überflüssige Kanten von ebenen und zylindrischen Flächen.

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Befestigung](Part_EditAttachment/de.md): Befestigt ein Objekt an ein oder mehrere andere Objekte.



## Veraltete Werkzeuge 



### Messwerkzeuge

Das Werkzeug <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Std Measure](Std_Measure/de.md) ersetzt die folgend gelisteten Werkzeuge. {{Version/de|1.0}}

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Linear messen](Part_Measure_Linear/de.md) Erzeugt eine lineare Messung. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Winkel messen](Part_Measure_Angular/de.md) Erzeugt eine Winkelmessung. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Messung aktualisieren](Part_Measure_Refresh/de.md) Aktualisiert alle Messungen. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Alles löschen](Part_Measure_Clear_All/de.md) und [Messung löschen](View_Measure_Clear_All/de.md) Löscht alle Messungen. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Messung AlleUmschalten](Part_Measure_Toggle_All/de.md) und [Ansicht Messen alle löschen](View_Measure_Toggle_All/de.md): Zeigt alle Messungen an oder blendet sie aus. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [3D umschalten](Part_Measure_Toggle_3D/de.md) Zeigt 3D-Messungen an oder blendet sie aus. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Delta umschalten](Part_Measure_Toggle_Delta/de.md) Zeigt oder blendet Delta Messungen aus. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.



## Einstellungen

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Einstellungen](PartDesign_Preferences/de.md): Einstellungen für den Arbeitsbereich Part.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import-/Export-Einstellungen](Import_Export_Preferences/de.md): Einstellungen für den Import aus unterschiedlichen und den Export in unterschiedliche Dateiformate.
-   [Feinabstimmung](Fine-tuning/de#Arbeitsbereich_Part.md): Einige zusätzliche Parameter zur Feineinstellung des Verhaltens des Arbeitsbereichs Part.



## Skripten

Siehe [Part Skripten](Part_scripting/de.md)



## Tutorien

-   [Import aus STL oder OBJ](Import_from_STL_or_OBJ/de.md): Kurzanleitung zum Import von STL/OBJ Dateien in FreeCAD
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md): Kurzanleitung zum Export von STL/OBJ Dateien aus FreeCAD
-   [Whiffle Ball Tutorium](Whiffle_Ball_tutorial/de.md): Kurzanleitung zur Verwendung des Part-Arbeitsbereiches



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/de
