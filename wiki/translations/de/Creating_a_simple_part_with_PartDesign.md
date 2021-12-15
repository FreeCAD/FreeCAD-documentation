# Creating a simple part with PartDesign/de
{{TutorialInfo/de
|Topic=Modellierung
|Level=Anfänger
|Author=GlouGlou
|Time=1 Stunde
|FCVersion=0.17 or above
|Files=[https://github.com/FreeCAD/Examples/blob/master/Creating_a_simple_PartDesign_Body.FCStd Creating a simple PartDesign Body.FCStd]
}}

![](images/GGTuto1_Vue.PNG )

Dieses Tutorial soll FreeCAD Anfängern anhand eines Beispiels einige grundlegende Funktionen vermitteln. Nachdem die Grundlagen im [User hub/de](User_hub/de.md) behandelt wurden, wirst Du in der Lage sein, Schritt für Schritt ein erstes Teil zu modellieren.

**Wir werden in diesem Tutorial vor allem folgendes behandeln:**

-   Verwenden des [Part Design Arbeitsbereich](PartDesign_Workbench/de.md), nachzeichnen der Skizze.
-   Verwenden von Polster- und Taschen -Formelementen.
-   Ändern von Farbe und Transparenz.
-   Manuelles Verschieben des Teils.
-   Anzeige von Referenzabmessungen in der Skizze.
-   Bearbeiten einer oder mehrerer Abmessungen.
-   Verwenden von äußeren Geometrie Formelementen und Verwendung einer Referenzebene zum Zentrieren einer Bohrung.

### Verwenden des [Part Design Arbeitsbereich](PartDesign_Workbench/de.md) nachverfolgen der Skizze 

Erstelle ein neues Dokument und wechsle in den **<img src=images/Workbench_PartDesign.svg style="width:24px"> '''Part Design Arbeitsbereich'''** entweder mit dem [Arbeitsbereich Wahlschalter](Getting_started#Exploring_the_interface/de.md) (im verknüpften Bild mit 10 beschriftet) oder über das Menü *Ansicht → Arbeitsbereich*. FreeCAD startet mit den Werkzeugleisten oben, die Comboansicht links und der 3D Ansicht rechts.

**Erstelle Körper:**

Drücke <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [/de\|Körper erstellen](PartDesign_Body.md). **Hinweis:** verwechsle nicht den Körper, dessen Symbol blau ist, mit dem Part Behälter, dessen Icon gelb ist.\'\' Im Modell Reiter unter der Combo Ansicht Sidebar erscheint ein neues Objekt mit der Bezeichnung \"Körper\" unter der Dokumentbezeichnung, das derzeit \"Unnamed\" ist, da wir unser Dokument noch nicht gespeichert haben. Der Körper ist ein Behälter, in dem die PartDesign Formelemente nacheinander angeordnet werden, um einen einzelnes Festkörper zu bilden. Er enthält seine eigenen Referenzachsen und -ebenen. Er wird im Modellbaum hellblau hervorgehoben, was bedeutet, dass er aktiv ist, d.h. wir können die darin enthaltenen Elemente bearbeiten und neue Elemente hinzufügen. Wenn er nicht hervorgehoben ist, doppelklicke darauf oder klicke mit der rechten Maustaste und wähle *Aktiven Körper umschalten* im Kontextmenü. Vor dem Körper Schild befindet sich ein blaues Symbol, das mit dem obigen identisch ist, sowie ein Pfeil oder ein Pluszeichen, je nach Betriebssystem. Ein Klick auf den Pfeil oder das Pluszeichen vor dem Körper erweitert den Inhalt. Er enthält an dieser Stelle nur ein Element mit der Bezeichnung *Origin*. Vor diesem *Ursprung* befindet sich ebenfalls ein Pfeil oder ein Pluszeichen. Klicke darauf, um den Inhalt zu erweitern. Es zeigt die oben genannten Bezugsachsen und -ebenen, wie im Bild unten dargestellt:

![](images/PartDesign_Body_tree_Unnamed.png ) *Der neu geschaffene aktive Körper mit seinem Inhalt erweitert.*

Der *Ursprung* ist ausgegraut, was bedeutet, dass sein Inhalt in der 3D Ansicht nicht sichtbar ist. Du kannst den Inhalt von *Origin* in der 3D Ansicht sichtbar machen, indem Du *Origin* auswählen und die Leertaste auf Ihrer Tastatur drückst. Origin\" wird nun schwarz im Baum angezeigt. Drücke erneut die Leertaste, um den Inhalt in der 3D Ansicht auszublenden. Klicke erneut auf den Pfeil oder das Pluszeichen vor *Ursprung*, um den Inhalt im Modellbaum auszublenden.

Bevor wir fortfahren, wollen wir die Gelegenheit nutzen, den Körper umzubenennen.

**Körper umbenennen:**

Klicke im Modellbaum mit der rechten Maustaste auf den Körper. Wähle Umbenennen und gib einen Namen ein, z.B. \"Körper Teil1\" und drücke **Enter** zur Bestätigung.

**Erstelle Skizze:**

Wir werden nun die Skizze aufzeichnen, die die allgemeine Form des Teils definiert. Eine Skizze ist ein Diagramm, das ein Profil beschreibt, das auf ein Formelement angewendet werden soll, um eine Form zu erzeugen. Es kann entweder \"positiv\" oder \"additiv\" sein, wie z.B. ein Polster; oder \"negativ\" oder \"subtraktiv\", wie eine Tasche.

Da die allgemeine Form des Bauteils entlang der Y Achse regelmäßig ist, werden wir das Polster entlang dieser Achse erzeugen.

Drücke <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Neue Skizze](Sketcher_NewSketch/de.md). Die Combo Ansicht wechselt nun zur **Aufgaben** Registerkarte und zeigt das *Formelement auswählen* Dialogfeld an. Dieser Dialog erwartet die Auswahl einer Ebene, an die unsere Skizze angefügt werden soll, und listet die verfügbaren Ebenen auf. Wähle *XZ\_Ebene (Basisebene)* und drücke **OK**. Die Benutzeroberfläche ändert sich nun, der Skizzenzeichner übernimmt nun und seine Symbolleisten erscheinen über der 3D Ansicht. Wir befinden uns nun auf der XZ Ebene des Körpers, um die Skizze zu zeichnen.

Um das Skizzieren zu erleichtern, stellen Sie die folgenden Optionen unter \"Steuerelemente bearbeiten\" im Aufgabenpaneel auf der linken Seite ein:

-   Gitter anzeigen: aktiviert.
-   Rastermaß: 10 mm
-   Auto Beschränkungen: aktiviert

Wir werden die folgende Skizze nachzeichnen:

![](images/GGTuto1_0.PNG )

\"Fangen wir mit den ersten Abschnitten an:

Wähle die Datei <img alt="" src=images/Sketcher_Line.svg  style="width:24px;"> [Linie](Sketcher_CreateLine/de.md) Werkzeug. Klicke auf den Ursprungspunkt, wobei Du zunächst darauf achten musst, dass neben und rechts vom Mauszeiger ein kleiner roter Punkt erscheint. Klicke als nächstes auf die X Achse etwa 10 Quadrate nach rechts oder bei etwa 100 mm. Wenn das Segment an diesem Punkt nicht genau 100 mm ist, spielt es keine Rolle, wir geben ihm später ein festes Maß, das diese Länge beschränkt.

Mache das gleiche für die anderen Abschnitte, versuche auf die von dir erstellten Punkte zu zielen, die gelb aufleuchten müssen. Das bedeutet, dass diese Punkte zusammenfallen werden. Du solltest so ziemlich das hier bekommen:

![](images/GGTuto1_1.PNG )

Beachte die kleinen roten Linien über und neben den von Ihnen gezeichneten Segmenten: dies sind horizontale und vertikale Beschränkungen. Ihre Linien sind gezwungen, entweder horizontal oder vertikal zu bleiben. Beachte auch das Symbol in Form eines kleinen Bogens auf der linken Seite: es bedeutet, dass der Punkt an der Z Achse fixiert ist.

Wähle nun mit der linken Maustaste verschiedene Linienabschnitte aus und versuche bei gedrückter linker Taste mit der Maus zu verschieben: einige sind frei, andere nicht.

**Anwendung von Beschränkungen:**

Oben im Combo-Feld, im Aufgabenpaneel, kannst Du die Anzahl der Freiheitsgrade der bereits skizzierten Elemente ablesen: sie muss etwa 6 betragen, die Zielsetzung der Beschränkungen ist es, die Anzahl der Freiheitsgrade auf 0 zu reduzieren.

Die schräge Linie sollte sich zu diesem Zeitpunkt frei drehen können: wir geben ihr eine Winkelbeschränkung, um sie zu fixieren. Drücke \"ALT-UMSCHALT-S\", um zu speichern, oder \"ALT-UMSCHALT-D\", um zur nächsten Meldung zu springen, oder \"ALT-UMSCHALT-B\", um eine Zusammenfassung zu erhalten, oder \"ALT\" für andere Verknüpfungen. Dokumentation hinzufügen

Klicke auf die schräge Linie, dann auf die untere Linie; sobald diese Linien ausgewählt sind, werden sie dunkelgrün; dann klicke auf die <img alt="" src=images/Constraint_InternalAngle.svg  style="width:24px;"> [Beschränke Innenwinkel](Sketcher_ConstrainAngle.md) Symbol.

![](images/GGTuto1_2.PNG )

Gib einen Wert von 30° ein. Beide Linien haben nun einen festen Winkel. Die Zwangsbedingung wurde links von der Skizze erstellt; bewege sie mit der Maus innerhalb des Profils.

Wir werden nun die untere Linie mit einer Bemaßung beschränken: Wähle diese aus und klicke auf <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:24px;"> [Beschränke Horizontalen Abstand](Sketcher_ConstrainDistanceX/de.md).

Gib einen Wert von 100 mm ein. Die senkrechte Linie auf der rechten Seite richtet sich nun genau auf das 10. Quadrat des Gitters rechts vom Ursprung aus.

Lass uns die Gesamthöhe auf das Profil einstellen, indem wir den höchsten Punkt links und dann den Ursprungspunkt auswählen. Klicke auf <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:24px;"> [Beschränke vertikalen Abstand](Sketcher_ConstrainDistanceY.md), gib einen Wert von 50 mm ein.

Mach das selbe für die horizontale Länge der Schräglinie mit einer weiteren horizontalen Abstandsbeschränkung von 50 mm.

Verschiebe die Abmessungen zur besseren Sichtbarkeit vom Profil weg. Sie sollten jetzt so etwas wie das hier haben:

![](images/GGTuto1_3.PNG )

Beachte, dass sich die Anzahl der Freiheitsgrade auf 2 reduziert hat. Dies sind die noch offenen Enden.

**Den Bogen nachzeichnen**

Klicke auf <img alt="" src=images/Sketcher_Arc.svg  style="width:24px;"> [Bogen](Sketcher_CreateArc/de.md), positioniere den Mittelpunkt auf ungefähr x = 80 y = 30; klicke dann, um den ersten Startpunkt des Bogens auf dem rechten Endpunkt der oberen horizontalen Linie zu definieren; klicke dann, um das Ende des Bogens auf den oberen Endpunkt der rechten vertikalen Linie zu definieren (stelle sicher, dass die Punkte gelb markiert sind, bevor Du klickst).

Gib dem Radius eine Radiusbeschränkung: Wähle den Bogen aus und klicke dann auf <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Beschränke Radius](Sketcher_ConstrainRadius.md) gib dann einen Wert von 20 mm ein.

