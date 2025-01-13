---
 GuiCommand:
   Name: Sketcher ConstrainRadius
   Name/de: Sketcher RadiusFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Radius festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **R**
   SeeAlso: Sketcher_ConstrainRadiam/de, Sketcher_ConstrainDiameter/de
---

# Sketcher ConstrainRadius/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> [Sketcher RadiusFestlegen](Sketcher_ConstrainRadius/de.md) legt den Radius von Kreisen, Bögen und [B-Spline-Gewichtskreisen](Sketcher_CreateBSpline/de#Hinweise.md) fest.

![](images/Sketcher_ConstrainRadius_example.png )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Werkzeuge für Maßeinträge** auf {{Value|Einzelnes Werkzeug}} gesetzt (Standardeinstellung): Den Abwärtspfeil rechts neben der Schaltfläche **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und die Menüoption **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> Radius festlegen** im Ausklappmenü auswählen.

    -   Besitzt die Voreinstellung einen anderen Wert (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> [Radius festlegen](Sketcher_ConstrainRadius/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Radius festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Abmessung → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Radius festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **K** dann **R**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Für weitere Schritte siehe [Sketcher Radiam festlegen](Sketcher_ConstrainRadiam/de#Continue_mode.md).



### Einmal-Ausführen-Modus 

Siehe [Sketcher RadiamFestlegen](Sketcher_ConstrainRadiam/de#Einmal-Ausführen-Modus.md).



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Die Seite [Sketcher Skripten](Sketcher_scripting.md) erklärt die Werte, die für `ArcOrCircle` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/de
