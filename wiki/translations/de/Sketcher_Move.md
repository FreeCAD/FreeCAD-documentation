---
 GuiCommand:
   Name: Sketcher Move
   Name/de: Sketcher Verschieben
   MenuLocation: Sketch , Skizzen-Werkzeuge , Verschieben
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **M**
   Version: 0.18
   SeeAlso: Sketcher_Clone/de, Sketcher_Copy/de
---

# Sketcher Move/de



## Beschreibung

Der Befehl <img alt="" src=images/Sketcher_Move.svg  style="width:16px;"> [Sketcher Verschieben](Sketcher_Move/de.md) verschiebt die ausgewählten Skizzenelemente von einem Punkt zum anderen, wobei der zuletzt ausgewählte Punkt als Referenz verwendet wird.

![](images/sketcher_move.png‎ )



*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt. Ein Element '''A''' auswählen; Es erscheint eine durch zwei rote Linien gekennzeichnete  Vektorlinie, die vom Ausgangspunkt '''A''' zum Mauszeiger mit Positionsnummer '''2''' verläuft. Zieht man den Mauszeiger auf die Zielposition '''3''', wird das Element nun als '''B''' dargestellt und automatisch auf Punkt '''3''' (koinzident) festgelegt.*



## Anwendung

1.  Skizzenelemente für den Verschiebevorgang auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_Move.svg style="width:16px"> [Verschieben](Sketcher_Move/de.md)** drücken.
    -   Das Tastaturkürzel **Z** dann **M**.
    -   Den Menüeintrag **Skizze → Skizzen-Werkzeuge → [<img src=images/Sketcher_Move.svg style="width:16px"> Verschieben** auswählen.
3.  Den Mauszeiger in der [3D-Ansicht](3D_view/de.md) auf die gewünschten Position bewegen.Wird die **Ctrl**-Taste (**Cmd** in macOS) gedrückt gehalten, kann der zur Position gehörige Winkel in 5° Schritten eingestellt werden. {{Version/de|0.20}}
4.  Mit einem Links-Klick in der 3D-Ansicht wird die Verschiebung abgeschlossen. Vorhandene Randbedingungen werden ebenfalls verschoben.
5.  Soll ein Element gelöst und frei bewegt werden, löscht man seine festhaltenden Randbedingungen und verschiebt es mit der Maus.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Move/de
