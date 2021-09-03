---
- GuiCommand:/de
   Name:PartDesign Mirrored
   Name/de:PartDesign Gespiegelt
   MenuLocation:PartDesign → Ein Muster anwenden → Gespiegelt
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
---

## Beschreibung

Das **Gespiegelt** Werkzeug spiegelt Formelemente auf einer Ebene.

![](images/PartDesign_Mirrored_example.svg )


*Oben: Eine Taschenformelement wurde aus einer Skizze erstellt, die einen Kreis (A) enthält. Die Tasche wurde anschließend zum Erstellen eines gespiegelten Formelements verwendet. Die vertikale Skizzenachse (B) wurde als Symmetrieachse verwendet. Das Ergebnis (C) wird rechts angezeigt.*

## Anwendung

Um eine Spiegelung zu erstellen:

1.  Wähle das eine oder mehrere Formelement(e), das gespiegelt werden soll.
2.  Drücke die**<img src=images/PartDesign_Mirrored.svg style="width:24px">  '''Gespiegelt'''** Schaltfläche.
3.  Wenn du mehrere Formelement in der Spiegelung hast, kann deren Reihenfolge wichtig sein, siehe zum Beispiel das Bild in der [PolarMuster Formelement](PartDesign_PolarPattern#Usage/de.md). {{Version/de|0.19}} Du kannst die Reihenfolge ändern, indem du die Funktion in der Liste ziehst, und du siehst das Ergebnis sofort als Vorschau.

Definiere die Spiegel **Ebene**. Siehe [Optionen](#Optionen.md).

1.  Drücke **OK**.

Hinzufügen oder Entfernen von Formelementen aus einer bestehenden Spiegelung:

1.  Drücke **Formelement hinzufügen**, um ein Formelement hinzuzufügen, das gespiegelt werden soll. Das Formelement muss in der [3D Ansicht](3D_view/de.md) sichtbar sein:
    1.  Wechsle in den Modellbaum;
    2.  Wähle im Baum das hinzuzufügende Formelement aus und drücke **Leertaste**, um es in der [3D Ansicht](3D_view/de.md) sichtbar zu machen;
    3.  Wechsle zurück zum Aufgabenpaneel;
    4.  Wähle das Formelement in der 3D Ansicht; es wird der Liste hinzugefügt.
    5.  Wiederhole diesen Vorgang, um weitere Formelemente hinzuzufügen.
    6.  Drücke **Formelement entfernen**, um ein Formelement aus der Liste zu entfernen, oder rechtsklicke auf das Formelement in der Liste und wähle *Entfernen*.

## Optionen

![Mirrored parameters](images/Mirrored_parameters_v017.png )

### Ebene

Beim Erstellen einer gespiegelten Funktion bietet der Dialog \'\'\'Mirrored Parameters \'\'\'verschiedene Möglichkeiten zum Angeben der Spiegelungslinie oder -ebene.

#### Horizontale Sikzzenachse 

Nutzt die Horizontale Achse der Skizze als Symmetrieachse.

#### Vertikale Skizzenachse 

Nutzt die Vertikale Achse der Skizze als Symmetrieachse.

#### Wähle Referenz\... 

Ermöglicht die Auswahl einer Ebene (wie einer Oberfläche eines Bauteils) als Spiegelungsbene .

#### Erstellte Skizzenachse 

Wenn die Skizze, die das zu spiegelnde Formelement definiert, auch eine Konstruktionslinie (oder -linien) enthält, enthält die Dropdown-Liste eine benutzerdefinierte Skizzenachse für jede Konstruktionslinie. Die erste Konstruktionslinie trägt die Bezeichnung \"Skizzenachse 0\". Das folgende Bild zeigt ein Beispiel, bei dem die Skizze im Bearbeitungsmodus anzeigt, dass sie eine Konstruktionslinie zur Verwendung als gespiegelte Achse enthält.

![](images/PartDesign_Mirrored_axis_fromconstructionlines.jpg )

#### Basis (XY/XZ/YZ) Ebene 

Wähle eine der Standardebenen des Körperursprungs (XY, XZ or YZ).

### Vorschau

Das Spiegelungsergebnis kann in Echtzeit in der Vorschau angezeigt werden, bevor Sie auf **OK** klicken, indem Sie \"Ansicht aktualisieren\" aktivieren. 

## Begrenzungen

-   Die Spiegelungsfunktion kann keinen ganzen Festkörper spiegeln. Dafür, siehe [Formteil Spiegeln](Part_Mirror/de.md) .

-   Das gespiegelte Formelement muss das Bauteil (auch *support* genannt) schneiden auf dem es basiert, ansonsten versagt die Funktion .





{{PartDesign Tools navi

}} 
