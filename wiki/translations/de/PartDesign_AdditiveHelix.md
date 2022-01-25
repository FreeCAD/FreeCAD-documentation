---
- GuiCommand:/de
   Name:PartDesign AdditiveHelix
   Name/de:PartDesign Additive Helix
   MenuLocation:PartDesign → Create an additive feature → Additive Helix
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.19
   SeeAlso:[PartDesign Subtraktive Helix](PartDesign_SubtractiveHelix.md)
---

# PartDesign AdditiveHelix/de

## Beschreibung

Das Werkzeug **AdditiveHelix** erstellt einen Körper durch das Führen einer Skizze entlang eines Helix-Pfades.

<img alt="" src=images/PartDesign_AdditiveHelix_example_overview.png  style="width:650px;">

\"Das Profil (B) wird um eine Achse (A) geführt und erzeugt eine geschlossene Helix (C)\"

## Anwendung

1.  Wähle die Zeichnung (Sketch) der in eine Helix überführt werden soll.
2.  Klicke **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [PartDesign AdditiveHelix](PartDesign_AdditiveHelix/de.md)
**
3.  Setze die Parameter für die Helix (siehe nächsten Abschnitt)
4.  Prüfe die Helix in der Ansicht. Stelle sicher, dass sich die Helix nicht selbst überschneidet.
5.  Klicke **OK**.

## Optionen

Der Dialog **Helix parameters** bietet verschiedene Parameter an, wie die Zeichnung geführt werden soll.

![](images/PartDesign_AdditiveHelix_taskpanel.png )

### Axis


<div class="mw-translate-fuzzy">

Diese Option legt die Achse fest, um die die Skizze geführt werden soll.

-   **Vertical sketch axis**: wählt die vertikale Skizzen-Achse.
-   **Horizontal sketch axis**: wählt die horizontale Skizzen-Achse.
-   **Construction line**: wählt eine eine Konstruktionslinie der Skizze, die für die Helix genutzt wird. In der Drop-Down-Liste ist jede Konstruktionslinie vorhanden.Die erste in der Skizze erstellte Konsruktionslinie hat die Bezeichnung *Construction line 1*.
-   **Base (X/Y/Z) axis**: wählt die X, Y or Z Achse des Ursprungs des Körpers.
-   **Select reference\...**: erlaubt in der 3D-Ansicht die Auswahl einer Kante auf dem Körper oder eine [Datum Linie](PartDesign_Line.md).


</div>

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

### Cone Angle 


<div class="mw-translate-fuzzy">

Der Winkel mit dem der Radius der Helix zu- oder abnimmt. Zulässige Werte: \[-89°, +89°\].


</div>

### Left handed 

Wenn gewählt, ändert sich die Drehrichtung der Helix von der Voreinstellung \"im Uhrzeigersinn\" in \"gegen den Uhrzeigersinn\".

### Reversed

Wenn gewählt wird die Achsenrichtung umgedreht.

### Update view 

Wenn gewählt, ändert sich die Ansicht bei jeder Parameteränderung automatisch.

## Einstellungen

Eine additive Helix, die sich nicht selbst überschneidet ist sichtbar, wenn **Tools → Edit parameters... → BaseApp → Preferences → Mod → PartDesign → AdditiveHelixPreview** auf `True` steht. Die Voreinstellung ist `False`. <small>(v0.20)</small> 

## Eigenschaften


<div class="mw-translate-fuzzy">

-    **Pitch**: Der axiale Abstand zwischen zwei Umdrehungen.

-    **Height**: Die Gesamtlänge der Helix (ohne Berücksichtigung des Umfangs des Profils)

-    **Turns**: Die Anzahl der Umdrehungen (muss keine Ganzzahl sein).

-    **Left Handed**: links drehend, gegen den Uhrzeigersinn

-    **Reversed**: true oder false. Siehe [Reversed](#Reversed.md).

-    **Angle**: Der Winkel mit dem der Radius der Helix zu- oder abnimmt. Zulässige Werte: \[-89°, +89°\].

-    **Reference axis**: Die Helix Achse.

-    **Mode**: Die Helix Eingabeart: (pitch-height, pitch-turns, turns-height)

-    **Outside**: Nicht genutzt (wird in SubtractiveHelix genutzt).

-    **Has Been Edited**: Wenn \"false\", wird ein Initialwert aufgrund der \"profile bounding box\"vorgeschlagen so dass die Selbstüberschneidung vermieden wird.

-    **Refine**: true oder false. Wenn diese Option auf \"true\" gesetzt ist, wird der Volumenkörper von den verbleibenden Kanten befreit, die von Features hinterlassen wurden. Siehe [Part RefineShape](Part_RefineShape/de.md) für weitere Details.

-    **Profile**: Entweder eine Skizze mit einer geschlossenen Kontur oder eine Fläche.

-    **Midplane**: Nicht genutzt.

-    **Up to face**: Nicht genutzt.

-    **Allow multiple face**: Nicht genutzt.


</div>

## Beispiele

![Example helix using a [B-spline](images/Sketcher_CreateBSpline.md) in the sketch](PartDesign_AdditiveHelix_example_bspline.png )

![Example helix where the helix axis is normal to the sketch plane resulting in a \"Pad with twist\" effect.](images/PartDesign_AdditiveHelix_example_twisting_pad.png )





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveHelix/de
