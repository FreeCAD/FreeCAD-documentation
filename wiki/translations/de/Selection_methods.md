# Selection methods/de
{{TOCright}}

## Überblick

[Auswahlmethoden](Selection_methods/de.md) in FreeCAD ermöglichen das Auswählen von Objekten in der [FreeCAD-Oberfläche](Interface/de.md): z. B. [3D Ansicht](3D_view/de.md), [Baumansicht](Tree_view/de.md), [Auswahlansicht](Selection_view/de.md) und anderen Dialogen. Einige Auswahlmethoden sind Arbeitsbereich-spezifisch und in der jeweiligen Arbeitsbereich-Dokumentation dokumentiert.

## 3D Ansicht 

In der [3D Ansicht](3D_view/de.md) gibt es verschiedene Möglichkeiten, Objekte auszuwählen.

### Einfache Auswahl 


<div class="mw-translate-fuzzy">

Die einfache Auswahl mit der Maus (standardmäßig Linksklick) und die Vorauswahl (Hover) werden auf der Seite [Mausbedienung](Mouse_Model/de.md) beschrieben.


</div>

### Wiederholte Klicks 

Mit dem ersten Klick wird ein Unterelement (Punkt, Kante oder Fläche) des Objekts unter der Maus ausgewählt. Ein zweiter Klick wählt das gesamte Objekt aus. {{Version/de|0.18}}

Der dritte Klick erweitert die Auswahl auf das Containerobjekt [Körper](PartDesign_Body/de.md), [Standard Teil](Std_Part/de.md) und andere. Weitere Klicks erweitern die Auswahl in der Containerkette. {{Version/de|0.19}}

### Auswahl Befehle 

-   Um alle Objekte auszuwählen: [Std AllesAuswählen](Std_SelectAll/de.md).
-   Um mehrere Hauptobjekte in einem Kasten auszuwählen: [Std KastenAuswahl](Std_BoxSelection/de.md).
-   Um mehrere Flächen zu auszuwählen: [Std KastenElementAuswahl](Std_BoxElementSelection/de.md) oder [Part KastenAuswahl](Part_BoxSelection/de.md).

## Auswahlansicht

In der [Auswahlansicht](Selection_view/de.md) werden die Namen der ausgewählten Objekte angezeigt, einschließlich ihres vollständigen Namens innerhalb eines Objekts, z. B. `Unnamed#Body.Box001.Face17`.

Sie erlaubt auch einige Aktionen wie [Std AnsichtAuswahlEinpassen](Std_ViewFitSelection/se.md), und das Senden des Objekts an die [Python Konsole](Python_console/de.md).

### Objekt export 

Dies sollte auf der [Auswahlansicht](selection_view/de.md) Seite stehen.\'\'

Wähle ein beliebiges komplexes Objekt, z.B. einen [PartDesign Körper](PartDesign_Body/de.md) oder ein [Std Part](Std_Part/de.md), markiere dann in der [Auswahlansicht](selection_view/de.md) erneut das Objekt und drücke dann **Strg** + **C** auf der Tastatur, um den Dialog **Objektauswahl** zu öffnen. Dies ermöglicht das Kopieren des ausgewählten Objekts zusammen mit allen oder nur einigen der abhängigen Objekte dieses Objekts. Für ein [Std Part](Std_Part/de.md) zum Beispiel umfassen die möglichen Objekte, die ausgewählt werden können, das [Std Part](Std_Part/de.md) selbst, aber auch seinen Ursprung, seine drei Basisachsen (XYZ) und seine drei Basisebenen (XY, YZ, XZ).

Nachdem **OK** drücken, werden die ausgewählten Objekte in den Speicher kopiert und können dann in das Dokument eingefügt werden, um nur diese Objekte zu duplizieren.

![](images/ObjectSelection.png )


*Objektauswahldialog, der aus der [Auswahlansicht](Selection_view/de.md) heraus gestartet wird.*

## Baumansicht

In der [Baumansicht](tree_view/de.md) können Elemente eins nach dem anderen ausgewählt oder abgewählt werden, durch gedrückt halten der **Strg** Taste und mit der Maus klicken.

Eine Reihe von Elementen kann durch klicken auf das erste Element ausgewählt werden, durch gedrückt halten der **Shift** und klicken auf das letzte Element.

Selecting a single item will also show its properties in the [property editor](property_editor.md).

Double clicking will open any associated [task panel](task_panel.md) containing actions. Make sure to close this task panel before executing another command or switching to any other workbench.

More methods are available by opening the context menu (right-click), depending on the object selected or the active workbench; see the information in [tree view](tree_view.md).

## Skripterstellung

Selecting objects is inherently a graphical task and therefore it is only available when the graphical user interface is loaded.

These commands can be used in [macros](Macros.md) or from the [Python console](Python_console.md).


```python
import FreeCADGui as Gui

Gui.Selection.addSelection
Gui.Selection.addSelectionGate
Gui.Selection.Filter
```

The command `addSelectionGate` restricts the user from selecting objects not specified in the selection string. A symbol appears when the pointer is over an item not in the specified group.


```python
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Edge")
```

See the [Source documentation](Source_documentation.md) and [Std PythonHelp](Std_PythonHelp.md) for more help on using these tools.

---
[documentation index](../README.md) > Selection methods/de
