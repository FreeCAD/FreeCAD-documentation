---
- GuiCommand:/de
   Name:Assembly3 MovePart
   Name/de:Assembly3 TeilBewegen
   Icon:Assembly_Move.svg
   MenuLocation:Assembly3 → Move part
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
   Shortcut:**A** dann **M**
---

# Assembly3 MovePart/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_Move.svg‎‎  style="width:24px;"> [Move part](Assembly3_MovePart.md) stellt ein Werkzeug zum Bewegen eines Teils unter Berücksichtigung der Baugruppenzsammenhänge zur Verfügung.  Es besteht aus 3 Ringen zum Drehen des Teils und 6 Anfassern (gekreuzte Doppelpfeile) zum Verschieben des Teils ohne Drehung.  Die Lage und Ausrichtung der Ringe und Anfasser richtet sich nach dem lokalen Koordinatensystem (LKS) des ausgewählten Objekts.

<img alt="" src=images/Assembly3_MovePart.png  style="width:400px;">

## Anwendung

1.  Eine Fläche, eine Kante oder einen Eckpunkt des 3D-Teils oder das ganze Teil in der Baumansicht auswählen.
2.  Den Befehl <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> **Teil bewegen** aktivieren durch:
    -   Die Schaltfläche **<img src="images/Assembly_Move.svg‎‎" width=16px> [Teil bewegen](Assembly3_MovePart/de.md)**.
    -   Den Menüeintrag **Assembly3 → <img src="images/Assembly_Move.svg‎‎" width=16px> Teil bewegen**.
    -   Das Tastenkürzel: **A** dann **M**.
3.  An den Ringen und Anfassern ziehen, um die Lage des Teils zu verändern.
4.  Die **Esc**-Taste drücken, um die Lage festzusetzen und das Werkzeug zu beenden.

## Hinweise

Die Anfasser bewegen das Teil parallel zu einer der Basisebenen des LKS des gewählten Objekts; das Drücken und Halten der **shift**-Taste schränkt die Bewegung auf eine Achse ein.

---
[documentation index](../README.md) > Assembly3 MovePart/de
