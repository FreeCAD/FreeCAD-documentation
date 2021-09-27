---
- GuiCommand:/de
   Name:Sketcher External
   Name/de:Skizzierer Extern
   MenuLocation:Skizze → Skizzengeometrien → Skizzierer Extern
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:X
   SeeAlso:[KonstructionsModus](Sketcher_ToggleConstruction/de.md)
---

# Sketcher External/de

## Beschreibung

Verwende das **<img src="images/Sketcher_External.svg" width=16px> [Externe Geometrie](Sketcher_External/de.md)** Werkzeug wenn Du eine Beschränkung zwischen der Skizzengeometrie und etwas außerhalb der Skizze anwenden möchtest. Es funktioniert, indem eine verknüpfte Konstruktionsgeometrie in die Skizze eingefügt wird. Die Standardfarbe der extern verbundenen Kanten ist Magenta. Wie bei der standardmäßigen unverknüpften Konstruktionsgeometrie (blau) ist die extern verknüpfte Geometrie nur sichtbar, wenn sich die Skizze im Bearbeitungsmodus befindet und nicht direkt im späteren Ergebnis aus der Verwendung der Skizze in einem anderen Werkzeug verwendet wird. Beide Arten von Konstruktionsgeometrien können als Referenz für Beschränkungen innerhalb der Skizze verwendet werden.

Ein Hinweis zur Vorsicht, die Verwendung dieses Werkzeugs zur Verknüpfung mit generierter (Volumen) Geometrie kann aufgrund des _.

<FILE:Sketcher_ExternalEsempio1.png>

## Anwendung

-   Erstelle eine neue Skizze oder öffne eine bestehende Skizze.
-   Klicke auf die \"Skizzierer Extern\" Schaltfläche
-   Wähle eine Kante oder einen Knoten aus, auf den Du in der Skizze verweisen möchtest.
-   Drücke Esc oder wähle ein anderes Werkzeug, um den Import von Geometrien in die Skizze zu beenden.

### Auswahlregeln

-   Es sind nur Kanten und Knoten von Objekten aus demselben Koordinatensystem zulässig.

Das heißt, die Skizze und das Objekt müssen sich im gleichen Körper (Wenn im PartDesign Arbeitsbereich), oder im gleichen Teil (Wenn im Part Arbeitsbereich), oder beide außerhalb von Teilen und Körpern befinden.

Wenn sich die offene Skizze beispielsweise im Körper befindet, kannst du eine andere Skizze aus dem Körper als externe Geometrie verwenden, aber du kannst keine Skizze aus dem Körper001 oder eine Kante aus einem Teilewürfel im Wurzelbereich des Projekts verwenden. Verwende die Funktion Formbinder, um eine Kopie des Objekts in das Koordinatensystem der offenen Skizze einzubringen. Dann kannst du Kanten/Eckpunkte des Formbinderobjekts verwenden.

-   Rekursive Abhängigkeiten sind nicht erlaubt.

Das bedeutet, dass du nicht auf Taschen verweisen kannst, die mit dieser Skizze erstellt wurden. Du kannst nicht auf jedes Objekt verweisen, das von der Skizze abhängt.

Die Skizze muss sich nicht auf einer Fläche befinden, um dieses Werkzeug zu nutzen. Direkte Verbindungen zwischen Skizzen sind möglich und erwünscht, da sie zuverlässiger sind.

### Erscheinen bei erfolgreicher Verknüpfung 

Eine (standardmäßig magentafarbene) farbige Linie wird überlagert, wenn eine Kante erfolgreich verknüpft ist (die Knoten sind rot), und ist in deiner Skizze nur sichtbar, wenn sich deine Skizze im Bearbeitungsmodus befindet.

### Ähnlichkeit mit Konstruktionslinien 

Äußere Geometrielinien (Standardfarbe Magenta) sind ähnlich (Standardfarbe Blau) [Konstruktionslinien](Sketcher_ToggleConstruction/de.md), mit der Ausnahme, dass die äußeren Geometrielinien Magentalinien parametrisch mit einem Element des Körpers verknüpft sind, auf den die Skizze abgebildet ist. Konstruktionsgeometrie sind Linien, die sich innerhalb der Skizze befinden, nur sichtbar sind, wenn sich die Skizze im Bearbeitungsmodus befindet, und nur für Zwangsbeschränkte Referenzen verwendet werden, und nicht direkt für spätere Körperoperationen, wie Polster oder Tasche.

### Verwendung externer Geometrie in einem PartDesign Arbeitsbereich Arbeitsablauf 

Im Arbeitsablauf des PartDesign Arbeitsbereichs wird das Werkzeug Externe Geometrie verwendet, um die Positionierung eines Aspekts des von Dir konstruierten Körpers im Vergleich zum vorherigen Schritt in seiner Konstruktion zu unterstützen. PartDesign Arbeitsbereich ist für die Herstellung eines einzelnen Körpers vorgesehen, daher werden diese Skizzen mit externer Geometrie verwendet, um ein neues Merkmal dieses einen Körpers zu erzeugen.

Die Außengeometrie kann beispielsweise als Referenz für eine Zwangsbeschränkung verwendet werden, mit der ein Loch in einem Objekt an einer bestimmten Stelle relativ zu einer Kante oder einem Scheitelpunkt positioniert wird.

### Verwendung der externen Geometrie in einem Teil Arbeitsbereich Arbeitsablauf 

Du kannst jede beliebige Teilegeometrie verwenden, die sich im Koordinatensystem der Skizze befindet. Es wird empfohlen, auf das nächstmögliche Merkmal zu verknüpfen, da es eine stabilere Verbindung bildet.

## Beispiel

In v0.16 und älter muss die Skizze einer Fläche zugeordnet werden, um dieses Werkzeug zu verwenden. Seit v0.17 wurde diese Begrenzung aufgehoben, dies ist unten eine Skizze, die der Oberseite eines Festkörpers zugeordnet ist, der aus einem Polster einer vorherigen Skizze erstellt wurde. Die magentafarbenen Linien sind externe Geometrie, die mit zwei Kanten dieses bereits vorhandenen Polsters verbunden sind.

In diesem Fall werden sie als Referenz für Tangentialbeschränkungen mit den Umfängen eines Kreises verwendet. Sie werden auch als Referenz für eine horizontale und vertikale Zwangsbeschränkungung verwendet, um den Mittelpunkt des zweiten Kreises relativ zum Ende und zur Oberseite des Polsters zu ermitteln.

<FILE:Sketcher_ExternalEsempio2.png>

Dies ist die gleiche Skizze im Bearbeitungsmodus, wobei das Polster, auf das sie abgebildet ist, ausgeblendet ist.

<FILE:Sketcher_ExternalEsempio4.png>

Wenn der Skizzenbearbeitungsmodus geschlossen ist, sind externe Geometrielinien nicht sichtbar.

<FILE:Sketcher_ExternalEsempio3.png>





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/de
