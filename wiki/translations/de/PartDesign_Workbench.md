# <img alt="PartDesign Arbeitsbereichsymbol" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/de


{{TOCright}}

## Einführung

Der <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">[Arbeitsbereich PartDesign ](PartDesign_Workbench/de.md) bietet erweiterte Werkzeuge zur Modellierung komplexer Festkörper. Er konzentriert sich hauptsächlich auf die Erstellung mechanischer Teile, die hergestellt und zu einem Endprodukt montiert werden können. Dennoch können die erzeugten Körper generell für jeden anderen Zweck verwendet werden, wie z.B. [Architekturdesign](Arch_Workbench/de.md), [Finite Element Analyse](FEM_Workbench/de.md), oder [CNC-Bearbeitung und 3D Druck](Path_Workbench/de.md).

Der Arbeitsbereich PartDesign ist eng mit dem [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md) verbunden. Der Anwender erstellt normalerweise eine Skizze, verwendet dann das Werkzeug [PartDesign Aufpolsterung](PartDesign_Pad/de.md), um sie zu extrudieren und einen Basis Körper zu erstellen, anschließend wird dieser Körper weiter modifiziert.

Während der <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Arbeitsbereich Part](Part_Workbench/de.md) auf einer [konstruktiven Festkörpergeometrie](constructive_solid_geometry/de.md) (CSG) Methodik (engl.: Constructive Solid Geometry) für das Erstellen von Formen basiert, verwendet der Arbeitsbereich PartDesign eine parametrische Merkmal Bearbeitungsmethodik, d.h. ein Basis Körper wird sequentiell transformiert, indem Merkmale hinzugefügt werden, bis die endgültige Form erreicht ist. Um mit der Erstellung von Körpern zu beginnen, siehe die Seiten [Formelement bearbeiten](feature_editing/de.md) für eine ausführlichere Erläuterung dieses Vorgangs, und [Erstellen eines einfachen Teil mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md).

Eine detaillierte Diskussion des Arbeitsbereichs Part im Vergleich mit dem Arbeitsbereich Part Design findest du hier: [ Part und PartDesign](Part_and_PartDesign/de.md).

Die mit PartDesign erstellten Körper unterliegen oft dem [topologischen Benennungsproblem](Topological_naming_problem/de.md), wodurch bei Änderungen an den parametrischen Operationen interne Formelemente umbenannt werden. Dieses Problem kann minimiert werden, indem die auf der Seite [Formelemente bearbeiten](feature_editing/de.md) beschriebenen Erfolgsrezepte befolgt und die Vorteile von Bezugsobjekten als Unterstützung für Skizzen und Features genutzt werden.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Werkzeuge

Die Werkzeuge für PartDesign befinden sich alle im Menü {{MenuCommand/de|Part Design}} und in der PartDesign Werkzeugleiste, die beim Laden des Arbeitsbereichs angezeigt wird.

### Strukturwerkzeuge

Diese Werkzeuge sind gar keine Bestandteile des Arbeitsbereichs PartDesign. Sie gehören zum System [Std Base](Std_Base.md). Sie wurden in v0.17 mit der Absicht entwickelt, dass sie nützlich sein könnten, um ein Modell zu strukturieren und [Baugruppen](Assembly/de.md) zu erstellen.

-   <img alt="" src=images/Std_Part.png  style="width:32px;"> [Teil](Std_Part/de.md): fügt einen neuen Teilecontainer in das aktive Dokument ein und aktiviert ihn.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Gruppe](Std_Group/de.md): fügt einen Gruppencontainer in das aktive Dokument ein, der es erlaubt, die Objekte in der [Baumansicht](Tree_view/de.md) zu ordnen.

### Hilfswerkzeuge Part Design 

-   <img alt="" src=images/PartDesign_Body.png  style="width:32px;"> [Körper erstellen](PartDesign_Body/de.md): Erzeugen und aktivieren eines neuen [Körpers](Body/de.md).

-   <img alt="" src=images/PartDesign_NewSketch.png  style="width:32px;"> [Skizze erstellen](PartDesign_NewSketch/de.md): erstellt eine neue Skizze auf einer ausgewählten Fläche oder Ebene. Wenn vor der Ausführung dieses Werkzeugs keine Fläche ausgewählt wurde, wird der Anwender aufgefordert, eine Ebene aus dem Aufgabenbereich auszuwählen. Die Schnittstelle wechselt dann im Bearbeitungsmodus

