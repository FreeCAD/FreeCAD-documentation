# <img alt="Symbol des Arbeitsbereichs PartDesign" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/de






## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> **PartDesign** enthält Werkzeuge zum Modellieren von Festkörperkomponenten. Sein Fokus liegt hauptsächlich auf der Erstellung mechanischer Komponenten, die hergestellt und zu einem Endprodukt montiert werden können. Dennoch können die erzeugten Körper generell für jeden anderen Zweck verwendet werden, wie z.B. [Bauwerksdatenmodellierung](BIM_Workbench/de.md) (BIM), [Finite-Elemente-Analyse](FEM_Workbench/de.md), oder [CNC-Bearbeitung und 3D-Druck](CAM_Workbench/de.md).

Der Arbeitsbereich PartDesign verwendet eine auf Formelementen basierende Methodik. Eine Komponente wird durch einen Behälter Körper dargestellt (Body object container). Der Körper legt ein lokales Koordinatensystem fest und enthält die gesamten Formelemente, die die Komponente aufbauen. Die meisten Formelemente basieren auf parametrischer Skizzen sind hinzufügend oder abziehend. Z.B. fügt das Werkzeug [Pad](PartDesign_Pad/de.md) die extrudierte Skizze zum sich entwickelnden Festkörper hinzu, während das Werkzeug [Vertiefung](PartDesign_Pocket/de.md) die extrudierte Skizze abzieht. Jedes Formelement trägt zum Gesamtergebnis bei und baut dabei auf dem Ergebnis der vorherigen Formelemente auf. Es können auch Grundkörper (primitives) wie [Zylinder](PartDesign_AdditiveCylinder/de.md), [Kugeln](PartDesign_AdditiveSphere/de.md) usw. sowie Festkörper, die außerhalb des Körpers erstellt wurden, als Formelemente verwendet werden.

Siehe die Seite [Formelemente bearbeiten](Feature_editing/de.md) für eine umfassendere Erklärung dieses Prozesses und anschließend [Erstellen eines einfachen Bauteils mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md), um mit dem Erstellen von Festkörpern loszulegn.

Der Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/de.md) verwendet zum Erstellen von Festkörpern die alternative Methodik der [konstruktiven Festkörpergeometrie](constructive_solid_geometry/de.md) (engl.: Constructive Solid Geometry, kurz CSG). Eine detaillierte Diskussion der Arbeitsbereiche Part und Part Design im Vergleich befindet sich unter [Part und Part Design](Part_and_PartDesign/de.md).

![](images/PartDesign_Workbench_Example.jpg )



## Werkzeuge

Die Werkzeuge für PartDesign befinden sich alle im Menü **Part Design** und in der PartDesign-Symbolleiste, die beim Laden des Arbeitsbereichs angezeigt wird.



### Hilfswerkzeuge Part Design 

