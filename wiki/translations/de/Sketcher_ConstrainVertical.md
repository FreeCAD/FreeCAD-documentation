---
- GuiCommand:/de
   Name:Sketcher ConstrainVertical
   Name/de:Skizzierer BeschränkeVertikal
   MenuLocation:Skizze → Skizzierer Beschränkungen → Vertikal Beschränken
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:**V**
   SeeAlso:[Skizzierer Horizontale Beschränkung](Sketcher_ConstrainHorizontal/de.md)
---

# Sketcher ConstrainVertical/de

## Beschreibung

Erstellt eine vertikale Beschränkung für die gewählten Linien oder Polylinienelemente. Ab {<small>(v0.17)</small> } kann sie auch Knoten vertikal beschränken. Es kann mehr als ein Objekt ausgewählt werden.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle die Linien oder Knoten, die vertikal beschränkt werden sollen
2.  Um den Befehl für die vertikale Beschränkung aufzurufen:
    -   Drücke das**[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Constrain vertical](Sketcher_ConstrainVertical.md)**
    -   Verwende das Tastaturkürzel **V**
    -   Verwende den {{MenuCommand/de|Skizze → Skizzierer Beschränkungen → Vertikal beschränken}} Eintrag im Skizze Auswahlmenü.
3.  Alternativ kann das Werkzeug ohne vorherige Auswahl gestartet werden, und es erwartet eine Auswahl; aber nur Linien sind auswählbar.
4.  Rechtsklicke oder drücke **Esc** einmal, um das Werkzeug zu beenden.


</div>

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

Die [Skizzierer Skripten](Sketcher_scripting.md) Seite erklärt die Werte, die für `Linie` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python Skripten erstellt.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/de
