---
- GuiCommand:/de
   Name:Sketcher ToggleDrivingConstraint
   Name/de:Skizzierer UmschaltenTreibendeBeschränkung
   MenuLocation:Skizze → Skizzierer Beschränkungen → Umschalten Referenz/treibende Beschränkung
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Version:0.16
   SeeAlso:[Umschalten Konstruktion](Sketcher_ToggleConstruction/de.md)
---

# Sketcher ToggleDrivingConstraint/de


</div>

## Beschreibung

Das **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [ Umschalten treibende Beschränkung](Sketcher_ToggleDrivingConstraint/de.md)** Werkzeug wandelt Maßbeschränkungen (Schloss, Horizontaler/Vertikaler Abstand, Länge, Radius und Winkel) in den Referenzmodus und zurück. Die Symbole in der Werkzeugleiste färben sich blau, und anstelle von Maßbeschränkungen werden Referenzbemaßungen erstellt. Referenzbemaßungen beschränken die Skizze nicht. Es kann nützlich sein, in einer Skizze Referenzbemaßungen zu erstellen, um die Bemaßungen zu überprüfen; wenn ein Name angegeben wird, können sie auch dazu verwendet werden, die Beschränkungen in einer anderen Skizze durch [Ausdrücke](Expressions/de.md) zu steuern.

![](images/Sketcher_Constraint_Toolbar_ReferenceMode.png ) 
*Die Skizzier Beschränkungswerkzeugleiste mit den Maßbeschränkungen im Bezugsbemaßungsmodus (blau).*

![](images/Sketcher_ToggleConstraint_example.png ) 
*Eine horizontale Abstandsbeschränkung (50 mm), eine vertikale Beschränkung (30 mm) und eine Winkelbeschränkung (75°) wurden zur Definition des Profils festgelegt; ein Bezugsmaß wurde auf dem schrägen Liniensegment hinzugefügt, um seine Länge (31,0583 mm) zu erfassen.*

## Anwendung

1.  Drücke die **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Umschalten treibende Beschränkung](Sketcher_ToggleDrivingConstraint.md)** Taste. Die Symbole für Maßbeschränkungen in der Skizzierer Beschränkungswerkzeugleiste wechseln von rot nach blau.
2.  Die übliche Methode zum Erstellen von Maßbeschränkungen funktioniert genauso, aber stattdessen wird eine blaue Referenzabmessung hinzugefügt.
3.  Um die Skizzierer Beschränkungswerkzeugleiste wieder in den Beschränkungsmodus (rot) zu versetzen, drücke erneut die Schaltfläche Beschränkung umschalten.
4.  Um eine Maßbeschränkung in eine Bezugsbemaßung oder umgekehrt zu verwandeln, wähle sie aus und drücke die Taste Beschränkung Umschalten.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/de
