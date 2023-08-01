---
- GuiCommand:
   Name:Sketcher External
   Name/de:Sketcher ExterneGeometrie
   MenuLocation:Skizze → Skizzengeometrien → Externe Geometrie
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**G** **X**
   SeeAlso:[Sketcher UmschalterKonstruktion](Sketcher_ToggleConstruction/de.md)
---

# Sketcher External/de



## Beschreibung

Das Werkzeug **<img src="images/Sketcher_External.svg" width=16px> [Externe Geometrie](Sketcher_External/de.md)** wird verwendet, wenn eine Randbedingung zwischen Geometrien innerhalb und außerhalb der Skizze angewendet werden soll. Es funktioniert, indem eine *verknüpfte Hilfsgeometrie* in die Skizze eingefügt wird. Die Standardfarbe der extern verknüpften Kanten ist Magenta. Wie die normale unverknüpfte Hilfsgeometrie (blau) ist die extern verknüpfte Geometrie nur sichtbar, wenn sich die Skizze im Bearbeitungsmodus befindet und wird auch nicht bei der Verwendung der Skizze mit einem anderen Werkzeug benutzt. Beide Arten von Hilfsgeometrien können als Referenz für Randbedingungen innerhalb der Skizze verwendet werden.

Ein Hinweis zur Vorsicht, die Verwendung dieses Werkzeugs kann aufgrund des [Problems der Topologischen Benennung](Topological_naming_problem/de.md) zu unerwarteten Ergebnissen führen. Siehe auch [Ratschlag für stabile Modelle](Feature_editing/de#Ratschläge_zur_Erstellung_stabiler_Modelle.md).

<FILE:Sketcher_ExternalEsempio1.png>



## Anwendung

-   Eine neue Skizze erstellen oder eine bestehende Skizze öffnen.

-   Die Schaltfläche **[<img src=images/Sketcher_External.svg style="width:16px"> [Externe Geometrie](Sketcher_External/de.md)** drücken.

-   Eine Kante oder einen Knotenpunkt auswählen, auf die/den in der Skizze verwiesen werden soll.

-    **Esc**drücken oder ein anderes Werkzeug wählen, um den Import von Geometrien in die Skizze zu beenden.

### Auswahlregeln

-   Es sind nur Kanten und Knoten von Objekten **aus demselben Koordinatensystem** zulässig.

Das heißt, die Skizze und das Objekt müssen sich **im gleichen Körper** (für den Arbeitsbereich *PartDesign*), **im gleichen Teil** (für den Arbeitsbereich *Part*), **oder beide außerhalb** von Teilen und Körpern befinden.

Wenn sich die aktuell geöffnete Skizze beispielsweise im Körper **Body** befindet, kann eine andere Skizze aus dem Körper **Body** als externe Geometrie verwendet werden, nicht aber eine Skizze aus dem Körper **Body001** oder die Kante eines Part-Würfels im Wurzelbereich des Projekts. Für solche Fälle kann die Funktion **Formbinder** verwendet werden, um eine **Kopie des zu verknüpfenden Objekts** in das Koordinatensystem der aktuell geöffneten Skizze einzubringen. Dann können die Kanten/Eckpunkte dieses Formbinders (ShapeBinder-Objekt) verknüpft werden.

-   Rekursive Abhängigkeiten sind nicht erlaubt.

Das bedeutet, dass nicht auf eine Tasche verwiesen werden kann, die (erst) mit dieser Skizze erstellt wurde. Es kann auf kein Objekt verwiesen werde, das von der Skizze abhängt.

Die Skizze muss sich nicht auf einer Fläche eines Volumenkörpers befinden, um dieses Werkzeug zu nutzen. Direkte Verknüpfungen zwischen Skizzen sind auch möglich und werden empfohlen, da sie zuverlässiger sind.

### Darstellung bei erfolgreicher Verknüpfung 

Eine (standardmäßig magenta-) farbige Linie wird überlagert, wenn eine Kante erfolgreich verknüpft wurde (die Knoten sind rot). Sie ist (wie alle Hilfsgeometrie) nur im Bearbeitungsmodus der Skizze sichtbar.

### Ähnlichkeit mit Hilfslinien 

(Anmerkung des Übersetzers: Der englische Begriff \'construction lines\' wird im Deutschen anschaulicher mit \'Hilfslinien\' bezeichnet und nicht mit \'Konstruktionslinien\'.) Äußere Geometrielinien (Standardfarbe Magenta) sind ähnlich (Standardfarbe Blau) [Hilfslinien](Sketcher_ToggleConstruction/de.md), mit der Ausnahme, dass die äußeren Geometrielinien Magentalinien parametrisch mit einem Element des Körpers verknüpft sind, auf den die Skizze abgebildet ist. Hilfsgeometrie sind Linien, die sich innerhalb der Skizze befinden und nur sichtbar sind, wenn sich die Skizze im Bearbeitungsmodus befindet. Sie werden nur für Zwangsbeschränkte Referenzen verwendet, und nicht direkt für spätere Körperoperationen, wie Polster oder Tasche.



### Verwendung externer Geometrie in einem PartDesign Arbeitsbereich 

Im Arbeitsablauf des **PartDesign** Arbeitsbereichs wird das Werkzeug **Externe Geometrie** verwendet, um die Platzierung von Details der Konstruktion in Relation zu vorherigen Konstruktions-Schritten zu erleichtern. Der **PartDesign** Arbeitsbereich ist für die Herstellung eines einzelnen Körpers gedacht. Daher werden diese Skizzen mit externer Geometrie verwendet, um ein neues Detail dieses einen Körpers zu erzeugen.

Die externe Geometrie kann beispielsweise als Referenz für eine Zwangsbeschränkung verwendet werden, mit der ein Loch in einem Objekt an einer bestimmten Stelle relativ zu einer Kante oder einem Scheitelpunkt positioniert wird.



### Verwendung der externen Geometrie im Part Arbeitsbereich 

Man kann jede beliebige Teilegeometrie verwenden, **die sich im Koordinatensystem der Skizze befindet**. Es wird empfohlen, auf das nächstmögliche Merkmal zu verknüpfen, da es eine stabilere Verbindung bildet.



## Beispiel

Unten sieht man eine Skizze, die der Oberseite eines Festkörpers zugeordnet ist, der aus einem Polster einer vorherigen Skizze erstellt wurde. Die magentafarbenen Linien sind externe Geometrie, die mit zwei Kanten dieses bereits vorhandenen Polsters verbunden sind.

In diesem Fall werden sie als Referenz für Tangentialbeschränkungen mit den Umfängen eines Kreises verwendet. Sie werden auch als Referenz für eine horizontale und vertikale Zwangsbeschränkungung verwendet, um den Mittelpunkt des zweiten Kreises relativ zum Ende und zur Oberseite des Polsters zu ermitteln.

<FILE:Sketcher_ExternalEsempio2.png>

Dies ist die gleiche Skizze im Bearbeitungsmodus, wobei das Polster, auf das sie abgebildet ist, ausgeblendet ist.

<FILE:Sketcher_ExternalEsempio4.png>

Wenn der Skizzenbearbeitungsmodus geschlossen ist, sind die externen Geometrielinien nicht sichtbar.

<FILE:Sketcher_ExternalEsempio3.png>





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/de
