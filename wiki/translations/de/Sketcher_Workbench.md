# <img alt="Sketcher Arbeitsbereichssymbol" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/de


{{TOCright}}

## Einführung

Der FreeCAD <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Arbeitsbereich Sketcher](Sketcher_Workbench/de.md) wird verwendet, um 2D Geometrien für den Gebrauch im <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Arbeitsbereich PartDesign](PartDesign_Workbench/de.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arbeitsbereich Architektur](Arch_Workbench/de.md) und anderen Arbeitsbereichen zu erstellen. Im Allgemeinen wird eine 2D Zeichnung als Ausgangspunkt für die meisten CAD Modelle betrachtet, da eine 2D Skizze \"extrudiert\" werden kann, um eine 3D Form zu erstellen; weitere 2D Skizzen können verwendet werden, um andere Merkmale wie Taschen, Stege oder Extrusionen auf den zuvor erstellten 3D Formen zu erstellen. usammen mit boolschen Operationen, definiert im <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Arbeitsbereich Part](Part_Workbench/de.md), bildet der Skizzierer die Grundlage der [der konstruktive Festkörpergeometrie](constructive_solid_geometry/de.md) (CSG) Methode für das Bauen von Volumenkörpern. Darüber hinaus bildet der Skizzierer zusammen mit den Abläufen des <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Arbeitsbereichs PartDesign](PartDesign_Workbench/de.md) auch die Grundlage der [Funktionsbearbeitungsmethodik](feature_editing/de.md) zum erstellen von Geometrieelementen um Volumenkörper zu erzeugen.

Der Arbeitsbereich Sketcher bietet *Beschränkungen* (engl.: constraints), die es erlauben 2D Formen gemäß präzisen geometrischen Vorgaben in Bezug auf Länge, Winkel und Verknüpfungen (Horizontalität, Vertikalität, Rechtwinkligkeit, usw.) zu folgen. Ein Beschränkungslöser berechnet die beschränkte Ausdehnung der 2D Geometrie und ermöglicht die interaktive Untersuchung von Freiheitsgraden der Skizze.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Eine vollständig beschränkte Skizze‎*

## Basics of constraint sketching 


<div class="mw-translate-fuzzy">

## Grundlagen des Skizzierens mit Beschränkungen 

Um zu erklären, wie der Skizzierer arbeitet, ist es sinnvoll, das Vorgehen mit der traditionellen Art des Entwerfens zu vergleichen.


</div>

#### Traditional Drafting 


<div class="mw-translate-fuzzy">

#### Traditionelles Entwerfen 

