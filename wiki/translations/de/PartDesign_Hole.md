---
- GuiCommand:/de
   Name:PartDesign Hole
   Name/de:PartDesign Bohrung
   MenuLocation:Part Design → Subtraktives Formelement erstellen → Bohrung
   Workbenches:[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign Tasche](PartDesign_Pocket/de.md)
---

# PartDesign Hole/de

## Beschreibung


<div class="mw-translate-fuzzy">

Die Funktion **Bohrung** erzeugt eine oder mehrere Bohrungen aus den Kreisen einer ausgewählten Skizze. Viele Parameter können eingestellt werden, wie z. B. Gewinde und Größe, Passung, Bohrungstyp (Kegelsenkung, Plansenkung, gerade) und mehr.


</div>

<img alt="" src=images/Countersunk_and_counterbored_holes_cross-section1.png  style="width:600px;">



*Kegelgesenkte (links) und plangesenkte (zur Rechten) Bohrungen im Längsschnitt.*

## Anwendung

1.  Drücke die **<img src="images/PartDesign_Hole.svg" width=16px> '''Bohrung'''
**

Schaltfläche.

1.  Wird eine vorhandene unbenutzte Skizze gefunden, wird diese automatisch verwendet. Wenn mehr als eine Skizze gefunden wird, erscheint ein Fenster \"Formelement auswählen\", um eine Auswahl zu treffen. Alternativ kann eine Skizze ausgewählt werden, bevor der Befehl Bohrung ausgeführt wird.
2.  Definiere die Bohrungsparameter, die im Abschnitt [Optionen](#Options/de.md) beschrieben sind.
3.  Drücke **OK**.

## Optionen

Abhängig von der Auswahl werden einige Felder aktiviert oder bleiben deaktiviert.

![](images/PartDesign_Hole_parameters_de.png )

### Gewinde und Größe 


<div class="mw-translate-fuzzy">

-   **Profil**: Wenn auf *Kein* gesetzt, wird keine Gewindeinfo definiert.

[ISO](https://en.wikipedia.org/wiki/ISO_metric_screw_thread) und [UTS](https://en.wikipedia.org/wiki/Unified_Thread_Standard) Gewindeprofile aktivieren die *Größe*n Felder.

-   **Mit Gewinde versehen**: wenn angehakt werden Gewindedaten zur Lochfunktion hinzufügt und verwendet den kleineren Lochdurchmesser. Wenn nicht angehakt, gilt die Bohrung als gewindefrei und der Hauptnenndurchmesser mit definiertem *Freigang* wird gewählt.
-   **Richtung**: setzt die Gewinderichtung (rechtshändig oder linkshändig), wenn *Mit Gewinde versehen* aktiviert ist.
-   **Größe**: Legt die Gewindegröße fest. Erfordert, dass *Profil* auf eines der ISO oder UTS Profile eingestellt ist.
-   **Freigang**: setzt entweder Standard-, Nah- oder Großraumlochdurchmesser. Für ISO Gewinde entsprechen die Durchmesser der Norm ISO 273, für UTS werden sie nach einer Faustregel berechnet, da es keine Norm gibt, die sie definiert. Nur für Bohrungen ohne Gewinde verfügbar.
-   **Klasse**: definiert die Toleranzklasse.
-   **Durchmesser**: Definiert den Bohrungsdurchmesser, wenn *Profil* auf *Nichts* gesetzt wurde.
-   **Tiefe**: Tiefe der Bohrung von der Skizzierebene. *Abmessung* aktiviert ein Feld um einen Wert einzugeben. *Durch alles* wird die Bohrung durch den ganzen Körper schneiden.**Hinweis:** Aus technischen Gründen ist *Durch Alles* eigentlich ein 10 Meter tiefes Loch. Wenn du tiefere Löcher benötigst, verwende *Abmessung*.


</div>

### Lochschnitt

-   **Typ**: Setzt den Typ des Lochschnitts: *Kein* bedeutet kein Schnitt; andere Typen sind

unterschiedliche Schraubennormen (<small>(v0.19)</small> ) und die beiden generischen Typen *Zylindersenkung* und \'\'Kegelsenkung.

-   **Durchmesser**: Setzt den oberen Durchmesser (an der Skizzenebene) für den Lochschnitt.
-   **Tiefe**: Tiefe des Lochschnitts von der Skizzierebene gemessen.
-   **Kegelsenkung Winkel**: Winkel des konischen Lochschnitts. Nur anwendbar für Kegelsenkungen.

### Bohrspitze

-   **Typ**: definiert den Auslauf der Bohrung, wenn *Tiefe* auf *Abmessung* gesetzt ist.
    -   **Flach** erzeugt einen flachen Boden
    -   **Gewinkelt** erzeugt eine konische Spitze. Seine Option **Für Tiefe berücksichtigen** (<small>(v0.19)</small> ) subtrahiert die konische Höhe von der *Dimension*. Wenn also z.B. *Maß* 7,00 ist und die Option nicht verwendet wird, ist der zylindrische Teil der Bohrung 7,00 und die für den konischen Teil notwendige Tiefe wird zur Bohrungstiefe addiert. Wenn die Option verwendet wird, beträgt die gesamte Bohrungstiefe einschließlich der konischen Spitze 7,00.

### Sonstiges

-   **Kegelförmig**: setzt einen Kegelwinkel zur Bohrung. Der Wert wird aus der Normalen der Skizzenebene berechnet. 90 Grad setzt ein gerades Loch. Ein Wert unter 90 erzeugt einen kleineren Lochradius am Boden, ein Wert über 90 vergrößert den Lochradius am Grund.
-   **Umgekehrt**: kehrt die Bohrungsextrusionsrichtung um. Die Standardrichtung ist die Abbildungsrichtung der Bohrungsskizze zu ihrem Anhang.

## Eigenschaften

Viele der Dateneigenschaften sind die gleichen wie unter [Optionen](#Options.md).

-    **Kennzeichen**: Name, der dem Objekt gegeben wurde, dieser Name kann nach Belieben geändert werden.

-    **Umgekehrt**: wahr oder falsch. Kehrt die Extrusionsrichtung um.

-    {{PropertyData/de|Verfeinern}}: wahr oder falsch. Wenn auf true gesetzt, reinigt den Festkörper von Restkanten, hinterlassen von Funktionen. Siehe **<img src="images/Part_RefineShape.svg" width=16px> [Part FormVerfeinern](Part_RefineShape/de.md)** für weitere Details.

## Begrenzungen


<div class="mw-translate-fuzzy">

Die ausgewählte Skizze muss einen oder mehrere Kreis(e) enthalten. Der Radius des Kreises (der Kreise) innerhalb der Skizze wird nicht berücksichtigt. Die erzeugten Löcher sind identisch, auch wenn die Kreise in der Skizze unterschiedliche Radien haben.

-   Standardmäßig wird die Loch Funktion unterhalb der Skizzierebene extrudiert. Wenn der Festkörper auf der XY\_Ebene liegt und die Lochskizze mit der XY\_Ebene verbunden ist, wird es versuchen, sich vom Festkörper weg zu extrudieren und scheinbar kein Ergebnis zu erzielen. In diesem Fall muss die Option *Umgekehrt* gesetzt werden, alternativ kann die Skizze auf die Unterseite des Festkörpers abgebildet werden.


</div>

## Schnitttyp Definitionen 

Schnittarten (Schraubentypen) werden seit Version 0.19 in [json](https://de.wikipedia.org/wiki/JavaScript_Object_Notation) Dateien definiert. Es gibt einen Satz von Dateien, die mit FreeCAD verteilt werden, aber Benutzer können ihre eigenen Definitionen erstellen. Die Dateien werden in <UserAppDataDir>/PartDesign/Hole gesucht. Das `UserAppDataDir` kann durch Eingabe von `App.getUserAppDataDir()` in der [Python Konsole](Python_console/de.md) gefunden werden.

Die Datei sollte enthalten:

-   **name**: Der Name der Definition. Dieser muss eindeutig sein, da er als Bezeichner in der FreeCAD Benutzeroberfläche und als interner Index verwendet wird.
-   **cut\_type**: Entweder `countersink` oder `counterbore`.
-   **thread\_type**: Entweder `metric` oder `metricfine`.
-   **angle**: Der Winkel einer Kegelsenkung (nicht notwendig bei Flachsenkungen).
-   **data**: Eine Liste von Größen, bestehend aus:
    -   **thread**: Name des Gewindes, das FreeCAD bekannt ist.
    -   **diameter**: Der Durchmesser des Schnitts.
    -   **depth**: Tiefe der Flachsenkung (nicht notwendig bei Kegelsenkungen).

Beispiel: {{Code|lang=json|code=
{
    "name": "DIN 7984",
    "cut_type": "counterbore",
    "thread_type": "metric",
    "data": [
        { "thread": "M2",   "diameter":  4.3, "depth":  1.6 },
        { "thread": "M2.5", "diameter":  5.0, "depth":  2.0 },
        …
    ]
}
}}





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Hole/de
