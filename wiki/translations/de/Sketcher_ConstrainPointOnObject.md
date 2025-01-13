---
 GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   Name/de: Sketcher PunktAufObjektFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Punkt auf Objekt festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **O**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/de, Sketcher_ConstrainCoincident/de
---

# Sketcher ConstrainPointOnObject/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Sketcher PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) verbindet Punkte mit Kanten oder Achsen. Linien werden als unendlich angesehen und Kurven werden ebenso virtuell verlängert.


{{Version/de|1.0}}

: Dieses Werkzeug wird durch das Werkzeug [Sketcher KoinzidentFestlegenKombiniert](Sketcher_ConstrainCoincidentUnified/de.md) ersetzt, wenn die Option **Koinzidenz und Punkt auf Objekt vereinigen** in den [Voreinstellungen](Sketcher_Preferences/de#Allgemein.md) ausgewählt wurde.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> Punkt auf Objekt festlegen** auswählen.
    -   Das Tastaturkürzel **O**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Einen einzelnen Punkt und eine einzelne Kante (in beliebiger Reihenfolge) auswählen.
5.  Eine Randbedingung wird hinzugefügt.
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  eine der folgenden Möglichkeiten auswählen:
    -   Einen einzelnen Punkt und eine einzelne Kante auswählen (in beliebiger Reihenfolge).
    -   Mehrere Punkte und eine einzelne Kante auswählen (wie vorher).
    -   Einen einzelnen Punkt und mehrere Kanten auswählen (wie vorher).
2.  Das Werkzeug aufrufen, wie oben beschrieben.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Skripten

Die Randbedingung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch den folgenden Befehl erstellt werden:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`ist ein Skizzenobjekt

-    `LineMoving`ist die Nummer, die die Linie kennzeichnet, die den Punkt enthält, der auf die `LineFixed` (die Linie, die fixiert ist) verschoben werden soll.

-    `PointOfLineMoving`ist die Nummer des Knotens der Linie `LineMoving`, der sich auf die Linie `LineFixed` bewegen soll.

-    `LineFixed`ist die Nummer der Linie, an die der Punkt `PointOfLineMoving` befestigt werden soll.

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt, wie man die Nummern zum Bestimmen von Linien und Punkten erkennt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/de