Die traditionelle Art des CAD Entwurfs entstammt dem alten Zeichnen auf dem Reißbrett [1](https://de.wikipedia.org/wiki/Rei%C3%9Fbrett). [2](https://de.wikipedia.org/wiki/Orthogonalprojektion). Orthogonale Ansichten (2D) werden von Hand gezeichnet, vorgesehen um technische Zeichnungen (auch als Blaupausen bekannt) zu erstellen. Objekte werden genau in der gewünschten Größe und der gewünschten Abmessung gezeichnet. Wenn du eine horizontale Linie von 100 mm Länge zeichnen möchtest, die bei (0,0) beginnt, aktiviere das Linienwerkzeug, klicke entweder auf den Bildschirm oder gib die (0,0) Koordinaten für den ersten Punkt ein, mache dann einen zweiten Klick oder gib die Koordinaten des zweiten Punktes bei (100,0) ein. Oder du zeichnest deine Linie ohne Rücksicht auf ihre Position und verschiebst sie danach. Wenn du deine Geometrien fertig gezeichnet hast, füge ihre Bemaßungen hinzu.


</div>

#### Constraint Sketching 


<div class="mw-translate-fuzzy">

#### Skizzieren mit Beschränkungen 

Der **Skizierer** entfernt sich von dieser Logik. Objekte müssen nicht genau so gezeichnet werden, wie Du es beabsichtigst, weil diese später durch Beschränkungen festgelegt werden. Objekte können grob gezeichnet werden, und solange sie nicht beschränkt wurden, können diese verändert werden. Tatsächlich sind sie dabei *schwebend* und können verschoben, gestreckt, gedreht, skaliert, usw. werden. Das gibt dem Entwurfsprozess große Flexibilität.


</div>

#### What are constraints? 


<div class="mw-translate-fuzzy">

#### Was sind Beschränkungen? 

An Stelle von Abmessungen werden Beschränkungen verwendet, um die Freiheitsgrade eines Objektes zu begrenzen. Beispielsweise besitzt eine Linie ohne Beschränkung 4 [Freiheitsgrade](#Degrees_Of_Freedom/de.md) (abgekürzt als \" DOF \")(engl. degrees of freedom): Sie kann horizontal oder vertikal verschoben, sie kann gestreckt, oder gedreht werden.


</div>

Anwenden einer horizontalen oder vertikalen Beschränkung oder einer Winkelbeschränkung (relativ zu einer anderen Linie oder zu einer der Achsen), schränkt seine Fähigkeit zu rotieren ein, so daß 3 Freiheitsgrade übrig bleiben. Das Festsetzen einer der Punkte mit Bezug zum Ursprung entfernt weitere 2 Freiheitsgrade. Und das Anwenden einer Maßbeschränkung entfernt den letzten Freiheitsgrad. Die Skizze ist dann **vollständig eingeschränkt**.

Mehrere Objekte können untereinander beschränkt werden. Zwei Linien können durch einen ihrer Punkte mit der Deckungsgleicher Punktbeschränkung verbunden werden. Ein Winkel kann zwischen ihnen festgelegt werden oder sie können senkrecht zueinander platziert werden. Eine Linie kann tangential zu einem Bogen oder einem Kreis sein, usw.. Eine komplexe Skizze mit mehreren Objekten weist eine Reihe verschiedener Lösungen auf, und wenn man sie **vollständig-beschränkt** erstellt, bedeutet dies, dass nur eine dieser möglichen Lösungen auf der Grundlage der angewandten Beschränkungen erreicht wurde.


<div class="mw-translate-fuzzy">

Es gibt zwei Arten von Beschränkungen: geometrische und maßliche. Sie sind im Abschnitt [\'Die Werkzeuge\'](#Die_Werkzeuge.md) weiter unten ausführlich beschrieben.


</div>

#### What the Sketcher is not good for 


<div class="mw-translate-fuzzy">

#### Wofür der Skizzierer nicht geeignet ist 

Der Skizzierer ist nicht für die Herstellung von 2D Blaupausen vorgesehen. Sobald Skizzen verwendet werden, um eine Volumenkörpermerkmal zu erzeugen, werden sie automatisch verborgen. Beschränkungen sind nur im Bearbeitungsmodus Skizze sichtbar.


</div>

Falls du nur 2D Ansichten zum Ausdrucken erzeugen möchtest und keine 3D Modelle, dann schau dir den [Arbeitsbereich Entwurf](Draft_Workbench/de.md) an. Anders als Skizzierer Elemente, verwenden Entwurfsobjekte keine Beschränkungen; sie sind einfache Formen die im Augenblick der Erstellung definiert werden. Sowohl Draft und Skizzierer können zum zeichnen von 2D Geometrien und zum Erzeugen von 3D Volumenkörpern verwendet werden, obwohl ihre bevorzugte Verwendung unterschiedlich ist; der Skizzierer wird normalerweise mit dem [Part Arbeitsbereich](Part_Workbench/de.md) und [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) verwendet um Volumenkörper zu erzeugen; Entwurf wird normalerweise verwendet für einfache ebene Zeichnungen über einem Raster, so wie beim Zeichnen eines Architektur Grundrisses; in solchen Situationen werden Entwurfsobjekte hauptsächlich zusammen mit dem [Arch Arbeitsbereich](Arch_Workbench/de.md) verwendet. Das Werkzeug [EntwurfZuSkizze](Draft_Draft2Sketch/de.md) wandelt ein Entwurfsobjekt in ein Skizzenobjekt, und umgekehrt; Viele Werkzeuge, die ein 2D Element als Eingabe benötigen, arbeiten mit beiden Objekttypen, da eine interne Konversion automatisch erfolgt.

## Arbeitsablauf beim Skizzieren 

Eine Skizze ist stets zweidimensional (2D). Um einen Volumenkörper zu erzeugen, wird eine 2D Skizze eines einzelnen, eingeschlossenen Bereichs erstellt und dann entweder aufgepolstert oder gedreht, um die dritte Dimension hinzuzufügen und um einen 3D Volumenkörper aus einer 2D Skizze zu erzeugen.

Wenn eine Skizze Segmente besitzt, die einander überschneiden, wenn sie Stellen enthält an denen ein Punkt nicht direkt auf einem Segment liegt, oder Stellen an denen Lücken zwischen Endpunkten angrenzender Segmente existieren, wird Aufpolstern oder Rotieren keine Festkörper erstellen.

Manchmal funktioniert eine Skizze, die sich überschneidende Linien enthält, für eine einfache Operation wie Aufpolstern, jedoch spätere Arbeitsgänge wie etwa lineare Muster werden fehlschlagen. Vermeide am besten die Überschneidung von Linien. Die Konstruktionsgeometrie (blau) bildet eine Ausnahme von dieser Regel. Hier dürfen sich Linien überschneiden ohne Probleme zu verursachen.

Die zum eigentlichen Zeichnen (Erstellen der zweidimensionalen geometrischen Grundelemente) benutzten Werkzeuge sind unter **Skizziergeometrien** zusmmengefasst.

Sobald eine Skizze vollständig beschränkt ist, wechselt die Skizzenmerkmale zu einem leuchtend hellen grün; Konstruktionsgeometrie hingegen bleibt blau. Normalerweise ist die Skizze an dieser Stelle \"fertig bearbeitet\" und für die Erstellung eines 3D Volumenkörpers geeignet. Sobald das Dialogfeld Skizze geschlossen ist, lohnt es sich jedoch möglicherweise, zum <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md) zu gehen und **[<img src=images/Part_CheckGeometry.svg style="width:24px"> [Geometrie prüfen](Part_CheckGeometry/de.md)** auszuführen, um sicherzustellen, dass die Skizze keine Merkmale enthält, die zu späteren Problemen führen können.

## Tools


<div class="mw-translate-fuzzy">

## Die Werkzeuge 

Die Werkzeuge des Sketch-Arbeitsbereich sind alle im Sketch-Menü zu finden, das beim Laden des Arbeitsbereichs erscheint.


</div>

### Allgemein


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.png‎‎  style="width:32px;"> [Neue Skizze](Sketcher_NewSketch/de.md): Erstellt eine neue Skizze auf einer ausgewählten Fläche oder Ebene. Falls bei der Ausführung dieses Werkzeugs keine Fläche gewählt wurde, wird der Benutzer über ein Dialogfenster zur Auswahl einer Ebene aufgefordert.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Skizze bearbeiten](Sketcher_EditSketch/de.md): Editieren der gewählten Skizze. Dies öffnet den [Skizzierer Dialog](Sketcher_Dialog/de.md).


</div>

-   <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> [Skizze verlassen](Sketcher_LeaveSketch/de.md): Beenden des Skizzierer Bearbeitungsmodus.

-   <img alt="" src=images/Sketcher_ViewSketch.png‎  style="width:32px;"> [Skizze anzeigen](Sketcher_ViewSketch/de.md): Legt die Modellansicht senkrecht zur Skizzierebene fest.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Schnitt anzeigen](Sketcher_ViewSection/de.md): Erzeugt eine Schnittebene, und verbirgt vorübergehend jeden Gegenstand vor der Skizzierebene.

-   <img alt="" src=images/Sketcher_MapSketch.svg‎  style="width:32px;"> [Skizze einer Fläche zuordnen](Sketcher_MapSketch/de.md): Ordnet eine Skizze der vorher gewählten Fläche eines Volumenkörpers zu.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Skizze neu ausrichten](Sketcher_ReorientSketch/de.md): Erlaubt die Positionsänderung einer Skizze

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Skizze überprüfen](Sketcher_ValidateSketch/de.md): Überprüft die Toleranz verschiedener Punkte und passt sie an.

