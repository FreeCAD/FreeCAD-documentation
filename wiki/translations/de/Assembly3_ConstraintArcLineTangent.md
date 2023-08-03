---
 GuiCommand:
   Name: Assembly3 ConstraintArcLineTangent
   Name/de: Assembly3 Bogen-Linie-Tangente
   Icon: Assembly_ConstraintArcLineTangent.svg
   Workbenches: Assembly3_Workbench
---

# Assembly3 ConstraintArcLineTangent/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg  style="width:16px;"> [BogenLinieTangente](Assembly3_ConstraintArcLineTangent.md) verbindet zwei Objekte eines Zusammenbaus. Die gewählten Elemente der einzelnen Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt im Verhältnis zu einem anderen Objekt zu positionieren.

 Da das Werkzeug nicht funktionieren wollte, gibt es hier nur die Aussage der QuickInfo:

Add an \"Arc line tangent\" constraint to make a line tangent to an arc at the start or end point of the arc.

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Ein Bogenelement des einen Objekts auswählen.
3.  Ein Linienelement des anderen Objekts auswählen.
4.  Schaltfläche **<img src="images/Assembly_ConstraintArcLineTangent.svg" width=16px> [Bogen-Linie-Tangente](Assembly3_ConstraintArcLineTangent/de.md)** drücken.

Abhängig von der Reihenfolge der ausgewählten Linien erscheinen folgende \"Fehlermeldungen\":

Constraint "ArcLineTangent" requires the 1st element to be a circular edge
Constraint "ArcLineTangent" requires the 1st element to be an arc edge



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintArcLineTangent/de
