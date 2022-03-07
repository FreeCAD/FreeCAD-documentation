---
- GuiCommand:/de
   Name:PartDesign Boolean
   Name/de:PartDesign Boolesche Operation
   MenuLocation:Part Design → Boolesche Operation
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
---

# PartDesign Boolean/de

## Beschreibung

**PartDesign Boolesche Operation** importiert einen oder mehrere [PartDesign Körper (Body)](PartDesign_Body/de.md) oder [PartDesign Klone](PartDesign_Clone/de.md) (vorgesehen als \"Werkzeugkörper\") in den aktiven PartDesign Körper und führt eine Boolesche Operation aus: Vereinigung, Differenz oder Schnitt (nur gemeinsame Volumenelemente bleiben erhalten).

![](images/PartDesign_Boolean_example.png )



*Links der aktive Körper (A) mit den Werkzeugkörpern (B) und (C); Rechts das Ergebnis nach dem Ausführen der Booleschen Operation Differenz.*

## Anwendung

1.  [Aktiviere den Körper](PartDesign_Body#Active_status.md), der die Boolesche Eigenschaft erhalten soll. ***Hinweis**:: Es ist wichtig, dass weder der aktive Körper noch eines der darin enthaltenen Merkmale ausgewählt wird!*
2.  Drücke die **<img src="images/PartDesign_Boolean.svg" width=24px> '''Boolesche Operation'''** Schaltfläche.
3.  In **Boolesche Parameter**, klicke auf die **Körper hinzufügen** Schaltfläche. Der aktive Körper verschwindet vorübergehend aus der [3D Ansicht](3D_view/de.md) um die Auswahl des Werkzeugkörpers zu erleichtern.
4.  Wähle in der 3D Ansicht den Körper aus, der in der Booleschen Funktion verwendet werden soll. Wiederhole diesen Vorgang, um weitere Körper hinzuzufügen.
5.  Wähle den Typ der Boolesche Operation im Auswahlmenü (Veschmelzung, Schneiden oder Schnittmenge).
6.  Klicke **OK**.

Alternativ können ein oder mehrere Körper vor dem Klicken der Booleschen Schaltfläche ausgewählt werden; sie werden dann automatisch hinzugefügt.

## Optionen

-   **Verschmelzung** führt den/die Werkzeugkörper zum aktiven Körper hinzu.
-   **Schneiden:** subtrahiert den/die Werkzeugkörper vom aktiven Körper.
-   **Schnittmenge** extrahiert die Überschneidung aus dem gewählten Körper oder den Körpern mit dem aktiven Körper
-   Drücke die **Körper entfernen** Schaltfläche, um einen Körper durch Auswahl in der [3D Ansicht](3D_view/de.md) zu entfernen.

## Eigenschaften

-    {{PropertyData/de|Typ}}: legt die Boolesche Operation ( Verschmelzen, Schneiden, Schnittmenge) fest

-    {{PropertyData/de|Beschriftung}}: Name, der der Operation gegeben wurde, dieser Name kann nach Belieben geändert werden.

-    {{PropertyData/de|Gruppe}}: Listet die Werkzeugkörper auf.

-    {{PropertyView/de|Anzeige}}: Setzt die Anzeige zwischen zwei Modi:

    -   Ergebnis (Standard): Zeigt das Ergebnis der Booleschen Funktion an. In diesem Modus können die Werkzeugkörper nicht in ihrem ursprünglichen Zustand angezeigt werden, selbst wenn ihre Sichtbarkeit eingeschaltet ist.
    -   Werkzeuge: zeigt die Werkzeugkörper in ihrem ursprünglichen Zustand an. Dieser Modus ist nützlich, wenn die Werkzeugkörper bearbeitet werden müssen, oder für spätere Bearbeitungen verwendet werden.

-    {{PropertyView/de|Auswählbar}}: true oder false. Wenn auf \"false\" gesetzt, kann die Funktion nicht in der 3D Ansicht ausgewählt werden.

-    {{PropertyView/de|Sichtbarkeit}}: true oder false. Schaltet die Sichtbarkeit der Funktion in der 3D Ansicht um.

## Begrenzungen

-   Damit Schnittmenge mit mehr als einem Werkzeugkörper arbeiten kann, müssen sich alle zusammen mit dem aktiven Körper überschneiden.
-   Werkzeugkörper übernehmen den lokalen Ursprung des aktiven Körpers. Wenn sich der aktive Körper nicht bei (0,0,0) im globalen Koordinatensystem befindet, muss die Positionierung der Werkzeugkörper relativ zum aktiven Körper erfolgen. Es kann einfacher sein, die Positionierung des aktiven Körpers am Ursprung zu belassen, bevor die boolesche Funktion angewendet wird, als seine Positionierung zu ändern.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Boolean/de
