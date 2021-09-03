 {{UnfinishedDocu}}





{{TOCright}}

## Zweck


<div class="mw-translate-fuzzy">

Auf dieser Seite werden die strategischen Ziele für den Pfad Arbeitsbereich diskutiert. Dies soll keine Liste von zu implementierenden Funktionen sein, sondern umfassendere Ziele, die die allgemeine Richtung der Pfad Entwicklung lenken.


</div>

## Kernziele

Diese Dinge machen Pfad zu einem zuverlässigen, leistungsfähigen und flexiblen Werkzeug. Die Arbeit in diesem Bereich ist nie endend und hat immer hohe Priorität. Neue Entwickler sollten in Betracht ziehen, hier zu helfen, bevor sie neue Funktionen entwickeln.

-   Breite Testabdeckung
-   TROCKEN und gut dokumentierte Codebasis
-   Fehlerkorrekturen
-   Unterstützung für viele CNC Maschinen (Postprozessoren)

## Arbeitsablauf

Das Ziel ist offensichtlich ein Arbeitsablauf, der effizient ist und keine menschlichen Fehler zulässt. Der spezifische Arbeitsablauf kann jedoch je nach Art der Maschine, mit der der Benutzer arbeitet, und der Art der Geometrie, an der er arbeitet, variieren.

### Auftragsarten

Pfad ist für das 2,5D Fräsen optimiert. Es braucht das Konzept der Auftrag \'Arten\', um andere Arten von Arbeitsabläufen wie Drehbank, 4. Achse und reine 2D Maschinen zu behandeln. Zusätzliche Auftragsarten würden dazu beitragen, die Auswahlmöglichkeiten des Benutzers einzugrenzen und das visuelle Rauschen und die Verwirrung zu beseitigen, die durch Optionen entstehen, die nicht auf die gewünschte Aufgabe zutreffen.

### 2D Arbeitsablauf {#d_arbeitsablauf}

2D Arbeitsabläufe wie Laser/Wasserstrahl/Plasma haben einige besondere Anforderungen.

-   Schachtelung von Teilen in geschnittenen Blechen
-   Markierung für Teile ID, Falzlinien, Nähte, usw.
-   Effizienter Import aus DXF

Zusätzliche 2D Strategien

-   Gravieren - Gravieren, durch Folgen eines Satzes von 2D Kanten. Wir unterstützen dies jetzt teilweise, aber der Arbeitsablauf ist grob und die Ausrichtung der 2D Elemente an der Form ist fast unmöglich.
-   V-Carve - Gravieren, durch Folgen der Mittellinie zwischen den Kanten und dabei kontrollieren der Z Tiefe.
-   Schraffurfüllen - Füllen einer beliebigen Begrenzung mit einem Schraffurmuster

### Arbeitsablauf Drehmaschine {#arbeitsablauf_drehmaschine}

Die Drehmaschineneinrichtung unterscheidet sich vom Fräsen. Der Benutzer sieht das Koordinatensystem im Allgemeinen so, dass die Z Achse nach rechts und die X Achse in Richtung des Benutzers zeigt. Die Werkzeugpfade werden als 2D relativ zu einer Seite des Werkstücks oder relativ zum Ende für Plandrehoperationen betrachtet.

Drehbearbeitung

-   Zentrierbohren
-   Konturschruppen - Material abtragen, um zu approximieren
-   Konturschlichten - Konturschlichtdurchgang
-   Plandrehen
-   Aufbohren
-   Gewindeschneiden Außen
-   Gewindeschneiden Innen

### 4/5 Achsen Arbeitsablauf {#achsen_arbeitsablauf}

Kontinuierliche 4. Achsen Bearbeitungen können die 4. drehen, während der Fräser eingreift. Bei dieser Art von Bearbeitungen muss der Werkzeugpfad relativ zum Werkstück visualisiert werden. Bei anderen Bearbeitungen wird die 4. Achse verwendet, um das Werkstück in eine bestimmte Richtung zu drehen und dann eine reine 2,5D Bearbeitung des Werkstücks durchzuführen. Hier handelt es sich eher um mehrere Aufspannungen und die Visualisierung muss unter Umständen für jeden einzelnen Schritt berücksichtigt werden.

### 2.5D (Fräs) Arbeitsablauf {#d_fräs_arbeitsablauf}

Dies ist das stärkste Feld von Pfad. Aber es gibt noch Raum für Verbesserungen.

Zusätzliche Strategien

-   Gewindeschneiden
-   Bohren - Geradliniges Bohren Dosenbetrieb (G85/G89)
-   Schlitzsäge - Schlitzschneiden mit Sägewerkzeug an der Seite des Werkstücks

### 3D Oberflächenfräsen {#d_oberflächenfräsen}

Additional strategies

-   Constant scallop
-   Pencil

### Mehrprogramm Kontext {#mehrprogramm_kontext}