Jetzt machen wir den Bogen tangential zu den Linien, mit denen er verbunden ist: Wähle den Bogen, dann die oberste Zeile, dann klicke auf <img alt="" src=images/Constraint_Tangent.svg  style="width:24px;"> [Beschränke Tangente](Sketcher_ConstrainTangent/de.md). Eine *Beschränkungsersetzung* Meldung erscheint, klicke auf **OK**. Machen dasselbe für die Tangentialbeschränkung auf der anderen Seite des Bogens.

Wir sind in zwei Schritten vorangeschritten, um die Skizze zu erstellen, aber wir hätten das Profil auch komplett nachzeichnen können, bevor wir es vollständig begeschränkt haben.

**Vollständige beschränkte Skizze:**

Wenn du gut gearbeitet hast, solltest du das hier erhalten:

![](images/GGTuto1_4.PNG )

Die Skizze ist grün geworden, was bedeutet, dass sie vollständig begeschränkt ist. Es gibt keine Unklarheiten mehr, alles ist perfekt definiert. Dies wird durch die Löser Meldung oben links bestätigt. Beachte auch, dass sich der Mittelpunkt des Bogens leicht verschoben hat, da FreeCAD die wahre Position des Mittelpunktes berechnet hat:

Wenn deine Skizze noch nicht grün ist, sind ein oder mehrere Punkte nicht deckungsgleich (2 Punkte können übereinander gelegt werden, aber nicht deckungsgleich sein). Erstelle ein kleines Fenster (Fang Fenster) um einen zu selektierenden Punkt und erstelle eine <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:24px;"> [Deckungsgleich Bedingung](‎Sketcher_ConstrainCoincident/de.md). Hinweis: Verwechsledie Deckungsgleich Bedingung nicht mit dem Skizzenpunkt; während ihre Symbole sehr ähnlich sind, hat letzterer ein größeres Symbol; es fügt einen einzelnen Punkt in der Skizze hinzu.