-   <img alt="" src=images/Sketcher_MergeSketch.svg‎  style="width:32px;"> [Skizzen zusammenführen](Sketcher_MergeSketches/de.md): Führt zwei oder mehr Skizzen zusammen.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg‎  style="width:32px;"> [Skizze spiegeln](Sketcher_MirrorSketch/de.md): Spiegelt eine Skizze entlang der X-Achse, der Y-Achse oder dem Ursprung.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Vorgang anhalten](Sketcher_StopOperation/de.md): im Bearbeitungsmodus, hält den aktuellen Vorgang an, ob es sich um das Zeichnen, das Festlegen von Beschränkungen usw. handelt.


</div>

### Skizziergeometrien

Dies sind Werkzeuge zum Erstellen von Objekten.

-   <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> [Punkt](Sketcher_CreatePoint/de.md): Zeichnet einen Punkt.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Linie](Sketcher_CreateLine/de.md): Zeichnet ein Linienabschnitt zwischen 2 Punkten. Linien sind in Bezug auf bestimmte Beschränkungen unendlich.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;">[Einen Bogen erstellen](Sketcher_CompCreateArc/de.md): Dies ist ein Symbolmenü in der Skizzierer Werkzeugleiste, das die folgenden Befehle enthält:

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Bogen](Sketcher_CreateArc/de.md): Zeichnet ein Bogensegment aus Mittelpunkt, Radius, Startwinkel und Endwinkel.

