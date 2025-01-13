---
 GuiCommand:
   Name: Sketcher ValidateSketch
   Name/de: Sketcher SkizzeÜberprüfen
   MenuLocation: Sketch , Skizze überprüfen...
   Workbenches: Sketcher_Workbench/de, PartDesign_Workbench/de
   SeeAlso: Sketcher_ConstrainCoincident/de
---

# Sketcher ValidateSketch/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> [Sketcher SkizzeÜberprüfen](Sketcher_ValidateSketch/de.md) kann eine Skizze analysieren und reparieren, die sich nicht mehr bearbeiten lässt oder ungültige Randbedingungen enthält, oder fehlende Randbedingungen des Typs [Koinzident festleggen](Sketcher_ConstrainCoincident/de.md) zu einer Skizze hinzufügen, die aus importierter Geometrie, wie DXF-Dateien, erstellt wurde. Es eignet sich auch dazu, eine fehlende Deckungsgleichheit (Koinzidenz) in einer mit dem Sketcher erstellten Skizze zu finden, die bei dem Versuch, sie für ein PartDesign-Formelement zu verwenden, einen Fehler verursacht.

<img alt="" src=images/Sketcher_ValidateSketch_taskpanel.png  style="width:" height="500px;"> 
*Das Skizzierer Aufgabenpaneel Validierung*



## Anwendung

1.  Dieses Werkzeug kann nicht für eine Skizze verwendet werden, die sich im Bearbeitungsmodus befindet. Zum Beenden des Bearbeitungsmodus siehe [Sketcher SkizzeVerlassen](Sketcher_LeaveSketch/de.md).
2.  Eine Skizze auswählen.
3.  Es gibt mehrere Möglichkeiten, Das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ValidateSketch.svg" width=16px> [Skizze überprüfen...](Sketcher_ValidateSketch/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizze überprüfen...** auswählen.
4.  Der Aufgaben-Dialog **Skizzenprüfung** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Zum Beenden die Schaltfläche **Schließen** drücken.



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
