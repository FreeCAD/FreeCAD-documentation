# Feature editing/de
{{TOCright}}

## Einführung

Diese Seite erklärt, die Art und Weise wie der <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) für den Einsatz ab FreeCAD 0.17 vorgesehen ist.

Während der <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> _ **[Formelemente](PartDesign_Feature/de.md)**. Ein [Formelement](https://en.wikipedia.org/wiki/Feature_recognition) ist ein Vorgang, die die Form eines Modells verändert.

## Formelement Bearbeitungsmethodik 

Das erste Formelement wird allgemein als **Basisformelement** bezeichnet. Wenn dem Modell weitere Formelemente hinzugefügt werden, nimmt jedes Formelement die Form des vorherigen an und fügt Inhalte hinzu oder entfernt sie, wodurch lineare Abhängigkeiten von einem Formelement zum nächsten entstehen. In der Tat imitiert diese Methodik einen gemeinsamen Herstellungsprozess: Ein Block wird auf der einen Seite geschnitten, dann auf der anderen Seite, werden Löcher hinzugefügt, dann Rundungen, usw.

Alle Formelemente werden sequentiell im Modellbaum aufgelistet und können jederzeit bearbeitet werden, wobei das letzte Formelement am unteren Rand das letzte Teil darstellt.

Formelemente können in verschiedene Kategorien eingeteilt werden:

-   *Profil-basiert*\': Diese Formelement gehen von einem Profil aus, um die Form der hinzuzufügenden oder zu entfernenden Gegenstände zu definieren. Das Profil kann eine Skizze, eine ebene Fläche auf vorhandener Geometrie (ein Profil wird aus seinen Kanten extrahiert), ein FormBinder oder ein Entwurfsobjekt sein, das in den aktiven Körper aufgenommen wurde.

-   **Additiv**: fügt dem bestehenden Modell Substanz hinzu. Additive Formelemente zeigen gelbe Symbole.

-   **Subtraktiv**: entfernt Substanz aus dem bestehenden Modell. Subtraktive Formelemente zeigen rote und blaue Symbole.

-   **Grundkörper-basiert**: basiert auf geometrischen Grundkörpern (Würfel, Zylinder, Kegel, Torus\....). Sie können additiv oder subtraktiv sein.

-   Transformations Formelemente\'\'\'\'\': sie wenden eine Transformation auf bestehende Formelemente an (gespiegelt, lineares Muster, polares Muster, Mehrfachtransformation).

-   **Verschönerung**: Formelemente, die eine Behandlung auf Kanten oder Flächen anwenden, wie z.B. Verrundungen, Fasen und Entwürfe.

-   **Verfahrensorientiert**: kann man von Formelementen sprechen, die nicht auf Skizzen basieren, wie die Transformations- und Verschönerungsformelemente.

## Körper

Die Arbeit in PartDesign erfordert zunächst das Erstellen eines <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[Körper](PartDesign_Body/de.md)**. Der PartDesign Körper ist ein Behälter, der eine Folge von Formelementen gruppiert, die einen einzigen zusammenhängenden Volumenkörper bilden.

![](images/PartDesign_Body_tree.png )

**Was ist ein einzelner zusammenhängender Festkörper?** Es handelt sich um einen Gegenstand wie ein Gussstück oder etwas, das aus einem einzigen Metallblock bearbeitet wurde. Wenn das Objekt Nägel, Schrauben, Kleben oder Schweißen beinhaltet, ist es kein einzelner zusammenhängenden Volumenkörper. Als praktisches Beispiel würde ein Holzstuhl aus mehreren Körpern gemacht, mit einem für jede seiner Unterkomponenten (Beine, Latten, Sitz usw.).

Mehrere Körper können in einem FreeCAD Dokument erstellt werden; sie können auch zu einem einzigen zusammenhängenden Festkörper kombiniert werden.

In einem Dokument kann nur ein Körper aktiv sein. Der aktive Körper erhält die neu erstellten Formelemente. Ein Körper kann durch Doppelklick aktiviert oder deaktiviert werden. Ein aktivierter Körper wird hellblau hervorgehoben. Die Hervorhebungsfarbe kann in den Einstellungen unter Anzeige/Farben/Aktiv Container ab Version 0.18 eingestellt werden.

Wenn ein Modell mehrere Körper benötigt, wie im vorherigen Beispiel eines Holzstuhls, der Allzweck <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Part Behälter](Std_Part/de.md) kann verwendet werden um sie zu gruppieren und das Ganze als Einheit zu bewegen.

