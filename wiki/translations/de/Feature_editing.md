# Feature editing/de
{{TOCright}}

## Einführung

Diese Seite erklärt die vorgesehene Arbeitsweise des Arbeitsbereichs <img alt="" src=images/Workbench_PartDesign.svg  style="width   *32px;"> [PartDesign](PartDesign_Workbench/de.md) für den Einsatz ab FreeCAD 0.17.

Während der Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part](Part_Workbench/de.md) und andere Arbeitsbereiche Modelle konstruieren, indem sie Formen miteinander kombinieren (siehe [Konstruktive Volumenkörpergeometrie](Constructive_solid_geometry/de.md)), verwendet der Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign](PartDesign_Workbench.md) **[Formelemente](PartDesign_Feature/de.md)**. Als Formelement ([(form) feature](https   *//en.wikipedia.org/wiki/Feature_recognition)) wird ein Vorgang bezeichnet, der die Form eines Modells verändert.

## Formelement Bearbeitungsmethodik 

Das erste Formelement wird allgemein als **Basisformelement** bezeichnet. Wenn dem Modell weitere Formelemente hinzugefügt werden, übernimmt jedes Formelement die Form des vorherigen und fügt Inhalte hinzu oder entfernt sie, wodurch lineare Abhängigkeiten von einem Formelement zum nächsten entstehen. Eigentlich imitiert diese Methodik einen üblichen Herstellungsprozess   * Ein Block wird an der einen Seite beschnitten, dann werden an einer anderen Seite Löcher hinzugefügt, dann Rundungen, usw.

Alle Formelemente werden nacheinander im Modellbaum aufgelistet und können jederzeit bearbeitet werden, wobei das letzte Formelement am unteren Rand das fertige Teil darstellt.

Formelemente können in verschiedene Kategorien eingeteilt werden   *

-   **Profil-basiert**   * Diese Formelemente gehen von einem Profil aus, um die Form der hinzuzufügenden oder zu entfernenden Inhalte festzulegen. Das Profil kann eine Skizze, eine ebene Fläche auf vorhandener Geometrie (ein Profil wird aus ihren Kanten extrahiert), ein Formbinder oder ein Draft-Objekt sein, das in den aktiven Körper eingefügt wurde.

-   **Additiv**   * Fügt dem bestehenden Modell Material hinzu. Additive Formelemente werden mit gelben Symbolen dargestellt.

-   **Subtraktiv**   * Entfernt Material aus dem bestehenden Modell. Subtraktive Formelemente werden mit rot und blauen Symbolen dargestellt.

-   **Grundkörper-basiert**   * Basiert auf geometrischen Grundkörpern (Würfel, Zylinder, Kegel, Torus\....). Sie können additiv oder subtraktiv sein.

-   **Transformierende Formelemente**   * Sie wenden eine der Musterfunktionen (Transformationen) auf bestehende Formelemente an (Spiegeln, Lineares Muster, Polares Muster, Mehrfach-Transformation).

-   **Modifikationen** (Dress-up)   * Formelemente, die eine Veränderung an Kanten oder Flächen bewirken, wie z.B. Verrundungen, Fasen und Formschrägen.

-   **Prozedural** (Ablauforientiert)   * Formelemente, die nicht auf Skizzen basieren, wie die Musterfunktionen und Modifikationen.

## Körper

Die Arbeit in PartDesign erfordert zunächst das Erstellen eines <img alt="" src=images/PartDesign_Body.svg  style="width   *24px;"> **[Körpers](PartDesign_Body/de.md)**. Der PartDesign-Körper (Body-Objekt) ist ein Behälter, der eine Folge von Formelementen gruppiert, die einen einzigen zusammenhängenden Volumenkörper (Solid) bilden.

![](images/PartDesign_Body_tree.png )

**Was ist ein einzelner zusammenhängender Volumenkörper?** Es handelt sich um einen Objekt wie ein Gussstück oder etwas, das maschinell aus einem einzigen Metallblock herausgearbeitet wurde. Wenn das Objekt Nägel, Schrauben, Kleben oder Schweißen beinhaltet, ist es kein einzelner zusammenhängenden Volumenkörper. Ein praktisches Beispiel ist ein Holzstuhl, der aus mehreren Körpern zusammengestellt wird, mit einem für jede seiner Unterkomponenten (Beine, Latten, Sitz usw.).

In einem FreeCAD-Dokument können mehrere Körper erstellt werden; sie können auch zu einem einzigen zusammenhängenden Volumenkörper verbunden werden.

In einem Dokument kann nur ein Körper aktiv sein. Der aktive Körper erhält die neu erstellten Formelemente. Ein Körper kann durch Doppelklick aktiviert oder deaktiviert werden. Ein aktivierter Körper wird hellblau hervorgehoben. Die Hervorhebungsfarbe kann seit Version 0.18 in den Einstellungen unter Anzeige/Farben/Aktiver Container eingestellt werden.

Wenn ein Modell mehrere Körper benötigt, wie im vorherigen Beispiel des Holzstuhls, kann der uninverselle <img alt="" src=images/Std_Part.svg  style="width   *24px;"> [Part-Container](Std_Part/de.md) verwendet werden, um sie zu gruppieren und das Ganze als Einheit zu bewegen.

### Körpersichtbarkeitsverwaltung

Ein Body präsentiert standardmäßig sein neuestes Formelemente nach außen. Diese Funktion ist standardmäßig als die Spitze definiert. Eine gute Analogie ist der Ausdruck*die Spitze des Eisbergs*   * Nur die Spitze ist über dem Wasser sichtbar, der größte Teil der Masse des Eisbergs (die anderen Formelemente) ist verborgen. Wenn dem Körper ein neues Formelement hinzugefügt wird, wird die Sichtbarkeit des vorherigen Formelements deaktiviert, und das neue Formelement wird zur Spitze.

Es kann immer nur ein Formelement zur Zeit sichtbar sein. Es ist möglich, die Sichtbarkeit eines beliebigen Formelements im Körper [umzuschalten](Std_ToggleVisibility/de.md), indem man es im Modellbaum markiert und die **Leertaste** drückt, wodurch man sich in der Verlaufsgeschichte des Körpers zurück bewegt.

### Körperursprung

Der Körper hat einen Ursprung, der die Bezugsebenen (XY, XZ, YZ) und die Achsen (X, Y, Z) enthält, die von Skizzen und Formelementen verwendet werden können. Skizzen können an Ursprungsebenen angehängt werden, und sie müssen nicht mehr auf ebene Flächen abgebildet werden, damit darauf basierende Formelemente hinzugefügt oder vom Modell abgezogen werden können.

### Objekte verschieben und neu ordnen 

Es ist möglich, die Spitze vorübergehend einem Formelement in der Mitte des Körperbaums zuzuordnen, um (darunter) neue Objekte (Formelemente, Skizzen oder Bezugsgeometrie) einzufügen. Es ist auch möglich, Formelemente in einem Körper neu zu ordnen oder sie in einen anderen Körper zu verschieben. Das Objekt auswählen und mit der rechten Maustaste darauf klicken, öffnet ein Kontextmenü, das beide Optionen enthält. Die Operation kann abgebrochen werden, wenn das Objekt Abhängigkeiten im Quellkörper aufweist, z.B. wenn es an einer Fläche befestigt ist. Um eine Skizze in einen anderen Körper zu verschieben, sollte sie keine Verknüpfungen zu externer Geometrie enthalten.

### Unterschied zu anderen CAD Systemen 

Ein grundlegender Unterschied zwischen FreeCAD und anderen Programmen, wie Catia, besteht darin, dass FreeCAD es nicht erlaubt, dass ein <img alt="" src=images/PartDesign_Body.svg  style="width   *24px;"> **[PartDesign-Körper](PartDesign_Body/de.md)** mehrere nicht verbundene Volumenkörper enthält. Das heißt, ein neues Formelement sollte immer auf dem vorherigen aufbauen. Oder anders ausgedrückt, das neuere Formelement sollte das vorherige Formelement \"berühren\", so dass beide Formelemente miteinander vereinigt und zu einem einzigen Festkörper werden. Es darf keine \"schwebenden\" Volumenkörper geben.

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width   *550px;">



*Unterschied zwischen Catia und FreeCAD. Links   * Catia erlaubt unabhängige Körper, getrennt von den vorherigen Formelementen des Körpers. In FreeCAD verursacht dies einen Fehler; Rechts   * Das neuere Formelement sollte immer das vorherige Formelement berühren oder schneiden, so dass es sich mit ihm vereinigt und zu einem einzelnen zusammenhängenden Volumenkörper wird.*

## Bezugsgeometrie

Die Bezugsgeometrie besteht aus benutzerdefinierten Ebenen, Linien, Punkten oder extern verknüpften Formen. Sie können zur Verwendung als Referenz für Skizzen und Formelemente erstellt werden. Es gibt eine Vielzahl von Befestigungsmöglichkeiten für Bezugsobjekte.

In einigen CAD-Systemen kann eine Bezugsebene festgelegt werden, die zum vorherigen Körper versetzt ist, und es können nicht verbundenen Körper erstellt werden. Das Platzieren vieler Bezugsebenen und das Erstellen von Objekten auf ihnen ist also in Ordnung und führt nicht zu einem Fehler. Typischerweise werden die Ebenen schließlich an ihre Endpositionen angepasst, so dass die einzelnen Objekte miteinander vereinigt werden.

In FreeCAD sind, wie im vorigen Abschnitt erwähnt, unverbundene Körper **NICHT** erlaubt, so dass eine Skizze auf einer Bezugsebene, die einen nicht zusammenhängende Körper erzeugen würde, fehlschlägt.

In FreeCAD sind Bezugsebenen sinnvoll, wenn Skizzen (und Polsterungen, Taschen usw.) in nicht standardmäßigen Ausrichtungen platziert werden, d.h. in Ebenen, die um die drei Hauptachsen versetzt oder gedreht sind. Da Skizzen auf die gleiche Weise wie Bezugsebenen auch in nicht standardmäßigen Ausrichtungen platziert werden können, ist es oft nicht notwendig, Bezugsebenen zu verwenden.

Bezugsebenen sind auch dann sinnvoll, wenn es mehr als eine Skizze in derselben nicht standardmäßigen Ausrichtung geben wird. In diesem Fall kann eine Bezugsebene verwendet werden, und die Ausrichtung muss nur für die Bezugsebene angepasst werden, um alle zugehörigen Skizzen und die aus den Skizzen erstellten Formelemente anzupassen.

Sowohl Skizzen als auch Bezugsebenen sollten an den Basisebenen angebracht werden. Das Referenzieren auf erzeugte Geometrie (Geometrie, die das Ergebnis eines Vorgangs zur Formelement-Erzeugung ist, z.B. ein Polster oder eine Tasche) sollte vermieden werden, da Flächen und Kanten umbenannt werden und eine neue Zählnummer erhalten und die Referenzen sich nicht mehr auf dasselbe Element beziehen. Dies wird topologische Instabilität genannt und liegt in der Art und Weise begründet, wie FreeCAD einige der externen Geometriebibliotheken verwendet. Es ist zu hoffen, dass dies zukünftig verbessert wird. (Siehe Ratschläge zum Erstellen stabiler Modelle weiter unten).

Auch wenn sie nicht als Grundlage für Skizzen verwendet werden, sind Bezugsobjekte als visuelle Indikatoren hilfreich, um auf wichtige Merkmale oder Abstände im Modellierungsprozess hinzuweisen. (Allerdings bietet auch das einfache Hinzufügen von Geometrie zu einer Skizze eine ähnliche visuelle Rückmeldung).

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width   *550px;">



*Unterschied zwischen Catia und FreeCAD. Links   * Catia erlaubt unabhängige Körper, getrennt von den vorherigen Formelementen des Körpers. In FreeCAD verursacht dies einen Fehler; Rechts   * Das neuere Formelement sollte immer das vorherige Formelement berühren oder schneiden, so dass es mit ihm vereinigt und zu einem einzelnen zusammenhängenden Volumenkörper wird. In diesem Beispiel basiert der neue Volumenkörper auf einer Bezugsebene, die um die Y-Achse gedreht wird.*

## Querverweise

Es ist möglich, Querverweise von Elementen eines Körpers in einen anderen Körper über Bezüge zu erstellen. Zum Beispiel erlaubt der Bezug Formbinder, Flächen aus einem Körper als Referenz in einen anderen Körper zu kopieren. So sollte es leicht möglich sein, einen Kasten mit passendem Deckel in zwei verschiedenen Körpern zu bauen. FreeCAD hilft zu verhindern, versehentlich auf andere Körper zu verweisen, indem es nach einer Bestätigung für diese Aktion fragt.

## Anhängen

Das Anhängen von Objekten ist kein besonderes PartDesign-Werkzeug, sondern vielmehr ein in v0.17 eingeführtes Part-Dienstprogramm, das im Menü Formteil zu finden ist. Es wird im Arbeitsbereich PartDesign häufig verwendet, um Skizzen und Referenzgeometrie an die Standardebenen und -achsen des Körpers anzuhängen. Es stehen sehr umfangreiche Möglichkeiten zum Erstellen von Bezugspunkten, -linien und -ebenen zur Verfügung. Optionale Parameter für den Versatz von Anhängen machen dieses Werkzeug sehr vielseitig.

Weitere Information findet man auf der Seite [Part Befestigen](Part_EditAttachment/de.md) und im [Basic Attachment Tutorial](Basic_Attachment_Tutorial/de.md).

## Ratschläge zur Erstellung stabiler Modelle 

Die Idee der parametrischen Modellierung beinhaltet, dass die Werte bestimmter Parameter verändert werden können und die nachfolgenden Schritte den neuen Werten entsprechend geändert werden. Bei schwerwiegenden Änderungen kann das Modell jedoch aufgrund des in FreeCAD noch ungelösten [Problem der topologischen Benennung](topological_naming_problem/de.md) brechen. Der Bruch kann minimiert werden, wenn die folgenden Konstruktionsprinzipien eingehalten werden   *


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

Es gibt mehrere Arbeitsabläufe, die mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) möglich sind. Stets zu beachten ist, dass alle in einem [PartDesign Körper](PartDesign_Body/de.md) erstellten Formelemente miteinander vereinigt werden, um das endgültige Objekt zu erhalten.

### Verschiedene Skizzen 

Skizzen müssen von einer Ebene unterstützt werden. Diese Ebene kann eine der Hauptebenen (XY, XZ oder YZ) sein, die durch den Ursprung des Körpers definiert sind. Eine Skizze wird entweder mit einem Werkzeug wie <img alt="" src=images/PartDesign_Pad.svg  style="width   *24px;"> [PartDesign Polster](PartDesign_Pad/de.md) zu einem positiven Festkörper (Additiv) oder zu einem negativen Festkörper (subtraktiv) mit einem Werkzeug wie <img alt="" src=images/PartDesign_Pocket.svg  style="width   *24px;"> [PartDesign Tasche](PartDesign_Pocket/de.md) ausgeformt. Der erste fügt der endgültigen Form des Körpers Volumen hinzu, während der zweite das Volumen aus der endgültigen Form schneidet. Auf diese Weise können beliebig viele Skizzen und Teilkörper erzeugt werden; die endgültige Form (Spitze) ergibt sich aus der Verschmelzung dieser Vorgänge. Natürlich kann der Körper nicht nur aus subtraktiven Operationen bestehen, da die endgültige Form ein Körper mit einem Volumen größer Null sein sollte.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width   *600px;">

### Fortlaufende Merkmale 


<div class="mw-translate-fuzzy">

Skizzen können an Flächen früherer Festkörperoperationen befestigt werden. Dies kann notwendig sein, wenn man auf eine Fläche zugreifen muss, die erst nach der Erstellung eines bestimmten Merkmals verfügbar ist. Dieser Arbeitsablauf ist jedoch nicht besonders empfehlenswert, da bei einer Änderung des ursprünglichen Merkmals die folgenden Merkmale in der Sequenz ungültig werden können. Siehe [Topologisches Benennungsproblem](topological_naming_problem/de.md).


</div>

<img alt="" src=images/PartDesign_workflow_2.svg  style="width   *600px;">

### Verwendung von Bezugsebenen zur Unterstützung 


<div class="mw-translate-fuzzy">

Bezugsebenen sind nützlich, um die Skizzen zu unterstützen. Diese Hilfsebenen können auf dem Ursprung des Körpers basieren oder auf den Merkmalen (Kanten, Flächen) von zuvor erstellten Festkörpern. Darüber hinaus kann ein <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width   *24px;"> [PartDesign ShapeBinder/de](PartDesign_ShapeBinder/de.md) verwendet werden, um externe Geometrie in den Körper zu importieren, die als Referenz dient; dann können Skizzen an diesen Hilfskörper angehängt werden, entweder mit oder ohne Bezugsebene. Die Verwendung von Bezugsobjekten ist oft der beste Weg, um stabile Modelle zu erstellen, obwohl sie vom Benutzer etwas mehr Arbeit erfordert.


</div>

*Note   * In many cases, a sketch attached to a base plane with attachment offsets can accomplish the same function. Datums are particularly useful when multiple sketches or other constructs will use the datum. This means all changes to the datum will be apply to attached sketches, etc. Adding a single sketch to a datum, rather than using attachment offsets in the sketch properties, is an extra step and is essentially redundant.*

As with sketches, it is possible to attach Datum planes to generated geometry (edges, faces of previously created solids), ***but this is not recommended*** since it can cause the topological naming problem.

In addition, a <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width   *24px;"> [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) can be used to import external geometry into the body to serve as reference; then sketches can be attached to this auxiliary body, either using datum planes or not.

*Again, the ShapeBinder should be based on Sketches from the previous body, not generated geometry.*

Using datum objects is often the best way to produce stable models, when used with base planes and attachment offsets, although it requires a bit more work from the user. For details about basic attachment see   * [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) *Note   * while this tutorial talks about sketches, datum attachment is done in similar fashion.*

## Tutorien

Die Seite [Tutorien](Tutorials/de.md) enthält einige Beispiele für die Verwendung der Methode [Formelemente bearbeiten](Feature_editing/de.md) des Arbeitsbereichs <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign](PartDesign_Workbench/de.md).

-   [Erstellen eines einfachen Teils mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md)
-   [Grundlagen Part Design Tutorium](Basic_Part_Design_Tutorial/de.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial/de.md)

## Related


<div class="mw-translate-fuzzy">

## Verwandt

-   [Konstruktive Volumengeometrie](Constructive_solid_geometry/de.md)


</div>

<img alt="" src=images/PartDesign_workflow_3.svg  style="width   *600px;">


{{PartDesign Tools navi

}} 

[Category   *Common Questions](Category_Common_Questions.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/de
