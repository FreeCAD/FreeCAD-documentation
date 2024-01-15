---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/de: Sketcher Sperren
   MenuLocation: Skizze , Sketcher-Randbedingungen , Sperren
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **L**
   SeeAlso: Sketcher_ConstrainBlock/de
---

# Sketcher ConstrainLock/de



## Beschreibung

Die Randbedingung **Sperren** wendet die Randbedingungen **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md)** und **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md)** auf ausgewählte Knoten (Punkte) in der Skizze an. Wenn ein einzelner Knoten ausgewählt ist, beziehen sich die horizontalen und vertikalen Abstandsbedingungen auf den Ursprungspunkt der Skizze. Wenn zwei oder mehr Punkte ausgewählt sind, werden die horizontalen und vertikalen Abstandsbedingungen für jedes Punktpaar hinzugefügt. Es gibt keine automatische Aufforderung, die Werte der Randbedingungen zu bearbeiten, sie müssen manuell bearbeitet werden.



## Anwendung

1.  Einen oder mehrere Knoten (Punkte) in der Skizze auswählen.
2.  Die Schaltfläche **[<img src=images/Sketcher_ConstrainLock.svg style="width:16px"> [Sperren](Sketcher_ConstrainLock/de.md)** drücken.
3.  Um die Werte der Randbedingungen zu bearbeiten, doppelklickt man auf einen Wert in der 3D-Ansicht, doppelklickt auf die Randbedingung oder rechtsklickt und wählt **Wert bearbeiten** in der Liste der Randbedingungen im Aufgabenbereich.

**Anmerkung:** Dieses Werkzeug kann auch ohne vorherige Auswahl gestartet werden, aber es funktioniert dann nur mit einem einzigen Knoten und referenziert die Randbedingungen auf den Skizzenursprung. Voreingestellt arbeitet der Befehl im \"Fortsetzen-Mudus\", um neue Randbedingungen zu erstellen; die rechte Maustaste oder **ESC** einmal drücken, um den Befehl zu beenden.



## Skripten

Die Randbedingung <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sperren](Sketcher_ConstrainLock/de.md) ist ein GUI-Befehl, der die Randbedingungen <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md) und <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Sketcher YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md) erstellt, sie ist keine eigenständige Randbedingung. Siehe die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) für Details und Beispiele, wie diese Randbedingungen mit Python-Skripten erstellt werden können.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/de
