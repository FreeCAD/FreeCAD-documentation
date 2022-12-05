---
- GuiCommand:/de
   Name:Sketcher ToggleDrivingConstraint
   Name/de:Sketcher UmschalterFührendeRandbedingung
   MenuLocation:Sketch → Skizzen-Beschränkungen → Einschränkung zwischen festlegend und anzeigend umschalten
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**K** **X**
   Version:0.16
   SeeAlso:[Sketcher UmschalterKonstruktion](Sketcher_ToggleConstruction/de.md)
---

# Sketcher ToggleDrivingConstraint/de

## Beschreibung

Das Werkzeug **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [UmschalterFührendeRandbedingung](Sketcher_ToggleDrivingConstraint/de.md)** wandelt maßliche Randbedingungen (Sperren, X-, Y-Abstand, Länge, Radius und Winkel) in den Referenzmodus und zurück. Die Symbole in der Werkzeugleiste färben sich blau, und anstelle von Maßbedingungen (führende bzw. festlegende Randbedingungen) werden Referenzmaße (anzeigende Randbedingungen) erstellt. Referenzmaße legen keine Freiheitsgrade in der Skizze fest. Es kann nützlich sein, in einer Skizze Referenzmaße zu erstellen, um die Bemaßung zu überprüfen; wenn ein Name angegeben wird, können sie auch dazu verwendet werden, die Randbedingung in einer anderen Skizze durch [Ausdrücke](Expressions/de.md) zu steuern.

![](images/Sketcher_Constraint_Toolbar_ReferenceMode.png ) 
*Die Werkzeugleiste Skizzen-Beschränkungen mit den maßlichen Randbedingungen im Referenzmaßmodus (blau).*

![](images/Sketcher_ToggleConstraint_example.png ) 
*Eine horizontale Abstandsbeschränkung (50 mm), eine vertikale Beschränkung (30 mm) und eine Winkelbeschränkung (75°) wurden zur Definition des Profils festgelegt; ein Bezugsmaß wurde auf dem schrägen Liniensegment hinzugefügt, um seine Länge (31,0583 mm) zu erfassen.*

## Anwendung

1.  Die Schaltfläche **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Einschränkung zwischen festlegend und anzeigend umschalten](Sketcher_ToggleDrivingConstraint.md)** drücken. Die Symbole für Maßbedingungen in der Werkzeugleiste Skizzen-Beschränkungen wechseln von rot nach blau.
2.  Die übliche Methode zum Erstellen von Maßbedingungen funktioniert auch hier, fügt aber jetzt blaue Referenzmaße hinzu.
3.  Um die Werkzeugleiste Skizzen-Beschränkungen wieder in den festlegenden Modus (rot) zu versetzen, drückt man die Schaltfläche **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Einschränkung zwischen festlegend und anzeigend umschalten](Sketcher_ToggleDrivingConstraint.md)** erneut.
4.  Um eine Maßbedingung in ein Referenzmaß oder umgekehrt zu verwandeln, wählt man sie aus und drückt die Schaltfläche **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Einschränkung zwischen festlegend und anzeigend umschalten](Sketcher_ToggleDrivingConstraint.md)**.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/de