### Körpersichtbarkeitsverwaltung

Ein Body präsentiert standardmäßig sein neuestes Formelemente nach außen. Diese Funktion ist standardmäßig als die Spitze definiert. Eine gute Analogie ist der Ausdruck*die Spitze des Eisbergs*: Nur die Spitze ist über dem Wasser sichtbar, der größte Teil der Masse des Eisbergs (die anderen Formelemente) ist verborgen. Wenn dem Körper ein neues Formelement hinzugefügt wird, wird die Sichtbarkeit des vorherigen Formelements deaktiviert, und das neue Formelement wird zur Spitze.

Es kann immer nur ein Formelement gleichzeitig sichtbar sein. Es ist möglich, die

[Umschalten der Sichtbarkeit](Std_ToggleVisibility/de.md) eines beliebigen Formelements im Körper umzuschalten, indem man es im Modellbaum markiert und die **Leertaste** drückt, wodurch man in die Verlaufsgeschichte des Körpers zurückkehrt.

### Körperursprung

Der Körper hat einen Ursprung, der aus Bezugsebenen (XY, XZ, YZ) und Achsen (X, Y, Z) besteht, die von Skizzen und Formelementen verwendet werden können. Skizzen können an Ursprungsebenen angehängt werden, und sie müssen nicht mehr auf ebene Flächen abgebildet werden, damit darauf basierende Formelementen hinzugefügt oder vom Modell abgezogen werden können.

### Objekte verschieben und neu ordnen 

Es ist möglich, die Spitze eines Formelementes in der Mitte des Körperbaums vorübergehend neu zu definieren, um neue Objekte (Formelemente, Skizzen oder Bezugsgeometrie) einzufügen. Es ist auch möglich, Formelemente unter einem Körper neu zu ordnen oder sie in einen anderen Körper zu verschieben. Wähle das Objekt aus und rechtsklicke, um ein Kontextmenü zu sehen, das beide Optionen anbietet. Die Operation kann verhindert werden, wenn das Objekt Abhängigkeiten im Quellkörper aufweist, z.B. wenn es an einer Fläche befestigt ist. Um eine Skizze in einen anderen Körper zu verschieben, sollte sie keine Verknüpfungen zur externen Geometrie enthalten.

### Unterschied zu anderen CAD Systemen 

Ein grundlegender Unterschied zwischen FreeCAD und anderen Programmen, wie Catia, besteht darin, dass FreeCAD es Ihnen nicht erlaubt, viele nicht verbundene Festkörper in einem einzigen <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> \'\'\'[Konstruktionskörper](PartDesign_Body/de.md) zu haben. Das heißt, ein neues Formelement sollte immer auf dem vorherigen aufbauen. Oder anders ausgedrückt, das neuere Formelement sollte das vorherige Formelement \"berühren\", so dass beide Formelement miteinander verschmolzen werden und zu einem einzigen Festkörper werden. Du kannst keine \"schwebenden\" Festkörper haben.

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">


*Unterschied zwischen Catia und FreeCAD. Links: Catia erlaubt es, Körper von den vorherigen Formelementen des Körpers zu trennen. In FreeCAD verursacht dies einen Fehler; Rechts: das neuere Formelement sollte immer das vorherige Formelement berühren oder schneiden, so dass es mit ihm verschmolzen ist und zu einem einzelnen zusammenhängenden Festkörper wird.*

