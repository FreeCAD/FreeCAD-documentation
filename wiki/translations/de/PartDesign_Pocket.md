---
- GuiCommand:/de
   Name:PartDesign Pocket
   Name/de:PartDesign Tasche
   MenuLocation:PartDesign → Erstelle ein subtraktives Formelement → Tasche
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[PartDesign Polster](PartDesign_Pad/de.md)
---

## Beschreibung

Das **Tasche**nwerkzeug schneidet einen Festkörper aus, indem es eine Skizze (oder eine Fläche des Festkörpers) auf einem geraden Pfad extrudiert und vom Festkörper subtrahiert.

![](images/PartDesign_Pocket_example.svg ) \'\'Die Skizze mit dem Profil (A) wurde an die obere Fläche des Basis-Volumenkörpers (B) angeheftet; Ergebnis nach dem Taschenschnitt auf der rechten Seite. \'\' \'\'

## Anwendung

1.  Wähle die Skizze aus, die vertieft werden soll.

    :   Die Skizze muss auf die planare Fläche eines vorhandenen Volumenkörpers oder PartDesign Formelements abgebildet werden, sonst wird eine Fehlermeldung angezeigt. {{VersionMinus|0.16}}
2.  Drücke die **<img src="images/PartDesign_Pocket.svg" width=16px> '''Tasche'''** Schaltfläche.
3.  Lege die Taschenparameter fest (siehe nächster Abschnitt).
4.  Klicke OK.

## Optionen

![](images/Pocket_options.png )

Beim Erzeugen einer Tasche bietet der Dialog **Taschenparameter** fünf verschiedene Möglichkeiten, die Länge (Tiefe) festzulegen, bis zu der die Tasche extrudiert werden soll:

### Abmessung

Gib einen numerischen Wert für die Tiefe der Tasche ein. Die Standardrichtung für die Extrusion ist in die Auflage. Extrusionen erfolgen [normal](http://en.wikipedia.org/wiki/Surface_normal) zur definierenden Skizzierebene. Negative Bemaßungen sind nicht möglich. Verwende stattdessen die Option **Umgekehrt**.

### Zuerst

Die Tasche wird bis zur ersten Fläche des Trägers in Extrusionsrichtung extrudiert. Mit anderen Worten, sie wird durch das gesamte Material schneiden, bis sie eine leere Fläche erreicht.

### Durch alles 

Die Tasche schneidet durch das gesamte Material in Extrusionsrichtung. Mit der Option **Symmetrisch zur Ebene** schneidet die Tasche durch das gesamte Material in beiden Richtungen.**Hinweis:** Aus technischen Gründen ist **Durch alles** eigentlich eine 10 Meter tiefe Tasche. Wenn Sie tiefere Taschen benötigen, verwende *Abmessung*.

### Bis zur Fläche 

Die Tasche wird bis zu einer Fläche im Auflager extrudiert, die durch Anklicken ausgewählt werden kann.

### Zwei Abmessungen 

Hier kann eine zweite Länge eingegeben werden, in der die Tasche in die entgegengesetzte Richtung (in das Auflager) ausfahren soll. Auch dies kann durch Anklicken der Option **Umgekehrt** geändert werden. <small>(v0.17)</small> 

## Begrenzungen

-   Verwende den Typ **Abmessung** oder **Durch alles**, wo immer möglich, da die anderen Typen manchmal Probleme beim Mustern verursachen.
-   Ansonsten hat die Taschen Funktion die gleichen [Begrenzungen](PartDesign_Pad/de#Begrenzungen.md) wie die Polster Funktion.

## Nützliche Verweise 

Ein [Beispiel](http://forum.freecadweb.org/viewtopic.php?f=3&t=3733&start=10) mit der Praxis im Forum.





{{PartDesign Tools navi

}} 