:\* <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Bogen durch 3 Punkte](Sketcher_Create3PointArc/de.md): Zeichnet einen Kreisbogen aus zwei Endpunkten und einem weiteren Punktes auf dem Umfang.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;">[Einen Kreis erstellen](Sketcher_CompCreateCircle/de.md): Dies ist ein Symbolmenü in der Skizzierer Werkzeugleiste, das die folgenden Befehle enthält:

:\* <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [Kreis](Sketcher_CreateCircle/de.md): Zeichnet einen Kreis aus Mittelpunkt und Radius.

:\* <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Kreis durch 3 Punkte](Sketcher_Create3PointCircle/de.md): Zeichnet einen Kreis aus drei Punkten auf dem Umfang.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:48px;"> [Erstellen eines Kegels](Sketcher_CompCreateConic/de.md): Der Skizzierer stellt folgenden konische Abschnitte bereit. Im Gegensatz zu B-Splines können sie mit allen Arten von Beschränkungen wie z. B. [Tangenten](Sketcher_ConstrainTangent/de.md), [Punkt auf Objekt](Sketcher_ConstrainPointOnObject/de.md), oder [Orthogonal](Sketcher_ConstrainPerpendicular/de.md) verwendet werden.
    -   <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse durch Zentrum](Sketcher_CreateEllipseByCenter/de.md): Zeichnet eine Ellipse aus Mittelpunkt, Hauptradiuspunkt und Nebenradiuspunkt.
    -   <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse durch 3 Punkte](Sketcher_CreateEllipseBy3Points/de.md): Zeichnet eine Ellipse aus Hauptradius (2 Punkte) und kleinem Radiuspunkt
    -   <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Ellipsenbogen](Sketcher_CreateArcOfEllipse/de.md) : Zeichnet eine Ellipsenbogen aus Mittelpunkt, Hauptradiuspunkt, Startpunkt und Endpunkt.
    -   <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Hyperbelbogen](Sketcher_CreateArcOfHyperbola/de.md): Zeichnet einen Hyperbelbogen.
    -   <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Parabelbogen](Sketcher_CreateArcOfParabola/de.md): Zeichnet einen Parabelbogen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [B-spline erstellen](Sketcher_CompCreateBSpline/de.md): Dies ist ein Symbolmenü in der Skizzierer Werkzeugleiste, das die folgenden Befehle enthält:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline erstellen](Sketcher_CreateBSpline/de.md): Zeichnen einer B-spline Kurve (verkettete Linie) durch die Kontrollpunkte.
    -   <img alt="" src=images/Sketcher_Create_Periodic_BSpline.svg  style="width:32px;"> [Create periodic B-pline](Sketcher_CreatePeriodicBSpline/de.md): Zeichnet eine periodische (geschlossene) B-Spline Kurve anhand ihrer Kontrollpunkte.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polylinie (Mehrfach-Punkt Linie)](Sketcher_CreatePolyline/de.md):

Zeichnet eine Linie aus mehreren Liniensegmenten. Drücken der M Taste während des Zeichnens einer Polylinie schaltet zwischen den verschiedenen Polylinienmodi.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Rechtecke erstellen](Sketcher_CompCreateRectangles/de.md): Dies ist ein Symbolmenü in der Skizzierer Symbolleiste, das die folgenden Befehle enthält: {{Version/de|0.20}}


</div>

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rechteck](Sketcher_CreateRectangle/de.md): Zeichnet ein Rechteck aus zwei gegenüber liegenden Punkten.


<div class="mw-translate-fuzzy">

:\* <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Zentriertes Rechteck](Sketcher_CreateRectangle_Center/de.md): Zeichnet ein Rechteck aus einem zentralen Punkt und einem Randpunkt. {{Version/de|0.20}}


</div>


<div class="mw-translate-fuzzy">

:\* <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Abgerundetes Rechteck](Sketcher_CreateOblong/de.md): Zeichnet ein abgerundetes Rechteck aus 2 gegenüberliegenden Punkten. {{Version/de|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> [Erstellen regelmäßiges Polygon](Sketcher_CompCreateRegularPolygon/de.md): Dies ist ein Symbolmenü in der Skizzierer Werkzeugleiste, das die folgenden Befehle enthält:


</div>

-   <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Dreieck](Sketcher_CreateTriangle/de.md): Zeichnet ein regelmäßiges Dreieck, das einem Konstruktionsgeometriekreis einbeschrieben ist.

-   <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Quadrat](Sketcher_CreateSquare/de.md): Zeichnet ein regelmäßiges Quadrat, das einem Konstruktionsgeometriekreis einbeschrieben ist.