Gehe bei allen Punkten auf die gleiche Weise vor.

Wenn deine Skizze immer noch nicht grün ist, überprüfe, ob alle Linien (außer der schrägen) entweder ein <img alt="" src=images/Constraint_Horizontal.svg  style="width:24px;"> _ und füge, wenn nötig, eine Beschränkung hinzu.

### Verwendung der Polster- und Taschen Formelemente 

Klicke auf **Close** in der Aufgaben Registerkarte oben links in der Ecke. Wir verlassen automatisch den Skizzierer Arbeitsbereich, und den Part Design Arbeitsbereich wird wieder aktiviert. Die Combo Ansicht schaltet wieder auf die Modell Registerkarte um. Wenn Du dein *Körper Teil1* aufgeklappt gelassen hast, siehst Du ein neues **Skizzen**-Element unter *Ursprung* und unter dem Körper verschachtelt.

Lass uns an dieser Stelle unser Dokument speichern. Gib ihm einen Namen (z.B. "Tutorium1", oder einen beliebigen Namen, den Du relevant findest). Es ist eine bewährte Vorgehensweise, das Dokument oft zu speichern, z.B. nach der Fertigstellung einer Skizze oder eines Formelementes.

Klicke auf <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> **Isometrische Ansicht** dann <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [Alles einpassen](Std_ViewFitAll/de.md), was eine zentrierte isometrische 3D-Ansicht liefert.