Some parts require multiple setups to complete. Each setup is represented by a separate job but no structure links them together other than the top-level document. This is insufficient because the document may contain multiple parts that have completely independent manufacturing steps/jobs/setups.

Commercial CNC users usually produce a document called a [\'setup sheet\'](https://www.cnccookbook.com/art-setup-sheet/) which describes to the CNC operator how to set up the machine in order to manufacture the part. This \'setup sheet\' is not at all related to the Path setupsheet concept. It is a human-readable document meant to communicate assumptions and notes required to correctly execute the gcode. The setup sheet usually contains the following information:

-   tools required
-   lowest z level
-   Part name/number/version
-   customer
-   rough stock or starting condition
-   operations
-   estimated run time
-   critical dimensions and inspection criteria
-   notes about previous runs
-   gcode program name
-   Fixtures and workholding information

## Bibliotheken Niedriger Stufe {#bibliotheken_niedriger_stufe}


<div class="mw-translate-fuzzy">

Pfad verwendet mehrere Bibliotheken, um Werkzeugpfade basierend auf der Teilegeometrie zu erzeugen. Dazu gehören libarea/patharea/clipper, OCC und OpenCamLib. Weitere Bibliotheken sind verfügbar und es werden wahrscheinlich in Zukunft noch mehr geschrieben werden. Wir sollten diese einbeziehen, wann immer es möglich ist und wenn eine native (OCC) Lösung nicht verfügbar ist.


</div>


<div class="mw-translate-fuzzy">

Openvoronoi ist eine Bibliothek, die verfügbar und lizenzkompatibel ist. Zurzeit wird sie nicht für Python3 gebaut und ist nicht für die Verteilung mit FreeCAD gepackt. Die Bereitstellung von Openvoronoi würde den V-Carving Betrieb und möglicherweise einige andere interessante Werkzeugpfade ermöglichen.


</div>

[Deepnest](https://github.com/Jack000/Deepnest) or an equivalent nesting/bin packing library would allow us to efficiently arrange parts in a cut-sheet to minimize stock usage.

## Pfadänderungen

Some of the operations/strategies offer features and tools that are useful but not available for other op/strategies. We should work to make things more consistent.

Pocket/3D Pocket has a boundary extension tool. This should be available to all operations where it makes sense. For example adaptive, surface, waterline,

## Darstellung des restlichen Materials {#darstellung_des_restlichen_materials}

Path should have a more robust state for the remaining material. This would be useful for visualization, collision avoidance, and REST milling.

## Post Processing & Advanced Gcode {#post_processing_advanced_gcode}

-   Post to git

Gcode for the hobbyist is transient. It\'s used once and then likely not retained. If the user needs it again, they simply re-post the original file. For commercial users under certain certification standards, the gcode is a long-term asset and often may require version control protection. Integrating version control directly into the post-processing workflow might be an interesting feature.

-   modular output for older machines with limited memory.

Many old machines have an extremely limited capacity for gcode. While physically able to produce more complex paths, the very large output from surfacing and adaptive toolpaths make them unusable. It would be useful to post-process the output with an eye on the size of the resulting file. As a file reaches a maximum size, the post-processor could insert a spindle retraction and stop gracefully, then the next file could continue. Output files would be numbered to indicate sequence.

-   Support for Macros, subprograms, variables.

## Pfadanalyse

-   Tip up Prediction / avoidance

When 2D cutting (laser/waterjet/plasma) of material supported on a grating, small parts cut out of the main stock can \'tip up\' creating a crash hazard for the cutting tool during subsequent moves. Being able to predict these events or avoid them by ordering paths would be desirable. ([Further reading](https://shopfloorlasers.com/nesting-software/263-heads-up))

-   Visualization of remaining material after each operation could be improved

## Liste der Defizite {#liste_der_defizite}

The following list is not individual bugs but shows how Path is inconsistent in its application of concepts.

-   Inconsistent use of cut direction. We should be talking about climb/conventional everywhere and not using language like CW/CCW.
-   Inconsistent use of stepover. I wish we had used the terminology of DOC/WOC (depth of cut / width of cut) from the beginning but we didn\'t. We use \'stepdown\' and \'stepover\' but inconsistently apply it. Sometimes it is an absolute value and other times a percent of cutter diameter.
-   Inconsistent implementation of the ObjectOp class hierarchy. Some of the ops can\'t be toggled off.
-   Finishing Passes. I think we should add an additional ObjectOp.Feature for FeatureFinishPass. This would give a new tab where a user could configure the final finishing pass with a different tool controller, direction, etc.
-   Inconsistent control of performance vs. accuracy. Many operations have poorly named or inconsistent controls for tolerance. At a minimum these could be grouped into a consistently named property group.
-   Inconsistent use of stock shapes and extensions.
-   No high level path optimization / automatic grouping of disjunct cutting areas.





{{Path_Tools_navi

}} 