-   <img alt="" src=images/PartDesign_Body.png  style="width:32px;"> [Körper erstellen](PartDesign_Body/de.md): Erstellt einen [Körper](Body/de.md) (Body object) im aktiven Dokument und aktiviert ihn.

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Skizze erstellen:

  - <img alt="" src=images/PartDesign_NewSketch.svg  style="width:32px;"> [Skizze erstellen](PartDesign_NewSketch/de.md): erstellt eine neue Skizze auf einer ausgewählten Fläche oder Ebene. Wenn vor der Ausführung dieses Werkzeugs keine Fläche ausgewählt wurde, wird der Anwender aufgefordert, eine Ebene im Aufgaben-Bereich auszuwählen. Die Schnittstelle wechselt dann zum Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) in den Bearbeitungsmodus.

  - <img alt="" src=images/Sketcher_MapSketch.png‎  style="width:32px;"> [Skizze befestigen\...](Sketcher_MapSketch/de.md): Heftet eine Skizze an eine Geometrie, die am aktiven Körper ausgewählt wurde.

  - <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Skizze bearbeiten](Sketcher_EditSketch/de.md): Öffnet die ausgewählte Skizze zum Bearbeiten.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Skizze überprüfen](Sketcher_ValidateSketch/de.md): Überprüft die Toleranz verschiedener Punkte und passt sie an.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Geometrie prüfen](Part_CheckGeometry/de.md): Prüft die Geometrie von ausgewählten Objekte auf Fehler.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Formbinder erstellen](PartDesign_ShapeBinder/de.md): Erzeugt einen Formbinder, der Geometrie eines einzelnen übergeordneten Objekts referenziert.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Teilformbinder erstellen](PartDesign_SubShapeBinder/de.md): Erstellt einen Teilformbinder der Geometrie von einem oder mehreren übergeordneten Objekten referenziert.

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Klon erstellen](PartDesign_Clone/de.md): Erstellt einen Klon des ausgewählten Körpers.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Bezugselement erstellen (

  -<img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Bezugsebene erstellen](PartDesign_Plane/de.md): Erstellt eine Bezugsebene im aktiven Körper. ({{VersionMinus/de|1.0}})

  -<img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Bezugslinie erstellen](PartDesign_Line/de.md): Erstellt eine Bezugslinie im aktiven Körper. ({{VersionMinus/de|1.0}})

  -<img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Bezugspunkt erstellen](PartDesign_Point/de.md): Erstellt einen Bezugspunkt im aktiven Körper. ({{VersionMinus/de|1.0}})

  -<img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Lokales Koordinatensystem erstellen](PartDesign_CoordinateSystem/de.md): Erstellt ein lokales Koordinatensystem, das an der Bezugsgeometrie im aktiven Körper angeheftet ist. ({{VersionMinus/de|1.0}})

:   
    <small>(v1.1)</small> : these tools have been replaced by new [datum tools](Std_Base#Part_Datums.md).



### Modellierungswerkzeuge Part Design 



#### Additive Werkzeuge 

Dies sind Werkzeuge zum Erstellen von Basisformelementen oder zum Hinzufügen von Material zu einem bestehenden Körper.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Aufpolsterung](PartDesign_Pad/de.md): Extrudiert einen Volumenkörper aus einer ausgewählten Skizze.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Rotation](PartDesign_Revolution/de.md): Erzeugt einen Drehkörper, durch drehen einer Skizze um eine Achse. Die Skizze muss ein geschlossenes Profil ergeben.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Additive Ausformung](PartDesign_AdditiveLoft/de.md): Erzeugt einen Volumenkörper, indem ein Übergang zwischen zwei oder mehr Skizzen erstellt wird.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Additives Rohr](PartDesign_AdditivePipe/de.md): Erzeugt einen Volumenkörper, indem eine oder mehrere Skizzen entlang eines offenen oder geschlossenen Pfades ausgetragen wird.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Additive Helix](PartDesign_AdditiveHelix/de.md): erzeugt einen Festkörper durch Austragen einer Skizze entlang einer Wendel.

-   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Grundkörper hinzufügen:

  -<img alt="" src=images/PartDesign_Additive_Box.svg  style="width:32px;"> [Quader](PartDesign_AdditiveBox/de.md): Erstellt einen additiven Quader. {{Version/de|0.17}}

  -<img alt="" src=images/PartDesign_Additive_Cylinder.svg  style="width:32px;"> [Zylinder](PartDesign_AdditiveCylinder/de.md): Erstellt einen additiven Zylinder.

  -<img alt="" src=images/PartDesign_Additive_Sphere.svg  style="width:32px;"> [Kugel](PartDesign_AdditiveSphere/de.md): Erstellt eine additive Kugel.

  -<img alt="" src=images/PartDesign_Additive_Cone.svg  style="width:32px;"> [Kegel](PartDesign_AdditiveCone/de.md): Erstellt einen additiven Kegel. {{Version/de|0.17}}

  -<img alt="" src=images/PartDesign_Additive_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](PartDesign_AdditiveEllipsoid/de.md): Erstellt ein additives Ellipsoid.

  -<img alt="" src=images/PartDesign_Additive_Torus.svg  style="width:32px;"> [Torus](PartDesign_AdditiveTorus/de.md): Erstellt einen additiven Torus.

  -<img alt="" src=images/PartDesign_Additive_Prism.svg  style="width:32px;"> [Prisma](PartDesign_AdditivePrism/de.md): Erstellt ein additives Prisma.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Keil](PartDesign_AdditiveWedge/de.md): Erstellt einen additiven Keil.