-   <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Fünfeck](Sketcher_CreatePentagon/de.md): Zeichnen eines regelmäßigen Fünfecks das einem Umkreis einbeschrieben ist.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Sechseck](Sketcher_CreateHexagon/de.md): Zeichnen eines regelmäßigen Sechsecks das einem Umkreis einbeschrieben ist.

-   <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Siebeneck](Sketcher_CreateHeptagon/de.md): Zeichnen eines regelmäßigen Siebenecks das einem Umkreis einbeschrieben ist.

-   <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Achteck](Sketcher_CreateOctagon/de.md): Zeichnen eines regelmäßigen Achtecks das einem Umkreis einbeschrieben ist.


<div class="mw-translate-fuzzy">

:\* <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Regelmäßiges Polygon erzeugen](Sketcher_CreateRegularPolygon/de.md) : Zeichnen eines regelmäßigen Polygons durch Auswahl der Anzahl der Seiten und Auswahl zweier Punkte: dem Zentrum und einer Ecke.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Langloch](Sketcher_CreateSlot/de.md): Zeichnet ein Oval, indem das Zentrum des einen Halbkreises und ein Endpunkt des anderen Halbkreises ausgewählt werden.

-   <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> [Verrundung](Sketcher_CreateFillet/de.md): Erstellt eine Verrundung zwischen zwei Linien, die an einem Punkt verbunden sind. Wähle beide Linien oder klicke auf den Eckpunkt und aktiviere dann das Werkzeug.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Stutzen](Sketcher_Trimming/de.md): Stutzt eine Gerade, einen Kreis oder Kreisbogen mit Bezug zum angeklickten Punkt.


</div>

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Dehnen](Sketcher_Extend/de.md): Dehnt eine Linie oder einen Kreisbogen zu einer Grenzlinie, einem Bogen, einer Ellipse, einem Ellipsenbogen oder einem Raumpunkt.

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Teilen](Sketcher_Split/de.md): Teilt eine Linie oder einen Bogen in zwei, wandelt einen Kreis in einen Bogen um und behält dabei die meisten Beschränkungen bei. {{Version/de|0.20}}


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Externe Geometrie](Sketcher_External/de.md): Erstellt eine Kante verbunden mit einer externer Geometrie.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Kopie](Sketcher_CarbonCopy/de.md): Kopiert die Geometrie einer anderen Skizze.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Konstruktionsmodus](Sketcher_ToggleConstruction/de.md): Schaltet die Skizzengeometrie vom/ zum Konstruktionsmodus um. Konstruktionsgeometrie wird in Blau angezeigt und außerhalb des Skizziermodus verworfen.


</div>

### Skizzierbeschränkungen

Beschränkungen werden benutzt, um Längen zu definieren, Regeln zwischen Skizzenelementen aufzustellen und die Skizze entlang der vertikalen und horizontalen Achsen festzulegen. Einige Beschränkungen benötigen die Verwendung von [Hilfsbeschränkungen](Sketcher_helper_constraint/de.md).

#### Geometric constraints 


<div class="mw-translate-fuzzy">

#### Gometrische Beschränkungen 

Diese Beschränkungen sind nicht mit nummerischen Daten verknüpft.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Deckungsgleich](Sketcher_ConstrainCoincident/de.md):

Befestigt einen Punkt auf (deckungsgleich mit) einem oder mehreren anderen Punkten.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Punkt auf Objekt](Sketcher_ConstrainPointOnObject/de.md):

Fügt einen Punkt einem anderen Objekt hinzu, z. B. einer Linie, einem Kreisbogen oder einer Achse.


