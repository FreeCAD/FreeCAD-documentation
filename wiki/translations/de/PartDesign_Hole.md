---
- GuiCommand:/de
   Name:PartDesign Hole
   Name/de:PartDesign Bohrung
   MenuLocation:Part Design → Objekte abziehen → Bohrung
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign Tasche](PartDesign_Pocket/de.md)
---

# PartDesign Hole/de



## Beschreibung

Die Funktion **Bohrung** erstellt eine oder mehrere Bohrungen in den Mittelpunkten der Kreise und Bögen einer ausgewählten Skizze. Wenn Bögen vorhanden sind, müssen sie Bestandteil einer geschlossenen Kontur sein. Alle Bestandteile, die nicht Kreise oder Bögen sind, werden zwar ignoriert, müssen aber trotzdem zu einer geschlossenen Kontur gehören. Viele Parameter können eingestellt werden, wie z. B. Gewinde und Größe, Passung, Bohrungstyp (Kegelsenkung, Plansenkung, Durchgangsloch) und mehr.

Die Mittelpunkte der Kreise und Bögen werden verwendet, um die Bohrungen zu positionieren, es ist aber zu beachten, dass ihre Radien nicht berücksichtigt werden. Die erstellten Bohrungen werden identisch sein, auch wenn sich die Radien unterscheiden.

<img alt="" src=images/Countersunk_and_counterbored_holes_cross-section1.png  style="width:600px;">



*Bohrung mit Kegelgesenkung (links) und mit Flach-/Zylindersenkung (rechts) im Längsschnitt.*



## Anwendung

