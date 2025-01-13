---
 GuiCommand:
   Name: Sketcher ToggleDrivingConstraint
   Name/de: Sketcher FestlegendeRandbedingungUmschalten
   MenuLocation: Sketch , Sketcher-Randbedingungen , Randbedingung zwischen festlegend und anzeigend umschalten
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **X**
   Version: 0.16
   SeeAlso: Sketcher_ToggleActiveConstraint/de
---

# Sketcher ToggleDrivingConstraint/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:24px;"> [Sketcher FestlegendeRandbedingungUmschalten](Sketcher_ToggleDrivingConstraint/de.md) schaltet entweder den Modus der Werkzeuge zur Erstellung von [maßlichen Randbedingungen](Sketcher_Workbench/de#Sketcher_CompDimensionTools.md) auf festlegend bzw. anzeigend um oder wechselt den Modus ausgewählter Randbedingungen entsprechend.

Im Gegensatz zu festlegenden Randbedingungen tragen anzeigende Randbedingungen nicht zur Bestimmtheit der Skizze bei; ihr Wert hängt von anderen Randbedingungen ab, sie sind \"fremdgesteuert\". Sie können nützlich sein, um Maße zu prüfen. Sie können in [Ausdrücken](Expressions/de.md) eingesetzt werden, nur nicht in der Skizze selbst.

![](images/Sketcher_ToggleConstraint_example.png ) 
*Festlegende maßliche Randbedingungen (rot) für den horizontalen Abstand (50 mm), den vertikalen Abstand (30 mm) und den Winkel (75°) wurden zur Definition des Profils eingesetzt; auf dem schrägen Liniensegment wurde eine anzeigende Randbedingung hinzugefügt, um seine Länge (31,0583 mm) zu erfassen.*



## Anwendung



### Werkzeuge umschalten 

1.  Sicherstellen, dass keine maßlichen Randbedingungen ausgewählt sind.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> [Randbedingung zwischen festlegend und anzeigend umschalten](Sketcher_ToggleDrivingConstraint/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Randbedingung zwischen festlegend und anzeigend umschalten** auswählen.
    -   Das Tastaturkürzel **K** dann **X**.
3.  Der Modus der Werkzeuge zur Erstellung maßlicher Randbedingungen wird umgeschaltet:
    -   Im festlegenden Modus sind ihre Menü- und Werkzeugleistensymbole rot und sie erstellen festlegende Randbedingungen ([Standardfarbe](Sketcher_Preferences/de#Darstellung.md) Rot). Das Symbol dieses Werkzeugs ist dann: <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:16px;">.
    -   Im anzeigenden Modus sind ihre Menü- und Werkzeugleistensymbole blau und sie erstellen anzeigende Randbedingungen (Standardfarbe Blau). Das Symbol dieses Werkzeugs ist dann: <img alt="" src=images/Sketcher_ToggleConstraint_Driven.svg  style="width:16px;">.



### Randbedingungen umschalten 

1.  Eine oder mehrere maßliche Randbedingungen auswählen.
2.  Das Werkzeug wie oben beschrieben aufrufen oder mit einer der folgenden zusätzlichen Möglichkeiten:
    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view.md) und die Menüoption **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Randbedingung zwischen festlegend und anzeigend umschalten** im Kontextmenü auswählen.

    -   Ein Rechtsklick in den Abschnitt **Randbedingungen** des [Sketcher-Dialogs](Sketcher_Dialog/de.md) und die Menüoption **Randbedingung zwischen festlegend und anzeigend umschalten** im Kontextmenü auswählen.
3.  Die ausgewählten Randbedingungen wechseln von festlegend auf anzeigend oder umgekehrt. Ihre Darstellung passt sich entsprechend an.
4.  Der Modus der Werkzeuge zur Erstellung maßlicher Randbedingungen ändert sich nicht.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/de
