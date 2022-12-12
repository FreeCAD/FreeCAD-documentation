---
- GuiCommand:/de
   Name:Part Loft
   Name:Part Ausformung
   MenuLocation:Formteil → Ausformung...
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.13
   SeeAlso:[Part Austragung](Part_Sweep/de.md)
---

# Part Loft/de

## Übersicht


<div class="mw-translate-fuzzy">

## Überblick

Das FreeCAD-Ausformungswerkzeug (engl.: Loft) wird verwendet, um aus zwei oder mehr Konturen eine Fläche, Schale oder eine feste Form zu erstellen. Die Konturen können ein Punkt (Knoten), eine Linie (Kante), ein Draht oder eine Fläche sein. Kanten und Drähte können entweder offen oder geschlossen sein. Es gibt verschiedene [Begrenzungen und Schwierigkeiten](Part_Loft#Limitations_and_complications.md), siehe unten, jedoch können die Konturen aus den Grundkörpern des Part Arbeitsbereichs, den Funktionen des Draft Arbeitsbereichs und einer Skizze stammen.


</div>


<div class="mw-translate-fuzzy">

Die Ausformung hat drei Parameter, \"Regelfläche\", \"Festkörper\" und \"Geschlossen\", jeweils mit einem Wert von \"wahr\" oder \"falsch\".


</div>


<div class="mw-translate-fuzzy">

Wenn \"Festkörper\" \"wahr\" ist, erstellt FreeCAD einen Festkörper, falls die Konturen von geschlossener Geometrie sind, wenn \"falsch\" erzeugt FreeCAD eine Fläche oder (wenn mehr als eine Fläche) eine Hülle für offene oder geschlossene Profile.


</div>


<div class="mw-translate-fuzzy">

Wenn \"Regel\" \"wahr\" ist, erstellt FreeCAD eine Fläche, Flächen oder einen Festkörper aus geordneten Flächen. [Regelfläche auf Wikipedia.](https://de.wikipedia.org/wiki/Regelfl%C3%A4che)


</div>

Wenn \"Geschlossen\" \"wahr\" ist, versucht FreeCAD, das letzte Profil in das erste Profil auszuformen, um eine geschlossene Figur zu erzeugen.

Weitere Informationen, wie Profile miteinander verbunden werden, entnehme bitte der Seite [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md).


<div class="mw-translate-fuzzy">

![centre\|Part_Loft. Aus drei Profilen, die zwei Part_Kreise und eine Part_Ellipse sind. Die Parameter sind Festkörper \"wahr\" und Regelfläche \"wahr\".](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )


</div>

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Limitations and complications 


<div class="mw-translate-fuzzy">

## Begrenzungen und Schwierigkeiten 

-   Ein Knoten oder Punkt
    -   Knoten oder Punkt darf nur als erstes und/oder letztes Profil in der Liste der Profile verwendet werden.
        -   Zum Beispiel
            -   Du kannst nicht von einem Kreis zu einem Punkt, zu einer Ellipse ausformen.
            -   Allerdings kannst Du von einem Punkt zu einem Kreis zu einer Ellipse zu einem anderen Punkt ausformen.
-   Offene oder geschlossene Geometrieprofile können nicht in einer einzigen Loft gemischt werden.
    -   In einer Ausformung müssen alle Profile (Linienzüge usw.) entweder offen oder geschlossen sein.
        -   Zum Beispiel
            -   FreeCAD kann nicht zwischen einem Teilkreis und einer Standard Bauteillinie ausgeformt werden.
-   Funktionen des Entwurfs Arbeitsbereichs
    -   Funktionen des Entwurfs Arbeitsbereichs können direkt als Profil in FreeCAD 0.14 oder später verwendet werden.
        -   Beispielsweise können die folgenden Draft Funktionen als Profile in einer Part Ausformung verwendet werden.
            -   Entwurf Polygon.
            -   Entwurfspunkt, Linie, Draht,
            -   Entwurf B-Spline, Bezierkurve
            -   Entwurf Kreis, Ellipse, Rechteck
-   PartDesign Skizzen
    -   Das Profil kann mit einer Skizze erstellt werden. Allerdings wird nur eine gültige Skizze in der zur Verfügung stehenden Liste angezeigt.
    -   Die Skizze darf nur einen offenen oder geschlossenen Draht oder eine Linie enthalten (können mehrere Linien sein, wenn diese Linien alle verbunden sind, wie sie dann ein einziger Draht sind)
-   Part Arbeitsbereich
    -   das Profil kann ein gültiger geometrischer Part Grundkörper sein, der mit dem [Part Grundelement](Part_Primitives/de.md) Werkzeug erstellt werden kann.
        -   Zum Beispiel können die folgenden geometrischen Part Grundkörper ein gültiges Profil sein.
            -   Punkt (Knoten), Linie (Kante)
            -   Helix, Spirale
            -   Kreis, Ellipse
            -   Regelmäßiges Polygon
            -   Ebene (Fläche)


</div>

-   Geschlossene Ausformungen
    -   Die Ergebnisse geschlossener Ausformungen können unerwartet sein - die Ausformung kann Verdrehungen oder Knicke entwickeln. Ausformen ist sehr empfindlich auf die Platzierung der Profile und die Komplexität der Kurven, die erforderlich sind, um die zugehörigen Knoten in allen Profilen zu verbinden.

## An example Loft 


<div class="mw-translate-fuzzy">

## Eine Beispiel Ausformung 

Das Ausformungswerkzeug befindet sich im Part Arbeitsbereich, Menü Formteil -\> Ausformung\.... oder über das Symbol in der Werkzeugleiste.


</div>

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )


<div class="mw-translate-fuzzy">

In den \"Aufgaben\" befinden sich zwei Listen: \"Knoten / Draht\" und \"freie Form\".


</div>

![](images/Part_Loft_Liste3.png )


<div class="mw-translate-fuzzy">

### Auswahl der Abschnitte 

Im \"Knoten / Draht\" werden die verfügbaren Elemente angezeigt. Zwei Abschnitte müssen nach dem ersten in dieser Liste ausgewählt werden.


</div>

![](images/Part_Loft_Liste_Auswahl_3b.png )


<div class="mw-translate-fuzzy">

Danach wird mit dem blauen Pfeil dieser Eintrag in die Liste der \"freien Formen\" aufgenommen.


</div>

![](images/Part_Loft_Liste_Auswahl_3c.png )

Die ausgewählten Einträge müssen vom gleichen Typ sein.

Hinweis: Die aktiven/ausgewählten Einträge in der Liste werden im 3D-Bereich als aktiv/ausgewählt angezeigt.

### Command complete 


<div class="mw-translate-fuzzy">

### Befehl vollständig 

Wenn beide Abschnitte ausgewählt sind, kann der Befehl mit \"OK\" abgeschlossen werden.


</div>

![](images/Part_Loft_Liste_Auswahl_3d.png )

### Result


<div class="mw-translate-fuzzy">

## Ergebnis

== Aus geschlossenen Linien erhalten wir Oberflächen, die als oberflächliche Betrachtung von Festkörpern angesehen werden können.


</div>

![](images/Part_Loft_geschlossen.png )


<div class="mw-translate-fuzzy">

Wenn tatsächlich ein Festkörper erstellt werden muss, verwende die Taste \"Festkörper erstellen\" oder nachdem du Ausformung erzeugt hast, wechsle zu seinen *Eigenschaftsreiter*Daten\'\' und setze den Schalter \"Festkörper\" auf true.


</div>

Bei offenen Polylinien ist die Vorgehensweise die gleiche wie oben beschrieben.

### Changing the selection of sections 


<div class="mw-translate-fuzzy">

### Ändern der Auswahl der Abschnitte 

Wenn du die Auswahl der Abschnitte nach der Erstellung der Ausformung ändern möchtest, kannst du das Feld Abschnitte auf der Registerkarte Daten markieren und auf die erscheinende Schaltfläche Ellipse klicken. Die Liste aller auswählbaren Abschnitte erscheint, die aktuelle Auswahl wird hervorgehoben. Du kannst zusätzliche Abschnitte entfernen oder hinzufügen.


</div>

Die Reihenfolge der Abschnitte hängt von der Reihenfolge der Klicks in der Liste ab. Wenn Du wesentliche Änderungen vornehmen möchtest, empfiehlt es sich, zuerst alle zu deselektieren und dann die Auswahl in der richtigen Reihenfolge zu starten.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/de