Klicke auf <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Polster](PartDesign_Pad/de.md), gib eine Länge von 30 mm ein. Klicke auf **OK**, die Form ist fertig gestellt. In der Modellstruktur wird anstelle der Skizze ein **Pad** Objekt (das wir Formelement nennen) eingeblendet. Tatsächlich hat es die Skizze übernommen, da es auf ihr basiert; wenn Du auf den Pfeil oder das Pluszeichen vor *Pad* klickst, um sie zu erweitern, wird die darunter liegende Skizze angezeigt, die automatisch ausgeblendet wurde (ihre Beschriftung ist grau).

Beachte, dass die erzeugte Form einen Festkörper bildet.

![](images/GGTuto1_5.PNG )

**Das Loch erzeugen**

Klicke auf die obere (quadratische) Seite des Teils und klicke auf das <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> Symbol, um eine neue Skizze zu erstellen. FreeCAD erzeugt eine neue Skizze, die an diese Fläche angefügt wird. Wir befinden uns also auf einer Ebene, die parallel zur absoluten Ebene XY, aber in der Höhe versetzt ist zur Höhe des Teils, d.h. 50 mm.

Du kannst das 3D Fenster in eine isometrische Ansicht umschalten <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> oder in der Draufsicht bleiben <img alt="" src=images/Std_ViewTop.svg  style="width:24px;">. Jederzeit kannst Du zur Skizzenansicht zurückkehren (die Ansicht ist gegenüberliegend zur Skizzierebene ausgerichtet), unter Verwendung des <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:24px;"> [Sketcher ViewSketch/de](Sketcher_ViewSketch/de.md) Symbols.

