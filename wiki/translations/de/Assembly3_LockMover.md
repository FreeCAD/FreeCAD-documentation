---
- GuiCommand:
   Name:Assembly3 LockMover
   Name/de:Assembly3 BewegungVerhindern
   Icon:Assembly_LockMover.svg‎‎
   MenuLocation:Assembly3 - Lock mover
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 LockMover/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_LockMover.svg  style="width:24px;"> [Bewegung verhindern](Assembly3_LockMover/de.md) Ist ein Umschalter, der verhindert, dass Einzelteile bewegt werden, wenn sie mit der Bedingung zum <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:16px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) fixiert wurden.

Wenn aktiviert, kann keines der Bewegungswerkzeuge <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> [Teil bewegen](Assembly3_MovePart/de.md), <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:16px;"> [Axial bewegen](Assembly3_AxialMove/de.md) oder <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width:16px;"> [Schnelles Bewegen](Assembly3_QuickMove/de.md) ausgewählt werden, solange die Auswahl ein festgesetztes Objekt enthält. Dies scheint nicht für 2D-Geometrie zu gelten. (siehe [Hinweise](#Hinweise.md)).

## Anwendung

1.  Den Befehl <img alt="" src=images/Assembly_LockMover.svg  style="width:16px;"> **Bewegung verhindern** aktivieren durch:
    -   Die Schaltfläche **<img src="images/Assembly_LockMover.svg" width=16px> [Bewegung verhindern](Assembly3_LockMover/de.md)**.
    -   Den Menüeintrag **Assembly3 → <img src="images/Assembly_LockMover.svg" width=16px> Bewegung verhindern**.

## Hinweise

Ausgewählte **2D-Geometrien**, wie Draft-Linien, -Bögen und -Kreise, die mit der Randbedingung Sperren festgehalten werden, deaktivieren die Bewegungswerkzeuge nicht. Während Kreise und Bögen ihre Position weiterhin beibehalten, wenn ein Bewegungswerkzeug auf sie angewendet wird, können Linien verschoben und gedreht werden.



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 LockMover/de