</div>

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertikal](Sketcher_ConstrainVertical/de.md): Beschränkt die ausgewählten Linien oder Polylinienelemente auf eine echte vertikale Ausrichtung. Vor dem Anwenden dieser Beschränkung kann mehr als ein Objekt ausgewählt werden.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/de.md): Beschränkt die ausgewählten Linien oder Polylinienelemente auf eine echte horizontale Ausrichtung. Vor der Anwendung dieser Beschränkung kann mehr als ein Objekt ausgewählt werden.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel/de.md): Beschränkt zwei oder mehr Linien parallel zueinander.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Senkrecht](Sketcher_ConstrainPerpendicular/de.md): Beschränkt zwei Linien senkrecht zueinander oder eine Linie senkrecht zu einem Kreisbogenendpunkt.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/de.md): Erzeugt eine Tangenten Beschränkung zwischen zwei ausgewählten Objekten oder eine kollineare Beschränkung zwischen zwei Liniensegmenten. Ein Liniensegment muss nicht direkt an einem Kreis oder Kreisbogen liegen, um tangential beschränkt zu diesem Kreis oder Kreisbogen zu werden.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Gleiche Länge](Sketcher_ConstrainEqual/de.md): Beschränkt zwei ausgewählte Objekte zueinander gleichgesetzt. Bei Verwendung mit Kreisen oder Bögen werden deren Radien gleich gesetzt.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Symmetrisch](Sketcher_ConstrainSymmetric/de.md): Beschränkt zwei Punkte symmetrisch um eine Linie oder beschränkt die ersten zwei gewählten Punkte symmetrisch um einen dritten gewählten Punkt.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Beschränkung blockieren](Sketcher_ConstrainBlock/de.md): Ermöglicht grundsätzlich das Blockieren eines geometrischen Elements mit einer einzigen Beschränkung. Es sollte besonders praktisch bei der Arbeit mit B-Splines sein. Siehe das [Block Beschränkung Forumsthema](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Dimensional constraints 


<div class="mw-translate-fuzzy">

#### Dimensionale Beschränkungen 

Dies sind Beschränkungen, die mit numerischen Daten verknüpft sind, für die du die [Ausdrücke ](Expressions/de.md) verwenden kannst. Die Daten können aus einer [Kalkulationstabelle](Spreadsheet_Workbench/de.md) entnommen werden.


</div>

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Sperren](Sketcher_ConstrainLock/de.md):

Beschränkt das ausgewählte Element, in dem vertikale und horizontale Abstände relativ zum Ursprung festgelegt werden, wodurch die Position dieses Elements gesperrt wird. Diese Beschränkungsabstände können später bearbeitet werden.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md): Legt den horizontalen Abstand zwischen zwei Punkten oder Linienendpunkten fest. Wenn nur ein Element ausgewählt ist, wird der Abstand zum Ursprung festgelegt.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md): Legt den vertikalen Abstand zwischen 2 Punkten oder Linienendpunkten fest. Wenn nur ein Element ausgewählt ist, wird der Abstand zum Ursprung festgelegt.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Abstand](Sketcher_ConstrainDistance/de.md): Legt den Abstand einer ausgewählten Linie durch Beschränken ihrer Länge oder legt den Abstand zwischen zwei Punkten durch Beschränken des Abstands zwischen ihnen fest.

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Radius](Sketcher_ConstrainRadius/de.md): Definiert den Radius eines ausgewählten Kreisbogens oder Kreises durch Beschränkung des Radius.
-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Durchmesser](Sketcher_ConstrainDiameter/de.md): Definiert den Durchmesser eines ausgewählten Bogens oder Kreises durch Beschränkung des Durchmessers.
-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Radiam](Sketcher_ConstrainRadiam/de.md): Definiert automatisch Radius/Durchmesser eines ausgewählten Bogens oder Kreises (Gewicht für einen B-Spline-Pol, Durchmesser für einen vollständigen Kreis, Radius für einen Bogen) {{Version/de|0.20}}
-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Winkel](Sketcher_ConstrainAngle/de.md): Definiert den Innenwinkel zwischen zwei ausgewählten Linien.


<div class="mw-translate-fuzzy">

#### Besondere Beschränkungen 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Snelliussches Gesetz](Sketcher_ConstrainSnellsLaw/de.md): Beschränkt zwei Linien so, dass sie einem Brechungsgesetz unterliegen, um das durch eine Grenzfläche gehende Licht zu simulieren.


</div>

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:32px;"> [Interne Ausrichtung](Sketcher_ConstrainInternalAlignment/de.md): Richtet ausgewählte Elemente an der ausgewählten Form aus (z. B. eine Linie, die zur Hauptachse einer Ellipse wird).

#### Constraint tools 


<div class="mw-translate-fuzzy">

#### Beschränkungswerkzeuge

Die folgenden Werkzeuge können verwendet werden, um die Wirkung von Beschränkungen zu ändern:


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Umschalten Referenz/treibende Beschränkung](Sketcher_ToggleDrivingConstraint/de.md): Schaltet die Werkzeugleiste oder die ausgewählten Beschränkungen in/aus dem Referenzmodus um.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Umschalten aktive Beschränkung](Sketcher_ToggleActiveConstraint/de.md): Einschalten oder ausschalten einer bereits platzierten Beschränkung. {{Version/de|0.19}}


</div>

