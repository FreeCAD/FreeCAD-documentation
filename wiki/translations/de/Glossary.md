# Glossary/de
Diese Seite ist ein Glossar mit allgemeinen FreeCAD Begriffen und Definitionen.

Springe zu Buchstaben: {{CompactTOC|center=yes}}


<div class="mw-translate-fuzzy">

## A


{{gloss}}


{{term|Arc}}

\> Bogen {{defn|defn=Ein Teil oder Segment eines Kreises}} {{term|Arch|content=[Arch](Arch_Workbench/de.md)}} \> Architektur {{defn|defn=Eine Abkürzung für den architektonischen [Arbeitsbereich](#Workbench.md), der hauptsächlich für die Modellierung von Gebäuden und Strukturen verwendet wird. Eng verwandt mit dem [Arbeitsbereich Entwurf](#Draft.md).}} {{term|Assembly|content=[Zusammenbau](Assembly/de.md)}} {{defn|no=1|defn= eEin Satz von [Teilen](#Part/de.md), die definierte Positionen in Bezug zueinander haben.}} {{defn|no=2|defn= Ein [Arbeitsbereich](#Workbench/de.md), der die Erstellung von Baugruppen erleichtern soll. Sie befindet sich derzeit in der Entwicklung und ist noch nicht Teil von FreeCAD.}} {{term|Axes}} \> Achsen {{defn|defn=Eine imaginäre Linie duch den Ursprung des Arbeitsbereichs. Es gibt drei normale Achsen. Sie haben die drei klassischen Namen X, Y und Z. X ist horizontal, Y ist vertikal, Z ist in/aus Seite/Bildschirm.}} {{glossend}}


</div>

## B


{{gloss}}


{{term|term=Backtrace}}


{{defn|defn=Ausgabe eines Fehlersuchprogramms, das die Reihe von Anweisungen anzeigt, die FreeCAD befolgt hat, bevor ein Problem auftrat.}}


{{term|Bezier Curve|content=[https://de.wikipedia.org/wiki/B%C3%A9zierkurve Bézierkurve]}}


{{defn|defn=Ein Typ einer parametrischen Kurve}}


{{term|Blueprint}}

\> Blaupause {{defn|defn=alter Begriff aus der Zeit, als technische Zeichnungen von Hand auf Transparentpapier angefertigt wurden. Eine Blaupause war eine hell auf blauem Hintergrund erscheinende Kopie des Originals.}} {{term|Body}} \> Körper {{defn|defn=Ein Typ eines Containers aus dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md), der die Sequenz von Operationen: ([Skizzen](#Sketch/de.md), additive bzw. substraktive Geometrie sowie [Features](#Feature/de.md)) zusammenfasst, die einen einzelnen zusammenhängenden Körper erzeugen (eingeführt in FreeCAD v0.17).}} {{term|Boolean Logic}} \> [Boole\'sche Funktion](https://de.wikipedia.org/wiki/Boolesche_Funktion) {{defn|defn=Eine Methode zur Manipulation mit den Operanden: Und, Oder, Nicht (And, Or, Not)}} {{term|Boolean Operation}} \> Boole\'sche Verknüpfung {{defn|defn= Verwendung der Boole'schen Funktionen Vereinigung ([Fuse](#Fuse/de.md)), Differenz ([Cut](#Cut.md)), Schnitt (Intersection) und Section}} {{term|Boolean Operations check (BOPcheck)}} \> Boole\'sche Verknüpfung, Prüfung {{defn|defn=Eine Einstellung, die den "Geometrie überprüfen"-Werkzeugen in den Arbeitsbereichen Part und OpenSCAD erlaubt, auch Geometrien zu überprüfen, die mit
 [Boole'scher Logik](#Boolean_Logic/de.md) erstellt wurden. Die Standardeinstellung ist "false" (oder off), aber der Benutzer kann sie aktivieren, um bei "Geometrie überprüfen" höhere Genauigkeit zu erhalten, was allerdings zu längeren Laufzeiten dieser Überprüfung führt. Die Einstellung wird aktiviert durch Werkzeuge > Parameter bearbeiten > Preferences folder > Mod folder > Part folder > Check geometry folder, dann doppelklicken von "false" im rechten Fenster zur Änderung des Werts auf "true", klicken des {{button|OK}}-Buttons, klicken des {{button|Speichern}}-Buttons, dann klicken des {{button|Schließen}}-Buttons. Ein entsprechender Screenshot und eine Beschreibung, wie BOPCheck aktiviert werden kann, ist in diesem (englischsprachigen) [http://forum.freecadweb.org/viewtopic.php?t=8031#p65914 Forumsbeitrag] zu finden.}} {{term|brep}} \> File-Format \*.brep {{defn|defn=ursprüngliches Dateiformat von [Open ADCASCADE](#Open_CASCADE/de.md), das von FreeCAD zum Speichern im *.brep-Format benutzt werden kann}} {{term|Boundary representation (B-rep)}} \> Grenzflächen-Repräsentation {{defn|defn=Repräsentation eines Körpers durch seine ihn begrenzenden Flächen (siehe [https://de.wikipedia.org/wiki/Boundary_Representation Boundary Representation]),
 eine von zwei in FreeCAD verwendete Methoden (die andere ist die [mesh](#Mesh/de.md)-Repräsentation)}} {{term|BSpline}} \> BSpline {{defn|defn=Typ einer parametrischen Kurve; eine an eine tatsächliche Kurve angenäherte einfachere Kurve, siehe [https://de.wikipedia.org/wiki/Spline Spline].
 Bsplines haben eine bestimmte Basis (!B!-Splines)}} {{glossend}}

## C


{{gloss}}


{{term|Callout}}

\> erklärender Text mit hinzeigender Linie {{defn|defn= Textzeichenfolge, die mit einer Linie verbunden ist, die auf ein Objekt in einer [Zeichnung](#Drawing.md) zeigt.}}


{{term|Chamfer}}

\> Kantenschräge


{{term|1=Clipping Plane}}

\> Schnittebene {{defn|1=Die Beschneidungsebene wird verwendet, um in der 3D Ansicht am Modell wegzuschneiden. Sie ist nur eine visuelle Hilfe und schneidet das Modell nicht wirklich.}}


{{term|Clone}}

\> Klon {{defn|defn=Eine Kopie eines Objekts, wobei die Kopie parametrisch bleibt.  Wenn das Originalobjekt geändert wird, ändern sich auch der/die Klon(e), um die am Originalobjekt vorgenommenen Änderungen anzuzeigen.}}


{{term|Coin}}

\> COIN {{defn|defn=auch Coin3D genannt, eine von FreeCAD für 3D-Repräsentationen gebrauchte Drittpartei-Bibliothek }}


{{term|COLLADA}}

\> COLLADA {{defn|defn=Ein Austauschdateiformat für [Polygonnetz](#Mesh.md) Modelle. Dateiendung ist *.dae.}}


{{term|Command|content=[https://www.freecadweb.org/wiki/Command/de Command]}}


{{defn|defn=Eine Aktion ausgelöst von der [Benutzeroberfläche](#GUI/de.md), wenn ein Symbol in der Werkzeugleiste angeklickt wurde oder ein Tastenkürzel über die Tastatur oder ein Kommando in der Python-Konsole eingegeben wurde.}}


{{term|Compound}}

\> Verbund {{defn|defn=Gruppiert Objekte zusammen, ohne sie zu verschmelzen, wie es eine [Boolesche Vereinigung](#Boolean_Operation.md) tun würde.}}


{{term|CompSolid}}


{{defn|defn=Ein Set von [Körpern](#Solid.md) die über ihre [Flächen](#Face.md) verbunden sind. CompSolids werden im Arbeitsbereich [FEM](#FEM.md) benötigt, wenn mehr als ein Material innerhalb eines Netzes verwendet werden muss.}}


{{term|1=Constraint}}

\> Beschränkung {{defn|1=Eine Beschränkung der geometrischen Beziehung zwischen Grundelementen in einer [Skizze](#Sketch.md). Wenn eine Beschränkung einen numerischen Wert hat, wird sie als Bezugspunkt bezeichnet (z.B. hat eine Abstandsbeschränkung einen numerischen Wert - die Länge einer imaginären Linie, die die beiden Punkte verbindet). Eine Beschränkung, die keinen numerischen Wert hat (z.B. eine horizontale Beschränkung), wird manchmal auch als geometrische Beschränkung bezeichnet.}}


{{term|Constructive Solid Geometry|content=[https://de.wikipedia.org/wiki/Constructive_Solid_Geometry Constructive_Solid_Geometry] (CSG)}}

\> aus geometrischen Grundkörpern entstandener Körper {{defn|defn=aus geometrischen Grundkörpern ([primitives](#Primitive.md)) durch Anwendung Boole'scher Funktionen ([Boole'sche Operationen](#Boolean_Operation.md)) entstandener Körper}}


{{term|Coordinate}}

\> Koordinate {{defn|defn= [https://de.wikipedia.org/wiki/Kartesisches_Koordinatensystem kartesische] Koordinatenwerte zur Bestimmung der relativen Position eines Objekts}}


{{term|Coplanar}}


{{defn|defn=Koplanar; Auf der gleichen Ebene vorhanden}}


{{term|CSG}}


{{defn|defn=Abkürzung für [Konstruktive Festkörpergeometrie](#Constructive_Solid_Geometry.md).}}


{{term|Cut}}

\> Schnitt {{defn|defn=Anwenden einer [Booleschen Differenzbildung](#Boolean_Operation.md) zwischen Formen.}} {{glossend}}


<div class="mw-translate-fuzzy">

## D


{{gloss}}


{{term|term=DAG}}


{{defn|defn=See [Directed Acyclic Graph.](#Directed_Acyclic_Graph.md)}}


{{term|term=Degrees Of Freedom (DOF)}}

\> Freiheitsgrad {{defn|defn=eine Zahl > 0 als Summe der Unbestimmtheiten in den geometrischen Grundelementen einer Skizze (bzw. als Summe der verbleibenden Freiheiten für die Auslegung der geometrischen Grundelemente), siehe [Constraints](#Constraint.md)}}


{{term|term=Dependency Graph}}


{{defn|defn=Ein von FreeCAD unabhängiges Werkzeug, das benutzt wird, um die Abhängigkeiten der Konstruktionsobjekte im FreeCAD-Dokument untereinander grafisch darzustellen. Weitere Informationen finden sich in der [Dependency Graph Wiki page](Std_DependencyGraph/de.md)|.}}


{{term|term=Difference}}

-\> Differenz {{defn|no=1|defn=Das Ergebnis oder der Rest einer Subtraktion.}} {{defn|no=2|defn=Eine [Boolsche Operation](#Boolean_operation.md) im Arbeitsbereich Part, um eine Geometrie von einer anderen abzuziehen. Das Ergebnis ist ein [Cut](#Cut.md).}}


{{term|term=Directed Acyclic Graph}}

(abgekürzt als \"DAG\") {{defn|defn=Ein Typ eines [Abhängigkeitsgraphen](#Dependency_Graph.md) indem alle Beziehungen der Objekte in linearer Weise ohne zyklische Abhängigkeiten aufeinander aufbauen. Beim Verfolgen eines DAGs gibt es keinen Weg von einem Objekt A zu irgendeinen anderen Objekt und dann wieder zurück zum selben Objekt. In FreeCAD muss der Graph eines Modells immer ein "DAG" sein.}} {{term|term=Draft}} \> Entwurf oder Formschräge {{defn|no=1|defn=Arbeitsbereich Entwerfen,  vorwiegend 2D}} {{defn|no=2|defn=Formschräge von Gussteilen, die für deren Entnahme aus der Gussform erforderlich ist, siehe [[PartDesign Draft]]}}


{{term|term=Drawing}}

\> 2-dimensionale Standardansichten {{defn|no=1|defn=Erzeugen 2-dimensionaler Standardansichten 3-dimensionaler Objekte}} {{defn|no=2|defn=ein Arbeitsbereich zum Erzeugen 2-dimensionaler Standardansichten 3-dimensionaler Objekte, ergänzt zur technischen Zeichnung mittels Rahmen und Schriftfeld}}


{{glossend}}


</div>

## E


{{gloss}}


{{term|Edge}}

\> Kante {{defn|no=1|defn=Ein Segment, das zwei [Knoten](#Vertices/de.md) verbindet. Dieses Segment kann eine gerade Linie oder eine Kurve sein. Der CAD Kernel definiert es als: Eindimensionale Form, die einer Kurve entspricht und an jedem Ende durch einen Knoten begrenzt ist. Ein geschlossener Kreis hat daher nur einen Knoten, an dem er beginnt und endet. Siehe [ Profil: Definieren der Topologie](https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 "Open CASCADE Technology".md).}} {{defn|no=2|defn=Die Verbindungslinie zwischen zwei Flächen. Sie kann gekrümmt oder gerade sein.}} {{term|Element}} {{defn|Ein Element der Skizzierer Geometrie, wie z.B. ein Punkt, ein Liniensegment, ein Bogen, ein Kreis usw.}} {{term|Extrude}} \> Extrudieren {{defn|defn=Ein allgemeiner Begriff für die Ausdehnung eines 2D Objekts in 3D entlang 1 Richtung. Siehe auch [Polster](#Pad/de.md).}} {{glossend}}


<div class="mw-translate-fuzzy">

## F


{{gloss}}


{{term|1=Face}}

\> Fläche {{defn|defn=ein 2-dimensinales topologisches Konstrukt. Ein Würfel hat z.B. 6 solche Flächen. Eine Kugel hat eine Fläche. Die Flächen müssen nicht eben sein. Der [CAD-Kernel](#Geometric_modeling_kernel.md) definiert die Fläche als: Teil einer Oberfläche, die durch einen geschlossenen [Linienzug bzw. mehrere Linienzüge](#Wire.md) begrenzt ist. [ siehe Profile: Defining the Topology](https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3.md).}}


{{term|term=Facet}}

\> Facette {{defn|defn=Begriff für die ebene Fläche auf einem [Mesh = parkettierte Oberfläche](#Mesh.md), oder auch Masche in einer netzartigen Oberfläche.}}


{{term|term=FC}}

\> FC, Kurzform von FreeCAD


{{term|term=FCStd}}

\> Standardformat von FreeCAD-Dateien {{defn|defn=Datei-Endungen  *.fcstd, *.FCStd}}


{{term|1=Feature}}

\> Formelement {{defn|1=Ein Schritt bei der Erstellung eines dreidimensionalen Bauteils in dem [Arbeitsbereich PartDesign](PartDesign_Workbench/de.md), bei dem dem Bauteil ein weiteres Formelement hinzugefügt wird. Beispiele sind [Block](#Pad.md), [Tasche](#Pocket.md), [Nut](#Groove.md), [Verrundung](#Fillet.md), usw. Bei der Bearbeitung eines Modells im Arbeitsbereich PartDesign, übernimmt jedes neue Formelement (Feature) die [geometrische Figur](#Shape.md) des Schrittes zuvor und fügt etwas hinzu oder entfernt etwas. Somit ist ein Feature „Tasche“ nicht nur die hinzugefügte Öffnung, sondern repräsentiert das gesamte Bauteil einschließlich der hinzugefügten Tasche.}}


{{term|term=FEM}}


{{defn|defn=Finite Elemente Methode, ein [Arbeitsbereich](FEM_Workbench/de.md) mit dem die auftretenden Spannungen und Belastungen in einem Bauteil oder einer Konstruktion analysiert werden können.}}


{{term|term=Fillet}}

\> Rundung {{defn|defn=eine Rundung an einer Ecke oder einer Kante, siehe  [Part Kanten abrunden](Part_Fillet/de.md) und [Kanten abrunden](PartDesign_Fillet/de.md)}}


{{term|term=Fork}}

\> Gabel {{defn|defn=See [Forked Model](#Forked_Model.md).}}


{{term|term=Forked Model}}

\> verzweigtes Modell {{defn|defn=eine meist unbeabsichtigt und nicht korrekt durchgeführte Vervielfältigung eines Modells. Dies wird als Fehler angesehen. (Nicht zu verwechseln mit absichtlicher Vervielfältigung mit Werkzeugen wie Feld (Array)  Klonen (Duplikat) u.a.)}}


{{term|term=Frenet}}

\> Frenet {{defn|no=1|defn= Name eine französischen Mathematikers. siehe auch ([https://de.wikipedia.org/wiki/Frenetsche_Formeln Frenetsche_Formeln])}} {{defn|no=2|defn= Der Frenet-Parameter (tangential, binormal oder normal) bewirkt beim Verschieben eines Profils auf einer Helix mit dem ([Sweep Werkzeug](#Sweeping.md) ), dass dessen Orientierung zur Helix-Achse ausgerichtet bleibt.}}


{{term|term=Freetype|content=[http://www.freetype.org FreeType]}}

\> eine Software-Bibliothek {{defn|defn=eine freie Software zur Darstellung von FreeType-Schrifttypen}}


{{term|term=Frustum}}

\> Pyramidenstumpf {{defn|defn=ein zwischen zwei parallelen Schnitten befindliches Teil eines Körpers; Der Begriff wird auch in der Computervisualisierung zur Bezeichnung des sichtbaren Raumes benutzt. Nur Elemente zwischen den beiden Ebenen werden dargestellt. Dies führt in FreeCAD manchmal dazu, dass Objekte nicht oder nur angeschnitten dargestellt werden. Abhilfe schafft der Klick auf "Inhalt auf Bildschirmgröße einpassen".}}


{{term|term=Fully Constrained}}

\> vollständig bestimmt, Freiheitsgrad f = 0 {{defn|defn=siehe [Constraint](#Constraint.md)}}


{{term|term=Fuse}}

\> Boole\'sche Vereinigung {{defn|defn=siehe [boolean union](#Boolean_Operation.md)}} {{glossend}}


</div>

## G


{{gloss}}


{{term|GDB oder gdb}}


{{defn|defn=[https://www.gnu.org/software/gdb/ '''G'''NU Project '''D'''e'''B'''ugger], das Standard-Debuggingprogramm unter Linux und anderen 'nix Betriebssystemen um einen [ Stacktrace](https://de.wikipedia.org/wiki/Stacktrace.md) zu erhalten (siehe auch [backtrace](#Backtrace.md)). Der Stacktrace erlaubt Rückschlüsse darauf, welcher Programmteil für ein Problem verantwortlich ist. "gdb" (ohne die Anführungszeichen) ist auch der Aufrufname des GDB-Programms. Ein Beispiel wie der GDB mit FreeCAD genutzt werden kann, findet sich hier: [http://forum.freecadweb.org/viewtopic.php?t=7052#p56918 this forum post]}}


{{term|Geometric modeling kernel}}


{{defn|defn=Auch CAD-Kernel genannt. Eine Sammlung von komplexen Softwarebibliotheken, mit denen die 3D-Geometrien erzeugt werden. Alle geometrischen Operationen mit den 3D-Objekten (extrudieren, boolsche Operationen, Fasen und Rundungen an Kanten usw.) beruhen auf den CAD-Kernel. FreeCAD verwendet den CAD-Kernel Open CasCade Technology.}}


{{term|Git}}


{{defn|defn=[https://de.wikipedia.org/wiki/Git  verteilte Versionsverwaltung von Dateien] die von FreeCAD zur Verwaltung des Programmcodes benutzt wird.}}


{{term|[Group](Std_Group/de.md)}}

\> Gruppe {{defn|defn=wird zur Organisation der Objekte im Modellbaum benutzt. Mehrere Objekte lassen sich in einer Gruppe zusammenfassen.}} {{term|GUI}} \> graphische Benutzeroberfläche {{defn|defn='''G'''raphical '''U'''ser '''I'''nterface.  Ermöglicht die Bedienung von FreeCAD mittels Klickens des Mauszeigers auf graphische Symbole und Menüs.}} {{glossend}}

## H


{{gloss}}


{{term|Half_Space|content=[https://de.wikipedia.org/wiki/Halbraum Half_Space]}}

\> Halbraum {{defn|defn=Wenn eine Ebene komplett den dreidimensionalen Euklidischen Raum teilt, erhält man zwei Halbräume.}} {{glossend}}

## I


{{gloss}}


{{term|IGES}}


{{defn|defn=Ein standardisiertes Dateiformat für den Austausch von Produktgeometrien. Datei-Erweiterungen sind *.iges, *.igs. Vergleiche auch [STEP](#STEP.md).}}


{{term|Intersection|content=[http://en.wikipedia.org/wiki/Intersection Intersection]}}

\> \[<https://de.wikipedia.org/wiki/Menge_(Mathematik)#Durchschnitt_(Schnittmenge,_Schnitt>) Schnittmenge\] {{defn|defn=Der Teil, den zwei oder mehr geometrische Objekte gemeinsam haben. Beispielsweise ist die Schnittmenge von zwei sich schneidenden Geraden ein Punkt.}} {{glossend}}

## J


{{gloss}}


{{term|JT}}


{{defn|defn=Ein proprietäres 3D-Datenformat, entwickelt von Siemens PLM Software. FreeCAD unterstützt JT-Dateien momentan nicht.}}


{{glossend}}

## K


{{gloss}}


{{term|Kernel}}


{{defn|defn=Siehe [Geometric modeling kernel](#Geometric_modeling_kernel.md).}}


{{term|KML}}


{{defn|defn=Keyhole Markup Language - eine XML-basierte Auszeichnungssprache zur Beschreibung von Geodaten bekannt geworden durch die Verwendung bei Google Earth. FreeCAD hat aktuell (2018) keine Unterstützung für KML. [[https://de.wikipedia.org/wiki/Keyhole_Markup_Language KML]]}}


{{glossend}}


<div class="mw-translate-fuzzy">

## L


{{gloss}}


{{term|term=Label}}

\> Kennzeichnung {{defn|no=1|defn=Die Eigenschaft Label dient zur Kennzeichnung eines Objekts mit einer vom Benutzer eingetragenen Kennzeichnung. Eine eingetragene Kennzeichnung wird im Modellbaum angezeigt und dient der besseren Verständlichkeit.}} {{defn|no=2|defn=Ein beschreibender Text auf einer Zeichnung, (siehe auch [Draft Label](Draft_Label.md)).}} {{defn|defn=Vergleiche mit der Eigenschaft[Name](#Name.md).}} {{term|term=Line}} \> Linie {{defn|defn=Ein gerader Pfad zwischen zwei [Punkten](#Point.md).}} {{term|term=Lock}} \> Arretierung {{defn|defn=Die Bedingung [Constraint Lock](Sketcher_ConstrainLock/de.md) im Sketcher legt die Koordinaten für einen Punkt fest.}} {{term|term=Loft|content=[http://en.wikipedia.org/wiki/Loft_%283D%29 Loft]}} \> Ausformung {{defn|defn=Eine topologische Form. die durch das Verbinden von einer Reihe von aufeinanderfolgenden Profilen mit einer Oberfläche erzeugt wird. Dies ist ähnlich dem Prozess der Herstellung von mit Gewebe überzogenen Flugzeugen oder Booten. Auch die Funktion in FreeCAD zur Erstellung einer solchen Form wird so genannt.}} {{glossend}}


</div>

## M


{{gloss}}


{{term|Macro}}

\> Makro {{defn|defn=Eine gespeicherte Folge von FreeCAD-Anweisungen in der Scriptsprache Python. Es können entweder die Benutzeraktionen aufgezeichnet werden und als Makro gespeichert werden, oder das Makro wird vom Benutzer geschrieben.}} {{term|Manifold}} \> Mannigfaltigkeit {{defn|defn=Ein mathematischer Begriff, der im Zusammenhang mit FreeCAD meint, dass eine [geometrische Figur](#Shape.md) ein perfekt abgeschlossenes Volumen einschließt. Ein mehr geläufiges Synonym ist "wasserdicht". Um einen Körper aus einer [Hülle](#Shell.md) zu generieren, muss diese eine Mannigfaltigkeit sein.}} {{term|Mantis}} {{defn|defn=Der Name des vom FreeCAD-Projekt benutzten [Fehlerverfolgungssystems](#Tracker.md).}} {{term|Mesh}} \> Netz {{defn|defn=Eine Art von Objekt, die von FreeCAD importiert oder generiert werden kann. Für mehr Details siehe [Model}} \> Modell {{defn|defn=Auch 3D-Modell genannt. Es ist die Computer-Repräsentation eines dreidimensionalen [[#Part|Teils](https://de.wikipedia.org/wiki/Polygonnetz]].}} {{term.md) oder einer [Baugruppe](#Assembly.md).}} {{term|MultiTransform|content=[MultiTransform](PartDesign_MultiTransform.md)}} {{defn|defn=Steht für eine multiple Transformation. Ein [Feature](#Feature.md) des [PartDesign-Arbeitsbereiches](PartDesign_Workbench/de.md), der eine Serie von gleichen Transformationen (linear oder zirkuläres Muster oder gespiegelt) auf eine ausgewähltes Feature anwendet.}} {{glossend}}

## N


{{gloss}}


{{term|Name}}


{{defn|defn=Ein eindeutiger Bezeichner für ein Objekt eines FreeCAD-Dokuments. Der Name kann nicht mehr geändert werden, nachdem er einmal vom Programm vergeben wurde.  Siehe auch [Label](#Label.md).}}


{{term|Non-manifold}}


{{defn|defn=Non-manifold topology, also called zero-thickness, is two distinct solid bodies connected at a theoretical vertex or edge. It is an unsupported type of shape (not always detected by FreeCAD) that should be avoided, as it can cause trouble with further steps and export.}}


{{term|Null Shape}}


{{defn|defn=Ein [Shape](#Shape.md) welches nicht korrekt initialisiert wurde durch das erzeugende Programm oder Makro. Dies ist im allgemeinen ein Fehlerzustand.}}


{{glossend}}

## O


{{gloss}}


{{term|OCC}}


{{defn|defn= Abkürzung für [Open CASCADE](#Open_CASCADE.md). Bevor der Code frei verfügbar gestellt wurde, wurde er gewöhnlich CAS.CADE genannt (abgekürzt von Computer Aided Software for Computer Aided Design and Engineering).}}


{{term|OCE}}


{{defn|defn='''O'''pen CASCADE '''C'''ommunity '''E'''dition. Ein Projekt, das das offizielle [Open CASCADE](#Open_CASCADE.md) mit Korrekturen, Verbesserungen und experimentellem Code von Benutzern zur Verfügung stellte. FreeCAD arbeitet sowohl mit OCC als auch mit OCE.}}


{{term|OCCT}}


{{defn|Open CASCADE Technology. Siehe [OCC](#OCC.md).}}


{{term|Open CASCADE|content=[http://www.opencascade.org Open CASCADE]}}


{{defn|Der [Geometrie Modellkernel](#Geometric_modeling_kernel.md) (Softwarebibliothek), die FreeCAD zugrunde liegt. Auch [OCC](#OCC.md) oder [OCCT](#OCCT.md) (für Open CASCADE Technologie) genannt. Siehe auch [OCE](#OCE.md).}}


{{term|OpenSCAD|content=[http://www.openscad.org/ OpenSCAD]}}


{{defn|no=1|Der Name eines reinen skriptbasierten CAD Programms.}}


{{defn|no=2|Ein [Arbeitsbereich](#Workbench/de.md) in FreeCAD. Der [OpenSCAD](OpenSCAD_Workbench/de.md) [Arbeitsbereich](#Workbench/de.md) stellt eine Schnittstelle für den Import/Export von *.scad und *.csg Modellen zur Verfügung, sowie einige Werkzeuge zur Objektbearbeitung.}}


{{term|term=Origin}}

-\> Koordinatenursprung {{defn|defn=Das Zentrum eines Koordinatensystems. Alle Achsen starten von hier in entweder positiver oder negative Richtung. Ähnlich wie der Blick ins All mit der Erde als „Ursprung“.}} {{term|Orthographic}} -\> orthogonal {{defn|defn=Siehe [https://de.wikipedia.org/wiki/Orthogonalprojektion Orthogonalprojektion] und [https://de.wikipedia.org/wiki/Normalprojektion Normalprojektion].}} {{glossend}}


<div class="mw-translate-fuzzy">

## P


{{gloss}}


{{term|1=Pad}}

\> Block {{defn|1=Eine Erweiterung einer [Skizze](#Sketch.md) in die Richtung der Normalen zur Skizzenebene. Dabei wird aus der zweidimensionalen Skizze ein dreidimensionales Objekt erzeugt. Siehe auch [Extrusion](#Extrude.md).}} {{term|Part|content=[Part](Part_Workbench/de.md)}} \> Bauteil {{defn|no=1|Ein FreeCAD [Arbeitsbereich](#Workbench.md). Die verfügbare Arbeitsweise ist hauptsächlich [https://de.wikipedia.org/wiki/Constructive_Solid_Geometry Konstruktive Festkörpergeometrie].}} {{defn|no=2|Ein einvolumiger Körper. Die einfachste Komponente in einer Baugruppe.}} {{defn|no=3|Ein Container, der alle Typen von FreeCAD-Objekten gruppieren kann und eine [Platzierung](#Placement.md) besitzt (eingeführt in FreeCAD V0.17.)}} {{term|PartDesignNext}} {{defn|defn=Der Spitzname aus den Foren, um den [PartDesign-Arbeitsbereich](PartDesign_Workbench/de.md), der sich in der FreeCAD Version 0.17 von der Version v0.16 und früher durch weitgehende Änderungen der Arbeitsweise geändert hat, von dem ursprünglichen PartDesign zu unterscheiden.}} {{term|PD}} {{defn|defn=Abkürzung von [PartDesign](PartDesign_Workbench/de.md), einem [Arbeitsbereich](#Workbench.md) von FreeCAD.}} {{term|PDN}} {{defn|defn=Abkürzung von [PartDesignNext](#PartDesignNext.md).}} {{term|Perspective}} \> Perspektive {{defn|defn=[http://en.wikipedia.org/wiki/Graphical_projection#Perspective Perspective projection]}}


{{term|term=Pivy|content=[http://pypi.python.org/pypi/Pivy Pivy]}}


{{defn|defn=Eine Software-Bibliothek, die es Python erlaubt [[#Coin]] zu benutzen.}}


{{term|term=Placement}}

\> Platzierung {{defn|defn=Eine Zusammenstellung von Eigenschaften eines Objekt, das seine Koordinaten und die Orientierung im Raum definiert. Siehe [Platzierung](Placement/de.md).}} {{term|term=Planar}} \> eben {{defn|defn=Die Eigenschaft einer Geometrie, bei der alle Elemente in der selben Ebene liegen.}} {{term|Plane}} \> Ebene {{defn|no=1|Eine flache, zweidimensionale Fläche, die sich bis ins Unendliche erstreckt.}} {{defn|no=2|Ein grundlegendes zweidimensionales Objekt, das in dem Arbeitsbereich Part erstellt werden kann. Dort ist die Ebene jedoch mit Begrenzungen versehen.}} {{term|Plot}} {{defn|defn=<To be added.>}} {{term|1=Pocket}} {{defn|1=A [feature](#Feature.md) that removes material from a solid based on a [Sketch](#Sketch.md).}} {{term|1=Point}} \> Punkt {{defn|1=Eine Bezeichnung für einen Ort in dem 3D Arbeitsraum. Ein “Punkt” hat keine Ausdehnung. Er hat eine Ausdehnung auf dem Bildschirm, gewöhnlich durch ein Pixel dargestellt, so dass der Punkt sichtbar ist. Siehe auch [Vertex](#Vertex.md).}} {{term|Polygon mesh}} {{defn|defn=See [http://en.wikipedia.org/wiki/Polygonal_mesh Polygonal_mesh]}} {{term|Polyline}} \> Polylinie {{defn|defn=Eine Bezeichung für eine Reihe miteinander verbundener Kanten aus Geraden und Bögen.}} {{term|POV-Ray}} {{defn|defn=[http://en.wikipedia.org/wiki/POV-Ray POV-Ray] Ein Programm zum Erzeugen von photorealistischen Bilder aus dreidimensionalen Szenen.}} {{term|PPA}} {{defn|defn=Ein Akronym für '''P'''ersonal '''P'''ackage '''A'''rchive. Es ist eine Art von Software-Repositorium exklusiv für das Ubuntu-Linux-Betriebssystem. The FreeCAD project offers the latest release as well as development versions through two PPA repositories. Aktualisierungen werden über das Paketverwaltungssystem des Betriebssystems durchgeführt.}} {{term|Primitive}} \> Grundkörper {{defn|defn=Eine grundlegende Form, die bei der Kontruktion von Modellen benutzt wird. Einige 2D-Körper sind: Punkt, Linie, Polygon, Kreis, Ellipse, Spirale, Helix. 3D-Körper: Quader, Zylinder, Kegel, Torus, Kugel, Ellipsoid, Prisma.}} {{term|term=PySide|content=[http://www.pyside.org PySide]}} {{defn|defn=Eine frei verfügbare Sofware-Bibliothek, die es Python erlaubt, QT zu nutzen.}} {{term|term=Python|content=[http://www.python.org Python]}} {{defn|defn=Eine Programmiersprache, die sowohl bei der Entwicklung von FreeCAD als auch in benutzergeschriebenen [Makros](#Macro.md) oder Skripten verwendet wird.}} {{glossend}}


</div>

## Q


{{gloss}}


{{term|Qt|content=[http://qt-project.org Qt]}}


{{defn|1=Eine plattformübergreifende Bibliothek zur Erstellung von grafischen Benutzeroberflächen. Siehe auch Qt4.}}


{{glossend}}

## R


{{gloss}}


{{term|Raytracing}}


{{defn|defn=[https://de.wikipedia.org/wiki/Raytracing Raytracing] Ein Verfahren um aus einer dreidimensionalen Szene ein Bild durch Verfolgen von Lichtstrahlen zu generieren.}}


{{term|Revolve}}

-\> Drehen {{defn|defn=Ein Werkzeug aus dem [Part](Part_Workbench/de.md)-[workbench](#Workbench/de.md). Siehe [Drehen](Part_Revolve/de.md).}} {{term|Robot}} -\> Roboter {{defn|defn=[https://de.wikipedia.org/wiki/Industrieroboter Industrieroboter] Sowie ein Arbeitsbereich in FreeCAD zur Simulation eines Industrieroboters.}} {{term|Rotate}} -\> Rotation {{defn|defn=Die Aktion bei der ein Objekt um eine Achse gedreht wird, um seine Orientierung im Raum zu ändern.}} {{glossend}}

## S


{{gloss}}


{{term|Section}}

-\> Schnitt {{defn|defn=Schnitt durch einen Körper, siehe auch [https://de.wikipedia.org/wiki/Schnitt_(Darstellung)]. FreeCAD enthält Werkzeuge um Schnitte als geometrische Objekte, als auch um Schnitte zur Dokumentation in Zeichnungen zu erstellen.}} {{term|Self Intersection}} {{defn|defn=Ein Zustand, bei dem sich zum Beispiel eine Kurve mit sich selber schneidet (wie '8','&'). Dies kann der Geometrie-Kernel nicht verarbeiten und verursacht im allgemeinen einen Fehlerzustand.}} {{term|Shape}} {{defn|defn=Generische Bezeichnung, die in FreeCAD für die meisten Elemente benutzt wird. (Ausser für [meshes](#Mesh.md)) Der Begriff kann am ehesten mit geometrische Figur übersetzt werden. [https://de.wikipedia.org/wiki/Geometrische_Figur] In einem FreeCAD-Objekt enthält das Shape die geometrische Form.}} {{term|Shell}} -\> Hülle {{defn|defn=Hülle aus zwei oder mehr miteinander verbundenen Flächen (= [faces](#Face.md)). Eine vollkommen geschlossene Hülle([manifold](#Manifold.md)) kann in einen soliden Körper umgewandelt werden.}} {{term|1=Sketch}} -\> Skizze {{defn|1=Eine zweidimensionale Skizze auf einer Ebene oder auf einer ebenen Fläche ([Face](#Face.md)).  In FreeCAD ist eine Skizze immer ein zweidimensionales Objekt irgendwo im dreidimensionalen Raum.}} {{term|Sketcher|content=[Sketcher](Sketcher_Workbench/de.md)}} {{defn|defn=Ein Arbeitsbereich = [workbench](#Workbench.md) um zweidimensionale Konturen aus allgemeinen Geraden- und Kurvenelementen [elements](#Element.md) zur erstellen, die mit Hilfe von [constraints](#Constraint.md) festgelegt werden. Intern wird aus allen Eingaben ein nichtlineares Gleichungssystem erzeugt.}} {{term|Sketcher Solver}} {{defn|defn= Der FreeCAD-interne-Mechanismus, der das nichtlineare Gleichungssystem löst, dass sich aus den geometrischen [Elementen](#Element.md) und den dazugehörigen [Festlegungen](#Constraint.md) ergibt. Das Ergebnis der Berechnung ist die Position aller Punkte in der Skizze.}} {{term|Smooth Line}} {{defn|defn=In a Drawing, a line indicating a change between tangent surfaces, as in the transition from a flat surface to a fillet. Also "tangent edge". See [http://www.freecadweb.org/wiki/index.php?title=Drawing_View#Modify_an_existing_view Drawing View]}} {{term|Solid}} -\> Volumenkörper {{defn|defn=Teil des dreidimensionalen Raums, der durch eine [Hülle](#Shell.md) begrenzt wird. Ein Volumenkörper besitzt ein Volumen und weitere Eigenschaften, die Objekte mit einer Masse aufweisen.}} {{term|Solver}} {{defn|defn=See [Sketcher Solver](#Sketcher_Solver.md).}} {{term|1=Stable}} {{defn|1=Der Spitzname der zuletzt veröffentlichten offiziellen Version von FreeCAD. Dies ist oft die Version, die in Linux-Distributionen zur Verfügung steht. Vergleiche mit [Unstable](#Unstable.md).}} {{term|STL}} {{defn|''STereoLithography'', auch bekannt als ''Standard Tessellation Language.'' Ein [mesh](#Mesh.md) Dateiformat, das nur die Oberfläche eines 3D-Objektes mit Hilfe von Facetten definiert. Die Dateierweiterung ist *.stl}} {{term|term=STEP}} {{defn|defn=Ein Dateiformat nach dem ISO standard (ISO 10303) für den Auschtausch von 3D Daten und Produktinformationen. Es ersetzt weitgehend [IGES](#IGES.md). Dateinamenserweiterungen sind *.step, *.stp.}} {{term|SVG|content=[[SVG]]}} {{defn|[https://de.wikipedia.org/wiki/Scalable_Vector_Graphics]. Ein Dateiformat für Vektorgrafik.}} {{term|term=Sweep}} -\> Austragung {{defn|defn=Ein Verfahren welches ein 3-dimesionales Objekt generiert, in dem mindestens eine Kurve entlang einer Trajektorie (Pfad) geführt wird. Es können Körper oder Oberflächen erzeugt werden. Das dazu gebrauchte Werkzeug, sowie die entstandene Form werden oft genauso benannt. Siehe auch [http://de.wikipedia.org/wiki/Sweep_(Grafik)] (deutsch) [http://en.wikipedia.org/wiki/Solid_modeling#Sweeping Solid modeling] (englisch)}} {{glossend}}

## T


{{gloss}}


{{term|Task panel}}

-\> Bedienfeld {{defn|See [Tasks tab](#Tasks_tab.md).}} {{term|Tasks tab}} -\> Bedienfeld für die aktuelle Aufgabe {{defn|Ein Bedienfeld in FreeCAD, das die spezifischen Möglichkeiten für die aktuell anstehende Aufgabe anzeigt. Es kann die verfügbaren Werkzeuge in dem gerade offenen [Arbeitsbereich](#Workbench.md) anzeigen oder die einzustellenden Werte und Optionen für das gerade aktive [Kommando](#Command.md) zeigen.}} {{term|Tessellation}} -\> Parkettierung {{defn|Die Parkettierung einer Oberfläche ist das Pflastern dieser Oberfläche mit einem oder mehreren Typen von geometrischen Kacheln ohne Überlappung und ohne Lücken. In FreeCAD wird das benötigt, um die geometrischen Figuren in der 3D-Ansicht darzustellen. Die Größe der Kacheln relativ zu den Abmessungen der geometrischen Figuren kann in den Einstellungsdialog eingestellt werden. Man kann dadurch eine glattere Oberfläche von gekrümmten Teilen auf Kosten der Berechnungszeit erhalten. Siehe auch [Einstellungen...](Preferences_Editor/de.md).}} {{term|Thickness}} {{defn|no=1|Ein Maß für die Dicke eines Teils.}} {{defn|no=2|Ein Werkzeug des [Part-Arbeitsbereiches](Part_Workbench.md), um einen [Volumenkörper](#Solid.md) auszuhöhlen und mit einer gleichmäßigen Wandung einer definierten Dicke zu versehen. (Aufdicken) }} {{term|Toggle}} -\> Umschalter {{defn|Eine Einstellmöglichkeit, die eine von zwei Werten annehmen kann, zum Beispiel `True` oder `False`, oder Aus oder An.}} {{term|Topological Naming}} {{defn|Ein Schema, bei dem einer erzeugten Kante oder Fläche eine dauerhafter Name erteilt wird. Intern identifiziert FreeCAD die Kanten (edge) und Flächen (face) eines Volumenkörpers durch Nummerierung: Edge1, Edge2, Face1, Face2, usw. Das Problem ist, das diese Namen eher zufällig vergeben werden und dass sie sich ändern, wenn der Körper so geändert wird, dass sich die Zahl der Kanten oder Flächen ändert. Zum Beispiel kann sich ein Element, das mit der Fläche Nr. 2 verbunden ist, nach der Änderung des Modells mit einer völlig anderen Fläche verbunden sein, die jetzt die Flächennummer 2 bekommen hat. Dies wirkt sich für den Benutzer als Fehler aus, da er ein unerwünschtes Ergebnis erhält. Bei der Version 0.17 von FreeCAD wurde eine brauchbare topologische Benennung mit dauerhaften Namen noch nicht implementiert, so dass sich bei einer Modifizierung eines Objektes die Namen der Kanten und Flächen leider auch ändern können.}} {{term|Torus}} {{defn|Ein Grundkörper aus dem Arbeitsbereich Part.}} {{term|Tracker}} {{defn|Kurzform für das Fehlerverfolgungssystem, die webbasierte Software zur Verwaltung der gemeldeten Fehler und Verbesserungswünsche. Siehe auch [Mantis](#Mantis.md).}} {{glossend}}

## U


{{gloss}}


{{term|Union}}

-\> Vereinigung {{defn|defn=Ein Werkzeug des [Part](Part_Workbench/de.md) [Arbeitsbereichs](#Workbench/de.md), das eine [Boolsche Operation](#Boolean_Operation.md) mit den ausgewählten Körper in Form der Vereinigung durchführt.}} {{term|1=Unstable}} {{defn|1=Ein Spitzname für die aktuelle Entwicklungsversion von der FreeCAD Software. Diese Version enthält die aktuellen Änderungen der Entwickler. Sie liefert üblicherweise keine falschen Ergebnisse, aber wurde noch nicht gründlich getestet und kann sich auch noch ändern. Es ist nicht garantiert, dass sich Modelle, die mit dieser Version erzeugt wurden, später problemlos öffnen lassen.}} {{term|Upgrade|content=[Upgrade](Draft_Upgrade.md)}} {{defn|defn=Ein Werkzeug des [Draft](Draft_Workbench/de.md) [Arbeitsbereichs](#Workbench/de.md).}} {{glossend}}

## V


{{gloss}}


{{term|Vector}}

\> Vektor {{defn|defn=Eine Größenordnung mit einer Richtung. Oft grafisch als Pfeil in 2 oder 3 Dimensionen dargestellt. Zum Beispiel sind "fünfzig Schritte nach Norden", "9,8 m/s^2 nach unten" und "(3,5,6) Einheiten in der x, y, z Richtung" alles Vektoren. In FreeCAD werden sie am häufigsten als geordnete Paare (x, y) oder geordnete Tripel (x, y, z) bezeichnet.}} {{term|Vertex}} \> Knoten {{defn|defn=Ein einzelner [Punkt](#Point.md) im Raum oder die Ecke einer [Form](#shape.md), wo [Kanten](#Edge.md) aufeinander treffen. Die offene Kaskadentechnologie definiert ihn als nulldimensionale [Form](#shape.md), die einem Punkt in der Geometrie entspricht. [ siehe OCCT Profil: Definieren der Topologie](https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3.md)}} {{term|Vertices}} {{defn|defn=Plural von [Vertex](#Vertex.md)}} {{term|Viewprovider}} {{defn|defn=Allgemeine Schnittstelle für alle visuellen Dinge in FreeCAD. Ein ViewProvider generiert und handhabt alles rund um die Visualisierung und Präsentation von Objekten aus dem FreeCAD [App Layer](#App.md) für den Anwender. Diese Klasse und ihre Nachkommen müssen für jeden Objekttyp implementiert werden, um sie in der [3DView](#3DView.md) und [TreeView](#TreeView.md) anzuzeigen.}} {{glossend}}

## W


{{gloss}}


{{term|WB}}


{{defn|defn=Abkürzung für [workbench](#Workbench.md).}}


{{term|Wire}}

\> Linienzug {{defn|no=1|Eine Folge von [vertices](#Vertex.md) (Knoten), die durch [edges](#Edge.md) (Kanten) verbundenen sind. Der Begriff wird in diesem Sinn hauptsächlich von Open Cascade Technology [no=2|Ein [[Draft_Workbench/de|Draft](https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3]] verwendet und daher auch innerhalb von FreeCAD.}} {{defn.md) [workbench](#Workbench.md)-Befehl, der einen parametrisierten Linienzug erstellt.}} {{term|Workbench}} \> Arbeitsbereich {{defn|defn=Auch als Modul bezeichnet gruppiert jede(r) [workbench](Workbenches.md) (Arbeitsbereich) einen Satz von Werkzeugen für eine bestimmte Aufgabe.}} {{glossend}}

## X


{{gloss}}


{{term|X}}


{{defn|Bezieht sich im Allgemeinen auf die 2D oder 3D X [Achse](#Achse.md).}}


{{glossend}}

## Y


{{gloss}}


{{term|Y}}


{{defn|Bezieht sich im Allgemeinen auf die 2D oder 3D Y [Achse](#Achse.md).}}


{{glossend}}

## Z


{{gloss}}


{{term|Z}}


{{defn|Bezieht sich im Allgemeinen auf die 2D oder 3D Z [Achse](#Achse.md).}}


{{glossend}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Wiki](Category_Wiki.md) > [Glossary](Category_Glossary.md) > Glossary/de
