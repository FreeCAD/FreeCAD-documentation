---
- TutorialInfo:/de
   Topic:Schiff Arbeitsbereich
   Level:Anfänger
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial (II)/de





## Überblick

Bevor du mit diesem Tutorial beginnst, stelle bitte sicher, dass du bereits [der erste Teil](FreeCAD-Ship_s60_tutorial/de.md) durchgeführt hast.

Erfahre mehr über den Schiff Arbeitsbereich auf ihrer speziellen Wiki Seite: [Schiffs Arbeitsbereich](Ship_Workbench/de.md)

## Einführung

In diesem Tutorium werden wir mit Gewichten und Tanks arbeiten, um die GZ Kurve, den wichtigsten hydrostatischen Stabilitätsparameter, zu berechnen. GZ ist das statische Moment, das erzeugt wird, wenn das Schiff einen Rollwinkel einnimmt, da der GZ Arm positiv ist, das Schiff ein positives Moment hat und versuchen wird, die aufrechte Position wiederherzustellen, aber wenn GZ negative Zahlen annimmt, hat das Schiff keine Stabilität mehr und erreicht eine kritische Situation.

Die IMO (Internationale Seeschifffahrtsorganisation) legte folgende Kriterien fest:

-   *GM* \>= 0.15 m. GM\" (metazentrische Höhe) ist die Anfangstangente der \"GZ\" Kurve.
-   Der maximale *GZ* Wert muss über 30 Grad des Rollwinkels liegen.
-   Bei einem Rollwinkel von 30 Grad muss der *GZ* Wert mindestens 0,2 m betragen.
-   Der beteiligte Bereich der \"GZ\" Kurve bis zu einem Rollwinkel von 40 Grad muss mindestens 0,090 m - rad betragen.
-   Der beteiligte Bereich der \"GZ\" Kurve bis zu einem Rollwinkel von 30 Grad muss mindestens 0.055 m · rad betragen.
-   Der beteiligte Bereich der \"GZ\" Kurve von 30 bis 40 Grad Rollwinkel muss mindestens 0.030 m · rad betragen.

In diesem Tutorium werden wir Gewichte und Tanks für unser Schiff der Serie 60 in einer simulierten Situation einstellen.

## Schiffsgewichte

Um die GZ Kurve berechnen zu können, müssen wir die Schiffsgewichte und ihre Position bei jedem Rollwinkel kennen, daher werden die Gewichte in zwei Kategorien eingeteilt:

-   Feste Gewichte, die vollständig mit den Schiffsbewegungen verknüpft sind.
-   Tanks, bei denen sich die Form der Flüssigkeit mit dem Winkel ändert, so dass der Schwerpunkt an jeder Position berechnet werden muss.

Der Schiff Arbeitsbereich bietet zwei verschiedene Werkzeuge zur Erzeugung jeder Instanz.

![Gewichtsfestlegungswerkzeug Symbol.](images/FreeCAD-Ship-WeightIco.png )


<center>

Gewichtsfestlegungswerkzeug Symbol.


</center>

Das Werkzeug zur Definition von Gewichten kann zur Festlegung der ersten Kategorie von Gewichten verwendet werden. Wenn du das Werkzeug zum ersten Mal startest (mit ausgewählter Schiffsinstanz), initialisiert der Schiffs Arbeitsbereich die Schiffsgewichte mit Schiffsleichtgewicht (gleich der Schiffsverdrängung), das auf der X Koordinate des Schiffsgeometrieschwerpunkts und auf Höhe des Konstruktionsentwurfs liegt. Normalerweise gibt es mindestens 2 relevante Gewichte:

-   Struktur.
-   Hauptmaschine (oder mehrere davon).

Also werden wir es ändern. Mit einem Doppelklick auf jede Zelle können wir den Wert bearbeiten und Gewichte einstellen:

-   Struktur, 15000 kg, (-0.1, 0, 1.25) m
-   Steuerbordmotor, 5000 kg, (-6,5, -0,65, 0,5) m
-   Backbordmotor, 5000 kg, (-6,5, 0,65, 0,5) m
-   Notfall Motor, 2500 kg, (0,2, 0, 2,5) m

![Gewichtsdefinition 3D Vorschau.](images/FreeCAD-Ship-S60WeightsPreview.png )


<center>

Gewichtsdefinition 3D Vorschau.


</center>

