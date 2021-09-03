


<div id="itsfree" style="text-align:left;color:black;background:#f6f6f6;margin:1em 7em;padding:0.5em 2em;border:2px solid #a7d7f9;">

*Diese Version von FreeCAD ist unserem Freund Roland Frank gewidmet, [der uns im Jahr 2017 verlassen hat](https://forum.freecadweb.org/viewtopic.php?f=8&t=25673). Er war ein aktives und sehr geschätztes Mitglied des FreeCAD-Forums und seine Video-Tutorien auf den Youtube-Kanälen [Learn FreeCAD](https://www.youtube.com/watch?v=_HEvhclR4-o&list=PL6fZ68Cq3L8k0JhxnIVjZQN26cn9idJrj) und [BPLFRE](https://www.youtube.com/watch?v=m49z0weonog&list=PLsrwVwvqYb8G4Ri0iz1JIebsOXkgoytAY) haben vielen Menschen geholfen sich in FreeCAD zurechtzufinden.*


</div>

FreeCAD 0.17 wurde am 6. April 2018 veröffentlicht, man kann es auf der [Download](Download/de.md)-Seite herunterladen. Dies ist eine Zusammenfassung der interessantesten Änderungen. Die komplette Liste der Änderungen kann unter [MantisBT bugtracker FC 0.17 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=73) auf Englisch nachgelesen werden.

Ältere Veröffentlichungsnotizen von FreeCAD sind unter [Feature list](Feature_list#Release_notes/de.md) zu finden.

<img alt="" src=images/Release017_Title.jpg  style="width:800px;"> 
*Garten-Eisenbahnwagen Orenstein&Koppel (by FreeCAD-User \"Garden Railway Coach O&K\", see [Users Showcase](http://forum.freecadweb.org/viewtopic.php?f=24&t=17261))*

## Highlights

Es ist beinahe zwei Jahre her, seit der Veröffentlichung der vorherigen Version 0.16, aber das FreeCAD-Team hat sich in dieser Zeit nicht ausgeruht. Nahezu 6800 Änderungen wurden seitdem dem Quellcode von FreeCAD hinzugefügt. Zum Vergleich: das ist mehr als dreimal so viel, als zwischen den Versionen 0.15 und 0.16 geändert wurde! Die meisten Arbeitsbereiche haben von diesen Verbesserungen profitiert und zwei komplett neue Arbeitsbereiche wurden hinzugefügt. Weitere neue Module wurden von der FreeCAD-Gemeinde entwickelt. Einige der Glanzlichter:

Der Arbeitsbereich **PartDesign** wurde komplett überarbeitet. Ein neuer Körpercontainer nimmt jetzt eine Kette von Features (Formelementen) auf und enthebt von der Anforderung, die Skizzen auf ebenen Körperflächen anbringen zu müssen. Neue Werkzeuge zum Erstellen von Bezugsgeometrien wie Punkte, Achsen und Ebenen machen PartDesign erheblich vielseitiger. ![](images/PartDesign_Body_tree.png )

Der neue über das Werkzeug-Menü zugängliche [Addon manager](AddonManager/de.md) (der vorher als Makro zur Verfügung stand unter [addons installer macro](https://github.com/FreeCAD/FreeCAD-addons)) macht das Installieren und das Aktualisieren von zusätzlichen Modulen und Makros viel leichter und einheitlicher unter Windows, Mac OS X und Linux. <img alt="" src=images/Addon_manager_v017.png  style="width:300px;">

Der Arbeitsbereich **Sketcher** unterstützt nun die Erstellung von B-splines mit verschiedenen Weisen die Kontrollkurven zu bearbeiten und die Kurvendaten anzuzeigen. <img alt="" src=images/FC017_Sketcher_B-spline_01.png  style="width:300px;">

Der neue **Arbeitsbereich TechDraw** zielt darauf den Arbeitsbereich Drawing zu ersetzen und hat bereits mehr Werkzeuge als der alte Arbeitsbereich Drawing. <img alt="" src=images/TechDraw_Workbench_Example.png  style="width:300px;">

## Allgemein

-   Yorik van Havre schrieb das \"[Das FreeCAD Handbuch](Manual:Introduction/de.md)\", ein einführendes Buch über die Benutzung von FreeCAD.
-   Die Neuberechnung des Dokumentes kann nun über das Kontextmenü deaktiviert und aktiviert werden.
-   Es gibt einen neuen Revit-Navigationsstil.
-   Eine neue Navigationsanzeige an der unteren rechten Ecke des FreeCAD-Fensters erlaubt einen schnellen Zugriff auf den Navigationsstil.

![](images/FC017_Navigation_Indicator_01.png ) ![](images/FC017_Navigation_Indicator_02.png )

-   Dem [Abhängigkeitsgraphen](Std_DependencyGraph/de.md) kamen grafische Verbesserungen zugute.
-   Der STEP-import setzt auf den neuen [Partcontainer](Std_Part/de.md) auf und benutzt ihn, um die importierte STEP-Baugruppe in Unterbaugruppen zu organisieren und gibt damit weit besser die Struktur des Originaldokuments wieder. stpZ (ein komprimiertes STEP-Format) wird nun unterstützt.
-   Die meisten Icons in FreeCAD wurden überarbeitet und stimmen num besser mit den [Tango guidelines\|Tango-Richtlinien](http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines) überein.

-   Das FreeCAD-Projekt bedankt sich (acknowledges) für die Beiträge der Community durch Hinzufügen eines Credits-Reiters in der \"About FreeCAD\"-Anzeige. Neue License- und Libraries-Reiter zeigen die FreeCAD-Lizenz und bieten Informationen zu verwendeten Bibliotheken Dritter.

<img alt="" src=images/AboutFreeCAD_Credits.png  style="width:300px;">

## Arbeitsbereich Arch {#arbeitsbereich_arch}

-   Neues Werkzeug [Arch Schedule/de](Arch_Schedule/de.md): Diese Werkzeug wurde komplett überarbeitet und bietet nun einen viel flexibleren Weg, Daten aus dem Dokument in einer Tabelle zu sammeln. Es können verschiedene Arten von Abfragen, wie Zählen von Objekten eines bestimmten Typs oder Aufsummieren des Volumens einer bestimmten Kategorie von Objekten verwendet werden.

-   Ein neuer Satz von [Rohrwerkzeugen](Arch_Pipe/de.md) um Rohrsystem zu entwerfen. Man kann Linien, Skizzen oder Linienzüge benutzen, um Rohre zu platzieren und automatisch Verbindungen zwischen 2 oder 3 Rohren generieren.

-   Das [Arch Struktur Werkzeug](Arch_Structure/de.md) wurde um eine Reihe von neuen Voreinstellungen erweitert, um vorgefertigte Betonelemente zu generieren.

-   Während der 2017er Auflage vom [Google Summer of Code](Google_Summer_of_Code.md), an der FreeCAD partizipiert hat, wurde das [Arch Rebar](Arch_Rebar/de.md) Werkzeug wesentlich erweitert und bekam eine freundliche Benutzerschnittstelle, um die Betonstrukturen einfach mit verschiedene Typen von Bewehrungen zu versehen.

<img alt="" src=images/Arch_Rebar_preview.png  style="width:640px;">

-   [Fenster](Arch_Window/de.md) bekam verschiedene Erweiterungen, wie die Möglichkeit Unterkomponenten als \"zu öffnend\" zu definieren, Symbole für \"zu öffnend\" anzuzeigen, offen zu erscheinen und Lüftungsöffnungen zu integrieren.

<img alt="" src=images/Arch_Door_preview.png  style="width:640px;">

-   Das [Arch Achsen](Arch_Axis/de.md) Werkzeug wurde ebenso neu geschrieben und erlaubt mehr komplexe Systeme durch das Kombinieren von verschiedenen Serien von Achsen. Sie können desweiteren angepasst werden, um verschiedenen Situationen wie Ebenen anzuzeigen.

-   Ein neues Werkzeug [Arch Grid](Arch_Grid/de.md) erlaubt ein einfaches Erstellen von Objekten ähnlich zu Tabellenkalkulationen durch Strecken, Vereinigen oder Aufteilen von Zellen. Diese Gitterobjekte können als Achsensysteme benutzt werden oder als Basis für ein komplexes Fenster oder für ein Arrangement von Tafeln.

-   Ein neues [Tafelschnittwerkzeug](Arch_Panel_Cut.md) wurde speziell für die Tafelkonstruktion geschaffen. Damit ist es möglich ein Modell aus [Arch Panels](Arch_Panel/de.md) zu designen und dann Schnittmuster zu generieren, die direkt in dem Arbeitsbereich [Pfad](Path_Workbench/de.md) genutzt werden können, um G-Code für den Schnitt zu erstellen.

-   Ein neues (immer noch experimentelles) Werkzeug [Nesting](Arch_Nest/de.md), das es erlaubt,, durch das automatische Platzieren von 2D-Elementen in eine vorgegebene Form Schnittmuster zu erstellen.

-   [Multi-materials](Arch_MultiMaterial/de.md) wurden in den Arbeitsbereich Architektur eingeführt. Damit können automatisch mehrlagige Wände erstellt oder die verschiedenen Materialien in Verbundobjekten wie Fenstern organisiert werden.

-   Die Exportfunktionen für OBJ und DAE aus dem Arbeitsbereich Arch unterstützen nun Materialen sowohl beim Importieren als auch beim Exportieren.

-   Eine Ünterstützung für den Import des Formates [3DS](Arch_3DS.md) wurde hinzugefügt.

## Arbeitsbereich Draft {#arbeitsbereich_draft}

-   [Autogroup system](Draft_AutoGroup.md): Der Arbeitsbereich Draft offeriert nun eine Schaltfläche **auto-group** in der Hauptwerkzeugleiste. Alle neuen Draft- und Archobjekte werden automatisch in diese Gruppe platziert, wenn Auto-group aktiviert ist.

-   [Gefälle-Werkzeug](Draft_Slope.md): Wenn das Gefälle-Werkzeug auf eine [Draftlinie](Draft_Line/de.md) oder einen [Draft-Kantenzug](Draft_Wire/de.md) angewandt wird, erlaubt das Werkzeug dem Objekt eine vorgebene Steigung bzw. vorgegebenes Gefälle zu geben. Das heißt, die Zwischenpunkte und der Endpunkt bekommen niedrigere Z-Werte, so dass das gesamte Objekt eine konstante Steigung aufweist. Dies ist hilfreich für Linien oder Kantenzüge, die als Basis für Objekte dienen, die eine präzises Gefälle aufweisen müssen, wie Dachflächen oder Abwasserleitungen.

-   [Working Plane proxies](Draft_SetWorkingPlaneProxy/de.md): Beim Arbeiten mit [Draft working planes](Draft_SelectPlane/de.md) ist es oft notwendig die Lage von häufig genutzten Arbeitsebenen zu speichern. Dies ist nun möglich durch die Platzierung eines dieser Proxies (Stellvertreters) in dem Dokument. Es speichert die Lage der aktuellen Arbeitsebene und kann auch die aktuelle Ansicht und Objektsichtbarkeit wieder herstellen.

<img alt="" src=images/Draft_WP_preview.png  style="width:640px;">

-   [Draft Stretch/de](Draft_Stretch/de.md): Der Arbeitsbereich Draft hat nun ein Streckwerkzeug, das es erlaubt, die Eckpunkte (Vertices) von mehreren Draftobjekten auf einmal zu bewegen.

-   [Draft Label](Draft_Label.md): Mit diesem Werkzeug können Erläuterungen im Dokument platziert werden, die aus einem Text und einer Bezugslinie bestehen, die entweder frei oder angeheftet an ein spezifisches Objekt platziert wird. Der Text kann entweder einen beliebigen Text oder automatisch einen Eigenschaftsinhalt des Zielobjektes darstellen.

<img alt="" src=images/Draft_Label_Preview.png  style="width:640px;">

## Arbeitsbereich FEM {#arbeitsbereich_fem}


<div class="mw-translate-fuzzy">

-   FEM Mesh
    -   **Gmsh object** ToDo
    -   **Boundary layer object for gmsh** ToDo
    -   **Mesh group object for gmsh** ToDo
    -   **Mesh region object for gmsh** ToDo
    -   **GUI clear mesh tool** ToDo
    -   **GUI print mesh info tool** ToDo
    -   **GUI mesh view provider** Darstellung von sowohl Vierecknetzen als auch Hexaeder-, Pentaeder- und Pyramidennetzen
    -   **Mesh data model** Update von SMESH zu Version 7.7.1 <https://github.com/FreedCAD/FreeCAD/commit/666a3e5a>
    -   **Mesh API** Fähigkeit Netzgruppendaten aus dem FreeCAD SMESH FEM-mesh-Daten mittels Python zu lesen. Dies war die Basis für das Gmsh-Gruppen-Objekt:
    -   **Mesh API** Export von Netzgruppen in das inp-Dateiformat
    -   **FEM mesh 2 mesh tool** Werkzeug um die Oberfläche eines Volumennetzes in ein Oberflächennetz für das FreeCAD Mesh Modul zu konvertieren
    -   **Mesh problems** nicht positive Jacobi-Matrizen ist ein häufig gesehenes Problem in den FEM-Netzen. Elemente, die nicht positive Jacobi-Matrizen in dem CalculiX-Solver aufweisen, werden farbig dargestellt.
-   Neu unterstützte Analysetypen von Calculix
    -   **Coupled Thermal Structural Analysis**
    -   **1D pipe Flow analysis Analysis**
    -   **Coupled Beam Shell Solid models**


</div>

-   Objects
    -   **Beam rotation object** enables the analysis of beams rotated around their main axis.
    -   **Nonlinear material object** adds nonlinear material behavior to FreeCAD FEM. It supports linear change of stress strain curve.
    -   **Fluid material** \...
    -   **Constraint initial flow velocity** \...
    -   **Constraint fluid boundary**
    -   **Constraint electrostatic potential** \...
    -   **Constraint body heat source** \...
    -   **Constraint transform** \...
    -   **Constraint temperature** \...
    -   **Constraint contact** \...
    -   **Constraint plane rotation** \...
    -   **Constraint self weight** \...

-   Solver
    -   **Solver frame work** was written from scratch during a Google Summer of Code project.
    -   Support for FEM solver software **ElmerFEM**, <https://www.csc.fi/web/elmer>, was added.
    -   Inside the solver frame work the analysis type can be chosen by an **equation object** (Elmer solver only, ATM.)
    -   Basic support for FEM solver software **Z88**, <https://en.z88.de/z88os/>, was added.
    -   **CalculiX** was ported to the solver frame work. The ccxtools solver object remains in FreeCAD FEM because it is very well tested and has extended pre checks.

-   Calculix analysis
    -   **Coupled Thermal Structural Analysis** \...
    -   **1D pipe Flow analysis Analysis** \...
    -   **Coupled Beam Shell Solid models** \...

-   Standard Post Processing
    -   **Shell and beam 3D output** Make it possible to output shell and beam analysis as 3D solid output to see stresses in sections.
    -   **Peeq strain** Support for equivalent plastic strain has been added to the result object, result reader and vtk post processing.

-   Extended Post Processing
    -   **VTK** An extended post processing based on [VTK](https://www.vtk.org/) has been added.
    -   **Clip filter** \...
    -   **Scalar clip filter** \...
    -   **Cut filter** \...
    -   **Wrap vector filter** \...
    -   **Linearized stresses** \...
    -   **Data at point** A tool to get the result data for a specific point.
    -   **Data along line** A tool to get the result data for a specific line printed as a diagram.

-   Fixes, code and other stuff
    -   The **unit tests suite** for FEM work bench has been extended.
    -   The **code basis** has been massively improved.
    -   Most of FEM code has been ported to **Python3**.
    -   Furthermore there have been **tons of bugs** found and fixed.
    -   All **icons** have been nicely redrawn and in conjunction with guidelines.
    -   **Code formating** There should be no more tabs and white spaces in all FEM source code.
    -   Python code complies with most rules of **flake8**.
    -   Dozens of **typos** inside source code have been fixed (AFAIK this applies to all FreeCAD, luzpaz finds all of them like finding a needle in the haystack).

-   Some Pictures

<img alt="" src=images/bridge-all.png  style="width:640px;"> <img alt="" src=images/bridge-detail.png  style="width:640px;">

## Arbeitsbereich Part {#arbeitsbereich_part}

-   Der Open Cascade geometrische CAD-Kernel wird jetzt in der Version von 6.8.0 auf 7.2.0 angehoben (die aktuelle OCC-Version kann von der Plattform/Distribution abhängen). Diese Version enthält viele Fehlerkorrekturen in den Boolesche Operationen, dem Algorithmus zur Entfernung von unsichtbaren Linien und erlaubt neue Feature, die dem Arbeitsbereich Part hinzugefügt wurden.

-   Neue Features: [Boolean Fragments](Part_BooleanFragments.md), [Slice](Part_Slice.md) und [XOR](Part_XOR.md).

-   Durch diese neuen Fähigkeiten können nun zusammengesetzte Volumenkörper (compsolids) in FreeCAD erstellt werden. Diese sind insbesondere in dem Arbeitsbereich FEM von großen Nutzen.

-   Die Leistung und Zuverlässigkeit von [Connect](Part_JoinConnect.md) wurden verbessert und das Werkzeug wurde vielseitiger.

-   Ein neues Feature: [2D Offset](Part_Offset2D.md), um ebene Kantenzüge zu versetzen.

-   Erweiterung: Das Werkzeug [Part Extrude](Part_Extrude/de.md) unterstützt nun eine parametrische Normalenrichtung mittels einer verlinkten Kante, Richtungsumkehr, 2te Länge, 2ten Abschrägungswinkel und Symmetrie. Die erstelle Volumenkörper-Option ist nun automatisch ausgewählt, wenn der Dialog geöffnet wird und eine geschlossene Kontur ausgewählt wurde.

-   Erweiterung: Das Werkzeug [Part Revolve](Part_Revolve/de.md) unterstützt nun eine parametrische Verbindung zur Rotationsachse (eigentlich in nur in PartDesign).

-   Die neue Hilfsfunktion [Part Attachment](Part_Attachment/de.md) verfügbar über das Menü *Part → Attachment...* kann benutzt werden, um die meisten Typen von Objekten miteinander parametrisch zu verbinden.

-   Der neue [Part-Container](Std_Part/de.md) kann verwendet werden um die meisten Typen von [Shapes](Glossary/de#Shape.md) zu gruppieren und sie als Einheit zu bewegen. Er enthält auch die Standardebenen und -achsen, an denen ebenfalls Objekte angeheftet werden können. Er wird die Basis für den zukünftigen Arbeitsbereich Assembly bilden, um eine Möglichkeit zu haben, Baugruppen im Raum zu bewegen. Er steht in allen Arbeitsbereichen zusammen mit [Group](Std_Group/de.md) in der Werkzeugleiste zur Verfügung.

## Arbeitsbereich PartDesign {#arbeitsbereich_partdesign}

Der Arbeitsbereich PartDesign erlebte massive Änderungen, die Frucht der gemeinsamen Anstrengungen von einer Vielzahl von Entwicklern über einen Zeitraum von 5 Jahren. <img alt="" src=images/PartDesign017-teaser-motor-core.png  style="width:800px;">

-   Der neue Container [Body](PartDesign_Body/de.md) nimmt eine Kette von PartDesign-Features auf, die einen einzelnen zusammenhängenden Volumenkörper bilden. Er enthält auch die Standardebenen und -achsen, an denen ebenfalls Objekte angeheftet werden können. Dank des Body-Containers ist es nun nicht länger notwendig, die Skizzen an Flächen zu heften, wenn neue Formelemente hinzugefügt werden sollen. Diese Notwendigkeit war lange eine große Limitierung des alten PartDesign, die in vielen Fällen das Versagen der Modelle bei Parameteränderungen verursacht hat. Daher wird jetzt empfohlen, das Zuordnen von Skizzen zu Flächen zu vermeiden, soweit dies möglich ist.

-   Neue additive und subtraktive Formelemente: [Grundkörper](PartDesign_CompPrimitiveAdditive/de.md), [Ausformung](PartDesign_AdditiveLoft/de.md), [Austragung](PartDesign_AdditivePipe/de.md), [Thickness](PartDesign_Thickness/de.md).

-   Neue Bezugselemente wie [Bezugsebene](PartDesign_Plane/de.md), [Bezugslinie](PartDesign_Line/de.md) und [Bezugspunkt](PartDesign_Point/de.md), die für die Platzierung und Ausrichtung von Skizzen und als Drehachsen für Drehelemente dienen können.

-   Neue automatische Umschaltung zwischen den Arbeitsbereichen PartDesign und Sketcher. Wenn eine neue Skizze innerhalb des Arbeitsbereiches PartDesign erstellt wird, schaltet die Benutzeroberfläche auf den Arbeitsbereich Skizze in den Editiermodus um, sobald die Ausrichtung der Skizze definiert wurde. Wenn die Skizze geschlossen wird, schaltet die Benutzeroberfläche zurück in den Arbeitsbereich PartDesign und stellt die vorherige Ansicht wieder her. Folglich wurden die Werkzeuge des Sketchers aus der Werkzeugleiste von PartDesign entfernt, um Platz zu schaffen für die neuen PartDesign Features.

## Arbeitsbereich Path {#arbeitsbereich_path}

Der Arbeitsbereich Path wurde massiv überarbeitet in der Version 0.17. Die Überarbeitung resultierte in der Entfernung des alten Codes von HeeksCNC und den Ersatz der Python-Bibliothek für den Zugriff auf die Bibliothek libarea mit dem neuen Path-Area-Modul. Das Ergebnis war, dass die Operationen weit leistungsfähiger und schneller wurden mit einer deutlich vereinfachten Code-Basis.

-   Die Unterstützung für 2.5D Operationen ist komplett einschließlich [contour](Path_Contour.md), [face-milling](Path_MillFace.md), [pocketing](Path_Pocket_Shape.md), [profiling](Path_ProfileFace.md) und [drilling](Path_Drilling.md)

-   Es gibt eine eingeschränkte Unterstützung für [3D pocketing](Path_Pocket_3D.md) Operationen.

-   In Path kann das Werkzeug [Arch Panel](Arch_Panel.md) als ein Basisobjekt benutzt werden, um mehrere Teile zusammen zu gruppen, um sie zusammen aus einer Platte auszuschneiden.

-   Einführung von [Path Job](Path_Job.md). Der Job ist nun das zentrale Objekt der Arbeitsweise von Path. Er organisiert und koordiniert verschiedene Operationen, Werkzeuge, Grundmaterial, Orientierung und Ausrichtung der Teile. Ein individuell angepasster Job kann als \'Job Vorlage\' gespeichert und wiederverwendet werden, um das Einrichten zukünftiger Jobs zu vereinfachen. Job SetupSheets stellen einen Mechanismus zur Verfügung um die Konfiguration von Tiefen- und Geschwindigkeitseinstellungen zu automatisieren.

-   Alle Operationen haben eine konsistente Organisation über das Task-Panel.

-   Neue oder verbesserte [post-processors](Path_Post.md) für LinuxCNC, Smoothieboard, GRBL, Phillips, OpenSBP (shopbot), Roland Modela, Centroid, Fablin, und Dynapath. Die meisten Post-Prozessoren unterstützen Argumente.

-   Verbesserte [Werkzeugbibliothek](Path_ToolLibraryEdit.md) und -editor.

-   Das Werkzeug [Path Inspect](Path_Inspect.md) erlaubt das Hervorheben von individuellen Kommandos, um den Pfad zu visualisieren und den Gcode zu untersuchen.

-   Das Werkzeug [Path Simulator](Path_Simulator.md) simuliert in 3D das Schneiden, um die Ausführung von Path zu veranschaulichen.

-   Dress-up Operationen können zum Verfeinern der Kernoperationen und für zusätzliche Komplexität verwendet werden. Dressups existieren für [\'dogbone\'](Path_DressupDogbone.md) Ecken, [holding tags](Path_DressupTag.md), [ramp entry](Path_DressupRampEntry.md), und [dragknife](Path_DressupDragKnife.md) \'corner actions\'

## Arbeitsbereich Sketcher {#arbeitsbereich_sketcher}

-   Skizzen können nun in vielfältiger Weise zugeordnet werden, nicht nur an flachen Flächen, wie es zurvor üblich war. Von besonderer Bedeutung ist das Ausrichten normal zu Kanten, das für das Erstellen von Profilen mit [sweeping](Part_Sweep/de.md) sehr hilfreich ist.

-   Externe Geometrie verlinkt nicht mehr nur zu dem Objekt, dem die Skizze zugeordnet ist. Geometrie von anderen Skizzen wird ebenfalls unterstützt. Links zu externer Geometrie können innerhalb eines Part-Containers oder eines Body-Containers oder selbst in dem ganzen Projekt, wenn Part- und Body-Container nicht verwendet werden, erstellt werden.

-   Automatische Sichtbarkeit: wenn man jetzt beginnt eine Skizze zu bearbeiten, werden von der Skizze abhängige Objekte automatisch ausgeblendet um freie Sicht zu haben, und Objekte eingeblendet, die für externe Geometrie verwendet wurden; die vorherige Sichtbarkeit wird beim Schließen der Skizze wieder hergestellt.

-   Neuer kontinuierlicher Erstellungsmodus für Beschränkungen (constraints): Die Beschränkungswerkzeuge sind jetzt immer aktiv, selbst wenn kein Element ausgewählt wurde. Klicke auf eine Beschränkung und wähle dann die Objekte aus, auf die die Beschränkung angewemdet werden soll.

-   Neue Werkzeuge zur Erstellung von Hyperbeln und Parabeln.

-   Neues erweitertes Kantenbearbeitungswerkzeug.

-   Neues Werkzeug zur Erstellung von B-Splines, mit vielen Möglichkeiten die Kurve zu beeinflussen (Grad, Knoten Multiplizität, Gewichtung der Kontrolpunkte) und die Information anzuzeigen (Kontrolpolygon, Kurvenkamm, Knoten- Multiplizitätsanzeige).

![](images/FC017_Sketcher_B-spline_01.png )

-   Ein neues Werkzeug **Carbon Copy** um Geometrie von einer Skizze zu einer anderen zu kopieren.

-   Virtual space schaltet alle Beschränkungen auf einen anderen \"virtual space\" mit dem Effekt sie außer Sicht bringen.

-   Die Beschränkungslistenansicht hat nun die Fähigkeit die interne Ausrichtung auszublenden sowie das individuelle Ausblenden von Beschränkungen mit einem Auswahlkästchen.

-   Die Blockbeschränkung entfernt alle Freiheitsgrade für ein geometrisches Element auf seinem Platz mit einer einzigen Beschränkung. Dies ist besonders brauchbar für die Arbeit mit B-Splines, die umständlich zu beschränken sind.

-   Ein neues reguläres Polygon mit einer vom Benutzer definierten Anzahl von Seiten.

-   Alternative Löser für Skizzen sind erreichbar über *Zeige die erweiterte Solver-Steuerung in der Taskleiste* in den Sketcher Einstellungen.

-   Ein Rendern abhängig von der Art der Geometrie erlaubt das Umstellen der Reihenfolge zwischen normaler, Konstruktions- und externer Geometrie. Nützlich falls diese Arten von Geometrie sich überlappen.

-   Der Solver ersetzt nun automatisch eine Kombination der Beschränkungen *Koinzidenz erzwingen* + *Tangente setzen* mit einer Beschänkung *Punkt-auf-Punkt Tangente setzen*, da die erste Variante so nicht vorgesehen ist und Toleranzfehler bewirken kann, die zu Folgefehlern im Modell führen können. Der Benutzer wird auf die Ersetzung durch einen Dialog hingewiesen, der in den Einstellungen für den Sketcher unter dem Punkt \"Automatisch beim Ersatz einer Beschränkung benachrichtigen\" abgewählt werden kann.

-   Neues Häckchenfeld in der Task-ansicht im Bearbeitungsmodus \"Avoid redundant auto constraints\"?

-   Horizontale und vertikale Beschränkungen können benutzt werden, um ausgewählte Punkte auszurichten.

## Arbeitsbereich Spreadsheet {#arbeitsbereich_spreadsheet}

-   Ein Importfilter für Excel-Dateien wurde hinzugefügt.

## Arbeitsbereich Surface {#arbeitsbereich_surface}

-   Ein neuer Arbeitsbereich in v0.17, aktuell stehen in dem Arbeitsbereich Surface vier Funktionen für die Erstellung von Oberflächen zur Verfügung.

## Arbeitsbereich TechDraw {#arbeitsbereich_techdraw}


<div class="mw-translate-fuzzy">

[TechDraw](TechDraw_Workbench.md) ist ein neuer Arbeitsbereich zur Erstellung von technischen Zeichnungen, der antritt den veralteten Arbeitsbereich Drawing zu ersetzen. FreeCAD v0.17 wird immer noch mit dem Arbeitsbereich Drawing ausgeliefert, so dass es noch möglich ist, die Dokumente, die Drawing-Seiten enthalten, zu öffnen und zu editieren, aber Drawing wird in zukünftigen Versionen auslaufen. Einige der aufregenden neuen Sachen aus TechDraw:


</div>

-   Die meisten Werkzeuge des Arbeitsbereichs Drawing haben ein Gegenstück im Arbeitsbereich TechDraw.
-   Leichter Erstellung von Ansichten und deren Bearbeitung. Ansichten können an ihren Rahmen mit der Maus gefasst werden und auf der Seite verschoben werden. Die Ausrichtung der orthogonalen Ansichten kann festgelegt werden.
-   Besseres Linientypenmanagement (hart, gerundet, iso, Naht). Besseres Entfernen der verdeckten Linien dank der neuen [OCC](Glossary/de#OCC.md) Bibliothek.
-   Schnittansicht, Erstellung von Detailansichten.
-   Besseres Vorlagenmanagement.
-   Das Bemaßen wird nun mit mehreren Bemaßungswerkzeugen unterstützt: horizontal, vertikal, Länge, Radius, Durchmesser, Winkel.
-   Gestaltungswerkzeuge: Schraffur, Schraffur kompatibel zur Autodesk PAT Specifikation, Symbole, Bilder.

## Zussätzliche Module {#zussätzliche_module}

Einige der neuen Module, die von der FreeCAD-Gemeinschaft geschaffen wurden.

-   [Manipulator Workbench](Manipulator_Workbench.md) is aimed to help in Aligning, Moving, Rotating and Measuring 3D objects (Part Design allowed) through a friendly GUI.

-   [Curves](https://github.com/tomate44/CurvesWB), eine Sammlung von Werkzeugen, um \[<https://de.wikipedia.org/wiki/Non-Uniform_Rational_B-Spline%5D-Kurven> und -Oberflächen zu erstellen und zu bearbeiten.

-   [Nurbs](https://github.com/microelly2/freecad-nurbs), Eine Sammlung von Scripten zum Bearbeiten von Freiformoberflächen und -kurven.

-   [Silk](https://github.com/edwardvmills/Silk), eine Sammlung von Werkzeugen zur Bearbeitung von NURBS-Oberflächen mit dem Fokus auf niedrigen Grad und Nahtkontinuität.

-   [Flamingo Workbench](Flamingo_Workbench.md), a set of customized FreeCAD commands and objects that help to speed-up the drawing of frames and pipelines.

-   [Civil Engineering/Transportation Workbench](Civil_Engineering_Workbench.md)

-   [GDT](https://github.com/juanvanyo/FreeCAD-GDT), geometrische Bemaßung und Tolerierung (GD&T).

-   [InventorLoader](https://github.com/jmplonka/InventorLoader) Importfilter für Autodesk Inventor-Dateien (in Arbeit).

-   [Kicad StepUp Workbench](https://www.freecadweb.org/wiki/KicadStepUp_Workbench) is aimed to help KiCad and FreeCAD users in ECAD and MCAD collaboration.

[Category:News{{\#translation:}}](Category:News.md) [Category:Documentation{{\#translation:}}](Category:Documentation.md) [Category:Releases{{\#translation:}}](Category:Releases.md)