## Bezugsgeometrie

Die Bezugsgeometrie besteht aus benutzerdefinierten Ebenen, Linien, Punkten oder extern verknüpften Formen. Sie können zur Verwendung als Referenz für Skizzen und Formelementen erstellt werden. Es gibt eine Vielzahl von Befestigungsmöglichkeiten für Bezugsobjekte.

In einigen CAD Systemen kannst Du eine Bezugsebene definieren, die gegenüber dem vorherigen Körper versetzt ist, und Du kannst einen nicht verbundenen Körper erstellen. Das Platzieren vieler Bezugsebenen und das Erstellen von Objekten auf ihnen ist also in Ordnung und führt nicht zu einem Fehler. Typischerweise würdest Du die Ebenen schließlich an ihre Endpositionen anpassen, so dass die einzelnen Objekte miteinander verschmolzen werden.

In FreeCAD sind, wie im vorigen Abschnitt erwähnt, unverbundene Körper **NICHT** erlaubt, so dass eine Skizze auf einer Bezugsebene, die einen nicht zusammenhängende Körper erzeugen würde, fehlschlägt.

In FreeCAD sind Bezugsebenen sinnvoll, wenn du Skizzen (und Polsterungen, Taschen usw.) in nicht standardmäßigen Ausrichtungen platzierst, d.h. in Ebenen, die um die drei Hauptachsen versetzt oder gedreht sind. Da Skizzen auf die gleiche Weise wie Bezugsebenen auch in nicht standardmäßigen Ausrichtungen platziert werden können, ist es oft nicht notwendig, Bezugsebenen zu verwenden.

Bezugsebenen sind auch dann sinnvoll, wenn es mehr als eine Skizze in derselben nicht standardmäßigen Ausrichtung geben wird. In diesem Fall kann eine Bezugsebene verwendet werden, und die Ausrichtung muss nur für die Bezugsebene angepasst werden, um alle zugehörigen Skizzen und die aus den Skizzen erstellten Formelemente anzupassen.


<div class="mw-translate-fuzzy">

Sowohl Skizzen als auch Bezugsebenen sollten an den Basisebenen angebracht werden. Das Referenzieren erzeugter Geometrie (Geometrie, die das Ergebnis einer Formelement Erzeugungsoperation ist, z.B. ein Polster oder eine Tasche) sollte vermieden werden. (Siehe Ratschläge zum Erstellen stabiler Modelle weiter unten).


</div>

Auch wenn sie nicht zur Unterstützung von Skizzen verwendet werden, sind Bezugsobjekte als visuelle Indikatoren hilfreich, um auf wichtige Merkmale oder Abstände im Modellierungsprozess hinzuweisen. (Allerdings bietet auch das einfache Hinzufügen von Geometrie zu einer Skizze eine ähnliche visuelle Rückmeldung).

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">


*Unterschied zwischen Catia und FreeCAD. Links: Catia erlaubt es, Körper von den vorherigen Formelementen des Körpers zu trennen. In FreeCAD verursacht dies einen Fehler; Rechts: das neuere Formelement sollte immer das vorherige Formelement berühren oder schneiden, so dass es mit ihm verschmolzen ist und zu einem einzelnen zusammenhängenden Festkörper wird. In diesem Beispiel basiert der neue Festkörper auf einer Bezugsebene, die um die Y Achse gedreht wird.*

## Querverweise

Es ist möglich, Elemente aus einem Körper in einem anderen Körper über Bezugspunkte zu referenzieren. Zum Beispiel erlaubt der Bezugspunkt Form Binder, Flächen aus einem Körper als Referenz in einen anderen Körper zu kopieren. Auf diese Weise sollte es leicht möglich sein, einen Kasten mit passendem Deckel in zwei verschiedenen Körpern zu bauen. FreeCAD hilft dir zu verhindern, versehentlich auf andere Körper zu verweisen, indem es deine Bestätigung bei deiner Absicht abfragt.