### Skizzierer Werkzeuge 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Löser Freiheitsgrade auswählen](Sketcher_SelectElementsWithDoFs/de.md): Hebt in grün die Geometrie mit Freiheitsgraden (DOFs), d.h. nicht vollständig beschränkt, hervor.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Form schließen](Sketcher_CloseShape/de.md): Erstellt eine geschlossene Form, durch Anwendung deckungsgleicher Beschränkungen auf Endpunkte.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Elemente verbinden](Sketcher_ConnectLines/de.md): Verbindet Skizzenelemente, durch Anwendung von Koinzidenzbeschränkungen auf Endpunkte.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Beschränkung wählen](Sketcher_SelectConstraints/de.md): Wahl der Beschränkungen eines Skizziererelements.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Elemente verknüpfter Beschränkungen wählen](Sketcher_SelectElementsAssociatedWithConstraints/de.md): Wählt mit Skizzenelemente aus, die mit Beschränkungen verknüpft sind.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Redundante (überflüssige) Beschränkungen wählen](Sketcher_SelectRedundantConstraints/de.md): Wählt redundante Beschränkungen einer Skizze aus.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Widersprüchliche Beschränkungen wählen](Sketcher_SelectConflictingConstraints/de.md): Wählt widersprüchliche Beschränkungen einer Skizze aus.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Show/Hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry/de.md): Stellt fehlende oder löscht nicht benötigte interne Geometrie einer ausgewählten Ellipse, eines Ellipsen-/ Hyperbel-/ Parabel- oder B-Spline-Bogens.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Ursprung wählen](Sketcher_SelectOrigin/de.md): Wählt den Ursprung einer Skizze aus


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Vertikale Achse wählen](Sketcher_SelectVerticalAxis/de.md): Wählt die vertikale Achse einer Skizze aus.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Horizontale Achse wählen](Sketcher_SelectHorizontalAxis/de.md): Wählt die horizontale Achse einer Skizze aus


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetrie](Sketcher_Symmetry/de.md): Kopiert ein Skizzierelement symmetrisch zu einer ausgewählten Linie.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Klon](Sketcher_Clone/de.md): Klont ein Skizziererelement


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Kopieren](Sketcher_Copy/de.md): Kopiert ein Skizzenelement


</div>

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Verschieben](Sketcher_Move/de.md): Verschiebt die ausgewählte Geometrie unter Bezug auf den zuletzt ausgewählten Punkt.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Rechteckige Matrix](Sketcher_RectangularArray/de.md): Erstellt eine Anordnung ausgewählter Skizziererelemente


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Achsenausrichtung entfernen](Sketcher_RemoveAxesAlignment/de.md): Entfernen der Achsenausrichtung unter Beibehaltung der Beschränkungsbeziehung der Auswahl {{Version/de|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Jede Geometrie löschen](Sketcher_DeleteAllGeometry/de.md): Löscht alle Geometrien aus der Skizze.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Alle Beschränkungen löschen](Sketcher_DeleteAllConstraints/de.md): Löscht alle Beschränkungen aus der Skizze.


</div>

### Skizze B-spline Werkzeuge 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [B-Spline Grad anzeigen/ausblenden](Sketcher_BSplineDegree/de.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [B-Spline Kontrollpolygon anzeigen/ausblenden](Sketcher_BSplinePolygon/de.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [B-Spline Krümmungskamm anzeigen/ausblenden](Sketcher_BSplineComb/de.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [B-Spline Knotenvielfalt anzeigen/ausblenden](Sketcher_BSplineKnotMultiplicity/de.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [B-Spline Kontrollpunkt Zeichenbreite anzeigen/verbergen](Sketcher_BSplinePoleWeight.md), {{Version/de|0.19}}

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Geometrie in B-Spline umwandeln](Sketcher_BSplineApproximate/de.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Erhöhen B-Spline Grad](Sketcher_BSplineIncreaseDegree/de.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [B-Spline Grad verringern](Sketcher_BSplineDecreaseDegree.md), {{Version/de|0.19}}

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Knotenvielfalt erhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Knotenvielfalt verringern](Sketcher_BSplineDecreaseKnotMultiplicity/de.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md), <small>(v0.20)</small> 

### Skizzierer virtueller Raum 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Virtuellen Raum wechseln](Sketcher_SwitchVirtualSpace/de.md): Ermöglicht dir alle Beschränkungen einer Skizze auszublenden und wieder sichtbar zu machen.


</div>


<div class="mw-translate-fuzzy">

### Einstellungen


</div>

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Einstellungen](Sketcher_Preferences/de.md): Einstellungen für den **Skizzierer** Arbeitsbereich.

## Best Practices 


<div class="mw-translate-fuzzy">

