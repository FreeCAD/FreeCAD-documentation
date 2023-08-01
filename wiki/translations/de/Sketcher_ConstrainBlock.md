---
- GuiCommand:
   Name:Sketcher ConstrainBlock
   Name/de:Sketcher Fixieren
   MenuLocation:Sketch → Skizzen-Beschränkungen → Fixieren
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**K** **B**
   Version:0.17
   SeeAlso:[Sketcher Sperren](Sketcher_ConstrainLock/de.md)
---

# Sketcher ConstrainBlock/de

## Beschreibung

Die Randbedingung **Fixieren** setzt ein geometrisches Element an Ort und Stelle mit einer einzigen Bedingung fest.

Es ist hauptsächlich für die Verwendung mit **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-Splines](Sketcher_CreateBSpline/de.md)** vorgesehen, die sonst nur schwer vollständig bestimmt werden können.

## Anwendung

1.  Ein Element auswählen, das fixiert werden soll.
2.  Die Schaltfläche **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> [Fixieren](Sketcher_ConstrainBlock/de.md)** drücken.

Oder drücke zuerst die Taste , und wähle dann die Elemente aus.

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

Die [Skizzierer Skripten](Sketcher_scripting/de.md)-Seite erklärt die Werte, die für `Edge` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/de