in den [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md).

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Skizze bearbeiten](Sketcher_EditSketch/de.md): Bearbeiten der ausgewählten Skizze.

-   <img alt="" src=images/Sketcher_MapSketch.png‎  style="width:32px;"> [Eine Skizze einer Fläche zuordnen](Sketcher_MapSketch/de.md): Ordnet eine Skizze einer zuvor ausgewählten Ebene oder einer Fläche des aktiven Körpers zu.

### Modellierungswerkzeuge Part Design 

#### Bezugsswerkzeuge

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Bezugspunkt erstellen](PartDesign_Point/de.md): Erstellt einen Bezugspunkt im aktiven Körper. {{Version/de|0.17}}

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Bezugslinie erstellen](PartDesign_Line/de.md): Erstellt eine Bezugslinie im aktiven Körper. {{Version/de|0.17}}

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Bezugsebene erstellen](PartDesign_Plane/de.md): Erstellt eine Bezugsfläche im aktiven Körper. {{Version/de|0.17}}

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Erzeugt ein lokales Koordinatensystem](PartDesign_CoordinateSystem/de.md):

Erzeugt ein lokales Koordinatensystem, das an der Bezugsgeometrie im aktiven Körper angelegt ist.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Formbinder erstellen](PartDesign_ShapeBinder/de.md): Erzeugt einen Formbinder im aktiven Körper.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Unterobjekt FormBinder erstellen](PartDesign_SubShapeBinder/de.md): Erzeugt einen FormBinder zu einem Unterelement, wie eine Kante oder Fläche eines anderen Körpers, wobei die relative Position des Elements beibehalten wird. {{Version/de|0.19}}

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Klon erstellen](PartDesign_Clone/de.md): Erstellt einen Klon des ausgewählten Körpers.

#### Additive Werkzeuge 

Dies sind Werkzeuge zum Erstellen von Basisformelementen oder zum Hinzufügen von Material zu einem bestehenden Körper.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Aufpolsterung](PartDesign_Pad/de.md): polstert eine selektierte Skizze auf.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Rotation](PartDesign_Revolution/de.md): erzeugt einen Körper, indem eine Skizze um eine Achse gedreht wird. Die Skizze muss geschlossen sein.

-   <img alt="" src=images/PartDesign_Additive_Loft.svg  style="width:32px;"> [Additive Ausformung](PartDesign_AdditiveLoft/de.md): Erzeugt einen Volumenkörper, indem ein Übergang zwischen zwei oder mehreren Skizzen erstellt wird.

-   <img alt="" src=images/PartDesign_Additive_Pipe.svg  style="width:32px;"> [Additives Rohr](PartDesign_AdditivePipe/de.md): Erzeugt einen Volumenkörper, indem eine oder mehrere Skizzen entlang eines offenen oder geschlossenen Pfades ausgetragen wird.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Additive Helix](PartDesign_AdditiveHelix/de.md): erzeugt einen Festkörper durch Austragen einer Skizze entlang einer Helix. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Zusätzlicher Grundkörper](PartDesign_CompPrimitiveAdditive/de.md): fügt dem aktiven Körper einen additiven Grundkörper hinzu. {{Version/de|0.17}}

:\*<img alt="" src=images/PartDesign_Additive_Box.svg  style="width:32px;"> [zu addierender Quader](PartDesign_AdditiveBox/de.md): Erstellt einen additiven Quader. {{Version/de|0.17}}

:\*<img alt="" src=images/PartDesign_Additive_Cone.svg  style="width:32px;"> [zu addierender Kegel](PartDesign_AdditiveCone/de.md): Erstellt einen additiven Kegel. {{Version/de|0.17}}

:\*<img alt="" src=images/PartDesign_Additive_Cylinder.svg  style="width:32px;"> [zu addierender Zylinder](PartDesign_AdditiveCylinder/de.md): Erstellt einen additiven Zylinder.

:\*<img alt="" src=images/PartDesign_Additive_Ellipsoid.svg  style="width:32px;"> [zu addierendes Ellipsoid](PartDesign_AdditiveEllipsoid/de.md): Erstellt ein additives Ellipsoid.