## Anhängen

Das Anhängen von Objekten ist kein besonderes PartDesign Werkzeug, sondern vielmehr ein in v0.17 eingeführtes Teil Dienstprogramm, das im Part Menü zu finden ist. Es wird im PartDesign Arbeitsbereich häufig verwendet, um Skizzen und Referenzgeometrie an die Standardebenen und -achsen des Körpers anzuhängen. Es stehen sehr umfangreiche Möglichkeiten zum Erstellen von Bezugspunkten, -linien und -ebenen zur Verfügung. Optionale Parameter für den Anhängungsversatz machen dieses Werkzeug sehr vielseitig.

Weitere Information findet man auf der [Anhang](Part_EditAttachment/de.md)-Seite und dem [Basic Attachment Tutorial](Basic_Attachment_Tutorial/de.md).

## Ratschläge zur Erstellung stabiler Modelle 

Die Idee der parametrischen Modellierung beinhaltet, dass du die Werte bestimmter Parameter ändern kannst und die nachfolgenden Schritte entsprechend den neuen Werten geändert werden. Bei schwerwiegenden Änderungen kann das Modell jedoch aufgrund des in FreeCAD noch ungelösten [topologischen Namensproblems](topological_naming_problem/de.md) brechen. Der Bruch kann minimiert werden, wenn du die folgenden Konstruktionsprinzipien einhältst:


<div class="mw-translate-fuzzy">

-   Vermeide das Anhängen von Skizzen und Bezugspunkten an die generierte Geometrie des Modells. (Generierte Geometrie ist jede Fläche oder Kante, die als Ergebnis eines Polsters, einer Tasche usw. erzeugt wird)
-   Platziere deine Skizzen auf Standardebenen oder auf benutzerdefinierten Bezugsebenen.
    -   Skizzen mit Anbringungsversätzen oder an Bezugsebenen mit Anbringungsversätzen angehängt, sind weniger gefährdet, unerwartet an eine andere Referenz angehängt zu werden.
-   Wenn Bezugspunktgeometrie erstellt wird, hänge sie nicht an die generierte Geometrie an.
    -   Befestige es an Standardebenen/-achsen und/oder Skizzen und verwende Befestigungsversätze, um es nach Bedarf zu positionieren.
-   Verwende eine \"Meisterskizze\".
    -   Eine Meisterskizze sollte so einfach wie möglich sein und grundlegende geometrische Elemente deines Modells enthalten.
    -   Elemente der Meisterskizze können bei der Modellierung nachfolgender Formelemente referenziert werden.
    -   Eine Meisterskizze kann die erste Skizze im Körper oder außerhalb des Körpers sein.
    -   Eine Meisterskizze kann als externe Geometrie oder über einen FormBinder referenziert werden.
-   FormBinder nicht aus generierter Geometrie erzeugen
-   Denke daran, dass FormBinder ein Problem darstellen können, wenn Geometrie aus der Skizze, auf der sie basiert, gelöscht wird.
-   Wenn du zwangsläufig ein Zwischenformelement referenzieren musst, z.B. das Ergebnis einer Dickenbearbeitung
    -   Verwende die erste mögliche Referenz in der Liste der nachfolgenden Formelemente, wo das referenzierte geometrische Element vorkommt.
    -   Ab FreeCAD 0.17 musst du das neueste Formelement nicht mehr verwenden.
    -   Wenn du ein frühes Formelement als Referenz verwendest, werden alle Änderungen an Zwischenschritten dein Modell nicht zerstören.
    -   Versuche, eine Skizze oder Skizzengeometrie zu referenzieren, anstatt generierte Geometrie zu verwenden.
-   Beachte, dass die Verwendung von Tabellenkalkulationen, dynamischen Daten, Meisterskizzen usw. im Allgemeinen zu mehr parametrischen Modellen führt und dazu beiträgt, das Problem der topologischen Benennung zu vermeiden.


</div>

## Körperbau Arbeitsablauf 