Beachte, dass der Ursprung dieser neuen Skizze der des Körpers ist. Sie mögen unterschiedlich sein, aber hier vermengt mit dem exakten Ursprung.

Mit dem <img alt="" src=images/Sketcher_Circle.svg  style="width:24px;"> [ Kreis](Sketcher_CreateCircle/de.md) Werkzeug ungefähr in die Mitte der Fläche klicken und einen Kreis mit beliebigem Radius erstellen.

Wähle den Kreis aus und erstelle eine <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Radius Beschränkung](Sketcher_ConstrainRadius/de.md), gib einen Wert von 5 mm ein.

Wähle den Mittelpunkt des Kreises aus und erstelle eine <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sperr Beschränkung](Sketcher_ConstrainLock/de.md); doppelklicke auf die horizontale Bemaßung und gib -65 mm ein (hier geben wir eine Position relativ zum Ursprung der Skizze an). Mache dasselbe für die vertikale Bemaßung (-15 mm). Der Kreis nimmt seine korrekte Position ein und die Skizze wird grün und zeigt damit an, dass sie vollständig beschränkt ist:

![](images/GGTuto1_6.PNG )

Schließe die Skizze; im Modellbaum ist unter Pad ein neues **Sketch001** Objekt erschienen. Klicke, während Sketch001 noch ausgewählt ist, auf <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Tasche](PartDesign_Pocket.md).

Pocket ist ein Formelement \"subtraktiv\" genannt, es entfernt Material von unserem Teil, hier in der Form eines Zylinders, da die Skizze ein Kreis ist. Stelle \"Durch alles\" ein, um das Teil vollständig auszuschneiden. Drücke **OK**, um den Vorgang abzuschließen. Im Modellbaum erscheint ein neues Element mit der Bezeichnung **Pocket** am unteren Ende des Körper Teil1 und belegt Sketch001.

### Ändern von Farbe und Transparenz 

Es ist möglich, die Farbe des Teils zu ändern, es ist oft nützlich, ein Teil unter anderen zu unterscheiden. Auch die Transparenz des Teils kann verändert werden, was für die Anzeige seines Inneren nützlich ist.

Wähle den **Body part1** Körper; stelle sicher, dass der Modellreiter der Combo Ansicht ausgewählt ist und gehe zum unteren Teil der Combo Ansicht, dann klicke auf den Ansichtsreiter; suche die *Form Farbe* Eigenschaft; möglicherweise musst Du die vertikale Bildlaufleiste auf der rechten Seite verwenden, um sie zu finden. \'\'Du kannst auch die Eigenschaftsspalte verbreitern: Fahre mit dem Mauszeiger über die Trennlinie zwischen den Kopfzeilen *Eigenschaft* und *Wert*; wenn sich der Zeiger in einen doppelseitigen Pfeil verwandelt, drücke und halte die linke Maustaste und ziehe seitlich, dann lasse sie los. Klicke in der rechten Spalte auf das graue Quadrat, was den *\'Farbe auswählen* Dialog öffnet. Wähle eine andere Farbe aus und klicke dann auf OK. Als nächstes ändere wiederum in der Ansichts Registerkarte den Wert für \"Transparenz\", z. B. auf 50 und drücke **Enter**, um den Vorgang abzuschließen (0 = völlig deckend, 100 = völlig transparent).

