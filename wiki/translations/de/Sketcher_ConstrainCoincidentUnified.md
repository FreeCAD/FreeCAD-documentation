---
 GuiCommand:
   Name: Sketcher ConstrainCoincidentUnified
   Name/de: Sketcher KoinzidentFestlegenKombiniert
   MenuLocation: Skizze , Sketcher-Randbedingungen , Koinzidenz festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **C**
   Version: 1.0
   SeeAlso: Sketcher ConstrainCoincident/de, Sketcher_ConstrainPointOnObject/de
---

# Sketcher ConstrainCoincidentUnified/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:24px;"> [Sketcher KoinzidentFestlegenKombiniert](Sketcher_ConstrainCoincidentUnified/de.md) legt Deckungsgleichheit zwischen Punkten fest, verbindet Punkte mit Kanten oder Achsen (Linien werden als unendlich angesehen und offene Kurven werden auch virtuell verlängert) oder legt Kreise, Kreisbögen und/oder Ellipsen konzentrisch fest (indem ihre Mittelpunkte deckungsgleich festgelegt werden).

Dieses Werkzeug ersetzt die Werkzeuge [Sketcher KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) und [Sketcher PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md), wenn die Option **Kombiniertes Werkzeug für Koinzidenz und Punkt-auf-Objekt-Randbedingungen** in den [Voreinstellungen](Sketcher_Preferences/de#Allgemein.md) ausgewählt wurde.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> [Koinzidenz festlegen](Sketcher_ConstrainCoincidentUnified/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Koinzidenz festlegen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Koinzidenz festlegen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **C**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Punkte auswählen.
    -   Zwei Kanten von Kreisen, Kreisbögen, Ellipsen oder Ellipsenbögen auswählen.
    -   Einen einzelnen Punkt und eine einzelne Kante (in beliebiger Reihenfolge) auswählen.
5.  Eine Randbedingung wird hinzugefügt.
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei oder mehr Punkte auswählen.
    -   Zwei oder mehr Kanten von Kreisen, Kreisbögen, Ellipsen oder Ellipsenbögen auswählen.
    -   Einen einzelnen Punkt und eine einzelne Kante auswählen (in beliebiger Reihenfolge).
    -   Mehrere Punkte und eine einzelne Kante auswählen (in beliebiger Reihenfolge).
    -   Einen einzelnen Punkt und mehrere Kanten auswählen (in beliebiger Reihenfolge).
2.  Das Werkzeug aufrufen, wie oben beschrieben oder mit der folgenden zusätzlichen Möglichkeit:
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Constrain coincident** im Kontextmenü auswählen.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Hinweise

-    {{Version/de|1.0}}: Punkte denen die Randbedingung Koinzident festlegen zugeornet ist, werden mit der [Farbe](Sketcher_Preferences/de#Darstellung.md) der **Symbole für Randbedingungen** gekennzeichnet.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincidentUnified/de
