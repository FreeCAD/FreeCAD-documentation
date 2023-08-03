---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/de: Sketcher Sperren
   MenuLocation: Sketch , Skizzen-Beschränkungen , Sperren
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

**Anmerkung:** Das Beschränkungswerkzeug kann auch ohne vorherige Selektion gestartet werden, aber es wird dann nur mit einem einzigen Eckpunkt funktionieren und die Beschränkungen auf den Skizzenursprung referenzieren. Als Voreinstellung arbeitet der Befehl im \"Continue mode\", um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **ESC** einmal zur Beendigung des Befehls.

## Skripten

Die <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Schloss](Sketcher_ConstrainLock/de.md) Beschränkung ist ein GUI Befehl, der eine <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontaler Abstands](Sketcher_ConstrainDistanceX/de.md) und eine <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertikaler Abstands](Sketcher_ConstrainDistanceY/de.md) Beschränkung erzeugt, sie ist keine eigenständige Beschränkung. Siehe die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite für Details und Beispiele, wie diese Beschränkungen aus Python Skripten erstellt werden können.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/de
