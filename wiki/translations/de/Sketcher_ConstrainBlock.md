---
- GuiCommand:/de
   Name:Sketcher ConstrainBlock
   Name/de:Skizzierer BeschränkeBlock
   MenuLocation:Skizze → Skizzierer Beschränkungen → Beschränke Block
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Version:0.17
   SeeAlso:[[Sketcher_ConstrainLock/de|Skizzierer
Beschränkung Schloss]]
---

# Sketcher ConstrainBlock/de


</div>

## Beschreibung

**Beschränke Block** blockiert ein geometrisches Element an Ort und Stelle mit einer einzigen Beschränkung.


<div class="mw-translate-fuzzy">

Es ist hauptsächlich für die Verwendung mit **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-Splines](Sketcher_CreateBSpline/de.md)** vorgesehen, die sonst nur schwer vollständig beschränkt werden können.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle ein Element aus, das beschränkt werden soll.
2.  Drücke die **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> [Beschränke Block](Sketcher_ConstrainBlock/de.md)** Taste.


</div>

Oder drücke zuerst die Taste , und wähle dann die Elemente aus.

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

Die [Skizzierer Skripten](Sketcher_scripting/de.md)-Seite erklärt die Werte, die für `Edge` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/de