Die Bohrung ist nun im Inneren des Teils sichtbar. Dies ist oft nützlich, um die verborgenen oder inneren Flächen des Modells zu sehen.

Du kannst auch \"Linienfarbe\" und \"Linienbreite\" variieren, um die Linienstärke und die Farbe der Teilekontur zu ändern.

### Manuelles Bewegen des Teils 

Gehe in das Menü *Ansicht* und wähle *Achsenkreuz umschalten*. Dies sind die absoluten Achsen. Du solltest in der 3D Ansicht die 3 Achsen X, Y, Z in rot, grün und blau sehen. Diese Orientierungsmarke wird uns helfen, uns im Raum zu orientieren. Diese Orientierungsmarke ist fest und unveränderlich, es ist entweder die Ansicht, die sich dreht oder das Objekt, das sich in diesem Raum dreht.

Wähle den Körper aus; unten in der Combo Ansicht auf der linken Seite kannst du dies sehen (der *Daten* Reiter muss im Vordergrund sein, du musst eventuell auf den *Daten* Reiter klicken, um ihn sichtbar zu machen):

![](images/GGTuto1_10.PNG )

Klicke auf die drei kleinen Punkte, z. B. die Auslassungspunkte (wenn sie nicht erscheinen, klicke auf den Wert Abschnitt des Feldes **Platzierung**); dies öffnet einen neuen Dialog im Aufgaben Paneel. Mit Hilfe der Pfeile kannst Du die Position und die Winkel des Teils variieren. Es ist tatsächlich die Position des Körpers (also sein Ursprung), die sich im Raum bewegt, die Ausrichtung der 3D Ansicht ändert sich nicht.

Eine andere Methode: In der Combo Ansicht wähle den Körper aus und klicke mit der rechten Maustaste, dann wähle *Transformieren*. Es erscheint eine Ansicht wie diese:

![](images/GGTuto1_11.PNG )

Halte und ziehe die Kegel entlang der Achsen oder der Kugeln, um den Körper in alle Richtungen zu bewegen.

Bestätige. Dann setze Winkel und Koordinaten auf 0 zurück.

### Anzeigen der Referenzmaße in der Skizze 

Es kann nützlich sein, die Abmessungen einiger Teile der Skizze aus der internen Berechnung von FreeCAD zu kennen. Sie können nur als Referenz verwendet werden, oder sie später z.B. für andere Bemaßungen verwenden.

Im Modellbaum, wenn nötig ggf. *Körper Teil1* und dann *Polster* aufklappen, um die erste Skizze anzuzeigen. Doppelklicke darauf (oder klicke mit der rechten Maustaste und wähle *Skizze bearbeiten* im Kontextmenü) und klicke dann auf <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:24px;"> [Umschalten Beschränkung](Sketcher_ToggleDrivingConstraint/de.md). (**Hinweis:** abhängig von der Bildschirmauflösung Deines Computers ist dieses Symbol möglicherweise nicht sichtbar. Am rechten Ende der Werkzeugleiste Beschränkungen findest Du möglicherweise eine **»** Taste. Klicke darauf, um die Symbole aufzuklappen und auf zugeklappte Symbole zuzugreifen). Von nun an können wir Referenzbemaßungen anstelle von Abmessungsbeschränkungen erstellen: sie werden blau sein und haben keinen Einfluss auf die Formen der Skizze, aus der sie stammen, sie werden automatisch berechnet.

Du kannst diese Abmessungen anzeigen lassen zum Beispiel:

![](images/GGTuto1_7.PNG )

Wir können zum Beispiel sehen, dass der Bogen eine Länge von 20 hat, da er tangential zu den Kanten verläuft.

