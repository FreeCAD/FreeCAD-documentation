---
 GuiCommand:
   Name: Sketcher ConstrainVertical
   Name/de: Sketcher VertikalFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Vertikal festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **V**
   SeeAlso: Sketcher_ConstrainHorizontal/de
---

# Sketcher ConstrainVertical/de



## Beschreibung

Erstellt die Randbedingung VertikalFestlegen für die ausgewählten Linien- oder Linienzugelemente. Ab {{{VersionPlus/de|0.17}}} kann sie auch Knoten vertikal festlegen. Es kann mehr als ein Objekt ausgewählt werden.



## Anwendung

1.  Die Linien oder Knoten auswählen, die vertikal festgelegt werden sollen.
2.  Um den Befehl VertikalFestlegen aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Vertikal festlegen](Sketcher_ConstrainVertical/de.md)** drücken.
    -   Das Tastaturkürzel **V** verwenden.
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → [<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> Vertikal festlegen** im Sketch-Menü anklicken.
3.  Alternativ kann das Werkzeug ohne vorherige Auswahl gestartet werden, dann erwartet es eine Auswahl.
4.  Ein Rechtsklick oder einmal **Esc** drücken, um das Werkzeug zu verlassen.



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Line` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/de