#### Subtraktive Werkzeuge 

Dies sind Werkzeuge, um Material von einem bestehenden Körper abzuziehen.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Tasche](PartDesign_Pocket/de.md): Erstellt eine Tasche aus einer ausgewählten Skizze.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Bohrung](PartDesign_Hole/de.md): Erstellt ein Bohrungsmerkmal aus einer ausgewählten Skizze. Die Skizze muss einen oder mehrere Kreise enthalten.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Nut](PartDesign_Groove/de.md): Erzeugt eine Nut, indem eine Skizze um eine Achse gedreht wird.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Subtraktive Ausformung](PartDesign_SubtractiveLoft/de.md):

Erzeugt eine Körperform, indem es einen Übergang zwischen zwei oder mehreren Skizzen macht und diese vom aktiven Körper subtrahiert.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Subtraktives Rohr](PartDesign_SubtractivePipe/de.md):

Erzeugt eine Volumenkörperform, indem eine oder mehrere Skizzen entlang eines offenen oder geschlossenen Pfades ausgetragen und diese vom aktiven Körper abgezogen wird.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtraktive helix](PartDesign_SubtractiveHelix/de.md): erzeugt eine Festkörperform, indem eine Skizze entlang einer Helix ausgetragen wird, und subtrahiert sie vom aktiven Körper.

-   <img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Grundkörper abziehen:

  -<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Quader](PartDesign_SubtractiveBox/de.md): fügt dem aktiven Körper eine subtraktiven Quader hinzu.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Zylinder](PartDesign_SubtractiveCylinder/de.md): fügt dem aktiven Körper einen subtraktiven Zylinder hinzu.

  -<img alt="" src=images/PartDesign_Subtractive_Sphere.svg  style="width:32px;"> [Kugel](PartDesign_SubtractiveSphere/de.md): fügt dem aktiven Körper eine subtraktive Kugel hinzu.

  -<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Kegel](PartDesign_SubtractiveCone/de.md): fügt dem aktiven Körper einen subtraktiven Kegel hinzu.

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Ellipsoid](PartDesign_SubtractiveEllipsoid/de.md): fügt dem aktiven Körper ein subtraktives Ellipsoid hinzu.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Torus](PartDesign_SubtractiveTorus/de.md): fügt dem aktiven Körper einen subtraktiven Ring hinzu.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Prisma](PartDesign_SubtractivePrism/de.md): fügt dem aktiven Körper ein subtraktives Prisma hinzu.

  -<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Keil](PartDesign_SubtractiveWedge/de.md): fügt dem aktiven Körper einen subtraktiven Keil hinzu.



#### Boolesche Operationen 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Boolesche Operation](PartDesign_Boolean/de.md): importiert einen oder mehrere Körper oder PartDesign Klone in den aktiven Körper und führt eine Boolesche Operation aus.



### Modifikationswerkzeuge

Diese Werkzeuge modifizieren Kanten und Flächen.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Verrundung](PartDesign_Fillet/de.md): Verrundungen (Rundungen) der Kanten des aktiven Körpers.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Fase](PartDesign_Chamfer/de.md): fast die Kanten des aktiven Körpers an.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Entwurf](PartDesign_Draft/de.md): wendet einen winkligen Entwurf auf ausgewählte Flächen des aktiven Körpers an.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Dicke](PartDesign_Thickness/de.md): erzeugt ein Schalenobjekt (mit konstanter Wandstärke) aus dem aktiven Körper und öffnet ausgewählte Flächen.



### Transformationswerkzeuge