:\*<img alt="" src=images/PartDesign_Additive_Prism.svg  style="width:32px;"> [zu addierendes Prisma](PartDesign_AdditivePrism/de.md): Erstellt ein additives Prisma.

:\*<img alt="" src=images/PartDesign_Additive_Sphere.svg  style="width:32px;"> [zu addierende Kugel](PartDesign_AdditiveSphere/de.md): Erstellt eine additive Kugel.

:\*<img alt="" src=images/PartDesign_Additive_Torus.svg  style="width:32px;"> [zu addierender Torus](PartDesign_AdditiveTorus/de.md): Erstellt einen additiven Torus.

:\*<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [zu addierender Keil](PartDesign_AdditiveWedge/de.md): Erstellt einen additiven Keil.

#### Subtraktive Werkzeuge 

Dies sind Werkzeuge, um Material von einem bestehenden Körper abzuziehen.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Tasche](PartDesign_Pocket/de.md): Erstellt eine Tasche aus einer ausgewählten Skizze.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Bohrung](PartDesign_Hole/de.md): Erstellt ein Bohrungsmerkmal aus einer ausgewählten Skizze. Die Skizze muss einen oder mehrere Kreise enthalten.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Nut](PartDesign_Groove/de.md): Erzeugt eine Nut, indem eine Skizze um eine Achse gedreht wird.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Subtraktive Ausformung](PartDesign_SubtractiveLoft/de.md):

Erzeugt eine Körperform, indem es einen Übergang zwischen zwei oder mehreren Skizzen macht und diese vom aktiven Körper subtrahiert.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Subtraktives Rohr](PartDesign_SubtractivePipe/de.md):

Erzeugt eine Volumenkörperform, indem eine oder mehrere Skizzen entlang eines offenen oder geschlossenen Pfades ausgetragen und diese vom aktiven Körper abgezogen wird.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtraktive helix](PartDesign_SubtractiveHelix/de.md): erzeugt eine Volumenkörperform, indem eine Skizze entlang einer Helix ausgetragen wird, und subtrahiert sie vom aktiven Körper. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Erzeuge einen abzuziehenden Grundkörper](PartDesign_CompPrimitiveSubtractive/de.md): Fügt einen abzuziehenden Grundkörper zum aktiven Körper hinzu.

:\*<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Abzugsquader](PartDesign_SubtractiveBox/de.md): fügt dem aktiven Körper eine subtraktiven Quader hinzu.

:\*<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Abzuziehender Kegel](PartDesign_SubtractiveCone/de.md): fügt dem aktiven Körper einen subtraktiven Kegel hinzu.

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Abzuziehender Zylinder](PartDesign_SubtractiveCylinder/de.md): fügt dem aktiven Körper einen subtraktiven Zylinder hinzu.

:\*<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Abzuziehendes Ellipsoid](PartDesign_SubtractiveEllipsoid/de.md): fügt dem aktiven Körper ein subtraktives Ellipsoid hinzu.

:\*<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Abzuziehendes Prisma](PartDesign_SubtractivePrism/de.md): fügt dem aktiven Körper ein subtraktives Prisma hinzu.

:\*<img alt="" src=images/PartDesign_Subtractive_Sphere.svg  style="width:32px;"> [Abzuziehende Kugel](PartDesign_SubtractiveSphere/de.md): fügt dem aktiven Körper eine subtraktive Kugel hinzu.

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Abzuziehender Torus](PartDesign_SubtractiveTorus/de.md): fügt dem aktiven Körper einen subtraktiven Ring hinzu.

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Abzuziehender Keil](PartDesign_SubtractiveWedge/de.md): fügt dem aktiven Körper einen subtraktiven Keil hinzu.

#### Transformationswerkzeuge

Dies sind Werkzeuge zur Transformation bestehender Formelemente. Sie ermöglichen es, die zu transformierenden Formelemente auszuwählen.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Spiegeln](PartDesign_Mirrored/de.md): Spiegelt ein oder mehrere Formelemente auf einer Ebene oder Fläche.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Lineares Muster](PartDesign_LinearPattern/de.md) erstellt ein lineares Muster auf Grundlage eines oder mehrerer Formelemente.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Polares Muster](PartDesign_PolarPattern/de.md): Erstellt ein polares Muster aus einem oder mehreren Formelemente.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Mehrfachtransformation](PartDesign_MultiTransform/de.md): Erzeugt ein Muster mit einer beliebigen Kombination der anderen Transformationen.

