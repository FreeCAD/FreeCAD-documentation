# Draft Constrain/de
{{TOCright}}

## Beschreibung

Neben der Eingabe von Koordinaten oder der Verwendung vom _ und dem <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Architektur Arbeitsbereich](Arch_Workbench/de.md) sorgfältig zu Zeichnen. Für jeden nachfolgenden Punkt kannst du die Bewegung des Mauszeigers auf die X, Y oder Z Richtung des Koordinatensystems der [Arbeitsebene](Draft_SelectPlane/de.md) beschränken. Dies kann zum Beispiel verwendet werden, um eine perfekt vertikale Linie zu erzeugen.

Das Beschränken ist mit den meisten [Entwurf](Draft_Workbench/de.md)- und [Architektur](Arch_Workbench/de.md)-Befehlen verfügbar.

![](images/Draft_Constrain_taskpanel_example.png ) 
*Während der Mauszeiger beschränkt ist, sperrt das Aufgabenfeld die Werte, die nicht geändert werden*

## Anwendung horizontaler und vertikaler Beschränkungen 

1.  Wähle einen [Entwurf](Draft_Workbench/de.md) oder [Architektur](Arch_Workbench/de.md) Befehl, um deine Geometrie zu erstellen.
2.  Nimm einen ersten Punkt. Ein vorheriger Punkt ist erforderlich.
3.  Mache eins von folgendem:
    -   Für eine horizontale Beschränkung: Bewege den Mauszeiger nach links oder rechts zum vorherigen Punkt.
    -   Für eine vertikale Beschränkung: Bewege den Mauszeiger über oder unter den vorherigen Punkt.
4.  Halte **Shift** gedrückt.
5.  Der Mauszeiger ist jetzt beschränkt.
6.  Nimm den nächsten Punkt.
7.  Wenn der Befehl noch aktiv ist: Lasse wahlweise **Shift** los, um die Beschränkung zu deaktivieren.
8.  Lasse **Shift** immer los, wenn der Befehl beendet ist.

## Anwendung X, Y und Z Beschränkungen 

1.  Wähle einen [Entwurf](Draft_Workbench/de.md) oder [Architektur](Arch_Workbench/de.md) Befehl, um deine Geometrie zu erstellen.
2.  Nimm einen ersten Punkt. Ein vorheriger Punkt ist erforderlich.
3.  Drücke **X**, **Y** oder **Z**, um die Richtung anzugeben.
4.  Der Mauszeiger ist nun beschränkt.
5.  Nimm den nächsten Punkt.
6.  Wenn der Befehl noch aktiv ist, mach wahlweise etwas von folgendem:
    -   Drücke die gleiche Taste, um die Beschränkung zu deaktivieren.
    -   Drücke eine der beiden anderen Tasten, um in einer anderen Richtung zu beschränken.
7.  X-, Y- und Z-Beschränkungen werden automatisch deaktiviert, wenn der Befehl beendet ist.

## Hinweise

-   Beschränken kann mit [Fangen](Draft_Snap/de.md) kombiniert werden.
-   Der [Entwurf Versatz](Draft_Offset/de.md) Befehl und [Entwurf Trimex](Draft_Trimex/de.md) Befehl verwenden eine andere Art der Beschränkung, nämlich die Beschränkung des Einsatzes auf ein bestimmtes Segment.

## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Die Standardtaste **Beschränken mod**, **Shift**, kann geändert werden: **Bearbeiten → Einstellungen... → Entwurf → Raster und Fang → Fangen → Beschränken mod**.
-   Die Tastaturkürzel **X**, **Y** und **Z** können geändert werden: **Bearbeiten → Einstellungen... → Entwurf → Benutzeroberflächeneinstellungen → Befehlsinterne Tastaturkürzel**.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Constrain/de
