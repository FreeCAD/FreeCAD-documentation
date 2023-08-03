---
 GuiCommand:
   Name: PartDesign Boolean
   Name/de: PartDesign Boolesche Operation
   MenuLocation: Part Design , Boolesche Operation
   Workbenches: PartDesign_Workbench/de
   Version: 0.17
---

# PartDesign Boolean/de

## Beschreibung

**PartDesign Boolesche Operation** importiert einen oder mehrere [PartDesign-Körper (Bodies)](PartDesign_Body/de.md) oder [PartDesign-Klone](PartDesign_Clone/de.md) (hier \"Werkzeugkörper\" genannt) in den aktiven PartDesign-Körper und führt eine Boolesche Operation durch (Vereinigung, Differenz oder Schnitt ).

![](images/PartDesign_Boolean_example.png )



*Links der aktive Körper (A) mit den Werkzeugkörpern (B) und (C); Rechts das Ergebnis nach der Booleschen Operation Differenz.*

## Anwendung

1.  Den [Körper aktivieren](PartDesign_Body/de#Aktiver_Status.md), der das Boolean-Objekt erhalten soll. ***Hinweis**: Es ist wichtig, dass weder der aktive Körper noch eines der darin enthaltenen Elemente ausgewählt sind!*

2.  Die Schaltfläche **<img src="images/PartDesign_Boolean.svg" width=24px> '''Boolesche Operation'''** drücken.

3.  Unter **Boolesche Parameter**, klickt man auf die Schaltfläche **Körper hinzufügen**. Der aktive Körper verschwindet vorübergehend aus der [3D-Ansicht](3D_view/de.md), um die Auswahl von Werkzeugkörpern zu erleichtern.

4.  In der 3D-Ansicht den Körper auswählen, der in dem Boolean-Objekt verwendet werden soll. Diesen Vorgang wiederholen, um weitere Körper hinzuzufügen.

5.  Den Typ der Booleschen Operation im Auswahlmenü auswählen (Vereinigung, Differenz oder Schnitt).

6.  
    **OK**klicken.

Alternativ können ein oder mehrere Körper vor dem Drücken der Schaltfläche Boolesche Operation ausgewählt werden; sie werden dann automatisch hinzugefügt.

## Optionen

-   **Vereinigung:** Verbindet den/die Werkzeugkörper mit dem aktiven Körper.
-   **Differenz:** Zieht den/die Werkzeugkörper vom aktiven Körper ab.
-   **Schnitt:** Extrahiert die Überschneidung der/des gewählten Körper(s) mit dem aktiven Körper.
-   Die Schaltfläche **Körper entfernen** drücken, um einen Körper durch Auswahl in der [3D-Ansicht](3D_view/de.md) zu entfernen.

## Eigenschaften

-    {{PropertyData/de|Type}}: legt die Boolesche Operation (Vereinigung, Differenz, Schnitt) fest.

-    {{PropertyData/de|Label}}: Name, der der Operation gegeben wurde, dieser Name kann nach Belieben geändert werden.

-    {{PropertyData/de|Group}}: Listet die Werkzeugkörper auf.

-    {{PropertyView/de|Display}}: Setzt einen von zwei Anzeigemodi:

    -   Result (Standard): Zeigt das Ergebnis des Boolean-Objekts an. In diesem Modus können die Werkzeugkörper nicht in ihrem ursprünglichen Zustand angezeigt werden, selbst wenn ihre Sichtbarkeit eingeschaltet ist.
    -   Tools: zeigt die Werkzeugkörper in ihrem ursprünglichen Zustand an. Dieser Modus ist nützlich, wenn die Werkzeugkörper bearbeitet werden müssen, oder für spätere Bearbeitungen verwendet werden sollen.

-    {{PropertyView/de|Selectable}}: true oder false. Wenn auf \"false\" gesetzt, kann das Objekt nicht in der 3D-Ansicht ausgewählt werden.

-    {{PropertyView/de|Sichtbarkeit}}: true oder false. Schaltet die Sichtbarkeit des Objekts in der 3D-Ansicht um.

## Begrenzungen

-   Damit Schnitt mit mehr als einem Werkzeugkörper arbeiten kann, müssen sich alle untereinander und mit dem aktiven Körper überschneiden.
-   Werkzeugkörper übernehmen den lokalen Ursprung des aktiven Körpers. Wenn sich der aktive Körper nicht bei (0,0,0) im globalen Koordinatensystem befindet, muss die Positionierung der Werkzeugkörper relativ zum aktiven Körper erfolgen. Es kann einfacher sein, die Positionierung des aktiven Körpers am Ursprung zu belassen, bevor das Boolean-Objekt angewendet wird, als seine Positionierung zu ändern.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Boolean/de
