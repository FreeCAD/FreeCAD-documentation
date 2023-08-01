---
- GuiCommand:/de
   Name:Sketcher SelectElementsWithDoFs
   Name/de:Sketcher UnterbestimmteElementeAuswählen
   MenuLocation:Skizze → Skizzenwerkzeuge → Unterbestimmte Elemente auswählen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**Z** **F**
   Version:0.18
---

# Sketcher SelectElementsWithDoFs/de



## Beschreibung

Dieses Werkzeug soll dabei helfen, eine Skizze vollständig zu bestimmen, indem es die unterbestimmten Skizzenelemente in grün hervorhebt, d.h. die mit verbliebenen Freiheitsgraden (engl.: Degrees of Freedom, DoF).



## Anwendung

Im Meldungsfeld des Lösers, das sich oben im [Aufgabebereich](Task_panel/de.md) befindet, sollte eine der folgenden Meldungen angezeigt werden:

-   Im Falle einer **unterbestimmten** Skizze:

> Unterbestimmt: X DoF

:   wobei \"X\" für die Anzahl der in der Skizze verbliebenen Freiheitsgrade steht; weitere Informationen erhält man, wenn man auf den blauen Link klickt oder das Menü benutzt.

1.  Die unterbestimmten Elemente werden jetzt grün hervorgehoben.
2.  Irgendwo in die Skizzen klicken, um die Hervorhebungsfarbe zu löschen.

-   Im Falle einer **vollständig bestimmten** Skizze:

> Vollständig bestimmte Skizze 





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/de
