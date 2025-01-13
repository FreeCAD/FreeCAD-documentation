# Draft Constrain/de
## Beschreibung

Neben der Eingabe von Koordinaten oder der Verwendung von [Einrasten](Draft_Snap/de.md) gibt es eine Funktion namens Einschränken, um zu helfen in den Arbeitsbereichen <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) und <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/de.md) genau zu zeichnen. Für jeden nachfolgenden Punkt kann die Bewegung des Mauszeigers auf die X-, Y- oder Z-Richtung des Koordinatensystems der [Arbeitsebene](Draft_SelectPlane/de.md) eingeschränkt werden. Dies kann zum Beispiel verwendet werden, um eine perfekt vertikale Linie zu erzeugen.

Das Einschränken steht den meisten Befehlen der Arbeitsbereiche [Draft](Draft_Workbench/de.md) und [BIM](BIM_Workbench/de.md) zur Verfügung.

![](images/Draft_Constrain_taskpanel_example.png ) 
*Während der Mauszeiger eingeschränkt ist, sperrt der Aufgaben-Bereich die Werte, die nicht geändert werden*



## Anwendung horizontaler und vertikaler Einschränkungen 

1.  Einen [Draft-](Draft_Workbench/de.md) oder [BIM](BIM_Workbench/de.md)-Befehl auswählen, um Geometrie zu erstellen.

2.  Einen ersten Punkt auswählen. Ein vorausgewählter Punkt ist erforderlich.

3.  Eine der folgenden Möglichkeiten auswählen:
    -   Für eine Horizontal-Einschränkung: Den Mauszeiger vom vorherigen Punkt aus nach links oder rechts bewegen.
    -   Für eine vertikale Beschränkung: Den Mauszeiger vom vorherigen Punkt aus nach oben oder unten bewegen.

4.  
    **Shift**(Umschalttaste) gedrückt halten.

5.  Der Mauszeiger ist jetzt entsprechend eingeschränkt.

6.  Den nächsten Punkt auswählen.

7.  Ist der Befehl noch aktiv: Wahlweise **Shift** loslassen, um die Einschränkung zu deaktivieren.

8.  
    **Shift**stets loslassen, wenn der Befehl beendet ist.



## Anwendung der X-, Y- und Z-Einschränkungen 

1.  Einen [Draft-](Draft_Workbench/de.md) oder [BIM](BIM_Workbench/de.md)-Befehl auswählen, um Geometrien zu erstellen.

2.  Einen ersten Punkt auswählen. Ein vorausgewählter Punkt ist erforderlich.

3.  
    **X**, **Y** oder **Z** drücken, um die Richtung festzulegen.

4.  Der Mauszeiger ist jetzt entsprechend eingeschränkt.

5.  Den nächsten Punkt auswählen.

6.  Ist der Befehl noch aktiv: Wahlweise eine der folgenden Möglichkeiten auswählen:
    -   Dieselbe Taste nochmals drücken, um die Einschränkung zu deaktivieren.
    -   Eine der beiden anderen Tasten drücken, um eine andere Richtung festzulegen.

7.  X-, Y- und Z-Einschränkungen werden automatisch deaktiviert, wenn der Befehl beendet ist.



## Hinweise

-   Einschränken kann mit [Einrasten](Draft_Snap/de.md) kombiniert werden.
-   Die Befehle [Draft Versetzen](Draft_Offset/de.md) und [Draft Trimex](Draft_Trimex/de.md) verwenden eine andere Art der Einschränkung, nämlich das Begrenzen des Vorgangs auf ein bestimmtes Segment.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Der voreingestellte **Randbedingungs-Modifikator**, **Shift**, kann geändert werden: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten →  Randbedingungs-Modifikator**.
-   Die Tastaturkürzel **X**, **Y** und **Z** können geändert werden: **Bearbeiten → Einstellungen... → Draft → Schnittstelle → Befehlsinterne Tastaturkürzel**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Constrain/de
