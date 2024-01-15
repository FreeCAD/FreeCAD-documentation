---
 GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/de: Sketcher Fixieren
   MenuLocation: Skizze , Sketcher-Randbedingungen , Fixieren
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **B**
   Version: 0.17
   SeeAlso: Sketcher_ConstrainLock/de
---

# Sketcher ConstrainBlock/de



## Beschreibung

Die Randbedingung **Fixieren** setzt ein geometrisches Element an Ort und Stelle mit einer einzigen Bedingung fest.

Es ist hauptsächlich für die Verwendung mit **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-Splines](Sketcher_CreateBSpline/de.md)** vorgesehen, die sonst nur schwer vollständig bestimmt werden können.



## Anwendung

1.  Ein Element auswählen, das fixiert werden soll.
2.  Die Schaltfläche **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> [Fixieren](Sketcher_ConstrainBlock/de.md)** drücken.

Oder zuerst die Schaltfläche drücken, und dann die Elemente auswählen.



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Edge` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/de
