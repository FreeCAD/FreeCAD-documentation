---
- GuiCommand:/de
   Name:Sketcher ConstrainLock
   Name/de:Skizzierer BeschränkeSchloss
   MenuLocation:Skizze → Skizzierer Beschränkungen → Beschränke Schloss
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   SeeAlso:[Beschränke Block](Sketcher_ConstrainBlock/de.md)
---

# Sketcher ConstrainLock/de

## Beschreibung

**Beschränkung Schloss** wendet **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> <img src=images/Sketcher_ConstrainDistanceY.svg style="width:Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md)** und **[16px"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md)** Beschränkungen auf ausgewählte Knoten (Punkte) in der Skizze an. Wenn ein einzelner Knoten ausgewählt ist, beziehen sich die horizontalen und vertikalen Abstandsbeschränkungen auf den Skizzenursprungspunkt. Wenn zwei oder mehr Punkte ausgewählt sind, werden die horizontalen und vertikalen Abstandsbeschränkungen für jedes Punktpaar hinzugefügt. Es gibt keine automatische Aufforderung, die Werte der Beschränkungen zu bearbeiten, sie müssen manuell bearbeitet werden.

## Anwendung

1.  Wähle ein oder mehrere Knoten (Punkte) in der Skizze.
2.  Drücke die **<img src=images/Sketcher_ConstrainLock.svg style="width:16px"> [Beschränkung Schloss](Sketcher_ConstrainLock/de.md)** Taste.
3.  Um die Beschränkungswerte zu bearbeiten, doppelklicke auf einen Beschränkungswert in der 3D Ansicht oder doppelklicke auf die Beschränkung oder rechtsklicke und wähle **Wert bearbeiten** in der Beschränkungsliste im Aufgabenreiter.

**Anmerkung:** Das Beschränkungswerkzeug kann auch ohne vorherige Selektion gestartet werden, aber es wird dann nur mit einem einzigen Eckpunkt funktionieren und die Beschränkungen auf den Skizzenursprung referenzieren. Als Voreinstellung arbeitet der Befehl im \"Continue mode\", um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **ESC** einmal zur Beendigung des Befehls.

## Skripten

Die <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Schloss](Sketcher_ConstrainLock/de.md) Beschränkung ist ein GUI Befehl, der eine <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontaler Abstands](Sketcher_ConstrainDistanceX/de.md) und eine <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertikaler Abstands](Sketcher_ConstrainDistanceY/de.md) Beschränkung erzeugt, sie ist keine eigenständige Beschränkung. Siehe die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite für Details und Beispiele, wie diese Beschränkungen aus Python Skripten erstellt werden können.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/de
