---
- GuiCommand:
   Name:Part Loft
   Name:Part Ausformung
   MenuLocation:Formteil → Ausformung...
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.13
   SeeAlso:[Part Austragung](Part_Sweep/de.md)
---

# Part Loft/de



## Übersicht

Das Werkzeug **Part Ausformung** (Loft) wird verwendet, um aus zwei oder mehr Konturen eine Fläche, Schale oder eine Festkörper-Form zu erstellen. Die Konturen können ein Punkt (Knoten), eine Linie (Kante), ein Draht oder eine Fläche sein. Kanten und Drähte können entweder offen oder geschlossen sein. Es gibt verschiedene [Einschränkungen und Schwierigkeiten](Part_Loft/de#Einschränkungen_und_Schwierigkeiten.md), siehe unten, jedoch können die Konturen aus den Grundkörpern des Arbeitsbereichs [Part](Part_Workbench/de.md), den Objekten des Arbeitsbereichs [Draft](Draft_Workbench/de.md) und aus [Skizzen](Sketcher_Workbench/de.md) stammen.

Die Ausformung hat drei Parameter, \"Regelfläche\", \"Erzeuge Volumenkörper\" und \"Geschlossen\", jeweils mit einem Wert von \"wahr\" oder \"falsch\".

Wenn \"Erzeuge Volumenkörper\" auf \"wahr\" gesetzt ist, erstellt FreeCAD einen Festkörper, wenn die Konturen geschlossenen Geometrien sind, wenn auf \"falsch\" gesetzt, erzeugt FreeCAD eine Fläche oder (aus mehreren Flächen) eine Hülle für offene oder geschlossene Profile.

Wenn \"Regelfläche auf \" \"wahr\" gesetzt ist, erstellt FreeCAD eine Fläche, Flächen oder einen Festkörper aus Regelflächen. [Regelfläche auf Wikipedia.](https://de.wikipedia.org/wiki/Regelfl%C3%A4che)

Wenn \"Geschlossen\" \"wahr\" ist, versucht FreeCAD, das letzte Profil in das erste Profil auszuformen, um eine geschlossene Figur zu erzeugen.

Weitere Informationen, wie Profile miteinander verbunden werden, entnehme bitte der Seite [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md).

![centre\|Part Loft. Aus drei Profilen, die zwei Part Kreise und eine Part Ellipse sind. Die Parameter sind Festkörper \"wahr\" und Regelfläche \"wahr\".](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )



## Hinweise

-   [App-Link](App_Link/de.md)-Objekte, die auf geeignete Objektarten verweisen und [App-Part](App_Part/de.md)-Container, die geeignete sichtbare Objekte enthalten, können auch als Profile und Pfade verwendet werden. {{Version/de|0.20}}



## Einschränkungen und Schwierigkeiten 

-   Ein Knoten oder Punkt
    -   Knoten oder Punkt darf nur als erstes und/oder letztes Profil in der Liste der Profile verwendet werden.
        -   Zum Beispiel
            -   Du kannst nicht von einem Kreis zu einem Punkt, zu einer Ellipse ausformen.
            -   Allerdings kannst Du von einem Punkt zu einem Kreis zu einer Ellipse zu einem anderen Punkt ausformen.
-   Offene oder geschlossene Geometrieprofile können nicht in einer einzigen Loft gemischt werden.
    -   In einer Ausformung müssen alle Profile (Linienzüge usw.) entweder offen oder geschlossen sein.
        -   Zum Beispiel
            -   FreeCAD kann nicht zwischen einem Teilkreis und einer Standard-Bauteillinie ausgeformt werden.
-   Funktionen des Arbeitsbereichs Draft
    -   Funktionen des Arbeitsbereichs Draft können direkt als Profil in FreeCAD 0.14 oder später verwendet werden.
        -   Beispielsweise können die folgenden Draft-Funktionen als Profile in einer Part-Ausformung verwendet werden.
            -   Draft Polygon.
            -   Draft Punkt, Linie, Draht,
            -   Draft B-Spline, Bezierkurve
            -   Draft Kreis, Ellipse, Rechteck
-   PartDesign Skizzen
    -   Das Profil kann mit einer Skizze erstellt werden. Allerdings wird nur eine gültige Skizze in der zur Verfügung stehenden Liste angezeigt.
    -   Die Skizze darf nur einen offenen oder geschlossenen Draht oder eine Linie enthalten (es können mehrere Linien sein, wenn diese Linien alle verbunden sind und so einen einzigen Draht bilden)
-   Arbeitsbereich Part
    -   das Profil kann ein gültiger geometrischer Part-Grundkörper sein, der mit dem Werkzeug [Part Grundkörper erstellen](Part_Primitives/de.md) erstellt werden kann.
        -   Zum Beispiel können die folgenden geometrischen Part-Grundkörper ein gültiges Profil sein.
            -   Punkt (Knoten), Linie (Kante)
            -   Wendel (Helix), Spirale
            -   Kreis, Ellipse
            -   Regelmäßiges Polygon
            -   Ebene (Fläche)

-   Geschlossene Ausformungen
    -   Die Ergebnisse geschlossener Ausformungen können unerwartet sein - die Ausformung kann Verdrehungen oder Knicke entwickeln. Ausformen ist sehr empfindlich auf die Platzierung der Profile und die Komplexität der Kurven, die erforderlich sind, um die zugehörigen Knoten in allen Profilen zu verbinden.



## Eine Beispiel-Ausformung 

Das Werkzeug Ausformung befindet sich im Arbeitsbereich Part, Menü Part -\> Ausformung\... oder über das Symbol in der Werkzeugleiste.

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )

In den \"Aufgaben\" befinden sich zwei Listen: \"Vorhanden\" und \"Ausgewählt\".

![](images/Part_Loft_Liste3.png )

### Auswahl der Schnittkonturen 

Unter \"Verfügbare Profile\" werden die verfügbaren Elemente angezeigt. Zwei (Quer-) Schnitte müssen ausgewählt werden, einer nach dem ersten in dieser Liste .

![](images/Part_Loft_Liste_Auswahl_3b.png )

Danach wird dieser Eintrag mit dem blauen Pfeil zur Liste \"Ausgewählte Profile\" hinzugefügt.

![](images/Part_Loft_Liste_Auswahl_3c.png )

Die ausgewählten Einträge müssen vom gleichen Typ sein.

Hinweis: Die aktiven/ausgewählten Einträge in der Liste werden im 3D-Bereich als aktiv/ausgewählt angezeigt.



### Befehl vollständig 

Wenn beide Schnitte ausgewählt sind, kann der Befehl mit \"OK\" abgeschlossen werden.

![](images/Part_Loft_Liste_Auswahl_3d.png )



### Ergebnis

Aus geschlossenen Linien erhalten wir Oberflächen, die bei oberflächlicher Betrachtung als Festkörper angesehen werden könnten.

![](images/Part_Loft_geschlossen.png )

Wenn tatsächlich ein Festkörper erstellt werden muss, verwendet man die Schaltfläche \"Festkörper erstellen\" oder wechselt, nachdem die Ausformung erzeugt wurde, zum Reiter *Daten* in ihren \'\'Eigenschaften und setzt den Schalter \"Solid\" auf true.

Bei offenen Polylinien ist die Vorgehensweise die gleiche wie oben beschrieben.



### Auswahl der Querschnitte ändern 

Soll die Auswahl der Querschnitte nach der Erstellung der Ausformung geändert werden, kann das Feld Sections auf der Registerkarte Daten markiert und die erscheinende Schaltfläche **...** (Ellipse) angeklickt werden. Die Liste aller auswählbaren Querschnitte erscheint und die aktuelle Auswahl wird hervorgehoben. Es können zusätzliche Abschnitte entfernt oder hinzugefügt werden.

Die Reihenfolge der Abschnitte hängt von der Reihenfolge der Klicks in der Liste ab. Wenn Du wesentliche Änderungen vornehmen möchtest, empfiehlt es sich, zuerst alle zu deselektieren und dann die Auswahl in der richtigen Reihenfolge zu starten.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/de