Wir können auch sehen, dass FreeCAD die linke Fläche (50-50xTAN 30 °) berechnet, sowie das Abstandsmaß der Achse des Bogens zum Ursprung.

### Bearbeitung einer oder mehrerer Abmessungen 

Während der Modellierung kannst Du die Abmessungen des Modells variieren. Es ist sehr einfach: Für die Dicke des Teils doppelklicke auf Pad und gib dann einen neuen Wert ein, z.B. 40mm. Im unteren Teil der Combo Ansicht kannst Du diesen Wert ebenfalls ändern. Überprüfe, die Form des Objekts hat sich geändert.

Mache dasselbe für die Gesamtlänge des Stücks: Doppelklicke auf Skizze, dann doppelklicke auf die 100 mm Bemaßungsbeschränkung, ändere sie auf 110 mm und bestätige.

Wir können sehen, dass das Stück vergrößert wurde, aber die Bohrung nicht mehr in der Mitte der Oberseite zentriert ist. Das liegt daran, dass es auf den Skizzenursprung beschränkt wurde. Was nicht unbedingt dem entspricht, was man sich wünscht, die Bohrung sollte in der Mitte bleiben, unabhängig von der Größe der Fläche.

### Zentrieren der Bohrung 

**Erste Methode mit externer Geometrie.**

Bearbeite erneut die Skizze der Bohrung und lösche die horizontalen und vertikalen Abstandsbeschränkungen.

Dann klicke auf <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Externe Geometrie](Sketcher_External/de.md).

Wir werden nun zwei Linien in der Skizze erstellen, die jedoch aus einer externen Form (oder einem Formelement) zu dieser entnommen, und zuvor definiert wurden: die des Polsters.

Klicke auf eine vertikale Kante auf der Oberseite des Teils. Zum Beispiel die Seite der Kantenschräge.

Eine neue magentafarbene Linie erscheint über dem Rand. Wiederhole dies für die andere Kante, auf der abgerundeten Seite.

Wir können diese Linien (und vor allem ihre Endpunkte) nun zur Zentrierung des Kreises verwenden, allerdings müssen wir zwei Konstruktionslinien hinzufügen: zum Beispiel die Diagonalen.

Klicke auf <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> [Konstruktionsmodus](Sketcher_ToggleConstruction/de.md), wir wechseln in den Konstruktionsmodus: die Linien werden blau und außerhalb des Skizzenbearbeitungsmodus verworfen. Sie erlauben es, den Mittelpunkt des Kreises zu fixieren. Erstelle die Diagonalen auf die gleiche Weise, wie Du die ersten Linien gezeichnet haben. Stelle sicher, dass alle Punkte deckungsgleich sind.

Wähle dann den Mittelpunkt des Kreises, dann die beiden blauen diagonalen Linien und klicke auf <img alt="" src=images/Constraint_PointOnObject.svg  style="width:24px;"> [Punkt auf Objekt](Sketcher_ConstrainPointOnObject.md), der Kreis muss am Schnittpunkt der Diagonalen, also in der Mitte der Fläche zentriert werden. Die Skizze muss grün, vollständig beschränkt sein (es ist unerlässlich). Beachte, dass es neben dem Radius des Kreises, nicht mehr erforderlich ist, Bemaßungsbeschränkungen zu erstellen.

Bitte beachte , dass zusätzlich zum Umschalten der Symbolleiste in den Konstruktionsmodus die Datei <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> [Sketcher\_Konstruktionsmodus umschalten](Sketcher_ToggleConstruction/de.md) Taste können auch einzelne Skizzierer Elemente in den Konstruktionsmodus geschaltet werden, wenn sie ausgewählt wurden. Wenn du versehentlich ein Element in den Konstruktionsmodus schaltest, kann beim Verlassen der Skizze ein Fehler auftreten.

![](images/GGTuto1_8.PNG )

