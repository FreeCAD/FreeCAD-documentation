---
 GuiCommand:
   Name: Sketcher ConstrainCoincident
   Name/de: Skizzierer KoinzidentFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Koinzidenz festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **C**
   SeeAlso: Sketcher_ConstrainCoincidentUnified/de, Sketcher_ConstrainPointOnObject/de
---

# Sketcher ConstrainCoincident/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Sketcher KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) erstellt eine Randbedingung zwischen Punkten. die sie koinzident (deckungsgleich) festlegt oder ({{Version/de|0.21}}) eine Randbedingung zwischen Kreisen, Kreisbögen, Ellipsen, Ellipsenbögen, die sie konzentrisch festlegt (indem ihre Mittelpunkte koinzident festgelegt werden).


{{Version/de|1.0}}

: Dieses Werkzeug wird durch das Werkzeug [Sketcher KoinzidentFestlegenKombiniert](Sketcher_ConstrainCoincidentUnified/de.md) ersetzt, wenn die Option **Koinzidenz und Punkt auf Objekt vereinigen** in den [Voreinstellungen](Sketcher_Preferences/de#Allgemein.md) ausgewählt wurde.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainCoincident.svg" width=16px> [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainCoincident.svg" width=16px> KoinzidentFestlegen** auswählen.
    -   Das Tastaturkürzel **C**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Punkte auswählen.
    -   Zwei Kanten von Kreisen, Kreisbögen, Ellipsen oder Ellipsenbögen auswählen.
5.  Eine Randbedingung wird hinzugefügt.
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei oder mehr Punkte auswählen.
    -   Zwei oder mehr Kanten von Kreisen, Kreisbögen, Ellipsen oder Ellipsenbögen auswählen.
2.  Das Werkzeug wie oben beschrieben aufrufen.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Hinweise

-    {{Version/de|1.0}}: Punkte denen die Randbedingung Koinzident festlegen zugeornet ist, werden mit der [Farbe](Sketcher_Preferences/de#Darstellung.md) der **Symbole für Randbedingungen** gekennzeichnet.



## Skripten

Die Randbedingung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit dem folgenden Befehl erstellt werden:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

wobei :

-    `Sketch`ein Skizzenobjekt ist.

-    `LineFixed`die Nummer der Linie ist, die sich durch die Anwendung der Randbedingung nicht bewegt.

-    `PointOfLineFixed`bestimmt, welcher Knoten der Linie `LineFixed` die Randbedingung erfüllen muss.

-    `LineMoving`die Nummer der Zeile ist, die sich durch Anwendung der Randbedingung bewegt.

-    `PointOfLineMoving`bestimmt, welcher Knoten der Linie `LineMoving`, die Randbedingung erfüllen muss.

Wie die Namen `LineFixed` und `LineMoving` andeuten, bleibt, wenn sich beide beteiligten Knoten frei in jede Richtung bewegen können, der erste (in der GUI zuerst ausgewählte) fest und der andere bewegt sich. Sind jedoch weitere Randbedingungen vorhanden, dürfen sich beide Kanten bewegen.

Die Seite [Sketcher Skripten](Sketcher_scripting/de.md) erklärt die Werte, die für `LineFixed`, `PointOfLineFixed`, `LineMoving` und `PointOfLineMoving` verwendet werden können, und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/de