Es gibt mehrere Arbeitsabläufe, die mit der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) möglich sind. Was immer zu beachten ist, ist, dass alle in einem [PartDesign Körper](PartDesign_Body/de.md) erstellten Formelemente miteinander verschmolzen werden, um das endgültige Objekt zu erhalten.

### Verschiedene Skizzen 

Skizzen müssen von einer Ebene unterstützt werden. Diese Ebene kann eine der Hauptebenen (XY, XZ oder YZ) sein, die durch den Ursprung des Körpers definiert sind. Eine Skizze wird entweder mit einem Werkzeug wie <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _ ausgeformt. Der erste fügt der endgültigen Form des Körpers Volumen hinzu, während der zweite das Volumen aus der endgültigen Form schneidet. Auf diese Weise können beliebig viele Skizzen und Teilkörper erzeugt werden; die endgültige Form (Spitze) ergibt sich aus der Verschmelzung dieser Vorgänge. Natürlich kann der Körper nicht nur aus subtraktiven Operationen bestehen, da die endgültige Form ein Körper mit einem Volumen größer Null sein sollte.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Fortlaufende Merkmale 

Skizzen können an Flächen früherer Festkörperoperationen befestigt werden. Dies kann notwendig sein, wenn man auf eine Fläche zugreifen muss, die erst nach der Erstellung eines bestimmten Merkmals verfügbar ist. Dieser Arbeitsablauf ist jedoch nicht besonders empfehlenswert, da bei einer Änderung des ursprünglichen Merkmals die folgenden Merkmale in der Sequenz ungültig werden können. Siehe [Topologisches Benennungsproblem](topological_naming_problem/de.md).

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Verwendung von Bezugsebenen zur Unterstützung 


<div class="mw-translate-fuzzy">

Bezugsebenen sind nützlich, um die Skizzen zu unterstützen. Diese Hilfsebenen können auf dem Ursprung des Körpers basieren oder auf den Merkmalen (Kanten, Flächen) von zuvor erstellten Festkörpern. Darüber hinaus kann ein <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [PartDesign ShapeBinder/de](PartDesign_ShapeBinder/de.md) verwendet werden, um externe Geometrie in den Körper zu importieren, die als Referenz dient; dann können Skizzen an diesen Hilfskörper angehängt werden, entweder mit oder ohne Bezugsebene. Die Verwendung von Bezugsobjekten ist oft der beste Weg, um stabile Modelle zu erstellen, obwohl sie vom Benutzer etwas mehr Arbeit erfordert.


</div>

\'\'Note: In many cases, a sketch attached to a base plane with attachment offsets can accomplish the same function. Datums are particularly useful when multiple sketches or other constructs will use the datum. This means all changes to the datum will be apply to attached sketches, etc. Adding a single sketch to a datum, rather than using attachment offsets in the sketch properties, is an extra step and is essentially redundant. \'\'

As with sketches, it is possible to attach Datum planes to generated geometry (edges, faces of previously created solids), ***but this is not recommended*** since it can cause the topological naming problem.

In addition, a <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) can be used to import external geometry into the body to serve as reference; then sketches can be attached to this auxiliary body, either using datum planes or not.

*Again, the ShapeBinder should be based on Sketches from the previous body, not generated geometry.*

Using datum objects is often the best way to produce stable models, when used with base planes and attachment offsets, although it requires a bit more work from the user. For details about basic attachment see: [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) *Note: while this tutorial talks about sketches, datum attachment is done in similar fashion.*

## Tutorien

Die _.

-   [Erstellen eines einfachen Teils mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md)
-   [Grundlagen Part Design Tutorium](Basic_Part_Design_Tutorial/de.md)
-   [Basic\_Attachment\_Tutorial/de](Basic_Attachment_Tutorial/de.md)

## Verwandt

-   [Konstruktive Volumengeometrie](Constructive_solid_geometry/de.md)

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}} 

_

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Feature editing/de