Verlasse die Skizze, wir sehen, dass der Kreis genau zentriert ist. (Das Taschen Formelement wurde nicht gelöscht, sondern modifiziert). Wenn Du die Bemaßungen des Teils erneut änderst, die Dicke oder die Länge, bleibt der Kreis auf der Fläche zentriert.

**Vermeide Konstruktionslinien:**

Oftmals kann auf das Anlegen von Konstruktionslinien verzichtet werden. Du kannst die Skizze erneut bearbeiten, die Konstruktionslinien löschen und eine <img alt="" src=images/Constraint_Symmetric.svg  style="width:24px;"> [Symmetrie Beschränkung](Sketcher_ConstrainSymmetric/de.md) zwischen den beiden gegenüberliegenden Eckpunkten der äußeren Geometrielinien und dem Mittelpunkt des Kreises verwenden (wähle die Punkte in dieser Reihenfolge aus):

![](images/GGTuto1_12.PNG )

Wir erhalten genau das gleiche Ergebnis für die Position der Bohrung. Tatsächlich gibt es dank der im Skizzierer Arbeitsbereich verfügbaren Beschränkungen viele mögliche Methoden. Dieses Beispiel zeigt, dass es oft besser ist, die einfachste Methode zu wählen, wodurch die Anzahl der erzeugten Objekte und die daraus resultierenden Fehler begrenzt werden.

**Zweite Methode unter Verwendung einer Bezugsebene.**

Hier ist eine weitere, schnellere Methode, die seit Version 0.17 möglich ist: die Verwendung einer Bezugsebene und deren Anbindung.

Beginne mit dem Löschen der \"Taschen\" Funktion sowie der Skizze der Bohrung. Wähle die obere Fläche und klicke <img alt="" src=images/PartDesign_Point.svg  style="width:24px;"> [Bezugspunkt](PartDesign_Point/de.md): Erzeuge einen Bezugspunkt im aktiven Körper. Der gewählte Anfügemodus muss \"Massenschwerpunkt\" sein.

Da die Fläche rechteckig ist, entspricht ihr Massenschwerpunkt dem Mittelpunkt ihrer Diagonalen. Bestätige, und ein Bezugspunkt wird erstellt.

Wähle die obere Fläche erneut aus und während Du die STRG Taste gedrückt hälst, wähle den soeben erstellten Punkt im Modellbaum aus, lasse die STRG Taste los und klicke <img alt="" src=images/PartDesign_Plane.svg  style="width:24px;"> [Bezugsebene](PartDesign_Plane/de.md). Eine Referenzebene wird mit dem Ursprung des Punktes erzeugt. Klicke auf OK.

Es ist jetzt sehr einfach, den Kreis zu zentrieren! Wähle aus dem Modellbaum oder in der 3D Ansicht die von Dir erstellte Ebene aus und klicke auf <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Skizze erstellen](Sketcher_NewSketch/de.md), wird eine Skizze mit dem Ursprung der Ebene als Ursprung erstellt. Dann zeichne einfach den Kreis mit einem Radius von 5 mm auf diesem Ursprung ab und prüfe dann (die Skizze muss unbedingt grün sein).

Du erhälst mit \"Tasche\", wie zuvor erstellt, die Bohrung und sie wird immer zentriert sein.

![](images/GGTuto1_9.PNG )

Dieses Tutorial ist abgeschlossen, speichere diese Datei, dann kannst Du die verschiedenen Funktionen erkunden. Ändere andere Abmessungen, mache andere Formen, setze andere Löcher auf andere Flächen, erst wenn wir Fehler machen, kommen wir weiter!

Du kannst auch mit diesem anderen Tutorial eines etwas komplizierteren Teils fortfahren:

[Erstellen eines einfachen Bauteils mit PartDesign](Basic_Part_Design_Tutorial/de.md)


{{Tutorials navi

}} {{PartDesign Tools navi}} {{Sketcher Tools navi}}

---
[documentation index](../README.md) > Creating a simple part with PartDesign/de
