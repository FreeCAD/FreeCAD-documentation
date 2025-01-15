---
 GuiCommand:
   Name: Sketcher Clone
   Name/de: Sketcher Klonen
   MenuLocation: Sketch , Skizzen-Werkzeuge , Klonen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **L**
   Version: 0.16
   SeeAlso: Sketcher_Copy/de, Sketcher_Move/de
---

# Sketcher Clone/de



## Beschreibung

Der Befehl <img alt="" src=images/Sketcher_Clone.svg  style="width:16px;"> [Sketcher Klonen](Sketcher_Clone/de.md) klont die ausgewählten Skizzenelemente von einem Punkt an einen anderen, wobei der zuletzt gewählte Punkt als Referenzpunkt dient. Wenn die Quellelemente Beschränkungen enthalten, werden die neuen Beschränkungen mit den Quellbeschränkungen verbunden; wenn Beschränkungen in der Quelle verändert werden, ändern sich auch die Beschränkungen im Ziel. Um diese Verknüpfung zu vermeiden, siehe **[<img src=images/Sketcher_Copy.svg style="width:16px">[Skizzierer Kopieren](Sketcher_Copy/de.md)**.

Ein Klon eines Klons wird eine [Kopie](Sketcher_Copy/de.md). Wenn verbundene Beschränkungen erstellt werden sollen, sind die ursprünglichen Quellelemente zu klonen.



## Anwendung

1.  Die zu klonenden Skizzenelemente auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_Clone.svg style="width:16px"> [Klonen](Sketcher_Clone/de.md)** drücken.
    -   Den Menüeintrag **Sketch → Skizzen-Werkzeuge  → <img src="images/Sketcher_Clone.svg" width=16px> Klonen** auswählen.
3.  Die Maus in der [3D-Ansicht](3D_view/de.md) auf die gewünschte Position für den Klon bewegen.Wird **Shift** gedrückt gehalten, kann der Winkel um den Einsetzpunkt in 5°-Schritten angepasst werden. {{Version/de|0.20}}
4.  Mit der linken Maustaste in die 3D-Ansicht klicken, um den Klon zu erstellen.

Es werden keine zusätzlichen Randbedingungen für den Klon hinzugefügt.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Clone/de
