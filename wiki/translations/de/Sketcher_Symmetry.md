---
 GuiCommand:
   Name: Sketcher Symmetry
   Name/de: Sketcher Symmetrie
   MenuLocation: Skizze , Skizzenwerkzeuge , Symmetrie
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **S**
   Version: 0.16
   SeeAlso: Sketcher_MirrorSketch/de
---

# Sketcher Symmetry/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Symmetry.svg  style="width:24px;"> [Sketcher Symmetrie](Sketcher_Symmetry/de.md) erstellt gespiegelte Kopien von ausgewählten Elementen.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Eine oder mehrere Kanten und/oder Punkte auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Symmetry.svg" width=16px> [Symmetrie](Sketcher_Symmetry/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzenwerkzeuge → [<img src=images/Sketcher_Symmetry.svg style="width:16px"> Symmetrie** auswählen.
    -   Das Tastaturkürzel **Z** dann **S**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Der Abschnitt **Symmetrie-Parameter** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) hinzugefügt.
5.  Wahlweise die **U**-Taste drücken oder die CheckBox **Originalgeometrien löschen** aktivieren, um nur die gespiegelten Elemente zu behalten; {{Version/de|1.0}}.
6.  Wahlweise die **J**-Taste drücken oder die CheckBox **Erzeuge Symmetrie-Randbedingungen** aktivieren, um eine Randbedingung [Symmetrisch festlegen](Sketcher_ConstrainSymmetric.md) zwischen jedem originalen Punkt und dem dazugehörigen gespiegelten Punkt hinzuzufügen; {{Version/de|1.0}}.
7.  Eine Linie oder eine Skizzenachse auswählen, um die Symmetrieachse festzulegen oder einen Punkt, um den Symmetriepunkt festzulegen.
8.  Gespiegelte Kopien werden erstellt. Randbedingungen, die ausschließlich den ausgewählten Elementen zugeordnet sind werden auch übertragen.
    -   Wenn **Erzeuge Symmetrie-Randbedingungen** ausgewählt wurde, werden Randbedingungen zum Symmetrisch-Festlegen hinzugefügt.
    -   Wenn **Originalgeometrien löschen** ausgewählt wurde, wird die Originalgeometrie entfernt.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Symmetry/de
