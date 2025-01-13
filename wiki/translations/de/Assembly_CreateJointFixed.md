---
 GuiCommand:
   Name: Assembly CreateJointFixed
   Name/de: Assembly StarreVerbindungErstellen
   MenuLocation: Assembly , Starre Verbindung erstellen
   Workbenches: Assembly_Workbench/de
   Shortcut: **F**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointFixed/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:24px;"> [Assembly StarreVerbindungErstellen](Assembly_CreateJointFixed/de.md) erstellt eine Verbindung zwischen zwei Bauteilen, die keine Verschiebung oder Drehung zulässt.



## Anwendung

1.  Wahlweise zwei geometrsche Elemente zweier verschiedener Bauteile auswählen. Andere Auswahlen werden nicht verarbeitet.
2.  Es gibt mehrere Möglichkeiten, dieses Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Assembly_CreateJointFixed.svg" width=16px> [Starre Verbindung erstellen](Assembly_CreateJointFixed/de.md)** drücken.
    -   Den Menüeintrag **Assembly → <img src="images/Assembly_CreateJointFixed.svg" width=16px> Starre Verbindung erstellen** auswählen.
    -   Das Tastaturkürzel **F**.
3.  Vorausgewählte Bauteile werden so bewegt, dass sie sich an ihren ausgewählten Elementen treffen.
4.  Der Dialog **Verbindung erstellen** wird im [Aufgaben-Fenster](Task_panel/de.md) geöffnet und listet die vorausgewählten Elemente.
5.  Wahlweise die Art der Verbindung in der Ausklappliste ändern:
    -   **Starr** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
        2.  Die Bauteile werden so bewegt, dass sie sich an ihren ausgewählten Elementen treffen.
        3.  Wahlweise einen Wert für *Versatz* eingeben.
        4.  Wahlweise einen Wert für *Drehwinkel* eingeben.
        5.  Wahlweise **<img src="images/Button_sort.svg" width=16px>** drücken, um die Richtung der Verbindung umzukehren.
    -   **Drehverbindung** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
        2.  Die Bauteile werden so bewegt, dass sie sich an ihren ausgewählten Elementen treffen.
        3.  Wahlweise einen Wert für *Versatz* eingeben.
        4.  Wahlweise **<img src="images/Button_sort.svg" width=16px>** drücken, um die Richtung der Verbindung umzukehren.
        5.  Wahlweise die Option **Minimaler Winkel** aktivieren und einen Wert eingeben.
        6.  Wahlweise die Option **Maximaler Winkel** aktivieren und einen Wert eingeben.
    -   **Zylindrische Verbindung** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
        2.  Wahlweise **<img src="images/Button_sort.svg" width=16px>** drücken, um die Richtung der Verbindung umzukehren.
        3.  Wahlweise die Option **Minimale Länge** aktivieren und einen Wert eingeben.
        4.  Wahlweise die Option **Maximale Länge** aktivieren und einen Wert eingeben.
        5.  Wahlweise die Option **Minimaler Winkel** aktivieren und einen Wert eingeben.
        6.  Wahlweise die Option **Maximaler Winkel** aktivieren und einen Wert eingeben.
    -   **Gleitverbindung** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
        2.  Wahlweise einen Wert für *Drehwinkel* eingeben.
        3.  Wahlweise **<img src="images/Button_sort.svg" width=16px>** drücken, um die Richtung der Verbindung umzukehren.
        4.  Wahlweise die Option **Minimale Länge** aktivieren und einen Wert eingeben.
        5.  Wahlweise die Option **Maximale Länge** aktivieren und einen Wert eingeben.
    -   **Kugelverbindung** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
    -   **Abstand** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
        2.  Wahlweise einen Wert für *\'Abstand* eingeben.
        3.  Wahlweise **<img src="images/Button_sort.svg" width=16px>** drücken, um die Richtung der Verbindung umzukehren.
    -   **Parallel** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
        2.  Wahlweise **<img src="images/Button_sort.svg" width=16px>** drücken, um die Richtung der Verbindung umzukehren.
    -   **Rechtwinklig**auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
    -   **Winkel**.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente auswählen.
        2.  Wahlweise einen Wert für *Winkel* eingeben.
    -   **Zahnstange-Ritzel** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente zweier unterschiedlicher Bauteile auswählen, die zuvor verwendet wurden, um eine Gleitverbindung und eine Drehverbindung festzulegen. (Gleitrichtung und Drehachse müssen rechtwinklig zueinander verlaufen)
        2.  Wahlweise einen Wert für *Steigungsradius* eingeben.
    -   **Spindel** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente zweier unterschiedlicher Bauteile auswählen, die zuvor verwendet wurden, um eine Gleitverbindung und eine Drehverbindung festzulegen. (Gleitrichtung und Drehachse müssen parallel zueinander verlaufen)
        2.  Wahlweise einen Wert für *Steigungsradius* eingeben.
    -   **Zahnräder** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente zweier unterschiedlicher Bauteile auswählen, die zuvor verwendet wurden, um zwei unterschiedliche Drehverbindungen festzulegen.
        2.  Wahlweise einen Wert für *Radius 1* eingeben.
        3.  Wahlweise einen Wert für *Radius 2* eingeben.
        4.  Wahlweise die Option **Drehrichtung umkehren** aktivieren/deaktivieren. (Deaktivieren wählt die Option **Riemen** aus) - funktioniert bisher nicht für 1.0 RC
    -   **Riemen** auswählen.
        1.  Wenn die Auswahlliste leer ist: Zwei geometrische Elemente zweier unterschiedlicher Bauteile auswählen, die zuvor verwendet wurden, um zwei unterschiedliche Drehverbindungen festzulegen.
        2.  Wahlweise einen Wert für *Radius 1* eingeben.
        3.  Wahlweise einen Wert für *Radius 2* eingeben.
        4.  Wahlweise die Option **Drehrichtung umkehren** aktivieren/deaktivieren. (aktivieren wählt die Option **Zahnräder** aus) - funktioniert bisher nicht für 1.0 RC