1.  Drücke die Schaltfläche **<img src="images/PartDesign_Hole.svg" width=16px> '''Bohrung'''**.
2.  Wird eine vorhandene unbenutzte Skizze gefunden, wird diese automatisch verwendet. Wenn mehr als eine Skizze gefunden wird, erscheint ein Fenster \"Formelement auswählen\", um eine Auswahl zu treffen. Alternativ kann eine Skizze ausgewählt werden, bevor der Befehl Bohrung ausgeführt wird.
3.  Definiere die Bohrungsparameter, die im Abschnitt [Optionen](#Options/de.md) beschrieben sind.
4.  Drücke **OK**.



## Optionen

Abhängig von der Auswahl werden einige Felder aktiviert oder bleiben deaktiviert.

<img alt="" src=images/PartDesign_Hole_parameters_de.png  style="width:600px;">



### Gewindeart und -Größe 

-   **Profil**: Wenn auf *Ohne* gesetzt, wird keine Gewindeinfo definiert. Einträge für [ISO-](https://en.wikipedia.org/wiki/ISO_metric_screw_thread) und [UTS-](https://en.wikipedia.org/wiki/Unified_Thread_Standard)Gewindeprofile aktivieren die Felder zur Einstellung der *Größe*.
-   **Mit Gewinde versehen**: Wenn aktiviert, werden der Bohrungsfunktion Gewindedaten hinzufügt und der Kerndurchmesser des Gewindes verwendet. Wenn nicht aktiviert, gilt die Bohrung als gewindefrei und der Nenndurchmesser mit definiertem *Spiel* wird ausgewählt.
-   **Gewinde darstellen**: Wenn aktiviert, wird ein richtiges Gewinde geformt. Dies verbraucht viel Rechenleistung und wird für Modelle normalerweise nicht verwendet, außer für Anschauungszwecke oder manchmal für 3D-Drucke. Wenn es verwendet wird, wird empfohlen, diese Funktion als eine der letzten zu aktivieren, weil sie die Rechenzeit für Neuberechnungen signifikant erhöht. ({{Version/de|0.20}})
-   **Richtung**: Legt die Gewinderichtung fest (Rechtsgewinde oder Linksgewinde), wenn *Mit Gewinde versehen* aktiviert ist.
-   **Größe**: Legt die Gewindegröße fest. Erfordert, dass *Profil* auf eines der [ISO-](https://en.wikipedia.org/wiki/ISO_metric_screw_thread) oder [UTS-](https://en.wikipedia.org/wiki/Unified_Thread_Standard)Gewindeprofile eingestellt ist.
-   **Spiel**: Stellt entweder Standard, Eng oder Weit für das Spiel von Durchgangsbohrungen ein. Für ISO-Gewinde entsprechen die Durchmesser der Norm ISO 273, für UTS werden sie nach einer Faustregel berechnet, da es keine Norm gibt, die sie festlegt. Nur für Bohrungen ohne Gewinde (Durchgangsbohrung) verfügbar.
-   **Klasse**: Legt die Toleranzklasse fest.
-   **Durchmesser**: Definiert den Bohrungsdurchmesser, wenn *Profil* auf *Ohne* gesetzt wurde.
-   **Tiefe**: Tiefe der Bohrung ab der Skizzenebene. *Abmessung* aktiviert ein Feld um einen Wert einzugeben. *Durch alles* lässt die Bohrung durch den ganzen Körper verlaufen. **Hinweis:** Aus technischen Gründen ist *Durch Alles* eigentlich ein 10 m tiefes Loch. Weden tiefere Löcher benötigt, muss *Abmessung* verwendet werden.



### Bohrloch

-   **Typ**: Legt die Art der Senkung fest: *Nichts* bedeutet ohne Senkung (Durchgangsloch); andere Optionen sind verschiedene Schraubennormen und die generischen Typen *Flachsenkung*, *Kegelsenkung* und ({{Version/de|0.21}}) *Bohrsenkung*.
-   **Durchmesser**: Legt den oberen Durchmesser (an der Skizzenebene) für die Senkung fest.
-   **Tiefe**: Die Festlegung der Tiefe ist abhängig von der Art (Type) der Senkung:
    -   Für eine *Flachsenkung* ist es die Tiefe der Senkung, von der Skizzenebene aus gemessen.
    -   Für eine *Kegelsenkung* ist es die Höhe eines Schraubenkopfes unterhalb der Skizzenebene.
    -   Für eine *Bohrsenkung* ist es die Tiefe des zylindrischen Anteils der Senkung.
-   **Winkel der Kegelsenkung**: Kegelwinkel der Senkung. Nur anwendbar für Kegelsenkungen.



### Bohrungsgrund

-   **Typ**: definiert den Grund der Bohrung, wenn *Tiefe* auf *Abmessung* gesetzt ist.
    -   **Flach** erstellt einen flachen Bohrungsgrund
    -   **Konisch** erzeugt eine konische Vertiefung. Seine Option **Für die Tiefe berücksichtigen** zieht die Kegelhöhe von der *Abmessung* ab. Wenn also z.B. *Abmessung* 7,00 ist und die Option nicht verwendet wird, ist der zylindrische Teil der Bohrung 7,00 und die Höhe der konischen Vertiefung kommt noch hinzu. Wenn die Option verwendet wird, beträgt die gesamte Bohrungstiefe einschließlich der konischen Spitze 7,00.



### Sonstiges

-   **Kegelförmig**: Fügt einen Schrägungdwinkel zur Bohrung hinzu. Der Wert wird von der Normalen der Skizzenebene ausgehend berechnet. 90° ergibt ein zylindrisches Loch. Ein Wert unter 90° ergibt einen kleineren Lochradius am Bohrungsgrund, ein Wert über 90° vergrößert den Lochradius am Grund.
-   **Umgekehrt**: Kehrt die Bohrungsrichtung um. Die Standardrichtung ist die Abbildungsrichtung der Bohrungsskizze zu ihrem Anhang.



## Eigenschaften

Viele der Dateneigenschaften sind die gleichen wie unter [Optionen](#Optionen.md).

-    **Label**: Bezeichnung die dem Objekt gegeben wurde, diese kann nach Belieben geändert werden.

-    **Refine**: Wahr oder falsch. Wenn auf true gesetzt, wird der Volumenkörper von Restkanten befreit, die von Formelementen hinterlassen wurden. Siehe **<img src="images/Part_RefineShape.svg" width=16px> [Part FormAufbereiten](Part_RefineShape/de.md)** für weitere Details.



## Einschränkungen

-   Standardmäßig wird die Funktion Bohrung unterhalb der Skizzenebene extrudieren. Wenn der Volumenkörper auf der XY-Ebene liegt und die Lochskizze mit der XY-Ebene verbunden ist, wird sie versuchen, vom Volumenkörper weg zu extrudieren und scheinbar kein Ergebnis erzielen. In diesem Fall muss die Option *Umgekehrt* gesetzt werden, alternativ kann die Skizze auf die Unterseite des Volumenkörpers gelegt werden.
-   Gewinde darstellen funktioniert nur, wenn Umgekehrt nicht aktiviert ist.



## Schnitttyp Definitionen 

Schnittarten (Schraubentypen) werden in [json](https://de.wikipedia.org/wiki/JavaScript_Object_Notation)-Dateien definiert. Es gibt einen Satz von Dateien, die mit FreeCAD ausgeliefert werden, aber Benutzer können ihre eigenen Definitionen erstellen. Die Dateien werden in <UserAppDataDir>/PartDesign/Hole gesucht. Das `UserAppDataDir` kann durch Eingabe von `App.getUserAppDataDir()` in der [Python-Konsole](Python_console/de.md) gefunden werden.

Die Datei sollte enthalten:

-   **name**: Der Name der Definition. Dieser muss eindeutig sein, da er als Bezeichner in der FreeCAD Benutzeroberfläche und als interner Index verwendet wird.
-   **cut_type**: Entweder `countersink` oder `counterbore`.
-   **thread_type**: Entweder `metric` oder `metricfine`.
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
