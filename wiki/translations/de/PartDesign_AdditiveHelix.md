---
- GuiCommand:
   Name:PartDesign AdditiveHelix
   Name/de:PartDesign WendelHinzufügen
   MenuLocation:Part Design - Objekte hinzufügen - Wendel
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.19
   SeeAlso:[PartDesign WendelEntfernen](PartDesign_SubtractiveHelix/de.md)
---

# PartDesign AdditiveHelix/de

## Beschreibung

Das Werkzeug **WendelHinzufügen** erstellt einen Volumenkörper durch Führen einer Skizze entlang eines Wendel-Pfades.

<img alt="" src=images/PartDesign_AdditiveHelix_example_overview.png  style="width:650px;">

\"Das Profil (B) wird um eine Achse (A) geführt und erzeugt einen Wendel-Volumenkörper (C)\"

## Anwendung

1.  Die Skizze (Sketch) auswählen, die zu einer Wendel ausgetragen werden soll. Alternativ kann eine Fläche des schon vorhandenen Volumenkörpers ausgewählt werden.

2.  Die Schaltfläche **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [Wendel](PartDesign_AdditiveHelix/de.md)** drücken.

3.  Parameter für die Wendel festlegen (siehe nächsten Abschnitt).

4.  Die Wendel in der 3D-Ansicht überprüfen, um sicherzustellen, dass sich die Wendel nicht selbst durchdringt.

5.  
    **OK**klicken.

## Optionen

Beim Erstellen einer Wendel beinhaltet der Dialog **Wendel-Parameter** verschiedene Parameter die festlegen, wie die Skizze ausgetragen werden soll.

![](images/PartDesign_AdditiveHelix_taskpanel.png )

### Achse

Diese Option bestimmt die Achse, um die sich die Skizze winden soll.

-   **Senkrecht zur Skizze**: Wählt die Normale der Skizze, die durch den Skizzenursprung verläuft, als Achse aus. {{Version/de|0.20}}
-   **Vertikale Skizzenachse**: Wählt die vertikale Skizzenachse. Dies ist die Voreinstellung für neue Wendeln.
-   **Horizontale Skizzenachse**:Wählt die horizontale Skizzenachse.
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

### Ansicht aktualisieren 

Wenn aktiviert, ändert sich die Ansicht bei jeder Parameteränderung automatisch.

## Einstellungen

Eine Wendel, die sich nicht selbst durchdringt, ist sichtbar, wenn **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → PartDesign → AdditiveHelixPreview** auf `True` gesetzt ist. Die Voreinstellung ist `False`. {{Version/de|0.20}}

## Eigenschaften

-    {{PropertyData/de|Pitch}}: Der axiale Abstand zwischen zwei Windungen.

-    {{PropertyData/de|Height}}: Die Gesamtlänge der Wendel (ohne Berücksichtigung der Ausdehnung des Profils)

-    {{PropertyData/de|Turns}}: Die Anzahl der Windungen (muss keine Ganzzahl sein).

-    {{PropertyData/de|Left Handed}}: Siehe [Linksgängig](#Linksgängig.md).

-    {{PropertyData/de|Reversed}}: Siehe [Umgekehrt](#Umgekehrt.md).

-    {{PropertyData/de|Winkel}}: Der Winkel mit dem der Radius der Wendel zu- oder abnimmt. Zulässiger Wertebereich: \[-89°, +89°\].

-    {{PropertyData/de|Reference axis}}: Die Wendelachse.

-    {{PropertyData/de|Mode}}: Die Eingabeart der Wendel: (pitch-height, pitch-turns, turns-height)

-    {{PropertyData/de|Outside}}: Nicht genutzt (wird in WendelAbziehen genutzt).

-    {{PropertyData/de|Has Been Edited}}: Wenn \"false\", wird ein Startwert für die Steigung auf Basis der \"Bounding-Box\" des Profils vorgeschlagen, um eine Selbstdurchdringung zu vermeiden.

-    {{PropertyData/de|Refine}}: true oder false. Wenn auf \"true\" gesetzt, wird der Volumenkörper von (innerhalb von Flächen liegenden) verbliebenen Kanten befreit, die von Formelementen hinterlassen wurden. Siehe [Part FormAufbereiten](Part_RefineShape/de.md) für weitere Details.

-    {{PropertyData/de|Profile}}: Entweder eine Skizze mit einer geschlossenen Kontur oder eine Fläche.

-    {{PropertyData/de|Midplane}}: Nicht genutzt.

-    {{PropertyData/de|Up to face}}: Nicht genutzt.

-    {{PropertyData/de|Allow multiple face}}: Nicht genutzt.

## Beispiele

![Beispielwendel, die eine [B-Spline](images/Sketcher_CreateBSpline/de.md)-Kurve einer Skizze verwendet](PartDesign_AdditiveHelix_example_bspline.png )

![Beispielwendel mit einer Wendelachse, die normal zur Skizzenebene liegt, ergibt einen \"Block mit Dreh-Effekt\".](images/PartDesign_AdditiveHelix_example_twisting_pad.png )





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveHelix/de
