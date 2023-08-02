---
- GuiCommand:
   Name: PartDesign SubtractiveHelix
   Name/de: PartDesign WendelAbziehen
   MenuLocation: Part Design -> Objekte abziehen -> Wendel
   Workbenches: PartDesign_Workbench/de
   Version: 0.19
   SeeAlso: PartDesign_AdditiveHelix/de
---

# PartDesign SubtractiveHelix/de



## Beschreibung

Das Werkzeug **WendelAbziehen** ändert einen Volumenkörper durch Abziehen eines Formelements, das durch Führen einer Skizze oder eines 2D-Objekts entlang eines Wendel-Pfades entsteht.

![](images/PartDesign_SubtractiveHelix_example_overview.png )

\"Das Profil (B) wird um eine Achse (A) geführt, um eine Wendelförmige Vertiefung in das vorhandene Werkstück (C) einzubringen\"



## Anwendung

1.  Die Skizze (Sketch) auswählen, die zu einer Wendel ausgetragen werden soll. Alternativ kann eine Fläche des schon vorhandenen Volumenkörpers ausgewählt werden.

2.  Die Schaltfläche **<img src="images/_PartDesign_SubtractiveHelix.svg" width=16px> [Wendel](PartDesign_SubtractiveHelix/de.md)** drücken.

3.  Parameter für die Wendel festlegen (siehe nächsten Abschnitt).

4.  Die Wendel in der 3D-Ansicht überprüfen, um sicherzustellen, dass sich die Wendel nicht selbst durchdringt.

5.  
    **OK**klicken.



## Optionen

Beim Erstellen einer Wendel beinhaltet der Dialog **Wendel-Parameter** verschiedene Parameter die festlegen, wie die Skizze ausgetragen werden soll.

![](images/PartDesign_SubtractiveHelix_taskpanel.png )



### Achse

Diese Option bestimmt die Achse, um die sich die Skizze winden soll.

-   **Senkrecht zur Skizze**: Wählt die Normale der Skizze, die durch den Skizzenursprung verläuft, als Achse aus. {{Version/de|0.20}}
-   **Vertikale Skizzenachse**: Wählt die vertikale Skizzenachse aus.
-   **Horizontale Skizzenachse**:Wählt die horizontale Skizzenachse aus.
-   **Konstruktionslinie**: Wählt eine eine Konstruktionslinie der Skizze zur Verwendung mit der Wendel aus. Die Ausklappliste enthält für jede Konstruktionslinie einen Eintrag. Die als Erstes erstellte Konstruktionslinie wird *Konstruktionslinie 1* genannt.
-   **Basis (X/Y/Z)-Achse**: Wählt die X-, Y- oder Z-Achse des Ursprungs des Körpers aus.
-   **Referenz auswählen\...**: Erlaubt in der 3D-Ansicht eine Kante des Körpers oder eine [Bezugslinie](PartDesign_Line.md) auszuwählen.



### Modus

Dies steuert, welche Parameter zum Festlegen der Wendel verwendet werden. Zur Wahl stehen:

-   **Steigung-Höhe-Winkel**: Festlegung über die Steigung (Höhe pro Umdrehung) und die Gesamthöhe.
-   **Steigung-Windungen-Winkel**: Festlegung über die Steigung und die Anzahl der Windungen.
-   **Höhe-Windungen-Winkel**: Festlegung über die Gesamthöhe und die Anzahl der Windungen.
-   **Höhe-Windungen-Aufweitung** {{Version/de|0.20}}: Festlegung über die Gesamthöhe, die Anzahl der Windungen und die Aufweitungsrate des Wendelradius (Radiales Wachstum). Eine Höhe von Null ergibt einen spiralförmigen Pfad. Sind Höhe und Aufweitungsrate Null, ergibt sich ein kreisförmiger Pfad.



### Steigung

Der Abstand zwischen den Windungen der Wendel.



### Höhe

Die Höhe der Wendel (Zentrum-Zentrum).



### Windungen

Die Anzahl der Windungen der Wendel. Ergibt sich aus Höhe/Steigung.



### Kegelwinkel

Winkel des Kegels, der die Wendel umhüllt. Zulässiger Wertebereich: \[-89°, +89°\].



### Linksgängig

Wenn aktiviert, ändert sich die Drehrichtung der Wendel von der Voreinstellung \"im Uhrzeigersinn\" in \"gegen den Uhrzeigersinn\".



### Umgekehrt

Wenn aktiviert, wird die voreingestellte Ausrichtung der Wendel umgedreht.



### Außerhalb des Profils entfernen 

Wenn aktiviert, ist das Ergebnis das Schnittobjekt aus dem ausgetragenen Profil und dem vorhandenen Körper.



### Ansicht aktualisieren 

Wenn aktiviert, ändert sich die Ansicht bei jeder Parameteränderung automatisch.



## Einstellungen

Eine Wendel, die sich nicht selbst durchdringt, ist sichtbar, wenn **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → PartDesign → SubtractiveHelixPreview** auf `True` gesetzt ist. Die Voreinstellung ist `True`. {{Version/de|0.20}}



## Eigenschaften

-    {{PropertyData/de|Pitch}}: Der axiale Abstand zwischen zwei Windungen.

-    {{PropertyData/de|Height}}: Die Gesamtlänge der Wendel (ohne Berücksichtigung der Ausdehnung des Profils)

-    {{PropertyData/de|Turns}}: Die Anzahl der Windungen (muss keine Ganzzahl sein).

-    {{PropertyData/de|Left Handed}}: Siehe [Linksgängig](#Linksgängig.md).

-    {{PropertyData/de|Reversed}}: Siehe [Umgekehrt](#Umgekehrt.md).

-    {{PropertyData/de|Winkel}}: Der Winkel mit dem der Radius der Wendel zu- oder abnimmt. Zulässiger Wertebereich: \[-89°, +89°\].

-    {{PropertyData/de|Reference axis}}: Die Wendelachse.

-    {{PropertyData/de|Mode}}: Die Eingabeart der Wendel: (pitch-height, pitch-turns, turns-height)

-    {{PropertyData/de|Outside}}: Wenn auf \"true\" gesetzt, wird das Ergebnis das Schnittobjekt aus dem ausgetragenen Profil und dem vorhandenen Körper sein.

-    {{PropertyData/de|Has Been Edited}}: Wenn \"false\", wird ein Startwert für die Steigung auf Basis der \"Bounding-Box\" des Profils vorgeschlagen, um eine Selbstdurchdringung zu vermeiden.

-    {{PropertyData/de|Refine}}: true oder false. Wenn auf \"true\" gesetzt, wird der Volumenkörper von (innerhalb von Flächen liegenden) verbliebenen Kanten befreit, die von Formelementen hinterlassen wurden. Siehe [Part FormAufbereiten](Part_RefineShape/de.md) für weitere Details.

-    {{PropertyData/de|Profile}}: Entweder eine Skizze mit einer geschlossenen Kontur oder eine Fläche.

-    {{PropertyData/de|Midplane}}: Nicht genutzt.

-    {{PropertyData/de|Up to face}}: Nicht genutzt.

-    {{PropertyData/de|Allow multiple face}}: Nicht genutzt.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveHelix/de
