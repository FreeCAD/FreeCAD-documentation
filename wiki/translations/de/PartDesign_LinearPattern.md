---
- GuiCommand:/de
   Name:PartDesign LinearPattern
   Name/de:PartDesign Lineares Muster
   MenuLocation:PartDesign → Ein Muster anwenden → LinearesMuster
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
---

## Beschreibung

Das **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''LinearesMuster'''** Werkzeug erzeugt gleichmäßig verteilte Kopien eines Formelements in einer linearen Richtung. Ab {{VersionPlus/de|0.17}} kann das Linear Muster Werkzeug mehrere Formelemente mustern.

![](images/PartDesign_LinearPattern_example.svg )

\'Oben: Ein L-förmiger KLotz (B), das auf einem Basisklotz (A, auch als *Auflager* bezeichnet) angebracht ist, wird für ein lineares Muster verwendet. Das Ergebnis (C) ist rechts gezeigt.\'\'

## Anwendung

Um ein Muster zu erstellen:

1.  Wähle das Formelement ({{Version/de|0.19}} oder mehrere Formelemente), die gemustert werden sollen.
2.  Drücke die **<img src=images/PartDesign_LinearPattern.svg style="width:24px">  '''LinearesMuster'''** Schaltfläche.
3.  Definiere die **Richtung**. Siehe [Optionen](#Options/de.md).
4.  Definiere die **Länge** (Abstand) zwischen dem letzten kopierten Auftreten und dem Original Formelement.
5.  Lege die Anzahl der **Häufigkeiten** fest.
6.  Wenn du mehrere Formelemente im Muster hast, kann deren Reihenfolge wichtig sein, siehe z.B. das Bild im Abschnitt [PolarMuster Formelement](PartDesign_PolarPattern#Usage/de.md). {{Version/de|0.19}} Du kannst die Reihenfolge ändern, indem du das Formelement in die Liste ziehst, und du siehst das Ergebnis sofort als Vorschau.
7.  Drücke **OK**.

Zum Hinzufügen oder Entfernen von Formelementen zu einem bestehenden Muster:

1.  Drücke **Formelement hinzufügen**, um ein Formelement hinzuzufügen, das gemustert werden soll. Das Formelement muss in der [3D Ansicht](3D_view/de.md) sichtbar sein:
    1.  Wechsle in den Modellbaum;
    2.  Wähle in der Struktur das hinzuzufügende Formelement aus und drücke die **Leertaste**, um es in der [3D Ansicht](3D_view/de.md) sichtbar zu machen;
    3.  Wechsle zurück zum Aufgabenpaneel;
    4.  Wähle das Formelement in der 3D Ansicht; es wird der Liste hinzugefügt.
    5.  Wiederhole diesen Vorgang, um weitere Formelemente hinzuzufügen.
    6.  Drücke **Formelement entfernen**, um ein Formelement aus der Liste zu entfernen, oder klicke mit der rechten Maustaste auf das Formelement in der Liste und wähle **Entfernen**.

## Optionen

![Lineares Muster Parameters in v0.16 und davor.](images/Linearpattern_parameters.png ) ![Lineares Muster Parameter in v0.17 und höher.](images/Linearpattern_parameters_v017.png )

### Richtung

Bei der Erstellung eines Formelements Lineares Muster bietet der Dialog **LinearMuster Parameter** verschiedene Möglichkeiten die Richtung des Musters auszuwählen.

#### Horizontale Skizzenachse {#horizontale_skizzenachse}

Verwendet die horizontale Skizzenachse für die Richtung.

#### Vertikale Skizzenachse {#vertikale_skizzenachse}

Verwendet die vertikale Skizzenachse für die Richtung.

#### Flächennormale Skizzenachse {#flächennormale_skizzenachse}


{{VersionPlus/de|0.17}}

Verwendet die Flächennormale Skizzenachse für die Richtung.

#### Referenz auswählen\... {#referenz_auswählen...}

Ermöglicht entweder eine Bezugslinie (DatumLine) oder eine Kante eines Objekts oder eine Linie einer Skizze als Richtungsangabe zu verwenden.

#### Angepasste Skizzenachse {#angepasste_skizzenachse}

Wenn die Skizze für das zu wiederholende Muster Konstruktionslinien besitzen, werden diese Konstruktionslinien in dem Dropdown-MenüI als jeweils spezielle Achsen aufgelistet. Die erste Konstruktionslinie wird im Menü als *Konstruktionslinie 1* aufgelistet.

#### Basis (X/Y/Z) Achse {#basis_xyz_achse}


{{VersionPlus/de|0.17}}

Wähle eine der Standardachsen des Körperursprungs (X, Y oder Z) als Richtung. 


<div class="mw-translate-fuzzy">

## Begrenzungen

-   Musterformen dürfen einander nicht überlappen, außer im Sonderfall von nur zwei Vorkommen (Original plus eine Kopie)
-   Alle Musterformen, die die Auflage des Originals nicht überlappen, werden ausgeschlossen. Dies stellt sicher, dass ein PartDesign Formelement immer aus einem einzelnen, verbundenen Festkörper besteht.
-   Die PartDesign Muster sind noch nicht so optimiert wie ihre Draft Gegenstücke. Bei einer größeren Anzahl von Instanzen solltest du daher stattdessen die Verwendung von [Draft Anordnung](Draft_Array/de.md) in Kombination mit einer booleschen Part Operation in Betracht ziehen. Dies kann größere Änderungen an deinem Modell beinhalten, wenn du PartDesign verlässt, was bedeutet, dass du nicht einfach mit weiteren PartDesign Formelementen im selben Körper fortfahren kannst. Ein Beispiel wird in diesem [Forum Thema](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192) gezeigt.
-   Für weitere Begrenzungen siehe das [PartDesign Gespiegelt](PartDesign_Mirrored/de.md) Funktion


</div>





{{PartDesign Tools navi

}} 
