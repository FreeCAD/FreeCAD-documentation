---
- GuiCommand   */de
   Name   *Sketcher ConstrainInternalAlignment
   Name/de   *Sketcher InterneAusrichtungFestlegen
   MenuLocation   *Sketch → Skizzen-Beschränkungen → Interne Ausrichtung festlegen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   *
   Version   *0.15
   SeeAlso   *[Sketcher Show/Hide Internal Geometry](Sketcher_RestoreInternalAlignmentGeometry/de.md), [Sketcher EllipseDurch MittelpunktErstellen](Sketcher_CreateEllipseByCenter/de.md)
---

# Sketcher ConstrainInternalAlignment/de

## Beschreibung

Die Beschränkung InnereAusrichtung richtet Linien und Punkte an bestimmten Stellen eines komplexen Sketcher Elements aus (es gibt bisher nur ein \"komplexes\" Element, die [Ellipse](Sketcher_CreateEllipseByCenter/de.md)).

Für **[<img src=images/Sketcher_CreateEllipseByCenter.svg style="width   *16px">[Ellipse](Sketcher_CreateEllipseByCenter/de.md)** und seinen **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width   *16px"> [Ellipsenbogen](Sketcher_CreateArcOfEllipse/de.md)** unterstützt es beschränkte Linien die zu Haupt- und Nebendurchmessern und beschränkten **[<img src=images/Sketcher_CreatePoint.svg style="width   *16px"> /de[Punkte](Sketcher_CreatePoint.md)** zu Positionen der Ellipsenfoci werden.

Diese Beschränkung ist für erfahrene Benutzer gedacht, da ihre Verwendung nicht so einfach ist wie bei den anderen Beschränkungen. Es gibt ein Hilfswerkzeug namens **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width   *16px"> [Interne Geometrie anzeigen/ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md)**, um zu vermeiden, dass die Beschränkung InnereAusrichtung manuell aufgerufen werden muss.

## Einsatz auf Ellipse 


<div class="mw-translate-fuzzy">

1.  Wähle die auszurichtenden Elemente und eine Ellipse aus. Die Ellipse muss zuletzt ausgewählt werden. Akzeptiert werden bis zu zwei Linien und bis zu zwei Punkte.
2.  Das Aufrufen der Beschränkung kann auf verschiedene Weise erfolgen   *
    -   Drücken der **[<img src=images/Sketcher_ConstrainInternalAlignment.svg style="width   *16px"> [Beschränke innere Ausrichtung](Sketcher_ConstrainInternalAlignment/de.md)** Schaltfläche in der Werkzeugleiste.
    -   Verwendung der **Strg** + **A** Tastaturkürzel.
    -   Verwendung des **Skizze → Skizziererbeschränkungen → Beschränke [<img src=images/Sketcher_ConstrainInternalAlignment.svg style="width   *16px"> Beschränke InnereAusrichtung** Eintrags aus dem oberen Menü.


</div>

Die erste ausgewählte Linie wird so ausgerichtet, dass sie zum Hauptdurchmesser der Ellipse wird (aber wenn sie nicht bereits durch eine andere Linie belegt ist, wird sie sonst zum Nebendurchmesser). Die zweite Linie wird so ausgerichtet, dass sie zu einem Nebenradius wird. Die Linien werden automatisch auf [Konstruktion](Sketcher_ToggleConstruction/de.md) umgeschaltet.

Ebenso ist der erste Punkt beschränkt, um der erste unbesetzte Fokus zu werden, und der zweite Punkt geht zum anderen Fokus.

**Hinweis   *** Standardmäßig haben neue Ellipsen eine interne Konstruktionsgeometrie.Wenn diese die Ellipse bereits vollständig definiert, kannst du die Beschränkung InnereAusrichtung nicht direkt verwenden. Wenn diese die Ellipse bereits vollständig definiert, kannst du die Beschränkung InnereAusrichtung nicht direkt verwenden. Du musst zuerst die Konstruktionsgeometrie oder Teile davon löschen. Falls du die Konstruktionsgeometrie nicht siehst, wähle die Ellipse und verwende das Werkzeug **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width   *16px"> [Interne Geometrie ein-/ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md)**, um sie sichtbar zu machen.

## Skripten


```python
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment   *EllipseMajorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment   *EllipseMinorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment   *EllipseFocus1', index_of_point, 1, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment   *EllipseFocus2', index_of_point, 1, index_of_ellipse))
```

Anmerkungen   *

   *   
    {{Incode|Skizze}}ist ein Skizzenobjekt.

   *   Zahl {{Incode|1}} in den Schwerpunktsetzungen steht für den Startpunkt eines Punktelements (er wird ignoriert).

   *   Das {{Incode|index_of_point}}-Argument muss ein Punkt sein, es kann nicht genutzt werden, um z.B. auf einen Endpunkt einer Kante zu weisen.

Die [Skizzierer Skripten](Sketcher_scripting/de.md)-Seite erklärt die Werte, die für `inde_of_line`, `inde_of_point` und `index_of_ellipse` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainInternalAlignment/de