Die Position der Gewichte wird in der [3D Ansicht](3D_view/de.md) angezeigt. Hinweis: Die Anmerkungen werden entfernt, wenn das Werkzeug geschlossen wird. Wenn du **Accept** drückst, werden die Gewichte in deiner Schiffsinstanz gespeichert.

## Tanks

Die Tanks müssen über der Festkörpergeometrie als Schiffsinstanz erstellt werden, daher besteht der erste Schritt darin, zwei Bugtanks (einen pro Schiffsseite) Festkörpergeometrien zu erstellen, die wir in Betracht ziehen werden (normalerweise haben Schiffe viele Tanks für Kraftstoff, Süßwasser, Salzwasser, Ladung usw.).

### Geometrieerzeugung

Um Tanks zu generieren, laden wir [Part Modul](Part_Workbench/de.md), und erzeugen ein Kasten Volumenmodell.

Wir müssen den Kasten bearbeiten, also markieren wir ihn im **Attribute und Markierungen** Baum und wechseln von der Ansicht zum Datenreiter. Erweitere Platzierung, und in ihnen Position, und setze *x* auf 1,5, und z auf -1. Wir wollen auch die Kastenlänge ändern, indem wir sie für 5.0 ändern (beachte, dass die Einheiten in mm angegeben werden können, kümmere dich nicht darum).

Die Tankgeometrie wird gemeinsamer Bestandteil der erstellten Kasten- und Schiffsgeometrie sein, so dass wir die **Schiff** Instanz ausblenden und die **s60_IowaUniversity** Geometrie anzeigen können. Wenn wir Kasten und **s60_IowaUniversity** auswählen, können wir die Gemeinsame Arbeitsgang Erzeugung verwenden, die unsere Steuerbordtankgeometrie erzeugt.

![Generierte Tankgeometrie.](images/FreeCAD-Ship-S60TankGeometry.png )


<center>

Generierte Tankgeometrie.


</center>

Wir können den Tank auf der Backbordseite ausführen, indem wir unsere Steuerbordgeometrie auswählen und das Spiegelwerkzeug ausführen und XZ als Spiegelebene wählen.

Um die Geometrie in eine gewöhnliche feste Form unserer Tanks umzuwandeln und unsere **s60_IowaUniversity** Geometrie wiederherzustellen, können wir [Entwurf Modul](Draft_Workbench/de.md) laden und mit gewählter Steuerbord Tankgeometrie die Höherstufung ausführen und mit der Backbordseite der Tankgeometrie wiederholen. Wir können Geometrien umbenennen als:

-   SteuerbordTankGeom
-   BackbordTankGeom

Wir können erstellte Kästen, die wir nicht mehr benötigen, löschen.

### Generierung von Tankinstanzen 

Wenn du [FreeCAD Schiffsmodul](Ship_Workbench/de.md) ein anderes Mal neu lädst, können wir ein Werkzeug zum Generieren von Tankinstanzen finden.

![Tankinstanzenerzeugungswerkzeug Symbol.](images/FreeCAD-Ship-TankIco.png )


<center>

Tankinstanzenerzeugungswerkzeug Symbol.


</center>

Jetzt können wir **SteuerbordTankGeom** auswählen und das Werkzeug zur Erzeugung von Tankinstanzen ausführen, wobei einige Daten bereitgestellt werden müssen. Wir werden 40% des Füllstands und 925 kg/m$\mathrm{m}^{3}$ (Kraftstoffansatz) einstellen. Wenn **Annehmen** angeklickt wird, wird eine neue Tankinstanz mit dem Namen **Tank** erzeugt. Wir können sie in **SteuerbordTank** umbenennen und **Steuerbord-TankGeom** ausblenden.

Wir können den gleichen Vorgang wiederholen, um **BackbordTank** zu generieren.

![Ansicht erzeugter Gewichte.](images/FreeCAD-Ship-S60WeightsTanksPreview.png )


<center>

Ansicht erzeugter Gewichte.


</center>

Die Abbildung zeigt unser Schiffsergebnis, das wir berechnen werden.

### GZ Kurven Berechnung 

Der Schiffs Arbeitsbereich bietet ein Werkzeug zur einfachen Berechnung einer \'\'GZ\' Kurve.

<img alt="GZ Kurven Berechnungswerkzeug Symbol." src=images/Ship_GZ.svg  style="width:128px;">


<center>

GZ Kurven Berechnungswerkzeug Symbol.


</center>