6.  Die Bauteile werden so bewegt, dass sie sich an ihren ausgewählten Elementen treffen.
7.  Die Schaltfläche **OK** drücken um das Werkzeug zu beenden.



## Hinweise

-   Eine starre Verbindung kann als Antrieb zur Steuerung der Bewegung von kinematische Simulationen eingesetzt werden. Mausradaktionen im Aufgaben-Fenster werden direkt in neue Positionen der verbundenen Bauteile umgesetzt.
    -   Versatz bewirkt Bewegung entlang der lokalen Z-Achse; negative Versatzwerte werden akzeptiert.
    -   Drehung erfolgt um die lokale Z-Achse, Winkel \> 360° und sogar negative Winkel werden akzeptiert.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein **Fixed**-Objekt wird von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Joint}}

-    {{PropertyData/de|Activated|Bool}}: Dies zeigt an, ob die Verbindung aktiv ist.

-    {{PropertyData/de|Distance|Float}}: Dies ist der Abstand der Verbindung. Er wird nur für die Verbindungen Abstand, Zahnstange-Ritzel (Steigungsradius), Spindel, Zahnräder und Riemen (Radius1) eingesetzt.

-    {{PropertyData/de|Distance2|Float}}: Dies ist der zweite Abstand der Verbindung. Er wird nur für die Verbindungen Zahnräder und Riemen (Radius2) eingesetzt.

-    {{PropertyData/de|Joint Type|Ennumeration}}: Die Art der Verbindung. ({{Value|Fixed}}, {{Value|Revolute}}, {{Value|Cylindrical}}, {{Value|Slider}}, {{Value|Ball}}, {{Value|Distance}}, {{Value|Parallel}}, {{Value|Perpendicular}}, {{Value|Angle}}, {{Value|RackPinion}}, {{Value|Screw}}, {{Value|Gears}}, {{Value|Belt}})

