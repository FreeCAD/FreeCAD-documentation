---
- GuiCommand:
   Name:Part Tube
   Name/de:Part Rohr
   MenuLocation:Part → Grundkörper → Rohr erstellen
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.19
   SeeAlso:[Part ErstelleGrundkörper](Part_CreatePrimitives/de.md)
---

## Beschreibung

Der Befehl Rohr fügt ein Rohr in das aktive Dokument ein. Das Rohr wird geometrisch als ein Schnitt eines kleineren Zylinders in einen größeren behandelt. Standardmäßig fügt der Befehl ein 10 mm hohes Rohr mit einem Außenradius von 5 mm und einem Innenradius von 2 mm ein. Diese Parameter können geändert werden, nachdem das Objekt hinzugefügt wurde.

![Bildschirmfoto eines Rohrs](images/Part_Tube-screenshot.png )

## Anwendung

Um ein Rohr zu erstellen, entweder:

-   drücke die **<img src="images/Part_Tube.svg" width=16px> '''Rohr'''** Taste in der Werkzeugleiste
-   verwende das Menü **Part → Grundkörper → Rohr erstellen**

Um das Rohr zu bearbeiten

-   entweder
    -   wähle es im Baum aus und doppelklicke darauf
    -   bearbeite die Parameter im erscheinenden Dialog
-   oder verwende den [ Eigenschaftseditor](Property_Editor/de.md), um die Parameter zu bearbeiten

## Eigenschaften

-   Über den [ Eigenschafteneditor](Property_Editor/de.md):
    -   **Höhe:** Legt die Höhe fest (Standardwert ist 10 mm).
    -   **Innerer Radius:** Legt den inneren Radius fest (Standardwert ist 2 mm).
    -   **Außenradius:** Legt den Außenradius fest (Standardwert ist 5 mm).
    -   **Platzierung:** Legt die Ausrichtung und Position der Box im 3D Raum fest. Siehe [ Platzierung](Placement/de.md). Der Bezugspunkt ist die linke vordere untere Ecke des Kastens.
    -   **Beschriftung:** Die Beschriftung ist der Name, der der Operation gegeben wird. Dieser Name kann nach Belieben geändert werden.





 