Mit gewählter **Schiff** Instanz, können wir das Werkzeug ausführen. Das erste, was wir im geöffneten Dialog sehen können, ist eine Liste mit allen Tankinstanzen, die im aktiven Dokument gefunden wurden. Wir wollen beide verwenden, also klicken wir über die Tanks, die mit einem anderen Hintergrund versehen sind.

Um die sich daraus ergebende Schiffsverdrängung und den Tiefgang zu erfahren, können wir auf *\'Verdrängung und Tiefgang aktualisieren* drücken, was einige Zeit für die Berechnung benötigt. Wir erhalten folgende Daten:

-   Verdrängung = 37505.5 kg
-   Tiefgang = 0.818664 m

Wir befinden uns also in einer unbelasteten Situation, in der die Entwürfe geringfügig niedriger sind als die Konstruktionsentwürfe. Normalerweise bedeuten niedrigere Tiefgänge eine geringere Schiffsstabilität, der Tiefgang hängt vom Beladungszustand ab. Wenn wir also wirklich erwarten, dass das Schiff in diesem Beladungszustand betrieben werden kann, können wir den Einsatz von Ballasttanks in Erwägung ziehen.

Wir können auch automatisch den Schiffstrimm berechnen, ein Vorgang, der etwa eine Minute dauern kann, wobei wir feststellen können, dass unser Schiff einen Trimmwinkel von 0,95 Grad hat (positiv beim Heck). In diesem Beispiel werden wir ohne Trimmwinkel (0 Grad) arbeiten.

Werkzeuganforderung Rollwinkel werden ebenfalls berücksichtigt. In diesem Fall wollen wir das gesamte Schiffsverhalten kennen, damit wir einstellen können:

-   0 Grad Anfangsrollwinkel.
-   180 Grad Endrollwinkel.
-   46 Punkte. Einer für je 2 Grad. Die GZ Berechnung kann einige Zeit in Anspruch nehmen, also achte auf die Anzahl der gewünschten Punkte.

Wenn wir *\'Annehmen* drücken, startet das Werkzeug die Berechnung. Wenn du FreeCAD vom Terminal aus startest, kannst du den Arbeitsfortschritt sehen. In ein paar Sekunden erhalten wir die GZ Kurve.

Dieses Werkzeug verwendet [pyxplot](http://www.pyxplot.org.uk/) und [ghostscript](http://www.ghostscript.com/) ebenfalls. Du kannst sehen, wo die Ausgabedatei **gz.dat** in der Berichtsansicht (Ansicht/Ansichten/Berichtsansicht) platziert wurde, und sie mit Datenblattsoftware (z.B. [libreOffice](http://www.libreoffice.org)) laden. In der Nähe der Datendatei wurden auch mehrere Hilfsdateien erstellt:

-   **gz.dat**: Berechnete GZ Kurvendaten.
-   **gz.pyxplot**: pyxplot Layout, um die Kurve zu plotten..
-   **gz.eps**: EPS Bildversion.
-   **gz.png**: PNG Bildversion.

Diese Dateien werden überschrieben, wenn du das Werkzeug ein weiteres Mal ausführst.

### Ergebnisse

<img alt="Resultierende GZ Kurve." src=images/FreeCAD-Ship-s60GZ.png  style="width:800px;">


<center>

Resultierende GZ Kurve.


</center>

Der *GZ* Maximalwert wird über 30 Grad (45 Grad) gelegt und erhält 0,25 m bei 30 Grad (0,2 m ist das Minimum). Bis zu 30 Grad beträgt die Fläche unterhalb der *GZ* Kurve 0.065 m·rad, bis zu 40 Grad haben wir 0.092 m·rad, was der Fläche zwischen 30 und 40 Grad von 0.027 m·rad entspricht. Unser Schiff erfüllt also nicht die Anforderungen der IMO. Die Lösung ist die Platzierung von Ballasttanks.

Andererseits hat das Schiff in diesem schlechten Zustand positive *GZ* Werte bis zu 95 Grad Rollwinkel, war aber nicht ausreichend für die Stabilitätsanforderungen der IMO, was die harten Kriterien zeigt, die für diesen Punkt auferlegt wurden.

Natürlich ist dieses Beispiel nicht real (erstens können die Treibstofftanks nicht in der Doppelbodenstruktur oder unter Verwendung der Rumpfseite als Struktur platziert werden), aber es ist ein gutes Beispiel, um den Umgang mit [Schiff Arbeitsbereich](Ship_Workbench/de.md) zu erlernen.



---
⏵ [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial (II)/de
