---
- GuiCommand:/de
   Name:Sketcher SelectElementsWithDoFs
   Name/de:Skizzierer WähleElementeMitFreiheitsgraden
   MenuLocation:Skizze → Skizzierwerkzeuge → Wähle 
Löser Freiheitsgrade
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Version:0.18
---

# Sketcher SelectElementsWithDoFs/de

## Beschreibung

Dieses Werkzeug soll dabei helfen, eine Skizze vollständig zu beschränken, indem es die Skizzenelemente mit den verbleibenden Freiheitsgraden (engl.: Degrees of Freedom)(DoF) in grün hervorhebt.

## Anwendung

Im Meldungsfeld des Lösers, das sich oben im [Aufgabenreiter](Task_panel/de.md) befindet, sollte(n) die folgende(n) Meldung(en) angezeigt werden:

-   Im Falle einer **unter-beschränkten** Skizze:

> Unter-beschränkte Skizze mit X Freiheitsgraden

wobei \"X\" für die Anzahl der in der Skizze verbleibenden Freiheitsgrade steht; weitere Informationen erhälst Du, wenn Du auf den blauen Link klickst oder das Menü benutzt.

1.  Die Elemente, die Freiheitsgrade haben, sind jetzt grün hervorgehoben.
2.  Klicke irgendwo in die Skizze, um die Hervorhebungsfarbe zu löschen.

-   Im Falle einer **voll-beschränkten** Skizze:

> Vollständig beschränkte Skizze 





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/de