Dies sind Werkzeuge zur Transformation bestehender Formelemente.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Spiegeln](PartDesign_Mirrored/de.md): Spiegelt ein oder mehrere Formelemente.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Lineares Muster](PartDesign_LinearPattern/de.md) erstellt ein lineares Muster aus einem oder mehreren Formelementen.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Polares Muster](PartDesign_PolarPattern/de.md): Erstellt ein polares Muster aus einem oder mehreren Formelemente.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Mehrfachtransformation](PartDesign_MultiTransform/de.md): Erzeugt ein Muster durch eine beliebige Kombination der oben gelisteten Transformationen und der Transformation [Skalieren](PartDesign_Scaled/de.md).
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [Skalieren](PartDesign_Scaled/de.md): Skaliert ein oder mehrere Formelemente. Dieses steht nicht als eigenständiges Transformationswerkzeug zur Verfügung.

#### Extras

Einige zusätzliche Funktionen befinden sich im Menü Part Design:

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Kettenrad](PartDesign_Sprocket/de.md): Erstellt ein Kettenradprofil, das extrudiert werden kann.

-   <img alt="" src=images/PartDesign_InvoluteGear.svg  style="width:32px;"> [Evolventenzahnrad](PartDesign_InvoluteGear/de.md): erzeugt ein Evolventenzahnradprofil, das extrudiert werden kann.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Wellenauslegungsassistent](PartDesign_WizardShaft/de.md): Erzeugt eine Welle aus einer Wertetabelle und ermöglicht die Analyse von Kräften und Momenten. Die Welle wird mit einer umlaufenden Skizze erstellt, die bearbeitet werden kann.



### Kontextmenü Elemente 

-   [Unterdrückt](PartDesign_Suppressed/de.md): Checkbox zum Deaktivieren eines bestimmten Formelements ohne es zu löschen. {{Version/de|1.0}}

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Spitze setzen](PartDesign_MoveTip/de.md): definiert die Spitze neu, das ist das Merkmal, das außerhalb des Körpers erscheint.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Objekt in anderen Körper verschieben](PartDesign_MoveFeature/de.md): verschiebt die ausgewählte Skizze, Bezugsgeometrie oder das Formelement in einen anderen Körper.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Objekt nach anderem Objekt verschieben](PartDesign_MoveFeatureInTree/de.md): ermöglicht eine Neuordnung des Körperbaums, indem die ausgewählte Skizze, Bezugsgeometrie oder das Formelement an eine andere Position in der Formelementliste verschoben wird.



#### Mit dem Part Arbeitsbereich gemeinsam genutzte Elemente 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Aussehen](Std_SetAppearance/de.md): bestimmt das Aussehen des gesamten Teils (Farbtransparenz usw.).

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Farbe pro Fläche](Part_ColorPerFace.md): Weist den einzelnen Flächen von Objekten Farben zu.



### Veraltete Werkzeuge 

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrieren](PartDesign_Migrate/de.md): migriert Dateien von FreeCAD Versionen unter 0.17 zu Version 0.17. Dieses Werkzeug ist nicht verfügbar in <small>(v1.0)</small> .



## Einstellungen

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Einstellungen](PartDesign_Preferences/de.md): Einstellungen verfügbar für PartDesign Werkzeuge.
-   [Feinabstimmung](Fine-tuning/de.md): Einige zusätzliche Parameter zur Feinabstimmung des PartDesign Verhaltens



## Tutorien

-   [Wie FreeCAD anwenden](http://help-freecad-jpg87.fr/), eine Netzseite, die den Arbeitsablauf für die mechanische Konstruktion beschreibt.
-   [Erstellen eines einfachen Teils mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md)
-   [Grundlegende PartDesign-Anleitung 019](Basic_Part_Design_Tutorial_019/de.md)
-   [PartDesign Lagerträger Tutorial I](PartDesign_Bearingholder_Tutorial_I/de.md) (muss aktualisiert werden)
-   [PartDesign Lagerträger Tutorial II](PartDesign_Bearingholder_Tutorial_II/de.md) (muss aktualisiert werden)



## Beispiele

Ein paar Ideen, was mit den Part-Design-Werkzeugen erstellt werden kann, findet man unter: [PartDesign Beispiele](PartDesign_Examples/de.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">





 {{PartDesign_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/de
