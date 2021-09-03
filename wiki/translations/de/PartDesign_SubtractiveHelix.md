---
- GuiCommand:/de
   Name:PartDesign SubtractiveHelix
   Name/de:PartDesign Subtraktive Helix
   MenuLocation:PartDesign → Create a subtractive feature → Subtraktive Helix
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.19
   SeeAlso:[PartDesign Additive Helix](PartDesign_AdditiveHelix/de.md)
---

## Beschreibung

Das Werkzeug **Subtractive helix** erstellt einen Körper,der durch Führen einer Skizze oder eines 2D-Objekts entlang eines Helix-Pfades Material entfernt.

![](images/PartDesign_SubtractiveHelix_example_overview.png )

\"Die Skizze (B) wird um eine Achse (A) geführt und schneidet Material aus dem vorhandenem Werkstück (C)\"

## Anwendung

1.  Wähle die Skizze der in eine Helix überführt werden soll. Alternativ kann eine Fläche des zu schneidenden Körpers gewählt werden.
2.  Klicke **<img src="images/PartDesign_SubtractiveHelix.svg" width=24px> [PartDesign SubtractiveHelix](PartDesign_SubtractiveHelix.md)**.
3.  Setze die Parameter für die Helix (siehe nächsten Abschnitt)
4.  Prüfe die Helix in der Ansicht. Stelle sicher, dass sich die Helix nicht selbst überschneidet.
5.  Klicke **OK**.

## Optionen

Der Dialog **Helix parameters** bietet verschiedene Parameter an, wie die Zeichnung geführt werden soll.

![](images/PartDesign_SubtractiveHelix_taskpanel.png )

### Axis

Diese Option legt die Achse fest, um die die Skizze geführt werden soll.

-   **Vertical sketch axis**: wählt die vertikale Skizzen-Achse.
-   **Horizontal sketch axis**: wählt die horizontale Skizzen-Achse.
-   **Construction line**: wählt eine eine Konstruktionslinie der Skizze, die für die Helix genutzt wird. In der Drop-Down-Liste ist jede Konstruktionslinie vorhanden.Die erste in der Skizze erstellte Konsruktionslinie hat die Bezeichnung *Construction line 1*.
-   **Base (X/Y/Z) axis**: wählt die X, Y or Z Achse des Ursprungs des Körpers.
-   **Select reference\...**: erlaubt in der 3D-Ansicht die Auswahl einer Kante auf dem Körper oder eine [Datum Linie](PartDesign_Line.md).

### Mode


<div class="mw-translate-fuzzy">

Dieser Parameter definiert die Art der Helix. Zulässige Auswahlen sind: Pitch-Height (Steigung), Pitch-Turns (Umdrehungen) und Height-Turns (Umdrehungshöhe).


</div>

### Pitch

Der Abstand zwischen den Umdrehungen der Helix.

### Height

Die Höhe der Helix (Zentrum-Zentrum).

### Turns

Die Anzahl der Umdrehungen der Helix. Ergibt sich aus Höhe/Abstand zwischen den Umdrehungen.

### Cone Angle {#cone_angle}

Der Winkel mit dem der Radius der Helix zu- oder abnimmt. Zulässige Werte: \[-89°, +89°\].

### Left handed {#left_handed}

Wenn gewählt, ändert sich die Drehrichtung der Helix von der Voreinstellung \"im Uhrzeigersinn\" in \"gegen den Uhrzeigersinn\".

### Reversed

Wenn gewählt wird die Achsenrichtung umgedreht.

### Remove outside of profile {#remove_outside_of_profile}

Wenn gewählt, ist das Ergebnis der Überschneidung des Profils mit dem bereits existierendem Körper.

### Update view {#update_view}

Wenn gewählt, ändert sich die Ansicht bei jeder Parameteränderung automatisch.

## Einstellungen

Eine subtraktive Helix, die sich nicht selbst überschneidet ist sichtbar, wenn {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Mod → PartDesign → SubtractiveHelixPreview}} auf `True` steht. Die Voreinstellung ist `True`. <small>(v0.20)</small> 

## Eigenschaften

-    **Pitch**: Der axiale Abstand zwischen zwei Umdrehungen.

-    **Height**: Die Gesamtlänge der Helix (ohne Berücksichtigung des Umfangs des Profils)

-    **Turns**: Die Anzahl der Umdrehungen (muss keine Ganzzahl sein).

-    **Left Handed**: links drehend, gegen den Uhrzeigersinn

-    **Reversed**: true oder false. Siehe [Reversed](#Reversed.md).

-    **Angle**: Der Winkel mit dem der Radius der Helix zu- oder abnimmt. Zulässige Werte: \[-89°, +89°\].

-    **Reference axis**: Die Helix Achse.

-    **Mode**: Die Helix Eingabeart: (pitch-height, pitch-turns, turns-height)

-    **Outside**: Wenn \"true\", ist das Ergebnis der Schnitt des überstrichenen Profils und des bereits vorhandenen Körpers.

-    **Has Been Edited**: Wenn \"false\", wird ein Initialwert aufgrund der \"profile bounding box\"vorgeschlagen so dass die Selbstüberschneidung vermieden wird.

-    **Refine**: true oder false. Wenn diese Option auf \"true\" gesetzt ist, wird der Volumenkörper von den verbleibenden Kanten befreit, die von Features hinterlassen wurden. Siehe [Part RefineShape](Part_RefineShape/de.md) für weitere Details.

-    **Profile**: Entweder eine Skizze mit einer geschlossenen Kontur oder eine Fläche.

-    **Midplane**: Nicht genutzt.

-    **Up to face**: Nicht genutzt.

-    **Allow multiple face**: Nicht genutzt.





{{PartDesign Tools navi

}} 
