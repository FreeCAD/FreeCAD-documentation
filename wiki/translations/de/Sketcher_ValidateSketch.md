---
- GuiCommand:
   Name: Sketcher ValidateSketch
   Name/de: Sketcher SkizzeÜberprüfen
   MenuLocation: Sketch -> Skizze überprüfen…
   Workbenches: Sketcher_Workbench/de, PartDesign_Workbench/de
   SeeAlso: Sketcher_ConstrainCoincident/de, Topological_naming_problem/de
---

# Sketcher ValidateSketch/de

## Beschreibung

Das Dienstprogramm **Skizze validieren** kann verwendet werden, um eine Skizze zu analysieren und zu reparieren, die nicht mehr bearbeitbar ist oder ungültige Beschränkungen enthält, oder um fehlende [Deckungsgleiche Beschränkungen](Sketcher_ConstrainCoincident/de.md) zu einer Skizze hinzuzufügen, die aus importierter Geometrie wie DXF Dateien erstellt wurde. Es kann auch nützlich sein, eine fehlende Deckungsgleichheit in einer ursprünglichen Skizze zu finden, die beim Versuch, eine PartDesign Funktion anzuwenden, die Fehlermeldung \"kann gebrochene Fläche nicht validieren\" erzeugt.

![](images/Sketcher_ValidateSketch_taskpanel.png ) 
*Das Skizzierer Aufgabenpaneel Validierung*

## Anwendung

1.  Dieses Werkzeug kann nicht für eine Skizze verwendet werden, die sich im Bearbeitungsmodus befindet. Verlasse bei Bedarf den Bearbeitungsmodus, indem du einen der folgenden Schritte ausführst:

-   Drücke die **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Skizze verlassen](Sketcher_LeaveSketch/de.md)** Taste.

#\* Drücke die Schaltfläche **Schließen** am oberen Rand des [Aufgabenpaneels](Task_panel/de.md).

#\* Verwende das Tastaturkürzel: **Esc** (falls in den [Skizzierer Einstellungen](Sketcher_Preferences/de#Allgemein.md) aktiviert).

1.  Wähle die zu prüfende Skizze in der [Baumansicht](Tree_view/de.md) oder durch Klicken auf eine ihrer Kanten in der [3D Ansicht](3D_view/de.md) aus.
2.  Führe einen der folgenden Schritte aus, um das Dienstprogramm \"Skizze validieren\" zu öffnen:

-   Wähle im Menü die Option **Skizze → Skizze validieren...**.

#\* Drücke den **<img src="images/Sketcher_ValidateSketch.svg" width=16px> [Skizze validieren](Sketcher_ValidateSketch/de.md)** (nicht verfügbar im [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)).

1.  Siehe [Optionen](#Optionen.md) unten für die verfügbaren Arbeitsschritte.
2.  Drücke die Schaltfläche **Close**, wenn alles erledigt ist.

## Optionen

### Fehlende Deckungsgleichheit 

Findet fehlende Deckungsgleichheit für überlappende Knoten und fügt sie hinzu. Drücke die Taste **Find**; es erscheint ein Aufklappdialog, der anzeigt, wie viele fehlende zusammenfallende Punkte gefunden wurden; sie werden in der 3D Ansicht als gelbe Kreuze dargestellt. Drücke **OK**, um den Dialog zu schließen, und drücke dann die Taste **Fix**, um die fehlenden zusammenfallende Punkte hinzuzufügen.

Lege bei Bedarf einen größeren Toleranzwert im Aufklappfeld fest.


**Fehlerhafte Knotenpunkte hervorheben**

drücken, um Knoten zu markieren, die außerhalb dieser Toleranz liegen.

Diese Toleranz wird auch von dem Prozess **Find**/**Fix** verwendet.

Lasse das Kontrollkästchen \"Konstruktionsgeometrie ignorieren\" aktiviert, um die Konstruktionsgeometrie in der Analyse zu ignorieren.

### Ungültige Beschränkungen 

Prüft auf fehlerhafte Beschränkungen.

Gibt es beispielsweise eine Kreis-Linie-Tangente Beschränkung, die sich aber auf zwei Linien bezieht, wird sie als ungültig betrachtet.

(Dies geschieht manchmal aufgrund des [Problems der topologischen Benennung](Topological_naming_problem/de.md), wenn externe Geometrie ihren Typ ändert).

Es führt auch andere Prüfungen durch, z. B. auf leere Verweise.

### Entartete Geometrie 

Entartete Geometrie kann durch Löseraktionen in einer Skizze entstehen.

Wenn zum Beispiel eine Linie gezwungen wird, sich zu verkürzen, um fast ein Punkt zu bilden.

Andere Beispiele: eine Linie der Länge Null oder ein Kreis/Bogen mit dem Radius Null.

### Umgekehrte Äussere Geometrie 

Umgekehrte äußere Geometrie kann vorkommen, da die Behandlung von umgekehrter Geometrie in der Version 0.15 geändert wurde.

Dieser Prozess kann hilfreich sein, wenn Skizzen mit externer Geometrie aufgrund dieser Änderungen nicht gelöst werden können.

### Beschränkungsausrichtungssperre

Es werden tangentiale und senkrechte Beschränkungen implementiert (via-punkt).

Intern funktionieren sie, indem sie den Winkel zwischen tangentialen Vektoren beschränken. Bei der Tangentenbeschränkung kann der Winkel beispielsweise 0 oder 180 Grad betragen (gleichgerichtete oder entgegengesetzte Vektoren). Der aktuelle Winkel wird in den Bindungsdaten gespeichert (\"Bindungsausrichtung ist gesperrt\") und schützt so vor dem Umkippen. Der Winkel kann jedoch gelöscht (\"Bindungsausrichtung entsperren\") oder aktualisiert werden; genau das tun diese Werkzeuge.

Der Sperrmechanismus funktioniert in der Regel gut und dieses Werkzeug sollte nicht benötigt werden. Es sollte nur verwendet werden, nachdem eine Sicherung des geöffneten Dokuments erstellt wurde.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/de