-    {{PropertyData/de|Offset|Vector}}: Dies ist der Versatzvektor dieser Verbindung.

-    {{PropertyData/de|Rotation|Float}}: Dies ist der Drehwinkel dieser Verbindung.


{{TitleProperty|Joint Connector 1}}

-    {{PropertyData/de|Detach1|Bool}}: Dies verhindert das Neuberechnen von Placement1 und ermöglicht dessen Position selbst zu bestimmen.

-    {{PropertyData/de|Placement1|Placement}}: Dies ist das lokale Koordinatensystem innerhalb des Objekts von Reference1, das für die Verbindung eingesetzt wird.

-    {{PropertyData/de|Reference1|XlinkSubHidden}}: Die erste Referenz der Verbindung.

Entfallene Eigenschaften:

-    {{PropertyData/de|Element1|String}}: Das ausgewählte Element des ersten Objekts.

-    {{PropertyData/de|Object1|String}}: Das erste Objekt der Verbindung.

-    {{PropertyData/de|Part1|Link}}: Das erste Bauteil der Verbindung.

-    {{PropertyData/de|Vertex1|String}}: Der ausgewählte Knoten des ersten Objekts.


{{TitleProperty|Joint Connector 2}}

-    {{PropertyData/de|Detach2|Bool}}: Dies verhindert das Neuberechnen von Placement2 und ermöglicht dessen Position selbst zu bestimmen.

-    {{PropertyData/de|Placement2|Placement}}: Dies ist das lokale Koordinatensystem innerhalb des Objekts von Reference2, das für die Verbindung eingesetzt wird.

-    {{PropertyData/de|Reference2|XlinkSubHidden}}: Die zweite Referenz der Verbindung.

Entfallene Eigenschaften:

-    {{PropertyData/de|Element2|String}}: Das ausgewählte Element des zweiten Objekts.

-    {{PropertyData/de|Object2|String}}: Das zweite Objekt der Verbindung.

-    {{PropertyData/de|Part2|Link}}: Das zweite Bauteil der Verbindung.

-    {{PropertyData/de|Vertex2|String}}: Der ausgewählte Knoten des zweiten Objekts.


{{TitleProperty|Limits}}

-    {{PropertyData/de|Angle Max|Float}}: Dies ist der obere Grenzwert des Winkels zwischen den beiden Koordinatensystemen (zwischen ihren X-Achsen).

-    {{PropertyData/de|Angle Min|Float}}: Dies ist der untere Grenzwert des Winkels zwischen den beiden Koordinatensystemen (zwischen ihren X-Achsen).

-    {{PropertyData/de|Enable Angle Max|Bool}}: Aktiviert den Grenzwert **Maximaler Winkel** der Verbindung.

-    {{PropertyData/de|Enable Angle Min|Bool}}: Aktiviert den Grenzwert **Minimaler Winkel** der Verbindung.

-    {{PropertyData/de|Enable Length Max|Bool}}: Aktiviert den Grenzwert **Maximale Länge** der Verbindung.

-    {{PropertyData/de|Enable Length Min|Bool}}: Aktiviert den Grenzwert **Minimale Länge** der Verbindung.

-    {{PropertyData/de|Length Max|Float}}: Dies ist der obere Grenzwert des Abstandes zwischen den beiden Koordinatensystemen (entlang ihrer Y-Achsen).

-    {{PropertyData/de|Length Min|Float}}: Dies ist der untere Grenzwert des Abstandes zwischen den beiden Koordinatensystemen (entlang ihrer Y-Achsen).

Entfallene Eigenschaften:

-    {{PropertyData/de|Enable Limits|Bool}}: Verwendet diese Verbindung Grenzwerte?





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointFixed/de
