---
- TutorialInfo:/de
   Topic:Modellierung
   Level:Fortgeschrittener Anfänger
   Author:[Yorik](User_Yorik.md)
   FCVersion:0.14
---

# Arch tutorial/de





![](images/Arch_tutorial_00.jpg )



## Einleitung

Dieses Tutorial zeigt Ihnen die Grundlagen für das Arbeiten mit dem Arbeitsbereich [Arch](Arch_Workbench/de.md). Ich werde versuchen alles so einfach zu beschreiben, sodass keine Vorkenntnisse in FreeCAD notwendig sind. Vorliegende Erfahrungen mit 3D oder [Gebäudedatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling) sind jedoch von Vorteil. Unabhängig davon sollten Sie bei Bedarf weitere Informationen über FreeCAD im dazugehörigen [Wiki](Main_Page/de.md) nachschlagen. Besonders wichtig ist die Seite [Erste Schritte](Getting_started/de.md), die sich FreeCAD-Anfänger unbedingt durchlesen sollten. Weiterhin empfehlenswert sind die [Tutorien](tutorials/de.md) und die dazu passenden Videos auf [Youtube](http://www.youtube.com/results?search_query=freecad).

Der Zweck des Arbeitsbereichs [Arch](Arch_Workbench/de.md) ist es, alle notwendigen Arbeitsschritte für die [Gebäudedatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling) in FreeCAD zusammenzufassen. Da die Software momentan noch in der Entwicklungsphase ist, ist das Angebot an Werkzeugen im Vergleich zu kommerziellen Alternativen wie [Revit](https://de.wikipedia.org/wiki/Revit) oder [ArchiCAD](https://de.wikipedia.org/wiki/ArchiCAD) kleiner. Andererseits ist FreeCAD für einen größeren Aufgabenbereich als diese Programme nutzbar, was beim Arbeiten mit dem Arbeitsbereich [Arch](Arch_Workbench/de.md) einige nützliche Möglichkeiten mit sich bringt, die klassische BIM-Programme nur selten bieten können.

Im Folgenden sind einige Merkmale des Arbeitsbereichs [Arch](Arch_Workbench/de.md) gelistet, die nur selten in anderen BIM-Programmen zu finden sind:

-   Architekturobjekte sind stets Festkörper. Dies ist in Hinsicht des streng technischen Hintergrundes von FreeCAD sehr wichtig. Bool\'sche Operationen werden wesentlich fehlerfreier ausgeführt. Dies ist auch in Bezug auf Schnitterstellung ein wichtiger Punkt, da 3D-Objekte durch 2D-Flächen geschnitten werden.

-   Architektonische Objekte können grundsätzlich jede beliebige Form haben. Wände müssen nicht vertikal sein und Decken müssen nicht wie welche aussehen. Jeder beliebige Volumenkörper kann ein architektonisches Objekt sein. Sehr komplexe Dinge, die in anderen BIM Programmen normalerweise nur schwer zu beschreiben sind, z.B. eine Bodenplatte, die sich nach oben krümmt und in die Wand übergeht, stellen in FreeCAD kein besonderes Problem dar.

-   Ihnen stehen die gesamten Möglichkeiten von FreeCAD zur Verfügung. Sie können Ihre Objekte in jedem Arbeitsbereich von FreeCAD erstellen (z.B. [PartDesign](PartDesign_Workbench/de.md)) und hinterher in Architekturobjekte konvertieren. Das Objekt behält dabei seine Modellierungsgeschichte und seine Eigenschaften können nach wie vor geändert werden. Der Arbeitsbereich [Arch](Arch_Workbench/de.md) erbt zudem viele Funktionalitäten des Arbeitsbereichs [Draft](Draft_Workbench/de.md), wie z.B. [Draft Snap](Draft_Snap/de.md) oder [Wähle Ebene](Draft_SelectPlane/de.md).

-   Der Arbeitsbereich [Arch](Arch_Workbench/de.md) unterstützt auch Modelle aus [Polygonnetzen](Mesh_Workbench/de.md). Sie können das gewünschte Modell in einer 3D-Grafiksoftware, die mit Polygonnetzen arbeitet (z.B. [Blender](https://de.wikipedia.org/wiki/Blender_%28software%29) oder [SketchUp](https://de.wikipedia.org/wiki/Sketchup)), erstellen und hinterher in FreeCAD importieren. Wenn das Modell sorgfältig erstellt wurde und keine Überschneidungen von 3D-Körpern aufweist, dann ist nur ein Klick notwendig, um daraus ein Architekturobjekt zu erzeugen.

Zum momentanen Zeitpunkt, zu dem ich das Tutorial schreibe, besitzen FreeCAD und auch der Bereich [Arch](Arch_Workbench/de.md) einige Einschränkungen. An den meisten davon wird gearbeitet und sie werden wohl in der Zukunft verschwinden.

-   FreeCAD ist keine 2D-Anwendung, sondern wurde für 3D gemacht. Es gibt zwar in den Arbeitsbereichen [Draft](Draft_Workbench/de.md) und [Sketcher](Sketcher_Workbench/de.md) eine vernünftige Menge an Werkzeugen für das Zeichnen und Bearbeiten von zweidimensionalen Objekten, doch das Programm wurde nicht für die Verarbeitung von sehr großen (und manchmal schlecht gezeichneten) zweidimensionalen CAD-Dateien ausgelegt. Im Normalfall können solche Dateien zwar mit FreeCAD geöffnet werden, aber man sollte dabei besser keine hohe Leistungsfähigkeit des Programms erwarten. Sie wurden gewarnt.

-   Momentan keine Unterstützung von Materialien. FreeCAD wird irgendwann ein vollständiges System von [Materialien](Material.md) bekommen, das die Definition von komplexen Materialien mit all ihren Eigenschaften erlaubt. Der [Arch-Arbeitsbereich](Arch_Workbench/de.md) wird diese natürlich auch verwenden können, wenn es soweit ist.

-   Nur eingeschränkte Unterstützung des offenen Standards [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). Die dazugehörigen IFC-Dateien lassen sich zwar schon [importieren](Arch_IFC/de.md), wenn [IfcOpenShell](http://ifcopenshell.org) auf dem PC installiert ist, aber das Exportieren wird momentan offiziell noch nicht unterstützt. Die Entwickler von FreeCAD und IfcOpenShell arbeiten gemeinsam daran, sodass eine vollständige Unterstützung in der Zukunft zu erwarten ist.

-   Die meisten Werkzeuge im Arbeitsbereich *Arch* sind noch in Entwicklung. Deshalb können viele der Werkzeuge zum automatischen Generieren von komplexen Strukturen, wie z.B. [Arch Roof](Arch_Roof/de.md) oder [Arch Treppe](Arch_Stairs/de.md), bislang nur bestimmte Objekte erzeugen. Andere Werkzeuge mit Voreinstellungen, z.B. [Arch Struktur](Arch_Structure/de.md) oder [Arch Fenster](Arch_Window/de.md), bieten bisher nur wenige Voreinstellungen zur Auswahl. Der Umfang dieser Werkzeuge wird mit der Zeit sicherlich noch wachsen.

-   [Einheiten](Units.md) werden noch in FreeCAD implementiert, was die Arbeit mit jeder beliebigen Einheit ermöglichen wird. Momentan ist die Implementierung jedoch noch nicht abgeschlossen und der Arbeitsbereich *Arch* unterstützt sie noch nicht. Die Arbeit geschieht also einheitenlos.


{{Note|FreeCAD Version 0.14 oder neuer erfordert|Beim Erstellen dieses Tutorials wurde [FreeCAD version 0.14](Release_notes_0.14.md) verwendet. Sie werden entweder diese oder eine neuere Version des Programms benötigen, um alle Schritte des Tutorials nachvollziehen zu können.}}



## Typische Vorgehensweise 

Der [Arch-Arbeitsbereich](Arch_Workbench/de.md) ist hauptsächlich für zwei Vorgehensweisen ausgelegt:

-   Erstellen Sie das Modell mit einem schnelleren, auf Polygonnetzen basierendem Programm (z.B. [Blender](https://de.wikipedia.org/wiki/Blender_%28software%29) oder [SketchUp](https://de.wikipedia.org/wiki/Sketchup)) und importieren Sie das Modell anschließend in FreeCAD, um Pläne zu extrahieren und Schnittansichten zu erstellen. FreeCAD wurde für eine hochpräzise Modellierung ausgelegt, wie sie im Architekturbereich nur selten notwendig ist, sodass die Modellierung von Architekturobjekten unter Umständen langsam und schwerlich verläuft. Aus diesem Grund hat eine Vormodellierung mit 3D-Grafiksoftware mitunter große Vorteile. Ich habe dies in [diesem Artikel](http://yorik.uncreated.net/guestblog.php?2012=180) in meinem Blog beschrieben. Wenn Sie wirklich präzise modellieren wollen (sauber, Volumenkörper, ohne Überschneidungen der Polygonnetze), dann wird Ihnen diese Vorgehensweise dieselbe Präzision und Geschwindigkeit bringen wie die andere.

-   Erstellen des Modells direkt in FreeCAD. Diese Vorgehensweise wird in diesem Tutorial vorgestellt. Dabei benutzen wir hauptsächlich die drei Arbeitsbereiche [Arch](Arch_Workbench/de.md), [Sketcher](Sketcher_Workbench/de.md) und [Draft](Draft_Workbench/de.md). Die Werkzeuge von *Draft* sind bereits in *Arch* integriert, sodass kein Wechsel des Arbeitsbereichs notwendig ist. Es ist in diesem Fall zweckdienlich, eine eigene Werkzeugleiste im Arbeitsbereich *Arch* zu erstellen (Menü: **Werkzeuge → Benutzerdefiniert**) und die häufiger verwendeten Werkzeuge des Arbeitsbereichs *Sketcher* hinzuzufügen. Meine benutzerdefinierte Werkzeugleiste sieht wie folgt aus:

![](images/Arch_tutorial_01.jpg )

In diesem Tutorial werden wir ein Haus dreidimensional modellieren, basierend auf zweidimensionalen Zeichnungen, die wir aus dem Internet herunterladen.



## Vorbereitung

Um Zeit zu sparen, werden wir das Projekt nicht von Grund auf neu erstellen, sondern ein bereits existierendes Beispielprojekt verwenden. Ich habe dafür das wundervolle Haus des berühmten Architekten [Vilanova Artigas](http://en.wikipedia.org/wiki/Jo%C3%A3o_Batista_Vilanova_Artigas) ausgewählt, weil ich in der Nähe davon lebe und weil es ein wunderbares Beispiel für die erstaunliche modernistische Architektur São Paulos ist. Die dazugehörigen .dwg-Dateien sind in gepackter Form [frei verfügbar](http://www.bibliocad.com/library/second-house-vilanova-artigas_72926#) (erfordert kostenlose Registrierung). Alternativ kann eine dxf-Version davon [hier](http://yorik.uncreated.net/scripts/artigas.dxf) heruntergeladen werden.

Wir werden die 2D-Zeichnungen in der oben verlinkten dwg-Datei als Basis für unser Modell nutzen. Nach dem Entpacken der Datei sollte die resultierende dwg-Datei mit einer passenden Software wie z.B. [DraftSight](http://www.3ds.com/products-services/draftsight/overview/) geöffnet werden. Alternativ kann die Datei auch mit der Software [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) in eine dxf-Datei umgewandelt werden. Wenn der Converter installiert ist und sein Pfad in den Einstellungen von *Arch* richtig konfiguriert ist, dann lassen sich mit FreeCAD dwg-Dateien auch [direkt importieren](Draft_DXF/de.md). In der Regel ist es jedoch besser, die Dateien zuerst mit einer 2D-CAD-Software zu öffnen und von unnötigen Details zu bereinigen.

Hier habe ich alle Detailzeichnungen, Überschriften und Seitenlayouts entfernt, habe ungenutzte Instanzen beseitigt, die Abschnitte passend zur realen Lage neu angeordnet und alles zum Nullpunkt (0,0) verschoben. Danach kann die Datei ziemlich schnell von FreeCAD geöffnet werden. Prüfen Sie die verschiedenen Optionen in **Bearbeiten → Einstellungen → Import/Export → DXF/DWG**, denn diese beeinflussen wie und wie schnell FreeCAD solche Dateien importiert.

So sah die Datei nach dem anschließenden Öffnen in FreeCAD aus. Ich habe zudem die Dicke der Wände der Gruppe \"muros\" geändert und einige der Türen mit dem Werkzeug [Scale](Draft_Scale/de.md) umgedreht, weil diese mit der falschen X-Skalierung importiert wurden.

![](images/Arch_tutorial_02.jpg )

Die [Importfunktion](Draft_DXF/de.md) für dxf-Dateien, die auch beim Importieren von dwg-Dateien zur Anwendung kommt, gruppiert die importierten Objekte nach Ebenen. Es gibt zwar keine Ebenen in FreeCAD, aber es gibt [Gruppen](Std_Group/de.md). [Gruppen](Std_Group/de.md) bieten eine ähnliche Form der Organisation von Objekten, haben jedoch keine spezifischen Eigenschaften, die auf alle enthaltenen Objekte angewandt werden (wie bei Ebenen in [AutoCAD](https://de.wikipedia.org/wiki/AutoCAD)). Gruppen lassen sich jedoch innerhalb anderer Gruppen platzieren, was sehr hilfreich sein kann. Was wir nun als Erstes tun möchten, ist das Erstellen einer neuen [Gruppe](Std_Group/de.md) im [Modellbaum](Document_structure/de.md), indem wir per Rechtsklick das Dokument \"artigas\" anklicken und dann auf *Gruppe erstellen* klicken. Die neue Gruppe sollte in \"base 2D plans\" umbenannt werden und alle anderen Gruppen im Modellbaum sollte in diese Gruppe hinein verschoben werden.



## Einfügen der Wände 

Ebenso wie die meisten anderen Objekte in [Arch-Arbeitsbereich](Arch_Workbench/de.md), können auch [Wände](Arch_Wall/de.md) mit Hilfe vieler anderer Objekte erstellt werden: [Linien](Draft_Line/de.md), [Polylinien](Draft_Wire/de.md), [Skizzen](Sketcher_Workbench/de.md), Oberflächen oder Volumenkörper (oder auch von Grund auf, d.h. durch Angabe von Höhe, Breite und Länge). Die resultierende Geometrie der Wand hängt von der Geometrie der eben genannten Hilfsobjekte und ihren Attributen (z.B. der Breite) ab. Wie Sie sich wohl denken können, wird eine Wand, die auf einer Linie basiert, diese Linie für die Ausrichtung nutzen, während eine Wand, die auf einer Oberfläche basiert, diese Oberfläche als Grundfläche verwendet. Bei Volumenkörpern als Hilfsmittel nimmt die Wand die Gestalt des Volumenkörpers an. Folglich können Wände jede beliebige Form annehmen.

Es gibt in FreeCAD mehrere mögliche Strategien zum Konstruieren von Wänden. Eine davon ist es, alle vorgesehenen Wände zunächst mit dem Werkzeug [Sketcher](Sketcher_Workbench/de.md) zu zeichnen und dann ein einzelnes, großes Wandobjekt daraus zu erstellen. Dies funktioniert zwar, hat aber den Nachteil, dass alle Wände dieselbe Wandstärke (Dicke) haben werden. Alternativ kann jede Wand einzeln skizziert und umgewandelt werden. Am besten ist jedoch ein Mittelweg: Für jede Art von Wand eine [Polylinie](Draft_Wire/de.md) zeichnen und in ein Wandobjekt umwandeln. Diesen Weg werden wir im Folgenden nehmen.

![](images/Arch_tutorial_03.jpg )

Wie Sie in der Abbildung sehen können, habe ich Betonwände rot ([Vergleichsbilder](http://www.google.com/search?tbm=isch&q=casa+artigas)), die äußeren Ziegelwände grün und die Innenwände blau gezeichnet. Die Wände schneiden dabei die Türen, weil diese erst im Nachhinein eingefügt werden. Wände können außerdem auch links- oder rechtsbündig oder mittig auf ihrer Basislinie platziert werden, sodass es nicht wichtig ist, auf welcher Seite man die Basislinie zeichnet. Ich habe mich außerdem bemüht, Überschneidungen der Linien bestmöglich zu vermeiden, weil unser Modell damit sauberer werden wird. Wir werden uns später nochmal mit Überschneidungen beschäftigen.

Wenn dies erledigt ist, sollten alle erstellten Linien in einer [Gruppe](Std_Group/de.md) abgelegt werden. Anschließend sollten alle Linien gleichen Typs bei gedrückter Strg-Taste ausgewählt werden und das Werkzeug [Wand](Arch_Wall/de.md) verwendet werden. Hinterher müssen noch die Wandstärken korrigiert werden (Außenwände: 25 cm, Innenwände: 15 cm) und einige Ausrichtungen korrigiert werden. Das Ergebnis sollte wie folgt aussehen:

![](images/Arch_tutorial_04.jpg )

Wir hätten unsere Wände auch von Grund auf erstellen können. Wenn Sie den [Wand](Arch_Wall/de.md)-Button ohne gewähltes Objekt drücken, können Sie auf dem Bildschirm zwei Punkte anklicken, um eine Wand zu zeichnen. Unter der Haube allerdings wird das Wand-Werkzeug eine Linie zeichnen und eine Wand darauf bauen. In diesem Fall fand ich es didaktischer, Ihnen zu zeigen, wie die Dinge arbeiten.

Haben Sie bemerkt, dass ich großen Wert darauf gelegt habe, dass sich die Wände nicht kreuzen? Dies wird uns später einige Kopfschmerzen ersparen, wenn wir zum Beispiel unsere Arbeit an andere Anwendungen exportieren, die so etwas nicht mögen. Ich habe nur einen Schnittpunkt, wo ich zu faul war, zwei kleine Liniensegmente zu zeichnen und stattdessen eine große Polygonzugkreuzung gezeichnet habe. Das muss korrigiert werden. Glücklicherweise haben alle Arch-Objekte eine großartige Eigenschaft: Sie können eins mit einem anderen verbinden. Dabei werden ihre Geometrien miteinander vereint, sie sind aber immer noch unabhängig voneinander änderbar. Um eine der kreuzenden Wände mit der anderen zu verbinden, wählen Sie einfach eine, dann die andere bei gedrückter **Strg**-Taste und wählen das [Komponente hinzufügen](Arch_Add/de.md)-Werkzeug:

![](images/Arch_tutorial_05.jpg )

Links sind die beiden sich kreuzenden Wände, rechts das Ergebnis nach dem Hinzufügen der einen zu der anderen.


{{Note|Eine wichtige Anmerkung zu parametrischen Objekten|Etwas ist bereits jetzt zu berücksichtigen. Wie Sie sehen, ist in FreeCAD alles parametrisch: Unsere neue "vereinigte" Wand besteht aus zwei Wänden, jede basierend auf einer Grundlinie. Wenn Sie diese in der [Baumansicht](Document_structure.md) aufklappen, sehen Sie die ganzen Abhängigkeiten. Wie Sie sich vorstellen können, kann dieses kleine Spiel schnell sehr komplex werden. Wenn Sie bereits mit dem [Skizzen-Arbeitsbereich](Sketcher_Workbench/de.md) gearbeitet haben, dann hätten Sie die Grundlinien vermutlich mit beschränkten Linien gezeichnet. Diese ganze Komplexität hat ihren Preis: die Anzahl der durchzuführenden Berechnungen wächst exponentiell, wenn FreeCAD Ihre Modellgeometrie aktuell halten will. Also denken Sie daran, auf unnötige Komplexität zu verzichten, wenn es nicht notwendig ist. Halten Sie eine gute Balance zwischen einfachen und komplexen Objekten und benutzen Sie letztere in den Fällen, wo Sie diese wirklich benötigen.}}

Ich hätte beispielsweise alle meine obigen Grundlinien zeichnen können, ohne mich um Kreuzungen zu kümmern, und dies später mit dem [Komponente hinzufügen](Arch_Add/de.md)-Werkzeug reparieren können. Allerdings hätte ich die Komplexität meines Modells sehr erhöht, ohne etwas zu gewinnen. Es ist also besser, es gleich von Anfang an richtig zu machen und sie aus sehr einfachen Teilen der Geometrie zu erstellen.

Nachdem unsere Wände nun in Ordnung sind, müssen wir ihre Höhe anheben, bis sie das Dach schneiden. Weil das nicht automatisch passiert, wenn Wandobjekte auf Dächer treffen (das wird irgendwann in der Zukunft möglich sein), werden wir ein \"Dummy\"-Objekt erstellen, das der Dachform folgt, das dann von unseren Wänden subtrahiert wird.

Beim Blick auf unsere 2D-Zeichnungen sehen wir, dass der höchste Punkt des Daches 5,60 m über dem Boden ist. Deshalb werden wir unseren Wänden eine Höhe von 6 m geben, um sicherzustellen, dass sie von unserem Dummy-Dach-Objekt abgeschnitten werden. \"Warum 6 m und nicht 5,60 m?\" werden Sie vielleicht fragen. Wenn Sie bereits mit Boole\'schen Operationen (Vereinigung, Differenz, Schnittmenge) gearbeitet haben, dann wissen Sie, dass diese Operationen \"Face-to-Face\"-Situationen nicht besonders mögen. Sie ziehen klar und eindeutig kreuzende Objekte vor. Mit dem Längenüberschuss erreichen wir das.

Um die Höhen unserer Wände zu verändern, wählen Sie alle (vergessen Sie nicht die eine, die wir zur anderen hinzugefügt haben) in der Baumansicht und ändern Sie den Wert der \"Height\"-Eigenschaft.

Bevor wir das Dach machen und die Wände abschneiden können, müssen wir noch die übrigen Objekte erstellen, die abzuschneiden sind: die Wände des obigen Studios und die Säulen. Die Wände werden auf dem höher gelegenen Grundriss auf die gleiche Art gemacht wie vorher, aber auf einer Höhe von 2,60 m. Damit also die Oberkante auf 6 m ist, bekommen sie eine Höhe von 3,40 m. Sobald dies getan ist, werden wir unsere Wände auf 2,60 m anheben: Wählen Sie beide, wechseln in die Frontansicht (Ansicht → Standardansichten → Vorne), drücken den [Verschieben](Draft_Move/de.md)-Button, wählen einen ersten Punkt, geben dann 0, 2,6, 0 als Koordinaten ein und drücken Enter. Ihre Objekte sind nun 2,60 m hoch gesprungen:

![](images/Arch_tutorial_06.jpg )


{{Note|Zu Koordinaten|Die [Draft](Draft_Workbench/de.md)-Objekte und auch die meisten der [Arch](Arch_Workbench/de.md)-Objekte folgen einem Draft-System genannt [Ebene markieren](Draft_SelectPlane/de.md). Dieses System definiert eine 2D-Ebene, auf der die nächsten Operationen stattfinden. Wenn Sie keine angeben, dann richtet sich die Arbeitsebene nach der aktuellen Ansicht. Deshalb haben wir zur Frontansicht gewechselt, und Sie haben gesehen, dass wir Verschiebungen in der X-Richtung von 0 und der Y-Richtung von 2,6 angegeben haben. Wir hätten auch mit dem [Ebene markieren](Draft_SelectPlane/de.md)-Werkzeug die Arbeitsebene auf dem Boden belassen und dort als Verschiebung 0, 0, 2,6 (X, Y, Z) angeben können.}}

Jetzt verschieben wir die Wände horizontal an ihre richtige Position. Da wir Punkte zum Einrasten haben, ist es einfacher: Wählen Sie beide Wände, drücken das [Verschieben](Draft_Move/de.md)-Werkzeug und bewegen sie von einem Punkt zum anderen:

![](images/Arch_tutorial_07.jpg )

Schließlich habe ich die Farbe einiger Wände in eine backsteinähnliche Farbe geändert (damit sie einfacher zu unterscheiden sind) und eine kleine Korrektur durchgeführt: Einige Wände gehen nicht bis zum Dach, sondern enden in einer Höhe von 2,60 m. Ich habe die Höhe dieser Wände korrigiert.



## Anheben der Struktur 

Jetzt, da wir unsere Wände mit Hilfe eines Differenzkörpers abschneiden wollen, können wir auch nachsehen, ob es nicht weitere Objekte gibt, die auf diese Weise behandelt werden müssen. Bei einigen Säulen ist das so. Dies ist eine gute Gelegenheit, ein zweites Arch-Objekt einzuführen: die [Struktur](Arch_Structure/de.md). Strukturobjekte verhalten sich mehr oder weniger wie Wände, aber sie sind nicht gemacht, um einer Grundlinie zu folgen. Stattdessen basieren sie auf einem Profil, das extrudiert wird (entlang einer Profillinie oder nicht). Jedes flache Objekt kann ein Profil für eine Struktur sein, mit nur einer Voraussetzung: Sie müssen eine geschlossene Form bilden.

Bei unseren Säulen werden wir eine andere Strategie als bei den Wänden verwenden. Anstatt auf den 2D-Plänen zu \"zeichnen\" werden wir direkt Objekte daraus benutzen: Die Kreise, die die Säulen in der Planansicht darstellen. In der Theorie können wir einfach einen von ihnen wählen und den [Struktur](Arch_Structure/de.md)-Button drücken. Wenn wir das tun, werden wir allerdings nur ein \"leeres\" strukturelles Objekt erzeugen. Das liegt daran, dass man nie ganz sicher sein kann, wie gut die Objekte einer DWG-Datei gezeichnet wurden, und oftmals sind es keine geschlossenen Formen. Bevor wir sie also tatsächlich in Säulen umwandeln, werden wir sie durch zweimaligen Aufruf des [Hochstufen](Draft_Upgrade/de.md)-Werkzeugs in Flächen umwandeln. Beim ersten Mal entstehen daraus geschlossene Polygonzüge (Polylinien), beim zweiten Mal werden die Polygonzüge zu Flächen konvertiert. Der zweite Schritt ist nicht zwingend erforderlich, aber wenn Sie eine Fläche haben, dann können Sie absolut sicher sein, dass sie geschlossen ist (anderenfalls kann keine Fläche entstehen).

Nachdem alle Kreise zu Flächen konvertiert wurden, benutzen wir das [Struktur](Arch_Structure/de.md)-Werkzeug, und passen die Höhe an (einige haben 6 m, andere nur 2,25 m):

![](images/Arch_tutorial_08.jpg )

Auf dem obigen Bild sehen Sie zwei Säulen, die immer noch so sind wie in der DWG-Datei, zwei, die zu Flächen wurden, und zwei, die zu strukturellen Objekten mit einer Höhe von 6 m bzw. 2,25 m wurden.

Beachten Sie, dass all diese verschiedenen Arch-Objekte (Wände, Strukturen, und die anderen, die wir noch entdecken werden) eine Vielzahl von Dingen gemeinsam haben (z.B. können alle zusammengefügt werden, wie wir das bereits bei den Wänden gesehen haben, und jedes von ihnen kann zu einem anderen konvertiert werden). So ist es mehr eine Frage des Geschmacks, wir hätten unsere Säulen auch mit dem Wand-Werkzeug erstellen und sie bei Bedarf konvertieren können. Tatsächlich sind einige Wände aus Beton, wir könnten sie daher später zu Strukturen konvertieren.



## Subtraktionen

Jetzt ist es Zeit, unseren Differenzkörper zu erstellen. Der einfachste Weg ist, das Profil auf der Seitenansicht zu zeichnen. Dann drehen wir es und platzieren es an der richtigen Position. Verstehen Sie, warum ich die Ansichten auf diese Weise platziert habe? Es ist sehr bequem, um Dinge dort zu zeichnen, und sie dann an die richtige Position des Modells zu verschieben.

Lassen Sie uns einen Körper zeichnen, größer als das Dach, der von unseren Wänden subtrahiert wird. Um das zu tun, zeichnete ich zwei Linien auf die Basis des Daches und erweiterte sie ein wenig mit dem [Trimex](Draft_Trimex/de.md)-Werkzeug. Dann zeichnete ich einen [Polygonzug](Draft_Wire.md), auf diesen Linien einrastend und über unsere 6 m hinaus. Außerdem zeichnete ich eine blaue Linie auf dem Boden (0,00), die unsere Rotationsachse ist.

<img alt="" src=images/Arch_tutorial_09.jpg  style="width:1024px;">

Nun kommt der knifflige Teil: Wir werden das [Drehen](Draft_Rotate/de.md)-Werkzeug benutzen, um unser Profil um 90° nach oben in die richtige Position zu drehen, damit es extrudiert werden kann. Um das zu tun, müssen wir zuerst die [Arbeitsebene](Draft_SelectPlane/de.md) auf die YZ-Ebene setzen. Sobald dies getan ist, wird die Drehung in dieser Ebene stattfinden. Wenn wir es aber so machen würden wie ein wenig zuvor und die Ansicht auf die Seitenansicht setzen würden, wäre es schwierig zu sehen und unser Profil zu wählen, und zu wissen, wo der Basispunkt ist, um den gedreht werden muss, stimmt\'s? Dann müssen wir die Arbeitsebene manuell setzen: Drücken Sie den [Arbeitsebene](Draft_SelectPlane/de.md)-Button (er ist im \"Aufgaben\"-Reiter in der Baumansicht) und setzen Sie ihn auf YZ (welches die \"Seiten\"-Ebene ist). Sobald Sie die Arbeitsebene manuell auf diese Weise gesetzt haben, wird sie sich nicht mehr abhängig von Ihrer Ansicht ändern. Sie können nun Ihre Ansicht drehen, bis Sie einen guten Blick auf die Dinge haben, die Sie auswählen müssen. Um die Arbeitsebene später wieder zurück auf den \"automatischen\" Modus zu setzen, drücken Sie den [Ebene markieren](Draft_SelectPlane/de.md)-Button erneut und wählen \"Automatisch\".

Jetzt ist die Drehung einfach: Wählen Sie das Profil, drücken den [Drehen](Draft_Rotate/de.md)-Button, klicken auf einen Punkt der blauen Linie, geben 0 als Startwinkel (Base angle) an und 90 als Drehung (Rotation):

<img alt="" src=images/Arch_tutorial_10.jpg  style="width:1024px;">

Jetzt müssen wir nur noch das Profil etwas näher an das Modell heranschieben (setzen Sie die Arbeitsebene auf XY, falls nötig) und extrudieren Sie es. Dies kann entweder mit dem [Extrudieren](Part_Extrude/de.md)-Werkzeug oder [Trimex](Draft_Trimex/de.md) geschehen, das ebenfalls die spezielle versteckte Macht hat, um Flächen zu extrudieren. Stellen Sie sicher, dass Ihre Extrusion größer als alle Wände ist, die davon subtrahiert werden sollen, um Face-to-Face-Situationen zu vermeiden:

<img alt="" src=images/Arch_tutorial_11.jpg  style="width:1024px;">

Nun kommt das Gegenteil des [Komponente hinzufügen](Arch_Add/de.md)-Werkzeugs zum Einsatz: [Komponente entfernen](Arch_Remove/de.md). Wie Sie vielleicht vermutet haben, macht es ebenfalls ein Objekt zum Kind eines anderen, aber die Form wird vom Host-Objekt subtrahiert anstatt damit vereinigt. Jetzt sind die Dinge einfach: Wählen Sie den zu subtrahierenden Körper (ich habe es in \"Roof volume to subtract\" umbenannt in der Baumansicht, damit es einfach zu finden ist), wählen bei gedrückter **Strg**-Taste eine Wand und drücken den [Komponente entfernen](Arch_Remove/de.md)-Button. Nachdem die Subtraktion durchgeführt wurde, sehen Sie, dass der zu subtrahierende Körper aus der 3D-Ansicht und der Baumansicht verschwunden ist. Das liegt daran, dass er als Kind der Wand markiert und von der Wand \"verschluckt\" wurde. Wählen Sie die Wand, expandieren Sie diese in der Baumansicht, und dort ist unser Körper.

Wählen Sie nun den Körper in der Baumansicht, wählen bei gedrückter **Strg**-Taste die nächste Wand und drücken [Komponente entfernen](Arch_Remove/de.md). Wiederholen Sie das für die verbleibenden Wände, bis alle sauber abgeschnitten sind:

<img alt="" src=images/Arch_tutorial_12.jpg  style="width:1024px;">

Denken Sie daran, dass sowohl für [Komponente hinzufügen](Arch_Add/de.md) als auch [Komponente entfernen](Arch_Remove/de.md) die Reihenfolge bei der Auswahl der Objekte wichtig ist. Der Host ist immer das Letzte, wie in \"Entferne X von Y\" oder \"Füge X zu Y hinzu\".


{{Note|Eine Anmerkung zu Additionen und Subtraktionen|Arch-Objekte, die solche Additionen und Subtraktionen unterstützen (alle von ihnen außer den "visuellen" Hilfsobjekten wie etwa Achsen), behalten solche Objekte im Auge durch zwei Eigenschaften, nämliche "Additions" und "Subtractions", die eine Liste von Verweisen auf andere zu addierende oder subtrahierende Objekte enthalten. Das gleiche Objekt kann in den Listen verschiedener anderer Objekte sein, wie es der Fall bei unserem Differenzkörper ist. Jeder der Väter versucht, es in der Baumansicht zu verschlucken, aber es wird normalerweise nur im letzten "leben". Aber Sie können immer die Listen jedes Objekts editieren, indem Sie in der Baumansicht darauf doppelklicken, wodurch in FreeCAD der Änderungsmodus aufgerufen wird. Drücken von **Esc** beendet den Änderungsmodus.}}



## Die Dächer erstellen 

Um die Struktur zu vollenden, müssen wir jetzt nur noch das Dach und die kleineren inneren Decken erstellen. Wieder ist der einfachste Weg, die Profile mit dem [Polygonzug](Draft_Wire/de.md)-Werkzeug auf der Schnittansicht zu zeichnen. Hier habe ich drei Profile übereinander gezeichnet (ich habe sie im folgenden Bild voneinander getrennt, damit man sie besser sehen kann). Das grüne wird für die seitlichen Begrenzungen der Decken benutzt, dann das blaue für die Seitenteile und das rote für das Mittelteil, das über dem Badezimmerblock sitzt:

<img alt="" src=images/Arch_tutorial_13.jpg  style="width:1024px;">

Dann müssen wir die Drehungsoperation wiederholen, um die Objekte in eine vertikale Position zu drehen und sie dann an ihre richtigen Plätze zu verschieben, und einige kopieren, die zweimal extrudiert werden müssen. Mit dem [Verschieben](Draft_Move/de.md)-Werkzeug und gedrückter **ALT**-Taste werden Kopien des aktuellen Objekts angelegt anstatt es zu verschieben. Ich habe auch noch zwei weitere Profile für die Seitenwände der Badezimmeröffnung hinzugefügt.

<img alt="" src=images/Arch_tutorial_14.jpg  style="width:1024px;">

Wenn alles an der richtigen Stelle ist, werden die Teile mit dem [Trimex](Draft_Trimex/de.md)-Werkzeug extrudiert und anschließend zu [Struktur](Arch_Structure/de.md)-Objekten konvertiert.

<img alt="" src=images/Arch_tutorial_15.jpg  style="width:1024px;">

Danach sehen wir einige Probleme auftauchen: zwei der Säulen rechts sind zu kurz (sie sollten bis zum Dach reichen), und es gibt es eine Lücke zwischen der Decke und den Wänden des Studios rechts außen (die 2,60 m-Bemaßung in der Schnittansicht war offenkundig falsch). Dank der parametrischen Objekte ist all dies sehr einfach zu korrigieren: Ändern Sie bei den Säulen die Höhe einfach auf 6 m, holen Sie den Differenzkörper aus der Baumansicht und subtrahieren Sie ihn von den Säulen. Bei den Wänden ist es noch einfacher: Verschieben Sie diese ein wenig nach unten. Da der Differenzkörper am gleichen Platz bleibt, passt sich die Geometrie automatisch an.

Nun muss noch ein letztes Teil korrigiert werden, eine kleine Decke im Badezimmer, die einige Wände schneidet. Lassen Sie uns einen neuen Differenzkörper erstellen und diesen von den Wänden subtrahieren. Eine weitere Funktion des [Trimex](Draft_Trimex/de.md)-Werkzeugs, das wir zum extrudieren von Teilen benutzt haben, ist die Möglichkeit, nur eine einzelne Fläche eines Objekts zu extrudieren. Dies erstellt ein neues, separates Objekt, so dass keine Gefahr besteht, das andere Objekt zu \"beschädigen\". Also können wir die Basisfläche der kleinen Decke auswählen (die sichtbar wird, wenn man von unten in das Modell schaut), dann drücken Sie den [Trimex](Draft_Trimex/de.md)-Button und extrudieren Sie diese bis über die Dächer. Dann subtrahieren Sie diese von den beiden inneren Badezimmerwänden mit dem [Entfernen](Arch_Remove/de.md)-Werkzeug:

<img alt="" src=images/Arch_tutorial_16.jpg  style="width:1024px;">



## Fußböden, Treppe und Kamin 

Nachdem unsere Struktur vollständig ist, müssen wir nun eine Reihe kleinerer Objekte erstellen.



### Der Kamin 

Lassen Sie uns mit dem Kamin beginnen. Inzwischen wissen Sie, wie es funktioniert, oder? Zeichnen Sie eine Reihe von [Polygonzügen](Draft_Wire/de.md), verschieben diese mit dem [Verschieben](Draft_Move/de.md)-Werkzeug auf die korrekte Höhe, extrudieren sie mit dem [Trimex](Draft_Trimex/de.md)-Werkzeug, konvertieren den größeren in eine [Struktur](Arch_Structure/de.md), und subtrahieren die kleineren. Beachten Sie, dass der Kaminabzug nicht auf dem Boden gezeichnet wurde, aber ich habe die Position durch Ziehen von blauen Linien aus der Schnittzeichnung ermittelt.

<img alt="" src=images/Arch_tutorial_17.jpg  style="width:1024px;">



### Die Fußböden 

Die Fußböden sind in den Zeichnungen nicht gut dargestellt. Beim Blick auf die Schnittzeichnungen weiß man nicht, wo und wie dick die Bodenplatten sind. Daher werde ich annehmen, dass die Wände auf den Fundamentblöcken stehen, auf 0,00, und dass es Bodenplatten gibt, die ebenfalls auf diesen Blöcken liegen, 15 cm dick. Die Bodenplatten verlaufen nicht unter den Wänden, sondern darum herum. Wir können das tun, indem wir eine große rechteckige Bodenplatte erstellen, von der die Wände subtrahiert werden, aber denken Sie daran, Differenzoperationen kosten uns viel (Rechenzeit). Es ist besser, das in kleineren Teilen zu tun, das wird \"billiger\" in Bezug auf Berechnungen, und falls wir es intelligent tun, Raum für Raum, dann kann es uns später bei der Ermittlung der Bodenflächen helfen:

<img alt="" src=images/Arch_tutorial_18.jpg  style="width:1024px;">

Sobald die Polygonzüge gezeichnet sind, können diese in [Strukturen](Arch_Structure/de.md) umgewandelt werden und eine Höhe von 0,15 m erhalten:

<img alt="" src=images/Arch_tutorial_19.jpg  style="width:1024px;">



### Die Treppe 

Nun die Treppe. Lernen Sie das nächste der Arch-Werkzeuge kennen, die [Treppe](Arch_Stairs/de.md). Während ich dies schreibe, ist das Werkzeug immer noch in einer sehr frühen Entwicklungsphase, also erwarten Sie nicht zuviel. Es ist bereits ziemlich nützlich, um einfache, gerade Treppen zu erstellen. Das Treppen-Werkzeug ist dafür gedacht, um Treppen von einem flachen Boden zu einer Wand zu erstellen. Anders gesagt: In der Draufsicht nimmt das Treppenobjekt genau den Platz ein, den auch im Plan einnimmt, so dass die letzte Stufe nicht gezeichnet wird (aber sie wird natürlich bei der Berechnung der Höhen berücksichtigt).

In diesem Fall habe ich es vorgezogen, die Treppen in der Seitenansicht zu erstellen, weil wir viele Maße benötigen, die in dieser Ansicht einfacher zu ermitteln sind. Hier habe ich eine Reihe von roten Hilfslinien gezeichnet, dann zwei blaue Linien, die die Basis für unsere zwei Treppen bilden, und zwei grüne geschlossene Polygonzüge, die die fehlenden Teile bilden. Wählen Sie die erste blaue Linie, drücken das [Treppen](Arch_Stairs/de.md)-Werkzeug, setzen die Anzahl der Stufen auf 5, die Höhe auf 0,875, die Breite auf 1,30, den Strukturtyp auf \"massiv\" und die Strukturdicke auf 0,12. Für das andere Teil gelten die gleichen Werte.

Extrudieren Sie die beide grünen Polygonzüge auf 1,30, drehen und verschieben sie dann an die richtige Position.

<img alt="" src=images/Arch_tutorial_20.jpg  style="width:1024px;">

Zeichnen (und drehen) Sie in der Draufsicht die Treppeneinfassung.

<img alt="" src=images/Arch_tutorial_21.jpg  style="width:1024px;">

Dann verschieben Sie alles an den vorgesehenen Platz:

<img alt="" src=images/Arch_tutorial_22.jpg  style="width:1024px;">

Vergessen Sie nicht, auch die Säulen zu kürzen, die die Treppe schneiden, denn in der Gebäudedatenmodellierung ist es immer schlecht, sich kreuzende Objekte zu haben. Wir bauen wie in der realen Welt und dort können sich Festkörper nicht kreuzen. Hier wollte ich nicht die Säule direkt von den Treppen subtrahieren (anderenfalls würde das Säulenobjekt von den Treppenobjekten in der Baumansicht geschluckt werden, und das mochte ich nicht), so dass ich die Fläche, auf der die Säule steht, genommen und sie wieder extrudiert habe. Diese neue Extrusion wurde dann von den Treppen subtrahiert.

Gut! All die schwere Arbeit ist nun getan, machen wir mit der sehr schweren Arbeit weiter!



## Türen und Fenster 

[Fenster](Arch_Window/de.md) sind ziemlich komplexe Objekte. Sie werden benutzt, um alle Arten von \"eingefügten\" Objekten, wie etwa Fenster oder Türen. Ja, in FreeCAD sind Türen einfach nur eine spezielle Art von Fenstern. Im echten Leben auch, wenn Sie darüber nachdenken, oder? Das [Fenster](Arch_Window/de.md)-Werkzeug kann immer noch ein wenig schwierig zu benutzen sein, aber betrachten Sie das als Kompromiss, da es für maximale Leistung gemacht wurde. Fast jede Art von Fenster, die Sie sich vorstellen können, kann damit erstellt werden. Weil das Werkzeug noch weitere Voreinstellungen bekommen wird, verbessert sich dieser Zustand in der Zukunft sicherlich.

Das [Fenster](Arch_Window/de.md)-Objekt arbeitet wie folgt: Es basiert auf einem 2D-Layout, einem beliebiges beliebigem 2D-Objekt, aber vorzugsweise einer [Skizze](Sketcher_Workbench/de.md), die Polygonzüge (Polylinien) enthält. Diese Polygonzüge definieren die verschiedenen Teile des Fensters: Außenrahmen, Innenrahmen, Glasscheiben, feste Bestandteile (solid panels), etc. Die Fenster-Objekte haben eine Eigenschaft, in der gespeichert wird, was mit dem jeweiligen Polygonzug zu tun ist: extrudieren, in einem bestimmten Abstand platzieren, etc. Schließlich kann ein Fenster in ein Host-Objekt wie etwa eine Wand oder eine Struktur eingefügt werden, und erstellt automatisch ein Loch darin. Die Größe des Lochs wird aufgrund des größten im 2D-Layout gefundenen Polygonzugs berechnet.

Es gibt zwei Wege, um solch ein Objekt in FreeCAD zu erstellen: Durch Nutzung einer Voreinstellung oder zeichnen der Fensterausführung von Grund auf. Wir werden uns beide Methoden ansehen. Denken Sie aber daran, dass die Voreinstellungsmethode nichts anderes tut, als für Sie das Layout-Objekt zu erstellen und die notwendigen Extrusionen zu definieren.



### Voreinstellungen verwenden 

Wenn Sie das [Fenster](Arch_Window/de.md)-Werkzeug drücken, ohne ein Objekt zu wählen, werden Sie aufgefordert, entweder ein 2D-Layout herauszusuchen oder eine der Voreinstellungen zu benutzen. Lassen Sie uns die \"Einfache Tür\"-Voreinstellung verwenden, um die Haupteingangstür in unserem Modell zu platzieren. Stellen Sie ein Breite von 1 m, eine Höhe von 2,45 m sowie eine W1-Größe von 0,15 m ein und belassen Sie die anderen Parameter bei 0,05 m. Klicken Sie dann auf die linke untere Ecke der Wand, und Ihre neue Tür wurde erstellt:

<img alt="" src=images/Arch_tutorial_23.jpg  style="width:1024px;">

Sie werden feststellen, dass Ihre neue Tür nicht in der Baumansicht auftaucht. Der Grund ist, dass wir durch Einrasten an einer Wand andeuten, dass diese Wand das zugehörige Host-Objekt ist. Konsequenterweise wird es durch die Wand \"geschluckt\". Durch einen Rechtsklick auf die Tür → Gehe zur Auswahl finden Sie es im Baum.

Da unser Fenster nicht in irgendeine Wand eingefügt wird (die Öffnung war bereits vorhanden), könnten wir in diesem Fall unser Fenster von der Host-Wand lösen. Dies passiert durch doppelklicken der Host-Wand in der Baumansicht, um den Änderungsmodus aufzurufen. Dort findet sich das Fenster in der \"Subtractions\"-Gruppe. Wählen Sie das Fenster, drücken Sie den \"Komponente entfernen\"-Button und drücken \"OK\". Unser Fenster wurde von der Host-Wand entfernt und ist nun am Ende der Baumansicht.

Es gibt ein bisschen weiter links eine zweite, genau gleiche, Tür. Anstatt eine neue Tür von Grund auf zu erstellen, gibt es zwei Wege, um eine Kopie der ersten zu machen: Durch Nutzung des [Verschieben](Draft_Move/de.md)-Werkzeugs mit gedrückter **Alt**-Taste, was, wie Sie bereits wissen, eine Kopie eines Objekts macht anstatt es zu verschieben. Oder sogar noch besser das [Klonen](Draft_Clone/de.md)-Werkzeug. Das Klonen-Werkzeug erstellt einen Klon eines gewählten Objekts, das Sie herumschieben können, das aber die Form des ursprünglichen Objekts beibehält. Falls sich das Original ändert, ändert sich auch der Klon.

Nun bleibt noch, die Tür zu wählen, [Klonen](Draft_Clone/de.md) zu drücken und den Klon mit dem [Verschieben](Draft_Move/de.md)-Werkzeug an die richtige Stelle zu verschieben.



### Ihr Modell organisieren 

<img alt="" src=images/Arch_tutorial_24.jpg  style="width:400px;">

Nun wäre die richtige Zeit, um etwas aufzuräumen. Nachdem wir bereits zwei Fenster haben, bereinigen wir die Baumansicht ein wenig: Erstellen Sie eine neue [Gruppe](Std_Group/de.md), benennen sie in \"windows\" um und schieben die zwei Fenster dorthin. Ich empfehle auch, dass Sie mit anderen Elementen auf diese Weise verfahrenvoneinander zu trennen, wie den etwa Wände und Strukturen. Da Sie auch [Gruppen](Std_Group/de.md) innerhalb von Gruppen anlegen können, können Sie weiter organisieren, z.B. indem Sie alle Elemente, die das Dach formen, in eine separate Gruppe verschieben, so dass es einfach ist, sie zu aktivieren/deaktivieren (eine Gruppe sichtbar/unsichtbar machen tut das gleiche mit allen Objekten in dieser Gruppe).

Der [Arch-Arbeitsbereich](Arch_Workbench/de.md) bietet einige zusätzliche Werkzeuge, um Ihr Modell zu organisieren: [Grundstück](Arch_Site/de.md), [Gebäude](Arch_Building/de.md) und [Geschoss](Arch_Floor/de.md). Diese drei Objekte basieren auf der Standard-FreeCAD-Gruppe, so dass sie sich genau wie Gruppen verhalten, aber sie haben eine Reihe von zusätzlichen Eigenschaften. [Geschoss](Arch_Floor/de.md) hat die Fähigkeit, die Höhe der enthaltenen Wände und Strukturen zu setzen und zu verwalten, und wenn sie verschoben werden, werden auch die Inhalte verschoben.

Aber nachdem wir hier nur ein Gebäude mit einem (und einem halben) Geschoss haben, gibt es keine Notwendigkeit, solche Objekte zu benutzen, also lassen Sie uns bei einfachen Gruppen bleiben.




Lassen Sie uns zur Arbeit zurückkehren. Schalten Sie die Dach-Gruppe aus, so dass wir besser hineinsehen können, und ändern Sie den Anzeigemodus auf Drahtgitter (oder verwenden Sie das [Anzeige-Modus umschalten](Draft_ToggleDisplayMode/de.md)-Werkzeug), so dass wir weiterhin an sie einrasten können, denn auch wenn wir den Plan von unten sehen. Aber Sie können auch die Fußböden komplett ausschalten, dann Ihre Türen auf Level 0 platzieren und sie dann mit dem [Verschieben](Draft_Move/de.md)-Werkzeug um 15 cm anheben.

Lassen Sie uns die Innentüren platzieren. Verwenden Sie die \"Einfache Tür\"-Voreinstellung erneut und erstellen Türen von 1,00 m und 0,70 cm Breite, 2,10 m Höhe und W1-Größe 0,1 m. Stellen Sie sicher, dass Sie an der richtigen Wand einrasten, wenn Sie platzieren, so dass sie automatisch ein Loch in der Wand erstellen. Falls es schwierig ist, sie richtig zu positionieren, dann können Sie sie an einer einfacheren Stelle platzieren, an der Ecke der Wand zum Beispiel, und sie dann verschieben. Das \"Loch\" wird ebenfalls verschoben.

Wenn Sie aus Versehen ein Fenster in der falschen Wand platziert haben, ist das einfach zu korrigieren: Entfernen Sie im Änderungsmodus das Fenster aus der \"Subtraction\"-Gruppe der Host-Wand, wie wir das oben gesehen haben, und fügen Sie es auf die gleiche Weise in der \"Subtraction\"-Gruppe der richtigen Wand ein oder nutzen Sie einfach das [Komponente entfernen](Arch_Remove/de.md)-Werkzeug.

Nach ein wenig Arbeit sind alle Türen vorhanden:

<img alt="" src=images/Arch_tutorial_25.jpg  style="width:1024px;">

Bei einem genaueren Blick auf die Draufsicht? habe ich einen weiteren Fehler entdeckt: Die Oberkante der Ziegelwand ist nicht 2,60 m, sondern 17,5 cm tiefer, also 2,425 m. Glücklicherweise haben Fenster, die auf Voreinstellungen basieren, eine Möglichkeit, die allgemeinen Abmessungen (Breite und Höhe) durch die Eigenschaften anzupassen. Lassen Sie uns die Höhe auf 2,425 - 0,15, also 2,275 ändern. Das zweite Fenster, als ein Klon des ersten, wird sich ebenfalls anpassen. Das ist im Grunde genommen, wo sich die wahre Magie von parametrischem Design zeigt.

Nun können wir uns mit dem richtig interessanten Zeug befassen: wie man eigene maßgeschneiderte Fenster entwirft.



### Maßgeschneiderte Fenster erstellen 

Wie ich oben erklärt habe, werden [Fenster](Arch_Window/de.md) aus 2D-Layouts erstellt, die aus geschlossenen Elementen (Polygonzüge(Polylinien), Kreisen, Rechtecken, irgendetwas) bestehen. Nachdem [Draft](Draft_Workbench/de.md)-Objekte nicht mehr als eines dieser Elemente enthalten können, ist das bevorzugte Werkzeug zum Zeichnen von Fenster-Layouts der [Skizze](Sketcher_Workbench/de.md)-Arbeitsbereich. Unglücklicherweise kann man damit nicht an externen Objekten einrasten, wie das beim [Draft](Draft_Workbench/de.md)-Arbeitsbereich möglich ist. Da wir bereits dreidimensionale Objekte gezeichnet haben, wäre es schön, diese nutzen zu können. Glücklicherweise gibt es Werkzeug, um Draft-Objekte in eine Skizze konvertieren zu können: Das [Entwurf zu Skizze](Draft_Draft2Sketch/de.md)-Werkzeug.

Lassen Sie uns also mit unserem ersten Fenster-Layout beginnen. Ich habe auf die Draufsicht mehrere [Rechtecke](Draft_Rectangle/de.md) gezeichnet: Eins für die äußere Linie und vier für die innere Linie. Ich habe vor der Tür aufgehört, denn wie Sie sich erinnern, hat diese bereits einen Rahmen:

<img alt="" src=images/Arch_tutorial_26.jpg  style="width:1024px;">

Nach dem Auswählen aller Rechtecke drücken Sie den [Entwurf zu Skizze](Draft_Draft2Sketch/de.md)-Button (und löschen die Rechtecke, denn dieses Werkzeug löscht nicht die originalen Objekte, falls etwas schiefgeht). Nach Wählen der neuen Skizze drücken Sie das [Fenster](Arch_Window/de.md)-Werkzeug.

<img alt="" src=images/Arch_tutorial_27.jpg  style="width:1024px;">

Das Werkzeug wird feststellen, dass das Layout einen äußeren und mehrere innere Polygonzüge hat und Ihnen automatisch eine Standardkonfiguration vorschlagen: Ein Rahmen, entstanden durch Subtraktion der vier inneren vom äußeren Polygonzug, extrudiert auf 1 m. Lassen Sie uns das durch Doppelklick (Aufruf des Änderungsmodus) auf das Objekt in der Baumansicht ändern.

Sie werden eine \"Default\"-Komponente sehen, die automatisch durch das Fenster-Werkzeug erzeugt wurde, die die fünf Polygonzüge benutzt und einen Extrusionswert von 1 hat. Lassen Sie uns den Wert auf 0,1 ändern, damit dieser zu denen der Türen passt.

Lassen Sie uns jetzt vier neue Glasscheiben hinzufügen, die jede einen einzelnen Polygonzug verwenden, und setzen Sie einen Extrusionswert von 0,01 und einen Offset von 0,05, damit sie in die Mitte des Rahmens gesetzt werden. Das Fenster wird am Ende so aussehen:

<img alt="" src=images/Arch_tutorial_28.jpg  style="width:1024px;">

Ich vermute, dass Sie nun die Macht des Systems verstehen: Jede Kombination von Rahmen und Feldern beliebiger Form ist möglich. Wenn Sie es zweidimensional zeichnen können, kann daraus ein gültiges 3D-Objekt werden.

Lassen Sie uns jetzt die anderen Teile zeichnen und danach alles an die richtigen Stellen verschieben. Zuerst müssen wir aber in der 2D-Zeichnung noch einige Korrekturen durchführen, weil einige Linien fehlen, wo das Fenster auf die Treppe trifft. Wir können das durch Versetzen der Treppe um 2,5 cm erreichen, indem wir das [Draft Offset](Draft_Offset/de.md)-Werkzeug benutzen (mit gedrückter **Alt**-Taste, weil wir die Linien kopieren und nicht verschieben wollen). Jetzt können wir mit [Polygonzügen](Draft_Wire/de.md) ein Layout zeichnen, es zu einer Skizze konvertieren und dann ein Fenster daraus machen.

Nach mehrfacher Ausführung (ich habe es in vier separaten Stücken gemacht, aber das entscheiden Sie selbst) ist unsere Fassade vollständig:

<img alt="" src=images/Arch_tutorial_29.jpg  style="width:1024px;">

Wie vorher auch bleibt jetzt nur die Drehung der Stücke und das anschließende Verschieben an die richtige Position:

<img alt="" src=images/Arch_tutorial_30.jpg  style="width:1024px;">

Als letztes fehlendes Stück gibt es noch ein Wandsegment, das nicht im Plan aufgetaucht ist, und was wir noch hinzufügen müssen. Es gibt mehrere Möglichkeiten, das zu tun. Ich habe mich entschieden, eine Linie auf dem Fußboden zu zeichnen, sie anschließend auf die richtige Höhe anzuheben und dann daraus eine Wand zu erstellen. Ein weiteres Mal nehmen wir den Differenzkörper (er müsste in der Baumansicht bei der letzten Säule zu finden sein) und subtrahieren ihn. Nun ist diese Seite des Gebäudes fertig:

<img alt="" src=images/Arch_tutorial_31.jpg  style="width:1024px;">

Fertig? Nicht ganz. Auf dem obigen Bild sehen Sie, dass wir unsere Türen mit einem 5 cm Rahmen erstellt haben, erinnern Sie sich (das war der Standard der Voreinstellung)? Aber die anderen Fenster haben 2,5 cm Rahmen. Das müssen wir korrigieren.



### Fenster ändern 

Wir haben bereits gesehen, wie mit dem Fensteränderungsmodus Fensterkomponenten erstellt und aktualisiert werden können, aber man kann auch die darunterliegende Skizze ändern. Fenster mit Voreinstellungen unterscheiden sich nicht von maßgeschneiderten Fenster, das [Fenster](Arch_Window/de.md)-Werkzeug erstellt nur die darunterliegende Skizze für Sie. Wählen Sie das Türobjekt (das Original, nichr die Kopie, Sie erinnern sich, dass wir einen Klon erstellt haben) und expandieren Sie es in der Baumansicht. Das ist unsere Skizze. Doppelklicken Sie es, um den Änderungsmodus aufzurufen.

Der [Skizzen](Sketcher_Workbench/de.md)-Arbeitsbereich ist ein extrem mächtiges Werkzeug. Es fehlen einige Annehmlichkeiten des [Draft](Draft_Workbench/de.md)-Arbeitsbereiches, aber es hat viele andere Vorteile. In FreeCAD werden Sie abhängig von Ihren Bedürfnisses regelmäßig den einen oder anderen nutzen. Das wichtigste Merkmal der Skizze sind Einschränkungen. Einschränkungen erlauben Ihnen, die Position von Elementen relativ zu anderen automatisch zu fixieren/einzuschränken. Sie können beispielsweise ein Segment zwingen, immer vertikal zu sein oder immer einen bestimmten Abstand zu einem anderen zu haben.

Wenn wir unsere Türskizze ändern, können wir sehen, dass sie aus einer vollständig eingeschränkten Skizze besteht.

<img alt="" src=images/Arch_tutorial_32.jpg  style="width:1024px;">

Jetzt müssen wir nur den 5 cm Abstand zwischen der äußeren und der inneren Linie ändern, indem wir sie doppelklicken und den Wert aus 2,5 cm ändern. Nach Klicken des *OK*-Buttons sind unsere Tür und ihr Klon aktualisiert.



## Arbeiten ohne 2D-Unterstützung 

Bisher war unsere Arbeit relativ einfach, weil wir die darunterliegenden 2D-Zeichnungen hatten, auf die wir uns stützen konnten. Jetzt müssen wir aber die gegenüberliegende Fassade und das Glasatrium erstellen und die Dinge werden komplizierter: die Zeichnung der gegenüberliegenden Fassade enthält eine Menge von falschen Dingen, das Atrium wird überhaupt nicht dargestellt und wir haben einfach keine Zeichnung für die inneren Wände des Atriums. Wir müssen daher selbst eine Reihe von Dingen erfinden. Werfen Sie einen Blick auf [reference pictures](http://www.pedrokok.com.br/2010/02/residencia-artigas-sao-paulo-sp/img_8265-533px/), um herauszufinden, wie die Dinge aussehen. Oder machen Sie es nach Ihren Wünschen!

Eine Sache können wir bereits tun: Das komplizierte Treppenfenster kann mit dem [Verschieben](Draft_Move/de.md)-Werkzeug kopiert werden, denn es ist auf beiden Seiten identisch.

<img alt="" src=images/Arch_tutorial_33.jpg  style="width:1024px;">

Beachten Sie, dass ich hier lieber das [Verschieben](Draft_Move/de.md)-Werkzeug anstatt [Klonen](Draft_Clone/de.md) benutzt habe, denn der Klon unterstützt momentan nicht unterschiedliche Farben innerhalb von Objekten. Der Unterschied ist, dass der Klon eine Kopie der endgültigen Form des Originalobjekts ist, während bei einer Kopie ein neues Objekt mit den gleichen Eigenschaften des Originalobjekts ist (also auch der Basisskizze und der Definition der Fensterkomponenten, die beide als Eigenschaften gespeichert werden).

Nun müssen wir die Teile angehen, die nirgends gezeichnet wurden. Starten wir mit der Glaswand zwischen dem Wohnzimmer und dem Atrium. Es ist einfacher, das auf der Draufsicht zu zeichnen, weil wir die richtige Höhe des Daches erhalten. Sobald Sie in der Draufsicht sind, können Sie die Ansicht in Ansicht → Standardansichten → rechts/links drehen, bis Sie eine passende Sicht auf die Arbeit bekommen, wie hier:

<img alt="" src=images/Arch_tutorial_34.jpg  style="width:1024px;">

Beachten Sie, wie ich im obigen Bild eine Linie vom Modell zum linken Schnitt gezogen habe, um die exakte Größe des Fensters zu ermitteln. Dann habe ich diese Breite auf die Draufsicht übertragen und in vier Teile unterteilt. Anschließend habe ich ein Hauptfenster erstellt plus vier weitere Fenster für die Schiebetüren. Der Sketcher hat teilweise Schwierigkeiten mit überlappenden Polygonzügen, so dass ich sie lieber voneinander getrennt habe.

<img alt="" src=images/Arch_tutorial_35.jpg  style="width:1024px;">

Nach den notwendigen Drehungen passt alles perfekt an den Platz:

<img alt="" src=images/Arch_tutorial_36.jpg  style="width:1024px;">

Wir benötigen noch ein Eckstück hier. Ein kleiner nützlicher Trick beim [Ebene markieren](Draft_SelectPlane/de.md)-Werkzeug ist, dass es beim Drücken des Buttons die Arbeitsebene an der Fläche ausrichtet, die gerade ausgewählt ist (zumindest an der Position, und falls die Fläche rechteckig ist, auch an den Kanten). Das ist nützlich, 2D-Objekte direkt auf dem Modell zu zeichnen so wie hier, wo wir ein Rechteck zeichnen können, das gleich an der richtigen Position extrudiert werden kann.

<img alt="" src=images/Arch_tutorial_37.jpg  style="width:1024px;">

Befassen wir uns nun mit den zwei verbleibenden Stücken. Eins ist einfach, es ist eine Kopie dessen, was auf der anderen Seite ist, also können wir einfach die 2D-Zeichnung verwenden:

<img alt="" src=images/Arch_tutorial_38.jpg  style="width:1024px;">

Das andere ist etwas knifflig. Beim Blick auf die Bilder sehen wir, dass es viele vertikale Abschnitte hat, wie die Treppenfenster. Per Zufall (oder sehr guter Planung durch Vilanove Artigas) ist die Breite unseres Fensters von 4,50 m genau identisch zu dem des Treppenfensters, also können wir die gleiche Unterteilung verwenden: 15 Stücke à 30 cm. Hier habe ich das [orthogonale Anordnung](Draft_OrthoArray/de.md)-Werkzeug verwendet, um die beiden Linien 15 Mal zu kopieren und darauf Rechtecke zu zeichnen:

<img alt="" src=images/Arch_tutorial_39.jpg  style="width:1024px;">

Sobald das getan ist, können wir unser Fenster auf die bekannte Weise erstellen. Ein weiterer kleiner nützlicher Trick, falls Sie ihn nicht schon selbst gefunden haben: Wenn Sie beim Bearbeiten eines Fensters den Namen einer Komponente ändern, wird tatsächlich eine Kopie davon erstellt. Um die 15 inneren Glasscheiben zu erstellen, müssen Sie also nicht 15 Mal den \"Hinzufügen\"-Button drücken und 15 Mal die Daten eingeben, sondern nur eine bearbeiten und den Namen und den Polygonzug ändern, um jeweils eine Kopie zu erstellen.

Nachdem das Fenster gedreht und an den Platz geschoben wurde, ist das Atrium fertiggestellt:

<img alt="" src=images/Arch_tutorial_40.jpg  style="width:1024px;">



## Bearbeitungen und Korrekturen 

Wenn wir jetzt auf die Rückseite sehen und mit dem Plan vergleichen, dann stellen wir fest, dass noch einige Unterschiede korrigiert werden müssen. Das Schlafzimmerfenster ist nämlich kleiner als ich zuerst dachte und wir müssen noch einige Wände hinzufügen. Um das ordentlich zu tun, müssen zuerst einige Fußböden aufgeschnitten werden:

<img alt="" src=images/Arch_tutorial_41.jpg  style="width:1024px;">

Es gibt mehrere Wege, das zu tun. Einen Differenzkörper zu erstellen wäre leicht, aber dadurch würde eine unnötige Komplexität im Modell entstehen. Es ist besser, den Basispolygonzug jedes Fußbodens zu ändern. Hier kommt der [Bearbeiten](Draft_Edit/de.md)-Modus ins Spiel. Durch Expandieren dieser Fußböden in der Baumansicht werden die Polygonzüge sichtbar, so dass wir sie doppelklicken können, um in den Änderungsmodus zu kommen. Dort können wir ihre Punkte ändern oder Punkte hinzufügen oder entfernen. Dadurch wird die Änderung der Fußbodenplatten einfach.

<img alt="" src=images/Arch_tutorial_42.jpg  style="width:1024px;">

Nach ein wenig mehr Schweiß (die Person, die diese Zeichnungen gemacht hat, wurde offenkundig faul, als sie diese Erhebung gemacht hat, denn viel ist falsch gezeichnet), haben wir unser Haus fertiggestellt.

<img alt="" src=images/Arch_tutorial_43.jpg  style="width:1024px;">

Beachten Sie das Kaminrohr, das aus einem Kreis entstanden ist, den ich benutzt habe, um ein Loch in den Kaminblock zu machen, ihn extrudiert und dann mit dem [Versatz](Part_Offset/de.md)-Werkzeug zu einer Röhre konvertiert habe.


{{Note|Probleme in Objekten|Manchmal gibt es Probleme bei Objekten, die Sie erstellt haben. Beispielsweise wurde die Basis des Objekts gelöscht und das Objekt kann daher die Form
nicht erneut berechnen. Dies wird Ihnen durch ein kleines rotes Zeichen am Objekt und eine Warnung im Ausgabefenster angezeigt. Es gibt kein allgemeingültiges Rezept zum Reparieren dieser Probleme, da es vielfältige Gründe haben kann. Der einfachste Weg zur Lösung ist oftmals, es zu löschen und erneut zu erstellen, falls das Basisobjekt noch existiert.}}



## Ausgabe

Nachdem wir die ganze schwere Arbeit hinter uns haben, um dieses Modell zu erstellen, kommt die Belohnung: Was können wir damit tun? Das ist im Grunde genommen der große Vorteil von Gebäudedatenmodellierung, dass alle unsere traditionellen Architekturbedürfnisse, wie etwa 2D-Zeichnungen (Pläne, Schnitte, etc), Renderings und Berechnungen (Massenermittlung, etc.), aus dem Modell ermittelt werden können. Und besser noch, sie werden nach jeder Änderung am Modell wieder erneut generiert. Ich werde Ihnen zeigen, wie Sie diese verschiedenen Dokumente erhalten.



### Vorbereitungen

Bevor wir mit dem Export beginnen, gibt es eine interessante Überlegung: Wie Sie gesehen haben, wurde unser Modell zunehmend komplex, mit vielen Beziehungen zwischen Objekten. Dies kann bei folgenden Operationen, wie etwa Schnitte durch das Modell, zu umfangreichen Berechnungen führen. Ein schneller Weg, um Ihr Modell auf magische Weise drastisch zu \"vereinfachen\" besteht darin, diese Komplexität durch Export ins [STEP](https://de.wikipedia.org/wiki/Standard_for_the_exchange_of_product_model_data)-Format zu entfernen. Das Format wird Ihre komplette Geometrie erhalten, aber alle Beziehungen und Konstruktionen entfernen, so dass nur die endgültige Form übrigbleibt. Nach dem Reimport dieser STEP-Datei in FreeCAD erhalten Sie ein Modell ohne Beziehungen und einer viel geringeren Größe. Betrachten Sie es als eine \"Ausgabe\"-Datei, die Sie jederzeit aus Ihrer \"Master\"-Datei wieder erstellen können:

<img alt="" src=images/Arch_tutorial_44.jpg  style="width:1024px;">



### Export nach IFC und anderen Anwendungen 

<img alt="" src=images/Arch_tutorial_45.jpg  style="width:400px;">

Eins der sehr wesentlichen Dinge bei der Arbeit mit Gebäudedatenmodellierung ist die Möglichkeit zum Im- und Export von [IFC](https://de.wikipedia.org/wiki/Industry_Foundation_Classes)-Dateien. Diese Arbeit in FreeCAD ist noch nicht abgeschlossen. Das [IFC](Arch_IFC/de.md)-Format wird bereits unterstützt und der Import in FreeCAD funktioniert bereits ziemlich zuverlässig. Der Export ist allerdings noch experimentell und hat momentan noch viele Einschränkungen. Die Dinge werden besser und wir sollten sehr schnell einen sauberen IFC-Export erhalten.

[IFC-Export](Arch_IFC/de.md) erfordert sehr wenig Konfiguration, sobald die notwendigen Software-Bibliotheken installiert sind. Sie müssen nur die Gebäudestruktur auffrischen, was in allen IFC-Dateien nötig ist, indem Sie zu Ihrer Datei ein [Gebäude](Arch_Building/de.md) hinzufügen, dann ein [Geschoss](Arch_Floor/de.md) und anschließend alle Gruppen mit Objekten, aus denen Ihr Modell besteht, dorthin verschieben. Achten Sie darauf, dass Ihre Konstruktionselemente (die ganzen 2D-Objekte, die wir gezeichnet haben) ausgenommen bleiben, denn sonst wird die IFC-Datei unnötig aufgebläht.

Eine weitere Einstellung ist das Prüfen der \"Rolle\"-Eigenschaft von Strukturelementen. Da IFC im Gegensatz zu FreeCAD keine \"generischen\" Strukturelemente hat, müssen wir ihnen Rollen (Säule, Balken, etc.) zuweisen, so dass der Export-Prozess weiß, welches Element in der IFC-Datei zu erzeugen ist.

In diesem Fall brauchen wir unser gesamtes Architektursystem, so dass der IFC-Export-Prozess weiß, ob ein Objekt als Wand oder Säule exportiert werden muss. Daher verwenden wir unser \"Master\"-Modell, nicht unser \"Ausgabe\"-Modell.

Sobald dies getan ist, wählen Sie einfach Ihr Gebäude-Objekt aus und wählen das \"Industry Foundation Classes\"-Format. Der Export an Nicht-Gebäudedatenmodellierungs-Anwendungen wie etwa [Sketchup](http://www.sketchup.com/) ist ebenfalls einfach. Es gibt verschiedene Export-Formate zu Ihrer Verfügung, u.a. [Collada](Arch_DAE/de.md), STEP, IGES oder OBJ.




### Rendering

FreeCAD bietet auch ein Rendering-Modul, den [Raytracing-Arbeitsbereich](Raytracing_Workbench/de.md). Dieser Arbeitsbereich unterstützt momentan zwei Render-Engines, [PovRay](http://www.povray.org/) und [LuxRender](http://www.luxrender.net). Da FreeCAD nicht für Image-Rendering geplant ist, sind die Möglichkeiten des Raytracing-Arbeitsbereich ein wenig eingeschränkt. Der beste Weg zu sauberen Renderings ist, Ihr Modell in ein Netz-basiertes Format wie OBJ oder STL zu exportieren und es in einer Anwendung zu öffnen, die eher für Rendering geeignet ist, wie [blender](http://www.blender.org). Das folgende Bild wurde mit der cycles-Engine von Blender gerendert.

<img alt="" src=images/Arch_tutorial_47.jpg  style="width:1024px;">

Für ein schnelles Rendering ist der Raytracing-Arbeitsbereich bereits geeignet, mit dem Vorteil einer sehr einfachen Konfiguration, dank des Vorlagesystems. Dies ist ein Rendering unseres Modells, das innerhalb von FreeCAD mit der Luxrender-Engine und der \"internen\" Vorlage entstanden ist.

<img alt="" src=images/Arch_tutorial_48.jpg  style="width:1024px;">

Der Raytracing-Arbeitsbereich bietet Ihnen noch eine sehr eingeschränkte Kontrolle über die Materialien, aber Beleuchtung und Umgebung sind in Vorlagen definiert, so dass sie umfassend anpassbar sind.



### 2D-Zeichnungen 

Sicherlich die wichtigste Nutzung von Gebäudedatenmodellierung ist die automatische Erstellung von 2D-Zeichnungen. Das passiert in FreeCAD mit dem [Ebene markieren](Arch_SectionPlane/de.md)-Werkzeug. Dieses Werkzeug erlaubt Ihnen, ein Schnittebenen-Objekt in der 3D-Ansicht zu platzieren, die Sie ausrichten können, um Pläne, Schnitte und Ansichten zu erstellen. Schnitte müssen wissen, welche Objekte zu berücksichtigen sind, so dass Sie nach der Erstellung eines Schnittebenen-Objekts Elemente mit dem [Komponente hinzufügen](Arch_Add/de.md)-Werkzeug hinzufügen müssen. Sie können einzelne Objekte, oder bequemer, eine Gruppe, ein Geschoss oder ein komplettes Gebäude hinzufügen. Das erlaubt es Ihnen, später durch hinzufügen oder entfernen von Objekten den Umfang einer bestimmten Schnittebene zu verändern. Jede Änderung an diesen Objekten wirkt sich auf die von dieser Schnittebene erzeugten Ansichten aus.

Die Schnittebene erstellt automatisch Schnitte von den Objekten, die sie schneidet. Mit anderen Worten, anstatt Ansichten anstelle von Schnitten zu erzeugen, müssen Sie nur die Schnittebene außerhalb Ihrer Objekte anlegen.

<img alt="" src=images/Arch_tutorial_49.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Die Schnittebenen können zwei verschiedene Ausgaben erzeugen: [Formteil](Part_Workbench/de.md)-Objekte, die im gleichen Dokument wie Ihr 3D-Modell entstehen, oder [Zeichenansichten](Drawing_Workbench/de.md), die erzeugt werden, um ein Zeichenblatt zu erstellen, das mit dem [Drawing-Arbeitsbereich](Drawing_Workbench/de.md) verwendet werden kann. Jedes verhält sich anders und hat seine eigenen Vorteile.


</div>

**Formteilansichten**

Diese Ausgabe wird bei ausgewählter Schnittebene durch den [Draft Form in 2D-Ansicht](Draft_Shape2DView/de.md)-Arbeitsbereich erstellt. Sie erzeugen direkt im 3D-Raum eine 2D-Ansicht des Modells, wie im obigen Bild. Der Hauptvorteil hier ist, dass Sie mit dem [Draft-Arbeitsbereich](Draft_Workbench/de.md)-Werkzeug (oder jedem anderen Standard-Werkzeug) auf dieser Ansicht arbeiten können, so dass Sie Texte, Bemaßungen, Symbole, etc. hinzufügen können.

<img alt="" src=images/Arch_tutorial_50.jpg  style="width:1024px;">

Auf dem obigen Bild wurden zwei [Draft Form zu 2D-Ansichten](Draft_Shape2DView/de.md) für jeden Schnitt erstellt, eine, die alles zeigt, und eine andere, die nur die Schnittlinien zeigt. Dies erlaubt uns, andere Linienbreiten und Schraffuren einzustellen. Dann wurden Bemaßungen, Texte und Symbole hinzugefügt und eine Reihe von DXF-Blöcken für die Darstellung von Möbeln importiert. Diese Ansichten können dann einfach nach DXF oder DWG exportiert und in Ihrer bevorzugten 2D-CAD-Anwendung geöffnet werden, wie [LibreCAD](http://www.librecad.org) oder [DraftSight](http://www.3ds.com/products-services/draftsight/overview/), wo Sie weiter daran arbeiten können:

<img alt="" src=images/Arch_tutorial_51.jpg  style="width:1024px;">

Beachten Sie, dass einige Merkmale noch nicht vom [DXF/DWG-Exporter](Draft_DXF/de.md) unterstützt werden, so dass das Ergebnis in Ihrer 2D-Anwendung ein wenig abweichen kann. Beispielsweise musste ich im obigen Bild die Schraffur neu erstellen und die Position einiger Bemaßungstext korrigieren. Wenn Sie Ihre Objekte in FreeCAD in verschiedenen Gruppen ablegen, dann werden diese in Ihrer 2D-Anwendung zu Ebenen (layers).

**ArchViews**

The other kind of output that can be produced from [section planes](Arch_SectionPlane.md) are [TechDraw ArchViews](TechDraw_ArchView.md). This method has one big limitation compared to the previous one: you have limited possibilities to edit the results, and at the moment, things like dimensioning or hatching are still not natively supported.

Auf der anderen Seite ist das endgültige Ergebnis einfacher zu handhaben und die grafischen Möglichkeiten des SVG-Formats sind riesig, so dass dies in Zukunft die bevorzugte Methode sein wird. Momentan bekommen Sie allerdings mit der ersten die besseren Ergebnisse.

<img alt="" src=images/Arch_tutorial_52.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Im obigen Bild ist die Geometrie die direkte Ausgabe der Schnittebene, aber einige andere Draft-Objekte wie Bemaßungen und Schraffur-Polygone wurden hinzugefügt und ein anderes Ansichtsobjekt mit gleichem Maßstab und Abstandswerten wurde mit dem [Draft-Zeichnung](Draft_Drawing/de.md)-Werkzeug erstellt. Zukünftig werden solchen Operationen direkt auf der Zeichenseite möglich sein, so dass das Modell davon frei sein wird.


</div>



### Mengenermittlung

Dies ist ebenfalls eine sehr wichtige Aufgabe, die bei Modellen der Gebäudedatenmodellierung auszuführen ist. In FreeCAD ist von Anfang an alles dafür vorhanden. Der OpenCasCade-Kernel von FreeCAD kümmert sich bereits um die Berechnung von Längen, Flächen und Körpern bei allen Formen, die erstellt werden. Da alle [Arch](Arch_Workbench/de.md)-Objekte \"solide\" sind, können Sie sicher sein, Sie daraus Körper erzeugen können.

**Tabellen benutzen**

Zur Füllung einer Kalkulationstabelle mit Werten aus dem Modell kann das [Arch Ablaufplan](Arch_Schedule/de.md)-Werkzeug benutzt werden.

![](images/Arch_schedule_example03.jpg )

**Der Überprüfungsmodus**

Ein weiterer Weg, Ihr Modell zu überprüfen und Werte zu ermitteln, ist der [Überprüfungs](Arch_Survey/de.md)-Modus. In diesem Modus können Sie auf Punkte, Kanten, Flächen klicken oder doppelklicken, um ganze Objekte zu wählen, und Sie erhalten Höhe, Länge, Fläche oder Körperinhalte, angezeigt im Modell, im FreeCAD-Ausgabefenster ausgedruckt und in die Zwischenablage kopiert, so dass Sie einfach die Werte in andere geöffnete Anwendungen übernehmen können.

<img alt="" src=images/Arch_tutorial_54.jpg  style="width:1024px;">



## Abschluss

Ich hoffe, dies gibt Ihnen einen guten Überblick über die verfügbaren Werkzeuge. Sehen Sie sich auch die Dokumentation zum [Arch](Arch_Workbench/de.md)- und [Draft](Draft_Workbench/de.md)-Arbeitsbereich und anderen an (es gibt weitere Werkzeuge, die ich hier nicht erwähnt habe), und allgemein den Rest der [FreeCAD-Dokumentation](Main_Page/de.md). Besuchen Sie auch das [Forum](http://forum.freecadweb.org), denn viele Probleme können dort umgehend gelöst werden und folgen Sie meinem [Blog](http://yorik.uncreated.net/guestblog.php?tag=freecad), um Neuigkeiten über die Arch-Arbeitsbereich-Entwicklung zu erfahren.

Die in diesem Tutorial erzeugten Dateien finden Sie [hier](http://yorik.uncreated.net/archive/projects/casa_artigas.fcstd).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch tutorial/de