## Bewährte Vorgehensweisen 

Jeder CAD Benutzer entwickelt im Laufe der Zeit seine eigene Arbeitsweise, aber es gibt einige nützliche allgemeine Grundsätze, die zu befolgen sind.


</div>

-   Eine Reihe einfacher Skizzen ist einfacher handzuhaben als eine komplexe einzelne Skizze. Beispielsweise kann eine erste Skizze für die grundlegenden 3D Funktionen (entweder ein aufpolstern oder ein drehen) erstellt werden, während eine zweite Skizze Löcher oder Ausschnitte (Taschen) enthalten kann. Einige Details können weggelassen werden, um später als 3D Funktionen realisiert zu werden. Sie können wählen, dass Verrundungen in Ihrer Skizze vermieden werden, wenn zu viele vorhanden sind, und diese als 3D Funktionen hinzugefügt werden.
-   Erstelle immer ein geschlossenes Profil, da Deine Skizze keinen Volumenkörper, sondern eine Reihe offener Seitenflächen erzeugt. Wenn Du nicht möchtest, dass einige der Objekte in die Volumenkörpererstellung einbezogen werden, können sie mit dem Konstruktionsmodus Werkzeug in Konstruktionselemente umgewandelt werden.
-   Verwende die automatische Beschränkungsfunktion, um die Anzahl der Beschränkungen zu begrenzen, die Sie manuell hinzufügen müssen.
-   Wende in der Regel zuerst geometrische und dann maßliche Beschränkungen an und sperre sie am Ende Deiner Skizze. Aber denke daran: Regeln sind dazu da, gebrochen zu werden. Wenn Probleme beim Bearbeiten Deiner Skizze auftreten, kann es hilfreich sein, zuerst einige Objekte einzuschränken, bevor Dein Profil vervollständigt wird.
-   Wenn möglich, zentriere Deine Skizze auf den Ursprung (0,0) mit der Sperr Beschränkung. Wenn Deine Skizze nicht symmetrisch ist, suche einen ihrer Punkte zum Ursprung oder wähle schöne runde Zahlen für die Verriegelungsabstände. Externe Beschränkungen (Beschränken der Skizze auf vorhandene 3D-Geometrie wie Kanten oder andere Skizzen) sind in v0.12 nicht implementiert. Dies bedeutet, dass die Abstände zur ersten Skizze manuell festgelegt werden müssen, um die Geometrie der folgenden Skizzen zur ersten Skizze festzulegen. Eine Sperrbeschränkung von (25,75) vom Ursprung kann man sich leichter merken als (23.47,73.02).
-   Wenn man die Möglichkeit hat, zwischen der Längenbeschränkung und der horizontalen oder vertikalen Abstandsbeschränkung zu wählen, bevorzuge die Letztere. Horizontale und vertikale Abstandsbeschränkungen sind rechentechnisch billiger.
-   Im Allgemeinen sind die besten Beschränkungen zur Verwendung: Horizontale und vertikale Beschränkungen; Horizontale und vertikale Längenbeschränkungen; Punkt-zu-Punkt Tangentialität. Wenn möglich, begrenze die Verwendung der folgenden: der allgemeinen Längenbeschränkung; Tangentialität von Kante zu Kante; Fixpunkt auf einer Linienbeschränkung; Symmetriebeschränkung.
-   Wenn Zweifel an der Gültigkeit einer Skizze bestehen, nachdem diese vollständig ist (Merkmale werden grün), schließe das Skizzierer Dialogfeld, wechsle zum <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [ Arbeitbereich Part](Part_Workbench/de.md) und führe das <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Geometrie prüfen](Part_CheckGeometry/de.md) aus.

## Tutorien

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) von chrisb. Dies ist ein 70 Seiten langes PDF Dokument, das als ausführliches Handbuch für den Skizzierers dient. Die Grundlagen zur Verwendung des Skizzierers werden erläutert und sie geht in zahlreiche Details zur Erstellung geometrischer Formen sowie zu den einzelnen Beschränkungen hinein.
-   [Basistutorium Skizzierer](Basic_Sketcher_Tutorial/de.md) für Anfänger
-   [Skizzierer Mikro Tutorial - Beschränkungspraxis](Sketcher_Micro_Tutorial_-_Constraint_Practices/de.md)
-   [Skizzierer Anforderungen an Skizzen](Sketcher_requirement_for_a_sketch/de.md) Mindestanforderung für eine Skizze und vollständige Festlegung einer Skizze

## Skripten

Die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite enthält Beispiele für die Erstellung von Beschränkungen aus Python Skripten.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/de