#### Verschönerungswerkzeuge

Diese Werkzeuge ermöglichen es, Kanten und Flächen nachzubearbeiten.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Verrundung](PartDesign_Fillet/de.md): Verrundungen (Rundungen) der Kanten des aktiven Körpers.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Fase](PartDesign_Chamfer/de.md): fast die Kanten des aktiven Körpers an.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Entwurf](PartDesign_Draft/de.md): wendet einen winkligen Entwurf auf ausgewählte Flächen des aktiven Körpers an.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Dicke](PartDesign_Thickness/de.md): erzeugt eine dicke Außenhaut aus dem aktiven Körper und öffnet ausgewählte Fläche(n).

#### Boolesche Operationen 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Boolesche Operation](PartDesign_Boolean/de.md): importiert einen oder mehrere Körper oder PartDesign Klone in den aktiven Körper und führt eine Boolesche Operation aus.

#### Extras

Einige zusätzliche Funktionen befinden sich im Menü Part Design:

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;">[Migrieren](PartDesign_Migrate/de.md): Migriert Dateien, die mit älteren FreeCAD Versionen erstellt wurden. Wenn die Datei rein PartDesign formelementbasiert ist, sollte die Migration erfolgreich sein. Wenn die Datei gemischte Part/Part Design/Entwurfsobjekte enthält, wird die Konvertierung höchstwahrscheinlich fehlschlagen.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Assistent für Kettenraddesign](PartDesign_Sprocket/de.md): Erstellt ein Kettenradprofil, das aufgepolstert werden kann. {{Version/de|0.19}}

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Assistent zur Auslegung von Evolventengetrieben](PartDesign_InvoluteGear/de.md): erzeugt ein Evolventenverzahnungsprofil, das von einem Polster verwendet werden kann.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Wellenauslegungsassistent](PartDesign_WizardShaft/de.md): Erzeugt eine Welle aus einer Wertetabelle und ermöglicht die Analyse von Kräften und Momenten. Die Welle wird mit einer umlaufenden Skizze erstellt, die bearbeitet werden kann.

### Kontextmenü Elemente 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Spitze setzen](PartDesign_MoveTip/de.md): definiert die Spitze neu, das ist das Merkmal, das außerhalb des Körpers erscheint.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Objekt in anderen Körper verschieben](PartDesign_MoveFeature/de.md): verschiebt die ausgewählte Skizze, Bezugsgeometrie oder das Formelement in einen anderen Körper.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Objekt nach anderem Objekt verschieben](PartDesign_MoveFeatureInTree/de.md): ermöglicht eine Neuordnung des Körperbaums, indem die ausgewählte Skizze, Bezugsgeometrie oder das Formelement an eine andere Position in der Formelementliste verschoben wird.

#### Mit dem Part Arbeitsbereich gemeinsam genutzte Elemente 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Aussehen](Std_SetAppearance/de.md): bestimmt das Aussehen des gesamten Teils (Farbtransparenz usw.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;">[Farben festlegen](Part_FaceColors/de.md): Weist den Teilflächen Farben zu.

## Einstellungen

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Einstellungen](PartDesign_Preferences/de.md): Einstellungen verfügbar für PartDesign Werkzeuge.
-   [Feinabstimmung](Fine-tuning/de.md): Einige zusätzliche Parameter zur Feinabstimmung des PartDesign Verhaltens

## Tutorien

-   [Wie FreeCAD anwenden](http://help-freecad-jpg87.fr/), eine Netzseite, die den Arbeitsablauf für die mechanische Konstruktion beschreibt.
-   [Erstellen eines einfachen Teils mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md)
-   [Grundlegende Teilekonstruktion Übung](Basic_Part_Design_Tutorial/de.md)
-   [PartDesign Lagerträger Tutorial I](PartDesign_Bearingholder_Tutorial_I/de.md) (muss aktualisiert werden)
-   [PartDesign Lagerträger Tutorial II](PartDesign_Bearingholder_Tutorial_II/de.md) (muss aktualisiert werden)





 {{PartDesign Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [PartDesign](Category_PartDesign.md) > PartDesign Workbench/de
